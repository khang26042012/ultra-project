# 🚀 BẢN GIAO VIỆC: SỬA TRIỆT ĐỂ BỊA ĐẶT THÔNG TIN TÁC GIẢ, XÓA NÚT 1500+ VÀ NÂNG CẤP MENU CHAT HISTORY CHUẨN CHATGPT
### Dự án: AgriVision (ultra-project)
### Tác giả: Phan Trọng Khang (Lớp 9¹, THCS Vĩnh An, Vĩnh Long)

---

## 🛑 NHIỆM VỤ 1: CHẶN ĐỨNG HOÀN TOÀN TÌNH TRẠNG AI BỊA ĐẶT TIỂU SỬ / TỰ SỰ VỀ TÁC GIẢ
- **Tệp chỉnh sửa:** `src/lib/systemPrompt.ts` & `src/lib/system_prompt.md`
- **Vấn đề thực tế:** AI đang tự ý bịa đặt các câu chuyện cảm động, tiểu sử đời tư và phát biểu thay tác giả (ví dụ: *"Khang sinh ra và lớn lên ở Mang Thít...", "Khang nhiều lần chứng kiến cảnh bà con khổ...", "Một học sinh lớp 9¹ đã xây dựng kho dữ liệu như thế nào?...", "Ước mơ bình dị của cậu học trò trường làng: Tâm nguyện của Khang không phải để lấy giải thưởng mà là..."*). Tác giả rất khó chịu vì điều này hoàn toàn là bịa đặt!
- **Hành động cụ thể:**
  - Thêm một điều lệ nghiêm cấm tối cao vào System Prompt:
    ```markdown
    ## 🚫 ĐIỀU LỆ TUYỆT ĐỐI CẤM: KHÔNG BỊA ĐẶT TIỂU SỬ, ĐỜI TƯ VÀ CẢM XÚC CỦA TÁC GIẢ PHAN TRỌNG KHANG

    1. **NGHIÊM CẤM TỰ Ý KỂ LỂ TIỂU SỬ:** Tuyệt đối KHÔNG ĐƯỢC tự nghĩ ra hoàn cảnh gia đình, tuổi thơ, động lực cá nhân hay hành trình lập trình của bạn Khang (CẤM các câu như: "Khang sinh ra lớn lên ở...", "Khang chứng kiến gia đình chòm xóm...", "Ước mơ bình dị của cậu học trò trường làng...", "Khang nung nấu quyết tâm...", "Tâm nguyện của Khang không phải để lấy giải thưởng...").
    2. **ĐỊNH DANH ĐÚNG 1 CÂU KHIÊM TỐN:** Bất cứ khi nào người dùng hỏi "Bạn là ai / Ai tạo ra bạn / Nguồn gốc dự án", CHỈ NÓI ĐÚNG 1 CÂU DUY NHẤT:
       > "AgriVision là hệ thống trợ lý bác sĩ cây trồng AI, được nghiên cứu và phát triển bởi bạn Phan Trọng Khang (Học sinh lớp 9¹, Trường THCS Vĩnh An, tỉnh Vĩnh Long) nhằm hỗ trợ bà con chẩn đoán bệnh học cây trồng và áp dụng phác đồ sinh học VietGAP."
    3. **100% TRỌNG TÂM LÀ CHUYÊN MÔN NÔNG HỌC:** Sau câu giới thiệu trên, chuyển ngay vào tư vấn cây trồng, triệu chứng vết bệnh và giải pháp kỹ thuật, tuyệt đối không viết văn tự sự dài dòng!
    ```

---

## 🗑️ NHIỆM VỤ 2: XÓA BỎ NÚT `1.500+` TRÊN ĐỈNH HEADER
- **Tệp chỉnh sửa:** `src/app/page.tsx`
- **Vấn đề:** Nút pill màu xanh lá cây `<Link href="/crops"> ... 1.500+ </Link>` nằm chình ình trên header mobile & desktop gây rối mắt và làm mất vẻ tối giản cao cấp của ứng dụng.
- **Hành động cụ thể:**
  - Mở `src/app/page.tsx`.
  - Tìm và **XÓA BỎ HOÀN TOÀN** thẻ `<Link href="/crops" ...> ... <span ...>1.500+</span></Link>` ở cả thanh header desktop và mobile.
  - Header trang chủ chỉ giữ lại:
    - Nút mở/đóng Sidebar (`PanelLeft`).
    - Nút Đoạn chat mới (`SquarePen`).
    - Hoàn toàn tối giản, thông thoáng, liền mạch với nền web. (Đường dẫn vào trang Toàn thư `/crops` đã có sẵn trong Sidebar và chân menu).

---

## 💬 NHIỆM VỤ 3: TỰ ĐỘNG ĐẶT TÊN CHAT BẰNG AI (3-5 TỪ TIẾNG VIỆT) & CONTEXT MENU CHUẨN CHATGPT

### A. Tự động phân tích và đặt tên Chat bằng AI:
- **Tệp chỉnh sửa:** `src/context/ChatContext.tsx` (và `src/app/api/chat/route.ts` nếu cần endpoint riêng)
- **Vấn đề:** Hiện tại các đoạn chat mới đang bị đặt tên sơ sài theo chữ đầu tiên người dùng gõ (ví dụ người dùng chào "Hi" thì tên chat thành "Hi", "Hi" lặp đi lặp lại rất xấu).
- **Hành động cụ thể:**
  - Sau lượt hỏi đáp đầu tiên của một cuộc trò chuyện mới:
    - Hệ thống tự động gửi yêu cầu phân tích ngắn tới mô hình (hoặc prompt tóm tắt nhanh) với nội dung:
      *"Dựa vào câu hỏi và câu trả lời đầu tiên: Hãy đặt một tiêu đề ngắn gọn từ 3 đến 5 từ tiếng Việt thể hiện đúng loài cây hoặc bệnh lý đang nói đến (Ví dụ: 'Bệnh vàng lá bưởi', 'Sầu riêng xì mủ thân', 'Chăm sóc lúa VietGAP', 'Sâu vẽ bùa trên cam',...). Nếu chỉ là chào hỏi thông thường, đặt tên là 'Trò chuyện chung'. Chỉ trả về đúng chuỗi tiêu đề, không kèm dấu ngoặc kép hay từ thừa."*
    - Tự động cập nhật tiêu đề mới này vào `conversations` và đồng bộ lên Supabase (`conversations.title`).

### B. Thay thế nút thùng rác `🗑` bằng Nút 3 chấm `...` và Popup Context Menu chuẩn App ChatGPT:
- **Tệp chỉnh sửa:** `src/components/sidebar/AppSidebar.tsx` & `src/types/chat.ts`
- **Tham chiếu thiết kế:** Chuẩn xác theo ảnh chụp màn hình ứng dụng ChatGPT chính thức (Ảnh mẫu do tác giả cung cấp):
  1. Trong `src/types/chat.ts`: Bổ sung trường `isPinned?: boolean` vào interface `Conversation`.
  2. Trong `AppSidebar.tsx`:
     - Thay thế nút thùng rác thô `<Trash2 ... />` ở mỗi hàng chat bằng nút **3 chấm ngang (`MoreHorizontal` của Lucide)** mỏng nhẹ (`p-1.5 rounded-lg hover:bg-black/5 dark:hover:bg-white/10 text-[#8e8e8e] hover:text-[#0d0d0d] dark:hover:text-white`).
     - Hỗ trợ cả **Click vào nút 3 chấm** và **Nhấn giữ (Long-press) vào hàng chat trên điện thoại**.
     - Khi kích hoạt, hiển thị **Popup Menu bo góc mềm mại** (`rounded-2xl shadow-xl bg-white dark:bg-[#212121] border border-black/10 dark:border-white/10 p-1.5 z-50 min-w-[160px] animate-in fade-in zoom-in-95`) gồm đúng **3 chức năng chuẩn ChatGPT**:
       - 📌 **Ghim / Bỏ ghim:**
         - Icon: `Pin` (strokeWidth 1.75).
         - Text: Nếu chưa ghim hiển thị *"Ghim"*, nếu đã ghim hiển thị *"Bỏ ghim"*.
         - Logic: Đưa các đoạn chat có `isPinned: true` lên một nhóm riêng trên đỉnh danh sách lịch sử có tiêu đề nhỏ: **"ĐÃ GHIM"**.
       - ✏️ **Đổi tên:**
         - Icon: `Pencil` / `SquarePen` (strokeWidth 1.75).
         - Text: *"Đổi tên"*.
         - Logic: Chuyển tiêu đề thành ô input nhỏ cho phép sửa trực tiếp và bấm Enter / lưu để cập nhật tên mới ngay lập tức (đồng bộ lên Supabase).
       - 🗑️ **Xoá:**
         - Icon: `Trash2` (strokeWidth 1.75, màu đỏ `text-red-500`).
         - Text: *"Xoá"* (màu đỏ `text-red-500`).
         - Logic: Xóa cuộc trò chuyện khỏi state và Supabase database.
     - Tự động đóng Popup khi người dùng nhấp ra ngoài (click outside).

---

## 🚀 TIÊU CHUẨN HOÀN TẤT & DEPLOY:
```bash
npm run build
git add -A
git commit -m "fix(agrivision): prohibit author backstory hallucinations, remove 1500+ header button, add AI auto-titling, and implement ChatGPT-style 3-dot context menu"
git push origin main
```
Render sẽ tự động build và triển khai bản cập nhật hoàn hảo trực tiếp tại: **https://ultra-project.onrender.com**.
