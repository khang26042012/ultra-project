'use client';

import React, { useState, useRef, useEffect } from 'react';
import { useChat } from '@/context/ChatContext';
import { Plus, ArrowUp } from 'lucide-react';
import gsap from 'gsap';

export default function FloatingInputIsland() {
  const { sendMessage, isStreaming } = useChat();
  const [input, setInput] = useState('');

  const islandRef = useRef<HTMLDivElement>(null);
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const sendBtnRef = useRef<HTMLButtonElement>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);
  const prevHasTextRef = useRef(false);

  const hasText = input.trim().length > 0;

  // Auto-resize textarea
  useEffect(() => {
    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto';
      const scrollHeight = textareaRef.current.scrollHeight;
      textareaRef.current.style.height = `${Math.min(scrollHeight, 180)}px`;
    }
  }, [input]);

  // GSAP Pop-in animation for send button when typing starts
  useEffect(() => {
    if (hasText && !prevHasTextRef.current && sendBtnRef.current) {
      gsap.fromTo(
        sendBtnRef.current,
        { scale: 0.7, opacity: 0.6 },
        { scale: 1, opacity: 1, duration: 0.25, ease: 'back.out(1.7)' }
      );
    }
    prevHasTextRef.current = hasText;
  }, [hasText]);

  const handleFocus = () => {
    if (islandRef.current) {
      gsap.to(islandRef.current, {
        scale: 1.005,
        duration: 0.25,
        ease: 'power2.out',
      });
    }
  };

  const handleBlur = () => {
    if (islandRef.current) {
      gsap.to(islandRef.current, {
        scale: 1,
        duration: 0.25,
        ease: 'power2.out',
      });
    }
  };

  const handleSubmit = (e?: React.FormEvent) => {
    if (e) e.preventDefault();
    if (!input.trim() || isStreaming) return;

    // GSAP micro-interaction bounce on send button (60 FPS)
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
      <div
        ref={islandRef}
        className="relative rounded-[28px] bg-[#ffffff] dark:bg-[#2f2f2f] border border-[#e5e5e5] dark:border-[#3e3e3e] shadow-lg dark:shadow-xl p-3 focus-within:border-[#0d0d0d] dark:focus-within:border-[#525252] transition-colors will-change-transform"
      >
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
          onFocus={handleFocus}
          onBlur={handleBlur}
          placeholder="Nhập câu hỏi hoặc mô tả triệu chứng bệnh cây..."
          rows={1}
          className="w-full bg-transparent text-[#0d0d0d] dark:text-[#ececec] placeholder-[#8e8e8e] resize-none outline-none text-[15px] leading-relaxed px-2 py-1 max-h-[180px] overflow-y-auto no-scrollbar"
        />

        {/* Action Controls Bar */}
        <div className="flex items-center justify-between pt-2 px-1">
          {/* Left: Nút đính kèm tệp / ảnh */}
          <div className="flex items-center gap-2">
            <button
              type="button"
              onClick={handleFileClick}
              title="Đính kèm ảnh hoặc tài liệu cây trồng"
              className="p-1.5 rounded-full hover:bg-[#f2f2f2] dark:hover:bg-[#3d3d3d] text-[#5d5d5d] hover:text-[#0d0d0d] dark:text-[#b4b4b4] dark:hover:text-white transition-all hover:scale-[1.05] active:scale-[0.95] cursor-pointer"
            >
              <Plus className="w-4 h-4" strokeWidth={1.75} />
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
              className={`p-1.5 rounded-full transition-all will-change-transform ${
                input.trim() && !isStreaming
                  ? 'bg-[#0d0d0d] text-white hover:opacity-90 dark:bg-white dark:text-[#0d0d0d] shadow-md hover:scale-[1.05] active:scale-[0.95] cursor-pointer'
                  : 'bg-[#e5e5e5] text-[#8e8e8e] dark:bg-[#2f2f2f] dark:text-[#676767] cursor-not-allowed'
              }`}
            >
              <ArrowUp className="w-4 h-4" strokeWidth={2} />
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
