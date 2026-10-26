# 🚀 BẢN GIAO VIỆC TỔNG THỂ: CÀO TOÀN BỘ PHỔ BỆNH HỌC, ĐẠI TU KHO DỮ LIỆU CÂY TRỒNG, ĐỔI AVATAR & TÍCH HỢP TAVILY SEARCH MAX POWER
### Dự án: AgriVision (ultra-project)
### Tác giả: Phan Trọng Khang (Lớp 9¹, THCS Vĩnh An, Vĩnh Long)

---

## 🌾 NHIỆM VỤ 1: CÀO TOÀN BỘ PHỔ BỆNH HỌC TỪ CÁC KHO BÁU MÃ NGUỒN MỞ & HỢP NHẤT DỮ LIỆU
Viết script tự động (`tools/harvest_all_crop_pathologies.py` hoặc `.js`) cào dữ liệu từ các kho báu nguồn mở lớn:
1. **Danh sách nguồn khai thác:**
   - **Growstuff Open Data API:** `https://www.growstuff.org/api/v1/crops.json?page=1...30`
   - **OpenFarm Database:** `https://github.com/openfarmcc/OpenFarm`
   - **Planteome Plant Disease Ontology:** `https://github.com/Planteome/plant-disease-ontology`
   - **PlantVillage Dataset & Digital Agriculture:** `https://github.com/spMohanty/PlantVillage-Dataset` & `ricber/digital-agriculture-datasets`
   - **Nông nghiệp Việt Nam:** Viện Cây ăn quả Miền Nam (SOFRI), Cục Bảo vệ Thực vật Việt Nam.
2. **YÊU CẦU BẮT BUỘC VỀ BỆNH HỌC (QUAN TRỌNG NHẤT):**
   - **Không chỉ giới hạn 100 cây:** Cào TOÀN BỘ các loài cây trồng có trong các nguồn dữ liệu trên.
   - **BẮT BUỘC CÀO HẾT TẤT CẢ CÁC BỆNH CỦA MỖI CÂY:** Trong tài liệu nguồn, mỗi cây có bao nhiêu bệnh, bao nhiêu tác nhân vi sinh (Nấm, Vi khuẩn, Tuyến trùng, Virus, Rầy môi giới) thì **PHẢI CÀO HẾT VỀ 100%**, tuyệt đối không được cắt bớt hay để rập khuôn 2 bệnh!
   - **Thuật toán khử trùng cây & gộp bệnh thông minh:**
     - So khớp cây theo `scientific_name` và `name_vi`.
     - Nếu cây đã có trong cơ sở dữ liệu: **HỢP NHẤT (MERGE)** toàn bộ các bệnh mới từ nguồn khác vào mảng `danh_sach_benh` của cây đó, loại bỏ các bệnh trùng lặp trong cùng 1 cây.
     - Đảm bảo mỗi bệnh đều có đủ: `ten_benh`, `muc_do_nguy_hiem`, `tac_nhan` (loại tác nhân + tên khoa học), `trieu_chung_dien_hinh` (lá/thân/rễ/trái), `phan_biet_chan_doan_kep`, `kiem_tra_thuc_dia` và `phac_do_vietgap` sinh học.
3. Xuất tệp dữ liệu hoàn chỉnh vào: `src/data/vietnam_plant_pathology_1000_crops.json`.

---

## 🎨 NHIỆM VỤ 2: ĐẠI TU GIAO DIỆN TRANG KHO DỮ LIỆU CÂY TRỒNG (`src/app/crops/page.tsx`)
1. **Đổi tiêu đề trang:**
   - Đổi dòng chữ lớn `<h1>` thành: 👉 **`Kho dữ liệu cây trồng`** (Font chữ đậm, hiện đại, thanh lịch).
2. **Xóa bỏ triệt để toàn bộ các khối rác (theo đúng ảnh mẫu khoanh vùng):**
   - **XÓA BỎ hoàn toàn thanh header cố định trên đỉnh** (gồm các pill "Trò chuyện", "Toàn Thư Bệnh Học...", "1.500+ Loài Cây").
   - **XÓA BỎ hoàn toàn khối oval xám to đùng thống kê số liệu** (*"1.500+ loài cây trồng • 3.000+ hồ sơ bệnh lâm sàng • 100% Chuẩn VietGAP • < 2ms RAG nội tại"*).
   - **XÓA BỎ hoàn toàn cụm từ phô trương:** *"Kho Siêu Dữ Liệu Bệnh Học Cây Trồng Số 1 Việt Nam"*.
   - Đỉnh trang chỉ giữ lại **Nút mở Sidebar** nổi mềm mại ở góc trên bên trái, tiêu đề **"Kho dữ liệu cây trồng"**, dòng mô tả ngắn 1 dòng khiêm tốn, kế tiếp là thanh Tìm kiếm + nút Bộ lọc.
3. **Đồng bộ nút Sidebar & Sửa dứt điểm Bug điều hướng:**
   - Hiện tại bấm vào nút trên `/crops` bị bug tự động chuyển trang (`router.push('/')`) về đoạn chat cũ mà **KHÔNG mở được Sidebar**.
   - **Sửa lại:** Nhúng component `<AppSidebar />` vào layout/page của `/crops`, khi người dùng bấm vào nút Sidebar thì gọi hàm `toggleSidebar()` từ `ChatContext` để thanh Sidebar trượt ra tại chỗ mượt mà, giúp người dùng dễ dàng chuyển đổi qua lại giữa Chat và Kho dữ liệu.
4. **Xóa nút đen "Hỏi AI cây này" trong Modal chi tiết cây:**
   - Trong modal xem bệnh học của cây, **XÓA BỎ HOÀN TOÀN** nút màu đen to đùng `Hỏi AI cây này` nằm ở góc trên cạnh nút đóng. Góc trên modal chỉ giữ lại duy nhất nút đóng **`✕`**.
5. **Thanh tìm kiếm & Nút Bộ lọc (Filter):**
   - Xóa bỏ hàng nút tab dài ngoằng (`Tất cả cây trồng`, `Cây ăn trái đặc sản`...).
   - Thay bằng 1 nút **"Bộ lọc" (`SlidersHorizontal`)** bấm mở popover cho phép tích chọn danh mục cây trồng.
6. **Infinite Scroll tối ưu hiệu năng:**
   - Ban đầu chỉ nạp 20 cây, khi người dùng cuộn xuống đáy thì tự động tải tiếp 20 cây tiếp theo (`IntersectionObserver`), tối ưu RAM để thiết bị di động lướt mượt mà 60 FPS.

---

## 🖼️ NHIỆM VỤ 3: TÍNH NĂNG ĐỔI ẢNH ĐẠI DIỆN (AVATAR) & LƯU VÀO DATABASE SUPABASE
- **Tệp chỉnh sửa:** `src/app/settings/page.tsx`, `src/context/ChatContext.tsx`
- **Hành động cụ thể:**
  1. Khi người dùng bấm vào Avatar hoặc nút bút chì trên trang Cài đặt, kích hoạt thẻ `<input type="file" accept="image/*" className="hidden" />` cho phép chọn ảnh từ thư viện hoặc chụp từ camera điện thoại.
  2. Tự động vẽ ảnh lên `<canvas>` nén về kích thước chuẩn `160x160px` định dạng JPEG/WebP siêu nhẹ (~20KB - 30KB) dưới dạng chuỗi Base64.
  3. Cập nhật trực tiếp vào bảng `profiles` trên Database Supabase:
     ```typescript
     await supabase
       .from('profiles')
       .update({ 
         avatar_url: compressedBase64,
         updated_at: new Date().toISOString()
       })
       .eq('id', currentUser.id);
     ```
  4. Cập nhật vào `currentUser.avatar_url` trong state và `localStorage`, hiển thị ngay lập tức ảnh đại diện mới trên trang Cài đặt, chân Sidebar và trong bong bóng chat người dùng.

---

## 🔍 NHIỆM VỤ 4: TÍCH HỢP TAVILY SEARCH MAX POWER VỚI CỤM 5 KEYS (HARDCODE BASE64)
- **Tệp chỉnh sửa:** Tạo `src/lib/tavilySearch.ts` và tích hợp vào `src/app/api/chat/route.ts` thay thế hoàn toàn cho 9Router search.
- **Yêu cầu mã hóa bắt buộc (Anti-GitGuardian / Secret Scanner):**
  - **TUYỆT ĐỐI KHÔNG** để lộ chuỗi literal bắt đầu bằng `tvly-` trong mã nguồn.
  - Phải **hardcode trực tiếp vào code** bằng cơ chế **mã hóa Base64 tách chuỗi (Split-string base64 obfuscation)** và giải mã lúc runtime.
- **Cơ chế Cụm 5 Keys Xoay Vòng & Auto-Failover (5.000 requests/tháng):**
  - Hệ thống sử dụng xoay vòng 5 key. Nếu một key gặp lỗi hạn ngạch (HTTP 429 hoặc 432), hệ thống tự động nhảy sang key kế tiếp trong 0.001s.
- **Bật tối đa sức mạnh Tavily:**
  - `search_depth: "advanced"`: Đào sâu tài liệu chuyên khảo & file PDF nghiên cứu.
  - `include_answer: "advanced"`: Tự động tổng hợp tóm tắt phác đồ y học nông nghiệp.
  - `include_images: true` & `include_image_descriptions: true`: Cào luôn ảnh mẫu bệnh thực tế kèm mô tả để AI hiển thị cho bà con đối chiếu.
  - `include_domains`: Giới hạn tìm kiếm trong các nguồn nông nghiệp đầu ngành:
    `["khuyennongvn.gov.vn", "sofri.org.vn", "bvtv.gov.vn", "ctu.edu.vn", "nongnghiep.vn"]`.

---

## 🚀 TIÊU CHUẨN HOÀN TẤT & DEPLOY:
1. Chạy `npm run build` kiểm tra 100% Pass không có lỗi TypeScript hay Turbopack.
2. Commit và push lên nhánh `main` với thông điệp sạch sẽ:
   ```bash
   git add -A
   git commit -m "feat(agrivision): harvest full disease spectrum, redesign crops encyclopedia, enable real avatar upload, and integrate 5-key Tavily search cluster"
   git push origin main
   ```
Render sẽ tự động build và triển khai bản cập nhật hoàn hảo trực tiếp tại: **https://ultra-project.onrender.com**.
