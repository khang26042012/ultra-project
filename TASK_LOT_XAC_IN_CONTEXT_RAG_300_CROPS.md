# 🚀 BẢN GIAO VIỆC "LỘT XÁC" HỆ THỐNG AGRIVISION (IN-CONTEXT PATHOLOGY TOOL & 300 CÂY TRỒNG MỚI)
### Dự án: AgriVision (ultra-project)
### Tác giả: Phan Trọng Khang (Lớp 9¹, THCS Vĩnh An, Vĩnh Long)
### Mục tiêu: Tích hợp công cụ tra cứu tri thức nội tại (In-Context Pathology Tool), mở rộng thêm 300 cây trồng Việt Nam, áp dụng bộ quy tắc lâm sàng sắt đá và test toàn diện bằng đa Subagent trình duyệt.

*(Lưu ý: Không hardcode key, toàn bộ API Keys và Database đã có sẵn trong .env.local và process.env)*

---

## 🧠 NHIỆM VỤ 1: MODULE IN-CONTEXT PATHOLOGY TOOL (`search_crop_database`)
*Khi người dùng hỏi về bệnh cây hoặc gửi ảnh, AI lập tức suy nghĩ (Thinking) và tự động gọi Tool để lục tìm trong file data JSON kết hợp với nội dung trả lời:*

1. **Xây dựng module `src/lib/cropSearch.ts`:**
   - Đọc và nạp dữ liệu từ tệp tri thức cây trồng (`src/data/vinh_long_plant_pathology_100_crops.json` và `src/data/vietnam_plant_pathology_400_crops.json`).
   - Xây dựng hàm tìm kiếm: `searchCropKnowledge(cropName: string, symptoms: string[])`:
     - Chuẩn hóa tiếng Việt (hỗ trợ có dấu và không dấu).
     - So khớp tên cây (bưởi, sầu riêng, cam, lúa, cà chua, cà phê,...) và triệu chứng (vàng lá, thối rễ, xì mủ, nứt thân,...).
     - Trả về chi tiết bệnh học có độ tương đồng cao nhất: tác nhân nấm/khuẩn/virus, triệu chứng lá/thân/rễ/trái, cách phân biệt chẩn đoán kép, bài test thực địa và phác đồ sinh học VietGAP.

2. **Tích hợp Tool vào Agent Loop (`src/app/api/chat/route.ts`):**
   - Khai báo 2 Tool cho Gemini Gateway:
     - Tool 1: `search_crop_database` (tra cứu dữ liệu cây trồng nội bộ).
     - Tool 2: `web_search` (tra cứu giá cả, thuốc BVTV thị trường qua 9Router).
   - **Luồng hoạt động tự động của AI:**
     - Khi người dùng gửi câu hỏi bệnh cây hoặc ảnh lá bệnh:
     - AI suy luận trong khối thought: *"Người dùng đang hỏi về cây X với triệu chứng Y, kích hoạt tool search_crop_database để lấy hồ sơ bệnh học chuẩn xác..."*.
     - Hệ thống thực thi tool `search_crop_database`, trả dữ liệu bệnh học vào mảng tin nhắn với role `tool`.
     - Nếu cần số liệu thị trường hay dịch bệnh thời sự, AI tự động gọi tiếp tool `web_search`.
     - Phản hồi cuối cùng: 100% chuẩn y học thực vật, có trích dẫn nguồn từ Kho dữ liệu bệnh học AgriVision, loại bỏ hoàn toàn ảo giác!

---

## 🌾 NHIỆM VỤ 2: PHÂN CHIA SUBAGENTS BỔ SUNG THÊM 300 CÂY TRỒNG MỚI TẠI VIỆT NAM
*Khởi tạo nhiều subagents chạy song song tra cứu qua 9Router để bổ sung 300 cây trồng mới trên khắp các vùng sinh thái Việt Nam (ĐBSCL, Tây Nguyên, Đông Nam Bộ, Miền Trung, Bắc Bộ, Đà Lạt):*

1. **Quy mô:** Đạt tối thiểu **400+ cây trồng** trong tệp `src/data/vietnam_plant_pathology_400_crops.json` (hoặc cập nhật vào file json hiện tại).
2. **Yêu cầu bắt buộc về cấu trúc:**
   - Giữ nguyên 100% cấu trúc JSON chuẩn mực hiện có.
   - **BẮT BUỘC MỖI CÂY PHẢI ĐỦ BỆNH:** Từ 2 đến 5 bệnh đặc thù (cả bệnh cơ bản và bệnh phức tạp hiểm nghèo).
   - Mỗi bệnh phải có đầy đủ:
     - `ten_benh`, `muc_do_nguy_hiem`
     - `tac_nhan` (loại vi khuẩn/nấm/virus/tuyến trùng, tên khoa học)
     - `trieu_chung_dien_hinh` (lá, thân, cành, rễ, trái)
     - `phan_biet_chan_doan_kep` (bóc tách triệu chứng dễ nhầm lẫn)
     - `kiem_tra_thuc_dia` (thao tác sờ nắn, mùi chua, thử nghiệm ngâm nước)
     - `phac_do_vietgap` (biện pháp canh tác và chế phẩm sinh học an toàn)

---

## 🛡️ NHIỆM VỤ 3: DANH SÁCH QUY TẮC KHẮC KHE (THE STRICT CLINICAL MANDATE)
*Cập nhật vào `src/lib/systemPrompt.ts` để nâng tầm AI thành một Bác sĩ cây trồng lâm sàng có kỷ luật sắt đá:*

1. **Nguyên tắc Bóc tách ca bệnh kép (Double Diagnosis):** Mọi chẩn đoán đều bắt buộc phải so sánh với ít nhất 1 bệnh tương đồng dễ nhầm lẫn (ví dụ: Vàng lá Greening HLB vs Vàng lá thối rễ vs Thiếu vi lượng kẽm). Không bao giờ phán đoán một chiều.
2. **Nguyên tắc 3 cấp độ chắc chắn:**
   - Nếu chưa đủ 100% căn cứ: Bắt buộc dùng từ thận trọng (*"Nghi ngờ mức độ..."*), **BẮT BUỘC HỎI NGƯỢC LẠI NÔNG DÂN** 2 câu hỏi sờ nắn xúc giác thực địa (mùi chua, sờ ráp, mủ thân, kiểm tra rễ).
3. **Ưu tiên 100% Phác đồ sinh học an toàn VietGAP:** Tuyệt đối không tự ý kê thuốc hóa học cấm hoặc độc hại. Ưu tiên Trichoderma, Bacillus subtilis, nấm đối kháng, gốc đồng nano sinh học, dầu khoáng SK Enspray.
4. **Giao diện Thẻ Bệnh Án Tương Tác (`ChatMessage.tsx`):**
   - Render Thẻ Bệnh Án Lâm Sàng trực quan có huy hiệu phân cấp độ nguy hiểm (Hiểm nghèo 🔴 / Nặng 🟠 / Vừa 🟡).
   - Có các nút bấm nhanh xúc giác thực địa (ví dụ: `[Có mùi chua]`, `[Không mùi]`) để nông dân bấm 1 chạm gửi phản hồi cho AI tiếp tục chẩn đoán.

---

## 🧪 NHIỆM VỤ 4: PHÂN CHIA SUBAGENTS DÙNG TRÌNH DUYỆT KIỂM THỬ TOÀN DIỆN & TỰ HOÀN THIỆN
*Khởi tạo nhiều subagents mở trình duyệt thực tế test TẤT CẢ MỌI THỨ từ A đến Z:*
1. **Kiểm thử Tool RAG & Chat:** Thử hỏi một câu hỏi bệnh bất kỳ (ví dụ: *"Bệnh xì mủ sầu riêng"* hoặc gửi ảnh lá cà chua) ➔ Kiểm tra AI có tự động gọi tool `search_crop_database` lấy dữ liệu nội tại và hiển thị Thẻ Bệnh Án tương tác không.
2. **Kiểm thử Dataset:** Kiểm tra file JSON có đủ trên 400 cây trồng và không bị lỗi cú pháp parse.
3. **Kiểm thử Giao diện & Cuộn:** Kiểm tra trên mobile và desktop, kiểm tra nút cuộn nhanh xuống đáy và lightbox ảnh.
4. **QUY TẮC BẮT BUỘC (SELF-HEALING):** Bất kỳ điểm nào bị lỗi logic, vỡ giao diện hoặc nhìn xấu ➔ Subagent phải **TỰ ĐỘNG SỬA CODE, TỐI ƯU CSS VÀ HOÀN THIỆN NGAY LẬP TỨC!**

---

## 🚀 TIÊU CHUẨN HOÀN TẤT & PUSH CODE:
```bash
npm run build
git add -A
git commit -m "feat(agrivision): integrate in-context pathology tool, expand 300+ crops dataset, enforce strict clinical mandate, and verify via browser subagents"
git push origin main
```
