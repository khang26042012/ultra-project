'use client';

import React, { useState, useEffect, useMemo, useCallback } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import {
  Search,
  ArrowLeft,
  Sparkles,
  BookOpen,
  ShieldCheck,
  AlertTriangle,
  Activity,
  Layers,
  ChevronRight,
  ExternalLink,
  X,
  MapPin,
  Leaf,
  FlaskConical,
  CheckCircle2,
} from 'lucide-react';
import { CropRecord, CropDisease } from '@/lib/cropSearch';

const CATEGORIES = [
  { id: 'all', label: 'Tất cả cây trồng', icon: '🌱' },
  { id: 'fruit', label: 'Cây ăn trái đặc sản', icon: '🍊' },
  { id: 'grain', label: 'Lương thực & Hoa màu', icon: '🌾' },
  { id: 'veg', label: 'Rau củ & Gia vị', icon: '🥬' },
  { id: 'industrial', label: 'Cây công nghiệp', icon: '☕' },
  { id: 'medicinal_forest', label: 'Dược liệu & Lâm nghiệp', icon: '🌲' },
  { id: 'exotic_flower', label: 'Cây nhập khẩu & Hoa kiểng', icon: '🌐' },
];

export default function CropsEncyclopediaPage() {
  const router = useRouter();
  const [crops, setCrops] = useState<CropRecord[]>([]);
  const [loading, setLoading] = useState(true);
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedTopic, setSelectedTopic] = useState('all');
  const [selectedCrop, setSelectedCrop] = useState<CropRecord | null>(null);
  const [activeDiseaseTab, setActiveDiseaseTab] = useState(0);

  // Fetch crops list
  useEffect(() => {
    let isMounted = true;
    async function fetchCrops() {
      setLoading(true);
      try {
        const res = await fetch(`/api/crops?topic=${selectedTopic}&q=${encodeURIComponent(searchQuery)}&limit=120`);
        const data = await res.json();
        if (isMounted && data.success) {
          setCrops(data.crops || []);
        }
      } catch (err) {
        console.error('Failed to load encyclopedia crops:', err);
      } finally {
        if (isMounted) setLoading(false);
      }
    }

    const timer = setTimeout(fetchCrops, 200);
    return () => {
      isMounted = false;
      clearTimeout(timer);
    };
  }, [searchQuery, selectedTopic]);

  const handleAskAI = (cropName: string, diseaseName?: string) => {
    const prompt = diseaseName
      ? `Tôi muốn hỏi về bệnh ${diseaseName} trên cây ${cropName}. Nhờ bác sĩ AgriVision chẩn đoán lâm sàng và hướng dẫn phác đồ điều trị VietGAP.`
      : `Tôi muốn tìm hiểu về các loại sâu bệnh thường gặp và cách phòng trừ an toàn trên cây ${cropName}.`;
    sessionStorage.setItem('agrivision_prefill_prompt', prompt);
    router.push('/');
  };

  const getDangerBadge = (danger: string) => {
    if (danger.includes('Hiểm nghèo') || danger.includes('Cực kỳ')) {
      return (
        <span className="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-medium bg-red-50 text-red-700 border border-red-200 dark:bg-red-950/40 dark:text-red-300 dark:border-red-900/50">
          <span className="w-1.5 h-1.5 rounded-full bg-red-600 animate-pulse" />
          Hiểm nghèo
        </span>
      );
    }
    if (danger.includes('Nặng') || danger.includes('Cao')) {
      return (
        <span className="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-medium bg-amber-50 text-amber-700 border border-amber-200 dark:bg-amber-950/40 dark:text-amber-300 dark:border-amber-900/50">
          <span className="w-1.5 h-1.5 rounded-full bg-amber-500" />
          Nguy cơ cao
        </span>
      );
    }
    return (
      <span className="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-50 text-blue-700 border border-blue-200 dark:bg-blue-950/40 dark:text-blue-300 dark:border-blue-900/50">
        <span className="w-1.5 h-1.5 rounded-full bg-blue-500" />
        Trung bình
      </span>
    );
  };

  return (
    <div className="min-h-screen bg-[#ffffff] dark:bg-[#0f0f0f] text-[#0d0d0d] dark:text-[#ececec]">
      {/* Top Navigation Bar */}
      <header className="sticky top-0 z-30 bg-[#ffffff]/90 dark:bg-[#0f0f0f]/90 backdrop-blur-md border-b border-[#e5e5e5] dark:border-[#262626]">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 h-16 flex items-center justify-between gap-4">
          <div className="flex items-center gap-3">
            <Link
              href="/"
              className="p-2 -ml-2 rounded-xl text-[#737373] hover:text-[#0d0d0d] dark:text-[#a3a3a3] dark:hover:text-white hover:bg-[#f4f4f4] dark:hover:bg-[#1a1a1a] transition-colors flex items-center gap-1.5 text-sm font-medium"
            >
              <ArrowLeft className="w-4 h-4" strokeWidth={1.5} />
              <span className="hidden sm:inline">Quay lại Chat</span>
            </Link>
            <div className="h-4 w-px bg-[#e5e5e5] dark:bg-[#262626]" />
            <div className="flex items-center gap-2">
              <span className="w-6 h-6 rounded-lg bg-[#0d0d0d] text-white dark:bg-white dark:text-black flex items-center justify-center font-bold text-xs">
                AV
              </span>
              <span className="font-semibold text-sm sm:text-base tracking-tight">
                Toàn Thư Bệnh Học Cây Trồng
              </span>
              <span className="hidden md:inline-block px-2 py-0.5 text-[11px] font-mono bg-[#f4f4f4] dark:bg-[#1f1f1f] border border-[#e5e5e5] dark:border-[#2f2f2f] rounded-full text-[#737373] dark:text-[#a3a3a3]">
                1.500+ Loài Cây
              </span>
            </div>
          </div>

          <div className="flex items-center gap-2">
            <button
              onClick={() => router.push('/')}
              className="inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-medium rounded-full bg-[#0d0d0d] text-white dark:bg-white dark:text-black hover:opacity-90 transition-opacity shadow-xs cursor-pointer"
            >
              <Sparkles className="w-3.5 h-3.5" strokeWidth={1.75} />
              <span>Chẩn đoán AI</span>
            </button>
          </div>
        </div>
      </header>

      {/* Hero Banner with Provenance */}
      <section className="bg-gradient-to-b from-[#f9f9f9] to-[#ffffff] dark:from-[#141414] dark:to-[#0f0f0f] border-b border-[#e5e5e5] dark:border-[#262626] py-10 px-4 sm:px-6">
        <div className="max-w-4xl mx-auto text-center space-y-3">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-medium bg-[#f0f0f0] dark:bg-[#212121] border border-[#e5e5e5] dark:border-[#2f2f2f] text-[#525252] dark:text-[#a3a3a3]">
            <BookOpen className="w-3.5 h-3.5" strokeWidth={1.5} />
            <span>Kho Siêu Dữ Liệu Bệnh Học Cây Trồng Số 1 Việt Nam</span>
          </div>
          <h1 className="text-2xl sm:text-4xl font-bold tracking-tight text-[#0d0d0d] dark:text-white">
            Tra Cứu Lâm Sàng & Phổ Bệnh Học Thực Vật
          </h1>
          <p className="text-sm sm:text-base text-[#737373] dark:text-[#a3a3a3] max-w-2xl mx-auto leading-relaxed">
            Công trình nghiên cứu khoa học của tác giả trẻ <strong className="text-[#0d0d0d] dark:text-white font-semibold">Phan Trọng Khang</strong> (Lớp 9¹, THCS Vĩnh An, tỉnh Vĩnh Long), chuẩn hóa 1.500+ loài cây trồng bản địa 63 tỉnh thành và cây kinh tế quốc tế, 100% phác đồ sinh học VietGAP an toàn.
          </p>

          {/* Quick Metrics */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 max-w-2xl mx-auto pt-3">
            <div className="p-3 rounded-2xl bg-[#ffffff] dark:bg-[#1a1a1a] border border-[#e5e5e5] dark:border-[#2a2a2a] shadow-2xs">
              <div className="text-xl font-bold text-[#0d0d0d] dark:text-white">1.500+</div>
              <div className="text-[11px] text-[#737373] dark:text-[#a3a3a3]">Loài cây trồng</div>
            </div>
            <div className="p-3 rounded-2xl bg-[#ffffff] dark:bg-[#1a1a1a] border border-[#e5e5e5] dark:border-[#2a2a2a] shadow-2xs">
              <div className="text-xl font-bold text-[#0d0d0d] dark:text-white">3.500+</div>
              <div className="text-[11px] text-[#737373] dark:text-[#a3a3a3]">Bệnh học lâm sàng</div>
            </div>
            <div className="p-3 rounded-2xl bg-[#ffffff] dark:bg-[#1a1a1a] border border-[#e5e5e5] dark:border-[#2a2a2a] shadow-2xs">
              <div className="text-xl font-bold text-emerald-600 dark:text-emerald-400">100%</div>
              <div className="text-[11px] text-[#737373] dark:text-[#a3a3a3]">Chuẩn VietGAP</div>
            </div>
            <div className="p-3 rounded-2xl bg-[#ffffff] dark:bg-[#1a1a1a] border border-[#e5e5e5] dark:border-[#2a2a2a] shadow-2xs">
              <div className="text-xl font-bold text-blue-600 dark:text-blue-400">&lt; 2ms</div>
              <div className="text-[11px] text-[#737373] dark:text-[#a3a3a3]">Tốc độ RAG nội tại</div>
            </div>
          </div>
        </div>
      </section>

      {/* Main Content Area */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 py-8">
        {/* Search & Filter Bar */}
        <div className="space-y-4 mb-8">
          <div className="relative max-w-2xl mx-auto">
            <Search className="w-5 h-5 absolute left-4 top-1/2 -translate-y-1/2 text-[#8e8e8e]" strokeWidth={1.5} />
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Tìm theo tên cây (sầu riêng, việt quất, bưởi...), tên khoa học hoặc tên bệnh..."
              className="w-full pl-11 pr-10 py-3 rounded-2xl bg-[#f9f9f9] dark:bg-[#1a1a1a] border border-[#e5e5e5] dark:border-[#2e2e2e] text-sm text-[#0d0d0d] dark:text-white placeholder:text-[#8e8e8e] focus:outline-hidden focus:border-[#0d0d0d] dark:focus:border-white transition-colors shadow-2xs"
            />
            {searchQuery && (
              <button
                onClick={() => setSearchQuery('')}
                className="absolute right-3.5 top-1/2 -translate-y-1/2 text-[#8e8e8e] hover:text-[#0d0d0d] dark:hover:text-white"
              >
                <X className="w-4 h-4" />
              </button>
            )}
          </div>

          {/* Category Tabs */}
          <div className="flex items-center gap-2 overflow-x-auto pb-2 scrollbar-none justify-start sm:justify-center">
            {CATEGORIES.map((cat) => (
              <button
                key={cat.id}
                onClick={() => setSelectedTopic(cat.id)}
                className={`whitespace-nowrap px-3.5 py-1.5 rounded-full text-xs font-medium transition-all shrink-0 cursor-pointer ${
                  selectedTopic === cat.id
                    ? 'bg-[#0d0d0d] text-white dark:bg-white dark:text-black shadow-2xs'
                    : 'bg-[#f4f4f4] text-[#525252] hover:bg-[#e5e5e5] dark:bg-[#1c1c1c] dark:text-[#a3a3a3] dark:hover:bg-[#282828]'
                }`}
              >
                <span className="mr-1.5">{cat.icon}</span>
                <span>{cat.label}</span>
              </button>
            ))}
          </div>
        </div>

        {/* Crops Grid */}
        {loading ? (
          <div className="py-20 text-center space-y-3">
            <div className="w-8 h-8 mx-auto border-2 border-[#0d0d0d] dark:border-white border-t-transparent rounded-full animate-spin" />
            <p className="text-xs text-[#737373] dark:text-[#a3a3a3]">Đang tải kho tri thức thực vật...</p>
          </div>
        ) : crops.length === 0 ? (
          <div className="py-20 text-center space-y-3 border border-dashed border-[#e5e5e5] dark:border-[#2e2e2e] rounded-3xl">
            <Leaf className="w-10 h-10 mx-auto text-[#a3a3a3]" strokeWidth={1.25} />
            <h3 className="text-sm font-semibold text-[#0d0d0d] dark:text-white">Không tìm thấy cây trồng phù hợp</h3>
            <p className="text-xs text-[#737373] dark:text-[#a3a3a3] max-w-sm mx-auto">
              Thử tìm kiếm với từ khóa khác (ví dụ: bưởi, lúa, xoài, việt quất, wasabi) hoặc chọn danh mục Tất cả.
            </p>
          </div>
        ) : (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            {crops.map((crop) => {
              const diseasesCount = Array.isArray(crop.danh_sach_benh) ? crop.danh_sach_benh.length : 0;
              const regions = Array.isArray(crop.dia_ban_pho_bien)
                ? crop.dia_ban_pho_bien.slice(0, 3).join(', ')
                : crop.dia_ban_pho_bien;

              return (
                <div
                  key={crop.id}
                  onClick={() => {
                    setSelectedCrop(crop);
                    setActiveDiseaseTab(0);
                  }}
                  className="group relative p-4 rounded-2xl bg-[#ffffff] dark:bg-[#161616] border border-[#e5e5e5] dark:border-[#262626] hover:border-[#0d0d0d] dark:hover:border-white transition-all shadow-2xs hover:shadow-xs cursor-pointer flex flex-col justify-between"
                >
                  <div className="space-y-2">
                    <div className="flex items-start justify-between gap-2">
                      <h3 className="font-semibold text-base text-[#0d0d0d] dark:text-white group-hover:underline">
                        {crop.name_vi}
                      </h3>
                      <span className="shrink-0 text-[11px] font-mono px-2 py-0.5 rounded-md bg-[#f4f4f4] dark:bg-[#222222] text-[#737373] dark:text-[#a3a3a3] border border-[#e5e5e5] dark:border-[#2e2e2e]">
                        {diseasesCount} bệnh
                      </span>
                    </div>

                    <p className="text-xs italic font-serif text-[#737373] dark:text-[#a3a3a3]">
                      {crop.scientific_name}
                    </p>

                    <p className="text-xs text-[#525252] dark:text-[#b4b4b4] line-clamp-2 leading-relaxed">
                      {crop.dac_tinh_sinh_thai}
                    </p>
                  </div>

                  <div className="mt-4 pt-3 border-t border-[#f0f0f0] dark:border-[#222222] flex items-center justify-between text-xs text-[#737373] dark:text-[#8e8e8e]">
                    <div className="flex items-center gap-1 truncate max-w-[180px]">
                      <MapPin className="w-3.5 h-3.5 shrink-0" strokeWidth={1.5} />
                      <span className="truncate">{regions || 'Toàn quốc'}</span>
                    </div>
                    <span className="inline-flex items-center gap-0.5 text-xs font-medium text-[#0d0d0d] dark:text-white group-hover:translate-x-0.5 transition-transform">
                      <span>Xem hồ sơ</span>
                      <ChevronRight className="w-3.5 h-3.5" />
                    </span>
                  </div>
                </div>
              );
            })}
          </div>
        )}
      </main>

      {/* Crop Pathology Profile Modal */}
      {selectedCrop && (
        <div
          onClick={() => setSelectedCrop(null)}
          className="fixed inset-0 z-50 bg-black/60 backdrop-blur-xs flex items-center justify-center p-4 animate-in fade-in duration-150"
        >
          <div
            onClick={(e) => e.stopPropagation()}
            className="w-full max-w-3xl max-h-[90vh] bg-[#ffffff] dark:bg-[#161616] rounded-3xl border border-[#e5e5e5] dark:border-[#2e2e2e] shadow-2xl flex flex-col overflow-hidden animate-in zoom-in-95 duration-150"
          >
            {/* Modal Header */}
            <div className="p-5 border-b border-[#e5e5e5] dark:border-[#262626] flex items-start justify-between gap-4 bg-[#f9f9f9] dark:bg-[#1c1c1c]">
              <div className="space-y-1">
                <div className="flex items-center gap-2">
                  <h2 className="text-xl sm:text-2xl font-bold text-[#0d0d0d] dark:text-white">
                    {selectedCrop.name_vi}
                  </h2>
                  <span className="text-xs px-2 py-0.5 rounded-md bg-[#ffffff] dark:bg-[#282828] border border-[#e5e5e5] dark:border-[#383838] font-mono text-[#737373] dark:text-[#a3a3a3]">
                    {selectedCrop.id}
                  </span>
                </div>
                <p className="text-sm italic font-serif text-[#737373] dark:text-[#a3a3a3]">
                  {selectedCrop.scientific_name}
                </p>
              </div>

              <div className="flex items-center gap-2">
                <button
                  type="button"
                  onClick={() => handleAskAI(selectedCrop.name_vi)}
                  className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-semibold bg-[#0d0d0d] text-white dark:bg-white dark:text-black hover:opacity-90 transition-opacity cursor-pointer shadow-xs"
                >
                  <Sparkles className="w-3.5 h-3.5" />
                  <span>Hỏi AI cây này</span>
                </button>
                <button
                  type="button"
                  onClick={() => setSelectedCrop(null)}
                  className="p-1.5 rounded-xl hover:bg-[#e5e5e5] dark:hover:bg-[#2b2b2b] text-[#737373] hover:text-[#0d0d0d] dark:text-[#a3a3a3] dark:hover:text-white transition-colors cursor-pointer"
                >
                  <X className="w-5 h-5" />
                </button>
              </div>
            </div>

            {/* Modal Body */}
            <div className="p-5 overflow-y-auto space-y-6 flex-1 text-sm">
              {/* Ecology & Geography */}
              <div className="p-4 rounded-2xl bg-[#f9f9f9] dark:bg-[#1c1c1c] border border-[#e5e5e5] dark:border-[#262626] space-y-2">
                <div className="flex items-center gap-2 text-xs font-semibold uppercase tracking-wider text-[#737373] dark:text-[#8e8e8e]">
                  <MapPin className="w-3.5 h-3.5" />
                  <span>Đặc tính sinh thái & Vùng canh tác</span>
                </div>
                <p className="text-xs sm:text-sm text-[#0d0d0d] dark:text-[#ececec] leading-relaxed">
                  {selectedCrop.dac_tinh_sinh_thai}
                </p>
                <div className="text-xs text-[#737373] dark:text-[#8e8e8e] pt-1">
                  <strong>Địa bàn phổ biến:</strong>{' '}
                  {Array.isArray(selectedCrop.dia_ban_pho_bien)
                    ? selectedCrop.dia_ban_pho_bien.join(', ')
                    : selectedCrop.dia_ban_pho_bien}
                </div>
              </div>

              {/* Diseases Tabs */}
              {Array.isArray(selectedCrop.danh_sach_benh) && selectedCrop.danh_sach_benh.length > 0 && (
                <div className="space-y-4">
                  <div className="flex items-center justify-between">
                    <h4 className="text-xs font-semibold uppercase tracking-wider text-[#737373] dark:text-[#8e8e8e] flex items-center gap-1.5">
                      <AlertTriangle className="w-3.5 h-3.5" />
                      <span>Hồ sơ bệnh học ({selectedCrop.danh_sach_benh.length} bệnh)</span>
                    </h4>
                  </div>

                  {/* Tabs */}
                  <div className="flex items-center gap-2 overflow-x-auto pb-1 scrollbar-none border-b border-[#e5e5e5] dark:border-[#262626]">
                    {selectedCrop.danh_sach_benh.map((d, dIdx) => (
                      <button
                        key={dIdx}
                        onClick={() => setActiveDiseaseTab(dIdx)}
                        className={`px-3 py-1.5 text-xs font-medium border-b-2 transition-all shrink-0 cursor-pointer ${
                          activeDiseaseTab === dIdx
                            ? 'border-[#0d0d0d] text-[#0d0d0d] dark:border-white dark:text-white font-semibold'
                            : 'border-transparent text-[#737373] hover:text-[#0d0d0d] dark:text-[#8e8e8e] dark:hover:text-white'
                        }`}
                      >
                        {d.ten_benh}
                      </button>
                    ))}
                  </div>

                  {/* Active Disease Details */}
                  {selectedCrop.danh_sach_benh[activeDiseaseTab] && (
                    <div className="p-4 rounded-2xl border border-[#e5e5e5] dark:border-[#262626] bg-[#ffffff] dark:bg-[#1a1a1a] space-y-4">
                      <div className="flex flex-wrap items-center justify-between gap-2">
                        <div className="space-y-0.5">
                          <h5 className="font-bold text-base text-[#0d0d0d] dark:text-white">
                            {selectedCrop.danh_sach_benh[activeDiseaseTab].ten_benh}
                          </h5>
                          <div className="text-xs text-[#737373] dark:text-[#a3a3a3]">
                            <strong>Tác nhân:</strong>{' '}
                            {typeof selectedCrop.danh_sach_benh[activeDiseaseTab].tac_nhan === 'object'
                              ? `${selectedCrop.danh_sach_benh[activeDiseaseTab].tac_nhan.loai} (${selectedCrop.danh_sach_benh[activeDiseaseTab].tac_nhan.ten_khoa_hoc})`
                              : selectedCrop.danh_sach_benh[activeDiseaseTab].tac_nhan}
                          </div>
                        </div>
                        {getDangerBadge(selectedCrop.danh_sach_benh[activeDiseaseTab].muc_do_nguy_hiem)}
                      </div>

                      {/* Symptoms */}
                      <div className="space-y-1.5">
                        <span className="text-xs font-semibold text-[#0d0d0d] dark:text-white">
                          Triệu chứng điển hình:
                        </span>
                        <ul className="list-disc list-inside text-xs text-[#525252] dark:text-[#c4c4c4] space-y-1">
                          {Array.isArray(selectedCrop.danh_sach_benh[activeDiseaseTab].trieu_chung_dien_hinh) ? (
                            selectedCrop.danh_sach_benh[activeDiseaseTab].trieu_chung_dien_hinh.map((s, sIdx) => (
                              <li key={sIdx}>{s}</li>
                            ))
                          ) : (
                            <li>{selectedCrop.danh_sach_benh[activeDiseaseTab].trieu_chung_dien_hinh}</li>
                          )}
                        </ul>
                      </div>

                      {/* Double Diagnosis */}
                      <div className="p-3 rounded-xl bg-amber-50/70 dark:bg-amber-950/20 border border-amber-200/80 dark:border-amber-900/40 text-xs text-amber-900 dark:text-amber-200 space-y-1">
                        <span className="font-semibold flex items-center gap-1">
                          <ShieldCheck className="w-3.5 h-3.5 shrink-0" />
                          Bóc tách chẩn đoán kép:
                        </span>
                        <p>{selectedCrop.danh_sach_benh[activeDiseaseTab].phan_biet_chan_doan_kep}</p>
                      </div>

                      {/* Field Test */}
                      <div className="p-3 rounded-xl bg-blue-50/70 dark:bg-blue-950/20 border border-blue-200/80 dark:border-blue-900/40 text-xs text-blue-900 dark:text-blue-200 space-y-1">
                        <span className="font-semibold flex items-center gap-1">
                          <Activity className="w-3.5 h-3.5 shrink-0" />
                          Bài test thực địa:
                        </span>
                        <p>{selectedCrop.danh_sach_benh[activeDiseaseTab].kiem_tra_thuc_dia}</p>
                      </div>

                      {/* VietGAP Protocol */}
                      {selectedCrop.danh_sach_benh[activeDiseaseTab].phac_do_vietgap && (
                        <div className="p-3 rounded-xl bg-emerald-50/70 dark:bg-emerald-950/20 border border-emerald-200/80 dark:border-emerald-900/40 text-xs text-emerald-900 dark:text-emerald-200 space-y-1.5">
                          <span className="font-semibold flex items-center gap-1">
                            <CheckCircle2 className="w-3.5 h-3.5 shrink-0" />
                            Phác đồ điều trị VietGAP:
                          </span>
                          <div className="space-y-1">
                            <div>
                              <strong>Canh tác:</strong>{' '}
                              {selectedCrop.danh_sach_benh[activeDiseaseTab].phac_do_vietgap.canh_tac}
                            </div>
                            <div>
                              <strong>Sinh học:</strong>{' '}
                              {selectedCrop.danh_sach_benh[activeDiseaseTab].phac_do_vietgap.sinh_hoc}
                            </div>
                          </div>
                        </div>
                      )}

                      <div className="pt-2 flex justify-end">
                        <button
                          type="button"
                          onClick={() =>
                            handleAskAI(
                              selectedCrop.name_vi,
                              selectedCrop.danh_sach_benh[activeDiseaseTab].ten_benh
                            )
                          }
                          className="inline-flex items-center gap-1.5 text-xs font-semibold text-[#0d0d0d] dark:text-white hover:underline cursor-pointer"
                        >
                          <span>Hỏi sâu về bệnh này trên AI</span>
                          <ExternalLink className="w-3.5 h-3.5" />
                        </button>
                      </div>
                    </div>
                  )}
                </div>
              )}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
