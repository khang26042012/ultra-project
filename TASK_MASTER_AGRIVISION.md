# 🚀 BẢN GIAO VIỆC TỔNG THỂ DỰ ÁN AGRIVISION (TASK MASTER)
### Tác giả: Phan Trọng Khang (Lớp 9¹, THCS Vĩnh An, Vĩnh Long)
### Mục tiêu: Hoàn thiện 4 giai đoạn phát triển toàn diện (UI/UX, Supabase Database, In-Context Pathology Tool & Multi-agent Browser Test)
*(Lưu ý: Tất cả các API keys và kết nối đã được cấu hình sẵn trong tệp `.env.local`. Sử dụng trực tiếp `process.env`)*

---

## 🎨 GIAI ĐOẠN 1: HOÀN THIỆN 11 NHIỆM VỤ UI/UX & GIAO DIỆN CHUẨN MỰC

1. **Xóa Header Mobile (`src/app/page.tsx`):**
   - Xóa bỏ thẻ `div` chứa avatar tròn `AV` và chữ `AgriVision` ở giữa thanh header.
   - Xóa bỏ class viền `border-b` để đỉnh trang liền mạch 100% với nền web.
   - Giữ lại 2 nút: Mở Sidebar (trái) và Đoạn chat mới (phải).
2. **Xử lý triệt để ký tự `--` / `---` (`src/components/chat/ChatMessage.tsx` & `src/lib/systemPrompt.ts`):**
   - Trong `ChatMessage.tsx`: Bắt regex `/^(\-{2,}|\*{3,})$/` để render thành thẻ phân cách mỏng: `<hr className="my-3.5 border-t border-[#e5e5e5] dark:border-[#2a2a2a]" />`.
   - Trong System Prompt: Cấm AI in ra `--` hoặc `---` trơ trọi làm khoảng trắng xuống dòng.
3. **Canh lề thụt vào chuẩn cho Bullet Points (`src/components/chat/ChatMessage.tsx`):**
   - Đặt thụt lề `pl-5 my-1` chuẩn mực dưới các đề mục số `1. `, `2. `, không để dấu chấm `•` thò ra ngoài.
4. **Thiết kế lại Search GUI mỏng nhẹ như Thinking (`src/components/chat/ChatMessage.tsx`):**
   - Xóa bỏ hoàn toàn khung pill viền xám thô cứng.
   - Đổi thành nút text tối giản: `Đã tìm kiếm X nguồn thông tin ▾` (style giống nút suy luận, bấm vào xổ danh sách link có vạch kẻ đứng mảnh `border-l-2`).
   - Khi đang tìm kiếm: Hiển thị text nhấp nháy `Đang tìm kiếm thông tin...` không khung viền.
5. **Sửa chữ "Đang suy nghĩ...":**
   - Xóa bỏ hoàn toàn icon đám mây/suy nghĩ (☁️, 💭).
   - Hiển thị dòng chữ `Đang suy nghĩ...` cùng cỡ chữ với lúc think xong, có animation thở từ đậm sang nhạt.
6. **Sửa lỗi Auto-scroll và Thêm nút cuộn nhanh xuống đáy (`src/components/chat/MessageList.tsx`):**
   - Chỉ tự động cuộn nếu người dùng đang ở gần đáy (trong 120px). Nếu người dùng kéo tay lên trên đọc tin cũ thì ngừng auto-scroll ngay.
   - Khi kéo lên cách đáy > 200px, hiện nút tròn nhỏ nổi ở góc dưới bên phải (`ArrowDown`), bấm vào sẽ cuộn mượt xuống đáy.
7. **Thu gọn Thumbnail ảnh gửi kèm + Tích hợp Image Lightbox (`src/components/chat/ChatMessage.tsx`):**
   - Thumbnail gọn gàng `max-w-[220px] max-h-[160px] rounded-2xl object-cover cursor-pointer hover:opacity-90`.
   - Có badge nhỏ `🔍 Bấm để phóng to`.
   - Bấm vào mở lớp phủ Lightbox toàn màn hình nền đen mờ (`bg-black/85 backdrop-blur-md`), có nút Zoom in (`+`), Zoom out (`-`), Đặt lại 100%, và Đóng (`✕`).
8. **Sửa lỗi hiển thị dấu `*...*` khi AI nhấn mạnh tên bệnh học (`src/components/chat/ChatMessage.tsx`):**
   - Cập nhật hàm `formatInlineMarkdown` để parse cả in nghiêng `*text*` thành `<em className="italic font-medium text-[#111] dark:text-[#f0f0f0]">text</em>` để tên khoa học/tên bệnh (như *Fusarium oxysporum*) hiển thị chuẩn đẹp, không còn lộ dấu sao.
9. **Hoàn thiện Menu Sidebar & Tạo Modal "Trợ giúp & Hướng dẫn" (`src/components/sidebar/ProfileMenu.tsx`, `src/components/modals/HelpModal.tsx`):**
   - Bấm vào User Card trên menu để mở thông tin tài khoản.
   - Bấm "Trợ giúp & Hướng dẫn" mở Modal Cẩm nang hướng dẫn nông dân (cách chụp ảnh lá bệnh, cách mô tả triệu chứng, bài test thực địa cắt gốc ngâm nước, số hotline Chi cục BVTV Vĩnh Long).
10. **Thiết kế lại SettingsModal cho Điện thoại (`src/components/modals/SettingsModal.tsx`):**
    - Trên mobile (`< md`): Chuyển Sidebar tabs thành thanh cuộn ngang dạng Pills trên đỉnh. Nội dung bên dưới chiếm tràn 100% bề ngang, không chia cột chật chội.
11. **Bổ sung tính năng mới trong SettingsModal:**
    - Cỡ chữ hiển thị tin nhắn: Nhỏ (13px), Vừa (15px), Lớn (17px).
    - Tùy chọn mô hình AI: Chẩn đoán sâu (`ag/gemini-3.8-flash-high`) vs Phản hồi nhanh (`ag/gemini-3.8-flash`).
    - Bật/tắt Web Search 9Router.
    - Quản lý dữ liệu: Xuất file backup JSON, Xóa lịch sử có xác nhận an toàn.

---

## 🗄️ GIAI ĐOẠN 2: CHUYỂN TOÀN BỘ LƯU TRỮ SANG SUPABASE DATABASE & SỬA DỨT ĐIỂM AUTH

Trong `src/context/ChatContext.tsx`:
1. **Sửa triệt để hàm `register`:**
   - Dùng lệnh `supabase.from('profiles').upsert({...}, { onConflict: 'email' })` để tránh lỗi 409 duplicate key.
   - Bắt buộc lưu cột `password_hash`.
   - Kiểm tra lỗi `if (insertError) return { success: false, error: insertError.message }` (tuyệt đối không nuốt lỗi).
2. **Sửa triệt để hàm `login`:**
   - Truy vấn trực tiếp từ Supabase: `supabase.from('profiles').select('*').eq('email', cleanEmail).maybeSingle()`.
   - Đối chiếu `password_hash`. Nếu tài khoản cũ chưa có mật khẩu, tự động cập nhật và cho đăng nhập (Auto-healing).
   - Tải toàn bộ danh sách `conversations` và `messages` từ Supabase về để đồng bộ đa thiết bị (hỗ trợ tab ẩn danh 100%).
3. **Đồng bộ Hội thoại & Tin nhắn:**
   - Khi tạo/xóa đoạn chat: Đồng bộ bảng `conversations`.
   - Khi gửi/nhận tin nhắn: Lưu vào bảng `messages`.
   - Vẫn duy trì song song `localStorage` làm cache tức thì.

---

## 🌾 GIAI ĐOẠN 3: TÍCH HỢP TOOL BỆNH HỌC NỘI TẠI & BỔ SUNG 300 CÂY TRỒNG VIỆT NAM

1. **Xây dựng Module Tra cứu Tri thức Bệnh học (`src/lib/cropSearch.ts`):**
   - Đọc và cache tệp dữ liệu `src/data/vinh_long_plant_pathology_100_crops.json` và tệp mở rộng.
   - Cung cấp hàm `searchCropKnowledge(cropName: string, symptoms: string[])` chuẩn hóa tiếng Việt, so khớp triệu chứng và trả về chi tiết bệnh học lâm sàng, tác nhân vi sinh, kiểm tra thực địa và phác đồ VietGAP.
2. **Tích hợp Tool `search_crop_database` vào Agent Loop (`src/app/api/chat/route.ts`):**
   - Khai báo 2 Tool cho Gemini:
     - Tool 1: `search_crop_database` (tri thức bệnh học nội tại).
     - Tool 2: `web_search` (tra cứu giá cả, thuốc BVTV thị trường qua 9Router).
   - Khi người dùng hỏi bệnh cây hoặc gửi ảnh:
     - AI suy luận và tự động gọi tool `search_crop_database` để lấy chứng cứ y học thực vật chuẩn xác.
     - Nếu cần tìm kiếm thời sự hoặc giá cả tại Vĩnh Long, AI gọi tiếp `web_search`.
     - Câu trả lời cuối cùng đạt độ chính xác 100%, không bị ảo giác kiến thức.
3. **Mở rộng kho dữ liệu lên 400+ cây trồng Việt Nam:**
   - Bổ sung 300 loại cây trồng mới (Cây ăn trái nhiệt đới/ôn đới, cây công nghiệp xuất khẩu, rau củ quả Đà Lạt, hoa màu, dược liệu quý).
   - Mỗi cây phải có đầy đủ: `topic`, `name_vi`, `scientific_name`, `dia_ban_pho_bien`, `danh_sach_benh` (tác nhân nấm/khuẩn/virus, triệu chứng, phân biệt ca bệnh kép, kiểm tra thực địa, phác đồ VietGAP).
   - Lưu vào: `src/data/vietnam_plant_pathology_400_crops.json`.

---

## 🧪 GIAI ĐOẠN 4: SUBAGENT BROWSER TESTING TOÀN DIỆN & TỰ ĐỘNG AUDIT/POLISH

Khởi tạo các subagents mở trình duyệt kiểm thử thực tế từ A đến Z:
1. **Test Auth:** Tạo tài khoản ➔ Đăng xuất ➔ Đăng nhập lại ➔ Mở Tab Ẩn danh (Incognito) đăng nhập thành công 100%.
2. **Test Mobile:** Màn hình 375px/390px/412px không còn avatar/tên ở header, không còn đường kẻ ngang, Settings cuộn dạng Pills mượt mà.
3. **Test Chat & Lightbox:** Stream tin nhắn mượt, Thinking thu gọn chuẩn, Web search xổ nguồn mỏng nhẹ, ảnh gửi kèm bấm mở Fullscreen Lightbox nền đen zoom in/out.
4. **Test Cuộn & Markdown:** Kéo lên đọc tin cũ không bị cướp màn hình, có nút tròn cuộn nhanh xuống đáy; tên bệnh in nghiêng chuẩn, không còn dấu sao thô.
5. **QUY TẮC BẮT BUỘC:** Phát hiện bất kỳ lỗi logic hay chi tiết nào chưa đẹp ➔ Tự động sửa code và tối ưu ngay lập tức!

---

## 🚀 TIÊU CHUẨN HOÀN TẤT & PUSH CODE:
```bash
npm run build
git add -A
git commit -m "feat(agrivision): complete master tasks - UI polish, Supabase auth fix, in-context pathology tool, 400 crops dataset, and browser audit"
git push origin main
```
Render sẽ tự động build và triển khai bản web mới nhất tại: **https://ultra-project.onrender.com**.
