'use client';

import React, { useState } from 'react';
import { useChat } from '@/context/ChatContext';
import FloatingInputIsland from '@/components/input/FloatingInputIsland';
import { Sprout, Leaf, ShieldAlert, X } from 'lucide-react';

export default function EmptyState() {
  const { sendMessage } = useChat();

  const [suggestions, setSuggestions] = useState([
    {
      id: 'disease',
      icon: <ShieldAlert className="w-4 h-4 text-[#10a37f]" />,
      text: 'Chẩn đoán bệnh cây',
      prompt: 'Lá cây bị đốm vàng viền nâu, cháy từ chóp vào là bệnh gì và cách chữa?',
    },
    {
      id: 'nutrition',
      icon: <Leaf className="w-4 h-4 text-[#10a37f]" />,
      text: 'Chăm sóc & Dinh dưỡng',
      prompt: 'Quy trình bón phân và bổ sung vi lượng cho cây ăn trái giai đoạn ra hoa',
    },
    {
      id: 'pest',
      icon: <Sprout className="w-4 h-4 text-[#10a37f]" />,
      text: 'Phòng trừ sâu rầy',
      prompt: 'Biện pháp sinh học phòng ngừa rầy phấn trắng và bọ trĩ hiệu quả',
    },
  ]);

  const dismissSuggestion = (id: string, e: React.MouseEvent) => {
    e.stopPropagation();
    setSuggestions((prev) => prev.filter((s) => s.id !== id));
  };

  return (
    <div className="flex-1 flex flex-col justify-center items-center px-4 w-full max-w-3xl mx-auto">
      {/* Hero Greeting */}
      <div className="text-center mb-8">
        <h1 className="text-3xl sm:text-4xl font-semibold text-[#ececec] dark:text-[#ececec] tracking-tight">
          AgriVision — Trợ lý AI Cây Trồng
        </h1>
        <p className="text-sm text-[#8e8e8e] mt-2">
          Nhập mô tả triệu chứng hoặc đính kèm ảnh để chẩn đoán dịch bệnh tức thì
        </p>
      </div>

      {/* Center Input Box */}
      <div className="w-full mb-6">
        <FloatingInputIsland />
      </div>

      {/* Quick Action Suggestions */}
      {suggestions.length > 0 && (
        <div className="w-full flex flex-col sm:flex-row flex-wrap items-center justify-center gap-2.5">
          {suggestions.map((item) => (
            <div
              key={item.id}
              onClick={() => sendMessage(item.prompt)}
              className="group flex items-center justify-between gap-3 px-3.5 py-2 rounded-full border border-[#383838] bg-[#212121] hover:bg-[#2a2a2a] text-xs font-medium text-[#ececec] cursor-pointer transition-all hover:scale-[1.01]"
            >
              <div className="flex items-center gap-2">
                {item.icon}
                <span>{item.text}</span>
              </div>
              <button
                type="button"
                onClick={(e) => dismissSuggestion(item.id, e)}
                title="Đóng gợi ý"
                className="opacity-0 group-hover:opacity-100 hover:text-white text-[#8e8e8e] transition-opacity p-0.5 rounded-full"
              >
                <X className="w-3 h-3" />
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
