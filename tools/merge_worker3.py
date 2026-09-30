import json
import os
import re

def main():
    w3_candidates = [
        'src/data/worker3_crops.json',
        'ultra-project/src/data/worker3_crops.json',
        '../src/data/worker3_crops.json'
    ]
    w3_path = next((p for p in w3_candidates if os.path.exists(p)), None)

    master_candidates = [
        'src/data/vietnam_plant_pathology_1000_crops.json',
        'ultra-project/src/data/vietnam_plant_pathology_1000_crops.json',
    ]
    master_path = next((p for p in master_candidates if os.path.exists(p)), None)

    w3_crops = json.load(open(w3_path, 'r', encoding='utf-8'))
    master_crops = json.load(open(master_path, 'r', encoding='utf-8'))

    master_names = {c['name_vi'].lower().strip() for c in master_crops}
    master_scis = {c['scientific_name'].lower().strip() for c in master_crops}

    current_max_id = 0
    for c in master_crops:
        m = re.search(r'\d+', c.get('id', ''))
        if m:
            val = int(m.group(0))
            if val > current_max_id:
                current_max_id = val

    added_count = 0
    for c in w3_crops:
        name = c['name_vi'].lower().strip()
        sci = c['scientific_name'].lower().strip()
        if name not in master_names and sci not in master_scis:
            current_max_id += 1
            new_crop = dict(c)
            new_crop['id'] = f"crop_{current_max_id:04d}"
            master_crops.append(new_crop)
            master_names.add(name)
            master_scis.add(sci)
            added_count += 1

    print(f"Added {added_count} crops from Worker 3. New total: {len(master_crops)}")

    # Save to all target paths
    base_dir = os.path.dirname(master_path)
    targets = [
        os.path.join(base_dir, 'vietnam_plant_pathology_1000_crops.json'),
        os.path.join(base_dir, 'vietnam_plant_pathology_400_crops.json'),
        os.path.join(base_dir, 'vinh_long_plant_pathology_100_crops.json'),
    ]

    for t in targets:
        with open(t, 'w', encoding='utf-8') as f:
            json.dump(master_crops, f, ensure_ascii=False, indent=2)
        print(f"Saved {len(master_crops)} crops to {t} ({os.path.getsize(t)} bytes)")

if __name__ == '__main__':
    main()
