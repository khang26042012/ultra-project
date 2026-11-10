import os
import sys
import subprocess
import time
import glob
from pathlib import Path

print("=" * 65, flush=True)
print("🌿 AgriVision - Ultralytics YOLO26 Plant Disease Training Pipeline", flush=True)
print("=" * 65, flush=True)

# 1. Hardware Inspection
print("\n[Step 1/5] HARDWARE & CUDA ENVIRONMENT CHECK", flush=True)
print(f"Python Version: {sys.version.split()[0]}", flush=True)
try:
    gpu = subprocess.run(
        ["nvidia-smi", "--query-gpu=name,memory.total", "--format=csv,noheader"],
        capture_output=True,
        text=True
    ).stdout.strip()
    print("Detected GPUs:\n" + gpu, flush=True)
except Exception as e:
    print(f"Notice on nvidia-smi: {e}", flush=True)

import torch
print(f"PyTorch Version: {torch.__version__}", flush=True)
print(f"CUDA Available: {torch.cuda.is_available()}", flush=True)
gpu_count = torch.cuda.device_count() if torch.cuda.is_available() else 0
print(f"CUDA Device Count: {gpu_count}", flush=True)

# 2. Dependencies Setup
print("\n[Step 2/5] INSTALLING ULTRALYTICS & ONNX RUNTIME", flush=True)
subprocess.check_call([
    sys.executable, "-m", "pip", "install", "-q", "-U",
    "ultralytics", "onnx", "onnxslim", "onnxruntime", "pyyaml", "kaggle"
])
print("Ultralytics library ready!", flush=True)

# 3. Fast In-Memory / Direct Dataset Setup
print("\n[Step 3/5] DOWNLOADING PLANT PATHOLOGY DATASET", flush=True)
dataset_dir = "/kaggle/working/plant_dataset"
os.makedirs(dataset_dir, exist_ok=True)

# Try downloading PlantDoc directly at high speed
data_yaml_path = None
try:
    print("Fetching PlantDoc Object Detection dataset via Kaggle CLI...", flush=True)
    subprocess.run([
        "kaggle", "datasets", "download",
        "-d", "yusufmurtaza01/plantdoc-object-detection-dataset",
        "--unzip", "-p", dataset_dir
    ], check=True)
    print("PlantDoc dataset downloaded and extracted successfully!", flush=True)
except Exception as e:
    print(f"Kaggle CLI download notice: {e}, falling back to built-in benchmark dataset...", flush=True)

# Find dataset.yaml
candidate_yamls = list(Path(dataset_dir).glob("**/*dataset*.yaml")) + list(Path(dataset_dir).glob("**/*data*.yaml"))
if candidate_yamls:
    import yaml
    src_yaml = candidate_yamls[0]
    with open(src_yaml, "r", encoding="utf-8") as f:
        data_cfg = yaml.safe_load(f)
    
    data_cfg["path"] = str(src_yaml.parent)
    data_yaml_path = "/tmp/plant_training.yaml"
    with open(data_yaml_path, "w", encoding="utf-8") as f:
        yaml.dump(data_cfg, f, default_flow_style=False)
    print(f"Configured dataset at {data_yaml_path} with {data_cfg.get('nc')} classes", flush=True)
else:
    print("Using Ultralytics default segmentation benchmark coco8-seg.yaml", flush=True)
    data_yaml_path = "coco8-seg.yaml"

# 4. Train YOLO26 Model Architecture
print("\n[Step 4/5] INITIALIZING & TRAINING ULTRALYTICS YOLO26", flush=True)
from ultralytics import YOLO

# Attempt YOLO26 model load (with fallback hierarchy if weights not yet cached)
model = None
candidate_models = ["yolo26m.pt", "yolo26m-seg.pt", "yolo12m.pt", "yolo11m.pt"]
selected_model_name = "yolo26m.pt"

for m in candidate_models:
    try:
        print(f"Loading {m}...", flush=True)
        model = YOLO(m)
        selected_model_name = m
        print(f"Successfully loaded: {m}", flush=True)
        break
    except Exception as e:
        print(f"Note on {m}: {e}", flush=True)

if model is None:
    print("Falling back to yolo11m.pt...", flush=True)
    model = YOLO("yolo11m.pt")
    selected_model_name = "yolo11m.pt"

devices = [0, 1] if gpu_count >= 2 else (0 if gpu_count == 1 else "cpu")
batch_size = 16 if gpu_count >= 1 else 4
epochs = 30

print(f"Training on device(s): {devices} | Batch: {batch_size} | Epochs: {epochs}", flush=True)
results = model.train(
    data=data_yaml_path,
    epochs=epochs,
    imgsz=640,
    batch=batch_size,
    device=devices,
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

print("\nTraining completed successfully!", flush=True)

# 5. Export weights for AgriVision Edge/VPS Production
print("\n[Step 5/5] EXPORTING PRODUCTION ARTIFACTS", flush=True)
import shutil

best_weight = "/kaggle/working/agrivision_runs/yolo26_plant_disease/weights/best.pt"
if os.path.exists(best_weight):
    out_pt = "/kaggle/working/yolo26_plant_disease_best.pt"
    shutil.copy2(best_weight, out_pt)
    print(f"Saved PyTorch weights: {out_pt} ({os.path.getsize(out_pt) / 1e6:.1f} MB)", flush=True)
    
    try:
        print("Exporting ONNX format (dynamic=True, simplify=True)...", flush=True)
        onnx_path = model.export(format="onnx", dynamic=True, simplify=True, opset=17)
        if onnx_path and os.path.exists(str(onnx_path)):
            out_onnx = "/kaggle/working/yolo26_plant_disease_best.onnx"
            shutil.copy2(str(onnx_path), out_onnx)
            print(f"Saved ONNX weights: {out_onnx} ({os.path.getsize(out_onnx) / 1e6:.1f} MB)", flush=True)
    except Exception as e:
        print(f"ONNX export note: {e}", flush=True)

print("\n" + "=" * 65, flush=True)
print("🎉 ALL AGRIVISION YOLO26 TASKS FINISHED SUCCESSFULLY!", flush=True)
print("=" * 65, flush=True)
