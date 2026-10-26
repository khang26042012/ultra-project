# 🚀 BẢN GIAO VIỆC: SỬA TRIỆT ĐỂ BỊA ĐẶT THÔNG TIN TÁC GIẢ, XÓA NÚT 1500+, TÍCH HỢP CHIP LPU ĐẶT TÊN SIÊU TỐC & CONTEXT MENU CHATGPT
### Dự án: AgriVision (ultra-project)
### Tác giả: Phan Trọng Khang (Lớp 9¹, THCS Vĩnh An, Vĩnh Long)

---

## 🛑 NHIỆM VỤ 1: CHẶN ĐỨNG HOÀN TOÀN VIỆC AI BỊA ĐẶT TIỂU SỬ / TỰ SỰ VỀ TÁC GIẢ
- **Tệp chỉnh sửa:** `src/lib/systemPrompt.ts` & `src/lib/system_prompt.md`
- **Vấn đề:** AI đang tự ý bịa đặt câu chuyện cảm động, tiểu sử đời tư và phát biểu thay tác giả (ví dụ: *"Khang sinh ra lớn lên ở Mang Thít...", "Khang chứng kiến gia đình chòm xóm...", "Một học sinh lớp 9¹ đã xây dựng kho dữ liệu như thế nào?...", "Ước mơ bình dị của cậu học trò trường làng: Tâm nguyện của Khang không phải để lấy giải thưởng mà là..."*). Tác giả rất khó chịu vì điều này hoàn toàn là bịa đặt!
- **Hành động cụ thể:**
  - Thêm điều lệ nghiêm cấm tối cao vào System Prompt:
    ```markdown
    ## 🚫 ĐIỀU LỆ TUYỆT ĐỐI CẤM: KHÔNG BỊA ĐẶT TIỂU SỬ, ĐỜI TƯ VÀ CẢM XÚC CỦA TÁC GIẢ PHAN TRỌNG KHANG

    1. **NGHIÊM CẤM TỰ Ý KỂ LỂ TIỂU SỬ:** Tuyệt đối KHÔNG ĐƯỢC tự nghĩ ra hoàn cảnh gia đình, tuổi thơ, động lực cá nhân hay hành trình của bạn Khang (CẤM các câu như: "Khang sinh ra lớn lên ở...", "Khang chứng kiến gia đình...", "Ước mơ bình dị của cậu học trò trường làng...", "Khang nung nấu quyết tâm...", "Tâm nguyện của Khang không phải để lấy giải thưởng...").
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
    - Hoàn toàn tối giản, thông thoáng, liền mạch với nền web.

---

## ⚡ NHIỆM VỤ 3: TÁCH RIÊNG LUỒNG ĐẶT TÊN CHAT — KHÔNG NHÉT SYSTEM PROMPT LỚN, DÙNG CHIP LPU SIÊU NHANH
- **Tệp chỉnh sửa:** `src/context/ChatContext.tsx` (và tạo endpoint riêng `src/app/api/chat/title/route.ts`)
- **Nguyên lý kiến trúc 2 bước (Decoupled Two-Step Architecture):**
  1. **Bước 1: Đặt tên hội thoại (Titling Call):**
     - Tuyệt đối **KHÔNG nhồi nhét Master System Prompt 10.000 token** vào đây (vừa tốn chi phí vừa chậm).
     - Chỉ dùng một Prompt tí hon:
       ```typescript
       const titlePrompt = [
         {
           role: 'system',
           content: 'Bạn là trợ lý đặt tiêu đề tiếng Việt ngắn gọn 3-5 từ cho ứng dụng nông nghiệp AgriVision (ví dụ: "Bệnh vàng lá bưởi", "Sầu riêng xì mủ", "Tư vấn VietGAP lúa"). Nếu chỉ chào hỏi, đặt là "Trò chuyện nông nghiệp". Chỉ trả về đúng chuỗi tiêu đề, không dấu ngoặc kép, không từ thừa.'
         },
         {
           role: 'user',
           content: userFirstMessage
         }
       ];
       ```
     - **Nền tảng suy luận LPU siêu tốc & Free:**
       - Hỗ trợ Groq LPU Chip (`https://api.groq.com/openai/v1`, model `llama-3.1-8b-instant` hoặc `qwen-2.5-32b`) / OpenRouter Free (`qwen/qwen-2.5-7b-instruct:free`) / hoặc fallback sang `ag/gemini-3.8-flash-low` với `max_tokens: 15`.
       - Thời gian phản hồi: **Dưới 0.2 giây**!
       - Cập nhật tiêu đề này ngay vào state và Supabase `conversations.title`.
  2. **Bước 2: Gửi API lần 2 thực hiện yêu cầu người dùng (Main Diagnostic Stream):**
     - Sau khi (hoặc song song khi) đặt tên, API chính mới được gọi với đầy đủ Master Clinical System Prompt + Tools (In-context RAG + 9Router Web Search) trên model `ag/gemini-3.8-flash-high` để chẩn đoán chuyên sâu và stream về cho người dùng.

---

## 📱 NHIỆM VỤ 4: NÂNG CẤP POPUP CONTEXT MENU CHUẨN CHATGPT APP
- **Tệp chỉnh sửa:** `src/components/sidebar/AppSidebar.tsx` & `src/types/chat.ts`
- **Hành động cụ thể:**
  1. Trong `src/types/chat.ts`: Thêm `isPinned?: boolean` vào interface `Conversation`.
  2. Trong `AppSidebar.tsx`:
     - Thay nút thùng rác thô bằng nút **3 chấm ngang (`MoreHorizontal`)**.
     - Hỗ trợ cả **Click vào nút 3 chấm** và **Nhấn giữ (Long-press trên mobile)** vào cuộc trò chuyện.
     - Hiển thị Popup Menu chuẩn app ChatGPT (theo đúng ảnh mẫu của tác giả):
       1. 📌 **Ghim / Bỏ ghim:** Đưa các đoạn chat có `isPinned: true` lên mục riêng trên đỉnh có tiêu đề **"ĐÃ GHIM"**.
       2. ✏️ **Đổi tên:** Cho phép người dùng chỉnh sửa trực tiếp tên đoạn chat.
       3. 🗑️ **Xoá:** Chữ màu đỏ (`text-red-500`), bấm để xóa cuộc trò chuyện.
     - Tự động đóng popup khi click ra ngoài.

---

## 🚀 TIÊU CHUẨN HOÀN TẤT & DEPLOY:
```bash
npm run build
git add -A
git commit -m "feat(agrivision): clean author prompt, remove header button, decouple LPU fast titling, and implement ChatGPT context menu"
git push origin main
```
Render sẽ tự động build và triển khai bản cập nhật trực tiếp tại: **https://ultra-project.onrender.com**.
