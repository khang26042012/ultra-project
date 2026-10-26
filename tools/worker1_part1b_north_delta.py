# -*- coding: utf-8 -*-
"""
Worker 1 - Part 1b: Miền Bắc & Đồng Bằng Sông Hồng tiếp theo (Crops 11 to 25)
"""

def get_part1b_crops():
    return [
        {
            "id": "w1_011",
            "topic": "Cay_Luong_Thuc_Va_Hoa_Mau",
            "name_vi": "Củ từ nếp Tiên Lãng Hải Phòng",
            "scientific_name": "Dioscorea esculenta (Lour.) Burkill cv. Tien Lang",
            "dia_ban_pho_bien": ["Tiên Lãng", "Vĩnh Bảo", "Hải Phòng", "Thái Bình"],
            "dac_tinh_sinh_thai": "Cây dây leo ưa đất cát pha phù sa bãi bồi ven sông Văn Úc, tơi xốp, tầng canh tác sâu > 50cm, pH 5.5 - 6.5, thời gian sinh trưởng 8-9 tháng, củ mọc chùm dưới gốc nhiều tinh bột dẻo bùi.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Thán thư cháy dây khoai từ",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Colletotrichum gloeosporioides f. sp. dioscoreae"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết bệnh trên lá là những đốm tròn màu nâu thẫm viền vàng, sau lan rộng thành mảng cháy khô",
                        "Trên thân dây leo xuất hiện các vệt loét dài hình thoi màu nâu đen làm teo thắt thân dây",
                        "Dây khoai từ bị rụng lá hàng loạt từ gốc lên ngọn, ngọn dây teo tóp ngừng leo",
                        "Củ phát triển còi cọc, vỏ củ bị các vết nứt sần thâm đen"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Cháy nắng sinh lý: Cháy nắng phiến lá bạc trắng khô phẳng lì; Thán thư vết thâm tròn lõm sâu có tâm xám tro viền tía đỏ.",
                    "kiem_tra_thuc_dia": "Vò nhẹ đoạn dây leo thâm đen thấy gãy giòn rụm, tách vỏ thấy mô mạch dẫn bên trong thâm đen khô xác.",
                    "phac_do_vietgap": {
                        "canh_tac": "Làm giàn leo thông thoáng đón gió nắng, tỉa bớt nhánh phụ rậm rạp sát mặt luống.",
                        "sinh_hoc": "Phun dịch chiết tỏi ớt gừng kết hợp Chitosan nano kích kháng định kỳ 10 ngày/lần.",
                        "khuyen_cao_chuyen_gia": "Phun trừ bằng Azoxystrobin + Difenoconazole hoặc Mancozeb khi mưa phùn kéo dài."
                    }
                },
                {
                    "ten_benh": "Bệnh Tuyến trùng u sưng thối củ khoai từ",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Tuyến trùng",
                        "ten_khoa_hoc": "Meloidogyne incognita"
                    },
                    "trieu_chung_dien_hinh": [
                        "Bề mặt củ từ xuất hiện nhiều nốt u sần méo mó gồ ghề như mụn cơm",
                        "Các nốt u làm nứt toác vỏ củ tạo cửa ngõ cho vi khuẩn hoại sinh xâm nhập gây thối nhũn",
                        "Cây sinh trưởng kém, lá vàng úa cằn cỗi dù được bón đủ phân",
                        "Thịt củ bên trong bị xơ cứng, nhiều chấm đen sượng chát"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Sẹo cơ giới do sỏi đá cọ xát: Sẹo cơ giới vết phẳng liền sẹo mịn màng; Tuyến trùng nốt sần u cục sần sùi biến dạng toàn bộ hình dáng củ.",
                    "kiem_tra_thuc_dia": "Cắt lát củ qua nốt sần dùng kính lúp soi thấy các tế bào khổng lồ và con tuyến trùng cái hình quả lê màu trắng sữa nằm ẩn sâu bên trong.",
                    "phac_do_vietgap": {
                        "canh_tac": "Luân canh nước với lúa gạo 1-2 vụ, phơi ải đất kỹ và bón vôi bột 100kg/sào.",
                        "sinh_hoc": "Tưới chế phẩm nấm ký sinh tuyến trùng Paecilomyces lilacinus kết hợp bã bánh dầu neem.",
                        "khuyen_cao_chuyen_gia": "Xử lý đất trước khi trồng bằng hoạt chất trừ tuyến trùng sinh học Abamectin hoặc Chitosan."
                    }
                }
            ]
        },
        {
            "id": "w1_012",
            "topic": "Rau_Cu_Gia_Vi_Va_Nam",
            "name_vi": "Rau rút / Rau nhút Thường Tín",
            "scientific_name": "Neptunia oleracea Lour.",
            "dia_ban_pho_bien": ["Thường Tín", "Phú Xuyên", "Hà Nội", "Hà Nam", "Hải Dương"],
            "dac_tinh_sinh_thai": "Cây rau thủy sinh nổi trên mặt nước ao hồ ruộng trũng, ưa khí hậu nóng ẩm 25-35 độ C, nước sạch giàu hữu cơ bùn đáy phù sa, có lớp phao trắng xốp bao quanh đốt thân giúp cây nổi bồng bềnh.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Đốm xám mốc bấc thân phao rau rút",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Rhizoctonia solani"
                    },
                    "trieu_chung_dien_hinh": [
                        "Lớp phao trắng xốp bao quanh đốt thân bị thâm đen, úng nước và teo tóp rách nát",
                        "Thân rau rút bị thối mục gãy ngang làm đọt non chìm xuống đáy bùn chết ngạt",
                        "Lá chét kép bị úa vàng rụng sớm, cây cằn cỗi không đâm được rễ tơ ở các mắt đốt",
                        "Trên bề mặt thân cây xuất hiện các sợi tơ nấm màu nâu tro mỏng manh bám dính"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Rầy bọ trĩ chích hút: Côn trùng chích làm chồi xoăn queo rụt lại nhưng phao xốp vẫn lành lặn; Nấm thối bấc làm phao xốp thối nhũn xơ xác mục nát hoàn toàn.",
                    "kiem_tra_thuc_dia": "Lấy tay bóp nhẹ vào lớp phao xốp thấy nhũn nước xẹp lép phì ra nước bùn hôi mốc.",
                    "phac_do_vietgap": {
                        "canh_tac": "Tháo cạn nước vệ sinh bùn đáy ao bằng vôi bột trước vụ trồng, giữ mực nước sạch lưu thông nhẹ nhàng.",
                        "sinh_hoc": "Tưới phun chế phẩm vi sinh đối kháng Bacillus subtilis phân tán đều trên mặt nước ao.",
                        "khuyen_cao_chuyen_gia": "Phun phòng hoạt chất sinh học Validamycin A hoặc Booc-đô loãng khi chớm thấy phao xốp chuyển màu thâm."
                    }
                },
                {
                    "ten_benh": "Bệnh Thối nhũn vi khuẩn rau rút nước ngập",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Vi khuẩn",
                        "ten_khoa_hoc": "Erwinia carotovora subsp. carotovora"
                    },
                    "trieu_chung_dien_hinh": [
                        "Đọt non và chồi nách bị sũng nước thối mềm rục ra trong vòng 24-48 giờ",
                        "Mô thân bị phân hủy thành chất nhầy nhớt bốc mùi hôi thối nồng nặc",
                        "Các chùm lá chét bị rữa nát nổi lềnh bềnh trên mặt nước tạo vệt dịch loang nhanh",
                        "Cả đám rau rút bị lụi tàn hàng mảng lớn chỉ sau một đêm mưa rào dông bão"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Cháy lá do ngộ độc phân đạm: Ngộ độc đạm lá cháy viền khô giòn; Thối vi khuẩn mô lá thân mềm nhũn rục nước và bốc mùi tanh khắm nồng nặc.",
                    "kiem_tra_thuc_dia": "Vớt đoạn đọt non lên tay thấy nhầy nhớt trơn tuột, ngửi thấy mùi thối khắm vi khuẩn xộc thẳng vào mũi.",
                    "phac_do_vietgap": {
                        "canh_tac": "Vớt bỏ tiêu hủy ngay mảng rau bệnh xa nguồn nước, giảm lượng phân đạm ure thay bằng phân vi sinh hữu cơ.",
                        "sinh_hoc": "Sử dụng chế phẩm Nano Bạc Đồng 500ppm phun xịt mặt nước để dập tắt nguồn vi khuẩn lây lan.",
                        "khuyen_cao_chuyen_gia": "Xử lý nguồn nước bằng Kasugamycin hoặc thuốc trừ khuẩn gốc đồng hữu cơ an toàn cho thủy sinh vật."
                    }
                }
            ]
        },
        {
            "id": "w1_013",
            "topic": "Cay_Lam_Nghiep_Duoc_Lieu_Quy",
            "name_vi": "Sen Tây Hồ Hà Nội",
            "scientific_name": "Nelumbo nucifera Gaertn. cv. Tay Ho",
            "dia_ban_pho_bien": ["Tây Hồ", "Mê Linh", "Hà Nội", "Hà Nam", "Hưng Yên"],
            "dac_tinh_sinh_thai": "Cây sen bách diệp hồng đặc sản ướp trà, sinh trưởng trong bùn đầm lầy hồ nước ngọt giàu khoáng chất mùn tự nhiên sâu 0.5 - 1.2m, nhiệt độ thích hợp 25-35 độ C, nắng nhiều > 8 giờ/ngày.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Thán thư đốm mắt chim lá sen Tây Hồ",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Colletotrichum nymphaeae"
                    },
                    "trieu_chung_dien_hinh": [
                        "Phiến lá sen xuất hiện các chấm nâu tròn nhỏ, sau lan rộng thành đốm mắt chim viền đỏ tím",
                        "Giữa tâm vết bệnh bị khô giòn nứt toác thủng lỗ chỗ làm phiến lá rách nát",
                        "Cánh hoa sen bị thâm đốm làm hoa thối đen không nở được, mất hoàn toàn hương thơm ướp trà",
                        "Gương sen non bị chai sượng hạt lép đen"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Bọ trĩ cào rách lá sen: Bọ trĩ làm gân lá gồ ghề quăn mép bạc màu sờ ram ráp; Thán thư tạo các đốm thủng tròn đồng tâm rõ ràng có viền tía đỏ.",
                    "kiem_tra_thuc_dia": "Nhìn mặt lá sen nghiêng dưới ánh sáng thấy tâm vết đốm bị hoại tử thủng lỗ tròn đường kính 3-8mm như bị tàn thuốc lá châm.",
                    "phac_do_vietgap": {
                        "canh_tac": "Vớt bỏ lá già lá bệnh trên mặt đầm, dọn sạch rong rêu đáy hồ tạo lưu thông ánh sáng.",
                        "sinh_hoc": "Phun chế phẩm nấm đối kháng Chaetomium kết hợp dịch chiết vỏ tôm Chitosan nano an toàn với cá cảnh hồ sen.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bằng hoạt chất Azoxystrobin hoặc Difenoconazole nồng độ an toàn trước vụ trổ bông rộ."
                    }
                },
                {
                    "ten_benh": "Bệnh Thối ngó củ sen nấm Fusarium",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Fusarium oxysporum f. sp. nelumbonis"
                    },
                    "trieu_chung_dien_hinh": [
                        "Lá sen non mới vươn lên mặt nước bị héo rũ, mép lá cuộn lại ngả màu vàng úa",
                        "Ngó sen và đốt củ sen dưới bùn bị thối đen thâm sẫm, mô xốp ngó bị phân hủy rỗng ruột",
                        "Cắt ngang củ sen thấy các ống dẫn khí bên trong chứa đầy dịch nhầy màu nâu đen bốc mùi bùn thối",
                        "Đầm sen bị lụi tàn từng chòm lớn, không đâm được ngó non mới"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Hiện tượng ngộ độc khí bùn (H2S, CH4): Ngộ độc khí rễ củ thâm đen toàn bộ bề mặt nhưng rửa sạch mùi bùn vẫn rắn chắc; Bệnh nấm Fusarium thịt củ bên trong thối đen phân hủy rữa nát có mạch thâm tím sẫm.",
                    "kiem_tra_thuc_dia": "Nhổ ngó sen dưới bùn lên bẻ đôi thấy ống khí bị bít tắc dịch nâu sẫm, bóp vào củ thấy mềm rỗng ruột xì bọt khí.",
                    "phac_do_vietgap": {
                        "canh_tac": "Rút cạn nước phơi đáy đầm sen vụ đông, rải vôi tả 150kg/sào để tiêu diệt mầm nấm ngủ nghỉ.",
                        "sinh_hoc": "Bón lót phân vi sinh kết hợp chủng nấm đối kháng Trichoderma chuyên dùng cho cây thủy sinh.",
                        "khuyen_cao_chuyen_gia": "Xử lý giống củ sen sạch bệnh trước khi cấy bằng dung dịch Nano Bạc Đồng 500ppm ngâm trong 30 phút."
                    }
                }
            ]
        },
        {
            "id": "w1_014",
            "topic": "Cay_Lam_Nghiep_Duoc_Lieu_Quy",
            "name_vi": "Hoa nhài Quảng Bá Hà Nội",
            "scientific_name": "Jasminum sambac (L.) Aiton cv. Quang Ba",
            "dia_ban_pho_bien": ["Tây Hồ", "Bắc Từ Liêm", "Hà Nội", "Hà Nam", "Hải Dương"],
            "dac_tinh_sinh_thai": "Cây bụi hoa đặc sản ướp trà truyền thống Thăng Long, ưa đất thịt pha cát tơi xốp giàu mùn, pH 6.0 - 6.5, ánh sáng dồi dào, cần tỉa cành đốn gốc hàng năm sau mỗi đợt hoa nở rộ mùa hè thu.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Đốm mắt cua lá hoa nhài (Bệnh đốm Cercospora)",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Cercospora jasminicola"
                    },
                    "trieu_chung_dien_hinh": [
                        "Phiến lá xuất hiện nhiều đốm tròn nhỏ li ti màu nâu đỏ gờ gồ ghề như mắt cua",
                        "Các đốm bệnh phát triển tâm hóa xám trắng viền nâu thẫm, lá bị úa vàng rụng sớm trơ trụi cành",
                        "Nụ hoa nhài bị thâm đen đầu cánh, hoa nở xòe méo mó hoặc không nở được làm mất hương thơm",
                        "Cành nhài bị suy kiệt giảm sản lượng búp hoa nghiêm trọng"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Cháy lá sinh lý: Cháy lá sinh lý viền lá cháy sém khô đồng đều mép ngoài; Bệnh mắt cua là các chấm tròn đồng tâm sắc nét rải rác khắp bề mặt phiến lá.",
                    "kiem_tra_thuc_dia": "Dùng kính lúp soi đốm lá thấy các bào tử nấm màu đen mọc tua tủa như gai nhím li ti giữa tâm đốm xám trắng.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt tỉa cành già thông thoáng gốc sau mỗi lứa hái hoa, gom sạch lá rụng đem chôn.",
                        "sinh_hoc": "Phun phòng nấm đối kháng Bacillus subtilis kết hợp tinh dầu quế sinh học.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bằng hoạt chất Difenoconazole, Chlorothalonil hoặc Booc-đô 1% giai đoạn vừa đốn cành ra lộc non."
                    }
                },
                {
                    "ten_benh": "Bệnh Thối gốc lở cổ rễ mốc trắng hoa nhài",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Sclerotium rolfsii (Athelia rolfsii)"
                    },
                    "trieu_chung_dien_hinh": [
                        "Phần vỏ thân sát mặt đất bị thâm đen, úng nước mục nát vỏ",
                        "Quanh gốc thân và mặt đất phủ một lớp mạng tơ nấm màu trắng muốt như bông gòn",
                        "Trên màng tơ xuất hiện nhiều hạch nấm nhỏ tròn như hạt cải bắp màu nâu đỏ cánh gián",
                        "Cây hoa nhài héo rũ xanh rất nhanh, lá vẫn còn xanh nhưng rũ gập xuống và chết đứng"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Thối rễ do Phytophthora: Phytophthora không sinh mạng tơ nấm trắng muốt lộ thiên và không có hạt hạch nấm tròn màu cánh gián như hạt cải ở gốc thân.",
                    "kiem_tra_thuc_dia": "Gạt lớp đất mặt quanh gốc nhài thấy mạng tơ nấm trắng đan kín và vô số hạt hạch nấm tròn cứng màu nâu óng bám chặt vào vỏ thân.",
                    "phac_do_vietgap": {
                        "canh_tac": "Lên luống cao, không để cỏ rác đọng ẩm ướt ở cổ gốc; nhổ bỏ cây bệnh nặng và xúc cả bầu đất đem tiêu hủy.",
                        "sinh_hoc": "Rải chế phẩm nấm đối kháng Trichoderma harzianum quanh gốc để tiêu diệt hạch nấm trong đất.",
                        "khuyen_cao_chuyen_gia": "Tưới gốc bằng Validamycin A, Hexaconazole hoặc Flutolanil khi chớm thấy sợi tơ nấm trắng xuất hiện."
                    }
                }
            ]
        },
        {
            "id": "w1_015",
            "topic": "Cay_Lam_Nghiep_Duoc_Lieu_Quy",
            "name_vi": "Mộc hương ta Ba Vì",
            "scientific_name": "Osmanthus fragrans Lour. var. aurantiacus",
            "dia_ban_pho_bien": ["Ba Vì", "Sơn Tây", "Hà Nội", "Vĩnh Phúc", "Phú Thọ"],
            "dac_tinh_sinh_thai": "Cây gỗ nhỏ thân bụi đặc hữu quý giá, ưa đất đồi Feralit đỏ vàng thoát nước tốt, tầng đất dày, pH 5.5 - 6.5, ưa khí hậu mát mẻ vùng đồi núi thấp, hoa thơm ngát mùa thu đông rất giá trị kinh tế.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Đốm than xám lá mộc hương",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Phyllosticta osmanthicola"
                    },
                    "trieu_chung_dien_hinh": [
                        "Phiến lá xuất hiện những đốm tròn hoặc hình bầu dục méo mó màu xám tro viền nâu đen",
                        "Trên bề mặt vết đốm có các chấm đen li ti là các quả cành chứa bào tử nấm",
                        "Lá bị khô cháy từng mảng lớn ở mép và chóp lá, lá xỉn màu giảm vẻ đẹp phong thủy",
                        "Cây quang hợp kém, tán còi cọc đâm ít chồi hoa non"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Cháy chóp lá do thiếu Kali: Thiếu kali chóp lá già khô vàng đều màu từ mép viền ngoài vào; Bệnh đốm than tạo vết xám tro có chấm đen quả cành li ti rải rác.",
                    "kiem_tra_thuc_dia": "Dùng ngón tay sờ bề mặt vết đốm thấy nhẵn phẳng khô giòn, gõ nhẹ thấy màng lá thủng giòn rụm.",
                    "phac_do_vietgap": {
                        "canh_tac": "Tỉa bỏ lá bệnh đem tiêu hủy, kê chậu cao hoặc trồng nơi thoáng gió tránh đọng sương lâu trên lá.",
                        "sinh_hoc": "Phun dịch chiết nano Chitosan kết hợp dầu sả chanh sinh học xua đuổi mầm bệnh.",
                        "khuyen_cao_chuyen_gia": "Phun luân phiên Mancozeb, Difenoconazole hoặc Antracol 70WP định kỳ 20 ngày trong mùa mưa phùn."
                    }
                },
                {
                    "ten_benh": "Bệnh Khô cành nứt vỏ xì gôm mộc hương",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Botryosphaeria dothidea"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vỏ cành và thân cây xuất hiện các vết nứt dọc rỉ ra chất gôm nhựa màu nâu dẻo quánh",
                        "Mô vỏ dưới vết nứt chuyển màu nâu thẫm, khô lại và tróc vảy làm tắc nghẽn dòng nhựa",
                        "Cành phía trên vết nứt bị héo lá đột ngột, lá khô dính chặt trên cành không rụng",
                        "Cành chết khô giòn dễ gãy trong mùa gió rét"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Mọt đục cành cắn phá: Mọt đục cành có lỗ nhỏ tròn như đầu tăm đùn bột gỗ ra ngoài; Bệnh nấm nứt thân xì gôm vỏ nứt toác theo chiều dọc và ứa giọt nhựa quánh dẻo không có lỗ đục.",
                    "kiem_tra_thuc_dia": "Dùng móng tay cạo nhẹ lớp nhựa dẻo thấy vỏ gỗ bên dưới bị chai thâm đen thành rãnh nứt dọc.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt bỏ cành khô dưới vết nứt 10cm đem đốt, khử trùng vết cắt bằng cồn hoặc keo liền sẹo.",
                        "sinh_hoc": "Quét gốc bằng dung dịch Bordeaux 2% trộn nấm đối kháng Chaetomium bảo vệ thân cây vào đầu mùa xuân.",
                        "khuyen_cao_chuyen_gia": "Phun phòng thân cành bằng Tebuconazole hoặc Thiophanate-Methyl khi bắt đầu có dấu hiệu nứt vỏ."
                    }
                }
            ]
        },
        {
            "id": "w1_016",
            "topic": "Cay_Lam_Nghiep_Duoc_Lieu_Quy",
            "name_vi": "Dành dành lấy quả Nho Quan Ninh Bình",
            "scientific_name": "Gardenia jasminoides J.Ellis",
            "dia_ban_pho_bien": ["Nho Quan", "Gia Viễn", "Ninh Bình", "Hòa Bình", "Thanh Hóa"],
            "dac_tinh_sinh_thai": "Cây bụi dược liệu và màu thực phẩm truyền thống quý giá, ưa đất đồi đá vôi phong hóa hoặc đất thịt pha sét, chịu khô hạn và nắng nóng tốt, quả có 6-8 cạnh dọc chứa nhiều chất crocin vàng cam rực rỡ.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Đốm vi khuẩn lá quả dành dành",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Vi khuẩn",
                        "ten_khoa_hoc": "Xanthomonas gardeniae"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết bệnh bắt đầu là các chấm ủng nước trong mờ ở mặt dưới phiến lá",
                        "Sau vết bệnh chuyển màu nâu đen góc cạnh bị chặn bởi các gân lá nhỏ có quầng vàng xung quanh",
                        "Quả dành dành bị các đốm thâm đen lõm sâu làm méo mó quả và rụng sớm",
                        "Lá rụng lả tả làm cây xơ xác giảm năng suất thu hái quả dược liệu"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Đốm thán thư: Đốm vi khuẩn có dạng góc cạnh ngậm nước trong suốt giai đoạn đầu và quầng vàng mỏng; Thán thư đốm tròn đồng tâm khô giòn có chấm bào tử nấm màu hồng cam khi ẩm.",
                    "kiem_tra_thuc_dia": "Lấy lá tươi giơ ngược ánh nắng thấy rõ các đốm ngậm nước trong suốt viền gân lá góc cạnh.",
                    "phac_do_vietgap": {
                        "canh_tac": "Dọn sạch cỏ dại quanh gốc cây, tạo khoảng cách trồng thông thoáng 1.5m x 1.5m đón gió.",
                        "sinh_hoc": "Phun phòng định kỳ Nano Bạc Đồng 400ppm kết hợp chế phẩm sinh học Bacillus subtilis.",
                        "khuyen_cao_chuyen_gia": "Phun phòng trừ bằng Kasugamycin, Oxytetracycline hoặc Bismerthiazol trong mùa mưa bão."
                    }
                },
                {
                    "ten_benh": "Bệnh Nấm bồ hóng đen lá quả do rệp vảy",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Nấm hoại sinh",
                        "ten_khoa_hoc": "Capnodium spp. / Coccus viridis",
                        "vector_truyen_benh": "Rệp vảy xanh (Coccus viridis)"
                    },
                    "trieu_chung_dien_hinh": [
                        "Mặt trên phiến lá phủ một lớp màng đen như muội đèn bồ hóng che kín khí khổng",
                        "Dưới mặt dưới lá và dọc các gân chính bám đầy những con rệp vảy màu xanh lục hình bầu dục dẹt",
                        "Quả dành dành bị bám muội đen không lên được màu vàng cam chuẩn khi sấy khô",
                        "Cây bị suy dinh dưỡng, cành còi cọc chậm ra hoa đậu quả"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Nấm thán thư đen quả: Bồ hóng dùng tay miết mạnh lớp đen bong ra như bột tro than để lộ vỏ quả lành lặn; Thán thư vỏ quả bị ăn mòn loét sâu không thể miết sạch.",
                    "kiem_tra_thuc_dia": "Lật mặt dưới lá thấy các vảy sáp màu xanh lục dính bết dọc gân lá, lấy đầu ngón tay cạy nhẹ vảy sáp tróc ra.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt tỉa cành la, cành khuất ánh sáng trong lòng tán, quét vôi trắng gốc cây ngăn kiến tha rệp.",
                        "sinh_hoc": "Phun chế phẩm nấm ký sinh Beauveria bassiana hoặc nấm Verticillium lecanii diệt trừ rệp vảy xanh.",
                        "khuyen_cao_chuyen_gia": "Phun dầu khoáng sinh học SK Enspray 99EC nồng độ 0.5% để rửa trôi muội đen và làm ngạt rệp vảy."
                    }
                }
            ]
        },
        {
            "id": "w1_017",
            "topic": "Cay_Lam_Nghiep_Duoc_Lieu_Quy",
            "name_vi": "Đơn đỏ dược liệu Bắc Ninh",
            "scientific_name": "Ixora coccinea L.",
            "dia_ban_pho_bien": ["Gia Bình", "Lương Tài", "Bắc Ninh", "Bắc Giang", "Hải Dương"],
            "dac_tinh_sinh_thai": "Cây bụi dược liệu thanh nhiệt tiêu độc quý, ưa đất phù sa ven sông Đuống tơi xốp, ưa sáng, chịu hạn khá tốt, ra hoa chùm đỏ rực rỡ và cho lá thu hái quanh năm.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Thán thư rách mép lá cây đơn đỏ",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Colletotrichum ixoricola"
                    },
                    "trieu_chung_dien_hinh": [
                        "Mép và chóp lá xuất hiện các vệt cháy thâm màu nâu sẫm lan dần vào trong phiến lá",
                        "Vết bệnh có các đường vân gợn sóng màu nâu đậm nhạt xen kẽ",
                        "Mô lá bị hoại tử khô xác, giòn rách làm biến dạng phiến lá dược liệu",
                        "Hoa chùm bị thâm đen đầu cánh, hoa rụng sớm không kết hạt"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Cháy nắng phiến lá: Cháy nắng vết bạc màu trắng xám khô giòn không có vân gợn sóng; Thán thư có viền gợn sóng sắc nét màu nâu đỏ sậm.",
                    "kiem_tra_thuc_dia": "Vò nhẹ mép lá thấy mô lá giòn rụm rách toạc hình răng cưa dọc theo vân bệnh.",
                    "phac_do_vietgap": {
                        "canh_tac": "Tưới tiêu hợp lý vào gốc không tưới phun đẫm lên tán lá vào buổi tối muộn.",
                        "sinh_hoc": "Phun dịch chiết Chitosan nano kết hợp nấm đối kháng Chaetomium định kỳ 15 ngày/lần.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bằng Antracol 70WP hoặc Difenoconazole khi độ ẩm không khí vượt trên 85%."
                    }
                },
                {
                    "ten_benh": "Bệnh Tuyến trùng nốt sưng rễ cằn cỗi cây đơn đỏ",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Tuyến trùng",
                        "ten_khoa_hoc": "Meloidogyne spp."
                    },
                    "trieu_chung_dien_hinh": [
                        "Hệ rễ tơ xuất hiện vô số nốt sần tròn nhỏ như hạt kê, hạt đỗ xâu thành chuỗi",
                        "Bộ rễ bị nghẹt không hút được nước và khoáng chất, rễ chính bị thâm đen mục rỗng",
                        "Tán lá chuyển màu xanh nhạt hoặc vàng úa, cây cằn cỗi đứng ngưng phát triển chồi non",
                        "Lá rụng nhiều khi gặp thời tiết hanh khô hoặc nắng trưa gay gắt"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Nốt sần vi khuẩn cố định đạm: Nốt sần vi khuẩn bóc ra có màu hồng đỏ chứa leghemoglobin và dễ dàng tuột khỏi vỏ rễ; Nốt sưng tuyến trùng là mô rễ tự sưng to dị dạng xơ cứng không có màu hồng bên trong.",
                    "kiem_tra_thuc_dia": "Đào nhẹ một cụm rễ tơ rửa nước thấy các hạt u sần méo mó dính liền trục rễ như chuỗi cườm.",
                    "phac_do_vietgap": {
                        "canh_tac": "Xới xáo phơi đất kỹ trước khi trồng, luân canh với cây cúc vạn thọ để tiết chất diệt tuyến trùng tự nhiên.",
                        "sinh_hoc": "Bón phân hữu cơ vi sinh ủ nấm ký sinh Paecilomyces lilacinus kết hợp bã bánh dầu neem.",
                        "khuyen_cao_chuyen_gia": "Tưới gốc bằng Abamectin sinh học hoặc Chitosan đậm đặc 2 lần cách nhau 15 ngày."
                    }
                }
            ]
        },
        {
            "id": "w1_018",
            "topic": "Cay_Lam_Nghiep_Duoc_Lieu_Quy",
            "name_vi": "Ngũ gia bì gai Phú Thọ",
            "scientific_name": "Eleutherococcus trifoliatus (L.) S.Y.Hu",
            "dia_ban_pho_bien": ["Thanh Ba", "Đoan Hùng", "Phú Thọ", "Yên Bái", "Tuyên Quang"],
            "dac_tinh_sinh_thai": "Cây bụi leo có gai dược liệu quý giúp bồi bổ khí huyết, ưa đất đồi Feralit giàu mùn ven bìa rừng, chịu bóng bán phần, ưa ẩm độ cao 80-90%, phát triển mạnh vào mùa xuân hè.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Rỉ sắt đốm vàng lá chét ngũ gia bì gai",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Aecidium acanthopanacis"
                    },
                    "trieu_chung_dien_hinh": [
                        "Mặt dưới lá chét xuất hiện các nốt mụn nhỏ li ti hình chén màu vàng cam rực rỡ như rỉ sắt gỉ đồng",
                        "Mặt trên lá tương ứng xuất hiện các đốm tròn màu vàng nhạt hơi nhô gồ ghề",
                        "Bào tử nấm rỉ sắt phát tán thành đám bụi phấn màu vàng cam dính vào tay khi chạm vào",
                        "Lá bị khô cháy vàng từng chòm và rụng sớm làm trơ cành gai nhọn"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Đốm vàng do nhện đỏ: Nhện đỏ tạo các chấm chích hút trắng li ti có màng tơ mỏng; Nấm rỉ sắt tạo các nốt mụn sưng gồ giải phóng bụi phấn nấm màu vàng cam rõ rệt.",
                    "kiem_tra_thuc_dia": "Lấy ngón tay xoa vào mặt dưới lá thấy bột phấn màu vàng cam óng dính đầy trên đầu ngón tay.",
                    "phac_do_vietgap": {
                        "canh_tac": "Phát quang cỏ dại, tỉa thưa giàn leo giúp ánh nắng chiếu vào các tầng lá dưới.",
                        "sinh_hoc": "Phun phòng bằng nấm đối kháng Trichoderma kết hợp dịch chiết Nano Bạc Đồng 300ppm.",
                        "khuyen_cao_chuyen_gia": "Phun trừ bằng Hexaconazole (Anvil 5SC) hoặc Diniconazole khi bắt đầu nhú các nốt mụn cam."
                    }
                },
                {
                    "ten_benh": "Bệnh Thối rễ cành héo rũ nấm Phytophthora",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Phytophthora cactorum"
                    },
                    "trieu_chung_dien_hinh": [
                        "Phần cổ rễ và gốc thân sát mặt đất bị úng nước thâm đen, vỏ rễ bị nứt mục tróc mảng",
                        "Lá chét héo rũ đột ngột nhưng vẫn giữ màu xanh xám, toàn bộ dây leo chết rũ đứng",
                        "Cắt ngang phần gốc thân thấy vòng mô mạch dẫn bị hóa đen thâm tím bốc mùi chua",
                        "Hệ rễ củ bị thối rữa nát chỉ còn trơ lõi xơ xác"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Chết khô do hạn: Héo do hạn lá khô giòn vàng đều, tưới nước cây tươi lại ngay; Héo Phytophthora lá héo rũ xanh, gốc thân thối đen và cây chết vĩnh viễn không hồi phục.",
                    "kiem_tra_thuc_dia": "Cào lớp đất cổ rễ thấy mô vỏ bị thối ướt trơn nhớt màu đen mun, ngửi có mùi hôi chua lên men.",
                    "phac_do_vietgap": {
                        "canh_tac": "Đánh rãnh thoát nước sâu quanh luống, tránh để nước mưa đọng vũng quanh gốc cây dược liệu.",
                        "sinh_hoc": "Tưới phòng gốc bằng hỗn hợp men vi sinh Bacillus subtilis và Trichoderma harzianum định kỳ 1 tháng/lần.",
                        "khuyen_cao_chuyen_gia": "Tưới thuốc trừ nấm Phosphonate hữu cơ hoặc Metalaxyl-M (Ridomil Gold) ngay khi cây chớm có biểu hiện héo ngọn."
                    }
                }
            ]
        },
        {
            "id": "w1_019",
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": "Bưởi đỏ Mê Linh Hà Nội",
            "scientific_name": "Citrus maxima Merr. cv. Do Me Linh",
            "dia_ban_pho_bien": ["Mê Linh", "Sóc Sơn", "Đông Anh", "Hà Nội", "Vĩnh Phúc"],
            "dac_tinh_sinh_thai": "Giống bưởi quý có cả tép và vỏ màu hồng đỏ khi chín, ưa đất bãi bồi phù sa sông Hồng, đất thịt pha cát tơi xốp, pH 6.0 - 6.5, thời tiết nắng ấm và hanh khô vào cuối thu giúp sắc tố lycopene đỏ đậm đà.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Xì mủ thối gốc chảy gôm bưởi đỏ",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Phytophthora nicotianae"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vỏ thân sát cổ rễ bị sũng nước nứt toác từng vệt dài rỉ dịch mủ màu cánh gián dính nhớt",
                        "Mô vỏ bị thối nâu đen ăn sâu vào lớp gỗ bên trong, lá vàng đồng loạt và rụng dần",
                        "Cây bưởi ra hoa trái vụ bất thường rồi suy kiệt khô cành chết đứng",
                        "Vỏ quả bưởi đỏ bị thâm nâu nhũn nước làm thối ủng tép bưởi bên trong"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Xì mủ do sâu đục vỏ: Sâu đục vỏ có vết đục cơ giới đùn mạt cưa phân sâu li ti; Phytophthora không có mạt cưa, mô vỏ nứt sũng nước bốc mùi chua nồng.",
                    "kiem_tra_thuc_dia": "Dùng dao cạo nhẹ vết nứt thân thấy lớp tầng sinh mô bên dưới bị thâm đen ướt nhầy, chất gôm dẻo quánh dính tay.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cào đất xới nhẹ để lộ cổ rễ cho thoáng gió, quét vôi trắng gốc cây cao 80cm vào đầu mùa mưa.",
                        "sinh_hoc": "Cạo sạch vết xì mủ rồi quét chế phẩm nấm đối kháng Chaetomium kết hợp Nano Bạc Đồng đặc.",
                        "khuyen_cao_chuyen_gia": "Quét gốc hoặc tưới đẫm vùng rễ bằng Phosphonate hữu cơ hoặc Aliette 800WG định kỳ trong mùa mưa."
                    }
                },
                {
                    "ten_benh": "Bệnh Đốm dầu vỏ quả bưởi đỏ (Bệnh mỡ bưởi)",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Mycosphaerella citri"
                    },
                    "trieu_chung_dien_hinh": [
                        "Mặt vỏ quả bưởi xuất hiện những đốm nhỏ trong suốt như giọt dầu loang trên bề mặt túi tinh dầu",
                        "Sau vết bệnh chuyển màu nâu đen hơi lồi lên làm vỏ quả sần sùi kém bóng bẩy",
                        "Mặt dưới lá xuất hiện các vết đốm dầu màu vàng nâu bết dính",
                        "Làm mất thẩm mỹ nghiêm trọng đối với bưởi đỏ trưng bày tết nguyên đán"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Vết trầy xước cơ giới: Vết xước liền sẹo trắng xám có vảy khô; Đốm dầu nấm là các chấm tròn thâm mỡ bóng loáng ăn theo từng cụm túi tinh dầu vỏ bưởi.",
                    "kiem_tra_thuc_dia": "Dùng ngón tay miết lên bề mặt quả thấy sần sùi ram ráp ở các điểm đốm dầu thâm đen.",
                    "phac_do_vietgap": {
                        "canh_tac": "Bao quả bằng túi chuyên dụng khi quả bưởi đạt kích thước bằng nắm tay; cắt tỉa thông thoáng tán lá.",
                        "sinh_hoc": "Phun phòng chế phẩm dầu khoáng hữu cơ kết hợp nấm đối kháng Bacillus subtilis.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bằng Booc-đô 1% hoặc Mancozeb khi bưởi vừa rụng cánh hoa đậu quả non."
                    }
                }
            ]
        },
        {
            "id": "w1_020",
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": "Ổi găng Đông Dư Gia Lâm",
            "scientific_name": "Psidium guajava L. cv. Dong Du",
            "dia_ban_pho_bien": ["Gia Lâm", "Long Biên", "Hà Nội", "Hưng Yên", "Bắc Ninh"],
            "dac_tinh_sinh_thai": "Cây ổi truyền thống nức tiếng vùng bãi sông Hồng, quả nhỏ tròn có 5 gờ nổi như quả găng, giòn ngọt thơm ngát khi chín vàng ươm, cây chịu ngập úng tạm thời cực tốt nhờ hệ rễ phát triển mạnh mẽ.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Rỉ sắt đốm lá quả non ổi găng",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Puccinia psidii"
                    },
                    "trieu_chung_dien_hinh": [
                        "Trên lá non: Xuất hiện các mụn sưng nhỏ li ti màu vàng tươi, sau biến thành các ổ nấm màu vàng cam như gỉ sắt",
                        "Lá non bị vặn vẹo biến dạng, chồi non bị khô thắt đầu ngọn chết lộc",
                        "Trên quả non: Vết bệnh là các nốt mụn tròn màu nâu đỏ làm quả non bị sần sùi chai cứng và rụng sớm",
                        "Bột phấn màu vàng rỉ sắt bám dính dày đặc trên các bộ phận bị nhiễm bệnh"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Đốm thán thư: Rỉ sắt có các ổ mụn nâng cao bề mặt giải phóng bụi phấn vàng cam rực rỡ; Thán thư là vết lõm sâu màu nâu xám có vòng tròn đồng tâm.",
                    "kiem_tra_thuc_dia": "Lấy tay quẹt nhẹ qua đám mụn trên lá thấy bụi phấn vàng cam óng bám dày vào ngón tay như nhũ vàng.",
                    "phac_do_vietgap": {
                        "canh_tac": "Tỉa cành đốn lộc tạo tán thưa thoáng, tiêu hủy triệt để cành lá non bị nhiễm bệnh sớm.",
                        "sinh_hoc": "Phun Nano Bạc Đồng 400ppm kết hợp chế phẩm sinh học Chitosan kích kháng màng tế bào.",
                        "khuyen_cao_chuyen_gia": "Phun luân phiên Tebuconazole, Azoxystrobin hoặc Hexaconazole khi lộc non bắt đầu bung nhú."
                    }
                },
                {
                    "ten_benh": "Bệnh Thối mềm quả ổi do nấm Rhizopus",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Rhizopus stolonifer"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết thối bắt đầu từ các vết xây xát nhẹ hoặc vết chích của ruồi đục quả",
                        "Vỏ quả nhanh chóng bị nhũn nước, thịt quả bên trong bị rữa nát thành chất lỏng chua",
                        "Trên bề mặt vỏ mọc lên một lớp nấm mốc trắng muốt xốp như sợi bông, trên đầu có các chấm đen li ti",
                        "Quả bị thối rụng bốc mùi men chua nồng nặc chỉ sau 24-36 giờ"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Thối do nấm Phytophthora: Nấm Phytophthora tạo vết nâu xám cứng dai không có sợi tơ nấm bông gòn chấm đen; Rhizopus tạo sợi tơ nấm bồng bềnh như mạng nhện có đầu bào tử đen li ti như đầu tăm.",
                    "kiem_tra_thuc_dia": "Cầm quả ổi thối thấy nhũn nát chảy dịch nước chua, lớp sợi tơ trắng mốc có các hạt đầu kim đen mọc tua tủa.",
                    "phac_do_vietgap": {
                        "canh_tac": "Thu hoạch quả nhẹ nhàng không làm trầy xước vỏ, bao quả sớm trước khi ruồi vàng chích.",
                        "sinh_hoc": "Xử lý sau thu hoạch bằng dung dịch sáp phủ sinh học Chitosan 1% hoặc rửa nước Nano Bạc an toàn.",
                        "khuyen_cao_chuyen_gia": "Đặt bẫy bả ruồi vàng sinh học Protein thủy phân hoặc Methyl Eugenol xung quanh vườn."
                    }
                }
            ]
        },
        {
            "id": "w1_021",
            "topic": "Rau_Cu_Gia_Vi_Va_Nam",
            "name_vi": "Hành tím Kinh Môn Hải Dương",
            "scientific_name": "Allium ascalonicum L. cv. Kinh Mon",
            "dia_ban_pho_bien": ["Kinh Môn", "Kim Thành", "Hải Dương", "Quảng Ninh", "Hải Phòng"],
            "dac_tinh_sinh_thai": "Cây gia vị chủ lực vùng đất bãi phù sa pha cát Kinh Môn sau vụ lúa mùa, ưa thời tiết mùa đông mát lạnh 18-22 độ C, đất tơi xốp giàu kali để củ hành tím chắc nịch, cay nồng và vỏ bóng đẹp.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Sương mai đốm mốc tím lá hành",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Peronospora destructor"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết bệnh ban đầu là những vệt màu xanh nhạt hoặc trắng ngà hình bầu dục dài trên cọng hành rỗng",
                        "Khi trời mưa phùn ẩm ướt sáng sớm, trên vết bệnh phủ lớp mốc mịn màu tím nhạt hoặc tím tro rất đặc trưng",
                        "Cọng hành bị gãy gập ngang vết bệnh, tóp lại và khô cháy từ ngọn xuống",
                        "Cả ruộng hành bị lụi tàn trắng xóa lá, củ hành không phát triển được còi cọc nhỏ thó"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Đốm tím Alternaria porri: Đốm Alternaria có màu nâu tía đậm tâm đồng tâm khô cứng; Sương mai Peronospora có lớp mốc nhung màu tím nhạt bao phủ vào buổi sáng ẩm ướt và cọng hành bị nhũn gãy gập.",
                    "kiem_tra_thuc_dia": "Sáng sớm có sương, vạch cọng hành thấy lớp lông tơ mịn màng màu tím tro bao quanh vệt gãy gập của lá.",
                    "phac_do_vietgap": {
                        "canh_tac": "Lên luống cao 30cm, tưới rãnh thấm thoát nước nhanh không để đọng nước mặt luống.",
                        "sinh_hoc": "Phun phòng nấm đối kháng Chaetomium kết hợp chế phẩm sinh học Nano Đồng 500ppm.",
                        "khuyen_cao_chuyen_gia": "Phun trừ bằng Metalaxyl-M + Mancozeb (Ridomil Gold), Cymoxanil hoặc Dimethomorph khi trời có sương mù ẩm ướt."
                    }
                },
                {
                    "ten_benh": "Bệnh Thối xám củ hành bảo quản",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Botrytis allii"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết bệnh bắt đầu từ phần cổ củ hành sau khi cắt cuống thu hoạch sấy chưa khô kiệt",
                        "Mô cổ củ bị sũng nước chuyển màu nâu xám, sau lan xuống các tép hành bên trong",
                        "Giữa các lớp vảy tép hành mọc lên lớp mốc màu xám tro dày đặc bốc mùi ẩm mốc hôi thối",
                        "Củ hành bị xẹp lép, thối rữa nát lây lan hàng loạt trong kho chứa nông sản"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Thối mềm vi khuẩn: Thối vi khuẩn mô tép hành nhũn chảy nước bốc mùi thối khắm tanh tưởi; Thối xám nấm Botrytis mô tép teo tóp dai có lớp mốc tro hạt bụi xám phủ kín.",
                    "kiem_tra_thuc_dia": "Tách lớp vỏ hành khô ngoài cùng thấy lớp tép bên trong phủ lớp phấn mịn màu xám tro, bóp nhẹ thấy cổ củ mềm rỗng.",
                    "phac_do_vietgap": {
                        "canh_tac": "Thu hoạch vào ngày nắng ráo, phơi nắng hoặc sấy khô cổ hành triệt để trước khi xếp vào giàn bảo quản thoáng gió.",
                        "sinh_hoc": "Xử lý củ giống trước khi trồng và phun phòng ruộng bằng men vi sinh Bacillus subtilis.",
                        "khuyen_cao_chuyen_gia": "Phun phòng trước khi thu hoạch 10 ngày bằng Iprodione (Rovral 50WP) hoặc Boscalid."
                    }
                }
            ]
        },
        {
            "id": "w1_022",
            "topic": "Cay_Luong_Thuc_Va_Hoa_Mau",
            "name_vi": "Nếp cái hoa vàng Kinh Môn Hải Dương",
            "scientific_name": "Oryza sativa L. var. glutinosa cv. Nep Cai Hoa Vang",
            "dia_ban_pho_bien": ["Kinh Môn", "Chí Linh", "Hải Dương", "Đông Triều", "Quảng Ninh"],
            "dac_tinh_sinh_thai": "Giống lúa nếp đặc sản trứ danh xứ Đông, gieo cấy vụ mùa (trỗ bông đón gió heo may tháng 9-10 âm lịch), ưa đất phù sa và đất sét pha thịt màu mỡ ven sông, hạt gạo tròn mẩy, đồ xôi dẻo quánh thơm lừng.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Đạo ôn cổ bông lúa nếp cái hoa vàng",
                    "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Magnaporthe oryzae (Pyricularia oryzae)"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết bệnh xuất hiện ở đoạn cổ giáp giữa thân và bông lúa, ban đầu là chấm thâm nhỏ sau lan thành vòng màu nâu sẫm thắt nghẽn",
                        "Toàn bộ bông lúa phía trên bị mất nguồn tiếp tế dinh dưỡng, bông lúa bị khô trắng đứng thẳng không vào hạt (bông bạc)",
                        "Nếu nhiễm muộn khi hạt đã ngậm sữa, hạt lúa bị lửng lép, vỏ trấu có vết đốm mắt chim viền nâu",
                        "Cổ bông bị giòn gãy gập rũ xuống khiến năng suất mất trắng 80-100%"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Bạc bông do sâu đục thân: Sâu đục thân cắt đứt hoàn toàn mạch ở gióng thân bên dưới, rút nhẹ dảnh lúa thấy đứt tuột dễ dàng; Đạo ôn cổ bông dảnh lúa dính chặt chắc chắn và chỉ có vết thâm thắt nghẽn ở đúng cổ giáp ranh bông lúa.",
                    "kiem_tra_thuc_dia": "Vạch bông lúa bạc nhìn đúng vị trí cổ bông thấy vệt thâm đen thắt eo lại, sờ vào thấy khô ráp giòn dễ gãy ngang.",
                    "phac_do_vietgap": {
                        "canh_tac": "Bón phân cân đối không bón thừa đạm ure, giữ mực nước chân ruộng ổn định lúc lúa trỗ bông.",
                        "sinh_hoc": "Phun phòng chế phẩm nấm đối kháng Chaetomium kết hợp dịch chiết Nano Bạc Đồng giai đoạn lúa trỗ lẹt xẹt.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bắt buộc 2 lần: lần 1 khi lúa trỗ lẹt xẹt 3-5% và lần 2 khi lúa trỗ đều bằng Tricyclazole (Beam 75WP) hoặc Isoprothiolane (Fuji-one 40EC)."
                    }
                },
                {
                    "ten_benh": "Bệnh Khô vằn thân bẹ lúa nếp",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Rhizoctonia solani"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết bệnh xuất hiện ở bẹ lá sát mặt nước dưới dạng các vệt loang lổ hình da hổ hoặc vân mây màu xám xanh viền nâu đỏ",
                        "Vết bệnh lan nhanh từ bẹ lá phía dưới lên các bẹ lá trên và phiến lá đòng",
                        "Trên bề mặt vết vằn xuất hiện các sợi tơ nấm trắng và các viên hạch nấm tròn cứng như hạt cải màu nâu đen",
                        "Làm cây lúa bị nghẹt đòng, bông nhỏ lép và dảnh lúa mềm rũ dễ bị ngã rạp khi mưa gió"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Vết thối bẹ vi khuẩn: Vết thối vi khuẩn không có vân mây da hổ sắc nét và không có hạch nấm hạt cải bám dính trên bẹ lá.",
                    "kiem_tra_thuc_dia": "Vạch gốc bụi lúa thấy các vết loang vân mây da hổ rõ rệt, dùng ngón tay gạt thấy các viên hạch nấm tròn màu nâu rơi lả tả xuống mặt nước.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cấy mật độ vừa phải không cấy quá dày, vớt sạch hạch nấm nổi trên mặt nước khi làm đất.",
                        "sinh_hoc": "Phun men vi sinh đối kháng Bacillus subtilis hoặc Trichoderma vào gốc lúa định kỳ.",
                        "khuyen_cao_chuyen_gia": "Phun trừ bằng hoạt chất sinh học Validamycin A (Vali 5SL) hoặc Hexaconazole (Anvil 5SC) khi bệnh mới chớm ở bẹ lá dưới."
                    }
                }
            ]
        },
        {
            "id": "w1_023",
            "topic": "Rau_Cu_Gia_Vi_Va_Nam",
            "name_vi": "Cải bẹ dưa Bắc Ninh",
            "scientific_name": "Brassica juncea (L.) Czern. cv. Bac Ninh",
            "dia_ban_pho_bien": ["Thuận Thành", "Quế Võ", "Bắc Ninh", "Hải Dương", "Bắc Giang"],
            "dac_tinh_sinh_thai": "Giống cải chuyên dùng muối dưa chua giòn ngon nức tiếng, bẹ to dày mọng nước, ưa vụ đông mát mẻ 15-22 độ C, đất phù sa bãi bồi ven sông Đuống giàu dinh dưỡng, thu hoạch sau 40-50 ngày gieo trồng.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Sương mai hoa thập tự lá cải bẹ dưa",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Hyaloperonospora brassicae (Peronospora parasitica)"
                    },
                    "trieu_chung_dien_hinh": [
                        "Mặt trên phiến lá xuất hiện những đốm màu vàng nhạt góc cạnh giới hạn bởi các gân nhỏ",
                        "Mặt dưới lá tương ứng xuất hiện một lớp màng phấn mốc màu trắng xám mịn màng",
                        "Lá già bị úa vàng khô cháy từ ngoài rìa mép vào, bẹ lá teo tóp nhăn nheo",
                        "Làm giảm mạnh sản lượng và bẹ cải bị sượng không đạt độ giòn chua khi muối dưa"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Đốm mắt cua do nấm Alternaria: Alternaria có các vòng tròn đồng tâm màu nâu đen khô giòn; Sương mai vết bệnh góc cạnh màu vàng nhạt và có lớp mốc trắng mịn mặt dưới.",
                    "kiem_tra_thuc_dia": "Lật mặt dưới lá cải thấy lớp lông phấn mốc trắng như mạng nhện mịn bám sát các rãnh gân lá góc cạnh.",
                    "phac_do_vietgap": {
                        "canh_tac": "Lên luống cao rãnh sâu, tránh tưới phun đọng nước trên tán lá cải vào buổi chiều tối.",
                        "sinh_hoc": "Phun Nano Bạc Đồng 300ppm kết hợp vi khuẩn đối kháng Bacillus subtilis.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bằng Mancozeb, Metalaxyl hoặc Fosetyl Aluminium khi thời tiết ẩm ướt nhiều sương."
                    }
                },
                {
                    "ten_benh": "Bệnh Cháy lá đốm tròn vi khuẩn cải bẹ",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Vi khuẩn",
                        "ten_khoa_hoc": "Pseudomonas syringae pv. maculicola"
                    },
                    "trieu_chung_dien_hinh": [
                        "Phiến lá xuất hiện các chấm nhỏ màu nâu đen ngậm nước rải rác",
                        "Vết bệnh lan rộng thành các đốm tròn hoặc góc cạnh có quầng halo vàng sáng bao quanh",
                        "Các đốm liên kết làm rách thủng phiến lá, bẹ cải bị các vệt thâm đen làm thối nhũn nhẹ",
                        "Cây cằn cỗi lá xơ xác mất giá trị thương phẩm"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Sâu cắn rách lá: Sâu cắn để lại mép rách răng cưa nham nhở không có quầng vàng vi khuẩn xung quanh vết rách.",
                    "kiem_tra_thuc_dia": "Soi lá ngược ánh sáng thấy các đốm nhỏ trong suốt viền quầng vàng sáng rực rỡ rất đồng đều.",
                    "phac_do_vietgap": {
                        "canh_tac": "Vệ sinh dọn sạch tàn dư lá cải sau thu hoạch, xử lý vôi bột trước khi gieo lứa mới.",
                        "sinh_hoc": "Phun dịch chiết tỏi ớt gừng sinh học định kỳ 7 ngày/lần để phòng ngừa.",
                        "khuyen_cao_chuyen_gia": "Phun trừ bằng Kasugamycin (Kasumin 2SL) hoặc Copper Hydroxide khi bệnh chớm xuất hiện."
                    }
                }
            ]
        },
        {
            "id": "w1_024",
            "topic": "Rau_Cu_Gia_Vi_Va_Nam",
            "name_vi": "Củ niễng Nam Định",
            "scientific_name": "Zizania latifolia (Griseb.) Turcz. ex Stapf",
            "dia_ban_pho_bien": ["Vụ Bản", "Ý Yên", "Nam Định", "Hà Nam", "Hải Dương"],
            "dac_tinh_sinh_thai": "Cây thảo thủy sinh vùng đồng trũng châu thổ sông Hồng, ưa bùn nước sâu 20-40cm, mùa thu đông nấm than ký sinh vào mô thân non làm gốc thân phình to mập mạp màu trắng xốp ăn giòn ngọt ngậy bùi.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Than đen u sưng quá mức bẹ niễng",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm ký sinh tạo củ",
                        "ten_khoa_hoc": "Ustilago esculenta"
                    },
                    "trieu_chung_dien_hinh": [
                        "Nấm ký sinh quá đà làm mô củ niễng bị biến tính chuyển sang giai đoạn sinh sản phát tán bào tử",
                        "Thịt củ niễng bên trong chuyển từ màu trắng ngà sang màu xám đen chứa đầy bụi bào tử than đen",
                        "Củ niễng bị nứt toác, vỏ bẹ chuyển màu đen xì bốc bụi than đen khi chạm vào",
                        "Củ mất hoàn toàn giá trị ẩm thực, ăn đắng chát xơ cứng không ăn được"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Củ niễng non chuẩn độ: Củ chuẩn độ thịt trắng phau mịn màng có các chấm đen sợi nấm li ti mờ nhạt; Củ quá lứa biến tính nứt vỡ ruột chứa đầy bột than đen kịt như thuốc súng.",
                    "kiem_tra_thuc_dia": "Bẻ đôi củ niễng thấy bột đen li ti bay ra dính đầy ngón tay làm đen sì đầu ngón tay như than tổ ong.",
                    "phac_do_vietgap": {
                        "canh_tac": "Thu hoạch niễng đúng độ tuổi (khi bẹ hơi phình to, chưa nứt vỏ bẹ ngoài); chọn lọc mầm giống niễng có tỷ lệ nhiễm nấm vừa phải.",
                        "sinh_hoc": "Điều tiết mực nước ruộng niễng hợp lý để khống chế quá trình phát tán bào tử than.",
                        "khuyen_cao_chuyen_gia": "Không để củ niễng quá lứa trên ruộng, thu gom tiêu hủy các củ bị xì bụi than để tránh lây nhiễm cho vụ sau."
                    }
                },
                {
                    "ten_benh": "Bệnh Đốm mắt cua bẹ lá niễng",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Bipolaris zizaniae"
                    },
                    "trieu_chung_dien_hinh": [
                        "Mặt phiến lá và bẹ ngoài xuất hiện các chấm nhỏ màu nâu đỏ hình bầu dục dài",
                        "Vết bệnh lan rộng tâm xám bạc viền tím thẫm như mắt cua chạy dọc theo gân lá",
                        "Lá niễng bị khô cháy từ chóp lá rũ xuống làm giảm quang hợp nuôi củ mập",
                        "Cây bị cằn cỗi đẻ nhánh ít, củ niễng nhỏ bé gầy guộc"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Rầy nâu chích hút: Rầy chích làm gốc bẹ có vết kim châm chảy nhựa và bồ hóng; Đốm nấm Bipolaris có vết bầu dục đồng tâm rõ ràng có viền tía sắc sảo.",
                    "kiem_tra_thuc_dia": "Vuốt nhẹ mép bẹ lá thấy khô rát, nhìn ngược sáng thấy đốm bầu dục tâm mỏng xám bạc thủng lỗ mọt.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt tỉa lá già sát mặt nước, bón bổ sung tro trấu và phân lân kali giúp thân bẹ cứng cáp.",
                        "sinh_hoc": "Phun phòng bằng nấm đối kháng Trichoderma kết hợp dịch Nano Bạc Đồng trên ruộng niễng.",
                        "khuyen_cao_chuyen_gia": "Phun hoạt chất Mancozeb hoặc Azoxystrobin giai đoạn trước khi niễng phình củ."
                    }
                }
            ]
        },
        {
            "id": "w1_025",
            "topic": "Cay_Lam_Nghiep_Duoc_Lieu_Quy",
            "name_vi": "Cây sưa đỏ Vĩnh Phúc",
            "scientific_name": "Dalbergia tonkinensis Prain",
            "dia_ban_pho_bien": ["Tam Đảo", "Vĩnh Tường", "Vĩnh Phúc", "Bắc Giang", "Hà Nội"],
            "dac_tinh_sinh_thai": "Cây gỗ lâm nghiệp và tâm linh cực kỳ quý hiếm, ưa đất feralit đỏ vàng đồi núi thấp hoặc đất phù sa cổ thoát nước cực tốt, ưa sáng hoàn toàn, rễ có nốt sần cố định đạm, lõi gỗ giác đỏ có vân 4 mặt tuyệt đẹp.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Phấn trắng lá sưa đỏ vườn ươm",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Phyllactinia dalbergiae"
                    },
                    "trieu_chung_dien_hinh": [
                        "Mặt dưới phiến lá chét sưa đỏ phủ một lớp màng phấn trắng xóa mỏng manh như tơ",
                        "Lá chét non bị quăn queo, mép lá cong rụt lại, lá vàng úa và rụng hàng loạt",
                        "Cây sưa non trong vườn ươm bị chùn đọt ngừng phát triển chiều cao",
                        "Cành non bị khô tóp từ ngọn xuống làm chết cây con"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Bụi đất bám: Bụi đất rửa nước trôi sạch ngay; Phấn trắng nấm có sợi tơ giác mút bám chặt vào biểu bì lá rửa nước không trôi.",
                    "kiem_tra_thuc_dia": "Lấy ngón tay miết nhẹ thấy phấn trắng mịn dính tay, phiến lá bên dưới bị mất diệp lục chuyển màu vàng nhạt.",
                    "phac_do_vietgap": {
                        "canh_tac": "Kê luống vườn ươm thoáng gió, giảm độ che bóng khi cây đã bén rễ cứng cáp.",
                        "sinh_hoc": "Phun chế phẩm sinh học Bacillus subtilis hoặc dung dịch tỏi ớt gừng xua đuổi mầm bệnh.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bằng Hexaconazole (Anvil 5SC) hoặc Difenoconazole định kỳ 10 ngày trong mùa mưa phùn xuân."
                    }
                },
                {
                    "ten_benh": "Bệnh Sâu đục thân xén tóc hại cây sưa đỏ",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Côn trùng gây hại đục thân",
                        "ten_khoa_hoc": "Aristobia testudo"
                    },
                    "trieu_chung_dien_hinh": [
                        "Ấu trùng sâu đục sâu vào lõi gỗ thân cây sưa tạo thành các đường hầm ngoằn ngoèo làm hỏng vân gỗ quý",
                        "Tại các lỗ đục trên thân cây rỉ nhựa cây và đùn ra các hạt mạt cưa phân sâu màu nâu nhạt",
                        "Tán lá phía trên lỗ đục bị héo vàng và khô chết cành",
                        "Thân cây bị rỗng ruột dễ dàng gãy đổ khi có gió bão lớn làm mất trắng giá trị kinh tế của cây gỗ quý"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Bệnh nấm nứt thân xì mủ: Nấm xì mủ chỉ ăn ở mô vỏ ngoài không có đường hầm sâu trong lõi và tuyệt đối không có phân mạt cưa đùn ra lỗ.",
                    "kiem_tra_thuc_dia": "Quan sát thân cây thấy các lỗ nhỏ đường kính 4-8mm có mạt cưa tươi đùn ra vương vãi quanh gốc cây, dùng dây thép chọc vào thấy rỗng sâu bên trong.",
                    "phac_do_vietgap": {
                        "canh_tac": "Bắt diệt xén tóc trưởng thành vào mùa sinh sản đầu mùa mưa, quét vôi trộn lưu huỳnh quanh gốc thân cây cao 1.5m.",
                        "sinh_hoc": "Bơm chế phẩm nấm ký sinh côn trùng Metarhizium anisopliae hoặc tuyến trùng ký sinh Steinernema carpocapsae vào lỗ đục.",
                        "khuyen_cao_chuyen_gia": "Dùng bông gòn thấm thuốc trừ sâu sinh học Abamectin nhét sâu vào lỗ đục rồi dùng đất sét bịt kín miệng lỗ để xông hơi diệt sâu non."
                    }
                }
            ]
        }
    ]
