# 🌾 BẢN GIAO VIỆC MỞ RỘNG KHO TRI THỨC BỆNH HỌC: BỔ SUNG 300 CÂY TRỒNG VIỆT NAM (TỔNG HỢP 400+ CÂY)
### Dự án: AgriVision (ultra-project)
### Tác giả: Phan Trọng Khang (Lớp 9¹, THCS Vĩnh An, Vĩnh Long)
### Mục tiêu: Khởi tạo mạng lưới Subagent chạy song song, tra cứu web 9Router liên tục để bổ sung thêm 300 loại cây trồng tại các vùng sinh thái nông nghiệp Việt Nam (ĐBSCL, Tây Nguyên, Đông Nam Bộ, Miền Trung, Bắc Bộ, Ôn đới Đà Lạt). Mỗi cây bắt buộc phải có đầy đủ toàn bộ phổ bệnh học (cơ bản & phức tạp).

---

## 🎯 1. QUY MÔ & TỆP LƯU TRỮ

- **Tệp xuất dữ liệu:** `src/data/vietnam_plant_pathology_400_crops.json` (hoặc cập nhật trực tiếp vào `src/data/vinh_long_plant_pathology_100_crops.json` với tổng số cây đạt từ **400 cây trở lên**).
- **Quy mô:** 105 cây hiện có + **300 cây trồng mới = Ít nhất 405 loài cây trồng**.
- **Phân bổ 300 cây mới theo các nhóm đề tài (Topics):**
  1. `Cay_An_Trai_Nhiet_Doi_Va_On_Doi` (~80 cây): Vải thiều Lục Ngạn, Nhãn lồng Hưng Yên, Mận Tam Hoa Bắc Hà, Đào Sa Pa, Lê Tai Nung, Hồng giòn Đà Lạt, Dâu tây Đà Lạt, Na dai Chi Lăng, Bơ Booth / Bơ 034 Tây Nguyên, Chanh dây (Lạc tiên), Sầu riêng Musang King, Sầu riêng Black Thorn, Vú sữa Hoàng Kim, Nho Ninh Thuận, Táo gió Ninh Thuận, Dưa lưới nhà màng, Việt quất, Kiwi nhiệt đới, Bưởi Luận Văn, Cam Cao Phong, Cam bù Hương Sơn, Quýt Bắc Kạn, Mắc cọp, Phật thủ, Sa-kê, Trâm đỏ, Thốt nốt, Dâu tằm,...
  2. `Cay_Cong_Nghiep_Xuat_Khau` (~60 cây): Cà phê Robusta Tây Nguyên, Cà phê Arabica Cầu Đất, Hồ tiêu Phú Quốc / Chư Sê, Cao su Đông Nam Bộ, Điều Bình Phước, Chè Shan tuyết Suối Giàng, Chè xanh Thái Nguyên, Ca cao Chợ Gạo, Mía đường Lam Sơn, Cọ dầu, Bông vải, Dừa sáp Cầu Kè,...
  3. `Cay_Luong_Thuc_Va_Hoa_Mau` (~50 cây): Lúa nếp cái hoa vàng, Lúa rẫy Tây Nguyên, Lúa đen Brieng, Ngô ngọt, Ngô nếp tím, Khoai tây Đà Lạt, Khoai mỡ, Khoai sọ Thuận Châu, Khoai môn Lệ Phố, Củ đậu (Sắn dây), Dong riềng, Đậu xanh, Đậu đen, Đậu đỏ, Đậu nành (Đậu tương), Đậu phộng sẻ, Mè đen,...
  4. `Rau_Cu_Gia_Vi_Va_Nam` (~60 cây): Súp lơ xanh/trắng, Bắp cải tím, Cà rốt Đà Lạt, Ớt chuông Đà Lạt, Ớt hiểm, Tỏi Lý Sơn, Hành tím Vĩnh Châu, Củ kiệu, Măng tây xanh, Atisô Đà Lạt, Bạc hà (Dọc mùng), Ngò rí, Thì là, Rau húng lủi, Tía tô, Kinh giới, Diếp cá, Cần tây, Rau má bến tre, Nấm đùi gà, Nấm linh chi, Nấm bào ngư, Nấm kim châm nhiệt đới, Nấm mộc nhĩ,...
  5. `Cay_Lam_Nghiep_Duoc_Lieu_Quy` (~50 cây): Sâm Ngọc Linh, Sâm Bố Chính, Quế Trà Bồng, Hồi Lạng Sơn, Sa nhân tím, Ba kích tím, Đương quy, Hà thủ ô đỏ, Xuyên tâm liên, Trinh nữ hoàng cung, Cà gai leo, Đinh lăng lá nếp, Tràm trà, Bạch đàn cao sản, Keo lai, Giổi xanh, Hạt dẻ Trùng Khánh, Mắc ca (Macadamia), Trầm hương (Dó bầu),...

---

## 🔬 2. CẤU TRÚC JSON CHUẨN MỰC (GIỮ NGUYÊN 100% CẤU TRÚC HIỆN TẠI)

Mỗi cây trồng mới phải kế thừa và tuân thủ tuyệt đối cấu trúc sau:

```json
{
  "id": "crop_106",
  "topic": "Cay_Cong_Nghiep_Xuat_Khau",
  "name_vi": "Cà phê Robusta (Cà phê Vối)",
  "scientific_name": "Coffea canephora",
  "dia_ban_pho_bien": ["Đắk Lắk", "Lâm Đồng", "Gia Lai", "Đắk Nông"],
  "dac_tinh_sinh_thai": "Ưa khí hậu nhiệt đới nóng ẩm, đất đỏ bazan tầng canh tác dày > 70cm, thoát nước tốt, nhu cầu phân bón và nước tưới trong mùa khô rất cao.",
  "danh_sach_benh": [
    {
      "ten_benh": "Bệnh Gỉ sắt cà phê (Coffee Leaf Rust)",
      "muc_do_nguy_hiem": "Rất nghiêm trọng (Gây rụng lá hàng loạt, khô cành)",
      "tac_nhan": {
        "loai": "Nấm",
        "ten_khoa_hoc": "Hemileia vastatrix"
      },
      "trieu_chung_dien_hinh": [
        "Mặt dưới lá xuất hiện các đốm tròn màu vàng nhạt ban đầu",
        "Sau đó hình thành lớp bột phấn màu vàng cam phủ đầy mặt dưới lá",
        "Mặt trên lá tương ứng với vết bệnh bị mất diệp lục, chuyển sang màu vàng loang lổ",
        "Lá bệnh nặng bị cháy khô từng mảng lớn và rụng trơ cành"
      ],
      "phan_biet_chan_doan_kep": "Khác với bệnh Đốm mắt cua (Cercospora coffeicola): Gỉ sắt có lớp bột phấn vàng phấn cam ở mặt dưới lá có thể quẹt dính tay; Đốm mắt cua có tâm màu xám trắng viền nâu đậm và không có bột phấn rơi",
      "kiem_tra_thuc_dia": "Dùng ngón tay miết nhẹ mặt dưới lá bệnh, nếu có bột phấn màu vàng cam bám dính vào ngón tay thì khẳng định 100% nấm gỉ sắt",
      "phac_do_vietgap": {
        "canh_tac": "Cắt tỉa cành thông thoáng đầu mùa mưa, dọn sạch tàn dư lá bệnh rụng gom đốt",
        "sinh_hoc": "Phun phòng bằng hoạt chất sinh học gốc đồng, nấm đối kháng Bacillus subtilis hoặc chế phẩm Trichoderma viride",
        "khuyen_cao_chuyen_gia": "Tham khảo hướng dẫn bảo vệ thực vật của Viện KHKT Nông Lâm nghiệp Tây Nguyên (WASI)"
      }
    },
    {
      "ten_benh": "Bệnh Thối rễ tơ do Tuyến trùng & Nấm phức hợp",
      "muc_do_nguy_hiem": "Đặc biệt nguy hiểm (Chết cây hàng loạt)",
      "tac_nhan": {
        "loai": "Tuyến trùng & Nấm phức hợp",
        "ten_khoa_hoc": "Pratylenchus coffeae kết hợp Fusarium oxysporum / Rhizoctonia solani"
      },
      "trieu_chung_dien_hinh": [
        "Cây sinh trưởng còi cọc, vàng lá từ đọt non xuống dần cành dưới",
        "Rễ tơ bị thối đen từng đoạn, sưng u sần sùi hoặc bị đứt cụt rễ cọc",
        "Cây lay nhẹ thấy lỏng gốc, vào mùa nắng cây héo rũ rất nhanh dù đất ẩm"
      ],
      "phan_biet_chan_doan_kep": "Khác với bệnh Khô cành khô quả (Colletotrichum): Khô cành chỉ chết từ chóp cành vào, bộ rễ vẫn khỏe; Bệnh thối rễ tuyến trùng phá hủy hoàn toàn hệ rễ dưới đất trước",
      "kiem_tra_thuc_dia": "Đào nhẹ lớp đất mặt sâu 15-20cm, dùng kéo bấm rễ tơ kiểm tra mức độ thối đen và các nốt sưng u nang tuyến trùng",
      "phac_do_vietgap": {
        "canh_tac": "Bón phân hữu cơ ủ hoai mục kết hợp vôi bột nâng pH đất trên 5.5, tuyệt đối không xới xáo làm đứt rễ trong mùa mưa",
        "sinh_hoc": "Tưới chế phẩm vi sinh đối kháng tuyến trùng Paecilomyces lilacinus kết hợp nấm Trichoderma định kỳ 3 lần/năm"
      }
    }
  ]
}
```

---

## 🤖 3. QUY TRÌNH PHÂN CHIA NHIỀU SUBAGENTS TỰ ĐỘNG THU THẬP

1. **Khởi tạo nhiều Subagent chạy song song:**
   - Viết kịch bản tự động (Node.js script với Worker Threads hoặc Batching async promises).
   - Chia danh sách 300 cây thành 6-8 nhóm Subagents chạy đồng thời:
     - *Subagent A:* Cây ăn trái miền Bắc & miền Trung (Vải, Nhãn, Đào, Mận, Lê, Na, Hồng,...).
     - *Subagent B:* Cây ăn trái Tây Nguyên & Đông Nam Bộ (Bơ, Sầu riêng, Chanh dây, Mắc ca,...).
     - *Subagent C:* Cây công nghiệp dài ngày (Cà phê, Tiêu, Cao su, Điều, Chè, Ca cao,...).
     - *Subagent D:* Cây rau ăn củ, quả, lá & gia vị (Đà Lạt, Hải Dương, Lý Sơn,...).
     - *Subagent E:* Cây lương thực màu & đậu hạt.
     - *Subagent F:* Cây lâm nghiệp, dược liệu quý (Sâm Ngọc Linh, Quế, Hồi, Ba kích,...).
2. **Khai thác công cụ Web Search từ 9Router:**
   - **Endpoint:** `POST http://nvnmc.asia:26627/v1/search`
   - **Headers:** `Authorization: Bearer sk-c276eac9b4322b74-tyrxri-1fc67c68`
   - Tự động query tìm kiếm: *"các bệnh thường gặp trên cây [Tên cây] triệu chứng tác nhân phòng trừ VietGAP"*.
3. **BẮT BUỘC PHẢI ĐỦ BỆNH CHO MỖI CÂY:**
   - Mỗi cây phải chứa từ **2 đến 5 bệnh đặc thù nhất** (gồm cả bệnh nấm lá/thân, bệnh thối rễ, bệnh do vi khuẩn, tuyến trùng hoặc virus).
   - Tuyệt đối không để cây có danh sách bệnh rỗng hoặc sơ sài.
4. **Hợp nhất và Kiểm chuẩn tệp JSON:**
   - Gộp 105 cây ban đầu với 300 cây mới vào: `src/data/vietnam_plant_pathology_400_crops.json`.
   - Đảm bảo định dạng UTF-8 không lỗi font tiếng Việt và parse JSON hợp lệ 100%.

---

## 🚀 4. KIỂM THỬ VÀ DEPLOY
```bash
# 1. Kiểm tra tổng số cây trong file JSON
node -e "const d = require('./src/data/vietnam_plant_pathology_400_crops.json'); console.log('Tổng số cây đã hoàn thiện:', d.length); if (d.length < 400) throw new Error('Chưa đủ 400 cây!');"

# 2. Build dự án Next.js
npm run build

# 3. Commit và push lên nhánh main
git add src/data/vietnam_plant_pathology_400_crops.json
git commit -m "feat(dataset): expand comprehensive plant pathology dataset to 400+ Vietnam crops via multi-agent search"
git push origin main
```
Render sẽ tự động đồng bộ kho dữ liệu bệnh học khổng lồ này lên: **https://ultra-project.onrender.com**.
