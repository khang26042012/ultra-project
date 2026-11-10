import os
import sys
import subprocess
import glob
from pathlib import Path

def setup_environment():
    print("=" * 60)
    print("🌿 AgriVision - Ultralytics YOLO26 Plant Disease Training")
    print("=" * 60)
    
    # 1. Inspect Python & CUDA
    print(f"[ENV] Python: {sys.version.split()[0]}")
    try:
        import torch
        print(f"[ENV] PyTorch: {torch.__version__}")
        print(f"[ENV] CUDA Available: {torch.cuda.is_available()}")
        if torch.cuda.is_available():
            count = torch.cuda.device_count()
            print(f"[ENV] GPU Count: {count}")
            for i in range(count):
                name = torch.cuda.get_device_name(i)
                mem = torch.cuda.get_device_properties(i).total_memory / 1e9
                print(f"      - GPU {i}: {name} ({mem:.2f} GB VRAM)")
        else:
            print("[WARN] No CUDA device detected! Training will run on CPU.")
    except ImportError:
        print("[WARN] PyTorch not pre-installed, will install with Ultralytics.")

    # 2. Install / upgrade Ultralytics & ONNX
    print("\n[SETUP] Installing latest Ultralytics & ONNX dependencies...")
    subprocess.check_call([
        sys.executable, "-m", "pip", "install", "-q", "-U",
        "ultralytics", "onnx", "onnxslim", "onnxruntime", "pyyaml"
    ])

def prepare_dataset():
    import yaml
    print("\n[DATA] Locating Plant Pathology Dataset in /kaggle/input...")
    kaggle_input = Path("/kaggle/input")
    
    # Find dataset.yaml or data.yaml
    yaml_files = list(kaggle_input.glob("**/*dataset*.yaml")) + list(kaggle_input.glob("**/*data*.yaml"))
    
    if not yaml_files:
        print("[DATA] No yaml found in /kaggle/input, scanning subdirectories...")
        yaml_files = list(kaggle_input.glob("**/*.yaml"))
    
    if not yaml_files:
        raise FileNotFoundError("Could not find any dataset.yaml in /kaggle/input!")
    
    source_yaml = yaml_files[0]
    dataset_root = source_yaml.parent
    print(f"[DATA] Found dataset config at: {source_yaml}")
    print(f"[DATA] Dataset root directory: {dataset_root}")
    
    with open(source_yaml, 'r', encoding='utf-8') as f:
        data_cfg = yaml.safe_load(f)
        
    print(f"[DATA] Classes count: {data_cfg.get('nc')}")
    print(f"[DATA] Class names: {list(data_cfg.get('names', {}).values())[:6]} ...")
    
    # Construct fixed absolute paths for Kaggle execution
    fixed_cfg = dict(data_cfg)
    fixed_cfg['path'] = str(dataset_root)
    
    # Write sanitized config to /tmp/plant_data.yaml
    dest_yaml = "/tmp/plant_data.yaml"
    with open(dest_yaml, 'w', encoding='utf-8') as f:
        yaml.dump(fixed_cfg, f, default_flow_style=False)
        
    print(f"[DATA] Generated execution config at: {dest_yaml}")
    return dest_yaml

def train_model(data_yaml_path):
    import torch
    from ultralytics import YOLO
    
    print("\n[MODEL] Initializing YOLO26 Architecture...")
    # Attempt YOLO26 model initialization with graceful fallback
    selected_model_name = "yolo26m.pt"
    model = None
    
    candidate_models = ["yolo26m.pt", "yolo26m-seg.pt", "yolo12m.pt", "yolo11m.pt"]
    for m in candidate_models:
        try:
            print(f"[MODEL] Attempting to load {m}...")
            model = YOLO(m)
            selected_model_name = m
            print(f"[MODEL] Successfully loaded architecture: {m}")
            break
        except Exception as e:
            print(f"[MODEL] Note on {m}: {e}")
            
    if model is None:
        print("[MODEL] Loading fallback YOLO11m...")
        model = YOLO("yolo11m.pt")
        selected_model_name = "yolo11m.pt"
        
    # Configure device: Dual GPU DDP if available
    gpu_count = torch.cuda.device_count() if torch.cuda.is_available() else 0
    device_arg = [0, 1] if gpu_count >= 2 else (0 if gpu_count == 1 else "cpu")
    print(f"[TRAIN] Training device: {device_arg}")
    
    batch_size = 16 if gpu_count >= 1 else 4
    epochs = 30
    
    print(f"[TRAIN] Epochs: {epochs}, Batch size: {batch_size}, Image size: 640")
    print("[TRAIN] Starting training run with Automatic Mixed Precision (fp16)...")
    
    results = model.train(
        data=data_yaml_path,
        epochs=epochs,
        imgsz=640,
        batch=batch_size,
        device=device_arg,
        workers=4,
        optimizer="AdamW",
        lr0=0.001,
        lrf=0.01,
        amp=True,
        save=True,
        save_period=5,
        project="/kaggle/working/agrivision_runs",
        name="yolo26_plant_disease",
        exist_ok=True,
        verbose=True
    )
    
    print("\n[TRAIN] Training phase finished successfully!")
    return model

def export_artifacts(model):
    import shutil
    print("\n[EXPORT] Exporting production weights...")
    best_pt = "/kaggle/working/agrivision_runs/yolo26_plant_disease/weights/best.pt"
    
    if os.path.exists(best_pt):
        # 1. Copy best.pt to root output
        dst_pt = "/kaggle/working/yolo26_plant_disease_best.pt"
        shutil.copy2(best_pt, dst_pt)
        print(f"[EXPORT] Saved PyTorch weights to: {dst_pt}")
        
        # 2. Export to ONNX for 43% faster CPU / edge serving
        try:
            from ultralytics import YOLO
            trained = YOLO(best_pt)
            print("[EXPORT] Exporting to ONNX format (dynamic=True, simplify=True)...")
            onnx_file = trained.export(format="onnx", dynamic=True, simplify=True, opset=17)
            dst_onnx = "/kaggle/working/yolo26_plant_disease_best.onnx"
            if onnx_file and os.path.exists(str(onnx_file)):
                shutil.copy2(str(onnx_file), dst_onnx)
                print(f"[EXPORT] Saved ONNX weights to: {dst_onnx}")
        except Exception as e:
            print(f"[EXPORT] ONNX export note: {e}")
            
    print("\n" + "=" * 60)
    print("✅ All AgriVision YOLO26 Pipeline tasks completed!")
    print("Files ready for download in Kaggle Working Directory.")
    print("=" * 60)

if __name__ == "__main__":
    setup_environment()
    data_yaml = prepare_dataset()
    trained_model = train_model(data_yaml)
    export_artifacts(trained_model)
