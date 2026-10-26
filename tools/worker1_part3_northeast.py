# -*- coding: utf-8 -*-
"""
Worker 1 - Part 3: Đông Bắc (Crops 51 to 63)
Hà Giang, Tuyên Quang, Cao Bằng, Bắc Kạn, Lạng Sơn, Quảng Ninh, Thái Nguyên, Bắc Giang
"""

def get_part3_crops():
    return [
        {
            "id": "w1_051",
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": "Cam sành Hàm Yên Tuyên Quang",
            "scientific_name": "Citrus nobilis Lour. cv. Ham Yen",
            "dia_ban_pho_bien": ["Hàm Yên", "Chiêm Hóa", "Tuyên Quang", "Bắc Quang", "Hà Giang"],
            "dac_tinh_sinh_thai": "Cây ăn quả chỉ dẫn địa lý nức tiếng vùng núi thấp, đất Feralit trên đá vôi giàu canxi và mùn hữu cơ, khí hậu trong lành biên độ nhiệt ngày đêm lớn, quả vỏ sần dày, mọng nước màu vàng cam đậm vị ngọt thanh pha chua dịu đậm đà.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Đốm rong đỏ cành lá cam sành Hàm Yên",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Tảo ký sinh",
                        "ten_khoa_hoc": "Cephaleuros virescens"
                    },
                    "trieu_chung_dien_hinh": [
                        "Trên mặt lá và cành già xuất hiện những đốm tròn nhung mịn màu đỏ cam hoặc vàng rỉ sắt",
                        "Lớp tảo phát triển dày đặc làm cản trở quang hợp, mô vỏ cành bên dưới bị nứt nẻ xù xì chai cứng",
                        "Cành cam bị suy kiệt, lá vàng rụng sớm, hoa quả đậu thưa thớt",
                        "Khi gặp độ ẩm cao vào mùa mưa, vết đốm rong phát tán bào tử động bơi lội lan tràn khắp tán cây"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bệnh rỉ sắt nấm: Rỉ sắt nấm là các mụn nứt u cục giải phóng bụi phấn; Đốm rong đỏ là lớp lông nhung mịn như thảm nhung màu đỏ gạch bám chắc trên biểu bì lá và vỏ cành.",
                    "kiem_tra_thuc_dia": "Lấy móng tay cạo nhẹ lớp nhung đỏ thấy tróc ra mảng màu xanh vàng nhạt, vỏ cành bên dưới bị nứt vảy nhẹ.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt tỉa cành thông thoáng, hạ bớt độ che bóng rậm rạp của cây chắn gió xung quanh vườn cam.",
                        "sinh_hoc": "Phun dung dịch Nano Đồng hữu cơ 500ppm quét sạch lớp tảo ký sinh mà không gây hại cho thiên địch.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bằng Booc-đô 1% hoặc gốc đồng Copper Hydroxide (Champion 77WP) vào đầu mùa mưa."
                    }
                },
                {
                    "ten_benh": "Bệnh Vàng lá thối rễ cam sành",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Tổ hợp nấm và tuyến trùng",
                        "ten_khoa_hoc": "Fusarium solani / Phytophthora nicotianae / Tylenchulus semipenetrans"
                    },
                    "trieu_chung_dien_hinh": [
                        "Gân lá và phiến lá cam đều ngả màu vàng úa đồng loạt từ tầng lá dưới lên tầng lá trên",
                        "Lá vàng nhưng gân lá không sưng gồ, lá rụng hàng loạt để lại cành trơ trụi đầu cành",
                        "Bộ rễ tơ ngầm dưới đất bị thối đen tuột lớp vỏ ngoài chỉ còn trơ lõi trắng như sợi chỉ",
                        "Cây suy kiệt héo rũ từ từ rồi chết khô đứng giữa vườn sau các đợt mưa bão úng ngập"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Vàng lá gân xanh HLB: HLB lá vàng loang lổ không đối xứng, gân chính vẫn xanh hoặc hóa bần sưng gồ và rễ vẫn nguyên vẹn giai đoạn đầu; Vàng lá thối rễ vàng cả gân lẫn phiến lá và toàn bộ rễ tơ bị thối tuột vỏ bốc mùi bùn thối.",
                    "kiem_tra_thuc_dia": "Dùng bay nhỏ cào lớp đất mặt ở mép tán cây nhặt rễ tơ lên vuốt nhẹ thấy vỏ rễ tuột tuột ra như chiếc bao ren để lộ lõi rễ trắng bên trong.",
                    "phac_do_vietgap": {
                        "canh_tac": "Lên mô cao, đào mương thoát nước sâu chống ngập úng mùa mưa; xới nhẹ phá váng đất sau mưa to.",
                        "sinh_hoc": "Tưới phòng gốc bằng hỗn hợp men vi sinh đối kháng Trichoderma kết hợp xạ khuẩn Streptomyces định kỳ 2 tháng/lần.",
                        "khuyen_cao_chuyen_gia": "Tưới gốc bằng Phosphonate sinh học kết hợp Ridomil Gold hoặc Aliette 800WG khi cây chớm có biểu hiện vàng lá ngọn."
                    }
                }
            ]
        },
        {
            "id": "w1_052",
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": "Quýt vỏ giòn Quang Hán Cao Bằng",
            "scientific_name": "Citrus reticulata Blanco cv. Quang Han",
            "dia_ban_pho_bien": ["Trà Lĩnh", "Quang Hán", "Cao Bằng", "Trùng Khánh", "Hà Giang"],
            "dac_tinh_sinh_thai": "Giống quýt bản địa đặc sắc thung lũng đá vôi vùng biên ải, quả dẹt vỏ vàng óng mỏng tang giòn rụm dễ bóc, múi mọng nước vị ngọt sắc đậm đà hương thơm quýt rừng quyến rũ, cây chịu rét buốt và khô hạn rất giỏi.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Loét sẹo quả và cành non quýt vỏ giòn",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Vi khuẩn",
                        "ten_khoa_hoc": "Xanthomonas citri subsp. citri"
                    },
                    "trieu_chung_dien_hinh": [
                        "Trên lá: Vết bệnh là nốt sần nhỏ ngậm nước lồi lên màu nâu xám, tâm nứt toác miệng núi lửa có quầng halo vàng sáng",
                        "Trên quả: Vết loét sần sùi đóng vảy cứng xù xì làm nứt vỏ quýt giòn, quả rụng non hoặc méo mó",
                        "Trên cành non: Vết loét dài làm khô cành giòn gãy",
                        "Bệnh lây lan rất mạnh theo giọt mưa gió bão vùng núi"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Ghẻ nhám: Ghẻ nhám chóp nhọn như hạt mụn cơm không có quầng vàng và không nứt miệng núi lửa; Loét sẹo có quầng halo vàng sáng và tâm nứt miệng núi lửa rõ rệt.",
                    "kiem_tra_thuc_dia": "Dùng tay sờ mặt lá và vỏ quả thấy cộm ráp nham nhở, soi ngược ánh sáng thấy quầng halo vàng sáng chói.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt tỉa cành bệnh triệt để sau vụ thu hoạch, vệ sinh kéo tỉa bằng cồn y tế.",
                        "sinh_hoc": "Phun phòng bằng vi khuẩn đối kháng Bacillus subtilis kết hợp Nano Bạc Đồng 400ppm.",
                        "khuyen_cao_chuyen_gia": "Phun luân phiên Bordeaux 1%, Kasugamycin hoặc Bismerthiazol sau các đợt mưa dông."
                    }
                },
                {
                    "ten_benh": "Bệnh Mốc xanh thối nhũn sau thu hoạch quýt Quang Hán",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Penicillium digitatum"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết bệnh bắt đầu từ các vết trầy xước nhẹ trên vỏ quýt mỏng trong quá trình hái và vận chuyển",
                        "Vỏ quả nhanh chóng bị mềm nhũn nước màu nâu nhạt, sau đó phủ một lớp màng phấn mốc màu xanh lục ô liu dày đặc",
                        "Thịt quả bên trong bị thối rữa nát thành chất lỏng chua có mùi mốc nồng nặc",
                        "Lây lan nhanh chóng sang các quả lành xung quanh trong thùng sọt đóng gói"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Mốc xám Botrytis: Mốc xám có màu xám tro bụi bặm; Mốc xanh Penicillium có màu xanh lục ô liu sáng viền mép trắng muốt.",
                    "kiem_tra_thuc_dia": "Cầm quả quýt thối thấy nhũn nát ngón tay ấn thủng vỏ, lớp bột phấn xanh lục dính đầy vào tay.",
                    "phac_do_vietgap": {
                        "canh_tac": "Thu hoạch quả bằng kéo cắt cuống phẳng khéo léo không bứt giật, lót sọt xốp mềm khi vận chuyển đường đèo dốc.",
                        "sinh_hoc": "Xử lý sau thu hoạch bằng dung dịch sáp phủ sinh học Chitosan 1% hoặc rửa nước Nano Bạc an toàn.",
                        "khuyen_cao_chuyen_gia": "Xử lý kho bảo quản bằng hơi tinh dầu quế/hồi hoặc phun phòng vườn trước thu hoạch 10 ngày bằng Iprodione."
                    }
                }
            ]
        },
        {
            "id": "w1_053",
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": "Na dai Đồng Bành Chi Lăng Lạng Sơn",
            "scientific_name": "Annona squamosa L. cv. Chi Lang",
            "dia_ban_pho_bien": ["Chi Lăng", "Đồng Mỏ", "Hữu Lũng", "Lạng Sơn"],
            "dac_tinh_sinh_thai": "Cây ăn quả danh tiếng trồng trên sườn núi đá vôi dựng đứng cheo leo hiểm trở, đu dây tời na bằng ròng rọc ngoạn mục, đất mùn trên đá vôi giàu khoáng canxi giúp quả na dai to tròn mắt nở căng mọng, thịt trắng muốt dai giòn ngọt lịm.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Thối đen nứt quả na dai Chi Lăng",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Phomopsis anonacearum"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết bệnh bắt đầu từ cuống quả hoặc kẽ múi dưới dạng đốm nâu đen nhỏ ngậm nước",
                        "Vết thâm lan rộng làm vỏ quả bị chai sượng nứt toác từng kẽ múi, thịt quả bên trong bị thối đen chua lét",
                        "Quả na non bị teo tóp quắt lại thành quả đen xì dính chặt trên cành đá",
                        "Lá na xuất hiện các đốm thán thư nâu xám khô rách mép lá"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Rệp sáp phủ phấn trắng: Rệp sáp là các ổ phấn trắng xốp có côn trùng cựa quậy; Phomopsis là vết loét hoại tử mô vỏ đen sì ăn sâu vào ruột múi na.",
                    "kiem_tra_thuc_dia": "Dùng tay ấn vào vết đen thấy vỏ nứt toác chảy nước thối chua, mô thịt múi bên dưới chuyển màu nâu sẫm nhũn nát.",
                    "phac_do_vietgap": {
                        "canh_tac": "Tỉa cành tạo tán thấp thông thoáng sau vụ thu hoạch na trên núi đá, thu dọn các quả na khô đen đem đốt tiêu hủy.",
                        "sinh_hoc": "Phun phòng chế phẩm Nano Chitosan kết hợp Trichoderma định kỳ khi na bắt đầu mở mắt.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bằng Antracol 70WP, Difenoconazole hoặc Booc-đô 1% giai đoạn đậu quả non."
                    }
                },
                {
                    "ten_benh": "Bệnh Thán thư lá cành quả na dai",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Colletotrichum gloeosporioides"
                    },
                    "trieu_chung_dien_hinh": [
                        "Phiến lá xuất hiện những đốm tròn màu nâu đỏ có viền đậm đồng tâm, tâm vết bệnh khô rách thủng",
                        "Cành non bị các vết lõm thâm đen làm khô giòn dễ gãy trong mùa mưa dông núi đá",
                        "Quả non bị đốm đen làm teo tóp rụng non hàng loạt",
                        "Làm cây suy kiệt rụng lá trơ trụi cành ảnh hưởng vụ na năm sau"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Vết cháy nắng: Cháy nắng vết màu vàng rơm khô phẳng lì; Thán thư đốm tròn có vân đồng tâm và tiết chất nhầy hồng cam khi trời sương ẩm.",
                    "kiem_tra_thuc_dia": "Vò nhẹ mép lá thấy mô lá giòn rụm thủng lỗ mọt, soi kính lúp thấy các chấm bào tử nấm hồng cam li ti.",
                    "phac_do_vietgap": {
                        "canh_tac": "Bón phân cân đối bổ sung thêm Canxi Bo giúp vỏ quả dày dai chống nứt múi.",
                        "sinh_hoc": "Phun men vi sinh đối kháng Bacillus subtilis phòng ngừa mầm nấm bề mặt lá quả.",
                        "khuyen_cao_chuyen_gia": "Phun luân phiên Amistar Top 325SC hoặc Difenoconazole giai đoạn hoa nhú và đậu quả non."
                    }
                }
            ]
        },
        {
            "id": "w1_054",
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": "Hồng không hạt Bảo Lâm Lạng Sơn",
            "scientific_name": "Diospyros kaki L.f. cv. Bao Lam",
            "dia_ban_pho_bien": ["Cao Lộc", "Văn Lãng", "Lạng Sơn", "Ngân Sơn", "Bắc Kạn"],
            "dac_tinh_sinh_thai": "Cây ăn quả bản địa quý hiếm mọc trên núi đá vôi vùng biên cương, quả hình thuôn dài khía 4 múi không có hạt, ngâm nước sạch khử chát cho thịt quả vàng ươm giòn rụm ngọt lịm như mật ong rừng, cây chịu rét cực giỏi.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Đốm mắt cua góc cạnh lá hồng Bảo Lâm",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Cercospora kaki"
                    },
                    "trieu_chung_dien_hinh": [
                        "Phiến lá xuất hiện những đốm nhỏ góc cạnh màu nâu đen bị giới hạn bởi các gân lá nhỏ",
                        "Mặt dưới lá tương ứng xuất hiện các đốm mốc mịn màu nâu xám xịt",
                        "Lá già bị úa vàng đồng loạt và rụng sớm từ giữa mùa hè làm cây trơ cành mang quả non",
                        "Quả hồng bị chín ép sớm, quả nhỏ còi cọc và rụng non hàng loạt"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Vàng lá rụng tự nhiên mùa đông: Rụng tự nhiên vào cuối thu đông khi quả đã chín vàng đỏ; Bệnh Cercospora làm lá rụng sớm ngay từ tháng 6-7 mùa hè khi quả còn xanh ngắt.",
                    "kiem_tra_thuc_dia": "Quan sát mặt lá thấy rõ các đốm góc cạnh đa giác nằm kẹp giữa các gân phụ, rung nhẹ cành thấy lá vàng rơi lả tả.",
                    "phac_do_vietgap": {
                        "canh_tac": "Thu gom toàn bộ lá rụng bệnh dưới gốc đem đốt tiêu hủy; bón phân cân đối tăng kali giúp lá dày cứng.",
                        "sinh_hoc": "Phun phòng định kỳ Nano Bạc Đồng 400ppm kết hợp vi khuẩn đối kháng Bacillus subtilis.",
                        "khuyen_cao_chuyen_gia": "Phun phòng ngừa bằng Mancozeb, Difenoconazole hoặc Antracol 70WP định kỳ 20 ngày trong mùa mưa."
                    }
                },
                {
                    "ten_benh": "Bệnh Thán thư rụng quả non cây hồng",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Colletotrichum gloeosporioides"
                    },
                    "trieu_chung_dien_hinh": [
                        "Cuống quả và tai đài hoa quả hồng non xuất hiện những chấm đen nhỏ lõm sâu",
                        "Vết thâm lan rộng quanh cuống quả làm tắc dòng nhựa nuôi quả, quả non bị rụng trắng gốc",
                        "Trên vỏ quả hồng xuất hiện các đốm tròn thâm nâu đồng tâm lõm sâu vào thịt quả",
                        "Cành non mang quả bị các vết sẹo dài màu đen làm khô giòn cành"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Rụng quả sinh lý do thiếu dinh dưỡng: Rụng sinh lý cuống quả vàng rụng tự nhiên không có đốm đen lõm sâu; Thán thư cuống và tai đài có vết thâm đen lõm sâu ứa dịch bào tử hồng cam.",
                    "kiem_tra_thuc_dia": "Nhặt quả hồng non rụng thấy tai đài và cuống bị đen sì chai cứng, soi kính lúp thấy các đĩa bào tử nấm li ti.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt tỉa cành thông thoáng đón gió sườn đồi, khơi rãnh thoát nước quanh gốc cây.",
                        "sinh_hoc": "Phun dịch chiết vỏ tôm Chitosan nano 2% kích thích cơ chế tự bảo vệ của biểu bì quả non.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bằng Azoxystrobin + Difenoconazole hoặc Booc-đô 1% giai đoạn ngay sau khi rụng cánh hoa."
                    }
                }
            ]
        },
        {
            "id": "w1_055",
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": "Hồng vành khuyên treo gió Bắc Kạn",
            "scientific_name": "Diospyros kaki L.f. cv. Vanh Khuyen",
            "dia_ban_pho_bien": ["Chợ Đồn", "Ba Bể", "Bắc Kạn", "Na Hang", "Tuyên Quang"],
            "dac_tinh_sinh_thai": "Giống hồng đặc sản có gờ vành khuyên tròn quanh cuống rất đặc trưng, quả to giòn ngọt lịm chuyên dùng làm hồng treo gió công nghệ Nhật Bản vang danh, cây ưa đất Feralit trên núi đá vôi khí hậu mùa thu se lạnh hanh khô.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Đốm tròn xám đục lá hồng vành khuyên",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Mycosphaerella nawae"
                    },
                    "trieu_chung_dien_hinh": [
                        "Phiến lá xuất hiện những đốm tròn màu nâu xám đục có quầng vàng hẹp xung quanh",
                        "Vết bệnh lan rộng tâm chuyển sang màu xám tro bạc, rải rác có các chấm đen li ti",
                        "Lá già bị úa đỏ vàng loang lổ rồi rụng hàng loạt từ dưới lên trên",
                        "Cây bị trơ trụi cành làm quả non bị sém nắng và rụng sớm"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Đốm góc cạnh Cercospora: Cercospora vết góc cạnh giới hạn bởi gân nhỏ; Mycosphaerella vết đốm tròn lớn lan qua các gân nhỏ tâm xám đục.",
                    "kiem_tra_thuc_dia": "Lấy tay miết phiến lá thấy giòn rách, quan sát mặt lá thấy các đốm tròn xám bạc loang lổ sắc nét.",
                    "phac_do_vietgap": {
                        "canh_tac": "Thu gom lá rụng đem chôn sâu tiêu hủy, quét vôi thân gốc vào mùa đông.",
                        "sinh_hoc": "Phun phòng bằng chế phẩm vi sinh Bacillus subtilis kết hợp Nano Bạc Đồng 400ppm.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bằng Difenoconazole, Tebuconazole hoặc Mancozeb vào đầu mùa mưa phùn xuân hè."
                    }
                },
                {
                    "ten_benh": "Bệnh Mốc đen muội bồ hóng quả hồng treo gió",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Nấm hoại sinh",
                        "ten_khoa_hoc": "Capnodium spp. / Pseudococcus sp.",
                        "vector_truyen_benh": "Rệp sáp trắng bám tai đài hồng"
                    },
                    "trieu_chung_dien_hinh": [
                        "Mặt vỏ quả và kẽ tai đài quả hồng bị phủ một lớp màng đen như muội than đáy nồi",
                        "Lớp muội đen làm vỏ quả bị lem nhem đen sì không thể gọt vỏ làm hồng treo gió cao cấp",
                        "Dưới lớp muội đen ở kẽ tai đài bám đầy các ổ rệp sáp trắng xốp tiết dịch mật ngọt",
                        "Lá hồng bị phủ đen làm giảm hiệu suất quang hợp"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Thán thư đen vỏ quả: Muội bồ hóng lấy khăn ướt lau sạch bong để lộ vỏ quả lành lặn; Thán thư ăn sâu hoại tử mô thịt quả không thể lau sạch.",
                    "kiem_tra_thuc_dia": "Lấy ngón tay miết mạnh lớp đen trên vỏ quả thấy bột than đen dính vào tay, vỏ quả bên dưới vẫn vàng bóng bình thường.",
                    "phac_do_vietgap": {
                        "canh_tac": "Tỉa cành thông thoáng, bắt diệt kiến đen tha rệp lên cây.",
                        "sinh_hoc": "Phun dung dịch nước rửa chén sinh học loãng 0.2% hoặc dầu khoáng SK Enspray 99EC diệt rệp sáp và rửa trôi muội đen.",
                        "khuyen_cao_chuyen_gia": "Phun trừ rệp sáp ở kẽ tai đài quả bằng Spirotetramat hoặc Abamectin sinh học giai đoạn quả non."
                    }
                }
            ]
        },
        {
            "id": "w1_056",
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": "Bưởi Soi Hà Yên Sơn Tuyên Quang",
            "scientific_name": "Citrus maxima Merr. cv. Soi Ha",
            "dia_ban_pho_bien": ["Yên Sơn", "Soi Hà", "Tuyên Quang", "Đoan Hùng", "Phú Thọ"],
            "dac_tinh_sinh_thai": "Giống bưởi đặc sản nổi tiếng chín sớm nhất miền Bắc (thu hoạch từ rằm tháng 8 âm lịch), mọc ven dòng sông Lô phù sa bồi đắp màu mỡ tơi xốp, quả tròn đều vỏ vàng tươi mỏng dính, tép bưởi róc mọng nước ngọt thanh mát không một chút đắng chát.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Nứt vỏ xì gôm chảy nhựa gốc bưởi Soi Hà",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Phytophthora nicotianae"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vỏ thân sát gốc và cổ rễ bị sũng nước nứt toác từng vệt dài, ứa ra những giọt nhựa mủ dẻo màu cánh gián",
                        "Mô vỏ dưới vết nứt bị thối đen ăn sâu vào tầng mô gỗ bên trong bốc mùi chua nồng",
                        "Tán lá ngả màu vàng đồng loạt và rụng dần làm cành trơ trụi cành khô",
                        "Bộ rễ tơ ngầm bị thối tuột vỏ chỉ còn trơ lõi trắng xơ xác"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Sâu đục thân xì mủ: Sâu đục thân có lỗ tròn đùn mạt cưa phân sâu li ti; Phytophthora nứt dọc thành mảng thối ướt không có mạt cưa.",
                    "kiem_tra_thuc_dia": "Dùng dao con cạo nhẹ lớp vỏ thấy tầng tượng tầng chuyển màu nâu đen sũng nước, nhựa mủ dính vào đầu ngón tay.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cào đất quanh cổ rễ để lộ cổ rễ thoáng gió, quét vôi trắng thân cây cao 1m trước mùa mưa.",
                        "sinh_hoc": "Cạo sạch mô vỏ thối rồi quét chế phẩm nấm đối kháng Chaetomium kết hợp Nano Đồng đặc.",
                        "khuyen_cao_chuyen_gia": "Quét gốc hoặc tưới đẫm vùng rễ bằng Phosphonate hữu cơ hoặc Aliette 800WG định kỳ trong mùa mưa."
                    }
                },
                {
                    "ten_benh": "Bệnh Ghẻ sẹo nhám sần quả bưởi",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Elsinoë fawcettii"
                    },
                    "trieu_chung_dien_hinh": [
                        "Trên lá non: Vết bệnh là các nốt mụn nhỏ nhô cao màu nâu vàng như hạt mụn cơm sần sùi, làm phiến lá nhăn nheo biến dạng",
                        "Trên quả: Vết bệnh đóng vảy cứng xù xì lồi lên như da cóc màu nâu xám, quả bị méo mó chai sượng giảm giá trị thương phẩm",
                        "Cành non bị các vệt ghẻ sần sùi làm còi cọc chùn ngọn",
                        "Bệnh lây lan rất nhanh theo giọt mưa phùn mùa xuân"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Loét sẹo vi khuẩn (Citrus Canker): Ghẻ nhám chóp nhọn nhô lên như hạt mụn cơm và không có quầng halo vàng sáng; Loét sẹo có miệng núi lửa nứt ở tâm và có quầng halo vàng sáng bao quanh.",
                    "kiem_tra_thuc_dia": "Lấy ngón tay sờ qua mặt quả thấy cộm gai rát ráp như giấy ráp, không có quầng sáng vàng bao quanh miệng nứt.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt tỉa cành bệnh triệt để trong mùa đông, vệ sinh dụng cụ cắt tỉa.",
                        "sinh_hoc": "Phun phòng nấm đối kháng Bacillus subtilis kết hợp dịch Nano Bạc Đồng 400ppm.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bằng Booc-đô 1%, Difenoconazole hoặc Antracol 70WP giai đoạn lộc xuân nhú 2-3cm."
                    }
                }
            ]
        },
        {
            "id": "w1_057",
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": "Lê vàng Đông Khê Cao Bằng",
            "scientific_name": "Pyrus pyrifolia (Burm.f.) Nakai cv. Dong Khe",
            "dia_ban_pho_bien": ["Thạch An", "Đông Khê", "Cao Bằng", "Ngân Sơn", "Bắc Kạn"],
            "dac_tinh_sinh_thai": "Cây ăn quả ôn đới đặc sản nức tiếng cửa ngõ biên cương Cao Bằng, quả hình tròn hơi dẹt vỏ màu vàng sáng mịn màng chấm cát nâu li ti, thịt quả giòn tan nhiều nước ngọt lịm không chát, ưa thung lũng núi đá vôi độ cao 600 - 1.000m mát mẻ.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Thối đen khô tâm lõi quả lê Đông Khê",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Alternaria alternata"
                    },
                    "trieu_chung_dien_hinh": [
                        "Nấm xâm nhập từ cuống rốn đài hoa lúc hoa nở lan sâu vào trong buồng hạt lõi quả",
                        "Bên ngoài quả nhìn vẫn vàng bóng bình thường nhưng phần tâm lõi hạt bên trong bị thối đen xốp mục",
                        "Thịt quả quanh tâm hạt bị thâm nâu biến tính bốc mùi men chua khó chịu",
                        "Quả bị chín ép sớm và rụng hàng loạt trước ngày thu hoạch chính vụ"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Thối nhũn vỏ quả: Thối vỏ quả bắt đầu từ bề mặt ngoài ăn vào; Bệnh thối tâm nấm Alternaria ăn từ trong lõi hạt ăn ra ngoài vỏ nhìn vẫn nguyên vẹn.",
                    "kiem_tra_thuc_dia": "Bổ đôi quả lê vàng thấy khoang chứa hạt bên trong đen sì mủn nát phủ lớp nấm mốc đen mịn.",
                    "phac_do_vietgap": {
                        "canh_tac": "Bao quả bằng túi chuyên dụng ngay sau khi cánh hoa rụng và tỉa bớt quả non dị dạng.",
                        "sinh_hoc": "Phun phòng bằng men vi sinh đối kháng Bacillus subtilis bảo vệ bầu nhụy hoa khi hoa vừa hé nở.",
                        "khuyen_cao_chuyen_gia": "Phun phòng ngừa bằng Iprodione hoặc Difenoconazole giai đoạn hoa nở rộ 50%."
                    }
                },
                {
                    "ten_benh": "Bệnh Cháy lá vi khuẩn cành non lê (Bệnh bạc lá hoại tử)",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Vi khuẩn",
                        "ten_khoa_hoc": "Erwinia amylovora"
                    },
                    "trieu_chung_dien_hinh": [
                        "Chùm hoa và đọt lộc non bị héo rũ thâm đen đột ngột như bị lửa thiêu cháy táp",
                        "Ngọn cành non bị uốn cong quặp xuống như chiếc cán gậy của mục đồng (shepherd's crook)",
                        "Lá khô cháy dính chặt trên cành không rụng làm cành trơ que đen xì",
                        "Tại vết loét trên cành rỉ ra các giọt dịch vi khuẩn màu trắng sữa hoặc nâu hổ phách dính nhớt"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Cháy do sương muối: Sương muối làm khô giòn đồng đều toàn bộ tán lá; Cháy lá vi khuẩn Erwinia làm ngọn cong quặp hình cán gậy mục đồng và có giọt dịch vi khuẩn nhờn tiết ra trên cành.",
                    "kiem_tra_thuc_dia": "Quan sát ngọn cành non thấy cong gập hình móc câu chữ U màu đen thui, bóp vào cành thấy dịch nhầy vi khuẩn rỉ ra.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt bỏ ngay cành bệnh sâu dưới vết loét 30-40cm cho vào túi đem đốt tiêu hủy; khử trùng kéo cắt bằng cồn 90 độ.",
                        "sinh_hoc": "Phun phòng bằng vi khuẩn đối kháng Pseudomonas fluorescens hoặc Nano Bạc Đồng 500ppm.",
                        "khuyen_cao_chuyen_gia": "Phun phòng trừ khẩn cấp bằng Kasugamycin, Oxytetracycline hoặc Streptomycin khi vừa dứt đợt mưa dông xuân."
                    }
                }
            ]
        },
        {
            "id": "w1_058",
            "topic": "Cay_Lam_Nghiep_Duoc_Lieu_Quy",
            "name_vi": "Trám đen Hà Châu Bắc Giang",
            "scientific_name": "Canarium tramdenum C.D.Dai & Yakovlev",
            "dia_ban_pho_bien": ["Hiệp Hòa", "Hà Châu", "Bắc Giang", "Hữu Lũng", "Lạng Sơn"],
            "dac_tinh_sinh_thai": "Cây gỗ lớn bản địa quý giá cao 20-30m, sống hàng trăm năm ven sông Cầu, đất phù sa cổ pha cát sỏi thoát nước tốt, quả trám đen hình thoi dài màu tím đen óng ả, cùi dày ngậy béo bùi đậm đà om nước sôi ăn với cơm nóng tuyệt đỉnh ẩm thực kinh bắc.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Đốm mắt cua vỏ quả thối đen trám đen",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Pestalotiopsis sp. / Colletotrichum sp."
                    },
                    "trieu_chung_dien_hinh": [
                        "Vỏ quả trám non xuất hiện những chấm đen tròn nhỏ hơi lõm xuống",
                        "Vết thâm lan rộng làm vỏ quả bị chai sượng nứt nẻ, cùi trám bên trong bị khô xơ cứng đơ",
                        "Quả non bị rụng hàng loạt vào mùa hè làm giảm sản lượng thu hái quả om",
                        "Lá già xuất hiện các vết cháy xám bạc rách thủng mép lá"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Vết ong chích quả non: Vết ong chích có chấm thủng cơ giới nhỏ rỉ giọt nhựa trong; Nấm bệnh là vết lõm tròn đồng tâm màu nâu đen lan rộng ra mô cùi.",
                    "kiem_tra_thuc_dia": "Bổ quả trám non bị bệnh thấy cùi thịt bên dưới chuyển màu nâu đen xơ cứng chai sần không có vị béo bùi.",
                    "phac_do_vietgap": {
                        "canh_tac": "Dọn sạch cỏ rác dưới tán cây cổ thụ, khơi rãnh thoát nước sâu tránh đọng nước mưa quanh gốc.",
                        "sinh_hoc": "Phun phòng bằng chế phẩm nấm đối kháng Chaetomium kết hợp Nano Chitosan kích kháng màng tế bào.",
                        "khuyen_cao_chuyen_gia": "Phun phòng trừ bằng Antracol 70WP hoặc Difenoconazole giai đoạn trước khi hoa nở và sau khi đậu quả non."
                    }
                },
                {
                    "ten_benh": "Bệnh Xén tóc đục thân cổ thụ trám đen",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Côn trùng gây hại",
                        "ten_khoa_hoc": "Batocera rubus"
                    },
                    "trieu_chung_dien_hinh": [
                        "Ấu trùng sâu non đục sâu vào lõi gỗ thân cây trám cổ thụ tạo thành các đường hầm khổng lồ ngoằn ngoèo",
                        "Tại các lỗ đục trên thân cây rỉ nhựa thơm và đùn ra từng đống mạt cưa phân sâu màu nâu nhạt",
                        "Cành lớn trên tán bị khô héo lá và chết khô từng phần",
                        "Thân cây bị rỗng ruột dễ dàng gãy đổ khi có gió bão lớn làm mất đi cây trám cổ thụ hàng trăm năm tuổi"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bệnh nấm thân: Nấm chỉ gây hại mô vỏ ngoài không có lỗ đục sâu vào gỗ và không có mạt cưa đùn ra.",
                    "kiem_tra_thuc_dia": "Quan sát thân cây thấy các lỗ nhỏ đùn ra từng đống mạt cưa tươi, dùng que sắt chọc vào thấy rỗng sâu bên trong lõi gỗ.",
                    "phac_do_vietgap": {
                        "canh_tac": "Quét vôi bột trộn lưu huỳnh quanh thân cây cao 2m vào đầu mùa mưa để ngăn xén tóc đẻ trứng.",
                        "sinh_hoc": "Bơm chế phẩm nấm ký sinh côn trùng Metarhizium anisopliae vào các lỗ đục sâu.",
                        "khuyen_cao_chuyen_gia": "Dùng bông tẩm thuốc sinh học Abamectin nhét sâu vào lỗ đục rồi dùng đất dẻo trát kín miệng lỗ xông hơi diệt ấu trùng."
                    }
                }
            ]
        },
        {
            "id": "w1_059",
            "topic": "Cay_Lam_Nghiep_Duoc_Lieu_Quy",
            "name_vi": "Trám trắng Đình Lập Lạng Sơn",
            "scientific_name": "Canarium album (Lour.) Raeusch.",
            "dia_ban_pho_bien": ["Đình Lập", "Lộc Bình", "Lạng Sơn", "Quảng Ninh", "Bắc Giang"],
            "dac_tinh_sinh_thai": "Cây gỗ lớn ưa sáng mọc trên đồi đất Feralit tầng dày thoát nước tốt, quả hình thoi hai đầu nhọn khi chín có màu vàng nhạt vị chua chát ngọt hậu giàu vitamin C và chất chống oxy hóa, dùng muối chua hoặc làm mứt trám truyền thống.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Thán thư thâm đốm cuống quả trám trắng",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Colletotrichum gloeosporioides"
                    },
                    "trieu_chung_dien_hinh": [
                        "Cuống quả và quả non xuất hiện những đốm đen nhỏ lõm sâu",
                        "Vết thâm lan rộng làm cuống quả bị thắt nghẽn khô đen, quả non rụng lả tả dưới gốc",
                        "Trên vỏ quả xuất hiện các đốm tròn thâm nâu đồng tâm mô cùi bên dưới bị sượng cứng",
                        "Lá già xuất hiện các vệt cháy thán thư màu nâu đỏ làm rách thủng phiến lá"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Rụng quả sinh lý do thiếu Bo: Thiếu Bo quả rụng cuống vẫn xanh tươi; Thán thư cuống quả thâm đen teo tóp có ổ bào tử nấm hồng cam khi ẩm.",
                    "kiem_tra_thuc_dia": "Nhặt quả trám non rụng thấy cuống quả bị thâm đen khô giòn, soi kính lúp thấy các chấm bào tử nấm màu hồng cam li ti.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt tỉa cành thông thoáng sau thu hoạch, dọn sạch tàn dư dưới gốc cây.",
                        "sinh_hoc": "Phun phòng bằng chế phẩm nấm đối kháng Bacillus subtilis kết hợp Nano Chitosan.",
                        "khuyen_cao_chuyen_gia": "Phun luân phiên Mancozeb hoặc Difenoconazole giai đoạn hoa nở rộ và đậu quả non."
                    }
                },
                {
                    "ten_benh": "Bệnh Rầy cánh phấn chích đọt non trám trắng",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Côn trùng chích hút",
                        "ten_khoa_hoc": "Aleurocanthus spiniferus"
                    },
                    "trieu_chung_dien_hinh": [
                        "Rầy cánh phấn đen và ấu trùng bám dày đặc ở mặt dưới phiến lá non và chồi lộc",
                        "Chích hút dịch nhựa non làm lá non bị xoăn queo vàng úa, chồi lộc cằn cỗi",
                        "Tiết ra dịch mật ngọt làm nấm bồ hóng đen phát triển phủ kín mặt lá",
                        "Cây bị suy giảm khả năng quang hợp nghiêm trọng"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Muội than do rệp sáp: Rầy cánh phấn có con trưởng thành nhỏ li ti cánh màu đen viền trắng bay rào rào khi rung cành.",
                    "kiem_tra_thuc_dia": "Lật mặt dưới lá non thấy hàng trăm con rầy nhỏ li ti bám thành đám, rung cành thấy rầy bay tỏa ra xung quanh.",
                    "phac_do_vietgap": {
                        "canh_tac": "Bảo vệ các loài bọ rùa và ong ký sinh tự nhiên trong vườn cây.",
                        "sinh_hoc": "Phun dầu khoáng SK Enspray 99EC loãng 0.5% hoặc chế phẩm nấm ký sinh Beauveria bassiana.",
                        "khuyen_cao_chuyen_gia": "Phun trừ bằng thuốc trừ sâu sinh học Abamectin hoặc Spirotetramat khi mật độ rầy cao."
                    }
                }
            ]
        },
        {
            "id": "w1_060",
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": "Hạt dẻ Trùng Khánh Cao Bằng",
            "scientific_name": "Castanea mollissima Blume cv. Trung Khanh",
            "dia_ban_pho_bien": ["Trùng Khánh", "Quảng Hòa", "Cao Bằng"],
            "dac_tinh_sinh_thai": "Cây ăn hạt đặc sản nức tiếng vùng biên cương phía Bắc, ưa độ cao 500 - 800m đất Feralit trên đá vôi giàu mùn canxi, quả có lớp vỏ gai nhọn bọc 1-3 hạt dẻ to mẩy màu nâu sẫm bóng bẩy, nhân hạt dẻ vàng ươm thơm ngậy bùi ngọt đậm đà khi nướng luộc.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Bỏng khô loét vỏ thân dẻ Trùng Khánh",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Cryphonectria parasitica (Endothia parasitica)"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vỏ thân cành cây dẻ xuất hiện các vết loét hình bầu dục màu nâu cam sưng phồng lên nứt nẻ",
                        "Bên dưới vết loét mô vỏ bị thối khô màu nâu đỏ ăn sâu vào tầng mô gỗ bít tắc mạch dẫn",
                        "Lá trên cành bị héo khô chuyển sang màu nâu vàng úa dính chặt trên cây không rụng",
                        "Cành dẻ bị chết khô giòn dễ gãy, toàn bộ cây dẻ cổ thụ bị suy tàn chết đứng chỉ sau 1-2 năm"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Xì mủ do sâu đục vỏ: Sâu đục vỏ có vết đục cơ giới đùn mạt cưa phân sâu li ti; Cryphonectria vỏ phồng rộp nứt nẻ màu nâu cam có các đốm nấm mụn nhỏ li ti màu vàng cam không có mạt cưa.",
                    "kiem_tra_thuc_dia": "Lấy dao rạch nhẹ vào mép vết loét thấy mô vỏ bên dưới có màu nâu đỏ cam khô xác, có các sợi tơ nấm màu vàng nhạt đan xen.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt bỏ cành bệnh sâu dưới vết loét 30cm đem đốt tiêu hủy ngay; khử trùng vết cắt bằng dung dịch sát khuẩn.",
                        "sinh_hoc": "Sử dụng các chủng nấm giảm độc lực (hypovirulent strains) để cấy truyền kiểm soát sinh học nấm độc lực cao.",
                        "khuyen_cao_chuyen_gia": "Quét gốc và cành thân bằng Bordeaux 2% hoặc Thiophanate-Methyl vào đầu mùa xuân."
                    }
                },
                {
                    "ten_benh": "Bệnh Vòi voi đục hạt dẻ non",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Côn trùng gây hại",
                        "ten_khoa_hoc": "Curculio elephas"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vòi voi trưởng thành dùng vòi dài khoan lỗ đẻ trứng xuyên qua lớp gai nhọn vào hạt dẻ non",
                        "Ấu trùng sâu non màu trắng ngà nở ra ăn rỗng nhân hạt dẻ thải ra các hạt phân màu nâu đen",
                        "Quả dẻ bị rụng non hoặc khi thu hoạch hạt dẻ bị rỗng ruột thối đen bên trong",
                        "Làm giảm mạnh tỷ lệ hạt dẻ đạt chuẩn thương phẩm xuất khẩu"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bệnh nấm thối hạt: Vòi voi để lại một lỗ đục tròn nhỏ li ti trên vỏ hạt dẻ có phân sâu bên trong ruột rỗng.",
                    "kiem_tra_thuc_dia": "Lắc nhẹ hạt dẻ thấy lóc cóc ruột lỏng, tách vỏ hạt thấy con sâu non màu trắng béo mầm đang nằm ăn nhân hạt dẻ.",
                    "phac_do_vietgap": {
                        "canh_tac": "Thu gom toàn bộ quả rụng sớm đem xử lý diệt ấu trùng trước khi sâu chui xuống đất làm nhộng.",
                        "sinh_hoc": "Rải chế phẩm nấm ký sinh côn trùng Metarhizium anisopliae hoặc Beauveria bassiana quanh đất gốc cây để diệt nhộng đất.",
                        "khuyen_cao_chuyen_gia": "Phun trừ vòi voi trưởng thành bằng thuốc sinh học Abamectin khi cây dẻ vừa kết thúc giai đoạn hoa rụng cánh."
                    }
                }
            ]
        },
        {
            "id": "w1_061",
            "topic": "Cay_Lam_Nghiep_Duoc_Lieu_Quy",
            "name_vi": "Trà hoa vàng Ba Chẽ Quảng Ninh",
            "scientific_name": "Camellia petelotii (Merr.) Sealy",
            "dia_ban_pho_bien": ["Ba Chẽ", "Tiên Yên", "Hải Hà", "Quảng Ninh", "Tam Đảo", "Vĩnh Phúc"],
            "dac_tinh_sinh_thai": "Cây trà hoa vàng mệnh danh là 'Nữ hoàng của các loài trà', mọc tự nhiên dưới tán rừng ẩm ven suối khe núi độ cao 200 - 800m, đất Feralit giàu mùn tơi xốp, hoa màu vàng óng ả cánh sáp dày chứa hơn 400 hoạt chất quý chống ung thư và hạ mỡ máu thượng hạng.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Đốm than đen đục lá trà hoa vàng",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Colletotrichum camelliae"
                    },
                    "trieu_chung_dien_hinh": [
                        "Phiến lá da dày xuất hiện những đốm tròn màu nâu đen có viền lượn sóng rõ rệt",
                        "Tâm vết bệnh bị khô xám bạc, có các chấm đen nhỏ li ti là ổ bào tử nấm",
                        "Búp nụ hoa màu vàng óng bị các đốm thâm đen làm thui chột không nở được thành hoa sáp",
                        "Lá già bị khô cháy mép rụng sớm làm giảm năng suất thu hái búp lá làm trà túi lọc"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bệnh cháy lá do nắng chiếu gắt: Cháy nắng vết màu vàng rơm khô phẳng lì; Thán thư đốm tròn có vân đồng tâm và có các chấm đen ổ bào tử nấm li ti.",
                    "kiem_tra_thuc_dia": "Vò nhẹ mép lá thấy mô lá giòn rụm thủng lỗ rách, soi kính lúp thấy các chấm bào tử nấm li ti trên nền lá bạc.",
                    "phac_do_vietgap": {
                        "canh_tac": "Trồng dưới tán che bóng 50-60%, không để ánh nắng mặt trời chiếu trực tiếp gắt gao lên tán lá trà hoa vàng.",
                        "sinh_hoc": "Phun phòng bằng chế phẩm nấm đối kháng Chaetomium kết hợp Nano Bạc Đồng 400ppm bảo vệ nụ hoa vàng.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bằng Difenoconazole hoặc Antracol 70WP giai đoạn nụ hoa bắt đầu nhú từ nách lá."
                    }
                },
                {
                    "ten_benh": "Bệnh Thối rễ ngập úng nấm Phytophthora",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Phytophthora cinnamomi"
                    },
                    "trieu_chung_dien_hinh": [
                        "Bộ rễ tơ và rễ cọc dưới đất bị sũng nước thối đen mục nát vỏ rễ",
                        "Lá trà hoa vàng bị mất độ bóng xanh chuyển sang màu vàng xám héo rũ",
                        "Cành ngọn bị khô tóp từ trên xuống, cây chết rũ đứng giữa vườn ươm hoặc tán rừng",
                        "Cắt ngang gốc thân thấy vòng mô mạch dẫn chuyển màu nâu đen thâm tím bốc mùi chua"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Nghẹt rễ sinh lý do nén dẽ: Nghẹt rễ rễ bị đen vỏ ngoài nhưng lõi rễ vẫn dai trắng; Phytophthora toàn bộ vỏ và lõi rễ mủn nát tuột vỏ bốc mùi hôi thối mục nát.",
                    "kiem_tra_thuc_dia": "Cào lớp đất quanh gốc thấy rễ tơ bị mủn nát trơn nhớt màu đen, bóp nhẹ thấy nước chua rỉ ra đầu ngón tay.",
                    "phac_do_vietgap": {
                        "canh_tac": "Lên luống cao, đắp gờ thoát nước triệt để quanh gốc khóm trà hoa vàng, không để ứ đọng nước mưa.",
                        "sinh_hoc": "Tưới phòng gốc bằng hỗn hợp men vi sinh đối kháng Trichoderma harzianum kết hợp Bacillus subtilis định kỳ hàng tháng.",
                        "khuyen_cao_chuyen_gia": "Tưới thuốc trừ nấm Phosphonate hữu cơ hoặc Ridomil Gold 68WG ngay khi chớm có dấu hiệu héo đọt non."
                    }
                }
            ]
        },
        {
            "id": "w1_062",
            "topic": "Cay_Lam_Nghiep_Duoc_Lieu_Quy",
            "name_vi": "Hồi Lạng Sơn cổ thụ",
            "scientific_name": "Illicium verum Hook.f.",
            "dia_ban_pho_bien": ["Văn Quan", "Bình Gia", "Chi Lăng", "Lạng Sơn", "Quảng Ninh"],
            "dac_tinh_sinh_thai": "Cây gỗ lâm sản ngoài gỗ biểu tượng kinh tế xứ Lạng, cao 10-15m, ưa độ cao 300 - 800m đất Feralit phong hóa từ đá biến chất giàu mùn, hoa quả hình ngôi sao 6-8 cánh thơm nức mùi tinh dầu Anethole xuất khẩu toàn cầu.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Thán thư rụng hoa quả sao hồi non",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Colletotrichum gloeosporioides"
                    },
                    "trieu_chung_dien_hinh": [
                        "Hoa hồi và các cánh sao quả non xuất hiện những chấm nâu đen nhỏ lõm sâu",
                        "Vết thâm lan rộng làm cuống quả bị thắt nghẽn thâm đen, quả sao non rụng lả tả trắng gốc rừng",
                        "Quả hồi trưởng thành bị các đốm thâm đen làm méo mó các cánh sao, giảm hàm lượng tinh dầu anethole",
                        "Lá hồi xuất hiện các mảng cháy thán thư màu nâu đỏ giòn rách"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Rụng quả sinh lý do khô hạn: Rụng hạn cuống quả khô vàng rụng tự nhiên; Thán thư cuống và cánh sao thâm đen lõm sâu có ổ bào tử nấm hồng cam khi ẩm.",
                    "kiem_tra_thuc_dia": "Nhặt quả sao non rụng thấy cuống và cánh sao bị thâm đen sì, soi kính lúp thấy các đĩa bào tử nấm li ti.",
                    "phac_do_vietgap": {
                        "canh_tac": "Phát quang cỏ dại bụi rậm quanh gốc cây hồi cổ thụ tạo độ thông thoáng đón gió sườn đồi.",
                        "sinh_hoc": "Phun phòng bằng chế phẩm nấm đối kháng Chaetomium kết hợp Nano Chitosan kích kháng sinh học.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bằng Antracol 70WP hoặc Difenoconazole giai đoạn trước khi hoa nở và sau khi đậu quả sao non."
                    }
                },
                {
                    "ten_benh": "Bệnh Bọ ánh kim cắn phá hoa đọt hồi",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Côn trùng gây hại",
                        "ten_khoa_hoc": "Chrysolina spp."
                    },
                    "trieu_chung_dien_hinh": [
                        "Bọ cánh cứng màu ánh kim xanh lục óng ánh bu bám cắn phá cánh hoa và đọt non cây hồi",
                        "Hoa hồi bị cắn nham nhở làm rụng hoa không thể thụ phấn tạo quả sao",
                        "Đọt non bị cắn cụt ngọn làm cây còi cọc chùn lộc",
                        "Xuất hiện thành từng đàn lớn vào mùa xuân hè tàn phá các đồi rừng hồi"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bệnh nấm: Bọ ánh kim nhìn thấy rõ bằng mắt thường, thân óng ánh màu kim loại bay lượn và bò trên cành hoa để lại vết cắn nham nhở cơ giới.",
                    "kiem_tra_thuc_dia": "Rung nhẹ cành hồi thấy các con bọ cánh cứng màu xanh kim loại rơi lả tả xuống đất hoặc xòe cánh bay vù vù.",
                    "phac_do_vietgap": {
                        "canh_tac": "Hun khói xua đuổi bọ ánh kim vào sáng sớm khi đàn bọ bắt đầu xuất hiện.",
                        "sinh_hoc": "Phun chế phẩm nấm ký sinh Beauveria bassiana hoặc nấm xanh Metarhizium để tiêu diệt bọ cánh cứng.",
                        "khuyen_cao_chuyen_gia": "Phun trừ bằng thuốc trừ sâu sinh học Abamectin hoặc Emamectin benzoate khi mật độ bọ cao."
                    }
                }
            ]
        },
        {
            "id": "w1_063",
            "topic": "Cay_Lam_Nghiep_Duoc_Lieu_Quy",
            "name_vi": "Hạt mắc mật Lạng Sơn",
            "scientific_name": "Clausena indica (Dalzell) Oliv.",
            "dia_ban_pho_bien": ["Bình Gia", "Văn Quan", "Bắc Sơn", "Lạng Sơn", "Cao Bằng"],
            "dac_tinh_sinh_thai": "Cây gỗ nhỏ bản địa quý giá mọc trên núi đá vôi, lá và quả chứa nhiều tinh dầu thơm nồng quyến rũ không thể thiếu trong món vịt quay lợn quay Lạng Sơn, quả mọng hình cầu mọc chùm khi chín có màu trắng trong mọng nước ngọt thanh dịu mát.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Rầy chổng cánh chích lá hoa mắc mật",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Côn trùng chích hút",
                        "ten_khoa_hoc": "Diaphorina citri"
                    },
                    "trieu_chung_dien_hinh": [
                        "Rầy chổng cánh non và trưởng thành bám dày đặc ở mặt dưới đọt non và cuống chùm hoa mắc mật",
                        "Chích hút dịch nhựa non làm lá non bị xoăn queo vàng úa, hoa rụng hàng loạt",
                        "Tiết ra các sợi sáp màu trắng xoắn tít bám quanh chồi lộc non",
                        "Tiết dịch mật ngọt làm nấm muội đen bồ hóng phát triển phủ kín tán lá làm giảm quang hợp"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Rầy mềm: Rầy chổng cánh khi đậu có tư thế chổng mông lên một góc 45 độ so với mặt lá rất đặc thù; Rầy mềm thân tròn béo mầm bò chậm chạp không chổng mông.",
                    "kiem_tra_thuc_dia": "Quan sát đọt non thấy các con rầy màu nâu xám đậu vểnh đuôi lên góc 45 độ, có các sợi sáp trắng xoắn tít bám quanh nách lá.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt tỉa cành thông thoáng, bảo vệ kiến vàng và bọ rùa săn mồi tự nhiên.",
                        "sinh_hoc": "Phun dầu khoáng sinh học SK Enspray 99EC loãng 0.5% kết hợp nấm ký sinh Beauveria bassiana.",
                        "khuyen_cao_chuyen_gia": "Phun trừ bằng thuốc sinh học Abamectin hoặc Spirotetramat khi phát hiện rầy nhú đợt lộc non."
                    }
                },
                {
                    "ten_benh": "Bệnh Thán thư đốm cháy chùm quả mắc mật",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Colletotrichum gloeosporioides"
                    },
                    "trieu_chung_dien_hinh": [
                        "Trên các quả mọng mắc mật xuất hiện những đốm đen tròn nhỏ lõm sâu",
                        "Vết thâm lan rộng làm quả bị nhũn thối nứt toác chảy dịch quả dính nhớt",
                        "Chùm quả bị thâm đen teo tóp khô quắt lại trên cành làm rụng quả non hàng loạt",
                        "Lá già xuất hiện các vệt cháy thán thư màu nâu đỏ làm rách thủng phiến lá"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Quả chín nứt sinh lý: Nứt sinh lý vết nứt tự nhiên thịt quả vẫn trắng trong thơm ngọt; Thán thư vỏ quả lõm sâu thâm đen bốc mùi lên men chua thối.",
                    "kiem_tra_thuc_dia": "Dùng tay bóp nhẹ quả mọng thấy vỏ lõm nát chảy dịch nhầy thâm đen bốc mùi men chua.",
                    "phac_do_vietgap": {
                        "canh_tac": "Thu dọn chùm quả thối đem chôn sâu, vệ sinh tán cây trước vụ quả mới.",
                        "sinh_hoc": "Phun Nano Bạc Chitosan phòng trừ mầm nấm bề mặt quả giai đoạn chuyển màu trắng trong.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bằng Difenoconazole hoặc Antracol 70WP trước khi thu hoạch 15 ngày."
                    }
                }
            ]
        }
    ]
