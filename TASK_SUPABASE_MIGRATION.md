# 🗄️ BẢN GIAO VIỆC TÍCH HỢP CLOUD DATABASE: SUPABASE (POSTGRESQL)
### Dự án: AgriVision (ultra-project)
### Tác giả: Phan Trọng Khang (Lớp 9¹, THCS Vĩnh An, Vĩnh Long)
### Mục tiêu: Di chuyển toàn bộ hệ thống lưu trữ (Hồ sơ người dùng, Lịch sử hội thoại, Tin nhắn chẩn đoán) lên Supabase Cloud Database để đồng bộ xuyên suốt đa thiết bị.

---

## 🔑 1. THÔNG SỐ CẤU HÌNH SUPABASE (ĐÃ KHỞI TẠO TẠI SINGAPORE)

Hạ tầng Supabase đã được khởi tạo sẵn sàng tại khu vực Singapore (gần Việt Nam, tốc độ truy vấn cực nhanh):
- **Project URL:** `https://dffycwpkbfnaqptuvvju.supabase.co`
- **Anon Public Key:** `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRmZnljd3BrYmZuYXFwdHV2dmp1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTI5NDA4NzgsImV4cCI6MjEwODUxNjg3OH0.hHWZ0haM0sxF_X9mKawdd39bmVp_TdAQKonikyf04Yk`
- **Cấu hình môi trường:** Thêm 2 biến sau vào tệp `.env.local`:
  ```env
  NEXT_PUBLIC_SUPABASE_URL=https://dffycwpkbfnaqptuvvju.supabase.co
  NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRmZnljd3BrYmZuYXFwdHV2dmp1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTI5NDA4NzgsImV4cCI6MjEwODUxNjg3OH0.hHWZ0haM0sxF_X9mKawdd39bmVp_TdAQKonikyf04Yk
  ```
*(Lưu ý: Các biến này cũng đã được nạp sẵn lên Cloud hosting Render để khi build production không bị thiếu)*.

---

## 🗃️ 2. CẤU TRÚC BẢNG CƠ SỞ DỮ LIỆU (DATABASE SCHEMA)
*(Toàn bộ 3 bảng bên dưới đã được tạo sẵn trên database và đã mở quyền truy cập RLS cho Anon key)*:

1. **Bảng `profiles` (Tài khoản người dùng):**
   - `id` (TEXT, PRIMARY KEY): Khóa định danh người dùng.
   - `email` (TEXT, UNIQUE): Email đăng nhập.
   - `name` (TEXT): Tên hiển thị người dùng / bà con nông dân.
   - `avatar_url` (TEXT): Ảnh đại diện hoặc URL ảnh.
   - `role` (TEXT, DEFAULT 'farmer'): Phân quyền người dùng.
   - `created_at` (TIMESTAMPTZ, DEFAULT NOW()).
   - `updated_at` (TIMESTAMPTZ, DEFAULT NOW()).

2. **Bảng `conversations` (Danh sách đoạn hội thoại chẩn đoán):**
   - `id` (TEXT, PRIMARY KEY): ID phiên chat.
   - `user_id` (TEXT, REFERENCES profiles.id ON DELETE CASCADE): ID người sở hữu phiên chat.
   - `title` (TEXT): Tiêu đề đoạn hội thoại (tự động đặt tên theo ca bệnh cây trồng).
   - `model` (TEXT, DEFAULT 'ag/gemini-3.8-flash-high'): Mô hình AI sử dụng.
   - `created_at` (TIMESTAMPTZ, DEFAULT NOW()).
   - `updated_at` (TIMESTAMPTZ, DEFAULT NOW()).

3. **Bảng `messages` (Chi tiết từng tin nhắn):**
   - `id` (TEXT, PRIMARY KEY): ID tin nhắn.
   - `conversation_id` (TEXT, REFERENCES conversations.id ON DELETE CASCADE): ID đoạn chat chứa tin nhắn.
   - `role` (TEXT): 'user' | 'assistant' | 'system' | 'tool'.
   - `content` (TEXT): Nội dung câu hỏi hoặc phản hồi chẩn đoán.
   - `image_url` (TEXT, NULLABLE): Chuỗi Base64 hoặc link ảnh lá/thân/trái cây bệnh.
   - `thought` (TEXT, NULLABLE): Quá trình suy luận phân tích bệnh học lâm sàng.
   - `sources` (JSONB, NULLABLE): Mảng các nguồn web search đã trích dẫn.
   - `timestamp` (TEXT): Thời gian gửi tin.
   - `created_at` (TIMESTAMPTZ, DEFAULT NOW()).

---

## 💻 3. HƯỚNG DẪN LẬP TRÌNH TÍCH HỢP VÀO SOURCE CODE

### Bước 1: Cài đặt SDK Supabase
```bash
npm install @supabase/supabase-js
```

### Bước 2: Tạo tệp Client Supabase (`src/lib/supabase.ts`)
```typescript
import { createClient } from '@supabase/supabase-js';

const supabaseUrl =
  process.env.NEXT_PUBLIC_SUPABASE_URL ||
  'https://dffycwpkbfnaqptuvvju.supabase.co';
const supabaseAnonKey =
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY ||
  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRmZnljd3BrYmZuYXFwdHV2dmp1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTI5NDA4NzgsImV4cCI6MjEwODUxNjg3OH0.hHWZ0haM0sxF_X9mKawdd39bmVp_TdAQKonikyf04Yk';

export const supabase = createClient(supabaseUrl, supabaseAnonKey);
```

### Bước 3: Cập nhật luồng lưu trữ trong `src/context/ChatContext.tsx`
1. **Đăng nhập & Tài khoản (Auth & Profile sync):**
   - Khi người dùng đăng nhập hoặc cập nhật profile: Gọi lệnh `supabase.from('profiles').upsert({...})` để lưu thông tin tài khoản lên Cloud.
2. **Quản lý Phiên chat (Conversations sync):**
   - Khi tạo mới: Gọi `supabase.from('conversations').upsert({...})`.
   - Khi xóa cuộc trò chuyện: Gọi `supabase.from('conversations').delete().eq('id', convId)`.
   - Khi đổi tên tiêu đề phiên chat: Gọi `supabase.from('conversations').update({ title, updated_at: new Date() }).eq('id', convId)`.
3. **Quản lý Tin nhắn (Messages sync):**
   - Mỗi khi người dùng bấm gửi tin nhắn hoặc AI stream phản hồi hoàn tất: Gọi `supabase.from('messages').upsert({...})`.
4. **Khởi tạo dữ liệu khi mở trang (Initial Data Load):**
   - Khi app vừa tải (hoặc khi đổi tài khoản): Kéo danh sách hội thoại từ Supabase về sắp xếp theo `updated_at DESC`.
   - Nạp các tin nhắn thuộc hội thoại đang chọn từ bảng `messages`.
5. **Cơ chế Fallback thông minh (Hybrid Local & Cloud Storage):**
   - Luôn duy trì bản cache trong `localStorage` song song để app có thể hiển thị tức thì không có độ trễ trắng trang (zero latency) và vẫn hoạt động bền bỉ khi mạng chập chờn.

---

## 🚀 4. QUY TRÌNH KIỂM THỬ VÀ DEPLOY
```bash
# 1. Chạy build kiểm tra không có lỗi kiểu TypeScript
npm run build

# 2. Commit toàn bộ thay đổi và push lên nhánh main
git add -A
git commit -m "feat(storage): migrate entire chat history, messages, and user profiles to Supabase cloud database"
git push origin main
```
Hệ thống Render sẽ tự động trigger build và triển khai bản web mới nhất tại: **https://ultra-project.onrender.com**.
