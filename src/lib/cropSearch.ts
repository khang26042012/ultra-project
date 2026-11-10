import fs from 'fs';
import path from 'path';

export interface DiseasePathogen {
  loai: string;
  ten_khoa_hoc: string;
  vector_truyen_benh?: string;
}

export interface DiseaseVietGAP {
  canh_tac: string;
  sinh_hoc: string;
  khuyen_cao_chuyen_gia?: string;
  khuyen_cao_vinh_long?: string;
}

export interface CropDisease {
  ten_benh: string;
  muc_do_nguy_hiem: string;
  tac_nhan: DiseasePathogen | string;
  trieu_chung_dien_hinh: string[] | string;
  phan_biet_chan_doan_kep: string;
  kiem_tra_thuc_dia: string;
  phac_do_vietgap: DiseaseVietGAP | Record<string, string>;
}

export interface CropRecord {
  id: string;
  topic: string;
  name_vi: string;
  scientific_name: string;
  dia_ban_pho_bien: string[] | string;
  dac_tinh_sinh_thai: string;
  danh_sach_benh: CropDisease[];
}

export interface CropSearchResult {
  crop_name: string;
  scientific_name: string;
  topic: string;
  dia_ban_pho_bien: string[] | string;
  dac_tinh_sinh_thai: string;
  matched_disease?: CropDisease;
  danh_sach_benh: CropDisease[];
  score: number;
}

// In-memory cache for fast retrieval (< 2ms)
let cachedCrops: CropRecord[] | null = null;

// Normalize Vietnamese string: remove diacritics, lowercase, strip punctuation
export function normalizeVietnamese(str: unknown): string {
  if (typeof str !== 'string' || !str) return '';
  return str
    .toLowerCase()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/[đĐ]/g, 'd')
    .replace(/[^a-z0-9\s]/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

// Load crops from files: 1000 crops -> 400 crops -> 100 crops
export function loadAllCrops(): CropRecord[] {
  if (cachedCrops && cachedCrops.length > 0) {
    return cachedCrops;
  }

  const candidatePaths = [
    path.join(/*turbopackIgnore: true*/ process.cwd(), 'src', 'data', 'vietnam_plant_pathology_1000_crops.json'),
    path.join(/*turbopackIgnore: true*/ process.cwd(), 'src', 'data', 'vietnam_plant_pathology_400_crops.json'),
    path.join(/*turbopackIgnore: true*/ process.cwd(), 'src', 'data', 'vinh_long_plant_pathology_100_crops.json'),
  ];

  for (const p of candidatePaths) {
    if (fs.existsSync(p)) {
      try {
        const raw = fs.readFileSync(p, 'utf8');
        const data = JSON.parse(raw);
        if (Array.isArray(data) && data.length > 0) {
          cachedCrops = data;
          return cachedCrops;
        }
      } catch (e) {
        console.error(`Error loading crop data from ${p}:`, e);
      }
    }
  }

  return [];
}

// Invalidate cache (useful after dataset updates)
export function invalidateCropCache(): void {
  cachedCrops = null;
}

// Search crop knowledge base by crop name and symptoms
export function searchCropKnowledge(
  cropName: string,
  symptoms: string[] | string = []
): {
  success: boolean;
  total_crops_in_db: number;
  results: CropSearchResult[];
  best_match?: CropSearchResult;
} {
  const allCrops = loadAllCrops();
  if (allCrops.length === 0) {
    return {
      success: false,
      total_crops_in_db: 0,
      results: [],
    };
  }

  const normCrop = normalizeVietnamese(cropName || '');
  const symptomsArray = Array.isArray(symptoms)
    ? symptoms
    : typeof symptoms === 'string'
    ? [symptoms]
    : [];
  const normSymptoms = symptomsArray
    .map((s) => normalizeVietnamese(s))
    .filter(Boolean);

  const scored: CropSearchResult[] = [];

  for (const crop of allCrops) {
    let score = 0;
    const nameNorm = normalizeVietnamese(crop.name_vi);
    const sciNorm = normalizeVietnamese(crop.scientific_name);

    if (normCrop) {
      if (nameNorm === normCrop) {
        score += 100;
      } else if (nameNorm.includes(normCrop) || normCrop.includes(nameNorm)) {
        score += 50;
      } else if (sciNorm.includes(normCrop)) {
        score += 40;
      } else {
        const cropWords = normCrop.split(' ').filter((w) => w.length > 1);
        for (const w of cropWords) {
          if (nameNorm.includes(w)) score += 12;
        }
      }
    }

    let bestMatchedDisease: CropDisease | undefined;
    let maxDiseaseScore = 0;

    if (Array.isArray(crop.danh_sach_benh)) {
      for (const d of crop.danh_sach_benh) {
        let diseaseScore = 0;
        const diseaseNameNorm = normalizeVietnamese(d.ten_benh);

        if (normCrop && diseaseNameNorm.includes(normCrop)) {
          diseaseScore += 30;
        }

        const rawSymptoms = Array.isArray(d.trieu_chung_dien_hinh)
          ? d.trieu_chung_dien_hinh.join(' ')
          : d.trieu_chung_dien_hinh || '';
        const symptomsNorm = normalizeVietnamese(rawSymptoms);

        for (const sym of normSymptoms) {
          if (diseaseNameNorm.includes(sym)) {
            diseaseScore += 25;
          } else if (symptomsNorm.includes(sym)) {
            diseaseScore += 15;
          } else {
            const symWords = sym.split(' ').filter((w) => w.length > 2);
            for (const sw of symWords) {
              if (symptomsNorm.includes(sw)) diseaseScore += 4;
            }
          }
        }

        if (diseaseScore > maxDiseaseScore) {
          maxDiseaseScore = diseaseScore;
          bestMatchedDisease = d;
        }
      }
    }

    score += maxDiseaseScore;

    if (score > 0) {
      scored.push({
        crop_name: crop.name_vi,
        scientific_name: crop.scientific_name,
        topic: crop.topic,
        dia_ban_pho_bien: crop.dia_ban_pho_bien,
        dac_tinh_sinh_thai: crop.dac_tinh_sinh_thai,
        matched_disease: bestMatchedDisease || crop.danh_sach_benh?.[0],
        danh_sach_benh: crop.danh_sach_benh || [],
        score,
      });
    }
  }

  scored.sort((a, b) => b.score - a.score);

  const topResults = scored.slice(0, 5);

  return {
    success: topResults.length > 0,
    total_crops_in_db: allCrops.length,
    results: topResults,
    best_match: topResults[0],
  };
}
