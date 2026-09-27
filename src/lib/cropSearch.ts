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
export function normalizeVietnamese(str: string): string {
  if (!str) return '';
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
  symptoms: string[] = []
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
  const normSymptoms = (symptoms || []).map((s) => normalizeVietnamese(s)).filter(Boolean);

  const scored: CropSearchResult[] = [];

  for (const crop of allCrops) {
    const cropNameNorm = normalizeVietnamese(crop.name_vi);
    const cropSciNorm = normalizeVietnamese(crop.scientific_name);

    let cropScore = 0;

    // Crop name matching
    if (normCrop) {
      if (cropNameNorm === normCrop || cropSciNorm === normCrop) {
        cropScore += 100;
      } else if (cropNameNorm.includes(normCrop) || normCrop.includes(cropNameNorm)) {
        cropScore += 60;
      } else {
        const cropTokens = cropNameNorm.split(' ');
        const queryTokens = normCrop.split(' ');
        const matches = queryTokens.filter((t) => t.length > 1 && cropTokens.includes(t));
        if (matches.length > 0) {
          cropScore += matches.length * 25;
        }
      }
    }

    // Symptom matching across crop diseases
    let bestDisease: CropDisease | undefined;
    let highestDiseaseScore = 0;

    if (Array.isArray(crop.danh_sach_benh)) {
      for (const disease of crop.danh_sach_benh) {
        let dScore = 0;
        const diseaseText = [
          disease.ten_benh || '',
          Array.isArray(disease.trieu_chung_dien_hinh)
            ? disease.trieu_chung_dien_hinh.join(' ')
            : disease.trieu_chung_dien_hinh || '',
          typeof disease.tac_nhan === 'object'
            ? `${disease.tac_nhan.loai || ''} ${disease.tac_nhan.ten_khoa_hoc || ''}`
            : disease.tac_nhan || '',
          disease.phan_biet_chan_doan_kep || '',
        ].join(' ');

        const normDiseaseText = normalizeVietnamese(diseaseText);

        for (const sym of normSymptoms) {
          if (normDiseaseText.includes(sym)) {
            dScore += 30;
          } else {
            const symTokens = sym.split(' ');
            const matched = symTokens.filter((t) => t.length > 1 && normDiseaseText.includes(t));
            if (matched.length > 0) {
              dScore += matched.length * 10;
            }
          }
        }

        if (dScore > highestDiseaseScore) {
          highestDiseaseScore = dScore;
          bestDisease = disease;
        }
      }
    }

    const totalScore = cropScore + highestDiseaseScore;

    if (totalScore > 0) {
      scored.push({
        crop_name: crop.name_vi,
        scientific_name: crop.scientific_name,
        topic: crop.topic,
        dia_ban_pho_bien: crop.dia_ban_pho_bien,
        dac_tinh_sinh_thai: crop.dac_tinh_sinh_thai,
        matched_disease: bestDisease || (crop.danh_sach_benh && crop.danh_sach_benh[0]),
        danh_sach_benh: crop.danh_sach_benh || [],
        score: totalScore,
      });
    }
  }

  scored.sort((a, b) => b.score - a.score);

  const topResults = scored.slice(0, 3);

  return {
    success: topResults.length > 0,
    total_crops_in_db: allCrops.length,
    results: topResults,
    best_match: topResults[0],
  };
}

// Get crop by ID
export function getCropById(id: string): CropRecord | undefined {
  const all = loadAllCrops();
  return all.find((c) => c.id === id);
}
