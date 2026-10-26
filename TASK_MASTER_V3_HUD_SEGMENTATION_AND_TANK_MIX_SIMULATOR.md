# 🚀 BẢN GIAO VIỆC TỔNG THỂ V3: TỐI ƯU CÀI ĐẶT, ĐỒNG BỘ AVATAR, NÂNG CẤP THỊ GIÁC AI HUD & BỘ NÃO MÔ PHỎNG XUNG ĐỘT PHA TRỘN THUỐC
### Dự án: AgriVision (ultra-project.onrender.com)
### Tác giả: Phan Trọng Khang (Lớp 9¹, THCS Vĩnh An, Vĩnh Long)

---

## 🎯 DANH SÁCH 4 NHIỆM VỤ CỐT LÕI

### 1. ⚙️ SỬA THÔNG TIN SỐ CÂY & BỆNH HỌC Ở TRANG CÀI ĐẶT (`/settings`)
- **Vấn đề hiện tại:** Trang cài đặt đang hiển thị chuỗi cứng `1.534 loài cây trồng & 3.020 bệnh học`, không tự động phản ánh đúng quy mô cơ sở dữ liệu thực tế sau khi cào và mở rộng.
- **Giải pháp:**
  - Chuyển sang cơ chế đếm động (Dynamic Count) từ dataset `src/data/vietnam_plant_pathology_1000_crops.json` hoặc qua helper `getAllCrops()` trong `src/lib/cropSearch.ts`.
  - Tính toán chính xác:
    - `totalCrops = crops.length`
    - `totalDiseases = crops.reduce((sum, c) => sum + (c.danh_sach_benh?.length || 0), 0)`
  - Hiển thị mượt mà trên thẻ: `{totalCrops.toLocaleString('vi-VN')} loài cây trồng & {totalDiseases.toLocaleString('vi-VN')} phác đồ bệnh học` kèm hiệu ứng đếm số nhẹ nhàng.

---

### 2. 👤 ĐỒNG BỘ AVATAR TÙY CHỈNH VÀO POPUP MENU HỒ SƠ (`ProfileMenu.tsx`)
- **Vấn đề hiện tại:** Trong khi nút avatar ở đáy Sidebar (`AppSidebar.tsx`) và trang Cài đặt đã hiển thị ảnh đại diện tùy chỉnh của người dùng, thì hộp thoại Popup (`src/components/sidebar/ProfileMenu.tsx`) vẫn chỉ hiển thị chữ viết tắt mặc định `PK`.
- **Giải pháp:**
  - Cập nhật `src/components/sidebar/ProfileMenu.tsx` tại khối hiển thị avatar của `userProfile`.
  - Kiểm tra điều kiện đồng bộ:
    ```tsx
    {userProfile.avatar_url ? (
      <img
        src={userProfile.avatar_url}
        alt={userProfile.name}
        className="w-8 h-8 shrink-0 rounded-full object-cover border border-[#3e3e3e]"
      />
    ) : (
      <div className="w-8 h-8 shrink-0 rounded-full bg-[#0d0d0d] text-white dark:bg-[#171717] dark:border dark:border-[#3e3e3e] dark:text-[#ececec] flex items-center justify-center font-bold text-xs shadow-xs">
        {userProfile.initials}
      </div>
    )}
    ```
  - Đảm bảo khi người dùng tải ảnh đại diện mới lên ở trang Cài đặt, Popup Menu cập nhật tức thì không cần tải lại trang.

---

### 3. 🔬 NÂNG CẤP COMPUTER VISION HUD & TÍCH HỢP TOOL TỰ ĐỘNG VÀO AI CHAT
- **Vấn đề thẩm mỹ & trải nghiệm:**
  - Nét viền hiện tại quá dày, thô, khung hộp vuông bao quanh che mất chi tiết của lá/quả.
  - Cần nâng tầm giao diện thị giác máy tính theo phong cách AgriTech HUD Futuristic (thanh lịch, chuẩn công nghệ cao).
- **Yêu cầu kỹ thuật:**
  1. **Tạo Module Vẽ HUD Tinh Tế (`src/lib/visionAnnotator.ts` hoặc Canvas Client/Server):**
     - **Viền bóc tách đa giác (Polygon Contour):** Nét thanh mảnh 1.2px - 1.5px, màu Neon Cyan (`#00F2FE`) hoặc Emerald Green (`#10B981`), viền tổn thương phát sáng nhẹ (glow 2px).
     - **Lớp phủ vết bệnh (Heatmap Lesion Mask):** Bán trong suốt mờ dịu (`rgba(239, 68, 68, 0.25)`), làm nổi bật vùng nấm/vi khuẩn mà không che mất cấu trúc gân lá hay vỏ quả.
     - **Khung định vị góc (Corner HUD Brackets):** Thay thế khung chữ nhật đặc thô cứng bằng 4 góc L-bracket siêu mỏng phong cách máy quét sinh học.
     - **Thẻ thông số nổi (Floating HUD Glass Badge):** Nền kính mờ dark frosted (`rgba(15, 23, 42, 0.85)`), viền sáng, hiển thị:
       - Tên phân loại tổn thương.
       - Tỷ lệ hoại tử: `Hoại tử: S = XX.X%` (tính bằng công thức diện tích Gauss Shoelace).
       - Độ tin cậy: `Độ chính xác: XX.X%`.
  2. **Xây dựng API Endpoint & Tool Gọi Cho AI:**
     - Endpoint: `/api/vision/segment-and-annotate` tiếp nhận ảnh gốc (Base64/URL).
     - Khai báo Tool `analyze_plant_lesion` trong danh mục công cụ của AI.
     - Cập nhật **System Prompt** (`src/lib/systemPrompt.ts`):
       - Quy định bắt buộc: Khi nông dân gửi ảnh chụp cây trồng, AI PHẢI tự động kích hoạt công cụ phân tích thị giác để tạo ảnh đánh dấu viền tổn thương, tính tỷ lệ hoại tử % và gửi kèm ảnh đã phân tích vào khung chat, kết hợp với tư vấn phác đồ xử lý chuyên sâu.

---

### 4. 🧪 BỘ NÃO MÔ PHỎNG XUNG ĐỘT HÓA SINH KHI PHA TRỘN THUỐC BVTV (BIOCHEMICAL TANK-MIX SIMULATOR)
- **Bối cảnh thực tiễn:** Nông dân ĐBSCL và Vĩnh Long thường pha chung 3-5 loại thuốc (trừ sâu + trừ nấm + phân bón lá + chất bám dính) vào một bình xịt. Việc pha sai làm thuốc kết tủa, mất hoạt tính diệt dịch hại, hoặc gây sốc nhiệt làm cháy lá, rụng bông hàng loạt.
- **Kiến trúc module (`src/lib/tankMixSimulator.ts` & giao diện `/tank-mix` hoặc Modal):**
  1. **Ma trận tương thích hóa sinh (Biochemical Compatibility Matrix):**
     - Tận dụng cơ sở dữ liệu các nhóm hoạt chất phổ biến tại Việt Nam:
       - **Gốc Đồng (Copper Hydroxide, Copper Oxychloride):** Đại kỵ Lân hữu cơ, Lưu huỳnh, thuốc có tính axit.
       - **Lưu huỳnh (Sulfur):** Kỵ tuyệt đối với dầu khoáng và các dạng nhũ dầu EC (khoảng cách tối thiểu 14 ngày).
       - **Nhóm Dithiocarbamate (Mancozeb, Propineb):** Kỵ các chế phẩm vi sinh (Bacillus, Trichoderma), kỵ kiềm mạnh.
       - **Phân bón lá chứa Canxi/Vi lượng:** Kỵ gốc Phosphat/Sunfat (tạo kết tủa không tan $CaSO_4$, $Ca_3(PO_4)_2$).
  2. **Quy tắc thứ tự hòa tan chuẩn WALES (Physical Formulation Order):**
     - $W$ (Wettable powders / Granules - Bột/Hạt thấm nước: WP, WG) $\rightarrow$ $A$ (Agitate - Khuấy đều tan hết) $\rightarrow$ $L$ (Liquid flowables - Huyền phù: SC, FL) $\rightarrow$ $E$ (Emulsifiable concentrates - Nhũ dầu: EC, OD) $\rightarrow$ $S$ (Surfactants / Solubles - Dung dịch & Bám dính: SL, SP).
  3. **Thuật toán kiểm tra xung đột cặp (Pairwise Compatibility Check):**
     - Đánh giá theo 3 cấp độ:
       - 🟢 **TƯƠNG THÍCH TỐT (Safe / Synergistic):** Hòa tan hoàn toàn, hỗ trợ nâng cao hiệu lực.
       - 🟡 **CẢNH BÁO / ĐIỀU KIỆN (Conditional):** Cần tuân thủ nghiêm ngặt thứ tự pha, khuấy kỹ, dùng ngay trong 4 giờ.
       - 🔴 **NGUY HIỂM / CẤM TRỘN (Incompatible / Danger):** Kết tủa vón cục, giảm hoạt tính sinh học, nguy cơ ngộ độc/cháy lá nghiêm trọng.
  4. **Giao diện Bình Phun Ảo (Virtual Spray Tank HUD):**
     - Nông dân chọn 2 hoặc nhiều loại thuốc từ danh mục.
     - Bình phun ảo hiển thị mô phỏng trực quan: dung dịch trong suốt, đổi màu hoặc hiện cảnh báo kết tủa vón cục kèm lời giải thích hóa học cặn kẽ và hướng dẫn cách khắc phục an toàn.

---

### 🛡️ NGUYÊN TẮC BẢO MẬT & TRIỂN KHAI
- Tuyệt đối không lưu trữ khóa API thô trong mã nguồn hoặc tệp markdown.
- Các khóa dịch vụ phải được quản lý qua biến môi trường hoặc cơ chế giải mã phân mảnh tại runtime.
- Sau khi kiểm thử cục bộ thành công, thực hiện build sản phẩm và cập nhật lên hệ thống.
