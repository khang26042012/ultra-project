'use client';

import React, { useState, useEffect, useRef, useCallback } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import {
  Search,
  PanelLeft,
  SlidersHorizontal,
  Sparkles,
  ShieldCheck,
  AlertTriangle,
  Activity,
  ChevronRight,
  ExternalLink,
  X,
  MapPin,
  Leaf,
  CheckCircle2,
  Check,
} from 'lucide-react';
import { CropRecord } from '@/lib/cropSearch';

const CATEGORIES = [
  { id: 'all', label: 'Tất cả nhóm cây', icon: '🌱' },
  { id: 'fruit', label: 'Cây ăn trái đặc sản', icon: '🍊' },
  { id: 'grain', label: 'Lương thực & Hoa màu', icon: '🌾' },
  { id: 'veg', label: 'Rau củ & Gia vị', icon: '🥬' },
  { id: 'industrial', label: 'Cây công nghiệp', icon: '☕' },
  { id: 'medicinal_forest', label: 'Dược liệu & Lâm nghiệp', icon: '🌲' },
  { id: 'exotic_flower', label: 'Cây nhập khẩu & Hoa kiểng', icon: '🌐' },
];

const PAGE_SIZE = 20;

export default function CropsEncyclopediaPage() {
  const router = useRouter();
  const [crops, setCrops] = useState<CropRecord[]>([]);
  const [totalCount, setTotalCount] = useState(0);
  const [loadingInitial, setLoadingInitial] = useState(true);
  const [loadingMore, setLoadingMore] = useState(false);
  const [hasMore, setHasMore] = useState(true);

  const [searchQuery, setSearchQuery] = useState('');
  const [debouncedQuery, setDebouncedQuery] = useState('');
  const [selectedTopic, setSelectedTopic] = useState('all');
  const [isFilterOpen, setIsFilterOpen] = useState(false);

  const [selectedCrop, setSelectedCrop] = useState<CropRecord | null>(null);
  const [activeDiseaseTab, setActiveDiseaseTab] = useState(0);

  const filterMenuRef = useRef<HTMLDivElement>(null);
  const scrollContainerRef = useRef<HTMLDivElement>(null);
  const sentinelRef = useRef<HTMLDivElement>(null);

  // Debounce search query
  useEffect(() => {
    const timer = setTimeout(() => {
      setDebouncedQuery(searchQuery.trim());
    }, 250);
    return () => clearTimeout(timer);
  }, [searchQuery]);

  // Click outside filter dropdown to close
  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (
        filterMenuRef.current &&
        !filterMenuRef.current.contains(event.target as Node)
      ) {
        setIsFilterOpen(false);
      }
    }
    if (isFilterOpen) {
      document.addEventListener('mousedown', handleClickOutside);
    }
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
    };
  }, [isFilterOpen]);

  // Initial fetch on debouncedQuery or selectedTopic change
  useEffect(() => {
    let isCancelled = false;

    async function fetchInitialCrops() {
      setLoadingInitial(true);
      setHasMore(true);

      try {
        const url = `/api/crops?topic=${encodeURIComponent(
          selectedTopic
        )}&q=${encodeURIComponent(debouncedQuery)}&limit=${PAGE_SIZE}&offset=0`;
        const res = await fetch(url);
        const data = await res.json();

        if (!isCancelled && data.success) {
          const fetchedCrops = Array.isArray(data.crops) ? data.crops : [];
          setCrops(fetchedCrops);
          setTotalCount(data.total || 0);
          setHasMore(fetchedCrops.length < (data.total || 0));
        }
      } catch (err) {
        console.error('Failed to load initial crops:', err);
      } finally {
        if (!isCancelled) setLoadingInitial(false);
      }
    }

    fetchInitialCrops();

    return () => {
      isCancelled = true;
    };
  }, [debouncedQuery, selectedTopic]);

  // Load more for infinite scroll
  const loadMore = useCallback(async () => {
    if (loadingMore || !hasMore || loadingInitial) return;

    setLoadingMore(true);
    try {
      const offset = crops.length;
      const url = `/api/crops?topic=${encodeURIComponent(
        selectedTopic
      )}&q=${encodeURIComponent(
        debouncedQuery
      )}&limit=${PAGE_SIZE}&offset=${offset}`;
      const res = await fetch(url);
      const data = await res.json();

      if (data.success && Array.isArray(data.crops)) {
        const nextCrops = data.crops;
        if (nextCrops.length === 0) {
          setHasMore(false);
        } else {
          setCrops((prev) => {
            const combined = [...prev, ...nextCrops];
            if (combined.length >= (data.total || 0)) {
              setHasMore(false);
            }
            return combined;
          });
        }
      } else {
        setHasMore(false);
      }
    } catch (err) {
      console.error('Failed to load more crops:', err);
      setHasMore(false);
    } finally {
      setLoadingMore(false);
    }
  }, [
    loadingMore,
    hasMore,
    loadingInitial,
    crops.length,
    selectedTopic,
    debouncedQuery,
  ]);

  // IntersectionObserver for infinite scrolling sentinel
  useEffect(() => {
    const sentinel = sentinelRef.current;
    if (!sentinel) return;

    const observer = new IntersectionObserver(
      (entries) => {
        const first = entries[0];
        if (first.isIntersecting && hasMore && !loadingMore && !loadingInitial) {
          loadMore();
        }
      },
      {
        root: scrollContainerRef.current,
        threshold: 0.1,
        rootMargin: '250px',
      }
    );

    observer.observe(sentinel);
    return () => observer.disconnect();
  }, [loadMore, hasMore, loadingMore, loadingInitial]);

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

  const activeCategory = CATEGORIES.find((c) => c.id === selectedTopic);

  return (
    <div className="h-[100dvh] flex flex-col bg-[#ffffff] dark:bg-[#0f0f0f] text-[#0d0d0d] dark:text-[#ececec] overflow-hidden">
      {/* Top Minimalist Navigation Bar */}
      <header className="shrink-0 h-14 sm:h-16 bg-[#ffffff]/90 dark:bg-[#0f0f0f]/90 backdrop-blur-md border-b border-[#e5e5e5] dark:border-[#262626] z-20">
        <div className="max-w-6xl mx-auto px-4 h-full flex items-center justify-between gap-4">
          <div className="flex items-center gap-3">
            <Link
              href="/"
              className="inline-flex items-center gap-2 px-3 py-1.5 -ml-2 rounded-xl text-[#525252] hover:text-[#0d0d0d] dark:text-[#a3a3a3] dark:hover:text-white hover:bg-[#f4f4f4] dark:hover:bg-[#1a1a1a] transition-colors text-sm font-medium"
              title="Quay lại Trò chuyện"
            >
              <PanelLeft className="w-4 h-4" strokeWidth={1.5} />
              <span>Trò chuyện</span>
            </Link>

            <div className="h-4 w-px bg-[#e5e5e5] dark:bg-[#262626]" />

            <div className="flex items-center gap-2">
              <span className="w-6 h-6 rounded-lg bg-[#0d0d0d] text-white dark:bg-white dark:text-black flex items-center justify-center font-bold text-xs">
                AV
              </span>
              <span className="font-semibold text-sm sm:text-base tracking-tight text-[#0d0d0d] dark:text-white">
                Toàn Thư Bệnh Học Cây Trồng
              </span>
            </div>
          </div>

          <div className="flex items-center gap-2">
            <span className="text-[11px] font-mono px-2.5 py-1 rounded-full bg-[#f4f4f4] dark:bg-[#1f1f1f] border border-[#e5e5e5] dark:border-[#2f2f2f] text-[#737373] dark:text-[#a3a3a3]">
              1.500+ Loài Cây
            </span>
          </div>
        </div>
      </header>

      {/* Main Scrollable Viewport */}
      <div
        ref={scrollContainerRef}
        className="flex-1 overflow-y-auto min-h-0 bg-[#ffffff] dark:bg-[#0f0f0f]"
      >
        {/* Hero Section */}
        <section className="bg-gradient-to-b from-[#f9f9f9] to-[#ffffff] dark:from-[#141414] dark:to-[#0f0f0f] border-b border-[#e5e5e5] dark:border-[#262626] py-8 sm:py-10 px-4">
          <div className="max-w-4xl mx-auto text-center space-y-3">
            <h1 className="text-2xl sm:text-3xl lg:text-4xl font-bold tracking-tight text-[#0d0d0d] dark:text-white">
              Tra Cứu Lâm Sàng & Phổ Bệnh Học Thực Vật
            </h1>
            <p className="text-xs sm:text-sm text-[#737373] dark:text-[#a3a3a3] max-w-2xl mx-auto leading-relaxed">
              Công trình nghiên cứu khoa học của tác giả{' '}
              <strong className="text-[#0d0d0d] dark:text-white font-semibold">
                Phan Trọng Khang
              </strong>{' '}
              (Lớp 9¹, THCS Vĩnh An, tỉnh Vĩnh Long), chuẩn hóa 1.500+ loài cây
              trồng bản địa 63 tỉnh thành và quốc tế, 100% phác đồ sinh học
              VietGAP an toàn.
            </p>

            {/* Single Refined Metric Pill Line */}
            <div className="pt-2 flex justify-center">
              <div className="inline-flex flex-wrap items-center justify-center gap-2 sm:gap-3 px-4 py-1.5 rounded-full bg-[#f4f4f4] dark:bg-[#1a1a1a] border border-[#e5e5e5] dark:border-[#2a2a2a] text-xs text-[#525252] dark:text-[#a3a3a3] font-medium shadow-2xs">
                <span>1.500+ loài cây trồng</span>
                <span className="text-[#cccccc] dark:text-[#444444]">•</span>
                <span>3.000+ hồ sơ bệnh lâm sàng</span>
                <span className="text-[#cccccc] dark:text-[#444444]">•</span>
                <span className="text-emerald-600 dark:text-emerald-400 font-semibold">
                  100% Chuẩn VietGAP
                </span>
                <span className="text-[#cccccc] dark:text-[#444444]">•</span>
                <span className="text-blue-600 dark:text-blue-400 font-mono">
                  &lt; 2ms RAG nội tại
                </span>
              </div>
            </div>
          </div>
        </section>

        {/* Content Area */}
        <main className="max-w-6xl mx-auto px-4 py-6 sm:py-8 space-y-6">
          {/* Search & Single 'Bộ lọc' Filter Action */}
          <div className="max-w-2xl mx-auto space-y-2.5">
            <div className="relative flex items-center gap-2">
              {/* Rounded 24px Search Input */}
              <div className="relative flex-1">
                <Search
                  className="w-4 h-4 absolute left-4 top-1/2 -translate-y-1/2 text-[#8e8e8e]"
                  strokeWidth={1.5}
                />
                <input
                  type="text"
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  placeholder="Tìm theo tên cây (sầu riêng, bưởi, việt quất...), tên khoa học hoặc bệnh..."
                  className="w-full pl-11 pr-10 py-2.5 sm:py-3 rounded-[24px] bg-[#f9f9f9] dark:bg-[#1a1a1a] border border-[#e5e5e5] dark:border-[#2e2e2e] text-xs sm:text-sm text-[#0d0d0d] dark:text-white placeholder:text-[#8e8e8e] focus:outline-hidden focus:border-[#0d0d0d] dark:focus:border-white transition-colors shadow-2xs"
                />
                {searchQuery && (
                  <button
                    type="button"
                    onClick={() => setSearchQuery('')}
                    className="absolute right-3.5 top-1/2 -translate-y-1/2 text-[#8e8e8e] hover:text-[#0d0d0d] dark:hover:text-white p-1 rounded-full cursor-pointer"
                  >
                    <X className="w-3.5 h-3.5" strokeWidth={1.5} />
                  </button>
                )}
              </div>

              {/* Single 'Bộ lọc' Button */}
              <div className="relative" ref={filterMenuRef}>
                <button
                  type="button"
                  onClick={() => setIsFilterOpen((prev) => !prev)}
                  className={`inline-flex items-center gap-1.5 px-3.5 py-2.5 sm:py-3 rounded-[24px] text-xs font-medium border transition-all cursor-pointer shrink-0 ${
                    selectedTopic !== 'all'
                      ? 'bg-[#0d0d0d] text-white dark:bg-white dark:text-black border-transparent shadow-xs'
                      : 'bg-[#f9f9f9] hover:bg-[#eaeaea] text-[#0d0d0d] dark:bg-[#1a1a1a] dark:hover:bg-[#252525] dark:text-white border-[#e5e5e5] dark:border-[#2e2e2e]'
                  }`}
                >
                  <SlidersHorizontal className="w-3.5 h-3.5" strokeWidth={1.5} />
                  <span>Bộ lọc</span>
                  {selectedTopic !== 'all' && (
                    <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse ml-0.5" />
                  )}
                </button>

                {/* Filter Dropdown Popover */}
                {isFilterOpen && (
                  <div className="absolute right-0 top-full mt-2 w-64 p-1.5 rounded-2xl bg-[#ffffff] dark:bg-[#1a1a1a] border border-[#e5e5e5] dark:border-[#2e2e2e] shadow-xl z-30 space-y-0.5 animate-in fade-in zoom-in-95 duration-100">
                    <div className="px-3 py-1.5 text-[11px] font-semibold uppercase tracking-wider text-[#737373] dark:text-[#8e8e8e]">
                      Chọn nhóm cây trồng
                    </div>
                    {CATEGORIES.map((cat) => {
                      const isSelected = selectedTopic === cat.id;
                      return (
                        <button
                          key={cat.id}
                          type="button"
                          onClick={() => {
                            setSelectedTopic(cat.id);
                            setIsFilterOpen(false);
                          }}
                          className={`w-full flex items-center justify-between px-3 py-2 rounded-xl text-xs font-medium transition-colors text-left cursor-pointer ${
                            isSelected
                              ? 'bg-[#0d0d0d] text-white dark:bg-white dark:text-black font-semibold'
                              : 'text-[#0d0d0d] dark:text-[#ececec] hover:bg-[#f4f4f4] dark:hover:bg-[#252525]'
                          }`}
                        >
                          <span className="flex items-center gap-2">
                            <span>{cat.icon}</span>
                            <span>{cat.label}</span>
                          </span>
                          {isSelected && (
                            <Check className="w-3.5 h-3.5" strokeWidth={1.5} />
                          )}
                        </button>
                      );
                    })}
                  </div>
                )}
              </div>
            </div>

            {/* Active Filter Pill indicator */}
            {selectedTopic !== 'all' && activeCategory && (
              <div className="flex items-center gap-2 text-xs text-[#737373] dark:text-[#a3a3a3] px-1">
                <span>Đang lọc:</span>
                <span className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-[#f4f4f4] dark:bg-[#202020] text-[#0d0d0d] dark:text-white font-medium border border-[#e5e5e5] dark:border-[#333333]">
                  <span>{activeCategory.icon}</span>
                  <span>{activeCategory.label}</span>
                  <button
                    type="button"
                    onClick={() => setSelectedTopic('all')}
                    className="hover:text-red-500 ml-0.5 cursor-pointer"
                    title="Xóa bộ lọc"
                  >
                    <X className="w-3 h-3" strokeWidth={1.5} />
                  </button>
                </span>
                <span className="text-[11px] font-mono">
                  ({totalCount} kết quả)
                </span>
              </div>
            )}
          </div>

          {/* Crops Grid & States */}
          {loadingInitial ? (
            <div className="py-24 text-center space-y-3">
              <div className="w-7 h-7 mx-auto border-2 border-[#0d0d0d] dark:border-white border-t-transparent rounded-full animate-spin" />
              <p className="text-xs text-[#737373] dark:text-[#a3a3a3]">
                Đang nạp dữ liệu cây trồng...
              </p>
            </div>
          ) : crops.length === 0 ? (
            <div className="py-20 text-center space-y-3 border border-dashed border-[#e5e5e5] dark:border-[#2e2e2e] rounded-3xl">
              <Leaf className="w-10 h-10 mx-auto text-[#a3a3a3]" strokeWidth={1.5} />
              <h3 className="text-sm font-semibold text-[#0d0d0d] dark:text-white">
                Không tìm thấy cây trồng phù hợp
              </h3>
              <p className="text-xs text-[#737373] dark:text-[#a3a3a3] max-w-sm mx-auto">
                Thử tìm với tên thông dụng (sầu riêng, bưởi, cà phê, lúa, wasabi) hoặc chuyển nhóm cây sang Tất cả.
              </p>
            </div>
          ) : (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
              {crops.map((crop) => {
                const diseasesCount = Array.isArray(crop.danh_sach_benh)
                  ? crop.danh_sach_benh.length
                  : 0;
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
                        <span>Hồ sơ lâm sàng</span>
                        <ChevronRight className="w-3.5 h-3.5" strokeWidth={1.5} />
                      </span>
                    </div>
                  </div>
                );
              })}
            </div>
          )}

          {/* Infinite Scroll Sentinel */}
          {!loadingInitial && (
            <div
              ref={sentinelRef}
              className="py-6 flex items-center justify-center text-xs text-[#737373] dark:text-[#8e8e8e]"
            >
              {loadingMore ? (
                <div className="flex items-center gap-2">
                  <div className="w-4 h-4 border-2 border-current border-t-transparent rounded-full animate-spin" />
                  <span>Đang tải thêm cây trồng...</span>
                </div>
              ) : !hasMore && crops.length > 0 ? (
                <span className="font-mono text-[11px] text-[#a3a3a3] dark:text-[#525252]">
                  Đã tải trọn bộ {crops.length} / {totalCount} cây trồng
                </span>
              ) : null}
            </div>
          )}
        </main>
      </div>

      {/* Crop Pathology Profile Detail Modal */}
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
                  <Sparkles className="w-3.5 h-3.5" strokeWidth={1.5} />
                  <span>Hỏi AI cây này</span>
                </button>
                <button
                  type="button"
                  onClick={() => setSelectedCrop(null)}
                  className="p-1.5 rounded-xl hover:bg-[#e5e5e5] dark:hover:bg-[#2b2b2b] text-[#737373] hover:text-[#0d0d0d] dark:text-[#a3a3a3] dark:hover:text-white transition-colors cursor-pointer"
                >
                  <X className="w-5 h-5" strokeWidth={1.5} />
                </button>
              </div>
            </div>

            {/* Modal Body */}
            <div className="p-5 overflow-y-auto space-y-6 flex-1 text-sm">
              {/* Ecology & Geography */}
              <div className="p-4 rounded-2xl bg-[#f9f9f9] dark:bg-[#1c1c1c] border border-[#e5e5e5] dark:border-[#262626] space-y-2">
                <div className="flex items-center gap-2 text-xs font-semibold uppercase tracking-wider text-[#737373] dark:text-[#8e8e8e]">
                  <MapPin className="w-3.5 h-3.5" strokeWidth={1.5} />
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
              {Array.isArray(selectedCrop.danh_sach_benh) &&
                selectedCrop.danh_sach_benh.length > 0 && (
                  <div className="space-y-4">
                    <div className="flex items-center justify-between">
                      <h4 className="text-xs font-semibold uppercase tracking-wider text-[#737373] dark:text-[#8e8e8e] flex items-center gap-1.5">
                        <AlertTriangle className="w-3.5 h-3.5" strokeWidth={1.5} />
                        <span>
                          Hồ sơ bệnh học ({selectedCrop.danh_sach_benh.length} bệnh)
                        </span>
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
                              {typeof selectedCrop.danh_sach_benh[activeDiseaseTab]
                                .tac_nhan === 'object'
                                ? `${selectedCrop.danh_sach_benh[activeDiseaseTab].tac_nhan.loai} (${selectedCrop.danh_sach_benh[activeDiseaseTab].tac_nhan.ten_khoa_hoc})`
                                : selectedCrop.danh_sach_benh[activeDiseaseTab].tac_nhan}
                            </div>
                          </div>
                          {getDangerBadge(
                            selectedCrop.danh_sach_benh[activeDiseaseTab]
                              .muc_do_nguy_hiem
                          )}
                        </div>

                        {/* Symptoms */}
                        <div className="space-y-1.5">
                          <span className="text-xs font-semibold text-[#0d0d0d] dark:text-white">
                            Triệu chứng điển hình:
                          </span>
                          <ul className="list-disc list-inside text-xs text-[#525252] dark:text-[#c4c4c4] space-y-1">
                            {Array.isArray(
                              selectedCrop.danh_sach_benh[activeDiseaseTab]
                                .trieu_chung_dien_hinh
                            ) ? (
                              selectedCrop.danh_sach_benh[
                                activeDiseaseTab
                              ].trieu_chung_dien_hinh.map((s, sIdx) => (
                                <li key={sIdx}>{s}</li>
                              ))
                            ) : (
                              <li>
                                {
                                  selectedCrop.danh_sach_benh[activeDiseaseTab]
                                    .trieu_chung_dien_hinh
                                }
                              </li>
                            )}
                          </ul>
                        </div>

                        {/* Double Diagnosis */}
                        <div className="p-3 rounded-xl bg-amber-50/70 dark:bg-amber-950/20 border border-amber-200/80 dark:border-amber-900/40 text-xs text-amber-900 dark:text-amber-200 space-y-1">
                          <span className="font-semibold flex items-center gap-1">
                            <ShieldCheck
                              className="w-3.5 h-3.5 shrink-0"
                              strokeWidth={1.5}
                            />
                            Bóc tách chẩn đoán kép:
                          </span>
                          <p>
                            {
                              selectedCrop.danh_sach_benh[activeDiseaseTab]
                                .phan_biet_chan_doan_kep
                            }
                          </p>
                        </div>

                        {/* Field Test */}
                        <div className="p-3 rounded-xl bg-blue-50/70 dark:bg-blue-950/20 border border-blue-200/80 dark:border-blue-900/40 text-xs text-blue-900 dark:text-blue-200 space-y-1">
                          <span className="font-semibold flex items-center gap-1">
                            <Activity
                              className="w-3.5 h-3.5 shrink-0"
                              strokeWidth={1.5}
                            />
                            Bài test thực địa:
                          </span>
                          <p>
                            {
                              selectedCrop.danh_sach_benh[activeDiseaseTab]
                                .kiem_tra_thuc_dia
                            }
                          </p>
                        </div>

                        {/* VietGAP Protocol */}
                        {selectedCrop.danh_sach_benh[activeDiseaseTab]
                          .phac_do_vietgap && (
                          <div className="p-3 rounded-xl bg-emerald-50/70 dark:bg-emerald-950/20 border border-emerald-200/80 dark:border-emerald-900/40 text-xs text-emerald-900 dark:text-emerald-200 space-y-1.5">
                            <span className="font-semibold flex items-center gap-1">
                              <CheckCircle2
                                className="w-3.5 h-3.5 shrink-0"
                                strokeWidth={1.5}
                              />
                              Phác đồ điều trị VietGAP:
                            </span>
                            <div className="space-y-1">
                              <div>
                                <strong>Canh tác:</strong>{' '}
                                {
                                  selectedCrop.danh_sach_benh[activeDiseaseTab]
                                    .phac_do_vietgap.canh_tac
                                }
                              </div>
                              <div>
                                <strong>Sinh học:</strong>{' '}
                                {
                                  selectedCrop.danh_sach_benh[activeDiseaseTab]
                                    .phac_do_vietgap.sinh_hoc
                                }
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
                                selectedCrop.danh_sach_benh[activeDiseaseTab]
                                  .ten_benh
                              )
                            }
                            className="inline-flex items-center gap-1.5 text-xs font-semibold text-[#0d0d0d] dark:text-white hover:underline cursor-pointer"
                          >
                            <span>Hỏi sâu về bệnh này trên AI</span>
                            <ExternalLink
                              className="w-3.5 h-3.5"
                              strokeWidth={1.5}
                            />
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
