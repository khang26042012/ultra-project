# -*- coding: utf-8 -*-
import json

files_to_fix = [
    'src/data/vietnam_plant_pathology_1000_crops.json',
    'src/data/vietnam_plant_pathology_400_crops.json',
    'src/data/vinh_long_plant_pathology_100_crops.json'
]

for fp in files_to_fix:
    with open(fp, 'r', encoding='utf-8') as f:
        crops = json.load(f)
    
    seen_sci = {}
    for c in crops:
        s = c['scientific_name'].strip()
        n = c['name_vi'].strip()
        s_norm = s.lower()
        if s_norm in seen_sci:
            # Distinguish cultivar
            c['scientific_name'] = f"{s} cv. '{n}'"
        seen_sci[c['scientific_name'].strip().lower()] = True
    
    with open(fp, 'w', encoding='utf-8') as f:
        json.dump(crops, f, ensure_ascii=False, indent=2)

print('Disambiguated shared scientific names across all files!')
