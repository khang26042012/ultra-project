# 🌾 AgriVision (Ultra Project) — Bác Sĩ Cây Trồng Lâm Sàng AI & Toàn Thư Bệnh Học 1.500+ Cây Trồng

> **Công trình nghiên cứu khoa học kỹ thuật dành cho học sinh trung học (Năm học 2026 - 2027)**  
> *Lĩnh vực: Hệ thống phần mềm (Mã 08) — Cuộc thi KHKT cấp tỉnh.*  
> **Website chính thức:** [https://ultra-project.onrender.com](https://ultra-project.onrender.com)  
> **Kho lưu trữ GitHub:** [https://github.com/khang26042012/ultra-project](https://github.com/khang26042012/ultra-project)

---

## 🌟 GIỚI THIỆU TỔNG QUAN

**AgriVision** là hệ sinh thái AI trợ lý Bác sĩ Cây trồng Lâm sàng chuyên sâu đạt chuẩn **Pixel-Perfect SaaS (Linear & ChatGPT)**, được xây dựng trên nền tảng **Next.js 16 (App Router / Turbopack)**, **React 19**, **GSAP Animations 60 FPS**, **Tailwind CSS v4** và **Supabase PostgreSQL**.

Dự án ra đời nhằm giải quyết nỗi đau lớn nhất của bà con nông dân Vĩnh Long, Đồng bằng Sông Cửu Long và 63 tỉnh thành: **phát hiện bệnh muộn, nhầm lẫn giữa các ca bệnh kép có triệu chứng tương đồng và phun sai thuốc bảo vệ thực vật hóa học gây cháy lá, chai đất và ô nhiễm nguồn nước.**

---

## 🚀 6 TRỤ CỘT ĐỘT PHÁ TOÀN DIỆN CỦA AGRIVISION

### 1. Siêu Cơ Sở Dữ Liệu Bệnh Học 1.502 Loài Cây Trồng (Pillar 6)
- **Quy mô tri thức:** **1.502 loài cây trồng độc nhất** và **3.020 hồ sơ ca bệnh học lâm sàng chi tiết**.
- **Độ bao phủ đa dạng:** Cây ăn trái đặc sản ĐBSCL, lúa nước & hoa màu, rau củ gia vị, nấm, cây công nghiệp xuất khẩu Tây Nguyên/Đông Nam Bộ, dược liệu quý Tây Bắc/Đông Bắc và các loại cây kinh tế quốc tế công nghệ cao (Việt quất, Dâu tây New Zealand, Nho mẫu đơn, Wasabi Đà Lạt, Nho thân gỗ Nam Mỹ, Cherry, Vanilla, Saffron,...).
- **100% Chuẩn VietGAP Sinh Học:** Rà soát và kiểm định nghiêm ngặt, tuyệt đối không chứa bất kỳ hoạt chất cấm độc hại nào.

### 2. In-Context Pathology Engine RAG (< 2ms) (Pillar 1)
- Tích hợp module truy vấn bộ nhớ đệm RAM Cache siêu tốc `src/lib/cropSearch.ts` với độ trễ phản hồi dưới **2 mili-giây**.
- Thuật toán so khớp tiếng Việt không dấu NFD và tính điểm tương đồng đa chiều (tên cây, tên khoa học, triệu chứng bệnh).
- Tích hợp trực tiếp vào Agent Loop đa bước tại `src/app/api/chat/route.ts` với Tool `search_crop_database` loại bỏ hoàn toàn hiện tượng ảo giác (hallucination).

### 3. Thẻ Bệnh Án Điện Tử & Phím Xúc Giác Thực Địa (Pillar 2)
- Tự động sinh mã bệnh án điện tử chuẩn hoá: `VL-PATH-2026-XXXX`.
- Cảnh báo rủi ro 3 cấp độ: **Hiểm nghèo (Đỏ)**, **Nguy cơ cao (Cam)**, **Trung bình (Xanh)**.
- **Nút bấm xúc giác thực địa (Tactile Buttons):** Đặt ra các bước test xúc giác thực tế tại vườn kèm 2 nút bấm nhanh **`[ ✓ Có ]`** và **`[ ✕ Không ]`** để nông dân gửi phản hồi tức thì về cho AI mà không cần gõ chữ.
- **Xuất Phiếu Khám Bệnh:** Nút một chạm sao chép toàn bộ hồ sơ bệnh án chuẩn mực vào bộ nhớ tạm.

### 4. Toàn Thư Bệnh Học Cây Trồng Trực Quan (`/crops`) (Pillar 3)
- Giao diện tra cứu hiện đại tại `/crops` với thanh tìm kiếm tức thì theo tên cây, tên khoa học hoặc triệu chứng.
- Phân loại theo 6 chuyên đề nông học trực quan.
- Modal Bệnh Học xem chi tiết tác nhân vi sinh, ranh giới chẩn đoán kép, bài test thực địa và phác đồ canh tác & sinh học.
- Lối tắt một chạm chuyển sang chat AI chuyên sâu.

### 5. Bộ Quy Tắc Lâm Sàng Khắc Khe (Strict Clinical Mandate) (Pillar 4)
- **Nguyên tắc bóc tách ca bệnh kép (Double Diagnosis):** Bắt buộc phân biệt với các bệnh tương đồng dễ gây nhầm lẫn (Greening HLB vs Vàng lá thối rễ vs Thiếu vi lượng; Xì mủ Phytophthora vs Mọt đục cành; Thán thư vs Cháy nắng sinh lý).
- **Ranh giới lâm sàng:** Tuyệt đối không khẳng định 100% nếu chỉ có mô tả ảnh 2D; bắt buộc yêu cầu kiểm tra thực địa.
- **100% Ưu tiên phác đồ sinh học:** Chế phẩm nấm đối kháng *Trichoderma*, *Bacillus subtilis*, nano đồng hữu cơ, Chitosan, dầu khoáng SK Enspray 99EC.

### 6. Kiến Trúc AI Gateway & Mô Hình Khóa An Toàn (Pillar 5)
- Mô hình suy luận lâm sàng chuyên sâu: **`ag/gemini-3.8-flash-high`** (Mô hình phụ phản hồi nhanh: `ag/gemini-3.8-flash`).
- Server-side Prompt Caching tĩnh giữ System Prompt và Tool Definitions cố định ở đầu ngữ cảnh, giảm 90% chi phí token và tăng tốc độ xử lý.
- Tích hợp 9Router Real-time Web Search Tool cập nhật công văn dịch bệnh và giá cả thị trường.

---

## 🏗️ CẤU TRÚC DỰ ÁN

```
ultra-project/
├── src/
│   ├── app/
│   │   ├── api/chat/route.ts        # Agent Loop đa bước (RAG + 9Router Web Search)
│   │   ├── api/crops/route.ts       # API tìm kiếm và phân loại 1.502 cây trồng
│   │   ├── api/storage/route.ts     # API lưu trữ và quản lý media
│   │   ├── crops/page.tsx           # Trang Toàn thư Bệnh học Cây trồng (/crops)
│   │   ├── page.tsx                 # Trang chính Bác sĩ Cây trồng AI Lâm sàng
│   │   └── layout.tsx               # Root Layout & Theme Providers
│   ├── components/
│   │   ├── chat/ChatMessage.tsx     # Thẻ bệnh án điện tử & Nút xúc giác thực địa
│   │   ├── input/                   # FloatingInputIsland (Thanh nhập nổi)
│   │   ├── sidebar/AppSidebar.tsx   # Sidebar điều hướng & Lối tắt Toàn thư (/crops)
│   │   └── modals/                  # SettingsModal, HelpModal, AuthModal
│   ├── context/ChatContext.tsx      # Quản lý State trò chuyện & Đồng bộ Supabase
│   ├── data/
│   │   └── vietnam_plant_pathology_1000_crops.json  # Siêu CSDL 1.502 cây trồng (4.6 MB)
│   ├── lib/
│   │   ├── cropSearch.ts            # In-Context Pathology Engine RAG (< 2ms)
│   │   ├── systemPrompt.ts          # Master System Prompt & Strict Clinical Mandate
│   │   └── supabase.ts              # Kết nối Supabase PostgreSQL Cloud
│   └── types/chat.ts                # TypeScript interfaces chuẩn hóa
├── tools/
│   ├── audit_check.py               # Script kiểm định tự động chất lượng CSDL
│   ├── browser_test_e2e.js          # Playwright E2E browser test toàn thư /crops
│   ├── browser_test_chat.js         # Playwright E2E browser test thẻ bệnh án & xúc giác
│   └── test_sse_chat.py             # Script kiểm thử luồng SSE & AI Gateway
└── package.json                     # Next.js 16, React 19, GSAP 3.15, Tailwind v4
```

---

## 🚀 HƯỚNG DẪN CÀI ĐẶT & CHẠY DỰ ÁN

### 1. Cài Đặt Thư Viện
```bash
cd ultra-project
npm install
```

### 2. Cấu Hình Biến Môi Trường (`.env.local`)
```env
# AI Model Gateway & 9Router Search
AI_GATEWAY_URL=http://nvnmc.asia:26627/v1/chat/completions
AI_GATEWAY_KEY=your_ai_gateway_key_here
SEARCH_API_URL=http://nvnmc.asia:26627/v1/search
DEFAULT_MODEL=ag/gemini-3.8-flash-high
FAST_MODEL=ag/gemini-3.8-flash

# Supabase Cloud Database (PostgreSQL)
NEXT_PUBLIC_SUPABASE_URL=https://dffycwpkbfnaqptuvvju.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key

# Deployment & CI/CD Keys
RENDER_API_KEY=your_render_key
RENDER_SERVICE_ID=srv-dberh3gae00c73e41ddg
GITHUB_TOKEN=your_github_token
```

### 3. Chạy Môi Trường Development & Kiểm Thử
```bash
# Khởi động máy chủ dev
npm run dev

# Kiểm tra kiểu dữ liệu TypeScript
npm run typecheck

# Kiểm tra bản dựng Production
npm run build
```

---

## 🏆 THÔNG TIN BẢN QUYỀN

Dự án được sáng lập và phát triển bởi:
* **Đề tài dự thi:** AgriVision - Phần mềm hệ thống nông nghiệp thông minh kết hợp trí tuệ nhân tạo AI.
* **Mã nguồn mở theo giấy phép MIT License.**
