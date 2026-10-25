'use client';

import React, { useState, useEffect } from 'react';
import { useChat } from '@/context/ChatContext';
import { X, Check, Sparkles } from 'lucide-react';

export default function UpgradeModal() {
  const { isUpgradeOpen, setIsUpgradeOpen } = useChat();
  const [tab, setTab] = useState<'personal' | 'business'>('personal');

  useEffect(() => {
    function handleKeyDown(e: KeyboardEvent) {
      if (e.key === 'Escape') {
        setIsUpgradeOpen(false);
      }
    }
    if (isUpgradeOpen) {
      window.addEventListener('keydown', handleKeyDown);
    }
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isUpgradeOpen, setIsUpgradeOpen]);

  if (!isUpgradeOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/50 backdrop-blur-xs animate-in fade-in duration-150">
      <div className="w-full max-w-2xl bg-[#ffffff] dark:bg-[#212121] border border-[#e5e5e5] dark:border-[#383838] rounded-3xl shadow-2xl p-6 sm:p-8 text-[#0d0d0d] dark:text-[#ececec] relative">
        {/* Close Button */}
        <button
          onClick={() => setIsUpgradeOpen(false)}
          className="absolute top-5 right-5 p-2 rounded-full hover:bg-[#f0f0f0] dark:hover:bg-[#2f2f2f] text-[#5d5d5d] hover:text-[#0d0d0d] dark:text-[#8e8e8e] dark:hover:text-white transition-colors cursor-pointer"
        >
          <X className="w-5 h-5" strokeWidth={1.75} />
        </button>

        {/* Title */}
        <div className="text-center mb-6">
          <h2 className="text-2xl font-bold text-[#0d0d0d] dark:text-white mb-4">Upgrade your plan</h2>

          {/* Segmented Tab */}
          <div className="inline-flex p-1 rounded-full bg-[#f4f4f4] dark:bg-[#171717] border border-[#e5e5e5] dark:border-[#333333]">
            <button
              onClick={() => setTab('personal')}
              className={`px-5 py-1.5 rounded-full text-xs font-semibold transition-all cursor-pointer ${
                tab === 'personal'
                  ? 'bg-[#ffffff] text-[#0d0d0d] dark:bg-[#2f2f2f] dark:text-white shadow-xs'
                  : 'text-[#5d5d5d] dark:text-[#8e8e8e] hover:text-[#0d0d0d] dark:hover:text-white'
              }`}
            >
              Personal
            </button>
            <button
              onClick={() => setTab('business')}
              className={`px-5 py-1.5 rounded-full text-xs font-semibold transition-all cursor-pointer ${
                tab === 'business'
                  ? 'bg-[#ffffff] text-[#0d0d0d] dark:bg-[#2f2f2f] dark:text-white shadow-xs'
                  : 'text-[#5d5d5d] dark:text-[#8e8e8e] hover:text-[#0d0d0d] dark:hover:text-white'
              }`}
            >
              Business
            </button>
          </div>
        </div>

        {/* Pricing Cards Comparison Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {/* Card 1: Free Plan */}
          <div className="p-5 rounded-2xl border border-[#e5e5e5] dark:border-[#383838] bg-[#f9f9f9] dark:bg-[#1a1a1a] flex flex-col justify-between">
            <div>
              <div className="text-sm font-semibold text-[#0d0d0d] dark:text-white mb-1">Free</div>
              <div className="text-xl font-bold text-[#0d0d0d] dark:text-white mb-2">
                $0 <span className="text-xs font-normal text-[#8e8e8e]">/ month</span>
              </div>
              <p className="text-xs text-[#5d5d5d] dark:text-[#8e8e8e] mb-4">
                Hỗ trợ truy vấn triệu chứng và xử lý bệnh cây thông thường.
              </p>

              <div className="space-y-2 text-xs text-[#5d5d5d] dark:text-[#b4b4b4]">
                <div className="flex items-center gap-2">
                  <Check className="w-3.5 h-3.5 text-[#0d0d0d] dark:text-white shrink-0" strokeWidth={1.75} />
                  <span>Mô hình Gemini 3.8 Flash High</span>
                </div>
                <div className="flex items-center gap-2">
                  <Check className="w-3.5 h-3.5 text-[#0d0d0d] dark:text-white shrink-0" strokeWidth={1.75} />
                  <span>Chẩn đoán qua mô tả hình ảnh</span>
                </div>
              </div>
            </div>

            <button
              disabled
              className="mt-6 w-full py-2.5 rounded-xl bg-[#e5e5e5] dark:bg-[#2a2a2a] text-[#8e8e8e] text-xs font-semibold cursor-not-allowed border border-[#d4d4d4] dark:border-[#333333]"
            >
              Gói hiện tại
            </button>
          </div>

          {/* Card 2: Plus Plan */}
          <div className="p-5 rounded-2xl border border-[#0d0d0d] dark:border-white bg-[#ffffff] dark:bg-[#1f1f1f] flex flex-col justify-between relative shadow-lg">
            <div className="absolute top-4 right-4">
              <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-[#0d0d0d] text-white dark:bg-white dark:text-black">
                PRO
              </span>
            </div>

            <div>
              <div className="flex items-center gap-1.5 text-sm font-semibold text-[#0d0d0d] dark:text-white mb-1">
                <Sparkles className="w-4 h-4 text-[#0d0d0d] dark:text-white" strokeWidth={1.75} />
                <span>AgriVision Plus</span>
              </div>
              <div className="text-xl font-bold text-[#0d0d0d] dark:text-white mb-2">
                $20 <span className="text-xs font-normal text-[#8e8e8e]">/ month</span>
              </div>
              <p className="text-xs text-[#5d5d5d] dark:text-[#b4b4b4] mb-4">
                Tốc độ suy luận siêu tốc, phân tích hình ảnh chuyên sâu và hỗ trợ ưu tiên 24/7.
              </p>

              <div className="space-y-2 text-xs text-[#0d0d0d] dark:text-[#ececec]">
                <div className="flex items-center gap-2">
                  <Check className="w-3.5 h-3.5 text-[#0d0d0d] dark:text-white shrink-0" strokeWidth={1.75} />
                  <span>Ưu tiên suy luận sâu bệnh phức tạp</span>
                </div>
                <div className="flex items-center gap-2">
                  <Check className="w-3.5 h-3.5 text-[#0d0d0d] dark:text-white shrink-0" strokeWidth={1.75} />
                  <span>Nhận diện đa bệnh qua ảnh độ phân giải cao</span>
                </div>
                <div className="flex items-center gap-2">
                  <Check className="w-3.5 h-3.5 text-[#0d0d0d] dark:text-white shrink-0" strokeWidth={1.75} />
                  <span>Tài liệu hướng dẫn điều trị độc quyền</span>
                </div>
              </div>
            </div>

            <button
              onClick={() => {
                alert('Cảm ơn bạn đã lựa chọn AgriVision Plus! (Chế độ Demo)');
                setIsUpgradeOpen(false);
              }}
              className="mt-6 w-full py-2.5 rounded-xl bg-[#0d0d0d] hover:bg-black text-white dark:bg-white dark:hover:bg-gray-100 dark:text-black text-xs font-semibold shadow-md transition-all cursor-pointer"
            >
              Nâng cấp gói Plus
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
