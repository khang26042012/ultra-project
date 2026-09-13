# 🧪 BẢN GIAO VIỆC KIỂM THỬ TOÀN DIỆN BẰNG ĐA SUBAGENT TRÌNH DUYỆT (BROWSER TESTING & POLISH)

### Mục tiêu:
Khởi tạo đồng thời **nhiều Subagent độc lập** mở trình duyệt thực tế (headless hoặc virtual browser / Playwright / Puppeteer / MCP browser) để **KIỂM THỬ TẤT CẢ MỌI THỨ TỪ A ĐẾN Z** trên ứng dụng AgriVision (`https://ultra-project.onrender.com` hoặc `http://localhost:3000`). Bất kỳ lỗi logic nào hay chi tiết giao diện nào chưa đẹp, subagent phải **TỰ ĐỘNG SỬA CODE VÀ TỐI ƯU NGAY LẬP TỨC**!

---

## 👥 PHÂN CÔNG 4 SUBAGENT KIỂM THỬ CHUYÊN BIỆT:

### 🤖 SUBAGENT 1: KIỂM THỬ BẢO MẬT & HỆ THỐNG AUTHENTICATION (TAB THƯỜNG & ẨN DANH)
1. **Test Đăng ký mới:**
   - Mở modal đăng ký, điền họ tên, email mới, mật khẩu `123456`.
   - Kiểm tra: Tài khoản có được lưu thành công vào bảng `profiles` trên Supabase và nạp vào `currentUser` không?
2. **Test Đăng xuất & Đăng nhập lại:**
   - Bấm Đăng xuất ➔ Mở lại modal Đăng nhập, nhập đúng email và mật khẩu vừa tạo ➔ Kiểm tra đăng nhập thành công 100%.
3. **Test Đăng nhập trong Tab Ẩn danh (Incognito Mode) / Trình duyệt mới:**
   - Mở phiên trình duyệt ẩn danh hoàn toàn mới (không có `localStorage` cũ).
   - Đăng nhập bằng tài khoản vừa tạo ➔ Kiểm tra hệ thống truy vấn Supabase Cloud Database và cho phép đăng nhập mượt mà.
4. **Test Xử lý lỗi:**
   - Thử nhập sai mật khẩu ➔ Kiểm tra hiện thông báo lỗi rõ ràng: *"Mật khẩu không chính xác"*.
   - Thử đăng ký email đã tồn tại ➔ Kiểm tra thông báo cảnh báo hợp lý.
5. **👉 Nhiệm vụ Tự Sửa:** Nếu đăng nhập ở ẩn danh bị lỗi hoặc không nạp được lịch sử, sửa ngay `ChatContext.tsx`.

---

### 🤖 SUBAGENT 2: KIỂM THỬ GIAO DIỆN MOBILE & RESPONSIVE DESIGN (375px - 412px)
1. **Test Header Mobile:**
   - Đặt kích thước màn hình `390x844` (iPhone 14) và `412x915` (Android phổ thông).
   - Kiểm tra đỉnh trang: **Tuyệt đối không còn avatar tròn AV và chữ ở giữa**, không còn thanh kẻ ngang xám chia cắt. Chỉ có nút mở menu bên trái và nút chat mới bên phải.
2. **Test Ô nhập liệu (Floating Input Island):**
   - Gõ văn bản dài: Kiểm tra ô textarea tự động giãn nở chiều cao mượt mà (tối đa ~180px), không làm tràn màn hình.
   - Kiểm tra nút `+` đính kèm ảnh và nút gửi tròn đen bo viền viên thuốc (pill shape).
3. **Test Modal Cài Đặt (Settings) trên Mobile:**
   - Mở Settings trên mobile: Kiểm tra thanh Tabs đã chuyển thành **dạng Pills cuộn ngang** phía trên đỉnh, nội dung phía dưới tràn 100% bề ngang, chữ không bị ép chật chội.
4. **Test Modal Trợ giúp & Hướng dẫn (HelpModal):**
   - Mở từ Menu Profile: Kiểm tra hiển thị đầy đủ 4 cẩm nang hướng dẫn nông dân (chụp ảnh bệnh, mô tả triệu chứng, test thực địa, hotline BVTV Vĩnh Long).
5. **👉 Nhiệm vụ Tự Sửa:** Nếu phát hiện bất kỳ chỗ nào bị tràn viền (overflow-x), vỡ layout hoặc nút bấm quá nhỏ khó chạm, tối ưu ngay class Tailwind.

---

### 🤖 SUBAGENT 3: KIỂM THỬ LUỒNG CHAT, SUY LUẬN (THINKING) & WEB SEARCH
1. **Test Stream Văn bản & Thinking:**
   - Gửi câu hỏi: *"Triệu chứng bệnh thán thư trên xoài Vĩnh Long là gì?"*
   - Kiểm tra:
     - Khi đang suy nghĩ: Dòng chữ `Đang suy nghĩ...` có animation thở nhấp nháy từ đậm sang nhạt, **không có icon đám mây ☁️/💭 thô**.
     - Khi hoàn tất: Tự động thu gọn thành 1 dòng mỏng: `Đã suy luận trong Xs ▾`.
     - Click vào dòng suy luận: Xổ ra khối trích dẫn có vạch kẻ đứng mảnh `border-l-2`, font chữ thường dễ đọc.
2. **Test 9Router Web Search Agent Loop:**
   - Gửi câu hỏi thời sự: *"Tra cứu giá lúa và tình hình dịch bệnh mới nhất tại Vĩnh Long"*.
   - Kiểm tra:
     - Có hiện badge tìm kiếm thực tế: `🔍 Đang tra cứu dữ liệu: "..."...`.
     - Có hiện nút mỏng nhẹ: `Đã tìm kiếm X nguồn thông tin ▾`, click vào mở danh sách liên kết có thể nhấp chuột.
3. **Test Đính kèm ảnh & Lightbox:**
   - Đính kèm một ảnh lá bệnh (ảnh mẫu có sẵn trong dự án hoặc base64).
   - Kiểm tra ảnh trong tin nhắn hiển thị thumbnail nhỏ gọn (`max-w-[220px]`) kèm badge phóng to.
   - Click vào ảnh: Kiểm tra mở **Image Lightbox toàn màn hình nền đen**, thử các nút Zoom in, Zoom out và nút đóng `✕`.
4. **👉 Nhiệm vụ Tự Sửa:** Nếu luồng search bị đơ hoặc lightbox không zoom được, sửa ngay `ChatMessage.tsx` và `route.ts`.

---

### 🤖 SUBAGENT 4: KIỂM THỬ HIỂN THỊ MARKDOWN, LOGIC CUỘN & CÀI ĐẶT
1. **Test Định dạng Bệnh học & Markdown:**
   - Kiểm tra các tên bệnh học như `*Fusarium oxysporum*` hiển thị thành chữ in nghiêng chuẩn, **không còn dấu sao `*...` thô**.
   - Kiểm tra ký tự `---` biến thành đường kẻ mỏng phân cách `<hr />`, không in ra chữ `---`.
   - Kiểm tra các dấu gạch đầu dòng bullet point thụt lề chuẩn `pl-5` dưới các đề mục số `1. `, `2. `.
   - Kiểm tra Markdown Table có khung viền bo tròn và cho phép cuộn ngang mượt mà.
2. **Test Smart Auto-scroll & Nút Cuộn Đáy:**
   - Khi tin nhắn đang stream dài: Dùng chuột/ngón tay cuộn lên trên đọc tin cũ ➔ Kiểm tra hệ thống **KHÔNG được giật cướp quyền cuộn** của người dùng.
   - Kiểm tra nút tròn nổi `ArrowDown` xuất hiện ở góc dưới bên phải, click vào cuộn mượt xuống đáy trang.
3. **Test Tính năng trong Settings:**
   - Đổi cỡ chữ Nhỏ / Vừa / Lớn ➔ Kiểm tra cỡ chữ tin nhắn trong khung chat thay đổi tương ứng tức thì.
   - Bật/tắt công tắc Web Search ➔ Kiểm tra state lưu trữ.
   - Bấm nút "Xuất JSON" ➔ Kiểm tra tải về file dữ liệu backup `.json` hợp lệ.
4. **👉 Nhiệm vụ Tự Sửa:** Hoàn thiện dứt điểm mọi chi tiết nhỏ nhất.

---

## 🚀 KẾT THÚC & DEPLOY:
Sau khi các Subagent hoàn thành kiểm thử và tự động sửa sạch mọi lỗi:
```bash
npm run build
git add -A
git commit -m "test(audit): multi-subagent full browser audit - verified auth incognito, mobile responsive, thinking UI, lightbox, and smart scroll"
git push origin main
```
Đảm bảo bản web `https://ultra-project.onrender.com` hoạt động hoàn hảo 100%!
