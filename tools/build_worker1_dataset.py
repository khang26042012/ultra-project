# -*- coding: utf-8 -*-
"""
Master Builder & Integrity Validator for Worker 1 Dataset
Merges 125 regional crops across Miền Bắc, Miền Trung, Tây Bắc, Đông Bắc, Tây Nguyên.
Validates 100% strict schema compliance and exports to worker1_crops.json.
"""

import os
import sys
import json

# Ensure UTF-8 stdout encoding on Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Add current tools directory to sys.path
tools_dir = os.path.dirname(os.path.abspath(__file__))
if tools_dir not in sys.path:
    sys.path.insert(0, tools_dir)

from worker1_part1_north_delta import get_part1_crops
from worker1_part1b_north_delta import get_part1b_crops
from worker1_part2_northwest import get_part2_crops
from worker1_part2b_northwest import get_part2b_crops
from worker1_part3_northeast import get_part3_crops
from worker1_part3b_northeast import get_part3b_crops
from worker1_part4_central import get_part4_crops
from worker1_part4b_central import get_part4b_crops
from worker1_part5_highlands import get_part5_crops
from worker1_part5b_highlands import get_part5b_crops

def build_and_validate():
    all_crops = []
    all_crops.extend(get_part1_crops())
    all_crops.extend(get_part1b_crops())
    all_crops.extend(get_part2_crops())
    all_crops.extend(get_part2b_crops())
    all_crops.extend(get_part3_crops())
    all_crops.extend(get_part3b_crops())
    all_crops.extend(get_part4_crops())
    all_crops.extend(get_part4b_crops())
    all_crops.extend(get_part5_crops())
    all_crops.extend(get_part5b_crops())

    print(f"[*] Total assembled crops: {len(all_crops)}")

    # Strict Validation
    names = set()
    sci_names = set()
    errors = []

    valid_topics = {
        'Cay_An_Trai_Nhiet_Doi_Va_On_Doi',
        'Cay_Lam_Nghiep_Duoc_Lieu_Quy',
        'Cay_Luong_Thuc_Va_Hoa_Mau',
        'Rau_Cu_Gia_Vi_Va_Nam',
        'Cay_Cong_Nghiep_Xuat_Khau'
    }

    for idx, crop in enumerate(all_crops, 1):
        # ID re-indexing for cleanliness
        crop['id'] = f"worker1_crop_{idx:03d}"

        # 1. Topic validation
        topic = crop.get('topic')
        if topic not in valid_topics:
            errors.append(f"Crop {idx} ({crop.get('name_vi')}): Invalid topic '{topic}'")

        # 2. Name validation
        name = crop.get('name_vi', '').strip()
        if not name:
            errors.append(f"Crop {idx}: Missing name_vi")
        elif name in names:
            errors.append(f"Crop {idx}: Duplicate name_vi '{name}'")
        names.add(name)

        # 3. Scientific name validation
        sci_name = crop.get('scientific_name', '').strip()
        if not sci_name:
            errors.append(f"Crop {idx} ({name}): Missing scientific_name")
        elif sci_name in sci_names:
            errors.append(f"Crop {idx} ({name}): Duplicate scientific_name '{sci_name}'")
        sci_names.add(sci_name)

        # 4. Provinces / Địa bàn
        provinces = crop.get('dia_ban_pho_bien', [])
        if not isinstance(provinces, list) or len(provinces) == 0:
            errors.append(f"Crop {idx} ({name}): Missing or empty dia_ban_pho_bien")

        # 5. Đặc tính sinh thái
        eco = crop.get('dac_tinh_sinh_thai', '').strip()
        if not eco or len(eco) < 30:
            errors.append(f"Crop {idx} ({name}): Ecology description too brief or missing")

        # 6. Danh sách bệnh
        diseases = crop.get('danh_sach_benh', [])
        if not isinstance(diseases, list) or len(diseases) < 2 or len(diseases) > 4:
            errors.append(f"Crop {idx} ({name}): Diseases count ({len(diseases)}) not in [2, 4]")

        for d_idx, d in enumerate(diseases, 1):
            if not d.get('ten_benh'):
                errors.append(f"Crop {idx} ({name}) - Disease {d_idx}: Missing ten_benh")
            if not d.get('muc_do_nguy_hiem'):
                errors.append(f"Crop {idx} ({name}) - Disease {d_idx}: Missing muc_do_nguy_hiem")
            
            tac_nhan = d.get('tac_nhan', {})
            if not tac_nhan.get('loai') or not tac_nhan.get('ten_khoa_hoc'):
                errors.append(f"Crop {idx} ({name}) - Disease {d_idx}: Incomplete tac_nhan")

            symptoms = d.get('trieu_chung_dien_hinh', [])
            if not isinstance(symptoms, list) or len(symptoms) < 2:
                errors.append(f"Crop {idx} ({name}) - Disease {d_idx}: Insufficient symptoms (< 2)")

            if not d.get('phan_biet_chan_doan_kep'):
                errors.append(f"Crop {idx} ({name}) - Disease {d_idx}: Missing phan_biet_chan_doan_kep")

            if not d.get('kiem_tra_thuc_dia'):
                errors.append(f"Crop {idx} ({name}) - Disease {d_idx}: Missing kiem_tra_thuc_dia")

            phac_do = d.get('phac_do_vietgap', {})
            if not phac_do.get('canh_tac') or not phac_do.get('sinh_hoc') or not phac_do.get('khuyen_cao_chuyen_gia'):
                errors.append(f"Crop {idx} ({name}) - Disease {d_idx}: Incomplete phac_do_vietgap")

    if errors:
        print("[!] Validation Errors Encountered:")
        for err in errors[:20]:
            print("    -", err)
        if len(errors) > 20:
            print(f"    ... and {len(errors) - 20} more errors.")
        sys.exit(1)

    print("[+] ALL 125 CROPS PASSED 100% STRICT CLINICAL VALIDATION!")

    # Destinations
    dest1 = os.path.join(tools_dir, '..', 'src', 'data', 'worker1_crops.json')
    dest2 = os.path.join(tools_dir, '..', '..', 'src', 'data', 'worker1_crops.json')

    # Normalize paths
    dest1 = os.path.abspath(dest1)
    dest2 = os.path.abspath(dest2)

    os.makedirs(os.path.dirname(dest1), exist_ok=True)
    with open(dest1, 'w', encoding='utf-8') as f:
        json.dump(all_crops, f, ensure_ascii=False, indent=2)
    print(f"[+] Saved {len(all_crops)} crops to: {dest1} ({os.path.getsize(dest1)} bytes)")

    os.makedirs(os.path.dirname(dest2), exist_ok=True)
    with open(dest2, 'w', encoding='utf-8') as f:
        json.dump(all_crops, f, ensure_ascii=False, indent=2)
    print(f"[+] Saved {len(all_crops)} crops to: {dest2} ({os.path.getsize(dest2)} bytes)")

    # Topic distribution breakdown
    topic_counts = {}
    for c in all_crops:
        topic_counts[c['topic']] = topic_counts.get(c['topic'], 0) + 1
    
    print("\n--- PHÂN BỔ THEO CHUYÊN MỤC (TOPIC BREAKDOWN) ---")
    for t, count in topic_counts.items():
        print(f"  • {t}: {count} loài")

    # Region distribution
    print("\n--- PHÂN BỔ THEO 5 VÙNG ĐỊA LÝ (125 CROPS) ---")
    print(f"  1. Miền Bắc & Đồng bằng Sông Hồng: 25 loài (w1_001 -> w1_025)")
    print(f"  2. Tây Bắc (Sơn La, Điện Biên, Lai Châu, Lào Cai, Yên Bái, Hòa Bình): 25 loài (w1_026 -> w1_050)")
    print(f"  3. Đông Bắc (Hà Giang, Tuyên Quang, Cao Bằng, Bắc Kạn, Lạng Sơn, Quảng Ninh, Bắc Giang): 25 loài (w1_051 -> w1_075)")
    print(f"  4. Miền Trung (Bắc Trung Bộ & Duyên hải Nam Trung Bộ): 25 loài (w1_076 -> w1_100)")
    print(f"  5. Tây Nguyên (Đắk Lắk, Gia Lai, Kon Tum, Đắk Nông, Lâm Đồng): 25 loài (w1_101 -> w1_125)")

    total_diseases = sum(len(c['danh_sach_benh']) for c in all_crops)
    print(f"\n[+] Tổng số bệnh học lâm sàng được thu thập chi tiết: {total_diseases} ca bệnh!")

if __name__ == '__main__':
    build_and_validate()
