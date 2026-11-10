#!/usr/bin/env python3
"""
AgriVision - Automated YOLO26 Kaggle GPU Training Pipeline
Author: Khang Phan Trọng / AgriVision Team
Automates training of Ultralytics YOLO26 on Kaggle Dual NVIDIA T4 GPUs.
"""

import os
import sys
import json
import time

KAGGLE_TOKEN = os.environ.get("KAGGLE_API_TOKEN", "KGAT_f1840d4f7d83003270cc33868d8d9739")
os.environ["KAGGLE_API_TOKEN"] = KAGGLE_TOKEN

def main():
    print("=" * 60)
    print("  AgriVision - Ultralytics YOLO26 Kaggle Training Pipeline")
    print("=" * 60)
    
    try:
        from kaggle.api.kaggle_api_extended import KaggleApi
    except ImportError:
        print("Installing kaggle sdk...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "kaggle", "six"])
        from kaggle.api.kaggle_api_extended import KaggleApi

    api = KaggleApi()
    api.authenticate()
    print("Authenticated with Kaggle as:", api.config_values.get("username", "khangphantrng"))
    
    kernel_slug = "khangphantrng/agrivision-yolo26-plant-disease-training"
    status_info = api.kernels_status(kernel_slug)
    print(f"\nKernel status on Kaggle: {status_info.get('status')}")
    print(f"Direct URL: https://www.kaggle.com/code/{kernel_slug}")
    
    if status_info.get("failureMessage"):
        print("Failure details:", status_info["failureMessage"])
    else:
        print("\nGPU Training is currently active or queued.")
        print("Dual NVIDIA T4 GPUs (32GB VRAM total) are allocated.")
        print("Upon completion, weights ('best.pt', 'best.onnx') will be saved in /kaggle/working/.")

if __name__ == "__main__":
    main()
