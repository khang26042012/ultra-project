# 🤖 ChatGPT Clone — Pixel-Perfect Next.js AI Web App

Một ứng dụng web clone giao diện **ChatGPT** đạt chuẩn **Pixel-Perfect**, được xây dựng trên nền tảng **Next.js 16 (App Router)**, **React 19**, **GSAP Animations**, **Tailwind CSS**, và **Shadcn UI**. Ứng dụng tích hợp bộ điều phối mô hình AI đa phương thức hỗ trợ luồng streaming thời gian thực (SSE) qua Gateway OpenAI-compatible.

---

## 🌟 TÍNH NĂNG NỔI BẬT

### 1. Giao diện ChatGPT Chuẩn Mực & Mượt Mà
- **AppSidebar (Thanh bên thông minh):**
  - Tự động gom nhóm cuộc hội thoại theo dòng thời gian (`Today`, `Yesterday`, `Previous 7 Days`, `Previous 30 Days`).
  - Tìm kiếm cuộc trò chuyện nhanh (`Search`), tạo chat mới (`New Chat`), quản lý và xóa hội thoại.
  - Menu tài khoản cá nhân, đổi theme (`Dark / Light Mode`) và nâng cấp gói.
  - Hiệu ứng thu gọn/mở rộng thanh bên mượt mà bằng **GSAP**.
- **FloatingInputIsland (Thanh nhập tin nhắn đảo nổi):**
  - Thiết kế nổi hiện đại ở đáy màn hình chuẩn phong cách OpenAI / Claude.
  - Hỗ trợ nút đính kèm tệp (`Plus`), kích hoạt chế độ suy luận chuyên sâu (`Thinking`), nhập giọng nói (`Microphone`).
  - **Menu chọn Model động:** Chuyển đổi linh hoạt giữa `Gemini 3.8 Flash`, `Gemini 3.8 Flash High`, `Gemini 3.7 Flash`, `Claude Sonnet 4.6`, và `GPT-4o`.
- **Trải nghiệm Hội thoại Đỉnh Cao:**
  - Hỗ trợ hiển thị Markdown đầy đủ (bảng biểu, in đậm, danh sách).
  - Khối mã nguồn (`CodeBlock`) tô màu cú pháp (Syntax Highlighting) kèm nút sao chép (`Copy`) một chạm.
  - Phản hồi dạng dòng ký tự chạy chữ theo thời gian thực (Server-Sent Events streaming).

### 2. Kiến Trúc Modular Skills
Toàn bộ hệ thống kỹ năng thiết kế, animation và tự động hóa được tích hợp tại thư mục `skills/`:
- **`skills/gsap`**: Thư viện hiệu ứng động chuyên sâu (GSAP Core, React, ScrollTrigger, Timeline).
- **`skills/ui-ux-pro-max` & `ui-styling`**: Hệ thống Design Tokens, WCAG contrast và chuẩn UI/UX.
- **`skills/ai-site-cloner`**: Công cụ sao chép và tái hiện giao diện web độc lập.
- **`skills/railway-automation`**: Tự động hóa CI/CD và triển khai cloud infrastructure.

---

## 🏗️ CẤU TRÚC THƯ MỤC DỰ ÁN

```
chatgpt-clone/
├── src/
│   ├── app/
│   │   ├── api/chat/route.ts      # API Endpoint proxy stream SSE về AI Gateway
│   │   ├── layout.tsx             # Root layout cấu hình theme & font chữ
│   │   ├── page.tsx               # Trang chính ứng dụng Chat
│   │   └── globals.css            # Biến CSS Tailwind & Dark/Light mode tokens
│   ├── components/
│   │   ├── chat/                  # Header, Message, CodeBlock, EmptyState
│   │   ├── input/                 # FloatingInputIsland (Thanh nhập nổi)
│   │   ├── sidebar/               # AppSidebar & ProfileMenu
│   │   ├── modals/                # SettingsModal & UpgradeModal
│   │   └── ui/                    # Các component cơ bản (Button, Dialog, ...)
│   ├── context/
│   │   └── ChatContext.tsx        # Quản lý State trò chuyện & API integration
│   ├── types/
│   │   └── chat.ts                # Định nghĩa kiểu dữ liệu TypeScript (Message, Model, ...)
│   └── lib/
│       └── utils.ts               # Tiện ích cn (clsx + tailwind-merge)
├── public/                        # Thư mục tài nguyên tĩnh (Images, Icons, SEO)
├── skills/                        # Bộ sưu tập các Modular Skills (GSAP, UI/UX, Cloner, ...)
├── Dockerfile                     # Docker container triển khai production
├── docker-compose.yml             # Cấu hình chạy nhanh với Docker Compose
├── package.json                   # Dependencies (Next 16, React 19, GSAP 3.15, Tailwind)
├── tsconfig.json                  # Cấu hình TypeScript với Path Alias (@/*)
├── next.config.ts                 # Cấu hình Next.js App Router
└── .env.example                   # Tệp mẫu biến môi trường
```

---

## 🚀 HƯỚNG DẪN CÀI ĐẶT & CHẠY DỰ ÁN

### 1. Yêu Cầu Hệ Thống
- **Node.js:** Phiên bản `18.18.0` hoặc cao hơn (khuyên dùng Node 20+).
- **Trình quản lý gói:** `npm`, `pnpm` hoặc `yarn`.

### 2. Cài Đặt Dependencies
```bash
# Di chuyển vào thư mục dự án
cd chatgpt-clone

# Cài đặt toàn bộ thư viện
npm install
```

### 3. Cấu Hình Biến Môi Trường
Tạo tệp `.env.local` từ tệp mẫu:
```bash
cp .env.example .env.local
```

Điền thông tin Gateway của bạn:
```env
AI_GATEWAY_URL=http://nvnmc.asia:26627/v1/chat/completions
AI_GATEWAY_KEY=sk-c276eac9b4322b74-tyrxri-1fc67c68
DEFAULT_MODEL=ag/gemini-3.8-flash
```

### 4. Khởi Chạy Môi Trường Development
```bash
npm run dev
```
Mở trình duyệt và truy cập: `http://localhost:3000` để trải nghiệm!

---

## 🐳 TRIỂN KHAI VỚI DOCKER

Dự án đã sẵn sàng với cấu hình Docker tối ưu:

```bash
# Build và chạy với Docker Compose
docker compose up -d --build
```

Ứng dụng sẽ hoạt động tại cổng `http://localhost:3000`.

---

## 👤 TÁC GIẢ & BẢN QUYỀN
- **Tác giả:** Phan Trọng Khang ([@khang26042012](https://github.com/khang26042012))
- **Giấy phép:** MIT License
