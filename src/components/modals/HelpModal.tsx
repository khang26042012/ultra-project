'use client';

import React, { useEffect } from 'react';
import { useChat } from '@/context/ChatContext';
import {
  X,
  Camera,
  FileSpreadsheet,
  TestTube2,
  PhoneCall,
  BookOpen,
} from 'lucide-react';

export default function HelpModal() {
  const { isHelpOpen, setIsHelpOpen } = useChat();

  // Close on Escape key
  useEffect(() => {
    function handleKeyDown(e: KeyboardEvent) {
      if (e.key === 'Escape') {
        setIsHelpOpen(false);
      }
    }
    if (isHelpOpen) {
      window.addEventListener('keydown', handleKeyDown);
    }
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isHelpOpen, setIsHelpOpen]);

  if (!isHelpOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-xs select-none p-3 sm:p-4 animate-in fade-in duration-150">
      <div className="w-full max-w-2xl bg-[#ffffff] dark:bg-[#1e1e1e] border border-[#e5e5e5] dark:border-[#333333] rounded-[24px] shadow-2xl overflow-hidden flex flex-col max-h-[90vh]">
        {/* Modal Header */}
        <div className="min-h-[3.5rem] py-2.5 px-4 sm:px-5 border-b border-[#e5e5e5] dark:border-[#333333] flex items-center justify-between shrink-0 gap-3">
          <div className="flex items-center gap-2.5 min-w-0 flex-1">
            <div className="w-8 h-8 rounded-full bg-[#f4f4f4] text-[#0d0d0d] dark:bg-[#2c2c2c] dark:text-white flex items-center justify-center font-bold text-xs shadow-xs shrink-0">
              <BookOpen className="w-4 h-4" strokeWidth={1.5} />
            </div>
            <div className="min-w-0">
              <h2 className="font-semibold text-sm sm:text-base text-[#0d0d0d] dark:text-white leading-tight">
                Cẩm nang Hướng dẫn Nông dân AgriVision
              </h2>
              <p className="text-[11px] text-[#737373] dark:text-[#a3a3a3] mt-0.5 leading-normal">
                Quy trình chuẩn hóa chẩn đoán bệnh học cây trồng VietGAP
              </p>
            </div>
          </div>

          <button
            type="button"
            onClick={() => setIsHelpOpen(false)}
            title="Đóng (Esc)"
            className="shrink-0 p-1.5 rounded-full hover:bg-[#f0f0f0] dark:hover:bg-[#2f2f2f] text-[#5d5d5d] hover:text-[#0d0d0d] dark:text-[#8e8e8e] dark:hover:text-white transition-colors cursor-pointer"
          >
            <X className="w-4 h-4" strokeWidth={1.5} />
          </button>
        </div>

        {/* Modal Scrollable Body */}
        <div className="flex-1 overflow-y-auto p-4 sm:p-6 space-y-4 no-scrollbar text-xs sm:text-sm text-[#0d0d0d] dark:text-[#ececec] leading-relaxed">
          {/* Section 1: Cách chụp ảnh chuẩn bệnh học */}
          <div className="p-4 rounded-2xl bg-[#f7f7f8] dark:bg-[#242424] border border-[#e5e5e5] dark:border-[#333] space-y-2">
            <div className="flex items-center gap-2.5 font-semibold text-sm text-[#0d0d0d] dark:text-white">
              <div className="p-2 rounded-full bg-[#ebebeb] dark:bg-[#333] text-[#0d0d0d] dark:text-white shadow-2xs">
                <Camera className="w-4 h-4" strokeWidth={1.5} />
              </div>
              <span>1. Cách chụp ảnh chuẩn bệnh học vi mô</span>
            </div>
            <ul className="space-y-1.5 pl-2 text-[#5d5d5d] dark:text-[#b4b4b4] text-xs">
              <li className="flex items-start gap-2">
                <span className="w-1.5 h-1.5 rounded-full bg-[#8e8e8e] mt-1.5 shrink-0" />
                <span><strong>Chụp sát vết bệnh:</strong> Khoảng cách lý tưởng từ 15cm – 20cm, lấy nét trực tiếp vào ranh giới giữa mô lá khỏe và mô bị bệnh.</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="w-1.5 h-1.5 rounded-full bg-[#8e8e8e] mt-1.5 shrink-0" />
                <span><strong>Chụp cả 2 mặt lá:</strong> Rất nhiều bệnh do nấm/nhện (như mốc lá, rầy, nhện đỏ) tập trung chủ yếu ở mặt dưới lá.</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="w-1.5 h-1.5 rounded-full bg-[#8e8e8e] mt-1.5 shrink-0" />
                <span><strong>Ánh sáng tự nhiên:</strong> Tránh chụp lúc nắng gắt gây chói lóa mất màu thực tế, hoặc lúc trời tối làm nhòe cấu trúc vi thể.</span>
              </li>
            </ul>
          </div>

          {/* Section 2: Mô tả triệu chứng hiệu quả */}
          <div className="p-4 rounded-2xl bg-[#f7f7f8] dark:bg-[#242424] border border-[#e5e5e5] dark:border-[#333] space-y-2">
            <div className="flex items-center gap-2.5 font-semibold text-sm text-[#0d0d0d] dark:text-white">
              <div className="p-2 rounded-full bg-[#ebebeb] dark:bg-[#333] text-[#0d0d0d] dark:text-white shadow-2xs">
                <FileSpreadsheet className="w-4 h-4" strokeWidth={1.5} />
              </div>
              <span>2. Mô tả triệu chứng hiệu quả cho AI</span>
            </div>
            <p className="text-xs text-[#5d5d5d] dark:text-[#b4b4b4]">
              Khi gửi câu hỏi kèm theo ảnh, bà con cung cấp thêm 3 thông tin then chốt để AI định danh chính xác 100%:
            </p>
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-2 pt-1 text-xs">
              <div className="p-2.5 rounded-xl bg-white dark:bg-[#1a1a1a] border border-[#e5e5e5] dark:border-[#333]">
                <div className="font-semibold text-[#0d0d0d] dark:text-white">Giống cây & Tuổi</div>
                <div className="text-[11px] text-[#737373] dark:text-[#8e8e8e] mt-0.5">Cam sành 3 năm, Bưởi Da Xanh mới ra hoa, Lúa OM 45 ngày...</div>
              </div>
              <div className="p-2.5 rounded-xl bg-white dark:bg-[#1a1a1a] border border-[#e5e5e5] dark:border-[#333]">
                <div className="font-semibold text-[#0d0d0d] dark:text-white">Vị trí phát bệnh</div>
                <div className="text-[11px] text-[#737373] dark:text-[#8e8e8e] mt-0.5">Chỉ bị ở đọt non, lá già chân, thối cổ rễ hay nứt vỏ thân...</div>
              </div>
              <div className="p-2.5 rounded-xl bg-white dark:bg-[#1a1a1a] border border-[#e5e5e5] dark:border-[#333]">
                <div className="font-semibold text-[#0d0d0d] dark:text-white">Xúc giác & Mùi</div>
                <div className="text-[11px] text-[#737373] dark:text-[#8e8e8e] mt-0.5">Sờ thấy ráp như giấy nhám, tróc nhọ nồi hay có mùi chua thối...</div>
              </div>
            </div>
          </div>

          {/* Section 3: Hướng dẫn kiểm tra thực địa */}
          <div className="p-4 rounded-2xl bg-[#f7f7f8] dark:bg-[#242424] border border-[#e5e5e5] dark:border-[#333] space-y-2">
            <div className="flex items-center gap-2.5 font-semibold text-sm text-[#0d0d0d] dark:text-white">
              <div className="p-2 rounded-full bg-[#ebebeb] dark:bg-[#333] text-[#0d0d0d] dark:text-white shadow-2xs">
                <TestTube2 className="w-4 h-4" strokeWidth={1.5} />
              </div>
              <span>3. Phương pháp thử nghiệm lâm sàng tại vườn</span>
            </div>
            <div className="space-y-2 text-xs text-[#5d5d5d] dark:text-[#b4b4b4]">
              <div className="p-2.5 rounded-xl bg-white dark:bg-[#1a1a1a] border border-[#e5e5e5] dark:border-[#333]">
                <span className="font-semibold text-[#0d0d0d] dark:text-white">Thử nghiệm giọt dịch vi khuẩn héo xanh (Bacterial Stream Test):</span>
                <p className="mt-1">Cắt một đoạn thân cây bị héo ngâm vào ly nước thủy tinh trong suốt. Sau 2-3 phút, nếu thấy các sợi mây trắng đục (dòng dịch vi khuẩn *Ralstonia*) tuôn ra từ bó mạch thì cây bị héo xanh vi khuẩn, không phải do nấm đất.</p>
              </div>
              <div className="p-2.5 rounded-xl bg-white dark:bg-[#1a1a1a] border border-[#e5e5e5] dark:border-[#333]">
                <span className="font-semibold text-[#0d0d0d] dark:text-white">Kiểm tra thối rễ vs Nhiễm mặn:</span>
                <p className="mt-1">Đào nhẹ lớp rễ tơ tầng mặt (0-15cm): Nếu vỏ rễ tuột khỏi lõi gỗ và có mùi tanh thối là bệnh Vàng lá thối rễ (*Phytophthora/Fusarium*). Nếu chóp lá cháy khô đối xứng mép lá vào trong thì do mặn hoặc cháy phân.</p>
              </div>
            </div>
          </div>

          {/* Section 4: Liên hệ khẩn cấp BVTV Vĩnh Long */}
          <div className="p-4 rounded-2xl bg-black/5 dark:bg-white/5 border border-[#e5e5e5] dark:border-[#333] space-y-2.5">
            <div className="flex items-center gap-2.5 font-semibold text-sm text-[#0d0d0d] dark:text-white">
              <div className="p-2 rounded-full bg-[#ebebeb] dark:bg-[#333] text-[#0d0d0d] dark:text-white shadow-2xs">
                <PhoneCall className="w-4 h-4" strokeWidth={1.5} />
              </div>
              <span>4. Thông tin liên hệ cơ quan bảo vệ thực vật địa phương</span>
            </div>
            <p className="text-xs text-[#5d5d5d] dark:text-[#b4b4b4]">
              Khi nghi ngờ dịch bệnh bùng phát diện rộng nguy hiểm (như Vàng lá Greening, Bệnh chổi rồng nhãn, Rầy nâu lúa), bà con vui lòng liên hệ ngay cơ quan chức năng:
            </p>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs">
              <div className="p-3 rounded-xl bg-white dark:bg-[#1a1a1a] border border-[#e5e5e5] dark:border-[#333]">
                <div className="font-semibold text-[#0d0d0d] dark:text-white">Chi cục Trồng trọt & BVTV Vĩnh Long</div>
                <div className="text-[11px] text-[#737373] dark:text-[#a3a3a3] mt-0.5">Số 1B, đường Hoàng Thái Hiếu, Phường 1, TP. Vĩnh Long</div>
                <div className="mt-1.5 font-medium text-[#0d0d0d] dark:text-white">Hotline: (0270) 3822 559</div>
              </div>
              <div className="p-3 rounded-xl bg-white dark:bg-[#1a1a1a] border border-[#e5e5e5] dark:border-[#333]">
                <div className="font-semibold text-[#0d0d0d] dark:text-white">Trạm Trồng trọt & BVTV các Huyện</div>
                <div className="text-[11px] text-[#737373] dark:text-[#a3a3a3] mt-0.5">Bình Minh, Tam Bình, Trà Ôn, Vũng Liêm, Long Hồ, Mang Thít, Bình Tân</div>
                <div className="mt-1.5 text-[11px] text-[#5d5d5d] dark:text-[#b4b4b4]">Gửi mẫu bệnh phẩm trực tiếp tại UBND xã/thị trấn</div>
              </div>
            </div>
          </div>
        </div>

        {/* Modal Footer */}
        <div className="p-3 px-4 sm:px-5 border-t border-[#e5e5e5] dark:border-[#333333] flex items-center justify-between bg-[#fbfbfb] dark:bg-[#181818] shrink-0 gap-3">
          <span className="text-[11px] text-[#8e8e8e] leading-tight">
            AgriVision v1.0 • Phát triển bởi Phan Trọng Khang (THCS Vĩnh An)
          </span>
          <button
            type="button"
            onClick={() => setIsHelpOpen(false)}
            className="shrink-0 px-4 py-2 rounded-xl bg-[#0d0d0d] hover:bg-[#262626] text-white dark:bg-white dark:hover:bg-gray-100 dark:text-black text-xs font-semibold shadow-xs transition-all cursor-pointer"
          >
            Đã hiểu
          </button>
        </div>
      </div>
    </div>
  );
}
