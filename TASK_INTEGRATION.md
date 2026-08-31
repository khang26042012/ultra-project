# 🌾 BẢN NHIỆM VỤ NÂNG CẤP TOÀN DIỆN: AGENT LOOP, WEB SEARCH 9ROUTER, STREAM THINKING & PROMPT CACHE
### Áp dụng cho: Repository `ultra-project` (Mô hình `ag/gemini-3.8-flash-high`)

---

## 📋 DANH SÁCH CÁC HẠNG MỤC CẦN NÂNG CẤP (TASKS):

### Task 1: Xóa Bỏ Hoàn Toàn Thông Tin Tác Giả Ở Chân Sidebar
- **Vị trí:** `src/components/sidebar/AppSidebar.tsx`
- **Hành động:** 
  - Tìm và xóa bỏ hoàn toàn khối `{/* Author Attribution Badge */}` (gồm dòng `AgriVision v1.0`, `Tác giả: Phan Trọng Khang`, `Lớp 9¹, THCS Vĩnh An (Vĩnh Long)` và đường kẻ `border-t`).
  - Chân Sidebar chỉ giữ lại nút Đăng nhập / Profile menu người dùng.

---

### Task 2: Tích Hợp Web Search Engine Từ 9Router
- **Endpoint đã kiểm thử thành công (HTTP 200 OK):**
  - **URL:** `http://nvnmc.asia:26627/v1/search`
  - **Headers:** 
    - `Authorization: Bearer sk-c276eac9b4322b74-tyrxri-1fc67c68`
    - `Content-Type: application/json`
  - **Payload mẫu:**
    ```json
    {
      "model": "ag",
      "query": "<từ khóa tìm kiếm>",
      "search_type": "web",
      "max_results": 5
    }
    ```
  - **Dữ liệu trả về:** Mảng `results` (chứa `title`, `url`, `snippet`, `content`) và trường tóm tắt `answer.text`.

---

### Task 3: Cập Nhật Master System Prompt Với Quy Định Tra Cứu Khắt Khe (Search Policy)
- **Vị trí:** `src/lib/systemPrompt.ts` (và `src/lib/system_prompt.md`)
- **Nội dung bổ sung vào mục Quy Tắc Bắt Buộc:**
  > **🛑 ĐIỀU LỆ TRA CỨU THỰC TẾ (WEB SEARCH POLICY):**
  > 1. Khi đề cập đến **tên thuốc bảo vệ thực vật, tên thương phẩm, hoạt chất sinh học, nồng độ pha chế, danh mục thuốc được phép lưu hành theo quy định Cục BVTV tại Việt Nam**: Nếu chưa chắc chắn 100% hoặc thông tin cần cập nhật mới nhất ➔ **BẮT BUỘC PHẢI GỌI TOOL `web_search` ĐỂ TRA CỨU NGAY**!
  > 2. Khi phân tích tình hình dịch bệnh mùa vụ, diễn biến thời tiết, hạn mặn tại **tỉnh Vĩnh Long và Đồng bằng sông Cửu Long**: **BẮT BUỘC PHẢI TRA CỨU THỰC TẾ** để có số liệu chính xác từ Chi cục Trồng trọt & BVTV Vĩnh Long.
  > 3. Tuyệt đối không bịa đặt tên thuốc, liều lượng phun hay giá cả thị trường nếu chưa được kiểm chứng qua kết quả tìm kiếm.

---

### Task 4: Hiển Thị Luồng Suy Luận `<think>` (Stream Thinking Accordion theo chuẩn DSH)
- Khi mô hình `ag/gemini-3.8-flash-high` gửi stream, chuỗi tư duy nằm trong `delta.reasoning_content` (hoặc bọc trong thẻ `<think>...</think>`).
- **Xây dựng Component `ThinkingBlock.tsx` trong tin nhắn chat:**
  - **Trong lúc đang stream suy luận:**
    - Khối Thinking mở ra ở đầu tin nhắn với hiệu ứng động: Icon 🧠 xoay nhẹ hoặc nhấp nháy, hiển thị dòng suy luận đang chạy theo thời gian thực (`live reasoning throughput`).
  - **Khi kết thúc suy luận (Settled / Bắt đầu ra câu trả lời chính):**
    - Khối Thinking **TỰ ĐỘNG THU GỌN (COLLAPSE)** lại thành một thanh toggle nhỏ gọn thanh lịch:  
      `💭 Đã suy luận trong Xs (Bấm để xem chi tiết)`.
    - Người dùng có thể bấm vào để mở rộng/thu gọn xem toàn bộ Chain-of-Thought bất kỳ lúc nào.
    - Màu sắc Light Mode: Nền xám nhạt `bg-[#f4f4f4]`, viền mảnh `border border-[#e5e5e5]`, chữ xám đen `text-[#5d5d5d]`.

---

### Task 5: Kiến Trúc Agent Loop Đa Bước & Giao Diện Gọi Tool Search (Mổ xẻ từ DeepSeek Harness)
1. **Kiến trúc Vòng lặp Agent (`src/app/api/chat/route.ts` - Agent Loop Pattern):**
   - Định nghĩa Tool `web_search` theo chuẩn Function Calling của OpenAI/Gemini:
     ```json
     {
       "type": "function",
       "function": {
         "name": "web_search",
         "description": "Tra cứu thông tin thực tế mới nhất về sâu bệnh, danh mục thuốc BVTV, tiêu chuẩn VietGAP và tình hình dịch hại tại Vĩnh Long.",
         "parameters": {
           "type": "object",
           "properties": {
             "query": { "type": "string", "description": "Từ khóa tìm kiếm chính xác" }
           },
           "required": ["query"]
         }
       }
     }
     ```
   - **Vòng lặp đa bước (Loop API):**
     - Khi Gemini trả về `tool_calls`:
       1. Bắn sự kiện SSE về Frontend hiển thị trạng thái: `🔍 Đang tra cứu: "<query>"...`.
       2. Gọi API `POST http://nvnmc.asia:26627/v1/search`.
       3. Đóng gói kết quả tìm kiếm vào tin nhắn `role: "tool"` và tiếp tục gọi lại Gemini (`loop boundary`).
       4. Vòng lặp tiếp tục tối đa 5 bước cho đến khi Gemini hoàn tất toàn bộ câu trả lời cuối cùng.
2. **Giao Diện Hiển Thị Tool Call (Frontend Tool Presentation):**
   - Khi đang tìm kiếm: Khối badge hiển thị nhấp nháy tinh tế: `🔍 Đang tra cứu dữ liệu thực tế: "..."`.
   - Khi tìm xong: Hiển thị thanh nguồn trích dẫn: `🌐 Đã tham khảo N nguồn tin tức` (người dùng bấm vào có thể xem danh sách link nguồn có favicon và tiêu đề).
3. **Tối Ưu Hóa Cache Prompt Token (DSH Prompt Cache Stability):**
   - Đảm bảo **System Prompt** và danh mục **Tool Definitions** luôn được giữ nguyên vẹn ở vị trí đầu tiên của mảng tin nhắn (Static Prefix).
   - Tuyệt đối không chèn timestamp ngẫu nhiên vào System Prompt để tận dụng tối đa cơ chế **Prompt Prefix Caching** của Gateway, giúp giảm 90% chi phí token và tăng tốc độ phản hồi tức thì.
