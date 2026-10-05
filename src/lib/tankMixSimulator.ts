// src/lib/tankMixSimulator.ts
// AgriVision Biochemical Conflict Engine & Virtual Spray Tank WALES Simulator
// Cố vấn kỹ thuật: Nông nghiệp công nghệ cao & Khuyến nông Vĩnh Long (VietGAP)

export type PesticideCategory =
  | 'fungicide' // Thuốc trừ nấm, vi khuẩn
  | 'insecticide' // Thuốc trừ sâu, rầy, bọ trĩ
  | 'foliar_fertilizer' // Phân bón lá, vi lượng
  | 'adjuvant' // Chất bám dính, loang trải, trợ lực
  | 'bio_control'; // Chế phẩm sinh học, vi sinh đối kháng

export type FormulationType =
  | 'WP' // Bột thấm nước (Wettable Powder)
  | 'WDG' // Hạt phân tán trong nước (Water Dispersible Granules)
  | 'WG' // Hạt phân tán
  | 'SP' // Bột hòa tan
  | 'SC' // Dung dịch huyền phù đậm đặc (Suspension Concentrate)
  | 'SL' // Dung dịch tan trong nước (Soluble Liquid)
  | 'FL' // Dạng lỏng huyền phù
  | 'EC' // Nhũ dầu (Emulsifiable Concentrate)
  | 'EW' // Nhũ tương dầu trong nước
  | 'ME' // Vi nhũ tương
  | 'OD' // Dầu phân tán
  | 'ADJ'; // Chất trợ lực, bám dính

export type CompatibilityLevel = 'compatible' | 'conditional' | 'incompatible';

export interface PesticideItem {
  id: string;
  name: string;
  tradeNames: string[];
  category: PesticideCategory;
  categoryLabelVi: string;
  activeIngredient: string;
  chemicalGroup: string;
  formulation: FormulationType;
  phType: 'acidic' | 'neutral' | 'alkaline';
  dosePer16L: string;
  dosePer25L: string;
  dosePer200L: string;
  description: string;
  targetPests: string;
}

export interface MixConflictRule {
  groupA: string;
  groupB: string;
  level: CompatibilityLevel;
  title: string;
  mechanism: string; // Cơ chế hóa sinh
  consequence: string; // Hậu quả thực địa (cháy lá, nghẹt béc, mất hoạt tính)
  recommendation: string; // Giải pháp khuyến nông
}

export interface WalesStep {
  stepIndex: number;
  walesCode: 'W' | 'A' | 'L' | 'E' | 'S';
  walesName: string;
  title: string;
  items: PesticideItem[];
  instructions: string;
}

export interface TankMixSimulationResult {
  overallStatus: CompatibilityLevel;
  statusBadge: {
    color: 'emerald' | 'amber' | 'red';
    text: string;
    icon: string;
  };
  hasIncompatibility: boolean;
  hasConditionals: boolean;
  conflicts: Array<{
    itemA: PesticideItem;
    itemB: PesticideItem;
    level: CompatibilityLevel;
    title: string;
    mechanism: string;
    consequence: string;
    recommendation: string;
  }>;
  walesSequence: WalesStep[];
  solutionVisual: {
    liquidColor: string; // CSS color string
    glowColor: string;
    hasPrecipitation: boolean;
    hasOilSeparation: boolean;
    statusText: string;
    description: string;
  };
  doseBreakdown: Array<{
    item: PesticideItem;
    calculatedDose: string;
  }>;
  generalAdvices: string[];
}

// 1. Comprehensive Database of Standard Pesticides & Active Ingredients in Vietnam
export const POPULAR_PESTICIDES: PesticideItem[] = [
  // --- GỐC ĐỒNG (COPPER) ---
  {
    id: 'copper_hydroxide',
    name: 'Đồng Hydroxide (Champion 77WP)',
    tradeNames: ['Champion 77WP', 'Kocide 53.8DF', 'Funguran-OH'],
    category: 'fungicide',
    categoryLabelVi: 'Trừ nấm & vi khuẩn',
    activeIngredient: 'Copper Hydroxide',
    chemicalGroup: 'copper_inorganic',
    formulation: 'WP',
    phType: 'alkaline',
    dosePer16L: '25 - 30 g',
    dosePer25L: '40 - 50 g',
    dosePer200L: '300 - 400 g',
    description: 'Thuốc trừ bệnh gốc đồng phổ rộng, tính kiềm cao, tiếp xúc bảo vệ.',
    targetPests: 'Ghẻ loét, đốm mắt cua, thán thư, cháy bìa lá vi khuẩn',
  },
  {
    id: 'copper_oxychloride',
    name: 'Đồng Oxychloride (Coc 85WP)',
    tradeNames: ['Coc 85WP', 'Cuproxat 345SC'],
    category: 'fungicide',
    categoryLabelVi: 'Trừ nấm & vi khuẩn',
    activeIngredient: 'Copper Oxychloride',
    chemicalGroup: 'copper_inorganic',
    formulation: 'WP',
    phType: 'alkaline',
    dosePer16L: '20 - 30 g',
    dosePer25L: '35 - 45 g',
    dosePer200L: '250 - 350 g',
    description: 'Đồng vô cơ phổ biến trừ nấm vi khuẩn, kiềm tính nhẹ.',
    targetPests: 'Rỉ sắt, nấm hồng, đốm lá, xì mủ vi khuẩn',
  },

  // --- GỐC LƯU HUỲNH (SULFUR) ---
  {
    id: 'sulfur_elemental',
    name: 'Lưu huỳnh vi sinh (Kumulus 80DF / Sulcox)',
    tradeNames: ['Kumulus 80DF', 'Thiovit 80WG', 'Microthiol Special'],
    category: 'fungicide',
    categoryLabelVi: 'Trừ nấm & nhện đỏ',
    activeIngredient: 'Sulfur (Lưu huỳnh)',
    chemicalGroup: 'sulfur_elemental',
    formulation: 'WG',
    phType: 'acidic',
    dosePer16L: '30 - 40 g',
    dosePer25L: '50 - 65 g',
    dosePer200L: '400 - 500 g',
    description: 'Trừ phấn trắng và nhện đỏ bằng cơ chế bốc hơi xông hơi.',
    targetPests: 'Phấn trắng, nhện đỏ, nhện lông nhung, rỉ sắt',
  },

  // --- DITHIOCARBAMATE ---
  {
    id: 'mancozeb',
    name: 'Mancozeb Xanh / Vàng (Dithane M-45 / Manozeb)',
    tradeNames: ['Dithane M-45 80WP', 'Mancozeb Xanh 80WP', 'Unizeb M-45'],
    category: 'fungicide',
    categoryLabelVi: 'Trừ nấm phổ rộng',
    activeIngredient: 'Mancozeb (Manganese + Zinc)',
    chemicalGroup: 'dithiocarbamate',
    formulation: 'WP',
    phType: 'neutral',
    dosePer16L: '40 - 50 g',
    dosePer25L: '60 - 80 g',
    dosePer200L: '500 - 600 g',
    description: 'Thuốc bảo vệ đa điểm tiếp xúc phổ cực rộng, bám dính tốt.',
    targetPests: 'Thán thư, mốc sương, đốm vòng, thối đen, rỉ sắt',
  },

  // --- TRIAZOLE & STROBILURIN ---
  {
    id: 'hexaconazole',
    name: 'Hexaconazole (Anvil 5SC)',
    tradeNames: ['Anvil 5SC', 'Saizole 5SC', 'Tungvil 5SC'],
    category: 'fungicide',
    categoryLabelVi: 'Trừ nấm nội hấp',
    activeIngredient: 'Hexaconazole',
    chemicalGroup: 'triazole',
    formulation: 'SC',
    phType: 'neutral',
    dosePer16L: '15 - 20 ml',
    dosePer25L: '25 - 30 ml',
    dosePer200L: '200 - 250 ml',
    description: 'Nội hấp lưu dẫn mạnh, trị nấm mốc và đốm vằn khô vằn.',
    targetPests: 'Khô vằn, đốm lá nấm, nấm hồng, phấn trắng',
  },
  {
    id: 'azoxystrobin_difenoconazole',
    name: 'Azoxystrobin + Difenoconazole (Amistar Top 325SC)',
    tradeNames: ['Amistar Top 325SC', 'Top Plus 325SC'],
    category: 'fungicide',
    categoryLabelVi: 'Trừ nấm cao cấp',
    activeIngredient: 'Azoxystrobin + Difenoconazole',
    chemicalGroup: 'strobilurin_triazole',
    formulation: 'SC',
    phType: 'neutral',
    dosePer16L: '10 - 15 ml',
    dosePer25L: '15 - 20 ml',
    dosePer200L: '150 - 200 ml',
    description: 'Bộ đôi đỉnh cao lưu dẫn hai chiều, dưỡng xanh lá và trị bệnh phổ rộng.',
    targetPests: 'Đạo ôn, lem lép hạt, thán thư, đốm nâu, đốm vòng',
  },
  {
    id: 'metalaxyl',
    name: 'Metalaxyl (Ridomil Gold / Mataxyl 500WP)',
    tradeNames: ['Ridomil Gold 68WG', 'Mataxyl 500WP', 'Vilaxyl 35WP'],
    category: 'fungicide',
    categoryLabelVi: 'Đặc trị nấm thủy mi Phytophthora',
    activeIngredient: 'Metalaxyl-M (Mefenoxam)',
    chemicalGroup: 'phenylamide',
    formulation: 'WP',
    phType: 'neutral',
    dosePer16L: '30 - 40 g',
    dosePer25L: '50 - 60 g',
    dosePer200L: '400 - 500 g',
    description: 'Chuyên trị nấm sương mai, Phytophthora xì mủ thân, thối rễ.',
    targetPests: 'Xì mủ sầu riêng, thối rễ vàng lá, sương mai cà chua',
  },
  {
    id: 'fosetyl_aluminium',
    name: 'Fosetyl Aluminium (Aliette 800WG)',
    tradeNames: ['Aliette 800WG', 'Alonil 80WP'],
    category: 'fungicide',
    categoryLabelVi: 'Lưu dẫn 2 chiều kích kháng',
    activeIngredient: 'Fosetyl Aluminium',
    chemicalGroup: 'phosphonate',
    formulation: 'WG',
    phType: 'acidic',
    dosePer16L: '20 - 30 g',
    dosePer25L: '35 - 45 g',
    dosePer200L: '300 - 400 g',
    description: 'Lưu dẫn hai chiều cực nhanh, kích thích cây tự tiết phytoalexin diệt nấm.',
    targetPests: 'Nứt thân xì mủ, thối trái, chết nhanh hồ tiêu',
  },

  // --- TRỪ SÂU SINH HỌC & HÓA HỌC ---
  {
    id: 'abamectin',
    name: 'Abamectin 3.6EC (BrightTin / Reasgant)',
    tradeNames: ['BrightTin 3.6EC', 'Reasgant 3.6EC', 'Abasuper 3.6EC'],
    category: 'insecticide',
    categoryLabelVi: 'Trừ sâu & nhện sinh học',
    activeIngredient: 'Abamectin',
    chemicalGroup: 'avermectin',
    formulation: 'EC',
    phType: 'neutral',
    dosePer16L: '8 - 10 ml',
    dosePer25L: '12 - 15 ml',
    dosePer200L: '100 - 120 ml',
    description: 'Gốc kháng sinh vi sinh vật, diệt nhện đỏ, sâu vẽ bùa, bọ trĩ nhanh.',
    targetPests: 'Nhện đỏ, bọ trĩ, sâu cuốn lá, sâu vẽ bùa',
  },
  {
    id: 'emamectin_benzoate',
    name: 'Emamectin benzoate (Proclaim / Angun 5WG)',
    tradeNames: ['Proclaim 1.9EC', 'Angun 5WG', 'Tungmectin 5EC'],
    category: 'insecticide',
    categoryLabelVi: 'Trừ sâu sinh học thế hệ mới',
    activeIngredient: 'Emamectin Benzoate',
    chemicalGroup: 'avermectin',
    formulation: 'WDG',
    phType: 'neutral',
    dosePer16L: '5 - 8 g',
    dosePer25L: '8 - 12 g',
    dosePer200L: '70 - 100 g',
    description: 'Hiệu lực cao với sâu kháng thuốc, an toàn cho thiên địch và môi trường.',
    targetPests: 'Sâu tơ, sâu xanh da láng, sâu đục trái, bọ trĩ',
  },
  {
    id: 'petroleum_oil',
    name: 'Dầu khoáng nông nghiệp (SK Enspray 99EC)',
    tradeNames: ['SK Enspray 99EC', 'Citrole 96.3EC'],
    category: 'insecticide',
    categoryLabelVi: 'Dầu khoáng trừ sâu nhện & loang trải',
    activeIngredient: 'Petroleum Spray Oil (Dầu khoáng)',
    chemicalGroup: 'petroleum_oil',
    formulation: 'EC',
    phType: 'neutral',
    dosePer16L: '30 - 40 ml',
    dosePer25L: '50 - 60 ml',
    dosePer200L: '400 - 500 ml',
    description: 'Làm tắc lỗ thở côn trùng, bọc trứng, tăng bám dính bảo vệ màng lá.',
    targetPests: 'Rệp sáp, rầy mềm, nhện đỏ, bọ trĩ, sâu vẽ bùa',
  },
  {
    id: 'chlorantraniliprole',
    name: 'Chlorantraniliprole (Virtako 40WG / Prevathon)',
    tradeNames: ['Virtako 40WG', 'Prevathon 5SC', 'Voliam Targo'],
    category: 'insecticide',
    categoryLabelVi: 'Đặc trị sâu đục thân & cuốn lá',
    activeIngredient: 'Chlorantraniliprole',
    chemicalGroup: 'diamide',
    formulation: 'WG',
    phType: 'neutral',
    dosePer16L: '3 - 4.5 g',
    dosePer25L: '5 - 7 g',
    dosePer200L: '35 - 50 g',
    description: 'Ức chế co cơ côn trùng thụ thể Ryanodine, hiệu lực kéo dài 14-21 ngày.',
    targetPests: 'Sâu đục thân, sâu cuốn lá, sâu đục bắp, bọ trĩ',
  },
  {
    id: 'pyrethroid_alpha',
    name: 'Alpha-cypermethrin (Fastac 5EC)',
    tradeNames: ['Fastac 5EC', 'Viper 5EC', 'Sherpa 25EC'],
    category: 'insecticide',
    categoryLabelVi: 'Cúc tổng hợp hạ gục nhanh',
    activeIngredient: 'Alpha-cypermethrin',
    chemicalGroup: 'pyrethroid',
    formulation: 'EC',
    phType: 'acidic',
    dosePer16L: '10 - 15 ml',
    dosePer25L: '15 - 20 ml',
    dosePer200L: '150 - 200 ml',
    description: 'Thuốc trừ sâu cúc tổng hợp tiếp xúc vị độc, nhạy cảm môi trường kiềm.',
    targetPests: 'Bọ xít muỗi, sâu khoang, bọ trĩ, rầy chổng cánh',
  },

  // --- VI SINH ĐỐI KHÁNG ---
  {
    id: 'trichoderma',
    name: 'Nấm đối kháng Trichoderma (Tri-Cho Bio)',
    tradeNames: ['Trichoderma Bio-M', 'Nema-Tri', 'Điền Trang Tricho'],
    category: 'bio_control',
    categoryLabelVi: 'Vi sinh đối kháng nấm bệnh rễ',
    activeIngredient: 'Trichoderma harzianum + T. viride',
    chemicalGroup: 'bio_microbial',
    formulation: 'WP',
    phType: 'neutral',
    dosePer16L: '30 - 50 g',
    dosePer25L: '50 - 75 g',
    dosePer200L: '400 - 500 g',
    description: 'Bào tử nấm vi sinh sống cạnh tranh và ký sinh nấm gây hại rễ.',
    targetPests: 'Fusarium, Phytophthora, Rhizoctonia, tuyến trùng rễ',
  },
  {
    id: 'bacillus_thuringiensis',
    name: 'Vi khuẩn diệt sâu Bt (Dipel 6.4WG / Delfin)',
    tradeNames: ['Dipel 6.4WG', 'Delfin WG', 'Bt-Thuringiensis'],
    category: 'bio_control',
    categoryLabelVi: 'Vi sinh diệt sâu miệng nhai',
    activeIngredient: 'Bacillus thuringiensis',
    chemicalGroup: 'bio_microbial',
    formulation: 'WDG',
    phType: 'neutral',
    dosePer16L: '15 - 20 g',
    dosePer25L: '25 - 30 g',
    dosePer200L: '200 - 250 g',
    description: 'Chứa tinh thể độc tố đục thủng ruột sâu non khi ăn phải lá.',
    targetPests: 'Sâu tơ, sâu đục trái non, sâu xanh bắp cải',
  },

  // --- PHÂN BÓN LÁ & VI LƯỢNG ---
  {
    id: 'calcium_boron',
    name: 'Canxi Bo vi lượng chelate (Canxi Bo Sữa)',
    tradeNames: ['Canxi Bo Sữa BoMax', 'Calci-Boron Gold', 'YaraVita Caltrac'],
    category: 'foliar_fertilizer',
    categoryLabelVi: 'Phân bón lá Canxi & Bo',
    activeIngredient: 'Calcium (Ca) + Boron (B)',
    chemicalGroup: 'calcium_boron_chelate',
    formulation: 'SL',
    phType: 'neutral',
    dosePer16L: '20 - 25 ml',
    dosePer25L: '30 - 40 ml',
    dosePer200L: '250 - 300 ml',
    description: 'Chống rụng hoa, tăng đậu trái, chống nứt da trái sầu riêng, cam sành.',
    targetPests: 'Khắc phục rụng bông, khô đọt, nứt trái, méo trái',
  },
  {
    id: 'mkp_phosphate',
    name: 'Phân bón lá Lân & Kali (MKP 0-52-34)',
    tradeNames: ['MKP Haifa 0-52-34', 'Mono Potassium Phosphate'],
    category: 'foliar_fertilizer',
    categoryLabelVi: 'Phân bón lá tạo mầm hoa',
    activeIngredient: 'Monopotassium Phosphate ($KH_2PO_4$)',
    chemicalGroup: 'phosphate_fertilizer',
    formulation: 'WP',
    phType: 'acidic',
    dosePer16L: '40 - 50 g',
    dosePer25L: '60 - 80 g',
    dosePer200L: '500 - 800 g',
    description: 'Lân và Kali cực cao giúp già lá, chặn đọt non, kích thích phân hóa mầm hoa.',
    targetPests: 'Chặn đọt ra bông, kích mầm hoa, chắc hạt vào gạo',
  },

  // --- CHẤT TRỢ LỰC BÁM DÍNH ---
  {
    id: 'adjuvant_sticker',
    name: 'Chất bám dính sinh học loang trải (Bám Dính Nano)',
    tradeNames: ['Bám dính Super Silicon 69', 'Keo bám dính sinh học', 'Silwet 408'],
    category: 'adjuvant',
    categoryLabelVi: 'Chất bám dính & trợ lực',
    activeIngredient: 'Polyether Polymethylsiloxane Copolymer',
    chemicalGroup: 'adjuvant_surfactant',
    formulation: 'ADJ',
    phType: 'neutral',
    dosePer16L: '5 - 10 ml',
    dosePer25L: '10 - 15 ml',
    dosePer200L: '80 - 100 ml',
    description: 'Phá vỡ sức căng bề mặt giọt nước, giúp thuốc lan trải cực mỏng chống rửa trôi.',
    targetPests: 'Tăng 30-50% hiệu lực tiếp xúc của thuốc trừ nấm sâu',
  },
];

// 2. Biochemical Conflict Rules Matrix (VietGAP Clinical Compatibility)
export const CONFLICT_RULES: MixConflictRule[] = [
  // 1. Đồng + Lưu huỳnh (CỰC KỲ NGUY HIỂM: Tạo kết tủa CuS đen, cháy lá)
  {
    groupA: 'copper_inorganic',
    groupB: 'sulfur_elemental',
    level: 'incompatible',
    title: '🔴 Xung đột tạo kết tủa CuS & Cháy lá nghiêm trọng',
    mechanism:
      'Gốc Đồng vô cơ ($Cu^{2+}$) phản ứng oxy hóa khử tức thì với Lưu huỳnh nguyên tố ($S$) tạo thành Đồng Sunfua ($CuS$) kết tủa màu nâu đen lơ lửng, đồng thời giải phóng ion làm biến tính diệp lục.',
    consequence:
      'Nước thuốc bị vón cục đen ngòm làm nghẹt béc phun; cây bị ngộ độc đồng (copper phytotoxicity) gây cháy xém lá diện rộng, rụng bông và trái non sau 24-48h.',
    recommendation:
      'Tuyệt đối KHÔNG pha chung Đồng và Lưu huỳnh. Nếu cần sử dụng cả hai, phải phun cách nhau tối thiểu 10 - 14 ngày!',
  },

  // 2. Lưu huỳnh + Dầu khoáng (NGUY HIỂM: Phá hủy tầng cutin, cháy lá)
  {
    groupA: 'sulfur_elemental',
    groupB: 'petroleum_oil',
    level: 'incompatible',
    title: '🔴 Xung đột Lưu huỳnh & Dầu khoáng gây cháy tế bào biểu bì',
    mechanism:
      'Dầu khoáng nông nghiệp hòa tan màng bảo vệ của lưu huỳnh, khiến lưu huỳnh xâm nhập ồ ạt qua lớp cutin vào tế bào mô lá mà không có cơ chế đào thải kịp.',
    consequence:
      'Gây hiện tượng cháy lá diện rộng do ánh nắng hội tụ qua lớp dầu mang lưu huỳnh nóng (solar scorch), lá xoăn quăn queo và rụng trụi cành.',
    recommendation:
      'Cấm phun dầu khoáng chung với lưu huỳnh. Khoảng cách an toàn giữa 2 lần phun dầu khoáng và lưu huỳnh phải từ 20 - 30 ngày!',
  },

  // 3. Gốc Đồng + Vi sinh đối kháng (Trichoderma, Bt, Beauveria)
  {
    groupA: 'copper_inorganic',
    groupB: 'bio_microbial',
    level: 'incompatible',
    title: '🔴 Bất hoạt & Tiêu diệt toàn bộ vi sinh vật có ích',
    mechanism:
      'Đồng vô cơ có hoạt tính diệt khuẩn và diệt nấm phổ rộng cực mạnh. Khi pha chung, các ion đồng sẽ phá hủy màng tế bào của nấm đối kháng Trichoderma hoặc vi khuẩn Bacillus.',
    consequence:
      '100% bào tử vi sinh vật trong bình phun bị tiêu diệt ngay lập tức trước khi chạm tới mặt lá/rễ, làm mất hoàn toàn giá trị của chế phẩm vi sinh hữu cơ.',
    recommendation:
      'Tách riêng biệt. Phun thuốc gốc đồng trước để dập dịch bệnh cấp tính, sau đó 10-15 ngày mới tưới bổ sung vi sinh Trichoderma/Bacillus vào đất.',
  },

  // 4. Gốc Lân hữu cơ / Cúc tổng hợp + Gốc Đồng (Môi trường kiềm thủy phân thuốc trừ sâu)
  {
    groupA: 'copper_inorganic',
    groupB: 'pyrethroid',
    level: 'incompatible',
    title: '🔴 Kiềm hóa thủy phân làm mất hoạt lực thuốc trừ sâu',
    mechanism:
      'Đồng Hydroxide và Boóc-đô có tính kiềm cao ($pH > 8.5$). Trong môi trường kiềm, liên kết este của hoạt chất cúc tổng hợp (Alpha-cypermethrin, Deltamethrin) bị thủy phân phân rã cực nhanh.',
    consequence:
      'Thuốc trừ sâu bị mất trên 80% tác dụng hạ gục côn trùng, xịt tốn công tốn tiền mà sâu rầy không chết, đồng thời tạo muối kết tinh bám dính đáy bình.',
    recommendation:
      'Không pha thuốc trừ sâu cúc tổng hợp với thuốc gốc đồng có tính kiềm cao.',
  },

  // 5. Canxi + Phân bón lân Phốt phát (MKP, Super Lân)
  {
    groupA: 'calcium_boron_chelate',
    groupB: 'phosphate_fertilizer',
    level: 'incompatible',
    title: '🔴 Tạo kết tủa Canxi Phosphat ($Ca_3(PO_4)_2$) nghẹt bình',
    mechanism:
      'Ion Canxi ($Ca^{2+}$) tự do kết hợp ngay với gốc Phosphate ($H_2PO_4^-$, $PO_4^{3-}$) tạo thành kết tủa Canxi Phosphat không tan trong nước.',
    consequence:
      'Nước bình chuyển sang màu trắng sữa đục như vôi, lắng cặn trắng dày dưới đáy bình gây tắc nghẽn hoàn toàn đường dẫn và béc phun; cây không hấp thu được cả Canxi lẫn Lân.',
    recommendation:
      'Phun Canxi Bo riêng rẽ, hoặc phun Lân MKP riêng rẽ vào các giai đoạn sinh trưởng khác nhau.',
  },

  // 6. Gốc Đồng + Mancozeb (Dithiocarbamate) -> Có điều kiện (Caution)
  {
    groupA: 'copper_inorganic',
    groupB: 'dithiocarbamate',
    level: 'conditional',
    title: '🟡 Lưu ý khi phối hợp Đồng và Mancozeb',
    mechanism:
      'Mancozeb có thể bị phân hủy một phần nếu pH dung dịch đồng quá kiềm ($pH > 8.0$). Tuy nhiên ở nồng độ loãng và phun ngay thì vẫn cộng hưởng phòng trừ nấm phổ rộng.',
    consequence:
      'Dung dịch có thể đổi màu nâu sẫm, nếu để quá 2 tiếng sẽ giảm 20-30% hoạt tính của Mancozeb.',
    recommendation:
      'Chỉ pha khi dùng ngay trong 2 giờ. Hòa tan Mancozeb với nước trước cho tan đều, sau đó mới cho đồng vào sau cùng, khuấy liên tục và phun ngay.',
  },

  // 7. Dầu khoáng nông nghiệp + Phân bón lá đậm đặc -> Có điều kiện (Caution)
  {
    groupA: 'petroleum_oil',
    groupB: 'phosphate_fertilizer',
    level: 'conditional',
    title: '🟡 Nguy cơ tách lớp nhũ dầu khi pha cùng muối phân bón nồng độ cao',
    mechanism:
      'Nồng độ ion muối hòa tan cao trong phân bón lá (MKP, NPK) có thể phá vỡ hệ chất nhũ hóa trong dầu khoáng EC.',
    consequence:
      'Dầu khoáng bị tách lớp nổi váng lên mặt nước, phun trúng ngọn non có thể làm táp lá cục bộ.',
    recommendation:
      'Thử Jar Test trong ca nhỏ trước. Luôn pha phân bón lá thật loãng trước, sau đó khuấy tan hoàn toàn rồi mới rót dầu khoáng vào cuối.',
  },

  // 8. Chế phẩm vi sinh + Thuốc trừ nấm hóa học (Triazole, Strobilurin)
  {
    groupA: 'bio_microbial',
    groupB: 'triazole',
    level: 'incompatible',
    title: '🔴 Thuốc trừ nấm nội hấp ức chế nấm sinh học có ích',
    mechanism:
      'Hoạt chất Hexaconazole / Triazole ức chế sinh tổng hợp Ergosterol trên màng tế bào của tất cả các loài nấm, bao gồm cả nấm có ích Trichoderma.',
    consequence:
      'Bào tử nấm Trichoderma bị ức chế phát triển, không thể nảy mầm hình thành khuẩn ty bảo vệ rễ.',
    recommendation:
      'Tuyệt đối không pha chung nấm đối kháng vi sinh với bất kỳ loại thuốc trừ nấm hóa học nào.',
  },
];

// 3. Helper to determine WALES sorting order
export function getWalesStepCode(formulation: FormulationType, category: PesticideCategory): 'W' | 'L' | 'E' | 'S' {
  if (category === 'adjuvant') return 'S';
  if (category === 'foliar_fertilizer' && formulation !== 'WP' && formulation !== 'WDG') return 'S';

  switch (formulation) {
    case 'WP':
    case 'WDG':
    case 'WG':
    case 'SP':
      return 'W';
    case 'SC':
    case 'SL':
    case 'FL':
      return 'L';
    case 'EC':
    case 'EW':
    case 'ME':
    case 'OD':
      return 'E';
    case 'ADJ':
      return 'S';
    default:
      return 'L';
  }
}

// 4. Master Simulation Engine
export function simulateTankMix(
  selectedItemIds: string[],
  tankVolumeLiters: 16 | 25 | 200 = 16
): TankMixSimulationResult {
  const selectedItems = selectedItemIds
    .map((id) => POPULAR_PESTICIDES.find((p) => p.id === id))
    .filter((p): p is PesticideItem => Boolean(p));

  // If less than 2 items, return baseline safe status
  if (selectedItems.length < 2) {
    const single = selectedItems[0];
    const walesOrder: WalesStep[] = single
      ? [
          {
            stepIndex: 1,
            walesCode: getWalesStepCode(single.formulation, single.category),
            walesName: single.formulation.includes('W') ? 'Wettable Powder' : 'Liquid/Solution',
            title: `Bước 1: Cho ${single.name} vào bình chứa 1/2 nước`,
            items: [single],
            instructions: 'Hòa tan riêng trong ca nhỏ trước, sau đó đổ vào bình và khuấy đều.',
          },
        ]
      : [];

    return {
      overallStatus: 'compatible',
      statusBadge: {
        color: 'emerald',
        text: 'Đơn chất an toàn (Chưa chọn phối trộn)',
        icon: 'ShieldCheck',
      },
      hasIncompatibility: false,
      hasConditionals: false,
      conflicts: [],
      walesSequence: walesOrder,
      solutionVisual: {
        liquidColor: 'rgba(16, 185, 129, 0.25)', // Smooth light emerald
        glowColor: '#10B981',
        hasPrecipitation: false,
        hasOilSeparation: false,
        statusText: 'Dung dịch đồng nhất, trong xanh an toàn',
        description: 'Chưa có tương tác xung đột. Hãy chọn thêm loại thuốc thứ 2 để chạy ma trận xung đột hóa sinh.',
      },
      doseBreakdown: selectedItems.map((item) => ({
        item,
        calculatedDose:
          tankVolumeLiters === 16
            ? item.dosePer16L
            : tankVolumeLiters === 25
            ? item.dosePer25L
            : item.dosePer200L,
      })),
      generalAdvices: [
        'Luôn đổ nước vào bình trước 1/2 đến 2/3 thể tích trước khi cho thuốc vào.',
        'Đeo đồ bảo hộ khẩu trang, kính bảo hộ và găng tay khi tiếp xúc với thuốc BVTV.',
      ],
    };
  }

  // Cross-compare all pairs C(n, 2)
  const detectedConflicts: TankMixSimulationResult['conflicts'] = [];

  for (let i = 0; i < selectedItems.length; i++) {
    for (let j = i + 1; j < selectedItems.length; j++) {
      const itemA = selectedItems[i];
      const itemB = selectedItems[j];

      for (const rule of CONFLICT_RULES) {
        const matchForward =
          (itemA.chemicalGroup === rule.groupA && itemB.chemicalGroup === rule.groupB) ||
          (itemA.chemicalGroup === rule.groupB && itemB.chemicalGroup === rule.groupA);

        if (matchForward) {
          detectedConflicts.push({
            itemA,
            itemB,
            level: rule.level,
            title: rule.title,
            mechanism: rule.mechanism,
            consequence: rule.consequence,
            recommendation: rule.recommendation,
          });
        }
      }
    }
  }

  // Overall status evaluation
  const hasIncompatible = detectedConflicts.some((c) => c.level === 'incompatible');
  const hasConditional = detectedConflicts.some((c) => c.level === 'conditional');

  let overallStatus: CompatibilityLevel = 'compatible';
  let badgeColor: 'emerald' | 'amber' | 'red' = 'emerald';
  let badgeText = '🟢 Tương thích hoàn toàn (An toàn)';
  let badgeIcon = 'ShieldCheck';

  if (hasIncompatible) {
    overallStatus = 'incompatible';
    badgeColor = 'red';
    badgeText = '🔴 CẤM PHA TRỘN (Xung đột hóa sinh nghiêm trọng)';
    badgeIcon = 'ShieldAlert';
  } else if (hasConditional) {
    overallStatus = 'conditional';
    badgeColor = 'amber';
    badgeText = '🟡 Pha trộn có điều kiện (Cần thử Jar Test)';
    badgeIcon = 'AlertTriangle';
  }

  // Visual simulation state
  let liquidColor = 'rgba(16, 185, 129, 0.35)'; // Default emerald
  let glowColor = '#10B981';
  let statusText = 'Dung dịch đồng nhất, trong suốt, không kết tủa';
  let description = 'Các hoạt chất tương thích tốt, tuân thủ đúng thứ tự WALES sẽ đạt hiệu lực phòng trừ tối đa.';
  const hasPrecipitation = hasIncompatible;
  let hasOilSeparation = false;

  if (hasIncompatible) {
    liquidColor = 'rgba(239, 68, 68, 0.45)'; // Crimson alert with turbidity
    glowColor = '#EF4444';
    statusText = 'Dung dịch bị vón cục, đổi màu, xuất hiện kết tủa chìm đáy';
    description =
      'CẢNH BÁO: Xảy ra phản ứng hóa sinh bất lợi làm kết tủa, sinh nhiệt hoặc phân hủy hoạt chất. Tuyệt đối KHÔNG đổ vào bình phun!';
  } else if (hasConditional) {
    liquidColor = 'rgba(245, 158, 11, 0.35)'; // Amber caution
    glowColor = '#F59E0B';
    statusText = 'Dung dịch hơi đục nhẹ, cần khuấy liên tục và phun ngay';
    description =
      'Các chất có thể phối trộn nhưng dễ giảm hiệu lực nếu để lâu. Bắt buộc thử nghiệm ca nhỏ Jar Test trước 15 phút.';
    hasOilSeparation = selectedItems.some((i) => i.chemicalGroup === 'petroleum_oil');
  }

  // Build WALES pouring sequence
  // W -> A -> L -> E -> S
  const groupW = selectedItems.filter(
    (item) => getWalesStepCode(item.formulation, item.category) === 'W'
  );
  const groupL = selectedItems.filter(
    (item) => getWalesStepCode(item.formulation, item.category) === 'L'
  );
  const groupE = selectedItems.filter(
    (item) => getWalesStepCode(item.formulation, item.category) === 'E'
  );
  const groupS = selectedItems.filter(
    (item) => getWalesStepCode(item.formulation, item.category) === 'S'
  );

  const walesSteps: WalesStep[] = [];
  let stepCounter = 1;

  if (groupW.length > 0) {
    walesSteps.push({
      stepIndex: stepCounter++,
      walesCode: 'W',
      walesName: 'Wettable Powders & Granules (Bột thấm nước WP / WDG / WG)',
      title: `Bước ${stepCounter - 1}: Cho dạng Bột & Hạt phân tán (${groupW.map((g) => g.name).join(', ')})`,
      items: groupW,
      instructions:
        'Hòa tan trước dạng bột vào một xô nước nhỏ, khuấy tan 100% không còn lợn cợn rồi mới đổ vào bình đang chứa 1/2 nước.',
    });
  }

  // Agitate step always between Powder and Liquid
  walesSteps.push({
    stepIndex: stepCounter++,
    walesCode: 'A',
    walesName: 'Agitation (Khuấy đảo hoàn toàn)',
    title: `Bước ${stepCounter - 1}: Khuấy đều nước thuốc trong bình`,
    items: [],
    instructions:
      'Dùng que sạch khuấy liên tục 1 - 2 phút cho các hạt phân tử bột phân tán đồng nhất trước khi thêm chất lỏng.',
  });

  if (groupL.length > 0) {
    walesSteps.push({
      stepIndex: stepCounter++,
      walesCode: 'L',
      walesName: 'Liquid Flowables & Suspensions (Dạng huyền phù SC / Dung dịch SL)',
      title: `Bước ${stepCounter - 1}: Rót dạng Nước & Huyền phù (${groupL.map((g) => g.name).join(', ')})`,
      items: groupL,
      instructions:
        'Rót từ từ dạng SC/SL vào bình trong khi vẫn tiếp tục khuấy đều tay để tránh hiện tượng sốc dung môi.',
    });
  }

  if (groupE.length > 0) {
    walesSteps.push({
      stepIndex: stepCounter++,
      walesCode: 'E',
      walesName: 'Emulsifiable Concentrates (Dạng Nhũ dầu EC / Nhũ tương EW)',
      title: `Bước ${stepCounter - 1}: Thêm dạng Nhũ Dầu (${groupE.map((g) => g.name).join(', ')})`,
      items: groupE,
      instructions:
        'Nhũ dầu EC cho vào sau khi các dạng bột đã phân tán hoàn toàn để dầu không bọc màng ngăn bột tan.',
    });
  }

  if (groupS.length > 0) {
    walesSteps.push({
      stepIndex: stepCounter++,
      walesCode: 'S',
      walesName: 'Surfactants, Adjuvants & Foliar (Chất bám dính, Trợ lực, Phân bón lá)',
      title: `Bước ${stepCounter - 1}: Cho Bám dính & Dinh dưỡng (${groupS.map((g) => g.name).join(', ')})`,
      items: groupS,
      instructions:
        'Chất bám dính loang trải cho vào sau cùng nhất để phủ đều giọt nước thuốc, sau đó châm thêm nước cho đủ thể tích bình và đậy nắp.',
    });
  }

  const doseBreakdown = selectedItems.map((item) => ({
    item,
    calculatedDose:
      tankVolumeLiters === 16
        ? item.dosePer16L
        : tankVolumeLiters === 25
        ? item.dosePer25L
        : item.dosePer200L,
  }));

  const generalAdvices = [
    'Quy tắc 50% Nước: Luôn đổ nước sạch vào bình ít nhất 50% trước khi cho bất kỳ loại thuốc nào vào.',
    'Bài test ca nhỏ (Jar Test): Nếu chưa từng phối trộn cặp thuốc này, hãy lấy 1 lít nước trong ca nhựa trong suốt, pha theo tỷ lệ rồi để yên 15 phút. Nếu thấy nổi váng dầu, kết tủa trắng/đen hoặc bốc khói nóng -> KHÔNG ĐƯỢC PHUN!',
    'Thời gian xịt thuốc: Nên phun vào lúc sáng sớm (khi sương vừa ráo, 6h - 8h30) hoặc chiều mát (16h30 - 18h). Tránh tuyệt đối trời nắng gắt làm bốc hơi nhanh và gây cháy lá.',
  ];

  return {
    overallStatus,
    statusBadge: {
      color: badgeColor,
      text: badgeText,
      icon: badgeIcon,
    },
    hasIncompatibility: hasIncompatible,
    hasConditionals: hasConditional,
    conflicts: detectedConflicts,
    walesSequence: walesSteps,
    solutionVisual: {
      liquidColor,
      glowColor,
      hasPrecipitation,
      hasOilSeparation,
      statusText,
      description,
    },
    doseBreakdown,
    generalAdvices,
  };
}
