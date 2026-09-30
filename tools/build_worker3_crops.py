# -*- coding: utf-8 -*-
"""
Builder script for Worker Subagent 3:
High-Value Imported and High-Tech Crops in Vietnam
Merges part1 and part2, validates schema, and writes to both target paths.
"""

import json
import os
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

from worker3_data_part1 import CROPS_PART1
from worker3_data_part2 import CROPS_PART2

def validate_and_build():
    all_crops = CROPS_PART1 + CROPS_PART2
    print(f"Total crops loaded: {len(all_crops)}")

    required_crop_keys = ['id', 'topic', 'name_vi', 'scientific_name', 'dia_ban_pho_bien', 'dac_tinh_sinh_thai', 'danh_sach_benh']
    allowed_topics = {'Cay_Nhap_Khau_Kinh_Te_Cao', 'Rau_Cu_Gia_Vi_Va_Nam', 'Cay_An_Trai_Nhiet_Doi_Va_On_Doi'}
    required_disease_keys = ['ten_benh', 'muc_do_nguy_hiem', 'tac_nhan', 'trieu_chung_dien_hinh', 'phan_biet_chan_doan_kep', 'kiem_tra_thuc_dia', 'phac_do_vietgap']

    errors = []
    total_diseases = 0

    for idx, crop in enumerate(all_crops):
        crop_id = crop.get('id', f'crop_{idx}')
        name_vi = crop.get('name_vi', 'Unknown')

        for key in required_crop_keys:
            if key not in crop or not crop[key]:
                errors.append(f"Crop {crop_id} ({name_vi}) missing required field: {key}")

        topic = crop.get('topic')
        if topic not in allowed_topics:
            errors.append(f"Crop {crop_id} invalid topic: {topic}")

        diseases = crop.get('danh_sach_benh', [])
        if len(diseases) < 2:
            errors.append(f"Crop {crop_id} has less than 2 diseases ({len(diseases)})")

        total_diseases += len(diseases)

        for d_idx, d in enumerate(diseases):
            d_name = d.get('ten_benh', f'Disease_{d_idx}')
            for d_key in required_disease_keys:
                if d_key not in d or not d[d_key]:
                    errors.append(f"Crop {crop_id} disease '{d_name}' missing field: {d_key}")

            tac_nhan = d.get('tac_nhan', {})
            if not tac_nhan.get('loai') or not tac_nhan.get('ten_khoa_hoc'):
                errors.append(f"Crop {crop_id} disease '{d_name}' incomplete tac_nhan: {tac_nhan}")

            phac_do = d.get('phac_do_vietgap', {})
            if not phac_do.get('canh_tac') or not phac_do.get('sinh_hoc'):
                errors.append(f"Crop {crop_id} disease '{d_name}' incomplete phac_do_vietgap: {phac_do}")

    if errors:
        print(f"Validation FAILED with {len(errors)} errors:")
        for err in errors[:10]:
            print(" -", err)
        sys.exit(1)

    print(f"Validation PASSED! 100% compliant with standard schema.")
    print(f"Total Crops: {len(all_crops)}")
    print(f"Total Diseases: {total_diseases} (Average {total_diseases/len(all_crops):.1f} diseases/crop)")

    # Target file paths
    # 1. Root workspace: src/data/worker3_crops.json
    # 2. ultra-project: ultra-project/src/data/worker3_crops.json
    workspace_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    ultra_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    target1 = os.path.join(workspace_root, "src", "data", "worker3_crops.json")
    target2 = os.path.join(ultra_root, "src", "data", "worker3_crops.json")

    for target_path in [target1, target2]:
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        with open(target_path, 'w', encoding='utf-8') as f:
            json.dump(all_crops, f, ensure_ascii=False, indent=2)
        print(f"Successfully saved {len(all_crops)} crops to: {target_path} (Size: {os.path.getsize(target_path):,} bytes)")

    print("\nSummary List of Collected Crops:")
    for i, c in enumerate(all_crops, 1):
        d_count = len(c['danh_sach_benh'])
        print(f"{i:2d}. [{c['id']}] {c['name_vi']} ({c['scientific_name']}) - {c['topic']} - {d_count} bệnh")

if __name__ == "__main__":
    validate_and_build()
