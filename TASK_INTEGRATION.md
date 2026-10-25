# 🌾 BẢN GIAO VIỆC NÂNG CẤP TOÀN DIỆN CHO ANTIGRAVITY AGENT
### Dự án: AgriVision (Repository: `ultra-project`)
### Phạm vi: Xóa Data Sidebar + Tích Hợp 9Router Search + Giao Diện Thinking Chuẩn ChatGPT/Claude + Agent Loop Đa Bước & Prompt Cache

---

## 🛠️ CHI TIẾT 5 NHIỆM VỤ CẦN THỰC HIỆN TRỰC TIẾP:

### 1. XÓA BỎ KHỐI THÔNG TIN TÁC GIẢ Ở CHÂN SIDEBAR
- **Tệp chỉnh sửa:** `src/components/sidebar/AppSidebar.tsx`
- **Hành động:** 
  - Tìm và xóa bỏ hoàn toàn khối `{/* Author Attribution Badge */}` (gồm dòng chữ `AgriVision v1.0`, `Tác giả: Phan Trọng Khang`, `Lớp 9¹, THCS Vĩnh An (Vĩnh Long)` và đường viền `border-t`).
  - Chân Sidebar chỉ giữ lại nút Đăng nhập / Profile Menu người dùng sạch sẽ.

---

### 2. THIẾT KẾ GIAO DIỆN THINKING CHUẨN CHATGPT (o1/o3) & CLAUDE (THAY THẾ HỘP CARD CŨ)
- **Tệp chỉnh sửa:** `src/components/chat/ChatMessage.tsx`
- **Hành động:** 
  - Loại bỏ hoàn toàn khối hộp card viền xám đóng khung thô kệch cũ.
  - Áp dụng chuẩn thiết kế tối giản đẳng cấp của ChatGPT & Claude:
    1. **Khi đang stream suy luận:** Hiển thị một dòng text tối giản có hiệu ứng shimmer/pulse nhẹ nhàng: `💭 Đang suy nghĩ...` (màu xám `text-[#737373]`, không khung viền).
    2. **Khi đã suy luận xong (Settled):** **TỰ ĐỘNG THU GỌN** thành duy nhất một dòng text mỏng nằm ngay trên câu trả lời chính:  
       `Đã suy luận trong Xs ▾` (hoặc `Tiến trình suy luận ▾`).  
       - Style: `text-xs font-medium text-[#737373] hover:text-[#0d0d0d] dark:text-[#a3a3a3] dark:hover:text-white transition-colors cursor-pointer`.
    3. **Khi người dùng click mở ra (Expanded):** Hiển thị dạng **Khối thụt lề có vạch kẻ đứng thanh mảnh bên trái (Left Accent Border)**:  
       `border-l-2 border-[#e5e5e5] dark:border-[#383838] pl-3.5 my-2 max-h-72 overflow-y-auto text-[13px] text-[#5d5d5d] dark:text-[#a3a3a3] font-sans leading-relaxed`. Dùng font chữ thường (sans-serif) dễ đọc, tuyệt đối không dùng font monospace code terminal thô ráp.

---

### 3. TÍCH HỢP WEB SEARCH ENGINE TỪ 9ROUTER (ĐÃ KIỂM THỬ HTTP 200 OK)
- **Endpoint 9Router:**
  - **URL:** `http://nvnmc.asia:26627/v1/search`
  - **Headers:** 
    - `Authorization: Bearer sk-c276eac9b4322b74-tyrxri-1fc67c68`
    - `Content-Type: application/json`
  - **Payload gửi đi:**
    ```json
    {
      "model": "ag",
      "query": "<từ khóa tra cứu thực tế>",
      "search_type": "web",
      "max_results": 5
    }
    ```
  - **Dữ liệu trả về:** Mảng `results` (chứa `title`, `url`, `snippet`, `content`) và trường tóm tắt `answer.text`.

---

### 4. CẬP NHẬT MASTER SYSTEM PROMPT VỚI QUY ĐỊNH TRA CỨU KHẮT KHE (SEARCH POLICY)
- **Tệp chỉnh sửa:** `src/lib/systemPrompt.ts` (và `src/lib/system_prompt.md`)
- **Bổ sung điều lệ bắt buộc tra cứu:**
  > **🛑 ĐIỀU LỆ TRA CỨU WEB BẮT BUỘC (SEARCH-FIRST POLICY):**
  > 1. Khi đề cập đến **tên thuốc bảo vệ thực vật, tên thương phẩm, hoạt chất sinh học, nồng độ pha chế, danh mục thuốc được phép lưu hành theo quy định Cục BVTV tại Việt Nam**: Nếu chưa chắc chắn 100% hoặc thông tin cần cập nhật mới nhất ➔ **BẮT BUỘC PHẢI GỌI TOOL `web_search` ĐỂ TRA CỨU NGAY**!
  > 2. Khi phân tích tình hình dịch bệnh mùa vụ, diễn biến thời tiết, hạn mặn tại **tỉnh Vĩnh Long và Đồng bằng sông Cửu Long**: **BẮT BUỘC PHẢI TRA CỨU THỰC TẾ** để có số liệu chính xác từ Chi cục Trồng trọt & BVTV Vĩnh Long.
  > 3. Cấm tuyệt đối bịa đặt tên thuốc, liều lượng phun hay giá cả thị trường nếu chưa được kiểm chứng qua kết quả tìm kiếm thực tế.

---

### 5. KIẾN TRÚC AGENT LOOP ĐA BƯỚC & GIAO DIỆN TOOL CALL SEARCH (CHUẨN DSH)
- **Tệp chỉnh sửa:** `src/app/api/chat/route.ts` & `src/components/chat/ChatMessage.tsx`
- **Quy trình Agent Loop:**
  1. Khai báo Tool `web_search` trong request gửi đến Gemini Gateway.
  2. Khi mô hình trả về `tool_calls` yêu cầu tìm kiếm:
     - Gửi event stream về giao diện hiển thị badge: `🔍 Đang tra cứu dữ liệu thực tế: "<query>"...`.
     - Thực hiện gọi API `POST http://nvnmc.asia:26627/v1/search`.
     - Đóng gói kết quả trả về vào message `role: "tool"` và tiếp tục vòng lặp gọi lại Gemini.
     - Vòng lặp tự động lặp lại (hỗ trợ gọi nhiều lần API liên tiếp) cho đến khi hoàn tất câu trả lời cuối cùng.
  3. **Giao diện hiển thị nguồn tin:** Khi có kết quả tìm kiếm, hiển thị thanh nguồn trích dẫn nhỏ gọn: `🌐 Đã tham khảo 5 nguồn thông tin thực tế` (bấm vào mở danh sách link có tiêu đề và favicon).
  4. **Tối ưu Prompt Cache Token:** Giữ nguyên System Prompt và Tool Definitions ở vị trí đầu tiên của mảng tin nhắn (Static Prefix) để kích hoạt cơ chế Server-side Prompt Caching của Gateway, giảm 90% chi phí và tăng tốc độ phản hồi.

---

## 🚀 LỆNH COMMIT & PUSH:
```bash
git add -A
git commit -m "feat(agrivision): clean sidebar author, integrate 9router web search, upgrade chatgpt/claude thinking UI, and implement multi-step agent loop with prompt caching"
git push origin main
```
