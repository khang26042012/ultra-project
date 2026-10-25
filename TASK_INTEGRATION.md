# 🌾 BẢN GIAO VIỆC TÍCH HỢP & NÂNG CẤP HỆ THỐNG: AGRIVISION (ULTRA PROJECT)

**Dành cho:** Antigravity Agent  
**Tác giả dự án:** Bạn **Phan Trọng Khang** — Học sinh lớp **9¹**, **Trường THCS Vĩnh An** (tỉnh Vĩnh Long)  
**Mục tiêu:** Tích hợp bộ não chẩn đoán bệnh học lâm sàng, khóa chuẩn mô hình `ag/gemini-3.8-flash-high`, đồng bộ nhận diện thương hiệu và cơ chế lưu trữ dữ liệu hoàn chỉnh.

---

## 📋 DANH SÁCH 5 NHIỆM VỤ TÍCH HỢP BẮT BUỘC (TASKS):

### Task 1: Tích Hợp Master System Prompt Vào Luồng API Chat
* **Vị trí thực thi:** `src/app/api/chat/route.ts` (hoặc lớp xử lý ngữ cảnh trước khi gọi Gateway).
* **Nội dung:** Nhúng toàn bộ quy tắc bệnh học lâm sàng, danh tính tác giả Phan Trọng Khang (Lớp 9¹ THCS Vĩnh An) và quy tắc 3 cấp độ chắc chắn:
  - Nếu độ tin cậy **< 100% (dù là 70-90%)**: Tuyệt đối **KHÔNG KẾT LUẬN KHẲNG ĐỊNH**, dùng từ thận trọng (*"Nghi ngờ cao..."*), **HỎI NGƯỢC LẠI NGƯỜI DÙNG** về cảm giác sờ nắn xúc giác, và khuyên liên hệ Trạm Khuyến nông / Chi cục Trồng trọt & BVTV Vĩnh Long.
  - Xưng hô lễ phép bằng tiếng Việt: Xưng *"em"*, gọi người dùng là *"bác / chú / anh chị"*.
  - Ưu tiên phác đồ sinh học an toàn VietGAP.

### Task 2: Khóa Cứng Mô Hình & Duy Trì Cửa Sổ Ngữ Cảnh (Context Window)
* **Model ID:** Luôn cố định là `ag/gemini-3.8-flash-high`.
* **Duy trì Context Window:** Khi gửi request đến `http://nvnmc.asia:26627/v1/chat/completions`, phải truyền toàn bộ mảng `messages` lịch sử các lượt hội thoại trước đó để AI có trí nhớ ngữ cảnh xuyên suốt, không hỏi lặp lại thông tin đã cung cấp.

### Task 3: Tối Ưu Nút Đính Kèm Ảnh & Giao Diện Quét
* **Nút `+` (Đính kèm tệp / ảnh):**
  - Cho phép người dùng bấm vào để chọn ảnh từ máy hoặc chụp trực tiếp từ camera.
  - Tự động nén ảnh tối ưu và chuyển thành Base64 (`data:image/jpeg;base64,...`) gửi kèm trong payload `image_url`.
  - Hiển thị thumbnail ảnh xem trước nhỏ gọn ngay phía trên ô nhập tin nhắn kèm nút `x` để hủy ảnh nếu muốn.

### Task 4: Cơ Chế Lưu Trữ Lịch Sử Chat & Cài Đặt (Local Persistence)
* Tự động lưu toàn bộ các cuộc trò chuyện, tin nhắn và hình ảnh vào `localStorage` theo từng phiên chat.
* Khi người dùng F5 hoặc mở lại trình duyệt, các đoạn hội thoại cũ trong mục `RECENTS` tại Sidebar phải được khôi phục nguyên vẹn.
* Thêm nút `Thùng rác` bên cạnh từng đoạn chat để người dùng có thể xóa khi không cần nữa.

### Task 5: Đồng Bộ Thông Tin Tác Giả & Giao Diện Sáng (Light Mode Default)
* Mặc định khi vào web luôn là **Light Mode** (nền trắng `#ffffff`, chữ đen `#0d0d0d`, icon đơn sắc monochrome thanh mảnh).
* Tại chân Sidebar (Profile Area) hoặc Modal giới thiệu:
  - Hiển thị trang trọng dòng chữ: **"AgriVision v1.0 — Tác giả: Phan Trọng Khang (Lớp 9¹, THCS Vĩnh An)"**.

---

## 🚀 QUY TRÌNH HOÀN TẤT & TRIỂN KHAI:
Sau khi hoàn thành các task trên, chạy lệnh kiểm tra, commit và push lên nhánh chính:
```bash
git add -A
git commit -m "feat(agrivision): integrate master clinical pathology system prompt, locked gemini-3.8-flash-high, image attachment, and persistent storage"
git push origin main
```
Render sẽ tự động build và deploy bản mới nhất tại: `https://ultra-project.onrender.com`.
