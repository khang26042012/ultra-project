'use client';

import React, { useState, useRef, useEffect } from 'react';
import { useChat } from '@/context/ChatContext';
import { Plus, ArrowUp, X, Image as ImageIcon } from 'lucide-react';
import gsap from 'gsap';

// Client-side image compressor: scales max dimension to 1200px and outputs clean JPEG base64
const compressImage = (file: File): Promise<string> => {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = (e) => {
      const img = new Image();
      img.onload = () => {
        const canvas = document.createElement('canvas');
        let width = img.width;
        let height = img.height;
        const maxDim = 1200;

        if (width > maxDim || height > maxDim) {
          if (width > height) {
            height = Math.round((height * maxDim) / width);
            width = maxDim;
          } else {
            width = Math.round((width * maxDim) / height);
            height = maxDim;
          }
        }

        canvas.width = width;
        canvas.height = height;
        const ctx = canvas.getContext('2d');
        if (ctx) {
          ctx.drawImage(img, 0, 0, width, height);
          const base64 = canvas.toDataURL('image/jpeg', 0.85);
          resolve(base64);
        } else {
          resolve(e.target?.result as string);
        }
      };
      img.onerror = () => reject(new Error('Không thể tải tệp hình ảnh'));
      img.src = e.target?.result as string;
    };
    reader.onerror = () => reject(new Error('Không thể đọc tệp hình ảnh'));
    reader.readAsDataURL(file);
  });
};

export default function FloatingInputIsland() {
  const { sendMessage, isStreaming } = useChat();
  const [input, setInput] = useState('');
  const [selectedImage, setSelectedImage] = useState<string | null>(null);
  const [imageName, setImageName] = useState<string>('');
  const [isCompressing, setIsCompressing] = useState<boolean>(false);

  const islandRef = useRef<HTMLDivElement>(null);
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const sendBtnRef = useRef<HTMLButtonElement>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);
  const prevCanSendRef = useRef(false);

  const canSend = (input.trim().length > 0 || selectedImage !== null) && !isStreaming && !isCompressing;

  // Auto-resize textarea from 1 line up to 6 lines (~180px)
  useEffect(() => {
    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto';
      const scrollHeight = textareaRef.current.scrollHeight;
      textareaRef.current.style.height = `${Math.min(scrollHeight, 180)}px`;
    }
  }, [input]);

  // GSAP Pop-in animation for send button when ready to send
  useEffect(() => {
    if (canSend && !prevCanSendRef.current && sendBtnRef.current) {
      gsap.fromTo(
        sendBtnRef.current,
        { scale: 0.7, opacity: 0.6 },
        { scale: 1, opacity: 1, duration: 0.25, ease: 'back.out(1.7)' }
      );
    }
    prevCanSendRef.current = canSend;
  }, [canSend]);

  const handleFocus = () => {
    if (islandRef.current) {
      gsap.to(islandRef.current, {
        scale: 1.005,
        duration: 0.2,
        ease: 'power2.out',
      });
    }
  };

  const handleBlur = () => {
    if (islandRef.current) {
      gsap.to(islandRef.current, {
        scale: 1,
        duration: 0.2,
        ease: 'power2.out',
      });
    }
  };

  const handleSubmit = (e?: React.FormEvent) => {
    if (e) e.preventDefault();
    if (!canSend) return;

    // GSAP micro-interaction bounce on send button (60 FPS)
    if (sendBtnRef.current) {
      gsap.fromTo(
        sendBtnRef.current,
        { scale: 0.75 },
        { scale: 1, duration: 0.25, ease: 'back.out(2.5)' }
      );
    }

    sendMessage(input, selectedImage || undefined);
    setInput('');
    setSelectedImage(null);
    setImageName('');
    if (fileInputRef.current) {
      fileInputRef.current.value = '';
    }
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

  const handleFileChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const files = e.target.files;
    if (files && files.length > 0) {
      const file = files[0];
      setImageName(file.name);
      setIsCompressing(true);
      try {
        const compressedBase64 = await compressImage(file);
        setSelectedImage(compressedBase64);
      } catch (err) {
        console.error('Lỗi nén ảnh:', err);
      } finally {
        setIsCompressing(false);
      }
    }
  };

  const handleRemoveImage = () => {
    setSelectedImage(null);
    setImageName('');
    if (fileInputRef.current) {
      fileInputRef.current.value = '';
    }
  };

  return (
    <div className="w-full max-w-3xl mx-auto px-3 sm:px-4 pb-4 select-none">
      <div
        ref={islandRef}
        className="relative rounded-[26px] bg-[#ffffff] dark:bg-[#212121] border border-black/10 dark:border-white/10 shadow-[0_2px_12px_rgba(0,0,0,0.08)] dark:shadow-none p-3 focus-within:border-black/25 dark:focus-within:border-white/25 transition-all will-change-transform"
      >
        {/* Hidden File Input for Image Upload / Camera Capture */}
        <input
          ref={fileInputRef}
          type="file"
          accept="image/*"
          onChange={handleFileChange}
          className="hidden"
        />

        {/* Thumbnail Preview Area with Remove Button */}
        {selectedImage && (
          <div className="relative inline-flex items-center gap-2.5 mb-2.5 p-1.5 pr-3 bg-[#f7f7f8] dark:bg-[#181818] border border-[#e5e5e5] dark:border-[#333] rounded-2xl shadow-xs">
            <div className="relative w-12 h-12 rounded-xl overflow-hidden border border-[#dedede] dark:border-[#444] bg-black/5 shrink-0">
              <img
                src={selectedImage}
                alt="Ảnh đính kèm cây trồng"
                className="w-full h-full object-cover"
              />
            </div>
            <div className="flex flex-col text-left max-w-[200px]">
              <span className="text-xs font-semibold text-[#0d0d0d] dark:text-[#ececec] truncate">
                {imageName || 'Ảnh cây trồng'}
              </span>
              <span className="text-[10px] text-[#5d5d5d] dark:text-[#8e8e8e] flex items-center gap-1">
                <ImageIcon className="w-3 h-3 text-[#0d0d0d] dark:text-white" strokeWidth={1.5} />
                <span>Sẵn sàng chẩn đoán vi mô</span>
              </span>
            </div>
            <button
              type="button"
              onClick={handleRemoveImage}
              title="Hủy ảnh"
              className="ml-1 p-1 rounded-full hover:bg-[#eaeaea] dark:hover:bg-[#333] text-[#5d5d5d] hover:text-[#0d0d0d] dark:text-[#b4b4b4] dark:hover:text-white transition-colors cursor-pointer"
            >
              <X className="w-3.5 h-3.5" strokeWidth={1.5} />
            </button>
          </div>
        )}

        {/* Textarea: Auto-resize up to 6 lines */}
        <textarea
          ref={textareaRef}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          onFocus={handleFocus}
          onBlur={handleBlur}
          placeholder={
            selectedImage
              ? "Mô tả thêm triệu chứng (loại cây, sờ ráp hay trơn, vị trí vườn...)"
              : "Nhập triệu chứng cây trồng hoặc bấm '+' đính kèm ảnh chụp..."
          }
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
              disabled={isCompressing || isStreaming}
              title="Đính kèm ảnh hoặc chụp từ camera"
              className="p-1.5 rounded-full hover:bg-[#f2f2f2] dark:hover:bg-[#333] text-[#5d5d5d] hover:text-[#0d0d0d] dark:text-[#b4b4b4] dark:hover:text-white transition-all hover:scale-[1.05] active:scale-[0.95] cursor-pointer"
            >
              <Plus className="w-4 h-4" strokeWidth={1.5} />
            </button>
            {isCompressing && (
              <span className="text-[11px] text-[#8e8e8e] italic animate-pulse">
                Đang xử lý ảnh...
              </span>
            )}
          </div>

          {/* Right: Nút gửi mũi tên lên */}
          <div className="flex items-center gap-1.5">
            <button
              ref={sendBtnRef}
              type="button"
              onClick={() => handleSubmit()}
              disabled={!canSend}
              title="Gửi câu hỏi"
              className={`p-1.5 rounded-full transition-all will-change-transform ${
                canSend
                  ? 'bg-[#0d0d0d] text-white hover:opacity-90 dark:bg-white dark:text-[#0d0d0d] shadow-md hover:scale-[1.05] active:scale-[0.95] cursor-pointer'
                  : 'bg-[#e5e5e5] text-[#8e8e8e] dark:bg-[#2b2b2b] dark:text-[#555] cursor-not-allowed'
              }`}
            >
              <ArrowUp className="w-4 h-4" strokeWidth={1.5} />
            </button>
          </div>
        </div>
      </div>

      {/* Footer Disclaimer */}
      <p className="text-center text-[11px] text-[#8e8e8e] mt-2 select-none">
        AgriVision hỗ trợ chẩn đoán tham khảo chuẩn VietGAP. Hãy gửi mẫu đến cán bộ BVTV địa phương khi cần khẳng định.
      </p>
    </div>
  );
}
