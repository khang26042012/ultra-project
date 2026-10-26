# 🚀 PROMPT THIẾT LẬP TOÀN DIỆN CHO AGENT (SETUP, CLONE, SKILLS & APIS)

Chào bạn, bạn là kỹ sư AI phụ trách phát triển hệ sinh thái **AgriVision (Ultra Project)** cho tác giả **Phan Trọng Khang** (Học sinh lớp **9¹**, **Trường THCS Vĩnh An**, tỉnh Vĩnh Long).

Dưới đây là thông tin chỉ đạo toàn diện để khởi tạo môi trường, nạp kỹ năng thiết kế, cấu hình Cloud Database và kết nối toàn bộ hệ thống API Keys:

---

## 📦 1. CLONE REPOSITORY & CÀI ĐẶT MÔI TRƯỜNG

Mở Terminal trong workspace của bạn và chạy tuần tự các lệnh sau:

```bash
# 1. Clone mã nguồn chính thức bằng GitHub Token đã cấp quyền
git clone https://YOUR_GITHUB_TOKEN@github.com/khang26042012/ultra-project.git
cd ultra-project

# 2. Cài đặt toàn bộ thư viện phụ thuộc (Next.js 16, React 19, Tailwind CSS v4, Lucide, GSAP, Supabase)
npm install

# 3. Chạy thử kiểm tra môi trường dev
npm run dev
```

Tạo tệp `.env.local` tại thư mục gốc của dự án với đầy đủ cấu hình:
```env
# AI Model Gateway & 9Router Search
AI_GATEWAY_URL=http://nvnmc.asia:26627/v1/chat/completions
AI_GATEWAY_KEY=YOUR_AI_GATEWAY_KEY
SEARCH_API_URL=http://nvnmc.asia:26627/v1/search
DEFAULT_MODEL=ag/gemini-3.8-flash-high
FAST_MODEL=ag/gemini-3.8-flash

# Supabase Cloud Database (PostgreSQL Singapore)
NEXT_PUBLIC_SUPABASE_URL=https://dffycwpkbfnaqptuvvju.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRmZnljd3BrYmZuYXFwdHV2dmp1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTI5NDA4NzgsImV4cCI6MjEwODUxNjg3OH0.hHWZ0haM0sxF_X9mKawdd39bmVp_TdAQKonikyf04Yk

# Deployment & CI/CD Keys
RENDER_API_KEY=YOUR_RENDER_KEY
RENDER_SERVICE_ID=srv-dberh3gae00c73e41ddg
GITHUB_TOKEN=YOUR_GITHUB_TOKEN
```

---

## 🧠 2. NẠP VÀ ÁP DỤNG BỘ KỸ NĂNG (SKILLS)

Trong thư mục `skills/` của repository đã có sẵn cẩm nang thiết kế và tiêu chuẩn kỹ thuật. Bạn **BẮT BUỘC PHẢI TUÂN THỦ**:
1. **`skills/ui-ux-pro-max` & `skills/ui-styling`**:
   - Thiết kế chuẩn phong cách SaaS hiện đại (Linear / ChatGPT): Mặc định Light Mode, nền sáng `#ffffff`, panel `#f9f9f9`, viền xám mảnh `#e5e5e5`, chữ đen tối giản `#0d0d0d`.
   - Hệ thống icon Lucide nét thanh mảnh (`strokeWidth={1.5}`), bảng biểu Markdown Table tự động co giãn và cuộn ngang linh hoạt.
2. **`skills/gsap-core` & `skills/gsap-react`**:
   - Sử dụng hook `useGSAP` khi render animation micro-interactions, hiệu ứng xuất hiện tin nhắn và transition, đảm bảo đạt chuẩn mượt mà 60 FPS không giật lag.
3. **`skills/design-system` & `skills/brand`**:
   - Duy trì tính nhất quán của token màu đơn sắc (monochrome) và nhịp điệu khoảng cách (padding/margin 4px, 8px, 12px, 16px).

---

## 🗄️ 3. KẾT NỐI & QUẢN TRỊ SUPABASE CLOUD DATABASE

Dự án sử dụng cơ sở dữ liệu Supabase PostgreSQL đặt tại Singapore (`https://dffycwpkbfnaqptuvvju.supabase.co`). Các bảng dữ liệu đã được khởi tạo sẵn:
1. **`profiles`**: Lưu trữ thông tin tài khoản người dùng (`id`, `email`, `name`, `password_hash`, `avatar_url`, `role`).
2. **`conversations`**: Lưu danh sách các phiên trò chuyện/chẩn đoán (`id`, `user_id`, `title`, `model`).
3. **`messages`**: Lưu chi tiết từng tin nhắn (`id`, `conversation_id`, `role`, `content`, `image_url`, `thought`, `sources`, `timestamp`).
- Thư viện kết nối: `@supabase/supabase-js`.
- Module khởi tạo: `src/lib/supabase.ts` xuất instance `supabase`.
- Quản lý đồng bộ: `src/context/ChatContext.tsx` tự động đồng bộ hai chiều giữa Cloud Database và `localStorage` (hỗ trợ sử dụng offline và đồng bộ đa thiết bị).

---

## 🔌 4. ĐẶC TẢ CHI TIẾT CÁC API & CƠ CHẾ VẬN HÀNH

### A. AI Model Gateway (OpenAI Compatible)
- **Chat Endpoint:** `POST http://nvnmc.asia:26627/v1/chat/completions`
- **API Key:** `YOUR_AI_GATEWAY_KEY`
- **Mô hình bắt buộc (Locked Model):** `ag/gemini-3.8-flash-high` (chế độ suy luận sâu cho chẩn đoán bệnh học lâm sàng).
- **Mô hình phụ (Fast Model):** `ag/gemini-3.8-flash`
- ⚠️ **QUY TẮC CỐT TỬ:** **TUYỆT ĐỐI KHÔNG DÙNG** `ag/gemini-4-argon-high` (tránh bị Gateway rate-limit 5 tiếng).
- **Server-side Prompt Caching:** Giữ System Prompt và Tool Definitions làm tiền tố tĩnh (`Static Prefix`) ở đầu mảng messages để Gateway tự động cache, giảm 90% chi phí token và tăng tốc độ trả lời.

### B. 9Router Real-time Web Search Tool
- **Endpoint:** `POST http://nvnmc.asia:26627/v1/search`
- **Headers:** `Authorization: Bearer YOUR_AI_GATEWAY_KEY`
- **Cơ chế:** Khi mô hình yêu cầu `tool_calls` với tool `web_search`, gọi endpoint này và trả kết quả dưới dạng `role: "tool"` trong chuỗi Agent Loop đa bước.

### C. Render Cloud Hosting (Auto Deploy)
- **Trang web chính thức:** `https://ultra-project.onrender.com`
- **Cơ chế triển khai tự động:** Mỗi khi bạn hoàn thành code, chạy kiểm tra `npm run build` và push lên nhánh `main` của GitHub:
  ```bash
  git add -A
  git commit -m "feat: your descriptive update"
  git push origin main
  ```
  Render sẽ tự động trigger build và cập nhật bản mới nhất lên Internet trong vòng 1-2 phút.