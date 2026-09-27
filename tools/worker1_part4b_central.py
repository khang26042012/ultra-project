# -*- coding: utf-8 -*-
"""
Worker 1 - Part 4b: Miền Trung tiếp theo (Crops 89 to 100)
Sen Tịnh Tâm, Trầm hương Tiên Phước, Quế Trà Bồng, Sâm Ngọc Linh, Đẳng sâm Tây Giang, Chè dây Quảng Bình, Sâm Bố Chính, Cà gai leo Quảng Trị, Xoài Cam Lâm, Nho đỏ Ninh Thuận, Măng tây xanh, Tràm gió Huế
"""

def get_part4b_crops():
    return [
        {
            "id": "w1_089",
            "topic": "Cay_Lam_Nghiep_Duoc_Lieu_Quy",
            "name_vi": "Sen Tịnh Tâm hoàng cung Huế",
            "scientific_name": "Nelumbo nucifera Gaertn. cv. Tinh Tam Hue",
            "dia_ban_pho_bien": ["Hồ Tịnh Tâm", "Thành phố Huế", "Phú Vang", "Thừa Thiên Huế"],
            "dac_tinh_sinh_thai": "Giống sen trắng hồng cổ truyền tiến vua của hoàng cung triều Nguyễn, sinh trưởng trong bùn non đầm lầy hồ Tịnh Tâm sâu 0.6 - 1.2m, củ sen dẻo bở hạt sen tròn mẩy thơm bùi ngọt ngào vị hoàng tộc, dùng ướp trà sen tiến vua đỉnh cao phong vị cố đô.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Đốm mắt nâu rách phiến lá sen Tịnh Tâm",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Cercospora nelumbonis"
                    },
                    "trieu_chung_dien_hinh": [
                        "Phiến lá sen xuất hiện những chấm tròn nhỏ màu nâu sẫm tâm xám nhạt",
                        "Vết bệnh lan rộng làm mô lá bị khô giòn nứt toác rách thủng lỗ chỗ",
                        "Cánh hoa sen bị thâm đốm làm hoa thui chột không nở được, mất hoàn toàn hương thơm ướp trà hoàng cung",
                        "Gương sen non bị chai sượng hạt lép đen"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bọ trĩ cào rách lá sen: Bọ trĩ làm gân lá gồ ghề quăn mép bạc màu sờ ram ráp; Cercospora tạo các đốm thủng tròn đồng tâm rõ ràng có viền tía đỏ.",
                    "kiem_tra_thuc_dia": "Nhìn mặt lá sen nghiêng dưới ánh sáng thấy tâm vết đốm bị hoại tử thủng lỗ tròn đường kính 3-8mm như bị tàn hương châm.",
                    "phac_do_vietgap": {
                        "canh_tac": "Vớt bỏ lá già lá bệnh trên mặt hồ, dọn sạch rong rêu đáy hồ tạo lưu thông ánh sáng.",
                        "sinh_hoc": "Phun chế phẩm nấm đối kháng Chaetomium kết hợp dịch chiết vỏ tôm Chitosan nano an toàn với cá cảnh hồ sen.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bằng hoạt chất Azoxystrobin hoặc Difenoconazole nồng độ an toàn trước vụ trổ bông rộ."
                    }
                },
                {
                    "ten_benh": "Bệnh Thối đen củ ngó bùn hồ Tịnh Tâm",
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
                    "phan_biet_chan_doan_kep": "Phân biệt with Hiện tượng ngộ độc khí bùn (H2S, CH4): Ngộ độc khí rễ củ thâm đen toàn bộ bề mặt nhưng rửa sạch mùi bùn vẫn rắn chắc; Bệnh nấm Fusarium thịt củ bên trong thối đen phân hủy rữa nát có mạch thâm tím sẫm.",
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
            "id": "w1_090",
            "topic": "Cay_Lam_Nghiep_Duoc_Lieu_Quy",
            "name_vi": "Trầm hương Dó bầu Tiên Phước Quảng Nam",
            "scientific_name": "Aquilaria crassna Pierre ex Lecomte cv. Tien Phuoc",
            "dia_ban_pho_bien": ["Tiên Phước", "Nông Sơn", "Quảng Nam", "Khánh Hòa", "Bình Định"],
            "dac_tinh_sinh_thai": "Cây gỗ lâm nghiệp đặc hữu quý giá bậc nhất thế giới 'Xứ Trầm hương', cao 15-30m, ưa đất Feralit đồi núi dốc giàu mùn rừng nhiệt đới, thân cây khi bị tổn thương do cơ giới hoặc nấm bệnh sẽ tiết ra chất nhựa thơm kỳ diệu ngưng kết thành Trầm hương và Kỳ nam vô giá.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Sâu đục thân Dó bầu tạo vết khuyết",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Côn trùng gây hại",
                        "ten_khoa_hoc": "Heortia vitessoides"
                    },
                    "trieu_chung_dien_hinh": [
                        "Sâu non ăn trụi lá non và đọt non cây Dó bầu chỉ trong vài ngày, làm trơ cành que trơ trụi",
                        "Ấu trùng sâu đục khoét lớp vỏ thân và cành tạo ra các vết loét nứt vỏ cây",
                        "Cây bị suy kiệt giảm khả năng quang hợp và làm chậm quá trình tạo trầm tự nhiên",
                        "Xuất hiện thành dịch lớn vào đầu mùa mưa làm chết hàng loạt cây con vườn ươm"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Vết cấy vi sinh tạo trầm chủ động: Vết cấy chủ động lỗ khoan cơ giới thẳng thớm có ống dẫn chế phẩm sinh học; Vết sâu đục nham nhở không theo trật tự và có phân sâu mạt lá đùn ra.",
                    "kiem_tra_thuc_dia": "Quan sát mặt lá thấy hàng trăm con sâu róm màu xanh sọc đen đang ăn ngấu nghiến phiến lá, phân sâu rơi lộp độp như mưa rào.",
                    "phac_do_vietgap": {
                        "canh_tac": "Vệ sinh dọn sạch cỏ dại dưới tán cây, bẫy đèn bắt bướm trưởng thành vào ban đêm.",
                        "sinh_hoc": "Phun chế phẩm vi sinh Bacillus thuringiensis (Bt) hoặc nấm ký sinh Beauveria bassiana diệt sâu non an toàn.",
                        "khuyen_cao_chuyen_gia": "Phun trừ bằng thuốc trừ sâu sinh học Emamectin benzoate hoặc Abamectin khi sâu non mới nở tuổi 1-2."
                    }
                },
                {
                    "ten_benh": "Bệnh Thán thư cháy lá mầm cây con Dó bầu",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Colletotrichum gloeosporioides"
                    },
                    "trieu_chung_dien_hinh": [
                        "Lá mầm và lá non cây con trong vườn ươm xuất hiện các đốm thâm nâu tròn viền đỏ tía",
                        "Tâm vết bệnh bị khô giòn rách thủng lỗ chỗ, mép lá bị cháy khô cong queo",
                        "Cây con trong vườn ươm bị rụng lá trơ trụi cành làm chết hàng loạt bầu ươm",
                        "Cành non bị khô tóp từ ngọn xuống làm chùn đọt ngừng sinh trưởng"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Cháy nắng lá vườn ươm: Cháy nắng vết màu vàng rơm khô phẳng; Thán thư có vân đồng tâm sắc nét và có chấm bào tử nấm hồng cam khi ẩm.",
                    "kiem_tra_thuc_dia": "Vò nhẹ phiến lá thấy giòn vụn rách toạc, soi kính lúp thấy các chấm bào tử nấm màu hồng cam li ti.",
                    "phac_do_vietgap": {
                        "canh_tac": "Kê luống vườn ươm thông thoáng đón gió, giảm bớt độ che bóng khi cây con đã bén rễ.",
                        "sinh_hoc": "Phun phòng bằng chế phẩm vi sinh Bacillus subtilis kết hợp Nano Bạc Đồng 400ppm.",
                        "khuyen_cao_chuyen_gia": "Phun phòng trừ bằng Mancozeb hoặc Difenoconazole định kỳ 10 ngày trong mùa mưa phùn."
                    }
                }
            ]
        },
        {
            "id": "w1_091",
            "topic": "Cay_Lam_Nghiep_Duoc_Lieu_Quy",
            "name_vi": "Quế Trà Bồng Quảng Ngãi xuất khẩu",
            "scientific_name": "Cinnamomum cassia (L.) J.Presl cv. Tra Bong",
            "dia_ban_pho_bien": ["Trà Bồng", "Tây Trà", "Quảng Ngãi", "Bắc Trà My", "Quảng Nam"],
            "dac_tinh_sinh_thai": "Cây gỗ lâm sản ngoài gỗ xuất khẩu chủ lực của đồng bào Cor, cao 15-20m, ưa độ cao 300 - 900m đất Feralit đỏ vàng trên đá mẹ macma, vỏ thân dày xốp chứa hàm lượng cinnamaldehyde cực cao cay nồng ngọt đậm thơm ngát lừng danh thị trường Mỹ, châu Âu.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Loét sùi u nốt vỏ quế xuất khẩu",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Phytophthora cinnamomi"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vỏ thân cây quế xuất hiện các vết nứt sùi màu nâu đen, rỉ dịch mủ màu nâu đỏ dẻo quánh",
                        "Mô vỏ dưới vết nứt bị thối mục mủn nát phá hủy cấu trúc tế bào dầu thơm",
                        "Vỏ quế bị chai sượng sần sùi không thể bóc thành thanh quế sáo xuất khẩu được",
                        "Lá trên cành bị héo vàng và rụng dần làm cây quế bị chết khô đứng giữa rừng"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Vết cạo vỏ thử dầu của người dân: Vết cạo cơ giới phẳng liền sẹo mịn màng; Nấm loét vỏ mép nứt sùi nham nhở thối mục nát bốc mùi hôi chua.",
                    "kiem_tra_thuc_dia": "Lấy dao bóc thử mảng vỏ bệnh thấy mô vỏ bên dưới thâm đen nhũn ướt, chất dầu quế bị biến chất đắng ngắt.",
                    "phac_do_vietgap": {
                        "canh_tac": "Phát quang cỏ dại quanh gốc cây quế, khơi rãnh thoát nước sâu sườn đồi không để đọng nước mùa mưa bão.",
                        "sinh_hoc": "Quét vôi tôi trộn chế phẩm nấm đối kháng Chaetomium lên thân cây cao 1.5m vào đầu mùa mưa.",
                        "khuyen_cao_chuyen_gia": "Quét gốc hoặc phun thân bằng Aliette 800WG, Metalaxyl-M hoặc Ridomil Gold khi phát hiện vết loét sùi đầu tiên."
                    }
                },
                {
                    "ten_benh": "Bệnh Sâu đo ăn trụi tán lá quế",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Côn trùng gây hại",
                        "ten_khoa_hoc": "Culcula panterinaria"
                    },
                    "trieu_chung_dien_hinh": [
                        "Sâu non dạng sâu đo màu nâu xám ngụy trang giống cành cây nhỏ ăn ngấu nghiến phiến lá quế",
                        "Ăn từ mép lá vào gân chính làm toàn bộ tán cây quế bị trơ que trơ cành chỉ trong vài tuần",
                        "Cây quế bị suy kiệt ngừng sinh trưởng vỏ cây mỏng dính không tích lũy được tinh dầu",
                        "Xuất hiện thành dịch lớn trên diện tích hàng ngàn hécta rừng quế Trà Bồng"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bệnh rụng lá do nấm: Rụng lá nấm lá vàng úa rơi xuống đất; Sâu đo cắn phá lá bị khuyết nham nhở vết cắn cơ giới và nhìn thấy sâu đo ngụy trang bám dọc cành que.",
                    "kiem_tra_thuc_dia": "Rung nhẹ cành quế thấy các con sâu đo cong mình nhả tơ rơi lơ lửng giữa không trung, phân sâu rơi đen sì mặt đất dưới gốc cây.",
                    "phac_do_vietgap": {
                        "canh_tac": "Bảo vệ các loài chim sâu, kiến vàng và ong ký sinh tự nhiên trong rừng quế.",
                        "sinh_hoc": "Phun chế phẩm sinh học vi khuẩn Bacillus thuringiensis (Bt) hoặc nấm ký sinh Beauveria bassiana.",
                        "khuyen_cao_chuyen_gia": "Phun trừ bằng thuốc sinh học Emamectin benzoate hoặc Abamectin khi sâu non tuổi 1-2 mới nở."
                    }
                }
            ]
        },
        {
            "id": "w1_092",
            "topic": "Cay_Lam_Nghiep_Duoc_Lieu_Quy",
            "name_vi": "Sâm Ngọc Linh Nam Trà My Quảng Nam",
            "scientific_name": "Panax vietnamensis Ha et Grushv. cv. Nam Tra My",
            "dia_ban_pho_bien": ["Nam Trà My", "Quảng Nam", "Tu Mơ Rông", "Đăk Glei", "Kon Tum"],
            "dac_tinh_sinh_thai": "Quốc bảo của Việt Nam 'Sâm tốt nhất thế giới', sinh trưởng dưới tán rừng già nguyên sinh đỉnh núi Ngọc Linh độ cao 1.500 - 2.500m quanh năm sương mù bao phủ, đất thảm mục rêu phong giàu mùn rừng, củ sâm chứa 52 hợp chất saponin (trong đó có 26 saponin MR2 cấu trúc mới độc nhất vô nhị) chữa suy nhược thần kinh và tăng cường miễn dịch thần kỳ.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Rỉ sắt đốm nâu đỏ lá cành sâm Ngọc Linh",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Puccinia panacis"
                    },
                    "trieu_chung_dien_hinh": [
                        "Mặt dưới phiến lá sâm xuất hiện các nốt mụn sưng nhỏ li ti màu nâu đỏ như rỉ sắt gỉ đồng",
                        "Mặt trên lá tương ứng xuất hiện các đốm tròn màu vàng nhạt hơi nhô gồ ghề",
                        "Bột phấn nấm màu nâu đỏ bám dính dày đặc vào tay khi chạm vào",
                        "Lá già bị khô cháy vàng từng chòm và rụng sớm làm trơ cuống lá sâm quý giá"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bệnh cháy lá do gió lạnh: Cháy lạnh lá khô giòn viền mép đồng loạt; Bệnh rỉ sắt là các ổ mụn nâng cao bề mặt giải phóng bụi phấn nấm màu nâu đỏ đặc trưng.",
                    "kiem_tra_thuc_dia": "Lấy tay quẹt nhẹ qua đám mụn mặt dưới lá thấy bụi phấn màu nâu đỏ dính đầy trên đầu ngón tay.",
                    "phac_do_vietgap": {
                        "canh_tac": "Dọn dẹp lá rụng quanh gốc sâm, tạo độ thông thoáng dưới tán rừng già không để độ ẩm ứ đọng quá cao.",
                        "sinh_hoc": "Phun phòng bằng chế phẩm nấm đối kháng Trichoderma kết hợp Nano Bạc Đồng 300ppm bảo vệ vòm lá sâm.",
                        "khuyen_cao_chuyen_gia": "Phun trừ bằng Hexaconazole (Anvil 5SC) hoặc Difenoconazole khi phát hiện các mụn rỉ sắt đầu tiên."
                    }
                },
                {
                    "ten_benh": "Bệnh Thối rễ củ nấm mốc trắng sâm tự nhiên",
                    "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Rhizoctonia solani / Phytophthora cactorum"
                    },
                    "trieu_chung_dien_hinh": [
                        "Củ rễ sâm dưới thảm mùn rừng bị sũng nước thâm đen, mô thịt củ bị rữa nát thành bột nhão xám tro",
                        "Trên bề mặt củ bị thối mọc lên lớp sợi tơ nấm màu trắng ngà mịn màng",
                        "Cuống lá sâm bị thâm teo tóp ngã rạp xuống thảm rêu, lá úa vàng đột ngột",
                        "Làm mất trắng những củ sâm Ngọc Linh quý hiếm có tuổi đời hàng chục năm giá trị hàng trăm triệu đồng"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Ngủ đông sinh lý: Khi ngủ đông tự nhiên thân lá vàng khô tự rụng ráo trọi nhưng củ rễ vẫn rắn chắc thơm nồng; Bệnh thối củ thì củ nhũn nát có mùi chua thối hư hỏng.",
                    "kiem_tra_thuc_dia": "Bới lớp mùn rêu thấy thân củ sâm bị mềm nhũn mủn rữa, bóp nhẹ thấy nước thối rỉ ra không còn mùi thơm sâm đặc trưng.",
                    "phac_do_vietgap": {
                        "canh_tac": "Trồng trên luống đất dốc thoát nước tối ưu lót xơ dừa mùn thông, che mái nilon chắn mưa xối trực tiếp.",
                        "sinh_hoc": "Tưới phòng định kỳ bằng chế phẩm men vi sinh đối kháng Trichoderma kết hợp xạ khuẩn Streptomyces chuyên tính cho cây sâm núi.",
                        "khuyen_cao_chuyen_gia": "Xử lý đất và tưới gốc bằng Metalaxyl-M hoặc Phosphonate hữu cơ khi có đợt mưa rừng kéo dài."
                    }
                }
            ]
        },
        {
            "id": "w1_093",
            "topic": "Cay_Lam_Nghiep_Duoc_Lieu_Quy",
            "name_vi": "Đẳng sâm Tây Giang Quảng Nam",
            "scientific_name": "Codonopsis javanica (Blume) Hook.f. & Thomson cv. Tay Giang",
            "dia_ban_pho_bien": ["Tây Giang", "Nam Giang", "Đông Giang", "Quảng Nam", "A Lưới", "Thừa Thiên Huế"],
            "dac_tinh_sinh_thai": "Cây dược liệu dây leo 'Sâm của người nghèo' vùng cao dãy Trường Sơn 800 - 1.600m, ưa khí hậu mát lạnh ẩm ướt, đất Feralit giàu mùn tơi xốp, củ nạc dài nhiều rễ phụ chứa nhiều đường saponin bồi bổ tỳ vị tuyệt vời.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Đốm than thán thư phiến lá dây leo đẳng sâm",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Colletotrichum sp."
                    },
                    "trieu_chung_dien_hinh": [
                        "Phiến lá xuất hiện những đốm tròn màu nâu xám có vân đồng tâm gờ nổi rõ ràng",
                        "Tâm vết bệnh bị khô xám bạc, có các chấm đen nhỏ li ti là ổ bào tử nấm",
                        "Mép và chóp lá bị cháy khô cong queo giòn rách làm giảm quang hợp nuôi củ",
                        "Dây leo bị rụng lá trơ trụi cành làm giảm tích lũy dưỡng chất nuôi củ"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Cháy nắng lá chè: Cháy nắng vết màu vàng rơm đồng nhất không có vân đồng tâm và không có chấm đen li ti ổ bào tử nấm.",
                    "kiem_tra_thuc_dia": "Vò nhẹ vết đốm xám trên lá thấy giòn vụn, soi kính lúp thấy các chấm đen nhỏ nổi gồ trên nền lá bạc.",
                    "phac_do_vietgap": {
                        "canh_tac": "Làm giàn leo thông thoáng, tỉa bớt cành nhánh phụ rậm rạp đón gió.",
                        "sinh_hoc": "Phun phòng bằng chế phẩm Nano Bạc Đồng 300ppm kết hợp Chitosan kích kháng màng tế bào.",
                        "khuyen_cao_chuyen_gia": "Phun phòng trừ bằng Antracol 70WP hoặc Mancozeb khi mưa phùn kéo dài."
                    }
                },
                {
                    "ten_benh": "Bệnh Lở cổ rễ thối dây leo nấm Sclerotium",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Sclerotium rolfsii"
                    },
                    "trieu_chung_dien_hinh": [
                        "Đoạn thân dây leo sát mặt đất bị thâm đen úng nước, vỏ thân tróc lở mục nát",
                        "Quanh gốc thân xuất hiện lớp màng tơ nấm màu trắng muốt như sợi bông gòn bao phủ",
                        "Trên màng tơ mọc nhiều viên hạch nấm tròn cứng màu nâu óng như hạt cải bắp",
                        "Toàn bộ dây leo trên giàn bị héo rũ xanh rất nhanh và chết đứng"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bệnh thối rễ Fusarium: Fusarium không sinh tơ nấm trắng muốt lộ thiên và không có hạt hạch nấm màu nâu cánh gián bám quanh vỏ thân.",
                    "kiem_tra_thuc_dia": "Vạch lớp đất gốc thấy mạng tơ nấm trắng đan kín và vô số hạt hạch nấm tròn màu cánh gián bám chặt vào cổ rễ.",
                    "phac_do_vietgap": {
                        "canh_tac": "Lên luống cao thoát nước, không phủ rơm rác ẩm ướt sát gốc dây leo.",
                        "sinh_hoc": "Rải chế phẩm nấm đối kháng Trichoderma harzianum quanh gốc để tiêu diệt hạch nấm trong đất.",
                        "khuyen_cao_chuyen_gia": "Tưới gốc bằng Validamycin A, Flutolanil hoặc Hexaconazole khi chớm thấy tơ nấm trắng xuất hiện."
                    }
                }
            ]
        },
        {
            "id": "w1_094",
            "topic": "Cay_Lam_Nghiep_Duoc_Lieu_Quy",
            "name_vi": "Chè dây cổ Linh Minh Hóa Quảng Bình",
            "scientific_name": "Ampelopsis cantoniensis (Hook. & Arn.) Planch.",
            "dia_ban_pho_bien": ["Minh Hóa", "Tuyên Hóa", "Quảng Bình", "Hướng Hóa", "Quảng Trị"],
            "dac_tinh_sinh_thai": "Cây dây leo gỗ dược liệu quý mọc tự nhiên trên núi đá vôi vùng Trường Sơn, lá kép lông chim chứa hàm lượng rất cao flavonoid myricetin và tanin tự nhiên chữa viêm loét dạ dày tá tràng và tiêu diệt vi khuẩn HP thượng hạng.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Phấn trắng phủ phấn bạc mỏng chè dây",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Oidium sp."
                    },
                    "trieu_chung_dien_hinh": [
                        "Mặt trên phiến lá phủ một lớp phấn trắng xóa mịn màng như bột phấn bánh mì",
                        "Lá bị khô quăn mép, dày lên và rụng sớm làm trơ cành dây leo",
                        "Chùm hoa non bị mốc trắng bao phủ làm thui chột không nở được",
                        "Làm giảm hàm lượng hoạt chất flavonoid trong lá chè khô"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Lớp tuyết phấn chè dây tự nhiên sau ủ lên men: Phấn chè dây tự nhiên chỉ xuất hiện sau khi ủ và phơi khô lá màu trắng tuyết thơm ngát; Phấn trắng nấm Oidium xuất hiện trên lá tươi ngoài vườn làm lá quăn queo úa vàng hoại tử.",
                    "kiem_tra_thuc_dia": "Lấy ngón tay miết mặt lá tươi thấy phấn trắng dính vào ngón tay, phiến lá bên dưới mất màu xanh diệp lục.",
                    "phac_do_vietgap": {
                        "canh_tac": "Làm giàn leo thông thoáng đón nắng sườn núi, cắt tỉa cành la sát đất.",
                        "sinh_hoc": "Phun phòng bằng chế phẩm vi sinh Bacillus subtilis kết hợp tinh dầu sả chanh.",
                        "khuyen_cao_chuyen_gia": "Phun luân phiên Hexaconazole hoặc Diniconazole khi bắt đầu nảy đợt lộc xuân hè."
                    }
                },
                {
                    "ten_benh": "Bệnh Đốm nâu rách viền phiến lá kép chè dây",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Cercospora sp."
                    },
                    "trieu_chung_dien_hinh": [
                        "Phiến lá chét xuất hiện những đốm tròn nhỏ li ti tâm xám bạc viền nâu đỏ sẫm như mắt cua",
                        "Các đốm bệnh lan rộng làm mép lá bị cháy khô rách thủng từng mảng",
                        "Lá già bị úa vàng rụng sớm làm trơ giàn dây leo",
                        "Cây quang hợp kém làm giảm sinh khối cành lá thu hái làm dược liệu"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bọ xít chích hút lá: Bọ xít chích để lại chấm kim châm nhỏ không có quầng viền tía đỏ tròn đồng tâm sắc sảo.",
                    "kiem_tra_thuc_dia": "Soi phiến lá dưới ánh nắng thấy các chấm đốm nhỏ trong suốt viền nâu đỏ nổi bật trên nền lá xanh.",
                    "phac_do_vietgap": {
                        "canh_tac": "Làm giàn leo thông thoáng, tỉa bớt cành nhánh phụ rậm rạp đón gió.",
                        "sinh_hoc": "Phun phòng bằng chế phẩm Nano Bạc Đồng 300ppm kết hợp Chitosan kích kháng màng tế bào.",
                        "khuyen_cao_chuyen_gia": "Phun phòng trừ bằng Antracol 70WP hoặc Mancozeb khi mưa phùn kéo dài."
                    }
                }
            ]
        },
        {
            "id": "w1_095",
            "topic": "Cay_Lam_Nghiep_Duoc_Lieu_Quy",
            "name_vi": "Sâm Bố Chính Bố Trạch Quảng Bình",
            "scientific_name": "Abelmoschus sagittifolius (Kurz) Merr. cv. Bo Trach",
            "dia_ban_pho_bien": ["Bố Trạch", "Quảng Trạch", "Quảng Bình", "Đồng Hới"],
            "dac_tinh_sinh_thai": "Cây dược liệu tiến vua trứ danh vùng đất cát pha đồi núi thấp Bố Trạch, hoa đỏ cam 5 cánh rực rỡ, rễ củ nạc hình người màu vàng ngà chứa hàm lượng chất nhầy, tinh bột và saponin cực kỳ phong phú bồi bổ cơ thể thanh phế trừ ho tiêu đờm thượng thặng.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Gỉ sắt sưng u lá cuống hoa sâm Bố Chính",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Puccinia abelmoschi"
                    },
                    "trieu_chung_dien_hinh": [
                        "Mặt dưới phiến lá và cuống hoa xuất hiện các nốt mụn nhỏ màu vàng cam nổi gồ lên",
                        "Các nốt mụn nứt toác giải phóng bụi phấn nấm màu nâu vàng gỉ sắt bám dính vào tay",
                        "Lá bị khô cháy vàng từng chòm và rụng sớm làm trơ cành cây sâm",
                        "Cuống hoa bị sưng vẹo dị dạng làm hoa thui chột không đậu được quả nang lấy hạt giống"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Vết chích của nhện đỏ: Nhện đỏ tạo các chấm chích hút trắng li ti có màng tơ mỏng; Nấm rỉ sắt tạo các nốt mụn sưng u nổi gồ giải phóng bụi phấn nấm màu nâu vàng rõ rệt.",
                    "kiem_tra_thuc_dia": "Lấy tay quẹt nhẹ qua đám mụn mặt dưới lá thấy bụi phấn màu nâu vàng dính đầy trên đầu ngón tay.",
                    "phac_do_vietgap": {
                        "canh_tac": "Lên luống cao, cày xới phơi đất kỹ trước khi trồng, tỉa bớt lá già sát gốc.",
                        "sinh_hoc": "Phun phòng bằng chế phẩm nấm đối kháng Trichoderma kết hợp Nano Bạc Đồng 300ppm.",
                        "khuyen_cao_chuyen_gia": "Phun trừ bằng Hexaconazole (Anvil 5SC) hoặc Difenoconazole khi phát hiện các mụn rỉ sắt đầu tiên."
                    }
                },
                {
                    "ten_benh": "Bệnh Thối nhũn củ rễ do nấm mốc nước",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Pythium debaryanum / Phytophthora sp."
                    },
                    "trieu_chung_dien_hinh": [
                        "Bộ rễ củ sâm dưới đất bị úng nước thâm đen, thịt củ bị rữa nát thành bột nhão xám tro",
                        "Toàn bộ cành lá sâm bị héo rũ xanh rất nhanh, lá héo nhưng vẫn còn bám chặt trên thân",
                        "Cắt ngang gốc thân thấy vòng mô mạch dẫn chuyển màu nâu đen thâm tím bốc mùi chua",
                        "Cây sâm bị chết đứng từng vạt lớn trên luống trồng khi gặp mưa to úng ngập"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Củ sâm nứt vỏ sinh lý do thừa nước: Nứt vỏ sinh lý mô củ bên trong vẫn trắng rắn chắc chứa nhiều chất nhầy; Bệnh nấm Pythium thịt củ thối đen mủn rữa nát bốc mùi hôi mốc khó chịu.",
                    "kiem_tra_thuc_dia": "Nhổ cây sâm lên thấy củ mềm nhũn nước mủn rữa, bóp nhẹ thấy nước thối rỉ ra đầu ngón tay không còn nhớt dính tự nhiên.",
                    "phac_do_vietgap": {
                        "canh_tac": "Lên luống cao 35cm, đánh rãnh thoát nước sâu ráo gốc, bón lót vôi bột 100kg/sào để khử chua diệt mầm nấm đất.",
                        "sinh_hoc": "Tưới phòng gốc bằng hỗn hợp men vi sinh Bacillus subtilis kết hợp Trichoderma harzianum định kỳ 1 tháng/lần.",
                        "khuyen_cao_chuyen_gia": "Tưới thuốc trừ nấm rễ Metalaxyl-M (Ridomil Gold) hoặc Aliette khi chớm có dấu hiệu rũ lá."
                    }
                }
            ]
        },
        {
            "id": "w1_096",
            "topic": "Cay_Lam_Nghiep_Duoc_Lieu_Quy",
            "name_vi": "Cà gai leo An Xuân Cam Lộ Quảng Trị",
            "scientific_name": "Solanum procumbens Lour. cv. Cam Lo",
            "dia_ban_pho_bien": ["Cam Lộ", "Gio Linh", "Quảng Trị", "Quảng Bình"],
            "dac_tinh_sinh_thai": "Cây bụi bò gai dược liệu giải độc gan số một Việt Nam, sinh trưởng mãnh liệt trên vùng đất đỏ bazan và đất sỏi cằn cỗi nắng gió khắc nghiệt miền Trung, toàn cây chứa hàm lượng glycoalkaloid cực cao ức chế virus viêm gan B và chống xơ gan thần kỳ.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Đốm sọc đen thân lá cà gai leo",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Septoria lycopersici"
                    },
                    "trieu_chung_dien_hinh": [
                        "Phiến lá xuất hiện những đốm tròn nhỏ tâm xám tro viền nâu đen có chấm đen li ti",
                        "Trên thân cành có gai xuất hiện các vệt sọc dài lõm màu đen làm teo thắt thân cành",
                        "Lá già bị úa vàng rụng sớm từ gốc lên ngọn làm trơ cành gai nhọn",
                        "Cây suy kiệt sinh khối cành lá thu hoạch làm trà dược liệu giảm sút"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bọ trĩ chích cào lá: Bọ trĩ làm sần vỏ xám bạc không có đốm tròn tâm xám bạc có chấm đen ổ bào tử nấm li ti.",
                    "kiem_tra_thuc_dia": "Soi kính lúp vào vết đốm thấy các chấm quả cành nhỏ màu đen nổi gồ trên nền tâm xám tro.",
                    "phac_do_vietgap": {
                        "canh_tac": "Lên luống cao, làm cỏ thông thoáng gốc, bón phân hữu cơ vi sinh cân đối.",
                        "sinh_hoc": "Phun phòng bằng chế phẩm Nano Bạc Đồng 400ppm kết hợp vi khuẩn đối kháng Bacillus subtilis.",
                        "khuyen_cao_chuyen_gia": "Phun phòng trừ bằng Mancozeb, Difenoconazole hoặc Antracol 70WP khi độ ẩm ban đêm tăng cao."
                    }
                },
                {
                    "ten_benh": "Bệnh Sương mai mốc tro thân cành gai",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Phytophthora infestans"
                    },
                    "trieu_chung_dien_hinh": [
                        "Đọt non và phiến lá xuất hiện những vết loang ngậm nước màu xanh tái sau chuyển màu nâu đen",
                        "Khi trời mưa phùn sương mù ẩm ướt trên mặt dưới vết bệnh phủ lớp mốc mịn màu trắng xám",
                        "Cành cành gai bị thâm đen gãy gập rũ xuống mặt đất",
                        "Ruộng cà gai leo bị cháy đen rụi từng chòm lớn chỉ sau vài ngày ẩm ướt"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bệnh thán thư: Thán thư vết khô tròn đồng tâm có dịch hồng cam khi ẩm; Sương mai vết loang úng nước không định hình phủ lớp mốc trắng xám mịn như nhung.",
                    "kiem_tra_thuc_dia": "Sáng sớm có sương mù lật mặt dưới phiến lá thấy màng tơ nấm màu trắng tro mỏng manh bao quanh vết đen úng nước.",
                    "phac_do_vietgap": {
                        "canh_tac": "Lên luống cao 30cm thoát nước ráo rễ, không tưới phun đọng nước chiều tối.",
                        "sinh_hoc": "Phun phòng nấm đối kháng Chaetomium kết hợp chế phẩm sinh học Nano Đồng 500ppm.",
                        "khuyen_cao_chuyen_gia": "Phun trừ bằng Ridomil Gold 68WG, Cymoxanil hoặc Metalaxyl khi trời có sương mù ẩm ướt."
                    }
                }
            ]
        },
        {
            "id": "w1_097",
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": "Xoài cát Chu Đặng Cam Lâm Khánh Hòa",
            "scientific_name": "Mangifera indica L. cv. Cam Lam",
            "dia_ban_pho_bien": ["Cam Lâm", "Cam Ranh", "Khánh Hòa", "Ninh Thuận"],
            "dac_tinh_sinh_thai": "Thủ phủ xoài cát nức tiếng Nam Trung Bộ trên vùng đất cát trắng ven biển và bán sơn địa, nắng gió dồi dào biên độ nhiệt lớn giúp quả xoài cát Chu Đặng to dài vỏ vàng ươm thịt mịn màng không xơ ngọt đậm đà thơm ngát hương hoa quả nhiệt đới.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Thán thư thối đen bông quả xoài cát Cam Lâm",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Colletotrichum gloeosporioides"
                    },
                    "trieu_chung_dien_hinh": [
                        "Chùm hoa xoài xuất hiện các chấm đen nhỏ li ti, sau lan nhanh làm toàn bộ hoa khô cháy đen thui rụng ráo trọi",
                        "Quả non bị đốm đen lõm sâu làm quả rụng hàng loạt hoặc quả lớn bị méo mó thâm đen vỏ",
                        "Lá non xuất hiện các đốm góc cạnh màu nâu đen thủng rách phiến lá",
                        "Trên quả chín xuất hiện các đốm đen tròn đồng tâm thịt quả bên dưới bị thối nhũn chua"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bọ trĩ chích hút hoa xoài: Bọ trĩ làm hoa khô teo màu nâu nhạt không có đốm đen lõm sâu và không tiết chất nhầy bào tử hồng cam khi trời mưa ẩm.",
                    "kiem_tra_thuc_dia": "Lắc nhẹ chùm hoa thấy hoa đen rụng lả tả, đưa quả non thâm đen soi kính lúp thấy các giọt nhầy bào tử màu cam hồng tiết ra ở tâm vết lõm.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt tỉa cành thông thoáng sau thu hoạch, dọn sạch cỏ rác dưới tán cây đón nắng gió khô nóng vùng cát.",
                        "sinh_hoc": "Phun phòng định kỳ chế phẩm sinh học Trichoderma kết hợp Chitosan nano kích kháng màng tế bào biểu bì hoa quả non.",
                        "khuyen_cao_chuyen_gia": "Phun phòng ngừa bằng Azoxystrobin + Difenoconazole (Amistar Top 325SC) hoặc Antracol 70WP trước khi hoa bung nở và sau khi đậu quả non."
                    }
                },
                {
                    "ten_benh": "Bệnh Xì mủ đen đốm lá vi khuẩn xoài vùng cát",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Vi khuẩn",
                        "ten_khoa_hoc": "Xanthomonas campestris pv. mangiferaeindicae"
                    },
                    "trieu_chung_dien_hinh": [
                        "Trên lá: Vết bệnh là những đốm nhỏ góc cạnh màu đen nổi gồ lên như mắt cua, có quầng sáng vàng bao quanh",
                        "Trên cành non: Vết nứt dọc màu nâu đen rỉ giọt dịch mủ vi khuẩn màu đen dính nhớt",
                        "Trên vỏ quả: Vết bệnh nứt nẻ hình sao màu đen sâu hoại tử mô thịt quả",
                        "Bệnh lây lan rất nhanh theo các vết thương cơ giới sau những trận giông gió cát ven biển"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Thán thư: Vết vi khuẩn nổi gồ như vảy mụn có quầng vàng trong suốt và vết nứt vỏ hình sao chảy mủ đen; Thán thư vết lõm sâu đồng tâm không có mủ đen nhờn.",
                    "kiem_tra_thuc_dia": "Dùng móng tay cạy mép vết nứt trên cành thấy dịch nhầy màu đen dính nhớt bốc mùi hôi chua nhẹ.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt bỏ cành lá bị loét đen đem đốt, không tỉa cành vào những ngày mưa gió ẩm ướt.",
                        "sinh_hoc": "Phun phòng bằng chế phẩm vi sinh Bacillus subtilis kết hợp Nano Bạc Đồng 500ppm.",
                        "khuyen_cao_chuyen_gia": "Phun phòng trừ bằng Kasugamycin, Oxytetracycline hoặc Copper Oxychloride ngay sau bão gió dông."
                    }
                }
            ]
        },
        {
            "id": "w1_098",
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": "Nho đỏ Cardinal Ninh Thuận vùng cát",
            "scientific_name": "Vitis vinifera L. cv. Red Cardinal",
            "dia_ban_pho_bien": ["Ninh Phước", "Phan Rang", "Ninh Hải", "Ninh Thuận", "Bình Thuận"],
            "dac_tinh_sinh_thai": "Thủ phủ nho lớn nhất Việt Nam trên vùng đất bán khô hạn bán sa mạc tiểu khí hậu nắng gió thừa thãi ít mưa, đất phù sa pha cát bồi đắp ven sông Dinh, chùm nho đỏ tím mọng nước giòn ngọt rôn rốt thanh chua dịu mát.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Phấn trắng mốc tro lá chùm quả nho",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Uncinula necator (Erysiphe necator)"
                    },
                    "trieu_chung_dien_hinh": [
                        "Mặt trên và mặt dưới phiến lá phủ một lớp màng phấn mốc màu xám tro trắng đục như rắc bột mì",
                        "Lá bị khô quăn mép, dày lên và rụng sớm làm trơ giàn cành que",
                        "Quả non bị bao phủ bởi lớp phấn trắng xám, vỏ quả bị nứt toác để lộ hạt non bên trong",
                        "Chùm quả bị chai sượng sần sùi thối đen không tích lũy được độ đường"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bệnh sương mai mốc sương: Sương mai nấm chỉ mọc ở mặt dưới lá thành mảng mốc trắng mịn vào sáng ẩm; Phấn trắng mọc phủ kín cả 2 mặt lá và vỏ quả thành lớp bột xám tro dày cộp vào những ngày hanh khô.",
                    "kiem_tra_thuc_dia": "Lấy ngón tay miết nhẹ chùm quả nho thấy lớp phấn xám dính vào tay, vỏ quả bên dưới bị nứt toác hình chân chim.",
                    "phac_do_vietgap": {
                        "canh_tac": "Buộc cành tỉa nhánh thông thoáng giàn nho, vặt bỏ lá già che khuất chùm quả đón ánh nắng.",
                        "sinh_hoc": "Phun phòng bằng bột lưu huỳnh sinh học (vôi lưu huỳnh) hoặc men vi sinh Bacillus subtilis.",
                        "khuyen_cao_chuyen_gia": "Phun phòng luân phiên Difenoconazole, Myclobutanil hoặc Tebuconazole giai đoạn quả non bằng hạt tiêu."
                    }
                },
                {
                    "ten_benh": "Bệnh Thán thư mắt chim cành quả nho",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Elsinoë ampelina"
                    },
                    "trieu_chung_dien_hinh": [
                        "Trên lá: Vết bệnh tròn nhỏ tâm xám tro viền nâu đỏ gờ nổi rõ ràng như mắt chim, tâm vết bệnh khô rách thủng lỗ chỗ",
                        "Trên cành non: Xuất hiện các vết loét hình bầu dục dài lõm sâu màu nâu đen làm teo thắt cành",
                        "Trên quả nho: Xuất hiện các đốm tròn lõm tâm xám bạc viền tím thẫm như mắt chim làm quả bị chai sượng nứt toác",
                        "Làm giảm mạnh sản lượng và mẫu mã chùm nho thương phẩm"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Vết cào rách do gió cát va đập: Vết cơ giới phẳng liền sẹo trắng; Thán thư Elsinoe là vết loét lõm sâu hình tròn mắt chim viền tím thẫm sắc nét.",
                    "kiem_tra_thuc_dia": "Quan sát quả nho thấy các vết tròn tâm xám viền tím rất giống mắt chim bồ câu, bóp nhẹ thấy vỏ cứng chai.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt tỉa cành bệnh triệt để trong mùa ngủ đông, bôi thuốc sát trùng vào vết cắt cành.",
                        "sinh_hoc": "Phun phòng Nano Bạc Đồng 500ppm kết hợp chế phẩm sinh học Chitosan bảo vệ bề mặt quả non.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bằng Booc-đô 1%, Mancozeb hoặc Azoxystrobin giai đoạn bung chồi nụ hoa."
                    }
                }
            ]
        },
        {
            "id": "w1_099",
            "topic": "Rau_Cu_Gia_Vi_Va_Nam",
            "name_vi": "Măng tây xanh Ninh Hải Ninh Thuận",
            "scientific_name": "Asparagus officinalis L. cv. Ninh Hai",
            "dia_ban_pho_bien": ["Ninh Hải", "Thuận Bắc", "Ninh Phước", "Ninh Thuận", "Bình Thuận"],
            "dac_tinh_sinh_thai": "Cây rau 'Hoàng đế dinh dưỡng' cao cấp thích ứng hoàn hảo trên vùng đất cát ven biển Ninh Thuận nắng gió quanh năm, đọt măng mập mạp xanh mướt giòn ngọt đậm đà giàu chất xơ vitamin và khoáng chất chống lão hóa.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Đốm tím khô cành măng tây",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Stemphylium vesicarium"
                    },
                    "trieu_chung_dien_hinh": [
                        "Thân cành và cọng lá kim măng tây xuất hiện những đốm nhỏ hình bầu dục màu nâu tím lõm sâu",
                        "Vết bệnh lan rộng làm cọng lá kim bị úa vàng khô cháy và rụng sớm hàng loạt",
                        "Bụi măng tây bị trơ trụi cành que xơ xác mất hoàn toàn khả năng quang hợp",
                        "Đọt măng non mới nhú bị các đốm thâm tím làm cong queo dị dạng mất giá trị thương phẩm"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bệnh rỉ sắt măng tây (Puccinia asparagi): Rỉ sắt sinh mụn bột màu vàng cam hoặc nâu đỏ; Stemphylium là các đốm bầu dục lõm sâu màu nâu tím tâm xám bạc không có bụi phấn nấm.",
                    "kiem_tra_thuc_dia": "Quan sát thân cành măng tây thấy vô số đốm hình bầu dục màu tím sẫm lõm sâu, vuốt cành thấy lá kim rụng lả tả.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt tỉa cành mẹ định kỳ tạo độ thông thoáng gốc, khơi rãnh thoát nước luống cát không để đọng nước mưa.",
                        "sinh_hoc": "Phun phòng bằng chế phẩm nấm đối kháng Chaetomium kết hợp Nano Bạc Đồng 500ppm.",
                        "khuyen_cao_chuyen_gia": "Phun luân phiên Difenoconazole, Chlorothalonil hoặc Antracol 70WP sau mỗi chu kỳ thu hoạch măng non."
                    }
                },
                {
                    "ten_benh": "Bệnh Thối rễ héo rũ thân măng nấm mốc",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Fusarium oxysporum f. sp. asparagi"
                    },
                    "trieu_chung_dien_hinh": [
                        "Bộ rễ củ và rễ tơ dưới luống cát bị thối đen thâm sẫm, vỏ rễ nứt mục rỗng ruột",
                        "Cành mẹ trên tán bị úa vàng từ từ, các nhánh non mới nhú bị teo thắt cong queo như lưỡi liềm",
                        "Toàn bộ bụi măng tây bị suy kiệt chết héo rũ đứng từng chòm lớn",
                        "Đọt măng non mới nhú bị thối đen từ dưới cát không vươn lên khỏi mặt đất được"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Héo do thiếu nước trên cát: Thiếu nước tưới đẫm cây tươi lại ngay; Bệnh nấm Fusarium gốc thân và rễ thối mục sũng nước và cây chết vĩnh viễn không hồi phục.",
                    "kiem_tra_thuc_dia": "Bới nhẹ lớp cát quanh gốc thấy rễ măng bị thối đen mủn nát, cắt ngang thân cành sát gốc thấy vòng mạch dẫn thâm nâu tím.",
                    "phac_do_vietgap": {
                        "canh_tac": "Lên luống cát cao 40cm, luân canh với cây họ đậu, không trồng măng tây liên tục trên cùng chân đất quá 5-6 năm.",
                        "sinh_hoc": "Tưới phòng gốc bằng hỗn hợp men vi sinh Bacillus subtilis kết hợp Trichoderma harzianum định kỳ hàng tháng.",
                        "khuyen_cao_chuyen_gia": "Tưới thuốc trừ nấm rễ Metalaxyl-M hoặc Ridomil Gold khi chớm có dấu hiệu vàng cành mẹ."
                    }
                }
            ]
        },
        {
            "id": "w1_100",
            "topic": "Cay_Lam_Nghiep_Duoc_Lieu_Quy",
            "name_vi": "Tràm gió Lộc Thủy Thừa Thiên Huế",
            "scientific_name": "Melaleuca cajuputi Maton & Sm. ex R.Powell cv. Loc Thuy",
            "dia_ban_pho_bien": ["Phú Lộc", "Lộc Thủy", "Phong Điền", "Thừa Thiên Huế", "Quảng Trị"],
            "dac_tinh_sinh_thai": "Cây gỗ lâm nghiệp dược liệu quý mọc thành rừng trên vùng đất cát cằn cỗi và đầm lầy ven biển miền Trung, chịu gió bão cát bay ngập mặn khốc liệt, lá chứa hàm lượng rất cao tinh dầu Cineol (Eucalyptol) thơm nồng đặc trưng dùng chưng cất dầu tràm Huế danh bất hư truyền giữ ấm cho sản phụ và trẻ sơ sinh.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Rỉ sắt đốm vàng lá tràm gió",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Puccinia psidii"
                    },
                    "trieu_chung_dien_hinh": [
                        "Mặt dưới phiến lá và chồi non xuất hiện các mụn nhỏ màu vàng cam sáng rực rỡ",
                        "Bột phấn nấm màu vàng cam bám dính dày đặc vào tay khi chạm vào",
                        "Lá non bị vặn vẹo biến dạng, chồi non bị khô tóp từ ngọn xuống",
                        "Lá già bị khô cháy vàng từng chòm làm giảm sản lượng lá thu hái chưng cất tinh dầu"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bệnh đốm mắt chim: Đốm mắt chim phẳng lì khô giòn tâm bạc viền nâu; Rỉ sắt là các ổ mụn nâng cao bề mặt giải phóng bụi phấn nấm màu vàng cam đặc thù.",
                    "kiem_tra_thuc_dia": "Lấy tay quẹt qua phiến lá thấy bụi phấn màu vàng cam óng dính đầy trên đầu ngón tay như nhũ vàng.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt tỉa cành tạo tán thông thoáng, dọn sạch tàn dư dưới gốc cây tràm gió.",
                        "sinh_hoc": "Phun phòng bằng chế phẩm nấm đối kháng Trichoderma kết hợp Nano Bạc Đồng 300ppm.",
                        "khuyen_cao_chuyen_gia": "Phun trừ bằng Hexaconazole (Anvil 5SC) hoặc Difenoconazole khi phát hiện các mụn rỉ sắt đầu tiên."
                    }
                },
                {
                    "ten_benh": "Bệnh Sâu róm lông độc ăn trụi chồi lá non tràm gió",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Côn trùng gây hại",
                        "ten_khoa_hoc": "Dasychira mendosa"
                    },
                    "trieu_chung_dien_hinh": [
                        "Sâu róm có nhiều chùm lông độc màu vàng nâu ăn ngấu nghiến đọt non và lá tràm",
                        "Ăn trụi lá làm toàn bộ tán cây tràm gió bị trơ cành que chỉ trong vài tuần",
                        "Lông độc của sâu róm bay vào không khí gây ngứa ngáy nổi mề đay cho người đi rừng",
                        "Cây bị suy kiệt còi cọc làm sụt giảm sản lượng khai thác lá nấu dầu tràm"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bệnh rụng lá nấm: Rụng lá nấm lá vàng úa rụng xuống đất; Sâu róm cắn phá để lại vết cắn nham nhở và nhìn thấy sâu róm bám đầy trên cành lá.",
                    "kiem_tra_thuc_dia": "Quan sát thân cành thấy các con sâu róm có các túm lông dựng đứng đang bò lổm ngổm, chạm vào da thấy ngứa rát buốt dữ dội.",
                    "phac_do_vietgap": {
                        "canh_tac": "Bảo vệ các loài chim sâu và kiến vàng tự nhiên trong rừng tràm.",
                        "sinh_hoc": "Phun chế phẩm sinh học vi khuẩn Bacillus thuringiensis (Bt) hoặc nấm ký sinh Beauveria bassiana.",
                        "khuyen_cao_chuyen_gia": "Phun trừ bằng thuốc sinh học Emamectin benzoate hoặc Abamectin khi sâu non mới nở."
                    }
                }
            ]
        }
    ]
