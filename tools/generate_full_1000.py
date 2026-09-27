# -*- coding: utf-8 -*-
"""
Full 1,000 Crops Generator & Consolidator for AgriVision (Phan Trọng Khang)
Brings total unique crops to >= 1,000 with rich pathology profiles.
"""
import json
import os
import re

# Helper to normalize for deduplication
def norm(s):
    if not s:
        return ""
    return re.sub(r'\s+', ' ', s.strip().lower())

def create_disease(name, danger, pathogen_type, pathogen_sci, symptoms, diff_diag, field_test, organic_proto, cultural_proto):
    return {
        "ten_benh": name,
        "muc_do_nguy_hiem": danger,
        "tac_nhan": {
            "loai": pathogen_type,
            "ten_khoa_hoc": pathogen_sci
        },
        "trieu_chung_dien_hinh": symptoms,
        "phan_biet_chan_doan_kep": diff_diag,
        "kiem_tra_thuc_dia": field_test,
        "phac_do_vietgap": {
            "canh_tac": cultural_proto,
            "sinh_hoc": organic_proto,
            "khuyen_cao_chuyen_gia": "Thực hiện theo quy chuẩn VietGAP và hướng dẫn của Chi cục Trồng trọt & BVTV địa phương"
        }
    }

def create_crop(topic, name_vi, scientific_name, regions, ecology, diseases):
    return {
        "topic": topic,
        "name_vi": name_vi,
        "scientific_name": scientific_name,
        "dia_ban_pho_bien": regions,
        "dac_tinh_sinh_thai": ecology,
        "danh_sach_benh": diseases
    }
