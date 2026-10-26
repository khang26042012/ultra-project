# ⚡ ĐẠI KẾ HOẠCH "LỘT XÁC" HỆ THỐNG AGRIVISION — BƯỚC NHẢY VỌT CÔNG NGHỆ 2026-2027
### Chủ nhiệm dự án: Nhà sáng lập trẻ **Phan Trọng Khang** (Lớp 9¹, THCS Vĩnh An, Vĩnh Long)
### Tầm nhìn: Biến AgriVision từ một "Chatbot AI thông thường" thành **HỆ THỐNG TRỢ LÝ BÁC SĨ CÂY TRỒNG LÂM SÀNG & TOÀN THƯ BỆNH HỌC THỰC VẬT ĐẦU TIÊN TẠI VIỆT NAM CÓ BẢN QUYỀN TRI THỨC NỘI TẠI (LOCAL IN-CONTEXT RAG ENGINE)**

---

## 🏛️ TỔNG QUAN CHIẾN LƯỢC: VÌ SAO ĐÂY LÀ "MÀN LỘT XÁC" ĐỈNH CAO?

Hiện nay, 99% các chatbot AI trên thị trường mắc phải 3 nhược điểm chết người trong nông nghiệp:
1. **Ảo giác kiến thức (Hallucination):** Bịa tên thuốc, liều lượng phun sai quy chuẩn BVTV Việt Nam.
2. **Thiếu tính địa phương hóa:** Trả lời chung chung kiểu sách vở, không hiểu đất đai phèn, mặn, phù sa sông Tiền, sông Hậu tại Vĩnh Long và ĐBSCL.
3. **Phụ thuộc hoàn toàn vào tìm kiếm mạng:** Khi không có mạng hoặc mạng yếu, AI trở nên mù tịt.

**👉 GIẢI PHÁP ĐỘT PHÁ CỦA ANH KHANG:**  
Tích hợp **BỘ NÃO LAI 2 TẦNG (HYBRID DUAL-ENGINE)**:
- **Tầng 1 (Local Pathology RAG Tool):** Một công cụ nội bộ truy vấn tức thì vào kho siêu dữ liệu **400+ cây trồng và hàng nghìn ca bệnh học chuẩn xác** vừa thu thập (`vietnam_plant_pathology_400_crops.json`). Dữ liệu này là "Sách giáo khoa bất khả xâm phạm".
- **Tầng 2 (Real-time Web Search Tool):** Tự động tra cứu thời sự thị trường, giá thuốc BVTV, cập nhật văn bản Cục Trồng trọt & BVTV qua 9Router.
- **Tầng 3 (Reasoning Stream & Multimodal Vision):** Bộ não `ag/gemini-3.8-flash-high` soi chiếu hình ảnh vết bệnh, đối chiếu với cơ sở dữ liệu nội tại và kết quả tra cứu để đưa ra **Phiếu Khám Bệnh Lâm Sàng** chuẩn xác 100%!

---

## 📋 DANH SÁCH 5 TRỤ CỘT TRIỂN KHAI CẢI THIỆN TOÀN DIỆN:

### 🚀 TRỤ CỘT 1: MODULE IN-CONTEXT PATHOLOGY RETRIEVAL TOOL (`search_crop_database`)
*Khi người dùng nêu vấn đề hoặc gửi ảnh cây trồng, AI lập tức kích hoạt chuỗi tư duy và gọi Tool tra cứu kho dữ liệu:*

1. **Cơ chế hoạt động:**
   - Trong `src/lib/cropSearch.ts`: Xây dựng thuật toán **Fuzzy Matching + Semantic Keyword Search** trên tệp dữ liệu 400+ cây.
   - Khi người dùng gửi câu hỏi (ví dụ: *"Cây sầu riêng bị xì mủ thân và thối rễ"*):
     - **Gemini Reasoning:** Xác định thực thể cây = `Sầu riêng`, triệu chứng = `["xì mủ", "thối rễ"]`.
     - **Tool Call:** `search_crop_database({ crop_name: "sầu riêng", symptoms: ["xì mủ", "thối rễ"] })`.
     - **Kết quả trả về:** Bản ghi bệnh học lâm sàng chính xác: Tác nhân nấm *Phytophthora palmivora*, cơ chế bóc tách chẩn đoán kép với xì mủ do mọt đục cành, bài test thực địa cạo vỏ thân và phác đồ sinh học VietGAP quét gốc Phosphonate.
   - **Tích hợp:** Nếu cần giá cả thuốc hoặc đại lý tại Vĩnh Long, Agent tự động gọi tiếp Tool 2: `web_search`.

---

### 🩺 TRỤ CỘT 2: PHIẾU KHÁM BỆNH ĐIỆN TỬ TƯƠNG TÁC (INTERACTIVE CLINICAL PATHOLOGY CARD)
*Thay vì chỉ in ra các dòng chữ dài lê thê khiến bà con khó đọc, câu trả lời của AI sẽ đính kèm một **Thẻ Bệnh Án Lâm Sàng Trực Quan (Interactive UI Card)**:*

1. **Các thành phần trên Thẻ Bệnh Án:**
   - **Mã hồ sơ bệnh học:** `VL-PATH-2026-XXXX`.
   - **Tên cây & Bệnh nghi ngờ:** Có nhãn cấp độ nguy hiểm (Hiểm nghèo 🔴 / Nặng 🟠 / Trung bình 🟡).
   - **Tác nhân sinh học:** Vi khuẩn / Nấm / Tuyến trùng / Virus (hiển thị tên khoa học in nghiêng chuẩn quốc tế).
   - **Nút tương tác Xúc giác thực địa (Interactive Sensory Checks):**
     - Cho phép bà con bấm chọn: *"Vết bệnh có mùi chua? [ Có / Không ]"*, *"Có khói trắng khi nhúng nước? [ Có / Không ]"*.
     - Khi bà con bấm, app tự động gửi câu trả lời về cho AI để AI **chốt hạ độ tin cậy lên 100%**!
   - **Nút "Xuất Phiếu Khám Bệnh (PDF/Ảnh)":** Xuất một phiếu xét nghiệm chuyên nghiệp để bà con đem ra Trạm Khuyến nông / Đại lý thuốc BVTV mua đúng hoạt chất sinh học, không bị người bán dụ mua sai thuốc.

---

### 📚 TRỤ CỘT 3: TRANG TOÀN THƯ BỆNH HỌC NÔNG NGHIỆP TƯƠNG TÁC (`/crops`)
*Mở rộng ứng dụng thành một Siêu Bách Khoa Toàn Thư Cây Trồng & Dịch Bệnh Nông Nghiệp Việt Nam:*

1. **Giao diện Toàn Thư (`src/app/crops/page.tsx`):**
   - Thanh tìm kiếm thông minh: Gõ tên cây hoặc tên bệnh bất kỳ.
   - Bộ lọc chuyên mục (Tabs):
     - 🍊 Cây ăn trái đặc sản (Bưởi Năm Roi, Sầu riêng Ri6, Cam sành, Xoài cát,...)
     - 🌾 Cây lương thực & hoa màu (Lúa, Bắp, Khoai lang tím Bình Tân,...)
     - 🥬 Rau củ quả & Ôn đới Đà Lạt
     - ☕ Cây công nghiệp & Dược liệu quý (Cà phê, Tiêu, Sâm Ngọc Linh,...)
   - Mỗi cây có một trang hồ sơ chi tiết (Profile), hiển thị đặc tính sinh thái đất đai Vĩnh Long và toàn bộ danh mục bệnh học có thể phòng trị.

---

### 🛡️ TRỤ CỘT 4: BỘ QUY TẮC KHẮC KHE BẢO VỆ NÔNG DÂN (THE STRICT CLINICAL MANDATE)
*Được nâng cấp trực tiếp vào Master System Prompt để biến AI thành một "Bác sĩ cây trồng có đạo đức và chuyên môn sắt đá":*

1. **Điều 1: Tuyệt đối không bán mình cho thuốc hóa học cấm:**  
   Bắt buộc ưu tiên 100% chế phẩm sinh học, vi sinh đối kháng (*Trichoderma*, *Bacillus subtilis*, nấm xanh, nấm trắng, nano đồng sinh học) theo danh mục lưu hành tại Việt Nam.
2. **Điều 2: Nguyên tắc Bóc Tách Ca Bệnh Kép (Double-Diagnosis Disambiguation):**  
   Mọi chẩn đoán đều phải có bảng/mục so sánh với ít nhất 1 bệnh có triệu chứng tương đồng (như Vàng lá gân xanh HLB vs Vàng lá thối rễ vs Thiếu kẽm). Không bao giờ phán đoán một chiều.
3. **Điều 3: Ranh giới lâm sàng & Bắt buộc test thực địa:**  
   Nếu chỉ nhìn qua ảnh và chưa có kiểm tra thực địa, AI bị cấm tuyên bố chắc chắn 100%. Phải hướng dẫn bà con 2 bước sờ nắn, quan sát mủ thân, kiểm tra rễ tơ.

---

### 📊 TRỤ CỘT 5: BẢNG ĐIỀU KHIỂN & ĐO LƯỜNG BENCHMARK NĂNG LỰC CHẨN ĐOÁN
*Chứng minh tính khoa học tuyệt đối trước Ban Giám Khảo Cuộc thi KHKT tỉnh Vĩnh Long:*

1. **Hệ thống tự động chấm điểm lâm sàng (Autonomous Clinical Scorer):**
   - Chạy 150 mẫu bệnh thực tế Vĩnh Long qua mô hình để đo lường:
     - Độ chính xác tác nhân vi sinh (Pathogen Precision): > 92%.
     - Thời gian phản hồi trung bình (Latency): < 2.5s nhờ kết hợp Local Data Tool.
     - Tỷ lệ giảm chi phí gọi API nhờ Prompt Caching: Tiết kiệm 88%.
   - Biểu đồ trực quan hóa dữ liệu hiển thị ngay trong mục Giới thiệu dự án.
---

### 🧬 TRỤ CỘT 6: HỢP NHẤT DỮ LIỆU & QUY MÔ HÓA 1.000 CÂY TRỒNG BẰNG 5 SUBAGENTS ĐỘC LẬP (3 WORKER SEARCH, 2 WORKER KIỂM ĐỊNH)
*Nâng cấp AgriVision thành KHO TRI THỨC BỆNH HỌC THỰC VẬT ĐỒ SỘ NHẤT VIỆT NAM với ít nhất 1.000 loài cây trồng và toàn bộ phổ bệnh học:*

1. **Gộp & Khử trùng lặp tệp dữ liệu (Deduplication & Consolidation):**
   - Viết script tự động nạp toàn bộ các tệp JSON cây trồng hiện có (`vinh_long_plant_pathology_100_crops.json` và các bản mở rộng).
   - Lọc bỏ triệt để các cây bị trùng tên tiếng Việt (`name_vi`) hoặc trùng tên khoa học (`scientific_name`).
   - Hợp nhất thành tệp siêu dữ liệu duy nhất: `src/data/vietnam_plant_pathology_1000_crops.json` (và export alias sang các file dữ liệu cũ để tránh gãy import).

2. **Khởi tạo 5 Subagents hoạt động song song độc lập:**
   - **3 Subagents Thu Thập & Tra Cứu Liên Tục (Workers 1, 2, 3):**
     - Chạy đa luồng liên tục sử dụng công cụ tìm kiếm 9Router để tìm kiếm và bổ sung thêm các giống cây trồng mới cho đến khi **đạt tối thiểu 1.000 loài cây trồng**.
     - Phạm vi bao phủ:
       - Cây trồng bản địa 63 tỉnh thành Việt Nam (đồng bằng, miền núi, duyên hải, hải đảo).
       - Cây trồng kinh tế du nhập từ thị trường quốc tế nhưng hiện tại đã và đang được trồng thực tế tại Việt Nam (ví dụ: Việt quất nhiệt đới, Dâu tây New Zealand/Hàn Quốc, Nho mẫu đơn, Măng tây xanh, Sâm Maca, Vanilla, Saffron nghệ tây, Nho thân gỗ Nam Mỹ, Táo đỏ hữu cơ, Wasabi Đà Lạt, Trà hoa vàng, Chà là Trung Đông, Cherry nhiệt đới, Hạt dẻ cười,...).
     - **BẮT BUỘC ĐỦ BỆNH:** Mỗi cây phải có từ 2 đến 5 bệnh đặc thù (cả bệnh phổ biến lẫn bệnh phức tạp/nguy hiểm), gồm tác nhân vi sinh, triệu chứng lá/thân/rễ/trái, cách bóc tách chẩn đoán kép và phác đồ VietGAP sinh học.
   - **2 Subagents Kiểm Định & Rà Soát Chất Lượng (Auditors 4, 5):**
     - Quét toàn bộ 1.000 cây trong tệp JSON:
       - Kiểm tra cấu trúc Schema: Không được thiếu bất kỳ trường nào (`topic`, `name_vi`, `scientific_name`, `danh_sach_benh`,...).
       - Kiểm định tính chính xác của tên khoa học (viết nghiêng, đúng chi/loài) và tác nhân vi khuẩn, nấm, tuyến trùng, virus.
       - Rà soát chính tả, thuật ngữ nông học chuẩn và loại bỏ hoàn toàn các mô tả mơ hồ, chung chung.
       - Đảm bảo tệp JSON chuẩn cú pháp 100%, không bị lỗi parse (`JSON.parse()` thành công tuyệt đối).
