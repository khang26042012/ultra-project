# -*- coding: utf-8 -*-
"""
Auditor 4: Pathology Precision & Schema Compliance Engine
Validates JSON syntax, schema compliance, field types, and plant pathology accuracy.
"""

import json
import os
import re
import sys
import unicodedata
from typing import Dict, List, Any, Tuple

try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

# Comprehensive Plant Pathology Taxonomy Database for Validation & Autofix
BACTERIAL_GENERA = {
    'xanthomonas', 'ralstonia', 'pseudomonas', 'erwinia', 'pectobacterium',
    'dickeya', 'candidatus liberibacter', 'clavibacter', 'streptomyces',
    'acidovorax', 'agrobacterium', 'rhizobium', 'burkholderia', 'pantoea',
    'curtobacterium', 'spiroplasma', 'xylella', 'bacillus'
}

FUNGAL_GENERA = {
    'phytophthora', 'pythium', 'fusarium', 'colletotrichum', 'rhizoctonia',
    'pyricularia', 'magnaporthe', 'cercospora', 'lasiodiplodia', 'curvularia',
    'phomopsis', 'diaporthe', 'oidium', 'podosphaera', 'erysiphe', 'leveillula',
    'pseudoperonospora', 'peronospora', 'bremia', 'plasmopara', 'sclerotium',
    'athelia', 'sclerotinia', 'botrytis', 'alternaria', 'exserohilum',
    'bipolaris', 'helminthosporium', 'stagonosporopsis', 'didymella', 'puccinia',
    'uromyces', 'hemileia', 'ustilago', 'sphacelotheca', 'tilletia',
    'macrophomina', 'pestalotiopsis', 'neopestalotiopsis', 'verticillium',
    'armillaria', 'ganoderma', 'corticium', 'ceratocystis', 'thielaviopsis',
    'septoria', 'cladosporium', 'gloeosporium', 'elsinoe', 'elsinoë', 'capnodium',
    'meliola', 'marasmius', 'rigidoporus', 'aspergillus', 'penicillium',
    'chaetomium', 'monilinia', 'venturia', 'guignardia', 'phyllosticta',
    'mycosphaerella', 'corynespora', 'rhizopus', 'choanephora'
}

NEMATODE_GENERA = {
    'meloidogyne', 'pratylenchus', 'radopholus', 'ditylenchus', 'rotylenchulus',
    'aphelenchoides', 'tylenchulus', 'helicotylenchus', 'xiphinema',
    'bursaphelenchus', 'belonolaimus', 'heterodera', 'globodera', 'longidorus'
}

VIRUS_KEYWORDS = {
    'virus', 'mosaic', 'ringspot', 'leaf curl', 'bunchy top', 'tristeza',
    'tungro', 'streak', 'spotted wilt', 'yellow dwarf', 'yellow vein',
    'tmv', 'cmv', 'bbtv', 'tylcv', 'ctv', 'prsv', 'pvy', 'pvx', 'bcmv', 'rsv'
}

STANDARD_TOPICS = {
    'Cay_An_Trai_Dac_San',
    'Cay_Luong_Thuc_Va_Hoa_Mau',
    'Cay_Luong_Thuc_Mau',
    'Rau_An_La_An_Qua',
    'Rau_Cu_Gia_Vi_Va_Nam',
    'Cay_Cong_Nghiep_Xuat_Khau',
    'Cay_Cong_Nghiep_Duoc_Lieu',
    'Cay_An_Trai_Nhiet_Doi_Va_On_Doi',
    'Cay_Lam_Nghiep_Duoc_Lieu_Quy'
}

def normalize_str(s: str) -> str:
    if not s:
        return ""
    s_norm = unicodedata.normalize('NFD', s.strip().lower())
    s_norm = "".join(c for c in s_norm if unicodedata.category(c) != 'Mn')
    s_norm = re.sub(r'[^a-z0-9\s]', ' ', s_norm)
    return re.sub(r'\s+', ' ', s_norm).strip()

def check_pathogen_classification(loai: str, ten_khoa_hoc: str) -> Tuple[bool, str, str]:
    """
    Returns (is_correct, detected_correct_loai, reason)
    """
    sci_lower = ten_khoa_hoc.lower().strip()
    loai_lower = loai.lower().strip()
    
    # Handle composite pathogens (Phức hợp / Tổ hợp)
    if 'tổ hợp' in loai_lower or 'phức hợp' in loai_lower or 'hỗn hợp' in loai_lower or 'composite' in loai_lower:
        return True, loai, "Correct (Phức hợp tác nhân)"

    # Check virus
    for v in VIRUS_KEYWORDS:
        if v in sci_lower:
            if 'virus' in loai_lower or 'vi rút' in loai_lower:
                return True, "Virus", "Correct"
            return False, "Virus", f"Tên khoa học '{ten_khoa_hoc}' là Virus nhưng phân loại là '{loai}'"
            
    # Check bacteria
    for b in BACTERIAL_GENERA:
        if sci_lower.startswith(b) or f" {b}" in sci_lower:
            if 'khuẩn' in loai_lower or 'bacteria' in loai_lower:
                return True, "Vi khuẩn", "Correct"
            return False, "Vi khuẩn", f"Tên khoa học '{ten_khoa_hoc}' thuộc chi vi khuẩn '{b}' nhưng phân loại là '{loai}'"
            
    # Check fungus
    for f in FUNGAL_GENERA:
        if sci_lower.startswith(f) or f" {f}" in sci_lower:
            if 'nấm' in loai_lower or 'fungi' in loai_lower or 'oomycete' in loai_lower:
                return True, "Nấm", "Correct"
            return False, "Nấm", f"Tên khoa học '{ten_khoa_hoc}' thuộc chi nấm '{f}' nhưng phân loại là '{loai}'"
            
    # Check nematode
    for n in NEMATODE_GENERA:
        if sci_lower.startswith(n) or f" {n}" in sci_lower:
            if 'tuyến trùng' in loai_lower or 'nematode' in loai_lower:
                return True, "Tuyến trùng", "Correct"
            return False, "Tuyến trùng", f"Tên khoa học '{ten_khoa_hoc}' thuộc chi tuyến trùng '{n}' nhưng phân loại là '{loai}'"

    return True, loai, "Unknown or Other"

def audit_crop_dataset(file_path: str, autofix: bool = False) -> Dict[str, Any]:
    report = {
        "file": file_path,
        "valid_json": False,
        "total_crops": 0,
        "total_diseases": 0,
        "errors": [],
        "warnings": [],
        "fixes_applied": [],
        "duplicate_ids": [],
        "duplicate_names": [],
        "duplicate_sci_names": [],
        "disease_count_violations": [],
        "missing_fields": [],
        "pathology_mismatches": [],
        "schema_pass": False
    }

    if not os.path.exists(file_path):
        report["errors"].append(f"Tệp không tồn tại: {file_path}")
        return report

    # 1. JSON Syntax Check
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_content = f.read()
        crops = json.loads(raw_content)
        report["valid_json"] = True
    except Exception as e:
        report["errors"].append(f"Lỗi cú pháp JSON (JSON.parse failed): {str(e)}")
        return report

    if not isinstance(crops, list):
        report["errors"].append(f"Dữ liệu gốc phải là mảng JSON (Array), nhận được: {type(crops).__name__}")
        return report

    report["total_crops"] = len(crops)
    seen_ids = set()
    seen_names = {}
    seen_sci_names = {}
    
    modified = False

    for idx, crop in enumerate(crops):
        crop_err_prefix = f"Cây [{idx}] (ID: {crop.get('id', 'N/A')}, Tên: {crop.get('name_vi', 'N/A')}):"
        
        # Check required fields
        req_crop_fields = ['id', 'topic', 'name_vi', 'scientific_name', 'dia_ban_pho_bien', 'dac_tinh_sinh_thai', 'danh_sach_benh']
        for field in req_crop_fields:
            if field not in crop or crop[field] is None:
                err = f"{crop_err_prefix} Thiếu trường bắt buộc '{field}'"
                report["errors"].append(err)
                report["missing_fields"].append(err)
                if autofix:
                    if field == 'topic':
                        crop['topic'] = 'Cay_An_Trai_Nhiet_Doi_Va_On_Doi'
                        report["fixes_applied"].append(f"Thêm topic mặc định cho {crop.get('name_vi')}")
                        modified = True
                    elif field == 'dia_ban_pho_bien':
                        crop['dia_ban_pho_bien'] = ['Đồng bằng sông Cửu Long', 'Đông Nam Bộ', 'Tây Nguyên']
                        report["fixes_applied"].append(f"Thêm địa bàn mặc định cho {crop.get('name_vi')}")
                        modified = True
                    elif field == 'dac_tinh_sinh_thai':
                        crop['dac_tinh_sinh_thai'] = "Thích hợp đất phù sa, đất thịt pha cát thoát nước tốt, pH 5.5 - 6.5, ẩm độ 70-80%."
                        report["fixes_applied"].append(f"Thêm đặc tính sinh thái cho {crop.get('name_vi')}")
                        modified = True
                    elif field == 'danh_sach_benh':
                        crop['danh_sach_benh'] = []
                        modified = True

        crop_id = str(crop.get('id', '')).strip()
        name_vi = str(crop.get('name_vi', '')).strip()
        sci_name = str(crop.get('scientific_name', '')).strip()
        
        # ID Check
        if not crop_id:
            report["errors"].append(f"{crop_err_prefix} 'id' rỗng")
        elif crop_id in seen_ids:
            err = f"{crop_err_prefix} Trùng lặp 'id': '{crop_id}'"
            report["errors"].append(err)
            report["duplicate_ids"].append(crop_id)
            if autofix:
                new_id = f"crop_{idx+1:04d}"
                crop['id'] = new_id
                seen_ids.add(new_id)
                report["fixes_applied"].append(f"Đổi ID trùng {crop_id} -> {new_id}")
                modified = True
        else:
            seen_ids.add(crop_id)

        # Name VI Check
        if not name_vi:
            report["errors"].append(f"{crop_err_prefix} 'name_vi' rỗng")
        else:
            norm_name = normalize_str(name_vi)
            if norm_name in seen_names:
                prev_id = seen_names[norm_name]
                msg = f"{crop_err_prefix} Trùng tên tiếng Việt '{name_vi}' với cây {prev_id}"
                report["warnings"].append(msg)
                report["duplicate_names"].append(name_vi)
            else:
                seen_names[norm_name] = crop_id

        # Scientific Name Check
        if not sci_name:
            report["errors"].append(f"{crop_err_prefix} 'scientific_name' rỗng")
        else:
            norm_sci = sci_name.lower().strip()
            if norm_sci in seen_sci_names:
                prev_id = seen_sci_names[norm_sci]
                msg = f"{crop_err_prefix} Trùng tên khoa học '{sci_name}' với cây {prev_id}"
                report["warnings"].append(msg)
                report["duplicate_sci_names"].append(sci_name)
            else:
                seen_sci_names[norm_sci] = crop_id

        # Check dia_ban_pho_bien
        dia_ban = crop.get('dia_ban_pho_bien')
        if not dia_ban or (isinstance(dia_ban, list) and len(dia_ban) == 0):
            report["warnings"].append(f"{crop_err_prefix} 'dia_ban_pho_bien' rỗng")

        # Check dac_tinh_sinh_thai
        sinh_thai = crop.get('dac_tinh_sinh_thai', '')
        if not sinh_thai or len(str(sinh_thai).strip()) < 10:
            report["warnings"].append(f"{crop_err_prefix} 'dac_tinh_sinh_thai' quá ngắn hoặc rỗng")

        # Check danh_sach_benh
        diseases = crop.get('danh_sach_benh', [])
        if not isinstance(diseases, list):
            report["errors"].append(f"{crop_err_prefix} 'danh_sach_benh' không phải là danh sách (Array)")
            continue

        disease_count = len(diseases)
        report["total_diseases"] += disease_count

        if disease_count < 2:
            viol_msg = f"{crop_err_prefix} Số lượng bệnh ({disease_count}) vi phạm quy định (phải có ít nhất 2 bệnh)"
            report["errors"].append(viol_msg)
            report["disease_count_violations"].append(viol_msg)

        # Audit each disease
        for d_idx, d in enumerate(diseases):
            d_prefix = f"{crop_err_prefix} Bệnh [{d_idx}] ({d.get('ten_benh', 'N/A')}):"
            
            # Required fields in disease
            req_d_fields = ['ten_benh', 'muc_do_nguy_hiem', 'tac_nhan', 'trieu_chung_dien_hinh', 'phan_biet_chan_doan_kep', 'kiem_tra_thuc_dia', 'phac_do_vietgap']
            for df in req_d_fields:
                if df not in d or d[df] is None:
                    err = f"{d_prefix} Thiếu trường bắt buộc '{df}'"
                    report["errors"].append(err)
                    report["missing_fields"].append(err)

            # Audit tac_nhan
            tn = d.get('tac_nhan')
            if isinstance(tn, dict):
                loai = str(tn.get('loai', '')).strip()
                ten_kh = str(tn.get('ten_khoa_hoc', '')).strip()
                if not loai:
                    report["errors"].append(f"{d_prefix} 'tac_nhan.loai' rỗng")
                if not ten_kh:
                    report["errors"].append(f"{d_prefix} 'tac_nhan.ten_khoa_hoc' rỗng")
                else:
                    # Microbiological precision audit
                    is_correct, detected_loai, reason = check_pathogen_classification(loai, ten_kh)
                    if not is_correct:
                        err = f"{d_prefix} LỖI Y HỌC THỰC VẬT: {reason}"
                        report["errors"].append(err)
                        report["pathology_mismatches"].append({
                            "crop": name_vi,
                            "disease": d.get('ten_benh'),
                            "pathogen": ten_kh,
                            "current_loai": loai,
                            "correct_loai": detected_loai,
                            "reason": reason
                        })
                        if autofix:
                            tn['loai'] = detected_loai
                            report["fixes_applied"].append(f"Sửa tác nhân cho {d.get('ten_benh')}: '{loai}' -> '{detected_loai}'")
                            modified = True
            elif isinstance(tn, str):
                report["warnings"].append(f"{d_prefix} 'tac_nhan' ở dạng chuỗi, nên chuẩn hóa thành đối tượng {{loai, ten_khoa_hoc}}")

            # Audit phac_do_vietgap
            pd = d.get('phac_do_vietgap')
            if isinstance(pd, dict):
                if 'canh_tac' not in pd or not pd['canh_tac']:
                    report["warnings"].append(f"{d_prefix} 'phac_do_vietgap' thiếu mục 'canh_tac'")
                if 'sinh_hoc' not in pd or not pd['sinh_hoc']:
                    report["warnings"].append(f"{d_prefix} 'phac_do_vietgap' thiếu mục 'sinh_hoc'")
            else:
                report["warnings"].append(f"{d_prefix} 'phac_do_vietgap' không phải là đối tượng chuẩn")

    if autofix and modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(crops, f, ensure_ascii=False, indent=2)
        print(f"✅ Đã tự động lưu sửa chữa vào tệp: {file_path}")

    report["schema_pass"] = (len(report["errors"]) == 0)
    return report

def format_audit_summary(report: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 60)
    lines.append(f"🔍 BÁO CÁO KIỂM ĐỊNH Y HỌC THỰC VẬT & SCHEMA AUDITOR 4")
    lines.append(f"📁 Tệp kiểm tra: {report['file']}")
    lines.append(f"📊 Cú pháp JSON: {'✅ HỢP LỆ (100% Valid JSON)' if report['valid_json'] else '❌ LỖI PARSE'}")
    lines.append(f"🌱 Tổng số cây trồng (Crops): {report['total_crops']}")
    lines.append(f"🦠 Tổng số bệnh học (Diseases): {report['total_diseases']}")
    lines.append(f"❌ Số lỗi nghiêm trọng (Errors): {len(report['errors'])}")
    lines.append(f"⚠️  Số cảnh báo (Warnings): {len(report['warnings'])}")
    lines.append(f"🔬 Lỗi phân loại tác nhân vi sinh: {len(report['pathology_mismatches'])}")
    lines.append(f"🆔 Trùng lặp ID: {len(report['duplicate_ids'])}")
    lines.append(f"🌿 Trùng lặp tên cây: {len(report['duplicate_names'])}")
    lines.append(f"📐 Vi phạm số lượng bệnh (>= 2 bệnh/cây): {len(report['disease_count_violations'])}")
    lines.append(f"🛠️  Số sửa chữa đã áp dụng (Autofixes): {len(report['fixes_applied'])}")
    lines.append(f"🏁 ĐÁNH GIÁ TỔNG QUAN: {'🟢 ĐẠT CHUẨN HOÀN TOÀN (100% COMPLIANT)' if report['schema_pass'] else '🔴 CHƯA ĐẠT CHUẨN'}")
    lines.append("=" * 60)
    
    if report['pathology_mismatches']:
        lines.append("\n🔬 CHI TIẾT CÁC LỖI TÍNH CHÍNH XÁC Y HỌC THỰC VẬT:")
        for idx, m in enumerate(report['pathology_mismatches'][:10]):
            lines.append(f"  {idx+1}. Cây: {m['crop']} | Bệnh: {m['disease']}")
            lines.append(f"     Tác nhân: {m['pathogen']} -> Hiện tại: '{m['current_loai']}' => Chuẩn: '{m['correct_loai']}'")
        if len(report['pathology_mismatches']) > 10:
            lines.append(f"  ... và còn {len(report['pathology_mismatches']) - 10} lỗi khác.")

    if report['errors'][:10]:
        lines.append("\n❌ TOP CÁC LỖI SCHEMA & DỮ LIỆU:")
        for idx, err in enumerate(report['errors'][:10]):
            lines.append(f"  {idx+1}. {err}")
        if len(report['errors']) > 10:
            lines.append(f"  ... và còn {len(report['errors']) - 10} lỗi khác.")

    return "\n".join(lines)

if __name__ == '__main__':
    target_file = sys.argv[1] if len(sys.argv) > 1 else 'ultra-project/src/data/vietnam_plant_pathology_400_crops.json'
    do_fix = '--fix' in sys.argv
    rep = audit_crop_dataset(target_file, autofix=do_fix)
    print(format_audit_summary(rep))
    if not rep['schema_pass']:
        sys.exit(1)
    sys.exit(0)
