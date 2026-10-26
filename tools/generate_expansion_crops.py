# -*- coding: utf-8 -*-
"""
Botany & Plant Pathology Expansion Dataset Generator for AgriVision
Author: Phan Trọng Khang (Lớp 9¹, THCS Vĩnh An)
Generates 600+ new unique crops covering 63 Vietnamese provinces and high-tech exotic crops.
"""
import json
import os

EXPANSION_CROPS = [
    # --- 1. CÂY KINH TẾ CAO DU NHẬP & CÔNG NGHỆ CAO (EXOTIC & HIGH-TECH CROPS) ---
    {
        "topic": "Cay_Nhap_Khau_Kinh_Te_Cao",
        "name_vi": "Việt quất nhiệt đới Southern Highbush",
        "scientific_name": "Vaccinium darrowii 'Southern Highbush'",
        "dia_ban_pho_bien": ["Đà Lạt", "Đơn Dương", "Lâm Hà", "Mộc Châu"],
        "dac_tinh_sinh_thai": "Cây bụi ưa đất chua pH 4.5 - 5.2, thoát nước cực tốt, trồng giá thể vỏ thông + xơ dừa trong nhà màng công nghệ cao.",
        "danh_sach_benh": [
            {
                "ten_benh": "Bệnh Thối rễ lở cổ rễ Phytophthora",
                "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
                "tac_nhan": {"loai": "Nấm", "ten_khoa_hoc": "Phytophthora cinnamomi"},
                "trieu_chung_dien_hinh": [
                    "Lá úa vàng từ ngọn, chuyển sang màu đỏ gạch rồi rụng trơ cành",
                    "Rễ tơ màu nâu đen, vỏ rễ tuột khỏi lõi gỗ khi kéo nhẹ",
                    "Cây còi cọc, ngưng đâm chồi mới và chết lụi dần"
                ],
                "phan_biet_chan_doan_kep": "Khác với thiếu sắt (lá vàng gân xanh ở chồi non nhưng rễ trắng khỏe); Phytophthora làm rễ thối đen mục nát.",
                "kiem_tra_thuc_dia": "Nhổ nhẹ bầu rễ kiểm tra rễ tơ xem có bị thối nâu đen và ngửi mùi úng chua.",
                "phac_do_vietgap": {
                    "canh_tac": "Kê cao chậu/túi bầu cách ly mặt đất 20cm, không để ứ nước đáy chậu",
                    "sinh_hoc": "Tưới định kỳ nấm đối kháng Trichoderma asperellum kết hợp chế phẩm Phosphonate sinh học",
                    "khuyen_cao_chuyen_gia": "Giữ pH giá thể ổn định 4.8 - 5.0 và kiểm soát độ ẩm giá thể không vượt quá 70%"
                }
            },
            {
                "ten_benh": "Bệnh Mốc xám quả chín (Botrytis Blight)",
                "muc_do_nguy_hiem": "Nặng",
                "tac_nhan": {"loai": "Nấm", "ten_khoa_hoc": "Botrytis cinerea"},
                "trieu_chung_dien_hinh": [
                    "Chùm hoa bị thối nhũn nâu sẫm, rụng sớm",
                    "Quả non và quả chín bị bao phủ một lớp tơ nấm màu xám tro như bụi khói",
                    "Quả bị mềm nhũn, chảy dịch chua và khô quắt lại dính trên cuống"
                ],
                "phan_biet_chan_doan_kep": "Khác với thán thư Colletotrichum (vết bệnh tròn lõm màu đen có dịch cam); Botrytis có lớp phấn mốc xám dày đặc.",
                "kiem_tra_thuc_dia": "Gõ nhẹ chùm quả thấy bụi phấn bào tử màu xám bay ra trong không khí ẩm.",
                "phac_do_vietgap": {
                    "canh_tac": "Tỉa thưa tán cành, bật quạt thông gió trong nhà màng giảm độ ẩm không khí < 80%",
                    "sinh_hoc": "Phun phòng chế phẩm vi khuẩn Bacillus subtilis hoặc nấm đối kháng Clonostachys rosea",
                    "khuyen_cao_chuyen_gia": "Thu hoạch quả ngay khi đạt độ chín, cách ly quả bệnh trong túi nilon kín"
                }
            }
        ]
    },
    {
        "topic": "Cay_Nhap_Khau_Kinh_Te_Cao",
        "name_vi": "Dâu tây New Zealand Mộc Châu",
        "scientific_name": "Fragaria × ananassa 'New Zealand'",
        "dia_ban_pho_bien": ["Mộc Châu", "Đà Lạt", "Sa Pa"],
        "dac_tinh_sinh_thai": "Cây thân thảo, ưa khí hậu ôn đới 15 - 24 độ C, trồng giàn bán thủy canh hoặc giá thể mụn xơ dừa xử lý tanin.",
        "danh_sach_benh": [
            {
                "ten_benh": "Bệnh Đốm mắt cua (Mycosphaerella Leaf Spot)",
                "muc_do_nguy_hiem": "Trung bình",
                "tac_nhan": {"loai": "Nấm", "ten_khoa_hoc": "Mycosphaerella fragariae"},
                "trieu_chung_dien_hinh": [
                    "Đốm tròn nhỏ 3-6mm trên lá, tâm trắng xám viền đỏ tía sẫm như mắt chim/mắt cua",
                    "Nhiều vết đốm liên kết làm phiến lá cháy rụi từng mảng",
                    "Cuống lá và cuống quả xuất hiện đốm lõm nâu sẫm làm héo quả non"
                ],
                "phan_biet_chan_doan_kep": "Khác với đốm góc lá Xanthomonas (vết bệnh bị chặn bởi gân lá soi ngược sáng trong suốt); mắt cua có tâm tròn trắng xám.",
                "kiem_tra_thuc_dia": "Soi mặt trên lá tìm vết tròn tâm trắng viền tím đặc trưng.",
                "phac_do_vietgap": {
                    "canh_tac": "Vặt bỏ lá già sát gốc, tưới nhỏ giọt không làm ướt phiến lá",
                    "sinh_hoc": "Phun nấm đối kháng Chaetomium cupreum kết hợp nano bạc đồng sinh học",
                    "khuyen_cao_chuyen_gia": "Phun ngừa giai đoạn bén rễ hồi xanh và phân hóa mầm hoa"
                }
            },
            {
                "ten_benh": "Bệnh Phấn trắng Dâu tây (Powdery Mildew)",
                "muc_do_nguy_hiem": "Nặng",
                "tac_nhan": {"loai": "Nấm", "ten_khoa_hoc": "Podosphaera aphanis"},
                "trieu_chung_dien_hinh": [
                    "Mặt dưới lá phủ lớp bột trắng mịn như phấn rôm",
                    "Mép lá cong vênh cuốn ngược lên trên hình lòng chảo",
                    "Quả non bị bao phủ lớp phấn trắng, quả chai cứng không lớn được, quả chín mất vị ngọt"
                ],
                "phan_biet_chan_doan_kep": "Khác với bọ trĩ chích hút (lá bị quăn nhưng không có lớp bột trắng cọ tróc được).",
                "kiem_tra_thuc_dia": "Dùng ngón tay miết mặt dưới lá thấy bột trắng mịn dính vào đầu ngón tay.",
                "phac_do_vietgap": {
                    "canh_tac": "Giảm bón thừa đạm, tăng cường kali hữu cơ và silic sinh học làm dày vách tế bào",
                    "sinh_hoc": "Phun dung dịch Baking Soda (NaHCO3 0.3%) hoặc dầu khoáng sinh học SK 99EC",
                    "khuyen_cao_chuyen_gia": "Phun luân phiên sáng sớm khi nấm vừa phóng thích bào tử"
                }
            }
        ]
    },
    {
        "topic": "Cay_Nhap_Khau_Kinh_Te_Cao",
        "name_vi": "Nho mẫu đơn Shine Muscat Nhật Bản",
        "scientific_name": "Vitis vinifera 'Shine Muscat'",
        "dia_ban_pho_bien": ["Ninh Thuận", "Bình Thuận", "Đà Lạt"],
        "dac_tinh_sinh_thai": "Giống nho xanh không hạt cao cấp, quả to giòn ngọt hương xoài, bắt buộc trồng giàn chữ Y có mái che nilon chống mưa axit.",
        "danh_sach_benh": [
            {
                "ten_benh": "Bệnh Sương mai Nho (Downy Mildew)",
                "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
                "tac_nhan": {"loai": "Nấm", "ten_khoa_hoc": "Plasmopara viticola"},
                "trieu_chung_dien_hinh": [
                    "Vết bệnh ban đầu như giọt dầu loang màu vàng nhạt trên mặt trên lá",
                    "Mặt dưới lá tương ứng xuất hiện lớp nấm tơ màu trắng xốp như bông tuyết vào sáng sớm sương mù",
                    "Chùm quả non bị quăn queo, teo tóp chuyển nâu đen và rụng hàng loạt"
                ],
                "phan_biet_chan_doan_kep": "Khác với phấn trắng (phấn trắng phủ cả 2 mặt lá dạng bụi khô mỏng); sương mai có lớp bông trắng xốp dày ở mặt dưới lá nơi ẩm ướt.",
                "kiem_tra_thuc_dia": "Kiểm tra mặt dưới vết bệnh vàng vào sáng sớm xem lớp bông tuyết tơ nấm trắng.",
                "phac_do_vietgap": {
                    "canh_tac": "Duy trì mái che nilon kín không để nước mưa tạt vào chùm quả, tỉa bỏ cành vượt",
                    "sinh_hoc": "Phun đồng đỏ Nano sinh học kết hợp chế phẩm Chitosan kích hoạt hệ miễn dịch SAR",
                    "khuyen_cao_chuyen_gia": "Phun phòng ngừa ngay trước và sau các đợt mưa dông chuyển mùa"
                }
            },
            {
                "ten_benh": "Bệnh Nứt quả thối chùm Nho Mẫu Đơn",
                "muc_do_nguy_hiem": "Nặng",
                "tac_nhan": {"loai": "Nấm cơ hội", "ten_khoa_hoc": "Aspergillus niger & Rhizopus stolonifer"},
                "trieu_chung_dien_hinh": [
                    "Vỏ quả nho căng mọng bị nứt dọc do chênh lệch áp suất thẩm thấu khi độ ẩm đất biến động",
                    "Từ vết nứt, dịch đường rỉ ra thu hút nấm men và nấm đen phát triển làm thối rữa cả chùm",
                    "Chùm quả bốc mùi rượu chua nồng nặc"
                ],
                "phan_biet_chan_doan_kep": "Khác với rầy chích hút (vết nứt cơ học do thừa nước kết hợp nấm mốc đen cơ hội).",
                "kiem_tra_thuc_dia": "Ngửi chùm quả thấy mùi men rượu chua và thấy vết nứt vỏ dọc theo thân quả.",
                "phac_do_vietgap": {
                    "canh_tac": "Bao chùm quả bằng túi giấy chuyên dụng chống thấm, duy trì độ ẩm tưới đều đặn không để đất quá khô rồi tưới dồn",
                    "sinh_hoc": "Phun chế phẩm Bacillus subtilis 10^9 CFU/ml ức chế nấm men thối rữa",
                    "khuyen_cao_chuyen_gia": "Bổ sung Canxi-Bo hữu cơ giai đoạn quả bắt đầu chuyển đường làm dai vỏ quả"
                }
            }
        ]
    },
    {
        "topic": "Cay_Nhap_Khau_Kinh_Te_Cao",
        "name_vi": "Măng tây xanh Green Asparagus",
        "scientific_name": "Asparagus officinalis 'UC-157'",
        "dia_ban_pho_bien": ["Ninh Thuận", "Bình Thuận", "Củ Chi", "Vĩnh Long", "Đồng Tháp"],
        "dac_tinh_sinh_thai": "Cây lâu năm lấy chồi mầm măng, ưa đất cát pha hoặc phù sa tơi xốp tầng canh tác sâu > 50cm, pH 6.5 - 7.5, mẫn cảm với ngập úng rễ.",
        "danh_sach_benh": [
            {
                "ten_benh": "Bệnh Héo vàng khô thân Măng Tây (Fusarium Crown and Root Rot)",
                "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
                "tac_nhan": {"loai": "Nấm", "ten_khoa_hoc": "Fusarium oxysporum f. sp. asparagi"},
                "trieu_chung_dien_hinh": [
                    "Cây măng mẹ bị vàng rũ từ cành lá kim xuống gốc, thân teo tóp khô giòn",
                    "Cổ rễ và chồi măng non dưới mặt đất bị thâm đen, lõi mạch dẫn hóa nâu đỏ",
                    "Gốc măng mục nát, rễ củ tích trữ dinh dưỡng bị rỗng ruột"
                ],
                "phan_biet_chan_doan_kep": "Khác với sâu đục gốc (vết cắn đứt rỗng thân có phân sâu); nấm Fusarium làm thâm đen bó mạch từ trong ra ngoài không có phân sâu.",
                "kiem_tra_thuc_dia": "Cắt ngang phần gốc sát cổ rễ thấy vòng mạch dẫn hóa nâu đỏ sẫm.",
                "phac_do_vietgap": {
                    "canh_tac": "Lên luống cao 30-40cm, đào rãnh thoát nước sâu giữa các hàng măng, rải vôi khử trùng hàng năm",
                    "sinh_hoc": "Tưới gốc hỗn hợp Trichoderma virens + Bacillus amyloliquefaciens định kỳ 20 ngày/lần",
                    "khuyen_cao_chuyen_gia": "Tuyệt đối không dùng nguồn giống từ vườn đã có tiền sử nhiễm bệnh Fusarium"
                }
            },
            {
                "ten_benh": "Bệnh Đốm thân thán thư Cercospora",
                "muc_do_nguy_hiem": "Trung bình",
                "tac_nhan": {"loai": "Nấm", "ten_khoa_hoc": "Cercospora asparagi"},
                "trieu_chung_dien_hinh": [
                    "Thân và cành nhánh xuất hiện các vết đốm bầu dục nhỏ màu nâu xám viền đỏ",
                    "Bệnh nặng làm cành lá kim rụng sớm hàng loạt, trơ lại cọc thân xơ xác",
                    "Cây mất khả năng quang hợp tích lũy đường bột về củ măng"
                ],
                "phan_biet_chan_doan_kep": "Khác với cháy nắng (vết cháy mảng dài màu trắng ngà); Cercospora có các chấm đen li ti là ổ bào tử nấm ở tâm đốm.",
                "kiem_tra_thuc_dia": "Soi kính lúp thấy các chấm đen nhỏ nổi gồ giữa tâm đốm xám trên thân cây.",
                "phac_do_vietgap": {
                    "canh_tac": "Cắt tỉa bớt cây mẹ già cỗi tạo độ thông thoáng gốc, thu gom cành bệnh tiêu hủy",
                    "sinh_hoc": "Phun phòng nano đồng sinh học kết hợp dịch chiết tỏi ớt gừng ức chế nảy mầm bào tử",
                    "khuyen_cao_chuyen_gia": "Phun luân phiên chế phẩm sinh học sau mỗi đợt cắt tỉa cây mẹ"
                }
            }
        ]
    },
    {
        "topic": "Cay_Nhap_Khau_Kinh_Te_Cao",
        "name_vi": "Phong lan Vani Vanilla Bourbon",
        "scientific_name": "Vanilla planifolia 'Bourbon'",
        "dia_ban_pho_bien": ["Bình Dương", "Đắk Lắk", "Gia Lai", "Lâm Đồng"],
        "dac_tinh_sinh_thai": "Cây lan leo lấy quả hương vani tự nhiên quý giá, cần trụ leo sống (cây xoan ổi, cây cọc rào), che lưới lan 50% bóng râm, giá thể thảm mục giàu mùn hữu cơ.",
        "danh_sach_benh": [
            {
                "ten_benh": "Bệnh Thối thân rễ Vanilla (Fusarium Root Rot)",
                "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
                "tac_nhan": {"loai": "Nấm", "ten_khoa_hoc": "Fusarium oxysporum f. sp. vanillae"},
                "trieu_chung_dien_hinh": [
                    "Rễ khí sinh bám trụ và rễ đất bị thâm đen, teo tóp khô quắt lại",
                    "Các lóng thân sát gốc chuyển màu vàng nâu rồi úng nhũn thâm đen đứt đoạn",
                    "Lá bị mất nước nhăn nheo, héo rũ từ gốc lên ngọn cây"
                ],
                "phan_biet_chan_doan_kep": "Khác với thiếu nước sinh lý (thân lá nhăn nhưng rễ vẫn xanh tươi); nấm bệnh làm rễ thối đen đứt lìa khỏi trụ leo.",
                "kiem_tra_thuc_dia": "Cắt nhẹ đốt thân bị teo kiểm tra mạch dẫn bên trong bị thâm đen và có dịch nhớt.",
                "phac_do_vietgap": {
                    "canh_tac": "Khử trùng kéo cắt bằng cồn 90 độ khi tỉa cành, không tưới nước đọng ở nách lá",
                    "sinh_hoc": "Tưới rễ định kỳ chế phẩm vi sinh Streptomyces lydicus kết hợp Trichoderma harzianum",
                    "khuyen_cao_chuyen_gia": "Cách ly ngay đoạn dây bị thối, quét vôi đặc hoặc bột quế nguyên chất vào vết cắt"
                }
            },
            {
                "ten_benh": "Bệnh Thán thư đốm quả Vanilla (Anthracnose)",
                "muc_do_nguy_hiem": "Nặng",
                "tac_nhan": {"loai": "Nấm", "ten_khoa_hoc": "Colletotrichum vanillae"},
                "trieu_chung_dien_hinh": [
                    "Đầu quả đậu vani xuất hiện vết đốm đen tròn lõm xuống",
                    "Vết bệnh lan nhanh dọc theo thân quả làm quả bị thâm đen, cong vẹo và rụng non",
                    "Làm mất hoàn toàn lượng tinh dầu vanillin quý giá trong quả"
                ],
                "phan_biet_chan_doan_kep": "Khác với vết rám nắng (chỉ ở mặt quả đón nắng; thán thư ở cả mặt khuất gió và ứa dịch nấm màu hồng cam).",
                "kiem_tra_thuc_dia": "Bóp nhẹ quả vani thấy vỏ mềm nhũn, tiết dịch nấm đặc dính.",
                "phac_do_vietgap": {
                    "canh_tac": "Đảm bảo giàn che thông gió, không để nước mưa ứ đọng trên chùm quả",
                    "sinh_hoc": "Phun phòng nano bạc hữu cơ kết hợp nấm Chaetomium liều lượng 2ml/lít nước",
                    "khuyen_cao_chuyen_gia": "Phun phòng ngừa ngay sau giai đoạn thụ phấn nhân tạo thành công"
                }
            }
        ]
    },
    {
        "topic": "Cay_Nhap_Khau_Kinh_Te_Cao",
        "name_vi": "Nghệ tây Saffron Crocus sativus",
        "scientific_name": "Crocus sativus 'Kashmir'",
        "dia_ban_pho_bien": ["Đà Lạt", "Sa Pa", "Mộc Châu"],
        "dac_tinh_sinh_thai": "Cây củ lấy nhụy hoa nghệ tây đắt đỏ nhất thế giới, trồng phòng lạnh kiểm soát nhiệt độ 15-20 độ C hoặc nhà kính cao nguyên mát mẻ, đất tơi xốp cát pha giàu mùn thoát nước tuyệt đối.",
        "danh_sach_benh": [
            {
                "ten_benh": "Bệnh Thối củ Saffron (Corm Rot)",
                "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
                "tac_nhan": {"loai": "Nấm", "ten_khoa_hoc": "Fusarium oxysporum f. sp. gladioli"},
                "trieu_chung_dien_hinh": [
                    "Lớp vỏ bọc củ bị thâm đen mủn mục, củ bên trong bị thối nhũn nâu đỏ",
                    "Mầm hoa nhú lên bị vàng khô không bung được cánh, nhụy hoa teo tóp biến dạng",
                    "Toàn bộ củ giống bị tiêu biến thành đống bột khô màu nâu"
                ],
                "phan_biet_chan_doan_kep": "Khác với chuột cắn củ (vết gặm có dấu răng sắc nhọn; nấm bệnh làm thối nhũn có mùi nấm mốc nồng).",
                "kiem_tra_thuc_dia": "Ấn ngón tay vào củ thấy vỏ lún mềm xốp, tiết nước chua hôi nấm mốc.",
                "phac_do_vietgap": {
                    "canh_tac": "Xử lý đất và giá thể bằng phương pháp xông hơi nóng hoặc phơi ải trước khi tra củ giống",
                    "sinh_hoc": "Ngâm xử lý củ giống 30 phút trong dung dịch Trichoderma viride trước khi gieo trồng",
                    "khuyen_cao_chuyen_gia": "Tuyệt đối kiểm soát độ ẩm giá thể không vượt quá 60% trong giai đoạn ủ mầm hoa"
                }
            },
            {
                "ten_benh": "Bệnh Cháy khô đầu lá Saffron (Leaf Blight)",
                "muc_do_nguy_hiem": "Trung bình",
                "tac_nhan": {"loai": "Nấm", "ten_khoa_hoc": "Rhizoctonia crocorum"},
                "trieu_chung_dien_hinh": [
                    "Lá kim thanh mảnh bị cháy khô từ chóp lá lùi dần xuống gốc",
                    "Xuất hiện các hạch nấm nhỏ li ti màu nâu đen bám quanh gốc lá sát mặt củ",
                    "Giảm diện tích quang hợp làm suy kiệt củ con thế hệ sau"
                ],
                "phan_biet_chan_doan_kep": "Khác với cháy đầu lá do thiếu nước (lá khô ráo không có hạch nấm; bệnh do nấm có hạch nấm li ti).",
                "kiem_tra_thuc_dia": "Dùng kính lúp kiểm tra gốc lá tìm các hạch nấm nhỏ li ti màu hạt mè nâu đen.",
                "phac_do_vietgap": {
                    "canh_tac": "Tưới nước nhỏ giọt vào gốc, giữ lá khô ráo trong nhà kính",
                    "sinh_hoc": "Phun nấm đối kháng Bacillus subtilis định kỳ 10 ngày/lần",
                    "khuyen_cao_chuyen_gia": "Duy trì thông gió liên tục trong phòng sinh trưởng của cây"
                }
            }
        ]
    },
    {
        "topic": "Cay_Nhap_Khau_Kinh_Te_Cao",
        "name_vi": "Nho thân gỗ tứ quý Nam Mỹ Jabuticaba",
        "scientific_name": "Plinia cauliflora 'Four Seasons'",
        "dia_ban_pho_bien": ["Đà Lạt", "Đồng Nai", "Bến Tre", "Vĩnh Long", "Hà Nội"],
        "dac_tinh_sinh_thai": "Cây thân gỗ lâu năm, hoa và quả mọc chi chít trên thân cành chính, ưa đất thịt màu mỡ pha cát, thích nghi cả khí hậu nhiệt đới và cận nhiệt.",
        "danh_sach_benh": [
            {
                "ten_benh": "Bệnh Gỉ sắt Nho thân gỗ (Myrtle Rust)",
                "muc_do_nguy_hiem": "Nặng",
                "tac_nhan": {"loai": "Nấm", "ten_khoa_hoc": "Austropuccinia psidii"},
                "trieu_chung_dien_hinh": [
                    "Chồi non, lá bánh tẻ và nụ hoa xuất hiện các ổ bột màu vàng nghệ tươi rực rỡ",
                    "Lá bị biến dạng phồng rộp, chồi non khô đen chết cháy",
                    "Làm rụng toàn bộ lứa hoa và quả non bám trên thân gỗ"
                ],
                "phan_biet_chan_doan_kep": "Khác với phấn hoa tự nhiên (chỉ ở nhị hoa; gỉ sắt mọc thành ổ sần sùi trên cả vỏ cành và phiến lá).",
                "kiem_tra_thuc_dia": "Quẹt ngón tay vào vết bệnh thấy dính lớp bột màu vàng cam sáng như bột nghệ.",
                "phac_do_vietgap": {
                    "canh_tac": "Cắt tỉa cành tăm cành vượt trong tán, giữ thân chính đón ánh sáng trực tiếp",
                    "sinh_hoc": "Phun phòng bằng chế phẩm vi sinh đối kháng Bacillus amyloliquefaciens kết hợp nano lưu huỳnh sinh học",
                    "khuyen_cao_chuyen_gia": "Phun ngay khi cây nhú các đợt lộc non hoặc mắt cua hoa trên thân"
                }
            },
            {
                "ten_benh": "Bệnh Thối nứt vỏ thân chảy gôm (Stem Canker)",
                "muc_do_nguy_hiem": "Cao",
                "tac_nhan": {"loai": "Nấm", "ten_khoa_hoc": "Botryosphaeria dothidea"},
                "trieu_chung_dien_hinh": [
                    "Vỏ thân chính xuất hiện các vết nứt dọc, rỉ ra những giọt nhựa màu nâu đỏ dính nhớt",
                    "Mô vỏ quanh vết nứt bị hoại tử thâm đen, phần gỗ bên dưới chuyển màu xám tro",
                    "Cành phía trên vết nứt bị héo lá và chết dần từng nhánh"
                ],
                "phan_biet_chan_doan_kep": "Khác với xì mủ do sâu đục thân (có lỗ khoét đùn phân mùn cưa; nấm nứt thân không có mùn cưa).",
                "kiem_tra_thuc_dia": "Cạo nhẹ lớp vỏ nứt thấy mô gỗ bên dưới có sọc thâm đen lan dọc thân cành.",
                "phac_do_vietgap": {
                    "canh_tac": "Cạo sạch phần vỏ hoại tử bằng dao khử trùng, quét vôi trộn đồng đỏ bảo vệ thân cây",
                    "sinh_hoc": "Quét gốc hỗn hợp nấm đối kháng Trichoderma harzianum đậm đặc vào vùng tổn thương",
                    "khuyen_cao_chuyen_gia": "Tránh va chạm cơ học làm rách vỏ thân khi chăm sóc và thu hoạch quả"
                }
            }
        ]
    },
    {
        "topic": "Cay_Nhap_Khau_Kinh_Te_Cao",
        "name_vi": "Wasabi Đà Lạt mù tạt Nhật Bản",
        "scientific_name": "Eutrema japonicum 'Daruma'",
        "dia_ban_pho_bien": ["Đà Lạt", "Lạc Dương"],
        "dac_tinh_sinh_thai": "Cây củ gia vị cao cấp, bắt buộc trồng vùng nước chảy róc rách ven suối lạnh 12 - 18 độ C hoặc hệ thống thủy canh hồi lưu có chiller làm lạnh nước, râm mát 70%.",
        "danh_sach_benh": [
            {
                "ten_benh": "Bệnh Thối đen thân củ Wasabi (Black Leg)",
                "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
                "tac_nhan": {"loai": "Nấm", "ten_khoa_hoc": "Phoma lingam / Plenodomus lingam"},
                "trieu_chung_dien_hinh": [
                    "Phần gốc sát mặt nước xuất hiện các vết lõm màu đen hình bầu dục",
                    "Củ wasabi bên trong bị thâm đen ruột, mất hoàn toàn vị cay nồng đặc trưng",
                    "Lá vàng úa, cây bị gãy ngang cổ củ và chết rụi trôi theo dòng nước"
                ],
                "phan_biet_chan_doan_kep": "Khác với thiếu oxy rễ (rễ ngả vàng không có vết lõm đen; Black Leg có vết loét đen sâu vào củ).",
                "kiem_tra_thuc_dia": "Cắt ngang củ wasabi thấy các vòng tròn chấm đen hoại tử trong bó mạch dẫn.",
                "phac_do_vietgap": {
                    "canh_tac": "Khử trùng nguồn nước bằng đèn UV công suất cao, duy trì nhiệt độ nước < 16 độ C",
                    "sinh_hoc": "Bổ sung vi khuẩn đối kháng Pseudomonas fluorescens vào dòng dinh dưỡng thủy canh",
                    "khuyen_cao_chuyen_gia": "Tiêu hủy ngay các cây chớm có vết đen để tránh lây lan theo dòng nước chảy"
                }
            },
            {
                "ten_benh": "Bệnh Thối nhũn vi khuẩn Wasabi (Bacterial Soft Rot)",
                "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
                "tac_nhan": {"loai": "Nấm & Vi khuẩn", "ten_khoa_hoc": "Pectobacterium carotovorum"},
                "trieu_chung_dien_hinh": [
                    "Cuống lá và chồi ngọn bị úng nước, nhũn mềm biến thành chất nhầy nhớt",
                    "Củ bị thối nhũn từ chóp xuống, bốc mùi hôi thối nồng nặc đặc trưng",
                    "Toàn bộ cây sụp đổ chỉ sau 24-48 giờ khi nhiệt độ nước tăng quá 20 độ C"
                ],
                "phan_biet_chan_doan_kep": "Khác với nấm thối khô (vết thối khô ráo không mùi; Pectobacterium thối ướt nhầy nhụa mùi hôi nồng).",
                "kiem_tra_thuc_dia": "Ngửi mùi mô bệnh thấy bốc mùi hôi thối tanh tưởi của vi khuẩn phân hủy protein.",
                "phac_do_vietgap": {
                    "canh_tac": "Hạ nhiệt độ nước ngay lập tức xuống 14 độ C, tăng sục khí oxy hòa tan > 8 mg/l",
                    "sinh_hoc": "Châm dung dịch Kasugamycin sinh học hoặc nano bạc diệt khuẩn vào bồn chứa",
                    "khuyen_cao_chuyen_gia": "Khử trùng định kỳ toàn bộ ống dẫn và giàn trồng sau mỗi chu kỳ thu hoạch"
                }
            }
        ]
    },
    {
        "topic": "Cay_Nhap_Khau_Kinh_Te_Cao",
        "name_vi": "Chà là Trung Đông Barhi cấy mô",
        "scientific_name": "Phoenix dactylifera 'Barhi Tissue Culture'",
        "dia_ban_pho_bien": ["Đồng Tháp", "Vĩnh Long", "Tây Ninh", "Bình Thuận", "An Giang"],
        "dac_tinh_sinh_thai": "Cây họ cau dừa, ăn quả tươi giòn ngọt, chịu hạn và phèn mặn rất tốt, ưa nắng gắt nhiệt độ cao, nhạy cảm với ngập úng ngọn vào mùa mưa dầm.",
        "danh_sach_benh": [
            {
                "ten_benh": "Bệnh Thối đọt non Chà Là (Black Scorch Disease)",
                "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
                "tac_nhan": {"loai": "Nấm", "ten_khoa_hoc": "Thielaviopsis paradoxa"},
                "trieu_chung_dien_hinh": [
                    "Đọt non trung tâm bị cháy đen như bị lửa đốt (black scorch)",
                    "Các bẹ lá non bị thâm đen khô quắt, củ đọt bị thối nhũn và đổ gục ngang",
                    "Cây mất đỉnh sinh trưởng dẫn đến chết hoàn toàn"
                ],
                "phan_biet_chan_doan_kep": "Khác với bọ cánh cứng cắn đọt (có vết gặm răng cưa; nấm bệnh làm lá non cháy đen giòn như than).",
                "kiem_tra_thuc_dia": "Rút nhẹ đọt non trung tâm thấy tuột gốc đọt thâm đen bốc mùi rượu chua lên men.",
                "phac_do_vietgap": {
                    "canh_tac": "Dọn dẹp bẹ lá già khô quanh cổ hũ, che nón bảo vệ đọt non trong mùa mưa dầm ĐBSCL",
                    "sinh_hoc": "Rải nấm đối kháng Trichoderma harzianum quanh gốc và phun nano đồng hữu cơ lên đỉnh sinh trưởng",
                    "khuyen_cao_chuyen_gia": "Phun phòng ngừa ngay sau các đợt mưa bão kéo dài nhiều ngày"
                }
            },
            {
                "ten_benh": "Bệnh Đốm lá than Graphiola (False Smut)",
                "muc_do_nguy_hiem": "Trung bình",
                "tac_nhan": {"loai": "Nấm", "ten_khoa_hoc": "Graphiola phoenicis"},
                "trieu_chung_dien_hinh": [
                    "Cả 2 mặt lá già xuất hiện vô số nốt sần cứng nhỏ 1-3mm màu đen nhô cao như hạt cát",
                    "Khi già, đỉnh nốt sần nứt ra phóng thích sợi tơ nấm màu vàng nhạt chứa đầy bào tử",
                    "Lá già bị vàng úa khô sớm làm giảm thẩm mỹ cây kiểng và giảm năng suất quả"
                ],
                "phan_biet_chan_doan_kep": "Khác với bọ trĩ chích hút (nốt Graphiola sần cứng cậy ra được hạt than đen).",
                "kiem_tra_thuc_dia": "Dùng móng tay cạy nốt sần đen thấy tróc ra hạt cứng như vảy than.",
                "phac_do_vietgap": {
                    "canh_tac": "Cắt tỉa các tàu lá già nhiễm nặng đem chôn tiêu hủy, tưới gốc không phun ướt tán lá",
                    "sinh_hoc": "Phun dung dịch nano lưu huỳnh kết hợp nấm Chaetomium liều lượng 2.5ml/lít nước",
                    "khuyen_cao_chuyen_gia": "Phun vào lúc trời râm mát tránh ánh nắng gắt trực tiếp"
                }
            }
        ]
    },
    {
        "topic": "Cay_Nhap_Khau_Kinh_Te_Cao",
        "name_vi": "Cherry nhiệt đới Surinam Pitanga",
        "scientific_name": "Eugenia uniflora 'Surinam Cherry'",
        "dia_ban_pho_bien": ["Vĩnh Long", "Tiền Giang", "Bến Tre", "Bình Dương", "Đồng Nai"],
        "dac_tinh_sinh_thai": "Cây bụi thân gỗ ăn quả có khía múi như quả bí đỏ mini, chuyển từ xanh vàng sang đỏ thẩm bóng mọng, ưa đất phù sa ven sông và đất đỏ bazan.",
        "danh_sach_benh": [
            {
                "ten_benh": "Bệnh Thán thư đốm quả Cherry Surinam",
                "muc_do_nguy_hiem": "Cao",
                "tac_nhan": {"loai": "Nấm", "ten_khoa_hoc": "Colletotrichum gloeosporioides"},
                "trieu_chung_dien_hinh": [
                    "Múi quả non và quả chín xuất hiện vết chấm tròn màu nâu đỏ lõm sâu",
                    "Quả bị nhăn nheo, khô quắt đen lại dính chặt trên cành",
                    "Lá xuất hiện đốm cháy viền gợn sóng màu nâu hạt dẻ"
                ],
                "phan_biet_chan_doan_kep": "Khác với ruồi vàng đục quả (vết ruồi đục có chấm kim chích và có giòi bên trong; thán thư lõm khô đồng tâm).",
                "kiem_tra_thuc_dia": "Bổ đôi quả thấy thịt quả chai cứng thâm đen quanh vết lõm không có giòi ruồi đục.",
                "phac_do_vietgap": {
                    "canh_tac": "Tỉa thông thoáng tán cành sau thu hoạch, thu gom quả khô đen rụng dưới gốc",
                    "sinh_hoc": "Phun phòng nấm đối kháng Trichoderma kết hợp chế phẩm sinh học Chitosan nano",
                    "khuyen_cao_chuyen_gia": "Phun luân phiên giai đoạn ra hoa rộ và sau khi đậu quả non 1 tuần"
                }
            },
            {
                "ten_benh": "Bệnh Đốm lá rỉ sắt Cercospora",
                "muc_do_nguy_hiem": "Trung bình",
                "tac_nhan": {"loai": "Nấm", "ten_khoa_hoc": "Cercospora eugeniae"},
                "trieu_chung_dien_hinh": [
                    "Lá xuất hiện các chấm đốm nhỏ góc cạnh màu nâu đỏ viền vàng sáng",
                    "Vết bệnh lan rộng làm lá bánh tẻ rụng lác đác, cành trơ trụi suy kiệt sức nuôi quả",
                    "Mặt dưới vết bệnh có lớp màng nhung mỏng màu nâu đen"
                ],
                "phan_biet_chan_doan_kep": "Khác với nhện đỏ chích hút (nhện tạo mảng bụi bạc li ti; Cercospora tạo đốm tròn rõ ranh giới).",
                "kiem_tra_thuc_dia": "Soi kính lúp thấy ranh giới vết bệnh viền đỏ rõ rệt không có màng tơ nhện.",
                "phac_do_vietgap": {
                    "canh_tac": "Bón phân hữu cơ hoai mục cân đối, không bón đạm hóa học kích lộc non mùa mưa",
                    "sinh_hoc": "Phun dung dịch Nano Đồng Bạc hữu cơ nồng độ 50ppm định kỳ 15 ngày/lần",
                    "khuyen_cao_chuyen_gia": "Phun ướt đều cả 2 mặt lá vào buổi chiều mát"
                }
            }
        ]
    },
    {
        "topic": "Cay_Nhap_Khau_Kinh_Te_Cao",
        "name_vi": "Cà chua thân gỗ Tamarillo",
        "scientific_name": "Solanum betaceum 'Red Ruby'",
        "dia_ban_pho_bien": ["Đà Lạt", "Đơn Dương", "Sa Pa", "Mộc Châu"],
        "dac_tinh_sinh_thai": "Cây thân gỗ nhỏ cao 2-4m, quả hình trứng vỏ đỏ tím giàu vitamin và chất chống oxy hóa, ưa khí hậu ôn đới 15-22 độ C, đất tơi xốp giàu hữu cơ.",
        "danh_sach_benh": [
            {
                "ten_benh": "Bệnh Héo xanh vi khuẩn Tamarillo",
                "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
                "tac_nhan": {"loai": "Vi khuẩn", "ten_khoa_hoc": "Ralstonia solanacearum"},
                "trieu_chung_dien_hinh": [
                    "Cây đang xanh tốt bỗng héo rũ cụp toàn bộ lá chỉ sau 1 đêm",
                    "Lá vẫn giữ nguyên màu xanh tươi khi rũ xuống (héo xanh)",
                    "Mạch dẫn bên trong thân cành bị thâm đen và tắc nghẽn hoàn toàn"
                ],
                "phan_biet_chan_doan_kep": "Khác với héo rũ do nấm Fusarium (Fusarium lá vàng từ dưới lên từ từ; Ralstonia héo đột ngột khi lá vẫn còn xanh).",
                "kiem_tra_thuc_dia": "Cắt đoạn gốc nhúng vào ly nước trong thấy dòng mủ vi khuẩn màu trắng đục như khói thuốc trào ra liên tục.",
                "phac_do_vietgap": {
                    "canh_tac": "Nhổ bỏ cây bệnh nặng đem chôn rắc vôi bột, luân canh với cây họ hòa thảo",
                    "sinh_hoc": "Tưới phòng chế phẩm vi khuẩn đối kháng Bacillus subtilis và Pseudomonas fluorescens",
                    "khuyen_cao_chuyen_gia": "Không cuốc xới sát gốc gây đứt rễ tạo vết thương cho vi khuẩn xâm nhập"
                }
            },
            {
                "ten_benh": "Bệnh Phấn trắng lá Tamarillo",
                "muc_do_nguy_hiem": "Trung bình",
                "tac_nhan": {"loai": "Nấm", "ten_khoa_hoc": "Oidium hortensiae"},
                "trieu_chung_dien_hinh": [
                    "Mặt trên lá xuất hiện các vệt màng bột trắng mỏng như rắc vôi bột",
                    "Phiến lá bị co rúm, mép lá cong queo, chồi ngọn kém phát triển",
                    "Lá già bị úa vàng sớm và rụng trút lá dưới gốc"
                ],
                "phan_biet_chan_doan_kep": "Khác với nhện trắng (nhện gây xoăn ngọn nhưng không có bột trắng bám cọ tróc được).",
                "kiem_tra_thuc_dia": "Lấy khăn ướt lau nhẹ thấy sạch lớp bột trắng lộ ra phiến lá bị úa vàng bên dưới.",
                "phac_do_vietgap": {
                    "canh_tac": "Tỉa bỏ các cành nhánh sát gốc, tăng cường ánh sáng chiếu vào tầng tán dưới",
                    "sinh_hoc": "Phun chế phẩm Nano Lưu huỳnh sinh học kết hợp dầu khoáng SK 99EC",
                    "khuyen_cao_chuyen_gia": "Phun ướt đẫm bề mặt lá vào sáng sớm trước khi nắng gắt"
                }
            }
        ]
    },
    {
        "topic": "Cay_Nhap_Khau_Kinh_Te_Cao",
        "name_vi": "Hạt dẻ cười Pistachio Đắk Lắk",
        "scientific_name": "Pistacia vera 'Kerman'",
        "dia_ban_pho_bien": ["Đắk Lắk", "Gia Lai", "Ninh Thuận"],
        "dac_tinh_sinh_thai": "Cây thân gỗ rụng lá ưa khô hạn và đất đồi sỏi thoát nước tốt, quả hạt có vỏ cứng nứt đôi khi chín, nhân bùi béo giá trị kinh tế rất cao.",
        "danh_sach_benh": [
            {
                "ten_benh": "Bệnh Đốm lá thán thư Panicle and Shoot Blight",
                "muc_do_nguy_hiem": "Cao",
                "tac_nhan": {"loai": "Nấm", "ten_khoa_hoc": "Botryosphaeria dothidea"},
                "trieu_chung_dien_hinh": [
                    "Chùm hoa và chồi non bị khô đen cháy rụi, rụng sớm hàng loạt",
                    "Trên vỏ quả xuất hiện các chấm đốm nhỏ màu đen liên kết thành mảng lớn làm quả bị điếc hạt",
                    "Cành non bị loét thâm đen làm khô chết ngọn cành"
                ],
                "phan_biet_chan_doan_kep": "Khác với khô cành sinh lý do nắng hạn (vết cháy loang không có viền; nấm bệnh có vết lõm rõ và hạt đen li ti).",
                "kiem_tra_thuc_dia": "Bẻ cành khô thấy lõi gỗ chuyển màu nâu đen loang lổ.",
                "phac_do_vietgap": {
                    "canh_tac": "Cắt tỉa cành chết vào mùa khô, quét vôi thân cây khử trùng ổ nấm",
                    "sinh_hoc": "Phun phòng nấm đối kháng Chaetomium kết hợp chế phẩm nano đồng sinh học",
                    "khuyen_cao_chuyen_gia": "Phun 2 lần: giai đoạn chồi hoa vừa nhú và sau khi đậu quả 2 tuần"
                }
            },
            {
                "ten_benh": "Bệnh Thối rễ Verticillium Wilt",
                "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
                "tac_nhan": {"loai": "Nấm", "ten_khoa_hoc": "Verticillium dahliae"},
                "trieu_chung_dien_hinh": [
                    "Lá trên một bên cành bị héo rũ, mép lá cháy khô cuốn cong rồi rụng",
                    "Mạch dẫn bên trong cành bị nhiễm bệnh hóa nâu đen thành vệt sọc dài",
                    "Toàn cây suy kiệt dần qua các năm và chết đứng"
                ],
                "phan_biet_chan_doan_kep": "Khác với Phytophthora (Phytophthora thối cổ rễ ướt át; Verticillium chỉ tắc mạch dẫn khô ráo bên trong).",
                "kiem_tra_thuc_dia": "Vạt xéo lớp vỏ cành bị héo thấy vệt nâu sẫm chạy dọc theo thớ gỗ mạch dẫn.",
                "phac_do_vietgap": {
                    "canh_tac": "Trồng trên gốc ghép kháng bệnh Verticillium (Pistacia integerrima)",
                    "sinh_hoc": "Tưới gốc định kỳ nấm đối kháng Trichoderma harzianum để tiêu diệt hạch nấm trong đất",
                    "khuyen_cao_chuyen_gia": "Không trồng xen với các cây họ cà (ớt, cà chua, khoai tây) vốn là ký chủ của Verticillium"
                }
            }
        ]
    },
    {
        "topic": "Cay_Nhap_Khau_Kinh_Te_Cao",
        "name_vi": "Mắc ca Tây Nguyên Macadamia",
        "scientific_name": "Macadamia integrifolia 'OC'",
        "dia_ban_pho_bien": ["Đắk Lắk", "Lâm Đồng", "Đắk Nông", "Gia Lai", "Điện Biên"],
        "dac_tinh_sinh_thai": "Cây thân gỗ lớn, quả hạch có nhân thơm ngon mệnh danh là nữ hoàng hạt khô, thích hợp đất đỏ bazan tầng dày, thoát nước tốt, pH 5.5 - 6.5.",
        "danh_sach_benh": [
            {
                "ten_benh": "Bệnh Thối hoa Mắc Ca (Phytophthora Blight)",
                "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
                "tac_nhan": {"loai": "Nấm", "ten_khoa_hoc": "Phytophthora capsici"},
                "trieu_chung_dien_hinh": [
                    "Chuỗi hoa dài đang nở xuất hiện các vết úng nước màu nâu xám",
                    "Hoa bị thối nhũn, chuyển sang màu đen và rụng trút hàng loạt chỉ trong 2-3 ngày mưa ẩm",
                    "Chùm quả non mới đậu bị thâm đen teo tóp không thể lớn"
                ],
                "phan_biet_chan_doan_kep": "Khác với bọ xít muỗi chích hoa (bọ xít chích tạo chấm đen nhỏ lõm; Phytophthora làm thối nhũn cả chuỗi hoa ướt át).",
                "kiem_tra_thuc_dia": "Cầm chuỗi hoa bóp nhẹ thấy nước nhầy nhớt chảy ra và có mùi thối chua nồng.",
                "phac_do_vietgap": {
                    "canh_tac": "Tỉa thông thoáng cành tán bên trong, làm cỏ sạch dưới tán để giảm độ ẩm",
                    "sinh_hoc": "Phun phòng chế phẩm Phosphonate sinh học kết hợp nấm đối kháng Trichoderma",
                    "khuyen_cao_chuyen_gia": "Phun phòng ngừa ngay trước khi hoa nở rộ và sau cơn mưa đầu mùa"
                }
            },
            {
                "ten_benh": "Bệnh Đốm vỏ quả Thán thư Macadamia",
                "muc_do_nguy_hiem": "Nặng",
                "tac_nhan": {"loai": "Nấm", "ten_khoa_hoc": "Colletotrichum acutatum"},
                "trieu_chung_dien_hinh": [
                    "Vỏ quả xanh xuất hiện các đốm nâu đen hình tròn hoặc bầu dục lõm sâu",
                    "Vết bệnh ăn sâu qua lớp vỏ quả thịt vào tận lớp vỏ gỗ cứng bên trong",
                    "Làm nhân hạt bên trong bị teo tóp, biến tính và hôi dầu không ăn được"
                ],
                "phan_biet_chan_doan_kep": "Khác với vết nứt vỏ sinh lý do hạn hán (vết nứt sạch không có màng tơ nấm; thán thư có ổ nấm màu hồng cam khi ẩm).",
                "kiem_tra_thuc_dia": "Quan sát vết lõm lúc sương sớm thấy các giọt dịch màu cam hồng tiết ra ở tâm vết bệnh.",
                "phac_do_vietgap": {
                    "canh_tac": "Thu gom quả rụng và quả khô dính trên cây đem đốt tiêu hủy sau vụ thu hoạch",
                    "sinh_hoc": "Phun chế phẩm Nano Bạc Đồng kết hợp dịch chiết tỏi ớt xua đuổi côn trùng truyền nấm",
                    "khuyen_cao_chuyen_gia": "Phun luân phiên các hoạt chất sinh học định kỳ 20 ngày/lần trong mùa mưa"
                }
            }
        ]
    },
    {
        "topic": "Rau_Cu_Gia_Vi_Va_Nam",
        "name_vi": "Nấm mối đen công nghệ cao",
        "scientific_name": "Oudemansiella radicata 'Black Termite Mushroom'",
        "dia_ban_pho_bien": ["Củ Chi", "Bình Dương", "Đồng Nai", "Vĩnh Long", "Cần Thơ"],
        "dac_tinh_sinh_thai": "Nấm ăn quý giá giòn ngọt vị như nấm mối tự nhiên, trồng phòng lạnh 24-26 độ C, độ ẩm 85-90%, cơ chất mùn cưa cao su + cám bắp tiệt trùng.",
        "danh_sach_benh": [
            {
                "ten_benh": "Bệnh Mốc xanh Trichoderma cạnh tranh cơ chất",
                "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
                "tac_nhan": {"loai": "Nấm cạnh tranh", "ten_khoa_hoc": "Trichoderma harzianum / Trichoderma viride"},
                "trieu_chung_dien_hinh": [
                    "Bề mặt bịch phôi xuất hiện các mảng tơ nấm màu xanh lục sẫm lan rộng nhanh chóng",
                    "Tiết ra độc tố ức chế làm sợi tơ nấm mối đen bị chết tiêu biến",
                    "Bịch phôi bị chua, không thể hình thành quả thể nấm"
                ],
                "phan_biet_chan_doan_kep": "Khác với tơ nấm mối đen (tơ nấm mối màu trắng ngà mịn màng; Trichoderma có màu xanh lá đậm như bột trà xanh).",
                "kiem_tra_thuc_dia": "Nhìn thấy mảng màu xanh lục lan rộng trên miệng bịch phôi và ngửi thấy mùi mốc chua nồng.",
                "phac_do_vietgap": {
                    "canh_tac": "Tiệt trùng phôi ở nhiệt độ 121 độ C trong 2-3 giờ, cách ly ngay bịch nhiễm ra khỏi phòng nuôi",
                    "sinh_hoc": "Xông phòng nuôi bằng tinh dầu quế hoặc sả chanh tự nhiên khử trùng không khí",
                    "khuyen_cao_chuyen_gia": "Đeo găng tay và sát trùng cồn 70 độ khi thao tác mở nút bông và tưới ẩm"
                }
            },
            {
                "ten_benh": "Bệnh Thối nhũn quả thể vi khuẩn (Bacterial Blight)",
                "muc_do_nguy_hiem": "Nặng",
                "tac_nhan": {"loai": "Vi khuẩn", "ten_khoa_hoc": "Pseudomonas tolaasii"},
                "trieu_chung_dien_hinh": [
                    "Mũ nấm xuất hiện các vệt ướt sũng nước màu nâu vàng nhớt nhầy",
                    "Tai nấm bị mềm nhũn, biến dạng và chảy nước có mùi hôi tanh",
                    "Bệnh lây lan rất nhanh theo các hạt sương nước bắn khi tưới phun sương"
                ],
                "phan_biet_chan_doan_kep": "Khác với nấm già rục (nấm già teo khô; vi khuẩn làm nhũn ướt nhầy nhụa hôi tanh).",
                "kiem_tra_thuc_dia": "Sờ tay vào mũ nấm thấy nhớt trơn tuột và có mùi tanh khó chịu.",
                "phac_do_vietgap": {
                    "canh_tac": "Giảm độ ẩm phòng nuôi xuống 80%, bật quạt lưu thông không khí làm ráo bề mặt mũ nấm",
                    "sinh_hoc": "Phun sương nước vôi trong pha loãng (pH 8.5) hoặc dung dịch nano bạc 10ppm khử khuẩn",
                    "khuyen_cao_chuyen_gia": "Không tưới nước trực tiếp lên tai nấm khi nhiệt độ phòng vượt quá 28 độ C"
                }
            }
        ]
    },
    {
        "topic": "Rau_Cu_Gia_Vi_Va_Nam",
        "name_vi": "Nấm hầu thủ Đà Lạt Lion's Mane",
        "scientific_name": "Hericium erinaceus 'Lion Mane'",
        "dia_ban_pho_bien": ["Đà Lạt", "Đức Trọng", "Bảo Lộc"],
        "dac_tinh_sinh_thai": "Nấm dược liệu quý hình đầu khỉ/bờm sư tử hỗ trợ thần kinh và trí nhớ, ưa nhiệt độ mát mẻ 16-22 độ C, giá thể mùn cưa gỗ mềm phối trộn bột cám gạo.",
        "danh_sach_benh": [
            {
                "ten_benh": "Bệnh Mốc cam Neurospora (Orange Bread Mold)",
                "muc_do_nguy_hiem": "Nặng",
                "tac_nhan": {"loai": "Nấm tạp", "ten_khoa_hoc": "Neurospora sitophila"},
                "trieu_chung_dien_hinh": [
                    "Mảng tơ nấm xốp màu cam phấn tươi phát triển thần tốc bao trùm nút bông và cổ chai",
                    "Phóng thích hàng triệu bào tử phấn màu cam bay lơ lửng trong không khí",
                    "Làm chết nghẹt sợi nấm hầu thủ bên trong phôi"
                ],
                "phan_biet_chan_doan_kep": "Khác với nấm mốc vàng (Neurospora có màu cam sáng rực rỡ và phát triển nhanh gấp 5 lần nấm thường).",
                "kiem_tra_thuc_dia": "Chạm nhẹ thấy lớp bột phấn màu cam dính đầy tay và bay bụi mù mịt.",
                "phac_do_vietgap": {
                    "canh_tac": "Đưa ngay bịch nhiễm ra khỏi nhà nuôi vào bao nilon kín đem hấp hủy nhiệt độ cao",
                    "sinh_hoc": "Lau rửa sàn và kệ nuôi bằng cồn hoặc dung dịch nano bạc sát khuẩn",
                    "khuyen_cao_chuyen_gia": "Tăng cường kiểm soát lọc bụi không khí cấp vào phòng nuôi cấy"
                }
            },
            {
                "ten_benh": "Bệnh Khô cháy tua gai nấm Hầu Thủ",
                "muc_do_nguy_hiem": "Trung bình",
                "tac_nhan": {"loai": "Nấm hoại sinh & Độ ẩm thấp", "ten_khoa_hoc": "Verticillium malthousei"},
                "trieu_chung_dien_hinh": [
                    "Các sợi tua gai rủ dài của nấm bị thâm vàng rồi khô quắt lại",
                    "Quả thể nấm chuyển sang màu vàng xám xỉn, cứng đơ và ngừng phát triển",
                    "Mất hoàn toàn giá trị thương phẩm xuất khẩu"
                ],
                "phan_biet_chan_doan_kep": "Khác với nấm chín già (nấm chín ngả vàng kem tự nhiên; bệnh làm tua gai khô cháy gãy vụn).",
                "kiem_tra_thuc_dia": "Sờ vào tua gai thấy giòn khô ráp như rơm vụn.",
                "phac_do_vietgap": {
                    "canh_tac": "Duy trì độ ẩm không khí ổn định 85-90% bằng máy tạo ẩm siêu âm hạt mịn",
                    "sinh_hoc": "Phun sương nước cất pha nano bạc nồng độ cực thấp 5ppm khử khuẩn không khí",
                    "khuyen_cao_chuyen_gia": "Tránh gió lùa trực tiếp từ quạt hút vào bề mặt quả thể nấm"
                }
            }
        ]
    },
    {
        "topic": "Cay_Lam_Nghiep_Duoc_Lieu_Quy",
        "name_vi": "Đông trùng hạ thảo nhân tạo Cordyceps",
        "scientific_name": "Cordyceps militaris 'Thai Strain'",
        "dia_ban_pho_bien": ["Đà Lạt", "TP.HCM", "Cần Thơ", "Vĩnh Long", "Hà Nội"],
        "dac_tinh_sinh_thai": "Nấm dược liệu quý cấy trên cơ chất nhộng tằm hoặc gạo lứt + nước dừa, nuôi trong phòng vô trùng nhiệt độ 18-20 độ C, ánh sáng xanh kích hoạt tạo quả thể cam.",
        "danh_sach_benh": [
            {
                "ten_benh": "Bệnh Thoái hóa giống đầu bạc (Sectoring & Degeneration)",
                "muc_do_nguy_hiem": "Nặng",
                "tac_nhan": {"loai": "Thoái hóa di truyền & Vi rút nấm", "ten_khoa_hoc": "Mycovirus & Somaclonal variation"},
                "trieu_chung_dien_hinh": [
                    "Ngọn quả thể nấm nhú lên bị bạc trắng, mất hoàn toàn sắc tố cam carotenoid",
                    "Quả thể ngắn còi cọc, đầu chóp bị tù không hình thành bao tử nang",
                    "Hàm lượng dược chất Cordycepin và Adenosine sụt giảm nghiêm trọng > 80%"
                ],
                "phan_biet_chan_doan_kep": "Khác với nấm thiếu ánh sáng (thiếu sáng toàn thân nấm nhợt nhạt; thoái hóa thì chỉ có chùm nấm đầu bạc đột biến).",
                "kiem_tra_thuc_dia": "Quan sát đầu chóp cây nấm thấy màu trắng bệch như hạt gạo đối lập với gốc màu cam.",
                "phac_do_vietgap": {
                    "canh_tac": "Phục tráng giống định kỳ từ bào tử đơn bội, không nhân giống truyền đời quá F3",
                    "sinh_hoc": "Bổ sung dịch chiết tảo xoắn Spirulina và khoáng chất hữu cơ vào môi trường dinh dưỡng",
                    "khuyen_cao_chuyen_gia": "Bảo tồn nguồn giống gốc trong nitơ lỏng -196 độ C"
                }
            },
            {
                "ten_benh": "Bệnh Mốc đen Aspergillus cạnh tranh hộp nuôi",
                "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
                "tac_nhan": {"loai": "Nấm mốc tạp", "ten_khoa_hoc": "Aspergillus niger"},
                "trieu_chung_dien_hinh": [
                    "Lớp cơ chất gạo lứt nhộng tằm xuất hiện các đốm bột màu đen kịt như bột than",
                    "Tỏa mùi hôi mốc, làm sợi nấm đông trùng bị thối đen nhũn rữa",
                    "Hộp nuôi nấm bị hỏng hoàn toàn phải loại bỏ"
                ],
                "phan_biet_chan_doan_kep": "Khác với nấm đông trùng già chuyển nâu (chuyển nâu tự nhiên không có lớp bụi than đen rơi rớt).",
                "kiem_tra_thuc_dia": "Lắc nhẹ hộp nuôi thấy bụi bào tử đen bám lên thành lọ thủy tinh.",
                "phac_do_vietgap": {
                    "canh_tac": "Hấp tiệt trùng môi trường ở 121 độ C trong 45 phút, thao tác cấy giống trong tủ cấy Clean Bench chuẩn vô trùng",
                    "sinh_hoc": "Khử trùng buồng cấy bằng đèn cực tím UV-C 30 phút trước khi thao tác",
                    "khuyen_cao_chuyen_gia": "Kiểm tra độ kín của màng thở trên nắp hộp nuôi nấm"
                }
            }
        ]
    }
]

def get_expansion_crops():
    return EXPANSION_CROPS
