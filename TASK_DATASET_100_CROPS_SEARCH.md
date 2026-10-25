# 🌾 BẢN GIAO VIỆC THU THẬP & TỔNG HỢP DỮ LIỆU BỆNH HỌC 100+ CÂY TRỒNG VĨNH LONG
### Dự án: AgriVision (ultra-project)
### Tác giả: Phan Trọng Khang (Lớp 9¹, THCS Vĩnh An, Vĩnh Long)
### Mục tiêu: Khởi tạo mạng lưới Subagent tự động tra cứu web đa luồng (Search & Scrape), xây dựng siêu dữ liệu chuẩn JSON cho ít nhất 100 loài cây trồng và toàn bộ phổ bệnh học lâm sàng tại tỉnh Vĩnh Long và Đồng bằng sông Cửu Long.

---

## 🎯 1. YÊU CẦU QUY MÔ & CẤU TRÚC KHO DỮ LIỆU

- **Vị trí lưu trữ tệp kết quả:** `src/data/vinh_long_plant_pathology_100_crops.json` (hoặc `data/vinh_long_crops_knowledge_base.json`).
- **Quy mô bắt buộc:** **Ít nhất 100 loại cây trồng** trồng thực tế tại tỉnh Vĩnh Long và ĐBSCL.
- **Phân loại Topic (Chuyên mục cây trồng):**
  1. `Cay_An_Trai_Dac_San`: Bưởi Năm Roi, Bưởi Da Xanh, Cam sành, Cam xoàn, Quýt đường, Chanh không hạt, Sầu riêng Ri6, Sầu riêng Monthong, Xoài cát Núm, Xoài cát Hòa Lộc, Nhãn xuồng cơm vàng, Nhãn Ido, Chôm chôm Java, Chôm chôm nhãn, Măng cụt, Mít Thái Changai, Mít ruột đỏ, Ổi nữ hoàng, Mận An Phước, Vú sữa Lò Rèn, Thanh long ruột đỏ, Đu đủ ruột vàng, Dừa xiêm xanh, Dừa mã lai, Chuối già Nam Mỹ, Chuối xiêm, Sapôchê (Hồng xiêm), Bơ sáp, Mãng cầu xiêm (Na gai), Mãng cầu ta (Na), Cóc Thái, Khế ngọt, Dâu hạ châu, Me ngọt,...
  2. `Cay_Luong_Thuc_Mau`: Lúa hè thu/đông xuân (OM5451, Dai Thom 8, ST25, Jasmine 85), Bắp lai, Khoai lang tím Nhật (đặc sản Bình Tân - Vĩnh Long), Khoai mì (Sắn), Mía đường,...
  3. `Rau_An_La_An_Qua`: Cà chua, Ớt chỉ thiên, Cà tím, Dưa hấu, Dưa leo, Khổ qua (Mướp đắng), Bầu, Bí đao, Mướp hương, Đậu bắp, Đậu cô ve, Rau muống nước, Cải xanh, Cải ngọt, Cải thìa, Xà lách, Bắp cải, Hành lá, Hẹ, Gừng, Nghệ, Sả, Ngò gai, Húng quế, Rau ngót,...
  4. `Cay_Cong_Nghiep_Duoc_Lieu`: Sen lấy hạt/ngó, Nấm rơm, Đậu phộng (Lạc), Mè (Vừng), Trà hoa vàng, Cà gai leo, Đinh lăng, Nha đam (Lô hội),...

---

## 🔬 2. CẤU TRÚC SCHEMA CHI TIẾT CỦA MỖI CÂY TRỒNG TRONG TỆP JSON

Mỗi đối tượng cây trồng trong mảng JSON phải tuân thủ nghiêm ngặt cấu trúc bệnh học chuyên sâu sau:

```json
{
  "id": "crop_001",
  "topic": "Cay_An_Trai_Dac_San",
  "name_vi": "Bưởi Năm Roi / Bưởi Da Xanh",
  "scientific_name": "Citrus maxima / Citrus grandis",
  "dia_ban_pho_bien": ["Bình Minh", "Tam Bình", "Trà Ôn", "Vũng Liêm"],
  "dac_tinh_sinh_thai": "Ưa đất thịt pha phù sa màu mỡ ven sông Tiền, sông Hậu, mẫn cảm cao với ngập úng và độ mặn > 1‰",
  "danh_sach_benh": [
    {
      "ten_benh": "Bệnh Vàng lá gân xanh (Huanglongbing - HLB / Greening)",
      "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
      "tac_nhan": {
        "loai": "Vi khuẩn",
        "ten_khoa_hoc": "Candidatus Liberibacter asiaticus",
        "vector_truyen_benh": "Rầy chổng cánh (Diaphorina citri)"
      },
      "trieu_chung_dien_hinh": [
        "Phiến lá vàng lốm đốm loang lổ không đối xứng (mottling)",
        "Gân chính và gân phụ vẫn giữ màu xanh đậm hoặc bị sưng gồ, hóa bần",
        "Lá nhỏ lại, dựng đứng như tai thỏ, chồi non ngắn ngủn",
        "Trái nhỏ, méo mó, tâm lệch về một bên, hạt lép đen, nước chua chát"
      ],
      "phan_biet_chan_doan_kep": "Khác với thiếu Kẽm (thiếu kẽm đối xứng hai bên gân lá) và Vàng lá thối rễ (vàng cả gân lẫn phiến lá, rễ tơ bị thối tuột vỏ)",
      "kiem_tra_thuc_dia": "Kiểm tra sự hiện diện của rầy chổng cánh ở chồi non; quan sát tính bất đối xứng của vết vàng",
      "phac_do_vietgap": {
        "canh_tac": "Chặt bỏ tiêu hủy triệt để cây bệnh, trồng cây sạch bệnh vi ghép đỉnh sinh trưởng, bón vôi nâng pH đất 5.5 - 6.5",
        "sinh_hoc": "Nuôi thả kiến vàng (Oecophylla smaragdina) khống chế rầy chổng cánh, phun nấm ký sinh Beauveria bassiana hoặc dầu khoáng SK Enspray 99 EC",
        "khuyen_cao_vinh_long": "Liên hệ ngay Chi cục Trồng trọt & BVTV Vĩnh Long để lấy mẫu xét nghiệm PCR khi phát hiện triệu chứng nghi ngờ diện rộng"
      }
    },
    {
      "ten_benh": "Bệnh Ghẻ loét vi khuẩn (Citrus Canker)",
      "muc_do_nguy_hiem": "Nặng (Gây rụng lá và xấu mã trái)",
      "tac_nhan": {
        "loai": "Vi khuẩn",
        "ten_khoa_hoc": "Xanthomonas citri subsp. citri"
      },
      "trieu_chung_dien_hinh": [
        "Vết bệnh ban đầu là đốm nhỏ trong suốt sũng nước dưới mặt lá",
        "Vết loét phát triển gồ lên bề mặt, màu nâu sẫm, ở giữa nứt rách như miệng núi lửa",
        "Xung quanh vết loét luôn có quầng vàng sáng (halo) rất rõ ràng",
        "Xuất hiện cả trên lá, cành non và vỏ trái"
      ],
      "phan_biet_chan_doan_kep": "Khác với bệnh Ghẻ nhám sẹo (Scab do nấm Elsinoë fawcettii): Ghẻ loét vi khuẩn có quầng vàng xung quanh và nứt miệng núi lửa, còn Ghẻ nhám chóp nhọn nhô lên như hạt mụn cơm và không có quầng vàng",
      "phac_do_vietgap": {
        "sinh_hoc": "Phun luân phiên thuốc gốc đồng sinh học (Đồng Oxyclorua, Bordeaux, Kasugamycin, nấm đối kháng Bacillus subtilis)",
        "canh_tac": "Cắt tỉa thông thoáng sau thu hoạch, phòng trừ sâu vẽ bùa (vì vết cắn sâu vẽ bùa là cửa ngõ cho vi khuẩn xâm nhập)"
      }
    }
  ]
}
```

---

## 🤖 3. HƯỚNG DẪN KHỞI TẠO SUBAGENTS TRA CỨU ĐA LUỒNG LIÊN TỤC

Để thu thập đầy đủ hơn 100 loài cây với hàng trăm ca bệnh phức tạp mà không bị timeout:
1. **Chia nhóm song song:** Viết script tự động (Node.js / Python) chia 100 cây thành 5-10 nhóm (Batches), khởi chạy nhiều tiến trình worker / subagent cùng lúc.
2. **Khai thác công cụ Web Search từ 9Router:**
   - Endpoint: `POST http://nvnmc.asia:26627/v1/search`
   - Headers: `Authorization: Bearer sk-c276eac9b4322b74-tyrxri-1fc67c68`
   - Truy vấn tìm kiếm từ các nguồn uy tín:
     - Viện Cây ăn quả Miền Nam (SOFRI)
     - Trung tâm Khuyến nông Quốc gia / Sở NN&PTNT Vĩnh Long
     - Trường Đại học Cần Thơ (Khoa Nông nghiệp & Sinh học ứng dụng)
3. **Tổng hợp và kiểm chuẩn JSON:** Hợp nhất kết quả từ các worker vào một tệp JSON hoàn chỉnh, chạy lệnh validate đảm bảo chuẩn cú pháp JSON 100% không bị lỗi parse.

---

## 🚀 4. QUY TRÌNH HOÀN TẤT & PUSH CODE
```bash
# 1. Kiểm tra tính hợp lệ của file JSON
node -e "const d = require('./src/data/vinh_long_plant_pathology_100_crops.json'); console.log('Tổng số cây đã thu thập:', d.length);"

# 2. Build dự án Next.js
npm run build

# 3. Commit và push lên main
git add src/data/vinh_long_plant_pathology_100_crops.json
git commit -m "feat(dataset): construct clinical plant pathology knowledge base for 100+ Vinh Long crops via multi-agent search"
git push origin main
```
