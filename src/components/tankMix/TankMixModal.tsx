'use client';

import React, { useState, useMemo } from 'react';
import {
  X,
  FlaskConical,
  ShieldAlert,
  ShieldCheck,
  AlertTriangle,
  RotateCcw,
  Copy,
  Check,
  Search,
  Plus,
  Trash2,
  Sparkles,
  Info,
  Droplets,
  Layers,
  HelpCircle,
} from 'lucide-react';
import {
  POPULAR_PESTICIDES,
  simulateTankMix,
  PesticideCategory,
  PesticideItem,
} from '@/lib/tankMixSimulator';

interface TankMixModalProps {
  isOpen: boolean;
  onClose: () => void;
}

export default function TankMixModal({ isOpen, onClose }: TankMixModalProps) {
  const [selectedIds, setSelectedIds] = useState<string[]>([
    'mancozeb',
    'hexaconazole',
    'abamectin',
    'adjuvant_sticker',
  ]);
  const [tankVolume, setTankVolume] = useState<16 | 25 | 200>(16);
  const [selectedCategory, setSelectedCategory] = useState<string>('all');
  const [searchQuery, setSearchQuery] = useState('');
  const [copied, setCopied] = useState(false);

  // Filtered pesticide items
  const filteredPesticides = useMemo(() => {
    return POPULAR_PESTICIDES.filter((p) => {
      const matchCat = selectedCategory === 'all' || p.category === selectedCategory;
      const q = searchQuery.toLowerCase().trim();
      const matchSearch =
        !q ||
        p.name.toLowerCase().includes(q) ||
        p.activeIngredient.toLowerCase().includes(q) ||
        p.tradeNames.some((t) => t.toLowerCase().includes(q)) ||
        p.targetPests.toLowerCase().includes(q);
      return matchCat && matchSearch;
    });
  }, [selectedCategory, searchQuery]);

  // Simulation result computed in real-time
  const simulation = useMemo(() => {
    return simulateTankMix(selectedIds, tankVolume);
  }, [selectedIds, tankVolume]);

  const togglePesticide = (id: string) => {
    if (selectedIds.includes(id)) {
      setSelectedIds(selectedIds.filter((item) => item !== id));
    } else {
      setSelectedIds([...selectedIds, id]);
    }
  };

  const handleCopyPrescription = async () => {
    try {
      const selectedNames = simulation.doseBreakdown
        .map((d, i) => `${i + 1}. ${d.item.name}: ${d.calculatedDose}`)
        .join('\n');

      const walesText = simulation.walesSequence
        .map((w) => `• [${w.walesCode}] ${w.title}\n  -> ${w.instructions}`)
        .join('\n');

      const conflictText =
        simulation.conflicts.length > 0
          ? '\n\n⚠️ CẢNH BÁO XUNG ĐỘT:\n' +
            simulation.conflicts
              .map(
                (c) =>
                  `[${c.title}]\n- Hậu quả: ${c.consequence}\n- Giải pháp: ${c.recommendation}`
              )
              .join('\n')
          : '\n\n✅ KẾT LUẬN: Hỗn hợp tương thích an toàn khi tuân thủ WALES.';

      const prescription = `🌾 PHÁC ĐỒ PHA TRỘN THUỐC BVTV CHUẨN WALES (AGRIVISION)
Dung tích bình: ${tankVolume} Lít
Trạng thái: ${simulation.statusBadge.text}

📋 DANH MỤC THUỐC & LIỀU LƯỢNG CHO BÌNH ${tankVolume}L:
${selectedNames}

🧪 THỨ TỰ HÒA TAN CHUẨN QUỐC TẾ WALES:
${walesText}
${conflictText}

💡 Khuyến cáo: Hòa tan từng loại vào ca nhỏ trước khi đổ chung vào bình đã có sẵn 1/2 nước!`;

      await navigator.clipboard.writeText(prescription);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch {
      setCopied(false);
    }
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-5 bg-black/70 backdrop-blur-sm animate-in fade-in duration-200">
      <div
        onClick={(e) => e.stopPropagation()}
        className="w-full max-w-6xl max-h-[92vh] flex flex-col bg-white dark:bg-[#121212] rounded-3xl border border-[#e5e5e5] dark:border-[#262626] shadow-2xl overflow-hidden text-[#0d0d0d] dark:text-[#ececec]"
      >
        {/* Top Header Bar */}
        <div className="px-5 py-4 border-b border-[#e5e5e5] dark:border-[#262626] flex items-center justify-between bg-[#fafafa] dark:bg-[#171717] shrink-0">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-2xl bg-emerald-600/10 dark:bg-emerald-500/20 text-emerald-600 dark:text-emerald-400 flex items-center justify-center border border-emerald-500/30">
              <FlaskConical className="w-5 h-5" strokeWidth={1.5} />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h2 className="text-base sm:text-lg font-bold tracking-tight text-[#0d0d0d] dark:text-white">
                  Bình Phun Ảo Mô Phỏng Xung Đột Thuốc BVTV
                </h2>
                <span className="hidden sm:inline-block px-2 py-0.5 text-[11px] font-mono font-medium rounded-full bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300 border border-emerald-300 dark:border-emerald-800">
                  Chuẩn Quốc Tế WALES
                </span>
              </div>
              <p className="text-xs text-[#737373] dark:text-[#a3a3a3]">
                Ma trận kiểm tra kết tủa, cháy lá, kiềm hóa & thứ tự hòa tan an toàn cho nhà nông
              </p>
            </div>
          </div>

          <div className="flex items-center gap-2">
            <button
              type="button"
              onClick={onClose}
              className="p-2 rounded-xl text-[#737373] hover:text-[#0d0d0d] dark:hover:text-white hover:bg-[#e5e5e5]/60 dark:hover:bg-[#262626] transition-colors cursor-pointer"
              title="Đóng (Esc)"
            >
              <X className="w-5 h-5" strokeWidth={1.5} />
            </button>
          </div>
        </div>

        {/* Tank Volume Selector & Quick Scenario Presets */}
        <div className="px-5 py-3 border-b border-[#e5e5e5] dark:border-[#262626] bg-white dark:bg-[#141414] flex flex-wrap items-center justify-between gap-3 text-xs shrink-0">
          {/* Tank Volume Switcher */}
          <div className="flex items-center gap-2">
            <span className="font-semibold text-[#525252] dark:text-[#a3a3a3] flex items-center gap-1.5">
              <Droplets className="w-4 h-4 text-emerald-600 dark:text-emerald-400" strokeWidth={1.5} />
              Dung tích bình:
            </span>
            <div className="inline-flex rounded-xl bg-[#f0f0f0] dark:bg-[#202020] p-1 border border-[#e5e5e5] dark:border-[#333]">
              {[16, 25, 200].map((vol) => (
                <button
                  key={vol}
                  type="button"
                  onClick={() => setTankVolume(vol as 16 | 25 | 200)}
                  className={`px-3 py-1.5 rounded-lg font-medium transition-all cursor-pointer ${
                    tankVolume === vol
                      ? 'bg-white dark:bg-[#2e2e2e] text-[#0d0d0d] dark:text-white shadow-xs font-bold'
                      : 'text-[#737373] dark:text-[#a3a3a3] hover:text-[#0d0d0d] dark:hover:text-white'
                  }`}
                >
                  {vol === 200 ? 'Phuy 200L' : `${vol} Lít`}
                </button>
              ))}
            </div>
          </div>

          {/* Quick Scenario Buttons */}
          <div className="flex flex-wrap items-center gap-1.5">
            <span className="text-[#888] hidden md:inline">Thử nhanh ca bệnh:</span>
            <button
              type="button"
              onClick={() => setSelectedIds(['copper_hydroxide', 'sulfur_elemental'])}
              className="px-2.5 py-1 rounded-lg bg-red-50 dark:bg-red-950/40 text-red-700 dark:text-red-300 border border-red-200 dark:border-red-900/40 hover:bg-red-100 transition-colors cursor-pointer"
            >
              🔴 Thử Đồng + Lưu huỳnh (Cấm)
            </button>
            <button
              type="button"
              onClick={() => setSelectedIds(['calcium_boron', 'mkp_phosphate'])}
              className="px-2.5 py-1 rounded-lg bg-red-50 dark:bg-red-950/40 text-red-700 dark:text-red-300 border border-red-200 dark:border-red-900/40 hover:bg-red-100 transition-colors cursor-pointer"
            >
              🔴 Thử Canxi + Phốt phát (Nghẹt béc)
            </button>
            <button
              type="button"
              onClick={() =>
                setSelectedIds([
                  'mancozeb',
                  'hexaconazole',
                  'abamectin',
                  'adjuvant_sticker',
                ])
              }
              className="px-2.5 py-1 rounded-lg bg-emerald-50 dark:bg-emerald-950/40 text-emerald-700 dark:text-emerald-300 border border-emerald-200 dark:border-emerald-900/40 hover:bg-emerald-100 transition-colors cursor-pointer"
            >
              🟢 Thử Phác Đồ Chuẩn 4 Món (An toàn)
            </button>
          </div>
        </div>

        {/* Main Content: Split 2 Panes */}
        <div className="flex-1 grid grid-cols-1 lg:grid-cols-12 overflow-hidden min-h-0">
          {/* LEFT PANE: Active Ingredients Selector (5 Cols) */}
          <div className="lg:col-span-5 border-r border-[#e5e5e5] dark:border-[#262626] flex flex-col bg-[#fcfcfc] dark:bg-[#141414] min-h-0">
            {/* Search & Filter Tabs */}
            <div className="p-3 border-b border-[#e5e5e5] dark:border-[#262626] space-y-2 shrink-0">
              <div className="relative">
                <Search
                  className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-[#888]"
                  strokeWidth={1.5}
                />
                <input
                  type="text"
                  placeholder="Tìm hoạt chất, tên thương mại (Coc 85, Anvil, Ridomil...)"
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  className="w-full pl-9 pr-3 py-2 rounded-xl text-xs bg-white dark:bg-[#1f1f1f] border border-[#e5e5e5] dark:border-[#333] focus:outline-hidden focus:border-emerald-500 text-[#0d0d0d] dark:text-[#ececec]"
                />
              </div>

              {/* Category Pills */}
              <div className="flex items-center gap-1.5 overflow-x-auto pb-1 text-[11px] no-scrollbar">
                {[
                  { id: 'all', label: 'Tất cả' },
                  { id: 'fungicide', label: 'Trừ nấm bệnh' },
                  { id: 'insecticide', label: 'Trừ sâu rầy' },
                  { id: 'foliar_fertilizer', label: 'Phân bón lá' },
                  { id: 'bio_control', label: 'Vi sinh' },
                  { id: 'adjuvant', label: 'Bám dính' },
                ].map((cat) => (
                  <button
                    key={cat.id}
                    type="button"
                    onClick={() => setSelectedCategory(cat.id)}
                    className={`px-2.5 py-1 rounded-full whitespace-nowrap transition-colors cursor-pointer ${
                      selectedCategory === cat.id
                        ? 'bg-[#0d0d0d] text-white dark:bg-white dark:text-black font-semibold'
                        : 'bg-[#eeeeee] dark:bg-[#252525] text-[#555] dark:text-[#a3a3a3] hover:text-black dark:hover:text-white'
                    }`}
                  >
                    {cat.label}
                  </button>
                ))}
              </div>
            </div>

            {/* List of Available Pesticides */}
            <div className="flex-1 overflow-y-auto p-3 space-y-2 divide-y-0">
              <div className="flex items-center justify-between text-xs text-[#737373] px-1 pb-1">
                <span>Chọn thuốc muốn pha vào bình:</span>
                <span className="font-semibold text-emerald-600 dark:text-emerald-400">
                  Đã chọn: {selectedIds.length} loại
                </span>
              </div>

              {filteredPesticides.map((p) => {
                const isSelected = selectedIds.includes(p.id);
                return (
                  <div
                    key={p.id}
                    onClick={() => togglePesticide(p.id)}
                    className={`p-3 rounded-2xl border transition-all cursor-pointer flex items-start gap-3 ${
                      isSelected
                        ? 'bg-emerald-50/70 dark:bg-emerald-950/30 border-emerald-500/60 shadow-xs'
                        : 'bg-white dark:bg-[#1a1a1a] border-[#e5e5e5] dark:border-[#2a2a2a] hover:border-[#ccc] dark:hover:border-[#444]'
                    }`}
                  >
                    <input
                      type="checkbox"
                      checked={isSelected}
                      onChange={() => {}}
                      className="mt-1 w-4 h-4 rounded text-emerald-600 focus:ring-0 cursor-pointer"
                    />

                    <div className="flex-1 min-w-0">
                      <div className="flex items-center justify-between gap-1">
                        <h4 className="text-xs sm:text-sm font-semibold truncate text-[#0d0d0d] dark:text-white">
                          {p.name}
                        </h4>
                        <span
                          className={`text-[10px] font-mono px-1.5 py-0.5 rounded font-bold uppercase shrink-0 ${
                            p.formulation.includes('W')
                              ? 'bg-blue-100 text-blue-800 dark:bg-blue-950 dark:text-blue-300'
                              : p.formulation === 'EC'
                              ? 'bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-300'
                              : p.formulation === 'SC' || p.formulation === 'SL'
                              ? 'bg-cyan-100 text-cyan-800 dark:bg-cyan-950 dark:text-cyan-300'
                              : 'bg-purple-100 text-purple-800 dark:bg-purple-950 dark:text-purple-300'
                          }`}
                        >
                          {p.formulation}
                        </span>
                      </div>

                      <div className="text-[11px] text-[#737373] dark:text-[#999] line-clamp-1 mt-0.5">
                        {p.tradeNames.join(', ')}
                      </div>

                      <div className="text-[11px] text-emerald-700 dark:text-emerald-400 font-medium mt-1">
                        Liều bình {tankVolume}L:{' '}
                        {tankVolume === 16
                          ? p.dosePer16L
                          : tankVolume === 25
                          ? p.dosePer25L
                          : p.dosePer200L}
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>

          {/* RIGHT PANE: Interactive Virtual Tank Visualizer & WALES Steps (7 Cols) */}
          <div className="lg:col-span-7 flex flex-col bg-white dark:bg-[#121212] overflow-y-auto p-4 sm:p-6 space-y-5">
            {/* Simulation Status Banner */}
            <div
              className={`p-4 rounded-2xl border flex items-start gap-3.5 ${
                simulation.overallStatus === 'incompatible'
                  ? 'bg-red-50 dark:bg-red-950/40 border-red-300 dark:border-red-900/60 text-red-900 dark:text-red-200'
                  : simulation.overallStatus === 'conditional'
                  ? 'bg-amber-50 dark:bg-amber-950/40 border-amber-300 dark:border-amber-900/60 text-amber-900 dark:text-amber-200'
                  : 'bg-emerald-50 dark:bg-emerald-950/40 border-emerald-300 dark:border-emerald-900/60 text-emerald-900 dark:text-emerald-200'
              }`}
            >
              <div className="mt-0.5 shrink-0">
                {simulation.overallStatus === 'incompatible' ? (
                  <ShieldAlert className="w-6 h-6 text-red-600 dark:text-red-400" strokeWidth={1.5} />
                ) : simulation.overallStatus === 'conditional' ? (
                  <AlertTriangle className="w-6 h-6 text-amber-600 dark:text-amber-400" strokeWidth={1.5} />
                ) : (
                  <ShieldCheck className="w-6 h-6 text-emerald-600 dark:text-emerald-400" strokeWidth={1.5} />
                )}
              </div>
              <div className="flex-1">
                <div className="font-bold text-sm sm:text-base flex items-center justify-between">
                  <span>{simulation.statusBadge.text}</span>
                  <span className="text-xs font-mono px-2 py-0.5 rounded-full bg-white/60 dark:bg-black/40">
                    Bình {tankVolume}L
                  </span>
                </div>
                <p className="text-xs mt-1 leading-relaxed opacity-90">
                  {simulation.solutionVisual.description}
                </p>
              </div>
            </div>

            {/* Interactive Virtual Tank Graphic HUD */}
            <div className="p-4 sm:p-5 rounded-3xl bg-[#090d16] border border-[#1e293b] text-white shadow-xl space-y-4">
              <div className="flex items-center justify-between border-b border-white/10 pb-3">
                <div className="flex items-center gap-2">
                  <div
                    className="w-3 h-3 rounded-full animate-ping"
                    style={{ backgroundColor: simulation.solutionVisual.glowColor }}
                  />
                  <span className="font-mono text-xs font-bold tracking-wider text-[#00F2FE]">
                    MẶT CẮT BÌNH PHUN ẢO (VIRTUAL SPRAY TANK HUD)
                  </span>
                </div>
                <span className="text-xs font-mono text-[#10B981]">
                  Mực nước: {tankVolume} Lít (100%)
                </span>
              </div>

              {/* The Virtual Tank Chamber Canvas Visualization */}
              <div className="relative w-full h-48 sm:h-56 rounded-2xl bg-[#040812] border border-white/15 overflow-hidden flex flex-col justify-end p-4">
                {/* Tank Liquid Fill */}
                <div
                  className="absolute inset-x-0 bottom-0 transition-all duration-700 rounded-b-xl flex flex-col justify-end"
                  style={{
                    height: '85%',
                    backgroundColor: simulation.solutionVisual.liquidColor,
                    boxShadow: `0 0 35px ${simulation.solutionVisual.glowColor} inset`,
                  }}
                >
                  {/* Fluid Surface Wave Effect */}
                  <div className="w-full h-2 bg-white/30 backdrop-blur-xs animate-pulse" />

                  {/* Bubbles or Precipitates particles */}
                  {simulation.solutionVisual.hasPrecipitation ? (
                    <div className="p-3 text-center space-y-1">
                      <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-red-950/80 border border-red-500/80 text-red-300 text-xs font-mono animate-pulse">
                        <AlertTriangle className="w-3.5 h-3.5" />
                        <span>KẾT TỦA VÓN CỤC LẮNG ĐÁY BÌNH</span>
                      </div>
                      <div className="flex justify-center gap-3 pt-2 opacity-80">
                        <span className="w-2.5 h-2.5 rounded-full bg-red-600 animate-bounce" />
                        <span className="w-3 h-3 rounded-full bg-stone-700 animate-pulse" />
                        <span className="w-2 h-2 rounded-full bg-red-400 animate-bounce" />
                        <span className="w-3.5 h-3.5 rounded-full bg-black border border-red-500" />
                        <span className="w-2 h-2 rounded-full bg-stone-600 animate-ping" />
                      </div>
                    </div>
                  ) : simulation.solutionVisual.hasOilSeparation ? (
                    <div className="p-3 text-center">
                      <span className="inline-flex items-center gap-1 px-3 py-1 rounded-full bg-amber-950/80 border border-amber-500 text-amber-300 text-xs font-mono">
                        Váng dầu khoáng lơ lửng mặt nước
                      </span>
                    </div>
                  ) : (
                    <div className="p-3 text-center space-y-1">
                      <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-950/80 border border-emerald-500 text-emerald-300 text-xs font-mono">
                        <Check className="w-3.5 h-3.5" />
                        <span>Dung dịch đồng nhất • Hòa tan 100%</span>
                      </span>
                    </div>
                  )}
                </div>

                {/* Volume measurement scale lines */}
                <div className="absolute right-3 inset-y-4 flex flex-col justify-between items-end text-[10px] font-mono text-white/50 pointer-events-none">
                  <span>{tankVolume}L —</span>
                  <span>{Math.round(tankVolume * 0.75)}L —</span>
                  <span>{Math.round(tankVolume * 0.5)}L —</span>
                  <span>{Math.round(tankVolume * 0.25)}L —</span>
                  <span>0L —</span>
                </div>
              </div>

              <div className="flex flex-wrap items-center justify-between text-xs text-white/80 gap-2">
                <span>
                  Trạng thái quan sát:{' '}
                  <strong className="text-white">{simulation.solutionVisual.statusText}</strong>
                </span>
                <button
                  type="button"
                  onClick={handleCopyPrescription}
                  className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-white/10 hover:bg-white/20 text-white font-medium transition-colors cursor-pointer border border-white/20 text-xs"
                >
                  {copied ? (
                    <>
                      <Check className="w-3.5 h-3.5 text-emerald-400" />
                      <span>Đã sao chép phác đồ!</span>
                    </>
                  ) : (
                    <>
                      <Copy className="w-3.5 h-3.5" />
                      <span>Sao chép phác đồ cho nông dân</span>
                    </>
                  )}
                </button>
              </div>
            </div>

            {/* Conflict Warnings Section (If Any) */}
            {simulation.conflicts.length > 0 && (
              <div className="space-y-3">
                <h3 className="text-sm font-bold tracking-tight text-red-600 dark:text-red-400 flex items-center gap-1.5">
                  <ShieldAlert className="w-4 h-4" strokeWidth={1.5} />
                  <span>Chi tiết xung đột hóa sinh đã phát hiện ({simulation.conflicts.length} cặp):</span>
                </h3>

                <div className="space-y-2.5">
                  {simulation.conflicts.map((conf, cIdx) => (
                    <div
                      key={cIdx}
                      className="p-4 rounded-2xl border border-red-300 dark:border-red-900/60 bg-red-50/50 dark:bg-red-950/20 space-y-2"
                    >
                      <div className="flex items-center justify-between gap-2">
                        <span className="font-bold text-xs sm:text-sm text-red-900 dark:text-red-300">
                          {conf.title}
                        </span>
                        <span className="text-[11px] font-mono px-2 py-0.5 rounded bg-red-200 dark:bg-red-900 text-red-900 dark:text-red-200">
                          {conf.itemA.name} ✖ {conf.itemB.name}
                        </span>
                      </div>

                      <div className="text-xs text-[#525252] dark:text-[#ccc] space-y-1 leading-relaxed">
                        <p>
                          <strong className="text-[#0d0d0d] dark:text-white">Cơ chế:</strong>{' '}
                          {conf.mechanism}
                        </p>
                        <p>
                          <strong className="text-red-700 dark:text-red-400">Hậu quả:</strong>{' '}
                          {conf.consequence}
                        </p>
                        <p>
                          <strong className="text-emerald-700 dark:text-emerald-400">
                            Khuyến cáo Khuyến nông:
                          </strong>{' '}
                          {conf.recommendation}
                        </p>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* WALES Pouring Sequence (Thứ tự hòa tan chuẩn quốc tế) */}
            <div className="space-y-3">
              <div className="flex items-center justify-between">
                <h3 className="text-sm font-bold tracking-tight text-[#0d0d0d] dark:text-white flex items-center gap-1.5">
                  <Layers className="w-4 h-4 text-emerald-600 dark:text-emerald-400" strokeWidth={1.5} />
                  <span>Quy trình đổ thuốc chuẩn WALES (Bình {tankVolume}L):</span>
                </h3>
                <span className="text-xs text-[#737373]">W ➔ A ➔ L ➔ E ➔ S</span>
              </div>

              <div className="space-y-2.5">
                {simulation.walesSequence.map((step) => {
                  const stepColor =
                    step.walesCode === 'W'
                      ? 'border-blue-300 dark:border-blue-900/60 bg-blue-50/50 dark:bg-blue-950/20'
                      : step.walesCode === 'A'
                      ? 'border-stone-300 dark:border-stone-800 bg-stone-50 dark:bg-stone-900/40'
                      : step.walesCode === 'L'
                      ? 'border-cyan-300 dark:border-cyan-900/60 bg-cyan-50/50 dark:bg-cyan-950/20'
                      : step.walesCode === 'E'
                      ? 'border-amber-300 dark:border-amber-900/60 bg-amber-50/50 dark:bg-amber-950/20'
                      : 'border-purple-300 dark:border-purple-900/60 bg-purple-50/50 dark:bg-purple-950/20';

                  const badgeBg =
                    step.walesCode === 'W'
                      ? 'bg-blue-600 text-white'
                      : step.walesCode === 'A'
                      ? 'bg-stone-700 text-white'
                      : step.walesCode === 'L'
                      ? 'bg-cyan-600 text-white'
                      : step.walesCode === 'E'
                      ? 'bg-amber-600 text-white'
                      : 'bg-purple-600 text-white';

                  return (
                    <div
                      key={step.stepIndex}
                      className={`p-3.5 rounded-2xl border transition-all ${stepColor}`}
                    >
                      <div className="flex items-center gap-2.5">
                        <span
                          className={`w-6 h-6 rounded-lg flex items-center justify-center font-bold text-xs shrink-0 ${badgeBg}`}
                        >
                          {step.walesCode}
                        </span>
                        <span className="font-bold text-xs sm:text-sm text-[#0d0d0d] dark:text-white flex-1">
                          {step.title}
                        </span>
                      </div>

                      <p className="text-xs text-[#525252] dark:text-[#a3a3a3] mt-1.5 pl-8 leading-relaxed">
                        {step.instructions}
                      </p>

                      {step.items.length > 0 && (
                        <div className="mt-2 pl-8 flex flex-wrap gap-2">
                          {step.items.map((item) => {
                            const dose =
                              tankVolume === 16
                                ? item.dosePer16L
                                : tankVolume === 25
                                ? item.dosePer25L
                                : item.dosePer200L;
                            return (
                              <span
                                key={item.id}
                                className="inline-flex items-center gap-1 text-[11px] font-mono px-2 py-0.5 rounded-md bg-white dark:bg-[#202020] border border-[#e5e5e5] dark:border-[#383838] text-[#0d0d0d] dark:text-white"
                              >
                                <strong>{item.name}</strong>: {dose}
                              </span>
                            );
                          })}
                        </div>
                      )}
                    </div>
                  );
                })}
              </div>
            </div>

            {/* General Advice Accordion / Tips */}
            <div className="p-4 rounded-2xl bg-[#f8f8f8] dark:bg-[#181818] border border-[#e5e5e5] dark:border-[#2a2a2a] text-xs space-y-1.5">
              <div className="font-semibold text-[#0d0d0d] dark:text-white flex items-center gap-1.5">
                <Info className="w-4 h-4 text-emerald-600 dark:text-emerald-400" strokeWidth={1.5} />
                <span>3 Lời khuyên vàng của Bác sĩ cây trồng AgriVision:</span>
              </div>
              <ul className="space-y-1 pl-5 list-disc text-[#666] dark:text-[#a3a3a3] leading-relaxed">
                {simulation.generalAdvices.map((adv, idx) => (
                  <li key={idx}>{adv}</li>
                ))}
              </ul>
            </div>
          </div>
        </div>

        {/* Bottom Footer Actions */}
        <div className="px-5 py-3 border-t border-[#e5e5e5] dark:border-[#262626] bg-[#fafafa] dark:bg-[#161616] flex flex-wrap items-center justify-between gap-3 text-xs shrink-0">
          <div className="flex items-center gap-2 text-[#737373]">
            <span>
              Tổng số thuốc trong bình:{' '}
              <strong className="text-[#0d0d0d] dark:text-white">{selectedIds.length}</strong>
            </span>
            <span>•</span>
            <button
              type="button"
              onClick={() => setSelectedIds([])}
              className="text-red-600 dark:text-red-400 hover:underline cursor-pointer"
            >
              Xóa sạch bình
            </button>
          </div>

          <div className="flex items-center gap-2">
            <button
              type="button"
              onClick={handleCopyPrescription}
              className="px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-medium transition-colors cursor-pointer flex items-center gap-1.5 shadow-xs"
            >
              {copied ? (
                <>
                  <Check className="w-4 h-4" />
                  <span>Đã sao chép!</span>
                </>
              ) : (
                <>
                  <Copy className="w-4 h-4" strokeWidth={1.5} />
                  <span>Sao chép phác đồ pha</span>
                </>
              )}
            </button>
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 rounded-xl border border-[#e5e5e5] dark:border-[#333] hover:bg-[#eaeaea] dark:hover:bg-[#252525] text-[#0d0d0d] dark:text-white font-medium transition-colors cursor-pointer"
            >
              Đóng
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
