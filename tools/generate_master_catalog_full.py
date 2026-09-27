# -*- coding: utf-8 -*-
"""
Master Catalog Full Generator for AgriVision 1,000 Crops
Author: Phan Trọng Khang (Lớp 91, THCS Vĩnh An, Vĩnh Long)
Generates 580+ distinct authentic Vietnamese crops and merges worker modules.
"""
import os
import sys

tools_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(tools_dir)
catalog_file = os.path.join(tools_dir, "master_crop_catalog.py")

print("Building Master Crop Catalog...")
