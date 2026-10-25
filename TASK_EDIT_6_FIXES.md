# 🛠️ BẢN GIAO VIỆC EDIT TOÀN DIỆN DỰ ÁN AGRIVISION (ULTRA-PROJECT)
### Tác giả: Phan Trọng Khang (Lớp 9¹, THCS Vĩnh An, Vĩnh Long)
### Mục tiêu: Hoàn thiện 11 nâng cấp giao diện, sửa lỗi Markdown, Responsive Mobile, Image Lightbox và Modal Cài Đặt chuyên nghiệp

---

## 📋 DANH SÁCH 11 NHIỆM VỤ THỰC THI CHI TIẾT:

### 📌 1. XÓA BỎ HEADER Ở MOBILE (AVATAR + TÊN Ở GIỮA) & XÓA ĐƯỜNG KẺ XÁM NGANG
- **Tệp chỉnh sửa:** `src/app/page.tsx`
- **Hành động:**
  - Trong thẻ `<header className="md:hidden ...">`:
    - **Xóa bỏ hoàn toàn** thẻ `div` chứa avatar tròn `AV` và chữ `AgriVision` ở giữa.
    - **Xóa bỏ** class viền `border-b border-[#e5e5e5]/80 dark:border-[#262626]/80` để đỉnh trang liền mạch 100% với nền web.
    - Giữ lại nút mở Sidebar (bên trái) và nút Đoạn chat mới (bên phải), layout dạng: `flex items-center justify-between px-3 bg-transparent shrink-0 select-none`.

---

### 📌 2. XỬ LÝ LỖI AI DÙNG `--` HOẶC `---` LÀM KHOẢNG CÁCH XUỐNG HÀNG
- **Tệp chỉnh sửa:** `src/components/chat/ChatMessage.tsx`, `src/lib/systemPrompt.ts`, `src/lib/system_prompt.md`
- **Hành động:**
  - **Trong `ChatMessage.tsx` (hàm `renderFormattedContent`):** Bắt regex nhận diện đường kẻ ngang Markdown và render thẻ phân cách mỏng thanh lịch:
    ```tsx
    if (/^(\-{2,}|\*{3,})$/.test(line.trim())) {
      elements.push(
        <hr key={i} className="my-3.5 border-t border-[#e5e5e5] dark:border-[#2a2a2a]" />
      );
      i++;
      continue;
    }
    ```
  - **Trong System Prompt:** Thêm quy tắc: *"Không dùng ký tự '--' hoặc '---' trơ trọi làm khoảng trắng xuống dòng. Hãy ngắt đoạn tự nhiên hoặc dùng tiêu đề rõ ràng."*

---

### 📌 3. TỐI ƯU DẤU GẠCH ĐẦU DÒNG (BULLET POINTS) KHÔNG BỊ NHÔ RA TRƯỚC ĐỀ MỤC
- **Tệp chỉnh sửa:** `src/components/chat/ChatMessage.tsx`
- **Hành động:**
  - Canh lề thụt vào trong chuẩn mực (`pl-5 my-1` hoặc `ml-4`) để các ý phụ thụt lùi vào trong so với tiêu đề số `1. `, `2. `.
  - Sử dụng chấm tròn đồng bộ: `<span className="w-1.5 h-1.5 rounded-full bg-[#8e8e8e] dark:bg-[#737373] mt-2.5 shrink-0" />`.

---

### 📌 4. THIẾT KẾ LẠI SEARCH GUI: MỎNG NHẸ NHƯ KHỐI THINKING (NÚT TEXT CÓ ▾ ĐỂ XEM NGUỒN)
- **Tệp chỉnh sửa:** `src/components/chat/ChatMessage.tsx`
- **Hành động:**
  - **Xóa bỏ hoàn toàn khung pill viền xám thô cứng.**
  - Đổi thành nút text mỏng nhẹ: `Đã tìm kiếm X nguồn thông tin ▾` (sử dụng cùng class `text-xs font-medium text-[#737373] hover:text-[#0d0d0d] dark:text-[#a3a3a3] dark:hover:text-white transition-colors cursor-pointer`).
  - Khi click mở ra: Hiển thị danh sách nguồn có vạch kẻ đứng thanh mảnh bên trái (`border-l-2 border-[#e5e5e5] dark:border-[#383838] pl-3.5 my-2`).
  - Khi đang tìm kiếm: Dòng text nhấp nháy: `Đang tìm kiếm thông tin...` không khung viền.

---

### 📌 5. SỬA PHẦN "ĐANG SUY NGHĨ": Y HỆT LÚC THINK XONG, LOẠI BỎ ICON ☁️ / 💭, HIỆU ỨNG THỞ ĐẬM → NHẠT
- **Tệp chỉnh sửa:** `src/components/chat/ChatMessage.tsx`
- **Hành động:**
  - Xóa bỏ icon đám mây/suy nghĩ (`☁️`, `💭`).
  - Dòng text: `<span className="inline-flex items-center text-xs font-medium text-[#737373] dark:text-[#a3a3a3] animate-pulse mb-2.5 select-none">Đang suy nghĩ...</span>`.

---

### 📌 6. KHẮC PHỤC LỖI KHÔNG KÉO LÊN ĐỌC TIN CŨ KHI STREAM & THÊM NÚT CUỘN NHANH XUỐNG ĐÁY
- **Tệp chỉnh sửa:** `src/components/chat/MessageList.tsx`
- **Hành động:**
  - **Smart Auto-scroll:** Chỉ tự động cuộn nếu người dùng đang ở gần đáy (trong vòng 120px). Nếu người dùng đã cuộn tay lên trên thì ngừng cuộn tự động.
  - **Floating Scroll-to-Bottom Button:** Khi cuộn lên xa đáy (> 200px), xuất hiện một nút tròn nhỏ gọn nổi ở góc dưới bên phải (trên ô chat) có icon `ArrowDown`. Bấm vào sẽ cuộn mượt xuống cuối trang.

---

### 📌 7. THU GỌN ẢNH GỬI KÈM + TÍCH HỢP IMAGE LIGHTBOX (PHÓNG TO / THU NHỎ / XEM ĐẦY MÀN HÌNH)
- **Tệp chỉnh sửa:** `src/components/chat/ChatMessage.tsx`
- **Vấn đề:** Ảnh gửi kèm trong tin nhắn hiện tại hiển thị quá to, choán hết diện tích và không thể bấm vào để soi kỹ chi tiết vết bệnh.
- **Hành động cụ thể:**
  - **Kích thước thumbnail gọn đẹp:** Giới hạn ảnh ở mức `max-w-[220px] max-h-[160px] rounded-2xl object-cover cursor-pointer hover:opacity-90 transition-all border border-black/10 dark:border-white/10`.
  - Thêm badge góc dưới ảnh: `🔍 Bấm để phóng to` nhỏ gọn.
  - **Tích hợp Image Lightbox Modal:** Khi click vào ảnh:
    - Mở lớp phủ mờ toàn màn hình (`fixed inset-0 z-50 bg-black/85 backdrop-blur-md flex flex-col items-center justify-center p-4`).
    - Hiển thị ảnh sắc nét ở kích thước lớn.
    - Thanh điều khiển góc trên: Phóng to (`+`), Thu nhỏ (`-`), Đặt lại kích thước (100%), Đóng (`✕` hoặc phím Escape / click nền đen).

---

### 📌 8. SỬA LỖI IN RA DẤU `*...*` KHI AI NHẤN MẠNH TÊN BỆNH / TÊN KHOA HỌC
- **Tệp chỉnh sửa:** `src/components/chat/ChatMessage.tsx` (hàm `formatInlineMarkdown`)
- **Vấn đề:** Hiện tại chỉ parse cú pháp `**bold**`, bỏ quên `*italic*` nên khi Gemini trả về tên nấm hoặc nhấn mạnh như `*Fusarium oxysporum*` hay `*Bác nhìn xem bó mạch...*`, dấu sao bị in nguyên vẹn ra màn hình.
- **Hành động cụ thể:**
  - Cập nhật hàm `formatInlineMarkdown` để xử lý đầy đủ các cấp độ Markdown:
    1. **Bold + Italic:** `***text***` ➔ `<strong><em>text</em></strong>`
    2. **Bold:** `**text**` ➔ `<strong className="font-semibold text-[#0d0d0d] dark:text-white">text</strong>`
    3. **Italic / Tên bệnh học:** `*text*` hoặc `_text_` ➔ `<em className="italic font-medium text-[#111] dark:text-[#f0f0f0]">text</em>`
    4. **Inline Code:** `` `code` `` ➔ thẻ `<code>`
    5. **Hyperlink:** `[tiêu đề](url)` ➔ thẻ `<a>` có thể bấm mở trang web.

---

### 📌 9. HOÀN THIỆN LOGIC MENU SIDEBAR & TẠO MODAL "TRỢ GIÚP & HƯỚNG DẪN" CHUYÊN NGHIỆP
- **Tệp chỉnh sửa:** `src/components/sidebar/ProfileMenu.tsx`, tạo thêm `src/components/modals/HelpModal.tsx`
- **Hành động cụ thể:**
  - **Thẻ User Profile trên cùng:** Bấm vào sẽ mở tab Tài khoản trong Cài đặt hoặc mở Modal thông tin.
  - **Mục "Trợ giúp & Hướng dẫn":** Xóa bỏ hàm `alert(...)` sơ sài! Mở **Modal Cẩm nang Nông dân AgriVision** với 4 phần thực tế:
    1. *Cách chụp ảnh chuẩn bệnh học:* Hướng dẫn chụp sát vết bệnh, chụp cả mặt trên và mặt dưới lá, đủ sáng, rõ nét.
    2. *Mô tả triệu chứng hiệu quả:* Cung cấp loại cây (sầu riêng, cam, bưởi, dừa, lúa), tuổi cây và vị trí nhiễm bệnh.
    3. *Hướng dẫn kiểm tra thực địa:* Hướng dẫn cách thử nghiệm ngâm nước kiểm tra vi khuẩn héo xanh, kiểm tra thối nhũn có mùi chua.
    4. *Liên hệ khẩn cấp:* Thông tin đường dây nóng Trạm Khuyến nông và Chi cục Trồng trọt & BVTV Vĩnh Long.

---

### 📌 10. THIẾT KẾ LẠI MODAL CÀI ĐẶT (SETTINGS) CHUẨN ĐIỆN THOẠI & CHUẨN HÓA TEXT
- **Tệp chỉnh sửa:** `src/components/modals/SettingsModal.tsx`
- **Vấn đề:** Trên mobile, giao diện 2 cột (cột tab bên trái + cột nội dung bên phải) bị ép chặt, gây bí bách và khó bấm.
- **Hành động cụ thể:**
  - **Responsive Mobile:**
    - Trên màn hình nhỏ (`< md`): Chuyển Tabs thành **thanh cuộn ngang dạng Pills** ở phía trên cùng: `[Chung] [Đọc & Hiển thị] [Mô hình AI] [Dữ liệu] [Giới thiệu]`. Khung nội dung hiển thị tràn 100% chiều rộng phía dưới.
    - Trên màn hình máy tính (`md:`): Giữ nguyên giao diện Sidebar 2 cột thanh lịch.
  - Chuẩn hóa toàn bộ text hướng dẫn rõ ràng, xúc tích, thuần Việt.

---

### 📌 11. BỔ SUNG CÁC TÍNH NĂNG MỚI VÀO CÀI ĐẶT (SETTINGS)
- **Tệp chỉnh sửa:** `src/components/modals/SettingsModal.tsx` & `src/context/ChatContext.tsx`
- **Thêm các tính năng thiết thực:**
  1. **Tùy chỉnh Cỡ chữ hiển thị:** Nhỏ (13px), Vừa (15px - mặc định), Lớn (17px - hỗ trợ bà con nông dân lớn tuổi dễ đọc).
  2. **Tùy chọn Mô hình AI:**
     - `ag/gemini-3.8-flash-high` (Suy luận bệnh học chuyên sâu - Mặc định).
     - `ag/gemini-3.8-flash` (Phản hồi siêu tốc).
  3. **Công tắc Bật/Tắt Tự động tra cứu Web Search (9Router):** Cho phép người dùng quyết định có muốn AI luôn tìm kiếm web thời gian thực hay không.
  4. **Công tắc Bật/Tắt Tự động bám đáy (Auto-scroll):** Lưu vào state/localStorage.
  5. **Quản lý Dữ liệu:** Hiển thị dung lượng đã lưu trữ, nút Tải file sao lưu (.json), nút Xóa sạch lịch sử với hộp thoại xác nhận 2 lớp.

---

## 🚀 QUY TRÌNH KIỂM THỬ VÀ DEPLOY:
```bash
npm run build
git add -A
git commit -m "feat(agrivision): complete master polish - image lightbox, markdown italic parser, mobile responsive settings, rich help guide, and full menu logic"
git push origin main
```
Render sẽ tự động build và cập nhật trực tiếp tại: **https://ultra-project.onrender.com**.
