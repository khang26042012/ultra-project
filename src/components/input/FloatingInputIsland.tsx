'use client';

import React, { useState, useRef, useEffect } from 'react';
import { useChat } from '@/context/ChatContext';
import { Plus, ArrowUp } from 'lucide-react';
import gsap from 'gsap';

export default function FloatingInputIsland() {
  const { sendMessage, isStreaming } = useChat();
  const [input, setInput] = useState('');

  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const sendBtnRef = useRef<HTMLButtonElement>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);

  // Auto-resize textarea
  useEffect(() => {
    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto';
      const scrollHeight = textareaRef.current.scrollHeight;
      textareaRef.current.style.height = `${Math.min(scrollHeight, 180)}px`;
    }
  }, [input]);

  const handleSubmit = (e?: React.FormEvent) => {
    if (e) e.preventDefault();
    if (!input.trim() || isStreaming) return;

    // GSAP micro-interaction bounce on send button (60 FPS composited scale)
    if (sendBtnRef.current) {
      gsap.fromTo(
        sendBtnRef.current,
        { scale: 0.75 },
        { scale: 1, duration: 0.25, ease: 'back.out(2.5)' }
      );
    }

    sendMessage(input);
    setInput('');
    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto';
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit();
    }
  };

  const handleFileClick = () => {
    fileInputRef.current?.click();
  };

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const files = e.target.files;
    if (files && files.length > 0) {
      const fileName = files[0].name;
      setInput((prev) =>
        prev
          ? `${prev} [Đính kèm ảnh: ${fileName}]`
          : `[Đính kèm ảnh: ${fileName}] Mô tả triệu chứng cây trồng:`
      );
    }
  };

  return (
    <div className="w-full max-w-3xl mx-auto px-4 pb-4 select-none">
      <div className="relative rounded-[28px] bg-[#2f2f2f] border border-[#3e3e3e] shadow-xl p-3 focus-within:border-[#525252] transition-all">
        {/* Hidden File Input for Image Upload */}
        <input
          ref={fileInputRef}
          type="file"
          accept="image/*,.pdf,.doc,.docx"
          onChange={handleFileChange}
          className="hidden"
        />

        {/* Textarea */}
        <textarea
          ref={textareaRef}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Nhập câu hỏi hoặc mô tả triệu chứng bệnh cây..."
          rows={1}
          className="w-full bg-transparent text-[#ececec] placeholder-[#8e8e8e] resize-none outline-none text-[15px] leading-relaxed px-2 py-1 max-h-[180px] overflow-y-auto no-scrollbar"
        />

        {/* Action Controls Bar */}
        <div className="flex items-center justify-between pt-2 px-1">
          {/* Left: Nút đính kèm tệp / ảnh */}
          <div className="flex items-center gap-2">
            <button
              type="button"
              onClick={handleFileClick}
              title="Đính kèm ảnh hoặc tài liệu cây trồng"
              className="p-1.5 rounded-full hover:bg-[#3d3d3d] text-[#b4b4b4] hover:text-white transition-colors cursor-pointer"
            >
              <Plus className="w-4 h-4" />
            </button>
          </div>

          {/* Right: Nút gửi mũi tên lên */}
          <div className="flex items-center gap-1.5">
            <button
              ref={sendBtnRef}
              type="button"
              onClick={() => handleSubmit()}
              disabled={!input.trim() || isStreaming}
              title="Gửi câu hỏi"
              className={`p-1.5 rounded-full transition-all cursor-pointer ${
                input.trim() && !isStreaming
                  ? 'bg-white text-black hover:opacity-90 shadow-md'
                  : 'bg-[#3d3d3d] text-[#676767] cursor-not-allowed'
              }`}
            >
              <ArrowUp className="w-4 h-4" />
            </button>
          </div>
        </div>
      </div>

      {/* Footer Disclaimer */}
      <p className="text-center text-[11px] text-[#8e8e8e] mt-2 select-none">
        AgriVision có thể đưa ra kết quả tham khảo. Hãy kiểm tra các thông tin dịch bệnh quan trọng.
      </p>
    </div>
  );
}
