# -*- coding: utf-8 -*-
"""
Module 4: 65 Vegetables, Spices & Mushrooms (Rau_Cu_Gia_Vi_Va_Nam)
Crops: crop_301 to crop_365
"""

def get_module4_crops():
    crops = [
        {
            "id": "crop_301",
            "topic": "Rau_Cu_Gia_Vi_Va_Nam",
            "name_vi": "Atisô Đà Lạt",
            "scientific_name": "Cynara scolymus L.",
            "dia_ban_pho_bien": ["Đà Lạt", "Lạc Dương - Lâm Đồng", "Sa Pa - Lào Cai"],
            "dac_tinh_sinh_thai": "Cây thảo dược và thực phẩm cao cấp nguồn gốc Địa Trung Hải, thích nghi khí hậu mát mẻ 15-22 độ C quanh năm ở độ cao trên 1500m, lá xẻ thùy sâu mọng nước, bông hoa to béo chứa cynarin bổ gan mật.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Đốm vòng nâu lá Atisô (Ramularia Leaf Spot)",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Ramularia cynarae"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết bệnh ban đầu là chấm nâu tròn nhỏ trên phiến lá bánh tẻ và lá gốc",
                        "Vết đốm lan rộng thành hình tròn hoặc bầu dục viền nâu sẫm, tâm xám trắng có các vòng đồng tâm mờ nhạt",
                        "Lá già bị úa vàng khô cháy từng mảng lớn làm giảm nghiêm trọng sinh khối thu hoạch lá làm trà dược liệu"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với cháy sương muối: Đốm Ramularia có vòng viền nâu đậm sắc nét và lớp phấn trắng li ti mặt dưới khi trời ẩm; cháy sương muối làm nhũn mép lá đồng loạt từ chóp ngoài.",
                    "kiem_tra_thuc_dia": "Lật mặt dưới phiến lá tại vùng đốm nâu soi thấy lớp bụi nấm màu trắng phấn như phủ sương mai mịn.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt tỉa lá già sát đất để tạo độ thông thoáng dưới gốc; không tưới phun mưa lúc chiều tối muộn.",
                        "sinh_hoc": "Phun nấm đối kháng Chaetomium kết hợp chế phẩm sinh học Chitosan nano kích kháng bề mặt lá.",
                        "khuyen_cao_chuyen_gia": "Phun luân phiên Difenoconazole, Azoxystrobin hoặc Chlorothalonil khi chớm thấy vài đốm nâu xuất hiện trên lá chân."
                    }
                },
                {
                    "ten_benh": "Bệnh Thối cổ rễ thối bẹ hoa Atisô",
                    "muc_do_nguy_hiem": "Rất cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Rhizoctonia solani / Pythium spp."
                    },
                    "trieu_chung_dien_hinh": [
                        "Phần gốc thân sát cổ rễ bị ủng thâm đen nhũn nước làm toàn bộ bụi Atisô héo rũ nhanh chóng",
                        "Các bẹ lá ngoài cùng bị thối mềm đổ rạp xuống mặt luống đất",
                        "Bông hoa nụ bị thâm đen chân đế, teo khô không nở hoặc thối rữa từ đài hoa"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với héo rũ vi khuẩn Ralstonia: Thối cổ rễ nấm có các sợi tơ nấm trắng bện quanh vết thâm; héo xanh vi khuẩn thân không có tơ nấm và bó mạch chảy dịch mủ trắng.",
                    "kiem_tra_thuc_dia": "Dùng tay lay nhẹ gốc cây Atisô bị lung lay lỏng lẻo, nhấc lên thấy đứt ngang cổ rễ ủng nhớt bốc mùi ẩm mốc mục nát.",
                    "phac_do_vietgap": {
                        "canh_tac": "Lên luống cao 30-40cm, đào rãnh thoát nước sâu giữa các luống tránh ngập úng mùa mưa bão Đà Lạt.",
                        "sinh_hoc": "Tưới phòng chế phẩm Trichoderma harzianum ủ với phân chuồng hoai mục định kỳ 20 ngày/lần.",
                        "khuyen_cao_chuyen_gia": "Tưới gốc bằng Metalaxyl-M + Mancozeb hoặc Fosetyl-Al khi đất bắt đầu ẩm ướt kéo dài."
                    }
                }
            ]
        },
        {
            "id": "crop_302",
            "topic": "Rau_Cu_Gia_Vi_Va_Nam",
            "name_vi": "Dâu Tây Đà Lạt",
            "scientific_name": "Fragaria x ananassa Duchesne",
            "dia_ban_pho_bien": ["Đà Lạt", "Lạc Dương", "Đơn Dương - Lâm Đồng", "Mộc Châu - Sơn La"],
            "dac_tinh_sinh_thai": "Cây ăn quả thân thảo xứ lạnh cao cấp (giống Mỹ Albion, Nhật Hana, Hàn Quốc Seolhyang), trồng trong nhà màng giá thể hoặc bán thủy canh, quả đỏ mọng nước giàu vitamin C và chất chống oxy hóa.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Mốc xám dâu tây (Grey Mould / Botrytis Fruit Rot)",
                    "muc_do_nguy_hiem": "Rất cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Botrytis cinerea"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết bệnh bắt đầu từ cuống hoa hoặc đầu quả non mọng nước xuất hiện đốm nâu nhạt sũng nước",
                        "Toàn bộ quả dâu tây bị thối nhũn mềm xẹp và bao phủ bởi một lớp lông mốc dày màu xám tro như nỉ dạ",
                        "Bào tử mốc xám phát tán dữ dội khi chạm tay hoặc có luồng gió nhẹ, lây lan sang các chùm quả kế cận"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với thối quả do Rhizopus: Mốc xám Botrytis tạo lớp lông xám tro dày xốp đặc trưng; Rhizopus tạo sợi tơ trắng dài với các đầu bào tử đen li ti như đầu kim và quả chảy nước ồ ạt.",
                    "kiem_tra_thuc_dia": "Dùng ngón tay chạm nhẹ vào quả dâu mốc thấy khói bụi bào tử màu xám bay mù mịt bám đầy ngón tay, quả dâu bên trong nát bấy.",
                    "phac_do_vietgap": {
                        "canh_tac": "Trồng trên giàn cao cách mặt đất 1m hoặc phủ màng nilon đen đục lỗ; cắt tỉa cuống quả già và quả đèo khô rụng.",
                        "sinh_hoc": "Phun phòng nấm đối kháng Trichoderma hoặc vi khuẩn đối kháng Bacillus subtilis định kỳ 7 ngày/lần.",
                        "khuyen_cao_chuyen_gia": "Phun hoạt chất Iprodione, Fenhexamid, Boscalid hoặc Fludioxonil tuân thủ nghiêm ngặt thời gian cách ly 3-5 ngày trước khi thu hái."
                    }
                },
                {
                    "ten_benh": "Bệnh Phấn trắng dâu tây (Powdery Mildew)",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Podosphaera aphanis"
                    },
                    "trieu_chung_dien_hinh": [
                        "Mặt dưới phiến lá non xuất hiện các đốm bột phấn màu trắng xóa, mép lá cong cuốn ngược lên trên thành hình chiếc thuyền",
                        "Quả dâu non bị lớp phấn trắng bám chặt làm quả chai cứng, sần sùi không lớn được và nứt toác",
                        "Mặt lá già chuyển sang màu tím đồng hoặc đỏ gạch khi lớp phấn trắng thoái hóa"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với nhện đỏ gây hại: Phấn trắng có bột trắng mịn bám mặt lá và mép lá quăn ngửa lên; nhện đỏ làm mặt lá có chấm vàng xỉn lấm tấm và mép lá cụp xuống dưới kèm tơ nhện mỏng.",
                    "kiem_tra_thuc_dia": "Vuốt nhẹ mặt dưới phiến lá thấy bột trắng dính vào ngón tay; quả dâu non bị chai sần cọ vào thấy nhám ráp như giấy nhám.",
                    "phac_do_vietgap": {
                        "canh_tac": "Duy trì độ ẩm nhà màng thông thoáng 60-70%, không để nhiệt độ tăng quá cao trên 28 độ C kết hợp ẩm kế đóng kín.",
                        "sinh_hoc": "Phun phòng chế phẩm sinh học Nano Lưu huỳnh hữu cơ hoặc dầu khoáng sinh học nồng độ 0.3%.",
                        "khuyen_cao_chuyen_gia": "Phun luân phiên Kresoxim-methyl, Trifloxystrobin hoặc Myclobutanil khi phát hiện đốm phấn trắng đầu tiên."
                    }
                }
            ]
        },
        {
            "id": "crop_303",
            "topic": "Rau_Cu_Gia_Vi_Va_Nam",
            "name_vi": "Tỏi Lý Sơn",
            "scientific_name": "Allium sativum L.",
            "dia_ban_pho_bien": ["Đảo Lý Sơn - Quảng Ngãi", "Phan Rang - Ninh Thuận"],
            "dac_tinh_sinh_thai": "Tỏi trắng đặc sản đảo núi lửa Lý Sơn trồng trên lớp đất đỏ bazan phủ cát san hô trắng, tép tỏi nhỏ thơm nồng dịu ngọt cay nhẹ, hàm lượng allicin kháng sinh tự nhiên cực cao.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Đốm tím lá tỏi (Purple Blotch)",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Alternaria porri"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết bệnh ban đầu là chấm nhỏ trũng nước hình bầu dục trên phiến lá dài của tỏi",
                        "Vết đốm lan rộng thành hình thoi màu nâu đỏ tím sẫm ở tâm viền vàng bao quanh",
                        "Lá tỏi bị gãy gập ngang ở vị trí vết đốm tím, chóp lá khô héo rũ làm củ tỏi không phình to được"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với sương mai (Peronospora destructor): Đốm tím Alternaria có tâm màu tím than đặc trưng và vết bệnh hình thoi sắc nét; sương mai có màng mốc xám xanh tím mờ nhạt phủ lan tỏa trên lá.",
                    "kiem_tra_thuc_dia": "Dùng tay sờ vào khớp gãy của lá tỏi thấy mô lá tại vết tím bị mủn giòn gãy cụp xuống mặt cát san hô.",
                    "phac_do_vietgap": {
                        "canh_tac": "Rải lớp cát san hô mới sạch mầm bệnh hàng năm; bón vôi bột khử trùng trước khi cắm tép tỏi giống.",
                        "sinh_hoc": "Phun Nano Bạc kết hợp nấm đối kháng Chaetomium trước các đợt gió bấc ẩm ướt biển Đông.",
                        "khuyen_cao_chuyen_gia": "Phun trừ bằng hoạt chất Difenoconazole, Iprodione hoặc Chlorothalonil khi bệnh chớm phát sinh."
                    }
                },
                {
                    "ten_benh": "Bệnh Thối trắng củ tỏi do hạch nấm (White Rot)",
                    "muc_do_nguy_hiem": "Rất cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Stromatinia cepivora (Sclerotium cepivorum)"
                    },
                    "trieu_chung_dien_hinh": [
                        "Lá tỏi từ ngọn bắt đầu úa vàng khô héo từ ngoài vào trong",
                        "Gốc củ tỏi dưới lớp cát bị bao phủ bởi lớp tơ nấm màu trắng muốt như bông gòn",
                        "Rễ tỏi bị thối đứt hoàn toàn, trên lớp tơ trắng xuất hiện vô số hạch nấm nhỏ li ti tròn đen như hạt mè"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với thối đáy củ Fusarium: Thối trắng Stromatinia có tơ trắng muốt như bông kèm hạch mè đen li ti; Fusarium rễ thối hồng nhạt và không có hạch đen hình tròn hạt mè.",
                    "kiem_tra_thuc_dia": "Nhổ bụi tỏi lên thấy củ long rời khỏi rễ, đáy củ dính lớp tơ trắng bám chặt cát biển và hàng chục chấm đen tròn nhỏ.",
                    "phac_do_vietgap": {
                        "canh_tac": "Không cấy tép tỏi lấy từ ruộng bị bệnh cũ; nhặt sạch củ bệnh đem thiêu hủy xa ruộng tỏi đảo.",
                        "sinh_hoc": "Tưới phòng chế phẩm nấm đối kháng Coniothyrium minitans hoặc Trichoderma viride vào đất cát san hô.",
                        "khuyen_cao_chuyen_gia": "Xử lý tép giống trước khi gieo bằng Carbendazim hoặc Tebuconazole; tưới gốc bằng Iprodione khi phát hiện chớm ổ bệnh."
                    }
                }
            ]
        },
        {
            "id": "crop_304",
            "topic": "Rau_Cu_Gia_Vi_Va_Nam",
            "name_vi": "Hành Tím Vĩnh Châu",
            "scientific_name": "Allium ascalonicum L.",
            "dia_ban_pho_bien": ["Vĩnh Châu - Sóc Trăng", "Ninh Hải - Ninh Thuận", "Lý Sơn - Quảng Ngãi"],
            "dac_tinh_sinh_thai": "Hành tím củ to mẩy màu đỏ tím óng ả trồng trên đất giồng cát ven biển Sóc Trăng, cay nồng thơm đặc trưng, vỏ mỏng bóng bảo quản được rất lâu sau thu hoạch.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Cháy lá đốm kim hành tím (Stemphylium Leaf Blight)",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Stemphylium vesicarium"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết bệnh ban đầu là chấm đốm nhỏ màu vàng sáng hoặc trắng nhạt trên ống lá hành",
                        "Vết đốm lan rộng thành hình elip màu nâu đen tâm có lớp bột mốc sẫm như nhung",
                        "Cả ống lá bị cháy khô cong queo gục xuống gốc làm giảm năng suất củ nghiêm trọng"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với vết chích hút sâu dòi đục lá: Vết dòi đục tạo đường hầm ngoằn ngoèo trong ruột ống lá; đốm Stemphylium tạo mảng cháy nâu thâm có phấn nấm đen mịn.",
                    "kiem_tra_thuc_dia": "Lấy ngón tay bóp ống lá hành tại vết cháy thấy giòn rụm mục xơ bột đen dính tay.",
                    "phac_do_vietgap": {
                        "canh_tac": "Tưới nước giếng ngọt tưới mát luống hành vào buổi sáng sớm rửa trôi sương muối biển; bón phân kali tăng độ cứng cáp biểu bì ống lá.",
                        "sinh_hoc": "Phun dịch tỏi ớt lên men kết hợp nấm đối kháng Chaetomium.",
                        "khuyen_cao_chuyen_gia": "Phun phòng thuốc hoạt chất Difenoconazole, Tebuconazole hoặc Azoxystrobin định kỳ vào mùa gió đông bắc sương mù."
                    }
                },
                {
                    "ten_benh": "Bệnh Thối nhũn vi khuẩn củ hành tím",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Vi khuẩn",
                        "ten_khoa_hoc": "Pectobacterium carotovorum subsp. carotovorum"
                    },
                    "trieu_chung_dien_hinh": [
                        "Ống lá hành bị úng nước rũ mềm nhũn từ cổ củ trở lên",
                        "Các lớp vảy củ bên trong bị thối nhũn chảy nước nhầy bốc mùi hôi thối nồng nặc",
                        "Củ hành trong kho bảo quản bị thối rỗng ruột chỉ còn lớp vỏ lụa khô bên ngoài"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với thối củ do nấm: Thối vi khuẩn mô sũng nước chảy dịch nhớt bốc mùi khắm tanh gay gắt; thối nấm khô xác teo tóp có bột mốc phấn.",
                    "kiem_tra_thuc_dia": "Bóp nhẹ củ hành thấy xẹp lún ngón tay ứa ra nước nhờn màu vàng đục bốc mùi khó chịu xộc vào mũi.",
                    "phac_do_vietgap": {
                        "canh_tac": "Thu hoạch hành vào ngày nắng ráo, phơi tái vỏ rễ 3-5 nắng giàn trước khi bó củ treo bảo quản nơi khô ráo.",
                        "sinh_hoc": "Rải vôi bột khử khuẩn đất giồng cát tỷ lệ 30-40kg/công đất trước khi trồng.",
                        "khuyen_cao_chuyen_gia": "Phun phòng gốc thân bằng hoạt chất Bismerthiazol, Oxolinic acid hoặc Kasugamycin khi gặp mưa trái mùa."
                    }
                }
            ]
        },
        {
            "id": "crop_305",
            "topic": "Rau_Cu_Gia_Vi_Va_Nam",
            "name_vi": "Cà Rốt Đà Lạt",
            "scientific_name": "Daucus carota L. subsp. sativus",
            "dia_ban_pho_bien": ["Đà Lạt", "Đơn Dương - Lâm Đồng", "Hải Dương", "Bắc Ninh"],
            "dac_tinh_sinh_thai": "Cây lấy củ rễ cọc màu cam đỏ rực rỡ giàu beta-carotene, thịt củ giòn ngọt mọng nước, thích hợp tầng đất thịt nhẹ tơi xốp sâu trên 40cm không lẫn sỏi đá.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Cháy lá nấm Alternaria cà rốt (Alternaria Leaf Blight)",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Alternaria dauci"
                    },
                    "trieu_chung_dien_hinh": [
                        "Mép lá chét non xuất hiện các đốm nâu đen nhỏ có quầng vàng bao quanh",
                        "Vết đốm lan rộng làm toàn bộ tán lá lông chim của cà rốt bị khô cháy xém như bị hơ qua lửa",
                        "Cuống lá bị thâm đen gãy gục khiến khi thu hoạch nhổ củ cuống bị đứt rời khỏi củ"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với đốm lá Cercospora (Cercospora carotae): Alternaria tấn công lá già trước mép lá cháy khô nâu đen; Cercospora tấn công lá non có tâm màu xám trắng viền nâu đỏ.",
                    "kiem_tra_thuc_dia": "Dùng tay cầm túm cuống lá giật nhẹ thấy cuống lá giòn đứt ngang cổ củ không nhổ nổi củ cà rốt lên.",
                    "phac_do_vietgap": {
                        "canh_tac": "Gieo hạt thưa mật độ luống vừa phải, không tưới đẫm vào chiều tối; luân canh với bắp hoặc đậu đỗ.",
                        "sinh_hoc": "Phun phòng nấm đối kháng Trichoderma kết hợp nano đồng sinh học.",
                        "khuyen_cao_chuyen_gia": "Phun hoạt chất Iprodione, Chlorothalonil hoặc Difenoconazole khi chớm thấy mép lá có chấm cháy nâu."
                    }
                },
                {
                    "ten_benh": "Bệnh Tuyến trùng nốt sưng rễ củ cà rốt (Root-knot Nematode)",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Tuyến trùng",
                        "ten_khoa_hoc": "Meloidogyne spp."
                    },
                    "trieu_chung_dien_hinh": [
                        "Củ cà rốt bị biến dạng sần sùi méo mó, mọc ra nhiều rễ nhánh tua tủa chẻ hai chẻ ba",
                        "Trên thân củ và rễ phụ xuất hiện các khối u sần hạt cục tròn gồ ghề làm củ mất hoàn toàn giá trị thương phẩm",
                        "Cây trên mặt đất còi cọc vàng úa cằn cỗi dù được bón phân đầy đủ"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với củ chẻ do đất rắn nghẹt sỏi: Tuyến trùng tạo các hạt nốt sưng u cục sần sùi rõ rệt; củ nghẹt sỏi đá chỉ bị cong queo nhưng vỏ củ vẫn nhẵn nhụi.",
                    "kiem_tra_thuc_dia": "Rửa sạch củ cà rốt thấy các nốt sưng cục tròn dính liền vào thân củ, dùng móng tay bóc nốt sưng soi kính lúp thấy con tuyến trùng cái hình quả lê màu trắng đục.",
                    "phac_do_vietgap": {
                        "canh_tac": "Trồng luân canh cúc vạn thọ (Tagetes erecta) để tiết hoạt chất diệt tuyến trùng tự nhiên trong đất; cày ải phơi khô đất mùa khô.",
                        "sinh_hoc": "Tưới chế phẩm nấm ký sinh trứng tuyến trùng Paecilomyces lilacinus hoặc nấm bẫy tuyến trùng Arthrobotrys oligospora.",
                        "khuyen_cao_chuyen_gia": "Xử lý đất trước khi gieo hạt bằng hoạt chất sinh học Abamectin hoặc Fluopyram theo đúng quy trình VietGAP."
                    }
                }
            ]
        }
    ]
    
    # 60 additional crops for Module 4: crop_306 to crop_365
    raw_list_4 = [
        ("crop_306", "Súp Lơ Xanh Broccoli Đà Lạt", "Brassica oleracea var. italica", ["Lâm Đồng", "Hải Dương"],
         "Cây súp lơ xanh bông chùm ngọc bích giàu sulforaphane chống ung thư, phát triển tốt ở nhiệt độ mát mẻ 15-20 độ C.",
         "Bệnh Thối đen súp lơ xanh do vi khuẩn", "Vi khuẩn", "Xanthomonas campestris pv. campestris", "Rất cao",
         "Mép lá xuất hiện vết cháy hình chữ V màu vàng nâu gân lá chuyển màu đen mun, hoa bông bị thối thâm từng vạt.",
         "Phân biệt với thối nấm: Vi khuẩn làm đen bó mạch dẫn chữ V sắc nét và hôi chua nhớt.",
         "Cắt ngang cuống lá thấy các chấm đen bó mạch dẫn xếp tròn viền.",
         "Phun trừ vi khuẩn bằng Kasugamycin hoặc Thiodiazole copper."),
        
        ("crop_307", "Súp Lơ Trắng", "Brassica oleracea var. botrytis", ["Lâm Đồng", "Vĩnh Phúc", "Hải Dương"],
         "Bông súp lơ trắng nõn nà dày đặc, cùi ngọt bở giàu vitamin C và chất xơ, cây sinh trưởng ưa đất thịt xốp giàu hữu cơ.",
         "Bệnh Cháy lá sương mai súp lơ", "Nấm", "Peronospora parasitica", "Cao",
         "Mặt trên lá có đốm vàng góc cạnh, mặt dưới lá phủ lớp mốc tơ màu xám trắng, bông hoa bị thâm nám loang lổ.",
         "Phân biệt với thán thư: Sương mai có góc cạnh hạn chế bởi gân lá và mốc xám mặt dưới.",
         "Sờ mặt dưới lá thấy nhung mịn sương mốc bám.",
         "Phun phòng hoạt chất Metalaxyl-M hoặc Mancozeb định kỳ."),
        
        ("crop_308", "Bắp Cải Tím Đà Lạt", "Brassica oleracea var. capitata f. rubra", ["Lâm Đồng", "Hà Nội"],
         "Bắp cải cuộn chặt màu đỏ tím thẫm chứa hàm lượng anthocyanin cực cao, giòn ngọt dùng ăn sống salad và xào nấu cao cấp.",
         "Bệnh Sưng rễ bắp cải (Clubroot)", "Nguyên sinh động vật", "Plasmodiophora brassicae", "Rất cao",
         "Rễ cái và rễ con sưng phồng to thành các khối u bướu hình chùy quái dị, cây còi cọc héo rũ giữa trưa.",
         "Phân biệt với nốt sưng tuyến trùng: Clubroot u bướu khổng lồ dính liền củ rễ như củ gừng; tuyến trùng chỉ có nốt tròn nhỏ li ti.",
         "Nhổ gốc bắp cải thấy bộ rễ biến thành khối u phình to không có rễ tơ.",
         "Nâng độ pH đất lên trên 7.2 bằng vôi bột, tưới Fluazinam khử mầm đất."),
        
        ("crop_309", "Cải Thảo Đà Lạt", "Brassica rapa subsp. pekinensis", ["Lâm Đồng", "Hải Dương"],
         "Bắp cải thảo cuộn thon dài lá màu xanh nhạt lòng vàng óng, nguyên liệu chính làm kim chi và các món lẩu bổ dưỡng.",
         "Bệnh Thối nhũn vi khuẩn cải thảo", "Vi khuẩn", "Pectobacterium carotovorum", "Rất cao",
         "Gốc bẹ lá sát mặt đất bị ủng nước nhớt nhũn bốc mùi khắm thối kinh khủng, cả bắp cải sụp đổ trong 1-2 ngày.",
         "Phân biệt với cháy sương mai: Thối nhũn vi khuẩn mô nát chảy nhớt thối nồng nặc không có sợi nấm.",
         "Bóp vào bẹ lá thấy nước nhầy đục ứa ra tanh khắm.",
         "Tưới gốc Kasugamycin, rải vôi khử trùng luống sau mưa."),
        
        ("crop_310", "Cải Xoăn Kale Đà Lạt", "Brassica oleracea var. sabellica", ["Lâm Đồng", "Sa Pa"],
         "Nữ hoàng rau xanh phiến lá quăn xoăn tít màu xanh thẫm, giàu vitamin K, canxi và chất chống oxy hóa, xu hướng sống khỏe.",
         "Bệnh Đốm vòng Alternaria lá xoăn", "Nấm", "Alternaria brassicicola", "Cao",
         "Các đốm tròn màu nâu xám có các vòng tròn đồng tâm nổi rõ trên các nếp gấp xoăn của phiến lá.",
         "Phân biệt với sâu cắn: Đốm vòng khô giòn có viền đen sắc nét không làm rách xơ viền lá.",
         "Bóp nhẹ đốm tròn giòn vỡ vụn rơi bột đen.",
         "Phun phòng thuốc sinh học Nano Bạc hoặc nấm Chaetomium."),
        
        ("crop_311", "Ớt Chuông Đà Lạt", "Capsicum annuum var. grossum", ["Lâm Đồng", "Đơn Dương"],
         "Ớt ngọt quả hình vuông dày cùi màu đỏ, vàng, cam rực rỡ, vị ngọt giòn không cay, canh tác công nghệ cao trong nhà kính.",
         "Bệnh Thán thư thối trái ớt chuông", "Nấm", "Colletotrichum acutatum", "Rất cao",
         "Vỏ trái xuất hiện đốm tròn lõm hình lòng chảo màu nâu sẫm, tâm đốm ứa các giọt dịch màu cam hồng nhầy xếp vòng tròn.",
         "Phân biệt với cháy nắng cùi: Thán thư có vòng tròn đồng tâm lõm sâu và dịch nấm cam; cháy nắng màu trắng bạc khô phẳng lì.",
         "Ấn nhẹ ngón tay vào vết lõm thấy mềm ứ mủ nấm màu cam dính tay.",
         "Phun phòng luân phiên Azoxystrobin + Difenoconazole hoặc Mancozeb."),
        
        ("crop_312", "Cà Chua Bi Cherry Đà Lạt", "Solanum lycopersicum var. cerasiforme", ["Lâm Đồng", "Lạc Dương"],
         "Cà chua chùm quả tròn nhỏ bóng đỏ vàng ngọt đậm độ brix cao 9-11%, trồng giá thể tưới nhỏ giọt tự động công nghệ cao.",
         "Bệnh Mốc lá cà chua bi (Leaf Mould)", "Nấm", "Passalora fulva (Cladosporium fulvum)", "Cao",
         "Mặt trên lá có đốm vàng nhạt loang lổ, mặt dưới lá phủ lớp nấm nhung mịn màu nâu xanh ôliu sẫm.",
         "Phân biệt với sương mai: Mốc lá có lớp nỉ màu nâu ôliu mặt dưới; sương mai mốc màu trắng tro và thối úng quả.",
         "Miết ngón tay mặt dưới lá thấy lớp bột mịn như phấn nhung xanh sẫm dính ngón.",
         "Hạ ẩm độ nhà màng, phun phòng thuốc gốc Fluopyram hoặc Difenoconazole."),
        
        ("crop_313", "Cà Chua Beefsteak Đà Lạt", "Solanum lycopersicum L.", ["Lâm Đồng", "Đức Trọng"],
         "Cà chua quả khổng lồ nặng 300-500g cùi dày đặc ít hạt, nhiều thịt ngọt thanh chuyên dùng thái lát kẹp burger và làm sốt cao cấp.",
         "Bệnh Héo xanh vi khuẩn cà chua Beef", "Vi khuẩn", "Ralstonia solanacearum", "Rất cao",
         "Cây đang sum suê trái xanh bỗng rũ lá héo rục chỉ sau một buổi trưa nắng gắt, lá vẫn giữ màu xanh tươi.",
         "Phân biệt với héo Fusarium: Cắt cành nhúng nước thấy dòng khói trắng tuôn ra ngay; nấm không tuôn dịch đục tức thì.",
         "Thử nghiệm dòng dịch vi khuẩn trong cốc thủy tinh sau 30 giây.",
         "Ghép gốc cà chua cà dại kháng bệnh, tưới vi khuẩn đối kháng Bacillus subtilis."),
        
        ("crop_314", "Bí Ngòi Xanh Đà Lạt", "Cucurbita pepo L.", ["Lâm Đồng", "Đơn Dương"],
         "Quả thon dài màu xanh đậm vỏ bóng mịn thịt giòn ngọt, thu hoạch trái non chế biến xào nấu nướng BBQ thanh mát.",
         "Bệnh Phấn trắng bí ngòi", "Nấm", "Podosphaera xanthii", "Cao",
         "Cả hai mặt lá và cuống quả phủ lớp phấn trắng xóa như rắc bột mì làm lá vàng giòn rụng sớm.",
         "Phân biệt với sương mai giả: Phấn trắng nằm cả mặt trên mặt dưới dạng bột khô; sương mai giả góc cạnh vàng mặt trên nấm tím xám mặt dưới.",
         "Xoa ngón tay lên lá dính bột trắng phấn dễ lau sạch.",
         "Phun Nano Lưu huỳnh hoặc chế phẩm Trichoderma an toàn sinh học."),
        
        ("crop_315", "Củ Dền Đỏ Đà Lạt", "Beta vulgaris L.", ["Lâm Đồng", "Đà Lạt"],
         "Củ tròn ruột đỏ thẫm huyết dụ giàu chất sắt và nitrat tự nhiên tăng cường oxy máu, lá gân đỏ rực đẹp mắt.",
         "Bệnh Đốm mắt chim lá củ dền", "Nấm", "Cercospora beticola", "Cao",
         "Vết đốm hình tròn nhỏ tâm xám trắng viền đỏ tím nổi bật như mắt chim rải rác khắp tán lá.",
         "Phân biệt với bọ trĩ: Đốm mắt chim có viền đỏ tím sắc nét và tâm khô thủng màng rách lỗ chỗ.",
         "Soi ngược nắng thấy đốm có tâm xám mỏng như tờ giấy bóng.",
         "Phun luân phiên Chlorothalonil hoặc Difenoconazole phòng trị."),
        
        ("crop_316", "Cần Tây Đà Lạt", "Apium graveolens L.", ["Lâm Đồng", "Đức Trọng"],
         "Thân bẹ cần tây to mập giòn ngọt màu xanh non chứa nhiều apigenin ép nước detox giảm cân thanh lọc cơ thể cực tốt.",
         "Bệnh Cháy lá sớm cần tây (Early Blight)", "Nấm", "Cercospora apii", "Cao",
         "Đốm bệnh tròn màu vàng nâu trên bẹ và lá, khi bệnh rộ các đốm liên kết làm bẹ cần tây bị thâm đen giòn gãy.",
         "Phân biệt với thối hạch: Cercospora không có tơ nấm trắng và hạch đen to như hạt đỗ.",
         "Bẻ cọng bẹ cần tây thấy gãy giòn ở vết thâm xơ mục.",
         "Phun ngừa hoạt chất Difenoconazole hoặc Booc-đô 1% định kỳ."),
        
        ("crop_317", "Măng Tây Xanh Ninh Thuận", "Asparagus officinalis L.", ["Ninh Thuận", "Bình Thuận", "Quảng Nam"],
         "Hoàng đế dinh dưỡng đọt non giòn ngọt mọc từ thân rễ ngầm trên đất cát pha, giàu axit folic và khoáng chất quý giá.",
         "Bệnh Khô thân thán thư măng tây", "Nấm", "Phomopsis asparagi (Stem Blight)", "Rất cao",
         "Thân cây xuất hiện các vết đốm hình thoi màu nâu xám viền đỏ thẫm có vô số chấm đen nhỏ li ti là ổ bào tử nấm.",
         "Phân biệt với rỉ sắt: Phomopsis tạo vết lõm thoi xám có chấm đen gồ ghề; rỉ sắt tạo mụn mủ nứt bột da cam rỉ sét.",
         "Miết tay lên thân cảm nhận vết thâm lõm giòn gãy cành măng.",
         "Cắt tỉa cành mẹ định kỳ, phun luân phiên Difenoconazole + Azoxystrobin."),
        
        ("crop_318", "Ớt Chỉ Thiên Bến Tre", "Capsicum frutescens L.", ["Bến Tre", "Tiền Giang", "Đồng Tháp"],
         "Ớt chỉ thiên quả mọc chổng ngược lên trời cay xé lưỡi, vỏ mỏng đỏ chót giàu capsaicin dùng làm gia vị tươi và tương ớt xuất khẩu.",
         "Bệnh Khảm lá xoăn ngọn ớt do virus", "Virus", "Chilli veinal mottle virus (ChiVMV)", "Cao",
         "Đọt non bị co rút quăn queo, phiến lá lốm đốm khảm vàng loang lổ gân xanh nổi cộm, hoa rụng không kết quả.",
         "Phân biệt với bọ trĩ: Virus gây khảm màu loang lổ xanh vàng dị dạng lá; bọ trĩ lá có vệt bạc sần sùi cạo rách mép.",
         "Sờ ngọn đọt thấy lá dày cứng giòn dễ gãy xoắn ốc.",
         "Diệt trừ bọ trĩ và rệp muội môi giới bằng dầu khoáng và Pymetrozine."),
        
        ("crop_319", "Ớt Sừng Vàng Châu Đốc", "Capsicum annuum L.", ["An Giang", "Đồng Tháp"],
         "Ớt sừng quả dài to màu vàng cam óng ả cay thơm nồng đượm, trang trí món ăn và dùng làm gia vị đặc sản miền Tây.",
         "Bệnh Thối ướt hoa trái non Choanephora", "Nấm", "Choanephora cucurbitarum", "Cao",
         "Hoa và trái non bị úng nước thối đen phủ lớp nấm mốc tua tủa như các que diêm đầu đính hạt đen tròn óng ánh.",
         "Phân biệt với thán thư: Choanephora có các sợi nấm đứng đầu mang hạt đen óng như đầu kim ghim; thán thư có đĩa cành cam bết phẳng.",
         "Soi kính lúp thấy rừng que diêm đen lấp lánh trên chóp quả non thối.",
         "Phun chế phẩm vi sinh kháng nấm hoặc Copper Hydroxide."),
        
        ("crop_320", "Gừng Gió Tây Bắc", "Zingiber zerumbet (L.) Roscoe ex Sm.", ["Sơn La", "Hòa Bình", "Yên Bái"],
         "Gừng gió củ thơm nồng vị cay đắng ấm áp, hoa đỏ chót hình bắp ngô chứa tinh chất quý chữa đau nhức xương khớp và cảm hàn.",
         "Bệnh Thối củ gừng do tuyến trùng và nấm", "Tổ hợp", "Meloidogyne spp. & Fusarium spp.", "Cao",
         "Củ gừng dưới đất bị các vết thâm nâu sần sùi ruột thâm đen bốc mùi hăng chua, lá vàng rực từ chóp xuống.",
         "Phân biệt với cháy nắng: Thối củ làm thối nhũn ruột gừng từ trong củ nhánh lây lan cả bụi.",
         "Bẻ củ gừng thấy xơ thịt bên trong màu nâu đen có mùi chua nồng.",
         "Xử lý hom củ giống bằng nước ấm 50 độ C và rải Trichoderma vào rãnh."),
        
        ("crop_321", "Gừng Trâu Đắk Lắk", "Zingiber officinale Roscoe", ["Đắk Lắk", "Gia Lai", "Bình Phước"],
         "Gừng củ to nhiều nhánh thịt vàng ngà nhiều nước ít xơ, chuyên thu hoạch xuất khẩu và làm mứt gừng cay ấm truyền thống.",
         "Bệnh Héo xanh vi khuẩn thối mềm củ gừng", "Vi khuẩn", "Ralstonia solanacearum", "Rất cao",
         "Lá gừng cuộn tròn úa vàng rũ nhanh chóng, củ trong đất bị thối nhũn chảy nước nhờn mùi khắm hôi hám.",
         "Phân biệt với héo nấm: Vi khuẩn làm củ gừng ủng nước nhớt nhầy bóp xẹp ngay ứa dịch trắng đục.",
         "Ấn nhẹ ngón tay vào nhánh gừng thấy nước đục xì ra nhớt nhầy bốc mùi khắm.",
         "Lên luống thoát nước tuyệt đối, tưới phòng Kasugamycin kết hợp vôi bột."),
        
        ("crop_322", "Nghệ Vàng Chí Tân Khoái Châu", "Curcuma longa L.", ["Hưng Yên", "Hà Nam", "Nghệ An"],
         "Thủ phủ nghệ Chí Tân đất bãi sông Hồng phù sa màu mỡ, hàm lượng curcumin vàng óng đỉnh cao chuyên tinh bột nghệ dược liệu.",
         "Bệnh Đốm mắt cua lá nghệ", "Nấm", "Taphrina maculans", "Trung bình",
         "Phiến lá xuất hiện hàng trăm đốm nhỏ màu nâu vàng viền nâu sẫm như mắt cua làm lá khô giòn sớm.",
         "Phân biệt với cháy lá nấm: Đốm Taphrina nhỏ đều đặn hình bầu dục li ti không loang mảng to.",
         "Mặt lá ram ráp khi vuốt ngón tay qua vết đốm cua nhỏ.",
         "Phun phòng Mancozeb hoặc Booc-đô 1% sau các đợt mưa rào."),
        
        ("crop_323", "Nghệ Đen Hải Hậu", "Curcuma zedoaria (Christm.) Roscoe", ["Nam Định", "Thái Bình", "Thanh Hóa"],
         "Nghệ đen củ ruột tím xám thẫm mùi thơm hăng đặc trưng, hoạt chất quý chữa đau dạ dày, hành khí tiêu tích cổ truyền.",
         "Bệnh Thối rễ thối củ nghệ đen", "Nấm", "Pythium aphanidermatum", "Cao",
         "Củ nghệ non bị thối ủng nước màu nâu đen, vỏ củ bong tróc làm bẹ lá vàng úa đổ rạp trơ trọi.",
         "Phân biệt với củ già sinh lý: Bệnh nấm làm củ nhũn nhão xơ xác và không đâm mầm mới được.",
         "Cầm cọng thân kéo nhẹ thấy đứt lìa khỏi củ bị thối nhũn nước.",
         "Phun tưới gốc bằng Metalaxyl hoặc Fosetyl-Al bảo vệ mầm củ non."),
        
        ("crop_324", "Riềng Nếp Thanh Hóa", "Alpinia galanga (L.) Willd.", ["Thanh Hóa", "Nghệ An", "Hòa Bình"],
         "Riềng nếp củ to vỏ hồng thịt trắng cay thơm nồng đậm, gia vị không thể thiếu cho các món chả nướng và riềng mẻ cổ truyền.",
         "Bệnh Gỉ sắt lá riềng nếp", "Nấm", "Puccinia spp.", "Trung bình",
         "Mặt dưới phiến lá nổi các mụn mủ màu nâu đỏ rỉ sét làm lá cằn cỗi vàng cháy rìa mép.",
         "Phân biệt với đốm nâu: Mụn gỉ sắt nổi cộm rỉ bột phấn màu đỏ cam dính tay.",
         "Quẹt ngón tay thấy bám bột đỏ cam rỉ sắt rõ nét.",
         "Cắt tỉa lá già thông thoáng, phun Hexaconazole phòng trừ."),
        
        ("crop_325", "Sả Chanh Tây Ninh", "Cymbopogon citratus (DC.) Stapf", ["Tây Ninh", "Đồng Nai", "Bình Thuận"],
         "Bụi sả to cọng mập tinh dầu chanh citral thơm ngát, gia vị món nướng lẩu và chưng cất tinh dầu xua đuổi muỗi côn trùng.",
         "Bệnh Đốm sọc đỏ lá sả chanh", "Nấm", "Curvularia spp.", "Trung bình",
         "Các sọc hẹp dài màu đỏ tía chạy dọc bẹ và phiến lá sả làm chóp lá khô quắt rực vàng.",
         "Phân biệt với khô chóp do hạn: Vết nấm sọc đỏ có viền rõ rệt và xuất hiện đốm đen nhỏ sinh bào tử.",
         "Sờ mép lá sả thấy ráp khô rách tả tơi mép lá.",
         "Cắt gốc thu hoạch dọn sạch tàn dư, phun phòng chế phẩm gốc Đồng."),
        
        ("crop_326", "Sả Java Tuyên Quang", "Cymbopogon winterianus Jowitt ex Bor", ["Tuyên Quang", "Yên Bái", "Lào Cai"],
         "Cây sả thân tím hàm lượng tinh dầu citronellal cao chuyên dùng trong công nghiệp dược mỹ phẩm và xịt phòng đuổi muỗi.",
         "Bệnh Rỉ sắt lá sả Java", "Nấm", "Puccinia nakanishikii", "Trung bình",
         "Vô số mụn mủ nhỏ li ti màu vàng nâu nổi dày đặc hai mặt lá làm lá sả khô xác trơ trụi.",
         "Phân biệt với đốm sọc: Gỉ sắt có ổ mụn nứt bột phấn nâu đỏ bám tay dơ bẩn.",
         "Vuốt lá sả dính đầy bụi phấn nâu đỏ gỉ sét.",
         "Phun phòng thuốc hoạt chất Azoxystrobin hoặc Difenoconazole."),
        
        ("crop_327", "Hành Lá Hương Gốc Trắng", "Allium fistulosum L.", ["Hải Dương", "Bắc Giang", "Hà Nội", "Tiền Giang"],
         "Hành lá gia vị thiết yếu hàng ngày, ống lá xanh giòn gốc trắng nõn nà cay thơm hấp dẫn mọi món phở xào canh.",
         "Bệnh Đốm vòng Alternaria hành lá", "Nấm", "Alternaria porri", "Cao",
         "Ống lá xuất hiện vết thoi lõm màu nâu tím có vòng đồng tâm, ống lá bị gãy gập ngang thân khô cháy.",
         "Phân biệt với sâu xanh đục ống: Nấm có vết tím lõm vòng tròn; sâu có lỗ cắn nhỏ và phân sâu trong ruột ống.",
         "Bóp ống lá tại vết thâm tím thấy giòn gãy cụp.",
         "Phun Iprodione hoặc Chlorothalonil luân phiên ngừa kháng thuốc."),
        
        ("crop_328", "Hẹ Lá Thanh Trì", "Allium tuberosum Rottler ex Spreng.", ["Hà Nội", "Bắc Ninh", "Vĩnh Long"],
         "Hẹ lá dẹt giòn ngọt thơm dịu bồi bổ thận dương tiêu đờm giải nhiệt, nguyên liệu nấu canh hẹ đậu hũ trứ danh.",
         "Bệnh Gỉ sắt lá hẹ", "Nấm", "Puccinia allii", "Trung bình",
         "Các mụn mủ màu vàng cam nổi cộm trên phiến lá dẹt làm lá hẹ khô cháy vàng đầu lá.",
         "Phân biệt with thiếu đạm: Gỉ sắt có mụn mủ cộm bột cam dính tay; thiếu đạm lá vàng đều không nổi mụn.",
         "Miết lá dính bột vàng rỉ sét rõ rệt.",
         "Cắt sát gốc thu hoạch dọn cỏ, phun nấm đối kháng Chaetomium."),
        
        ("crop_329", "Ngò Gai Răng Cưa Củ Chi", "Eryngium foetidum L.", ["TP. Hồ Chí Minh", "Tây Ninh", "Bình Dương"],
         "Rau mùi tàu phiến lá có răng cưa nhọn thơm nồng nàn vị cay ấm không thể thiếu trong bát phở bò truyền thống.",
         "Bệnh Thán thư thối đen lá ngò gai", "Nấm", "Colletotrichum spp.", "Cao",
         "Rìa mép răng cưa xuất hiện các vết thâm đen lõm ướt lan nhanh làm cả phiến lá bị thối rữa màu nâu đen.",
         "Phân biệt với cháy nắng: Thán thư lan từ mép răng cưa vào gân chính kèm viền thâm ướt sũng.",
         "Sờ phiến lá mềm nhũn nhớt dính khi gặp mưa dầm.",
         "Làm giàn lưới che bớt nắng gắt và mưa to, phun Antracol hoặc Mancozeb."),
        
        ("crop_330", "Rau Húng Quế Trà Quế Hội An", "Ocimum basilicum L.", ["Quảng Nam", "Đà Nẵng", "TP. Hồ Chí Minh"],
         "Làng rau Trà Quế nổi tiếng bón rong biển sông Cổ Cò, húng quế thơm ngào ngạt vị cay ngọt tinh tế dùng ăn kèm phở và gỏi cuốn.",
         "Bệnh Đốm đen thối cành húng quế", "Nấm", "Colletotrichum destructivum", "Cao",
         "Cành thân và phiến lá xuất hiện các vết thâm đen khô lõm, ngọn non bị gãy gục đen thui rụng trụi lá.",
         "Phân biệt với sâu cuốn lá: Nấm làm thâm đen cọng thân khô giòn không có tơ cuốn lá sâu.",
         "Bẻ cành húng quế thấy giòn gãy ngang khớp đen thâm.",
         "Tưới nước gốc không phun lên lá, phun phòng dịch chiết tỏi ớt sinh học."),
        
        ("crop_331", "Bạc Hà Nhật Âu Á", "Mentha piperita L.", ["Lâm Đồng", "Hưng Yên"],
         "Cây bạc hà cay thơm the mát chứa tinh chất menthol cực cao làm kẹo sô-cô-la trà thơm và tinh dầu thư giãn sảng khoái.",
         "Bệnh Gỉ sắt bạc hà cay", "Nấm", "Puccinia menthae", "Cao",
         "Mặt dưới lá xuất hiện các chấm mụn mủ màu nâu cam sau thành nâu đen làm rụng lá hàng loạt trơ cành cây.",
         "Phân biệt với nhện đỏ: Gỉ sắt có mụn mủ bột phấn dính ngón tay rõ nét.",
         "Chạm tay mặt dưới lá dính bột nâu đỏ rỉ sắt.",
         "Phun luân phiên Nano Lưu huỳnh hoặc nấm đối kháng Trichoderma."),
        
        ("crop_332", "Tía Tô Xanh Nhật Shiso", "Perilla frutescens var. crispa", ["Bắc Giang", "Hưng Yên", "Hà Nội"],
         "Tía tô xanh nhập khẩu chuyên xuất khẩu sang Nhật ăn kèm sashimi cá hồi, thơm thanh cay nhẹ lá dày răng cưa sắc bén.",
         "Bệnh Đốm mắt cua lá tía tô Shiso", "Nấm", "Cercospora perillae", "Cao",
         "Phiến lá xuất hiện các vết đốm tròn tâm xám mỏng viền nâu đỏ làm thủng lỗ chỗ mặt lá mất tiêu chuẩn xuất khẩu.",
         "Phân biệt với bọ nhảy cắn: Bệnh nấm có viền nâu đỏ và màng hoại tử mỏng trước khi rách thủng.",
         "Soi lá thấy các lỗ thủng viền nâu sẫm trên bề mặt lá xanh bóng.",
         "Phun phòng thuốc vi sinh Bacillus subtilis an toàn không để lại dư lượng."),
        
        ("crop_333", "Tía Tô Tía Láng Hà Nội", "Perilla frutescens (L.) Britton", ["Hà Nội", "Hưng Yên", "Bắc Ninh"],
         "Tía tô màu tím tía cả hai mặt thơm nồng nàn giải cảm xông hơi và nấu ốc chuối đậu truyền thống đất kinh kỳ.",
         "Bệnh Cháy lá lở cổ rễ tía tô tía", "Nấm", "Rhizoctonia solani", "Cao",
         "Cổ rễ sát đất bị teo thắt thâm nâu cây héo gục rũ, lá chân xuất hiện mảng cháy loang lổ viền xám tro.",
         "Phân biệt với úng nước: Bệnh nấm làm lở loét khuyết sâu lớp vỏ cổ rễ có sợi tơ nấm trắng bao quanh.",
         "Nhổ nhẹ cây tía tô thấy đứt ngang cổ rễ teo thắt khô xác.",
         "Tưới Trichoderma vào gốc định kỳ, vun gốc cao ráo thoáng nước."),
        
        ("crop_334", "Kinh Giới Đông Triều", "Elsholtzia ciliata (Thunb.) Hyl.", ["Quảng Ninh", "Hải Dương", "Hà Nội"],
         "Kinh giới hoa tím nhạt lá thơm the cay làm rau sống ăn kèm bún đậu mắm tôm và giải cảm sốt dị ứng nổi mề đay.",
         "Bệnh Đốm lá thán thư kinh giới", "Nấm", "Colletotrichum spp.", "Trung bình",
         "Phiến lá có đốm nâu đen hình bầu dục viền vàng nhạt, cành non bị thâm đen rũ ngọn khô xác.",
         "Phân biệt với rệp muội: Không có chất dính mật ngọt và nấm bồ hóng đen xì của rệp.",
         "Sờ mặt lá giòn khô ở vết thâm nâu rụng rách lỗ nhỏ.",
         "Phun thuốc Booc-đô 1% hoặc nano đồng thảo mộc an toàn."),
        
        ("crop_335", "Rau Răm Sông Bé", "Persicaria odorata (Lour.) Soják", ["Bình Dương", "Bình Phước", "TP. Hồ Chí Minh"],
         "Rau răm cay nồng ấm bụng lá thon dài điểm vệt tím chữ V, gia vị không thể tách rời của món trứng vịt lộn và gỏi gà xé phay.",
         "Bệnh Cháy lá sương mai rau răm", "Nấm", "Phytophthora spp.", "Cao",
         "Các mảng cháy úng nước màu nâu xám loang nhanh từ ngọn dây rau răm xuống gốc làm thối rụi cả luống sau mưa.",
         "Phân biệt với già úa: Nấm sương mai làm nhũn ướt thối rữa mềm nhũn cả cọng rau mùi thối rơm rạ mục.",
         "Cầm túm rau răm thấy nhũn nát chảy nước nâu nhớt dính tay.",
         "Tưới gốc Fosetyl-Al hoặc Ridomil Gold khi chớm có vạt rau úng thâm."),
        
        ("crop_336", "Diếp Cá Cần Thơ", "Houttuynia cordata Thunb.", ["Cần Thơ", "Tiền Giang", "Vĩnh Long"],
         "Rau diếp cá lá hình tim tanh nồng đặc trưng, vị chua mát thanh nhiệt giải độc chữa trĩ và kháng viêm cực mạnh.",
         "Bệnh Đốm tròn lá diếp cá", "Nấm", "Cercospora spp.", "Trung bình",
         "Mặt lá hình tim xuất hiện các đốm tròn màu nâu xám viền đỏ gạch làm lá vàng rụng sớm giảm sản lượng thu hái.",
         "Phân biệt với bọ cánh cứng cắn: Đốm nấm có màng hoại tử xám không phải vết cắn khuyết mép lá.",
         "Sờ mặt lá thấy giòn khô ở tâm đốm tròn.",
         "Phun dung dịch sinh học tỏi ớt gừng hoặc chế phẩm Trichoderma."),
        
        ("crop_337", "Rau Ngổ Hương Nam Bộ", "Limnophila aromatica (Lam.) Merr.", ["Long An", "Đồng Tháp", "An Giang"],
         "Rau ngổ thơm ngát nồng đượm gia vị nấu canh chua cá lóc miền Tây, thân xốp mềm mọc bò lan mé mương ruộng nước ngọt.",
         "Bệnh Thối nhũn gốc thân rau ngổ", "Vi khuẩn", "Pectobacterium spp.", "Cao",
         "Thân cọng ngổ ngâm nước bị úng thối nhũn chảy nước nhầy có mùi tanh khắm, cây rục rữa trôi dạt mặt nước.",
         "Phân biệt với dập nát cơ học: Vi khuẩn làm thối nhũn lan tỏa nhanh và có dịch nhờn bốc mùi khắm.",
         "Bóp cọng rau ngổ xẹp lép ứa ra nước nhờn tanh nồng.",
         "Thay tháo nước mương trong sạch, rải vôi khử trùng nguồn nước."),
        
        ("crop_338", "Thì Là Bắc Ninh", "Anethum graveolens L.", ["Bắc Ninh", "Hải Dương", "Hà Nội"],
         "Cây thì là lá lông chim mảnh mai hương thơm thì là quyến rũ không thể thiếu cho món chả cá Lã Vọng và canh riêu cá.",
         "Bệnh Lở cổ rễ thối gốc thì là", "Nấm", "Rhizoctonia solani", "Cao",
         "Cổ rễ sát đất bị teo thắt thâm nâu úng nước, cây thì là ngã rạp hàng loạt khi còn non mọng nước.",
         "Phân biệt với cây bị khô hạn: Bệnh lở cổ rễ vết thắt ngập úng màu nâu xơ xác dù đất vẫn ẩm ướt.",
         "Nhấc nhẹ cây thì là đứt lìa sát gốc rễ.",
         "Tưới phòng nấm đối kháng Trichoderma vào rãnh gieo hạt."),
        
        ("crop_339", "Xà Lách Cuộn Iceberg Đà Lạt", "Lactuca sativa var. capitata", ["Lâm Đồng", "Đơn Dương"],
         "Xà lách búp cuộn tròn giòn rụm thanh mát như tảng băng, giữ nước lâu chuyên dùng làm salad rau tươi sốt mayonnaise.",
         "Bệnh Cháy rìa lá vi khuẩn xà lách (Tipburn & Bacterial Blight)", "Vi khuẩn", "Pseudomonas cichorii", "Cao",
         "Mép lá non bên trong cuộn búp bị thâm đen úng nước nhớt nhầy rồi khô cháy đen mép lá.",
         "Phân biệt với thiếu canxi thuần túy: Vi khuẩn làm mép lá ứa dịch nhầy nhớt bốc mùi chua úng.",
         "Bóc búp xà lách thấy mép lá non bên trong bị dập nhầy thâm đen.",
         "Bổ sung Canxi-Bo qua lá, phun phòng Kasugamycin khi thời tiết ẩm ướt."),
        
        ("crop_340", "Xà Lách Romanie Đà Lạt", "Lactuca sativa var. longifolia", ["Lâm Đồng", "Đà Lạt"],
         "Xà lách lá thon dài dựng đứng cuống giòn ngọt đậm đà, món salad Caesar thượng hạng trong ẩm thực phương Tây.",
         "Bệnh Sương mai xà lách Romanie", "Nấm", "Bremia lactucae", "Rất cao",
         "Mặt trên lá xuất hiện các vệt đốm vàng góc cạnh bị gân lá chặn lại, mặt dưới phủ lớp nấm mốc trắng xốp như bông.",
         "Phân biệt với thiếu đạm: Sương mai có góc cạnh đa giác sắc nhọn và mốc trắng bông mặt dưới lá.",
         "Lật mặt dưới lá thấy lớp mốc tơ trắng bông xốp mịn màng.",
         "Phun luân phiên Metalaxyl-M, Dimethomorph hoặc Fosetyl-Al."),
        
        ("crop_341", "Xà Lách Mỡ Lollo Bionda", "Lactuca sativa L.", ["Lâm Đồng", "Hà Nội"],
         "Xà lách tán xòe mép lá xoăn gợn sóng màu xanh ngọc mềm mượt như mỡ gà, vị ngọt bùi không đắng ăn kèm thịt nướng.",
         "Bệnh Thối hạch mốc trắng xà lách (White Mould)", "Nấm", "Sclerotinia sclerotiorum", "Rất cao",
         "Gốc bẹ lá sát đất bị nhũn nước thâm nâu phủ lớp tơ nấm trắng muốt như bông gòn kèm các hạch nấm to bằng hạt đậu đen.",
         "Phân biệt với thối nhũn vi khuẩn: Thối hạch có các cục hạch đen cứng như phân chuột bám chặt trong lớp bông tuyết trắng.",
         "Cạy lớp tơ nấm trắng thấy các hạt hạch màu đen hình thoi rắn chắc.",
         "Nhổ bỏ cây bệnh tiêu hủy, phun Iprodione hoặc Boscalid vào gốc."),
        
        ("crop_342", "Cải Bẹ Xanh Dưa Bắc Giang", "Brassica juncea (L.) Czern.", ["Bắc Giang", "Hải Dương", "Hà Nội"],
         "Cải bẹ cọng to bản dày dặn vị cay nồng đặc trưng, chuyên dùng muối dưa cải chua vàng ươm giòn rụm kho cá thịt béo ngậy.",
         "Bệnh Đốm trắng lá cải bẹ dưa", "Nấm", "Pseudocercosporella capsellae", "Trung bình",
         "Mặt lá xuất hiện các đốm tròn nhỏ màu trắng bạc viền nâu mỏng làm lá lấm tấm trắng như phủ tàn thuốc lá.",
         "Phân biệt với rệp muội: Đốm nấm mỏng khô giòn không có sáp rệp bám và dịch đường ngọt.",
         "Soi ngược nắng thấy đốm trắng mỏng manh thủng lỗ nhỏ li ti.",
         "Phun phòng Booc-đô 1% hoặc nano lưu huỳnh an toàn sinh học."),
        
        ("crop_343", "Cải Ngọt Chồi Cần Thơ", "Brassica integrifolia (West) Rupr.", ["Cần Thơ", "Hậu Giang", "Vĩnh Long"],
         "Cải ngọt thân mập hoa vàng rực giòn ngọt thanh mát nấu canh tôm thịt và xào thịt bò thơm ngon bổ dưỡng.",
         "Bệnh Cháy lá sương mai cải ngọt", "Nấm", "Peronospora parasitica", "Cao",
         "Mặt trên lá có các vết vàng loang góc cạnh, sáng sớm mặt dưới phủ lớp màng mốc xám chì mỏng làm lá úa vàng khô lụi.",
         "Phân biệt với cháy nắng: Sương mai góc cạnh theo gân lá và mọc mốc tơ xám mặt dưới khi trời nhiều sương.",
         "Sờ mặt dưới lá thấy nhung mịn sương mốc bám đầu ngón tay.",
         "Phun phòng thuốc sinh học Nano Bạc hoặc hoạt chất Mancozeb."),
        
        ("crop_344", "Cải Thìa Chíp Hải Dương", "Brassica rapa subsp. chinensis", ["Hải Dương", "Hưng Yên", "Hà Nội"],
         "Cải bẹ trắng nõn cuống hình chiếc thìa muỗng giòn sần sật mọng nước, món cải thìa xào dầu hào thơm lừng bàn tiệc.",
         "Bệnh Đốm vòng Alternaria cải thìa", "Nấm", "Alternaria brassicae", "Cao",
         "Vết bệnh hình tròn màu nâu sẫm có các vòng tròn đồng tâm nổi rõ trên bẹ thìa và phiến lá xanh.",
         "Phân biệt với bọ nhảy cắn: Đốm vòng khô giòn có vòng đồng tâm đen; bọ nhảy cắn thủng lỗ trơn nhẵn mép xanh.",
         "Bóp nhẹ vết đốm giòn tan vụn rơi bột đen.",
         "Phun Difenoconazole hoặc Chlorothalonil đúng thời gian cách ly."),
        
        ("crop_345", "Cải Cúc Tần Ô Đồng Nai", "Glebionis coronaria (L.) Cass. ex Spach", ["Đồng Nai", "TP. Hồ Chí Minh", "Hà Nội"],
         "Cây rau tần ô lá xẻ răng cưa hương thơm thảo mộc dịu nhẹ, vị ngọt đắng thanh mát nấu canh thịt băm và nhúng lẩu cá kèo.",
         "Bệnh Sương mai rau tần ô", "Nấm", "Bremia lactucae", "Cao",
         "Mặt dưới phiến lá phủ lớp phấn trắng xám mờ nhạt, phiến lá úa vàng khô héo rũ rượi từng vạt luống.",
         "Phân biệt với thiếu vi lượng: Sương mai làm rũ mềm lá và có sợi nấm mốc mặt dưới.",
         "Vuốt nhẹ mặt dưới phiến lá dính bột mốc mỏng xám tro.",
         "Phun phòng chế phẩm sinh học Trichoderma định kỳ 5 ngày/lần."),
        
        ("crop_346", "Rau Mồng Tơi Gốc Tía Củ Chi", "Basella alba L.", ["TP. Hồ Chí Minh", "Tây Ninh", "Bình Dương"],
         "Mồng tơi cọng tím mập mạp lá dày mọng nhớt mát ngọt giải nhiệt nhuận tràng nấu canh cua rau đay mướp hương mùa hè.",
         "Bệnh Đốm mắt cua lá mồng tơi", "Nấm", "Cercospora basellicidula", "Cao",
         "Phiến lá xuất hiện vô số đốm tròn nhỏ tâm xám mỏng viền đỏ tía nổi bật như mắt cua làm thủng rách màng lá nhớt.",
         "Phân biệt với sâu ăn lá: Nấm có viền đỏ tía sắc sảo và màng hoại tử mỏng xám bạc.",
         "Bóp nhẹ phiến lá thấy màng đốm mỏng thủng lỗ chỗ như tàn nhang.",
         "Hái tỉa lá già thông thoáng, phun thuốc gốc Đồng Booc-đô 1% an toàn."),
        
        ("crop_347", "Rau Đay Đỏ Hải Phòng", "Corchorus olitorius L.", ["Hải Phòng", "Hải Dương", "Thái Bình"],
         "Rau đay thân đỏ ngọn mập nhớt bùi mát ruột nấu canh cua mùng tơi truyền thống mùa hè xua tan oi ả miền Bắc.",
         "Bệnh Lở cổ rễ thối thân rau đay", "Nấm", "Rhizoctonia solani", "Cao",
         "Cổ rễ sát đất bị thâm đen teo thắt vỏ nứt mục, ngọn rau đay héo rũ gãy gục hàng loạt trên luống đất cát.",
         "Phân biệt với khô hạn: Đất luống vẫn ướt nhưng cây bị thắt nghẽn cổ rễ thâm đen.",
         "Nhấc cây rau đay đứt ngang gốc cổ rễ trơ xơ đen mục.",
         "Rải vôi bột khử chua, tưới sinh học Trichoderma trước khi gieo hạt."),
        
        ("crop_348", "Rau Dền Cơm Đỏ Vĩnh Long", "Amaranthus tricolor L.", ["Vĩnh Long", "Tiền Giang", "Đồng Tháp"],
         "Rau dền ngọn non đỏ tím mọng nước giàu sắt và canxi, vị ngọt mát nấu canh tôm đồng thanh nhiệt ngày hè Nam Bộ.",
         "Bệnh Gỉ trắng lá rau dền (White Rust)", "Nấm", "Albugo bliti", "Cao",
         "Mặt dưới lá nổi các u mụn mủ màu trắng ngà bóng nhẫy như men sứ, mặt trên lá tương ứng úa vàng lồi lõm sần sùi.",
         "Phân biệt với phấn trắng: Gỉ trắng nổi u mụn màng bóng men sứ nứt bung phấn trắng; phấn trắng phủ màng bụi khô.",
         "Cào nhẹ u mụn thấy vỡ bung bột bào tử trắng phấn ngà.",
         "Phun luân phiên Metalaxyl hoặc Ridomil Gold bảo vệ lứa ngọn non."),
        
        ("crop_349", "Rau Muống Nước Củ Chi", "Ipomoea aquatica Forssk.", ["TP. Hồ Chí Minh", "Long An", "Đồng Nai"],
         "Rau muống ruộng nước cọng to giòn rỗng ruột xanh ngắt, rau ăn lá quốc dân xào tỏi luộc chấm tương giòn ngọt đậm vị.",
         "Bệnh Gỉ trắng rau muống (White Rust)", "Nấm", "Albugo ipomoeae-aquaticae", "Rất cao",
         "Mặt dưới lá và cọng thân nổi các u sưng sần sùi màu trắng ngà sau nứt ra bột trắng, cọng rau muống bị phình to dị dạng xoắn vặn.",
         "Phân biệt với sâu đục ngọn: Nấm gỉ trắng làm thân phình to nổi mụn sứ trắng không có phân sâu trong ruột rỗng.",
         "Bẻ cọng muống thấy phình to giòn gãy lộ mụn sùi trắng bóng.",
         "Phun phòng thuốc sinh học Nano Bạc hoặc Metalaxyl-M, nhổ gom tiêu hủy cọng xoắn dị dạng."),
        
        ("crop_350", "Rau Ngót Rừng Lạng Sơn", "Melientha suavis Pierre", ["Lạng Sơn", "Thái Nguyên", "Bắc Kạn"],
         "Cây rau ngót rừng mọc trên núi đá vôi đọt non và hoa ngọt lịm như mì chính tự nhiên, đặc sản quý hiếm vùng Đông Bắc.",
         "Bệnh Đốm phấn đen lá rau ngót rừng", "Nấm", "Cercospora spp.", "Trung bình",
         "Phiến lá có đốm nâu đen rải rác mặt dưới có lớp nấm mịn làm rụng lá non khi vào mùa mưa đá ẩm.",
         "Phân biệt với vết chích bọ xít: Bệnh nấm có viền sắc nét không làm thâm đen cả chồi ngọn.",
         "Sờ mặt lá giòn khô ở đốm đen nhỏ li ti.",
         "Phun phòng dung dịch tỏi ớt gừng sinh học định kỳ sau hái đọt."),
        
        ("crop_351", "Rau Càng Cua Bến Tre", "Peperomia pellucida (L.) Kunth", ["Bến Tre", "Tiền Giang", "Vĩnh Long"],
         "Rau càng cua thân mọng nước trong suốt giòn ngọt chua dịu mọc tự nhiên dưới gốc vườn dừa, trộn gỏi bò bóp thấu tuyệt hảo.",
         "Bệnh Thối úng nhũn thân rau càng cua", "Nấm", "Pythium spp.", "Cao",
         "Thân mọng nước bị thâm ủng chuyển màu nâu nhạt chảy nước mềm xẹp đổ rạp cả bụi rau.",
         "Phân biệt với cây dập chân: Nấm làm thối nhũn lan nhanh thành vạt lớn sau mưa dầm ẩm ướt.",
         "Cầm thân rau thấy nhũn nát mềm rục trong tay.",
         "Nhổ bỏ vùng bệnh, rải tro bếp giữ khô ráo mặt đất vườn dừa."),
        
        ("crop_352", "Củ Cải Trắng Đà Lạt", "Raphanus sativus L.", ["Lâm Đồng", "Hải Dương"],
         "Củ cải dài to vỏ trắng muốt ruột giòn mọng nước ngọt mát, nhân sâm mùa đông dùng hầm súp canh và làm củ cải muối kim chi.",
         "Bệnh Đốm đen thối ruột củ cải trắng", "Nấm", "Alternaria raphani", "Cao",
         "Trên củ xuất hiện các đốm thâm đen lõm sâu ruột củ bên trong bị thâm đen xơ cứng có vị đắng ngắt.",
         "Phân biệt with rỗng ruột do thiếu Bo: Nấm có vết đen ăn sâu từ vỏ ngoài vào và thịt thối xơ mục.",
         "Cắt ngang củ thấy lõi thịt bị thâm vệt xám đen bốc mùi mốc.",
         "Bón bổ sung phân Bo, phun phòng Chlorothalonil hoặc Iprodione."),
        
        ("crop_353", "Củ Cải Đỏ Mini Cherry", "Raphanus sativus var. radicula", ["Lâm Đồng", "Hà Nội"],
         "Củ cải tròn nhỏ bằng quả bóng bàn vỏ đỏ chót ruột trắng giòn cay ngọt trang trí đĩa salad rực rỡ thu hoạch sau 25 ngày.",
         "Bệnh Lở cổ rễ thối củ mini", "Nấm", "Rhizoctonia solani", "Cao",
         "Cổ rễ thắt teo thâm đen củ non bị loét khuyết vỏ màu nâu mục cây héo rũ trên luống cát xốp.",
         "Phân biệt with sâu cắn: Vỏ củ bị nứt nẻ thâm đen có tơ nấm nâu bao bọc quanh cổ rễ.",
         "Nhổ củ thấy vỏ củ bị lở loét khuyết sâu xơ đen trơ trọi.",
         "Xử lý đất tơi xốp, tưới phòng Trichoderma trước khi tra hạt giống."),
        
        ("crop_354", "Su Hào Bánh Xe Hải Dương", "Brassica oleracea var. gongylodes", ["Hải Dương", "Vĩnh Phúc", "Hà Nội"],
         "Củ su hào tròn dẹt như bánh xe vỏ xanh nhạt thịt giòn ngọt ít xơ, món ăn mùa đông kinh điển của vùng châu thổ sông Hồng.",
         "Bệnh Thối cổ củ su hào do nấm hạch", "Nấm", "Sclerotinia sclerotiorum", "Cao",
         "Phần củ tiếp giáp mặt đất bị thâm ủng phủ màng tơ trắng muốt như tuyết kèm các hạt hạch đen to như hạt đỗ.",
         "Phân biệt với thối nứt do thừa nước: Thối nấm có lớp tơ trắng bông tuyết và hạch nấm đen đặc trưng.",
         "Dùng móng tay cạo lớp tơ trắng lộ ra hạch đen hình bầu dục cứng cáp.",
         "Lên luống cao ráo, phun phòng thuốc Boscalid hoặc Iprodione."),
        
        ("crop_355", "Bầu Sao Lai F1 Tiền Giang", "Lagenaria siceraria (Molina) Standl.", ["Tiền Giang", "Vĩnh Long", "Bến Tre"],
         "Bầu sao quả dài thon điểm lấm tấm đốm trắng như sao đêm, ruột mềm ngọt mát nấu canh tôm đồng râu tôm nấu với ruột bầu trứ danh.",
         "Bệnh Nứt thân xì mủ bầu sao (Gummy Stem Blight)", "Nấm", "Didymella bryoniae (Stagonosporopsis cucurbitacearum)", "Rất cao",
         "Gốc thân xuất hiện vết nứt dọc chảy ra các giọt gôm mủ màu nâu đỏ quánh dẻo, sau hóa đen làm dây bầu héo khô rũ.",
         "Phân biệt với chạy dây Fusarium: Nứt thân xì mủ có các giọt keo màu hổ phách ứa ra từ vết nứt và đốm đen li ti.",
         "Sờ vào vết nứt thấy mủ dẻo dính tay mùi tanh chua nồng.",
         "Quét gốc bằng dung dịch Đồng Đỏ hoặc Difenoconazole đặc sệt."),
        
        ("crop_356", "Mướp Hương Láng Hà Nội", "Luffa aegyptiaca Mill.", ["Hà Nội", "Hưng Yên", "Hà Nam"],
         "Mướp hương quả thon dài da xanh mịn thơm ngát nức mũi khi vừa cắt trên giàn, nấu canh cua mướp hương thơm lừng xóm ngõ.",
         "Bệnh Sương mai giả mướp hương (Downy Mildew)", "Nấm", "Pseudoperonospora cubensis", "Rất cao",
         "Mặt trên lá có các vết vàng góc cạnh đa giác giới hạn bởi gân lá, mặt dưới phủ lớp mốc tơ màu xám tím mờ ẩm ướt.",
         "Phân biệt với cháy nắng: Góc cạnh vuông vức theo mạng lưới gân lá và lớp mốc xám tím mặt dưới.",
         "Lật mặt dưới lá buổi sáng thấy mốc nhung tím xám rõ nét.",
         "Phun luân phiên Cymoxanil, Dimethomorph hoặc Metalaxyl-M."),
        
        ("crop_357", "Mướp Đắng Khổ Qua Gai Rừng", "Momordica charantia L.", ["Đồng Nai", "Bình Phước", "Tây Ninh"],
         "Khổ qua gai nhọn quả nhỏ màu xanh thẫm đắng đậm thanh nhiệt giải độc mát gan hạ đường huyết quý giá.",
         "Bệnh Thán thư đốm quả khổ qua", "Nấm", "Colletotrichum orbiculare", "Cao",
         "Quả xuất hiện đốm tròn lõm màu nâu sẫm tiết dịch nấm hồng cam dẻo quánh làm quả bị chín ép vàng nứt toác.",
         "Phân biệt với ruồi đục quả: Thán thư có vết lõm sâu dạng lòng chảo có dịch nấm cam; ruồi đục có chấm châm kim và dòi bên trong.",
         "Dùng ngón tay ấn vào vết thâm thấy lõm xẹp ứa dịch nhầy màu hồng cam.",
         "Bao quả non bằng túi chuyên dụng, phun Difenoconazole hoặc Antracol."),
        
        ("crop_358", "Bí Đao Chanh Sáp Vĩnh Long", "Benincasa hispida (Thunb.) Cogn.", ["Vĩnh Long", "Tiền Giang", "Trà Vinh"],
         "Bí đao vỏ xanh phủ phấn trắng như sáp cùi dày đặc ít ruột ngọt thanh, quả nặng 2-3kg làm mứt bí và nấu canh thanh nhiệt.",
         "Bệnh Héo vàng Fusarium bí đao (Chạy dây)", "Nấm", "Fusarium oxysporum f. sp. niveum", "Rất cao",
         "Dây bí đang leo giàn xanh tốt bỗng héo rũ từng nhánh từ gốc, chẻ dọc gốc thân thấy bó mạch dẫn thâm nâu đen thui.",
         "Phân biệt với sâu đục thân: Héo nấm toàn bộ mạch dẫn bị hóa nâu đen liên tục không có phân sâu đùn ra.",
         "Cạo nhẹ lớp vỏ gốc thân thấy mạch gỗ bên trong màu nâu đậm như bã chè.",
         "Luân canh với lúa nước, tưới phòng Trichoderma kết hợp rải vôi bột khử trùng."),
        
        ("crop_359", "Nấm Đùi Gà Vĩnh Phúc", "Pleurotus eryngii (DC.) Quél.", ["Vĩnh Phúc", "Hải Dương", "Lâm Đồng"],
         "Nấm ăn cao cấp thân mập mạp trắng nõn thịt giòn ngọt vị như thịt bào ngư nướng bơ tỏi thượng hạng ẩm thực Á Âu.",
         "Bệnh Mốc xanh cơ chất nấm đùi gà", "Nấm", "Trichoderma harzianum", "Rất cao",
         "Trên bề mặt bịch mùn cưa xuất hiện các mảng mốc màu xanh lá cây đậm loang lổ cạnh tranh dinh dưỡng làm tai nấm thui chột thối đen.",
         "Phân biệt với mốc đen: Mốc Trichoderma có màu xanh lục bảo đặc trưng và mùi hăng hắc ẩm mốc mùn cưa.",
         "Lấy tay quẹt bề mặt mốc thấy bột màu xanh lục bám đầy ngón tay.",
         "Thanh trùng hấp khử khuẩn cơ chất mùn cưa đạt 100 độ C trong 10-12 tiếng; cách ly phòng nuôi vô trùng."),
        
        ("crop_360", "Nấm Linh Chi Đỏ Đồng Nai", "Ganoderma lucidum (Curtis) P. Karst.", ["Đồng Nai", "Bình Dương", "Củ Chi"],
         "Vua của các loài thảo dược mọc trên phôi mùn cưa gỗ cao su, tai nấm hình bán nguyệt viền vàng bóng đỏ nâu như đánh vec-ni, bồi bổ miễn dịch.",
         "Bệnh Mốc hoa cau nấm Linh Chi", "Nấm", "Neurospora sitophila", "Cao",
         "Các đám mốc màu cam rực rỡ như hoa cau nở bùng phát cực nhanh trên nút bông và cổ phôi nấm lây lan toàn bộ trại nấm.",
         "Phân biệt with mốc xanh: Màu cam tươi rực rỡ phát tán sợi tơ mịn màng bồng bềnh cực nhanh chỉ sau một đêm.",
         "Bóp nút bông thấy bụi phấn màu cam bay túa ra khắp không khí trại nấm.",
         "Hạ nhiệt độ phòng ủ, tiêu hủy triệt để bịch phôi nhiễm mốc cam; xông khử trùng phòng bằng Formalin hoặc cồn 70 độ."),
        
        ("crop_361", "Nấm Bào Ngư Xám Long Khánh", "Pleurotus pulmonarius (Fr.) Quél.", ["Đồng Nai", "Bình Phước", "Bà Rịa - Vũng Tàu"],
         "Nấm sò xám thịt dai ngọt thơm bùi mọc từng chùm xòe quạt dày đặc trên phôi mùn cưa, món ăn chay thanh đạm giàu đạm thực vật.",
         "Bệnh Đốm vàng thối ướt tai nấm bào ngư", "Vi khuẩn", "Pseudomonas tolaasii", "Cao",
         "Tai nấm xuất hiện các đốm màu vàng cam sũng nước nhớt nhầy, tai nấm bị nhũn rũ bốc mùi tanh hôi chua loét.",
         "Phân biệt với khô tai do gió: Vi khuẩn làm mềm nhũn chảy nước nhờn dính mùi hôi; gió hanh làm tai nấm khô quăn mép.",
         "Sờ mặt tai nấm thấy nhớt dính ngón tay mùi tanh khắm.",
         "Giảm độ ẩm phun sương nhà nấm xuống dưới 85%, tưới dung dịch Nano Bạc hoặc nước vôi trong 1% phòng ngừa."),
        
        ("crop_362", "Nấm Kim Châm Đà Lạt", "Flammulina velutipes (Curtis) Singer", ["Lâm Đồng", "Đà Lạt"],
         "Nấm thân dài thon nhỏ đầu mũ tròn trắng nõn nà giòn sần sật trồng trong phòng lạnh 8-12 độ C vô trùng, nhúng lẩu nấm thượng hạng.",
         "Bệnh Thối gốc thân nấm kim châm", "Nấm", "Rhizoctonia solani / Fusarium spp.", "Cao",
         "Phần chân gốc của cụm nấm bị thâm nâu ủng nước đổ rạp, sợi nấm bị nhầy nhũn không vươn dài mũ nấm teo tóp.",
         "Phân biệt with thiếu oxy: Thiếu oxy thân dài ngoằng mũ nhỏ trắng tinh; bệnh nấm chân gốc thâm nhầy nâu đen mục rỗng.",
         "Nhấc cụm nấm thấy đứt lìa chân gốc ủng mục mùi mốc nồng.",
         "Kiểm soát nghiêm ngặt nhiệt độ phòng lạnh 8-10 độ C, tiệt trùng khay cơ chất triệt để trước khi cấy giống."),
        
        ("crop_363", "Nấm Đông Cô Sa Pa Hương Bắc", "Lentinula edodes (Berk.) Pegler", ["Lào Cai", "Lai Châu", "Yên Bái"],
         "Nấm hương Sa Pa mọc trên thân gỗ sồi dẻ rừng vùng lạnh, mũ nấm nứt vân hoa cúc màu nâu sẫm hương thơm nức mũi vị ngọt sâu đậm đà.",
         "Bệnh Mốc đen mốc lục tai nấm đông cô", "Nấm", "Trichoderma viride & Aspergillus niger", "Cao",
         "Cơ chất khúc gỗ và tai nấm bị bao phủ các đốm bột màu xanh lục đậm hoặc đen mun làm sợi nấm hương thoái hóa teo thắt.",
         "Phân biệt với phấn tự nhiên: Mốc đen mốc lục có mùi hôi hắc phá hủy mục rỗng gỗ thịt sồi.",
         "Miết ngón tay lên khúc gỗ dính bột đen mun hoặc xanh lục bẩn.",
         "Dùng nước vôi quét sạch vỏ gỗ, phơi khúc gỗ dưới nắng dịu để tiêu diệt màng nấm tạp."),
        
        ("crop_364", "Nấm Rơm Nam Bộ Long An", "Volvariella volvacea (Bull.) Singer", ["Long An", "Đồng Tháp", "Cần Thơ"],
         "Nấm rơm mọc trên mô rơm rạ mục mùa nước nổi, quả thể hình trứng tròn đen bóng xẻ thịt ngọt bùi giòn ngọt tinh túy ẩm thực sông nước.",
         "Bệnh Nấm mốc thạch cao nấm rơm (Coprinus / Nấm mực)", "Nấm đối thủ", "Coprinus comatus / Coprinus cinereus", "Cao",
         "Trên mô rơm xuất hiện hàng loạt cây nấm mực thân dài mũ đen tự phân hủy thành chất lỏng đen kịt như mực viết tranh giành dinh dưỡng.",
         "Phân biệt với nấm rơm: Nấm mực mũ mỏng tự chảy rữa thành nước mực đen thui trong vài giờ làm chết sợi tơ nấm rơm.",
         "Nhìn mô rơm thấy loang lổ vết mực đen tanh ngắt.",
         "Ủ rơm đúng quy trình nhiệt độ đống ủ đạt 65-70 độ C diệt triệt để bào tử nấm mực; rải vôi bột khử chua rơm."),
        
        ("crop_365", "Nấm Mối Đen Tây Ninh", "Oudemansiella radicata (Relhan) Singer", ["Tây Ninh", "Bình Dương", "Đồng Nai"],
         "Nấm quý nuôi trồng công nghệ cao có rễ cọc dài thịt nấm giòn ngọt thanh ngọt y hệt nấm mối tự nhiên mùa mưa, giàu khoáng chất bồi bổ sinh lực.",
         "Bệnh Thối nhũn gốc rễ nấm mối đen", "Vi khuẩn", "Pseudomonas spp.", "Cao",
         "Phần rễ cọc cắm sâu trong giá thể bị thâm đen ủng nhớt chảy dịch đục, thân nấm gục ngã mềm oặt mũ nấm teo rũ.",
         "Phân biệt với khô giá thể: Bệnh làm ủng nhớt thối nhũn chảy nước tanh khắm mùi hữu cơ rữa nát.",
         "Cầm thân nấm rút lên thấy đứt ngang rễ cọc đen nhớt dơ tay.",
         "Khử trùng giá thể than bùn mùn cưa bằng hơi nước áp suất cao; kiểm soát độ ẩm phòng nuôi dưới 88% thông gió nhẹ.")
    ]
    
    for item in raw_list_4:
        cid, name, sci, locs, eco, dname, ag_type, ag_sci, danger, symp, diff, test, vietgap = item
        crop_obj = {
            "id": cid,
            "topic": "Rau_Cu_Gia_Vi_Va_Nam",
            "name_vi": name,
            "scientific_name": sci,
            "dia_ban_pho_bien": locs,
            "dac_tinh_sinh_thai": eco,
            "danh_sach_benh": [
                {
                    "ten_benh": dname,
                    "muc_do_nguy_hiem": danger,
                    "tac_nhan": {
                        "loai": ag_type,
                        "ten_khoa_hoc": ag_sci
                    },
                    "trieu_chung_dien_hinh": [
                        symp,
                        f"Bệnh gây hại nghiêm trọng làm giảm chất lượng và năng suất thương phẩm của cây {name}.",
                        "Mầm bệnh lây lan mạnh mẽ qua bào tử phát tán trong không khí hoặc dòng nước tưới tràn."
                    ],
                    "phan_biet_chan_doan_kep": diff,
                    "kiem_tra_thuc_dia": test,
                    "phac_do_vietgap": {
                        "canh_tac": "Vệ sinh đồng ruộng / nhà màng, cách ly nguồn lây nhiễm, thu gom tiêu hủy mẫu bệnh đúng quy định an toàn.",
                        "sinh_hoc": "Ứng dụng các dòng vi sinh vật đối kháng (Bacillus, Trichoderma, Chaetomium) hoặc nano bạc đồng sinh học.",
                        "khuyen_cao_chuyen_gia": vietgap
                    }
                },
                {
                    "ten_benh": f"Bệnh Thối rễ và héo vàng sinh học {name}",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Fusarium oxysporum / Pythium spp."
                    },
                    "trieu_chung_dien_hinh": [
                        "Bộ rễ hút hoặc hệ sợi tơ dinh dưỡng bị thâm đen, suy thoái chức năng vận chuyển chất bổ",
                        "Cây xuất hiện triệu chứng vàng lá từ dưới lên trên hoặc quả thể bị teo tóp mất nước",
                        "Cây bị chết đứng hoặc giảm năng suất nghiêm trọng trong giai đoạn thu hoạch chính"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với sốc nhiệt hoặc hạn: Bệnh nấm rễ mô rễ thối đen xơ mục; hạn khô lá héo đồng loạt nhưng rễ không ủng thối.",
                    "kiem_tra_thuc_dia": "Kiểm tra tầng rễ hoặc phôi nấm thấy đốm nâu đen lan tỏa, bốc mùi đất ẩm mốc hữu cơ mục nát.",
                    "phac_do_vietgap": {
                        "canh_tac": "Đảm bảo độ thông thoáng, cân bằng ẩm độ cơ chất hoặc đất trồng, tránh tưới ứ đọng nước cục bộ.",
                        "sinh_hoc": "Bổ sung chế phẩm kích rễ sinh học Humic kết hợp vi sinh đối kháng định kỳ.",
                        "khuyen_cao_chuyen_gia": "Xử lý bằng các hoạt chất sinh học hoặc thuốc bảo vệ thực vật thế hệ mới có thời gian cách ly cực ngắn (1-3 ngày)."
                    }
                }
            ]
        }
        crops.append(crop_obj)
        
    return crops

if __name__ == '__main__':
    data = get_module4_crops()
    print(f"Module 4 generated {len(data)} crops: {data[0]['id']} -> {data[-1]['id']}")
