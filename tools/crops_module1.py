# -*- coding: utf-8 -*-
"""
Module 1: Cây ăn trái nhiệt đới, cận nhiệt đới & ôn đới (80 cây: crop_106 -> crop_185)
Vùng sinh thái: Miền Bắc, Miền Trung, Tây Nguyên & Ôn đới Đà Lạt
"""

def create_disease(ten_benh, muc_do, loai, ten_kh, trieu_chung, phan_biet, kiem_tra, canh_tac, sinh_hoc, khuyen_cao, vector=None):
    tac_nhan = {"loai": loai, "ten_khoa_hoc": ten_kh}
    if vector:
        tac_nhan["vector_truyen_benh"] = vector
    return {
        "ten_benh": ten_benh,
        "muc_do_nguy_hiem": muc_do,
        "tac_nhan": tac_nhan,
        "trieu_chung_dien_hinh": trieu_chung,
        "phan_biet_chan_doan_kep": phan_biet,
        "kiem_tra_thuc_dia": kiem_tra,
        "phac_do_vietgap": {
            "canh_tac": canh_tac,
            "sinh_hoc": sinh_hoc,
            "khuyen_cao_chuyen_gia": khuyen_cao,
            "khuyen_cao_vinh_long": khuyen_cao
        }
    }

def get_module1_crops():
    crops = []
    
    # 106. Vải thiều Lục Ngạn
    crops.append({
        "id": "crop_106",
        "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
        "name_vi": "Vải thiều Lục Ngạn",
        "scientific_name": "Litchi chinensis 'Luc Ngan'",
        "dia_ban_pho_bien": ["Lục Ngạn (Bắc Giang)", "Thanh Hà (Hải Dương)", "Đông Triều (Quảng Ninh)"],
        "dac_tinh_sinh_thai": "Ưa khí hậu có mùa đông lạnh khô (13-15°C) để phân hóa mầm hoa, mùa hè nóng ẩm, đất đồi feralit thoát nước tốt.",
        "danh_sach_benh": [
            create_disease(
                "Bệnh Sương mai hại vải (Mốc sương cành quả)",
                "Cực kỳ nghiêm trọng (Gây thối rụng quả hàng loạt)",
                "Nấm", "Peronophythora litchii",
                [
                    "Vết bệnh trên quả ban đầu là đốm màu nâu đen ủng nước ở cuống",
                    "Gặp trời ẩm xuất hiện lớp mốc trắng như sương muối bao phủ quả",
                    "Quả bệnh bị thối nhũn, cùi vải chua loét, vỏ quả nứt và rụng trơ cuống",
                    "Trên lá bánh tẻ xuất hiện đốm nâu không định hình viền vàng nhạt"
                ],
                "Khác với bệnh Thán thư (Colletotrichum): Sương mai có lớp mốc trắng mịn khi trời ẩm; Thán thư có các chấm đen xếp đồng tâm và làm quả khô sần chứ không ủng nhũn mốc trắng",
                "Quan sát cuống quả vào buổi sáng sớm, nếu thấy lớp phấn trắng mịn như bột phấn rắc đều thì 100% là nấm sương mai",
                "Cắt tỉa cành tăm, cành sâu bệnh sau thu hoạch để vườn thông thoáng ánh sáng",
                "Phun phòng hoạt chất Mancozeb, Fosetyl-Aluminium hoặc dịch nấm đối kháng Trichoderma viride trước khi hoa nở và khi quả non bằng hạt đỗ",
                "Thực hiện theo chỉ đạo phòng trừ của Chi cục Trồng trọt & BVTV tỉnh Bắc Giang"
            ),
            create_disease(
                "Bệnh Thán thư hoa và quả vải",
                "Rất nghiêm trọng",
                "Nấm", "Colletotrichum gloeosporioides",
                [
                    "Chùm hoa bị cháy đen, teo tóp và rụng hàng loạt khi gặp mưa xuân",
                    "Vết bệnh trên quả có màu nâu đậm hơi lõm xuống, xung quanh có quầng xám",
                    "Khi trời ẩm, trên vết bệnh tiết ra các giọt dịch nhờn màu hồng cam chứa bào tử nấm"
                ],
                "Khác với Sương mai: Thán thư tạo vết lõm tròn có vòng đồng tâm và dịch màu hồng cam; Sương mai không lõm và mốc trắng xốp",
                "Dùng kính lúp kiểm tra các nốt chấm đen xếp vòng đồng tâm ở vết lõm trên vỏ quả",
                "Không bón thừa phân đạm giai đoạn ra hoa đậu quả, thu gom cành hoa khô đem tiêu hủy",
                "Phun hoạt chất sinh học Azoxystrobin kết hợp nấm vi sinh Bacillus subtilis 10^9 CFU/ml",
                "Khuyến cáo trạm Khuyến nông Lục Ngạn"
            ),
            create_disease(
                "Bệnh Sâu đục cuống quả vải (kèm nấm hoại sinh)",
                "Nặng",
                "Côn trùng & Nấm thứ cấp", "Conopomorpha sinensis kết hợp Fusarium spp.",
                [
                    "Đầu cuống quả non có vết châm nhỏ li ti màu nâu đen",
                    "Bên trong cuống bị sâu non đục rỗng, đùn phân mùn cưa màu nâu",
                    "Nấm Fusarium xâm nhập qua vết đục làm quả chín ép, nứt đít và rụng sớm"
                ],
                "Khác với nứt quả sinh lý: Nứt quả do sâu đục có vết phân sâu dạng hạt nhỏ li ti ngay tại đáy cuống",
                "Bẻ nhẹ cuống quả kiểm tra lỗ đục và phân sâu màu nâu bết dính",
                "Vệ sinh vườn, bao trái vải bằng túi chuyên dụng, bẫy đèn pheromone bắt ngài trưởng thành",
                "Phun thuốc sinh học Bt (Bacillus thuringiensis) hoặc thảo mộc Emamectin benzoate luân phiên",
                "Chi cục BVTV Bắc Giang khuyến cáo"
            )
        ]
    })

    # 107. Vải u hồng
    crops.append({
        "id": "crop_107",
        "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
        "name_vi": "Vải U Hồng (Vải chín sớm)",
        "scientific_name": "Litchi chinensis 'U Hong'",
        "dia_ban_pho_bien": ["Bắc Giang", "Hải Dương", "Phú Thọ", "Đắk Lắk"],
        "dac_tinh_sinh_thai": "Nhu cầu nhiệt độ lạnh thấp hơn vải thiều chính vụ, ra hoa sớm vào tháng 1-2, thu hoạch tháng 5, ưa đất đồi thoát nước.",
        "danh_sach_benh": [
            create_disease(
                "Bệnh Đốm đen lá và quả vải U Hồng",
                "Nặng",
                "Nấm", "Pseudocercospora litchii",
                [
                    "Phiến lá xuất hiện nhiều đốm nhỏ góc cạnh màu nâu đen",
                    "Lá bánh tẻ bị vàng từng mảng và rụng sớm làm kiệt cây",
                    "Vỏ quả có các chấm đốm nhỏ màu xám chì làm mã quả xấu, mất giá trị thương phẩm"
                ],
                "Khác với bệnh gỉ sắt: Đốm đen không có mụn sần sùi cộm tay, vết bệnh góc cạnh theo gân phụ lá",
                "Dùng tay miết phiến lá: vết bệnh trơn láng, không dính bột màu gỉ sắt",
                "Tỉa cành tạo bộ khung tán thông thoáng, dọn sạch tàn dư dưới gốc",
                "Phun Bordeaux sinh học hoặc chế phẩm nấm đối kháng Chaetomium cupreum",
                "Theo quy chuẩn VietGAP rau quả miền Bắc"
            ),
            create_disease(
                "Bệnh Cháy sém mép lá do thiếu Kali & nấm hoại sinh",
                "Trung bình",
                "Dinh dưỡng & Nấm yếu", "Thiếu K kết hợp Phomopsis spp.",
                [
                    "Mép lá già bị cháy khô viền ngoài hình chữ V ngược",
                    "Vùng giáp ranh giữa mô bệnh và mô khỏe có quầng vàng nhạt",
                    "Cành mang quả bị giòn dễ gãy khi gió to"
                ],
                "Khác với bệnh vi khuẩn: Vết cháy thiếu Kali khô giòn rụm, không ủng nước thối nhờn",
                "Bóp méo lá khô nghe tiếng giòn rụm, gân chính vẫn dẻo",
                "Bổ sung phân bón lá Kali hữu cơ chiết xuất từ rong biển, cân đối NPK",
                "Phun phòng nano đồng bảo vệ vết thương mép lá",
                "Trung tâm Khuyến nông Quốc gia khuyến cáo"
            )
        ]
    })

    # 108. Nhãn lồng Hưng Yên
    crops.append({
        "id": "crop_108",
        "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
        "name_vi": "Nhãn lồng Hưng Yên",
        "scientific_name": "Dimocarpus longan 'Hung Yen'",
        "dia_ban_pho_bien": ["Khoái Châu", "Kim Động", "Tiên Lữ (Hưng Yên)", "Hà Nam"],
        "dac_tinh_sinh_thai": "Ưa đất phù sa bãi bồi sông Hồng, tầng canh tác dày, giữ ẩm tốt nhưng sợ úng nước, chịu rét khá.",
        "danh_sach_benh": [
            create_disease(
                "Bệnh Chổi rồng hại nhãn (Witches' Broom)",
                "Cực kỳ nghiêm trọng (Gây mất trắng mùa vụ)",
                "Virus/Phytoplasma", "Longan Witches' Broom Associated Virus (LWBV)",
                [
                    "Chồi non ra lùm xùm thành búi như tổ chổi chổi quét nhà",
                    "Lá dị dạng xoăn tít, phiến lá nhỏ xíu dày cứng màu vàng úa",
                    "Chùm hoa bị thoái hóa thành chùm lá nhỏ, không đậu được trái nào",
                    "Cành bệnh sau đó bị khô chết dần từ ngọn xuống"
                ],
                "Khác với ngộ độc Paclobutrazol: Chổi rồng có chồi mọc dày đặc xoắn vặn và lây lan nhanh qua nhện lông nhung; ngộ độc phân thuốc chỉ đọt ngắn rụt đều toàn cây",
                "Dùng kính lúp soi đọt non tìm nhện lông nhung Eriophyes dimocarpi màu trắng sữa dài 0.2mm",
                "Cắt sâu cành chổi rồng 20-30cm gom tiêu hủy triệt để, khử trùng kéo bằng cồn",
                "Phun dầu khoáng sinh học tiêu diệt nhện lông nhung môi giới truyền bệnh",
                "Chi cục Trồng trọt & BVTV Hưng Yên khuyến cáo"
            ),
            create_disease(
                "Bệnh Thối hoa thối quả nhãn lồng",
                "Rất nghiêm trọng",
                "Nấm", "Phytophthora nicotianae",
                [
                    "Hoa nhãn bị thối nâu đen, rụng tơi tả vào những ngày mưa phùn ẩm ướt",
                    "Vỏ quả nhãn xuất hiện đốm nâu đen ủng nước loang dần khắp quả",
                    "Cùi nhãn bên trong bị lên men chua, quả rụng hàng loạt dưới gốc"
                ],
                "Khác với cháy nắng: Thối quả nấm Phytophthora mềm ủng nước có mùi chua; Cháy nắng chỉ nám khô rám vỏ mặt hứng nắng",
                "Dùng tay bóp nhẹ quả bệnh thấy nước dịch nâu ứa ra có mùi lên men men chua",
                "Vét mương rãnh thoát nước sâu 40-50cm quanh gốc trong mùa mưa lũ",
                "Phun thuốc trừ nấm sinh học hoạt chất Metalaxyl-M hoặc Fosetyl-Aluminium hữu cơ",
                "Khuyến cáo VietGAP Hưng Yên"
            )
        ]
    })

    # 109. Nhãn cùi tiến vua
    crops.append({
        "id": "crop_109",
        "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
        "name_vi": "Nhãn cùi tiến vua",
        "scientific_name": "Dimocarpus longan 'Cui Tien Vua'",
        "dia_ban_pho_bien": ["Hưng Yên", "Hà Nội", "Hải Dương"],
        "dac_tinh_sinh_thai": "Giống nhãn cổ cùi dày giòn khô nước, hạt nhỏ, cây sinh trưởng mạnh, đòi hỏi phân bón hữu cơ ủ hoai mục.",
        "danh_sach_benh": [
            create_disease(
                "Bệnh Đốm mốc xám quả nhãn (Grey Mould)",
                "Nặng",
                "Nấm", "Botrytis cinerea",
                [
                    "Vết bệnh ban đầu màu nâu nhạt trên vỏ quả gần thu hoạch",
                    "Gặp trời mưa ẩm kéo dài, lớp nấm mốc xám tro phủ kín chùm quả",
                    "Quả khô tóp lại và dính chặt vào cuống thành chùm khô cháy"
                ],
                "Khác với bồ hóng: Mốc xám ăn sâu làm thối cùi nhãn; Bồ hóng muội đen chỉ bám trên bề mặt vỏ quả lau chùi là sạch",
                "Dùng khăn ẩm lau nhẹ vết đen: nếu không sạch và cùi bên dưới thối đen thì là mốc xám",
                "Bao chùm quả bằng túi lưới chuyên dụng trước thu hoạch 30 ngày",
                "Phun chế phẩm sinh học Chitosan kết hợp nấm đối kháng Trichoderma",
                "Trung tâm Khuyến nông Hà Nội khuyến cáo"
            ),
            create_disease(
                "Bệnh Nứt gai nứt vỏ quả nhãn",
                "Trung bình",
                "Rối loạn sinh lý & Nấm yếu", "Alternaria alternata",
                [
                    "Vỏ quả bị nứt dọc một đường từ cuống xuống rốn quả sau cơn mưa rào lớn",
                    "Nước ngọt từ cùi quả ứa ra thu hút nấm Alternaria và ruồi đục quả xâm nhập",
                    "Quả nứt bị chua thối nhanh chóng trong vòng 24-48 giờ"
                ],
                "Khác với sâu đục: Vết nứt quả sinh lý dài thẳng mép nứt nham nhở không có lỗ đục tròn",
                "Kiểm tra mép vết nứt, không có mùn phân sâu bám dính",
                "Tưới nước đều đặn trong mùa khô, không để cây thiếu nước rồi tưới ồ ạt, bón bổ sung Canxi-Bo sinh học",
                "Phun phòng dung dịch tỏi ớt xua đuổi côn trùng ruồi đục",
                "Khuyến cáo trạm Khuyến nông Tiên Lữ"
            )
        ]
    })

    # 110. Mận Tam Hoa Bắc Hà
    crops.append({
        "id": "crop_110",
        "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
        "name_vi": "Mận Tam Hoa Bắc Hà",
        "scientific_name": "Prunus salicina 'Tam Hoa'",
        "dia_ban_pho_bien": ["Bắc Hà (Lào Cai)", "Mường Khương", "Si Ma Cai"],
        "dac_tinh_sinh_thai": "Cây ôn đới vùng cao > 800m, đòi hỏi tích lũy giờ lạnh mùa đông (300-400 giờ < 7°C), đất dốc thoát nước tốt.",
        "danh_sach_benh": [
            create_disease(
                "Bệnh Chảy gôm xì mủ thân mận (Gummosis)",
                "Rất nghiêm trọng (Làm suy kiệt và chết cành)",
                "Nấm", "Lasiodiplodia theobromae / Phytophthora spp.",
                [
                    "Vỏ thân và cành chính xuất hiện các vết nứt nẻ sẫm màu",
                    "Từ vết nứt ứa ra chất nhựa dẻo trong suốt, sau đông đặc lại thành cục gôm màu hổ phách nâu đỏ",
                    "Phần gỗ dưới vết nứt bị hoại tử thâm đen, cành phía trên bị vàng lá và chết khô rụi"
                ],
                "Khác với vết mủ do sâu xén tóc cắn: Chảy gôm do nấm không có lỗ đục sâu vào lõi gỗ và không có phân mùn cưa đùn ra",
                "Dùng dao cạo nhẹ lớp mủ gôm: nếu thấy mô vỏ dưới bị thối nâu đen ẩm ướt rộng loang lổ thì là nấm gôm",
                "Quét vôi bột hòa phèn xanh (Boóc-đô 5%) quanh gốc thân cây cao 1m trước mùa mưa lũ",
                "Cạo sạch vết gôm mủ đến phần gỗ tươi, bôi thuốc gốc đồng nano hoặc nấm đối kháng Chaetomium",
                "Sở Nông nghiệp & PTNT Lào Cai khuyến cáo"
            ),
            create_disease(
                "Bệnh Thủng lá mận (Bệnh đốm mắt chim đạn hoa)",
                "Nặng",
                "Vi khuẩn / Nấm", "Xanthomonas arboricola pv. pruni / Clasterosporium carpophilum",
                [
                    "Lá non xuất hiện các đốm nhỏ hình tròn úng nước màu nâu đỏ",
                    "Vết bệnh khô lại, phần mô chết rụng rơi ra tạo thành những lỗ thủng tròn như bị đạn bắn",
                    "Lá bị thủng lỗ chỗ xơ xác, quang hợp kém làm quả mận còi cọc chua chát"
                ],
                "Khác với sâu ăn lá: Vết thủng do bệnh có đường viền màu nâu sậm rất đều quanh lỗ thủng",
                "Soi mép lỗ thủng bằng kính lúp thấy gờ bần hóa màu nâu đậm",
                "Thu gom lá rụng đem ủ men vi sinh nhiệt độ cao hoặc đốt tiêu hủy",
                "Phun thuốc sinh học gốc Kasugamycin kết hợp đồng hữu cơ khi lộc xuân nhú 5-10cm",
                "Trạm BVTV Bắc Hà hướng dẫn"
            ),
            create_disease(
                "Bệnh Thối nâu quả mận (Brown Rot)",
                "Nặng",
                "Nấm", "Monilinia fructigena",
                [
                    "Quả mận sắp chín xuất hiện đốm tròn màu nâu nhạt lan rộng rất nhanh",
                    "Thịt quả bên trong bị thối nhũn thành nước nhưng vỏ quả vẫn căng bóng",
                    "Trên bề mặt quả xuất hiện các cụm nấm màu vàng kem xếp thành các vòng tròn đồng tâm",
                    "Quả bị teo quắt lại thành quả 'xác ướp' đen khô treo lơ lửng trên cành qua mùa đông"
                ],
                "Khác với quả thối do va đập: Thối nâu Monilinia có các nốt mốc phấn màu vàng kem xếp vòng tròn đồng tâm đặc hữu",
                "Quan sát vòng bào tử màu vàng kem đồng tâm trên vỏ quả thối",
                "Rung tỉa bỏ toàn bộ quả xác ướp khô trên cây vào mùa đông trước khi cây đâm chồi",
                "Phun phòng bằng hoạt chất sinh học Azoxystrobin hoặc nấm Bacillus amyloliquefaciens",
                "Khuyến cáo trạm Khuyến nông Bắc Hà"
            )
        ]
    })

    # 111. Mận Hậu Mộc Châu
    crops.append({
        "id": "crop_111",
        "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
        "name_vi": "Mận Hậu Mộc Châu",
        "scientific_name": "Prunus salicina 'Hau'",
        "dia_ban_pho_bien": ["Mộc Châu (Sơn La)", "Yên Châu", "Vân Hồ"],
        "dac_tinh_sinh_thai": "Cao nguyên Mộc Châu 1050m, khí hậu mát mẻ quanh năm, biên độ nhiệt ngày đêm lớn, đất mùn trên đá vôi.",
        "danh_sach_benh": [
            create_disease(
                "Bệnh Phấn trắng mận hậu",
                "Nặng",
                "Nấm", "Podosphaera tridactyla",
                [
                    "Lá non và chồi ngọn phủ một lớp bột phấn trắng xóa như rắc bột mì",
                    "Lá bệnh bị cong queo, xoăn mép, giòn dễ gãy và teo tóp",
                    "Quả non bị phấn trắng bám làm vỏ quả sần sùi, méo mó, nứt nẻ khi lớn"
                ],
                "Khác với bụi bẩn: Lớp phấn trắng do nấm bám chặt vào biểu bì lá và làm mô lá dưới bị biến dạng dị tật",
                "Dùng tay miết lá thấy bột trắng bay ra để lại vết thâm sạm trên biểu bì",
                "Tỉa cành thông thoáng, cắt bỏ đọt bị mốc phấn trắng đem đốt ngay",
                "Phun dung dịch lưu huỳnh hữu cơ vi sinh (Sulfit) hoặc dầu hạt neem ép lạnh (Neem oil 0.3%)",
                "Chi cục BVTV Sơn La khuyến cáo"
            ),
            create_disease(
                "Bệnh Loét vi khuẩn quả mận Hậu",
                "Nặng",
                "Vi khuẩn", "Pseudomonas syringae pv. syringae",
                [
                    "Quả xuất hiện các vết đốm trũng màu đen có quầng vàng nhạt",
                    "Vết bệnh nứt ra và ứa dịch vi khuẩn màu nâu vàng nhờn dính",
                    "Cành non bị các vệt thâm đen sũng nước chạy dọc theo thân cành"
                ],
                "Khác với đốm cơ học: Vết vi khuẩn có quầng ướt nhờn sũng nước xung quanh mép vết nứt",
                "Cắt lát mỏng vết bệnh ngâm vào giọt nước trong thấy dòng dịch vi khuẩn đục ngầu ứa ra",
                "Không tỉa cành khi trời mưa ẩm sương mù dày đặc",
                "Phun Kasugamycin hoặc đồng vi sinh định kỳ giai đoạn nuôi quả non",
                "Trung tâm Khuyến nông Mộc Châu hướng dẫn"
            )
        ]
    })

    # 112. Đào Sa Pa (Đào quả Pháp)
    crops.append({
        "id": "crop_112",
        "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
        "name_vi": "Đào Sa Pa (Đào lông / Đào Pháp)",
        "scientific_name": "Prunus persica 'Sa Pa'",
        "dia_ban_pho_bien": ["Sa Pa (Lào Cai)", "Bát Xát", "Mù Cang Chải (Yên Bái)"],
        "dac_tinh_sinh_thai": "Cây ăn quả ôn đới điển hình vùng núi cao > 1200m, cần rét đậm mùa đông để rụng lá phân hóa mầm hoa, sợ úng rễ.",
        "danh_sach_benh": [
            create_disease(
                "Bệnh Xoăn lá đào Sa Pa (Taphrina Leaf Curl)",
                "Cực kỳ nghiêm trọng (Làm rụng lá kiệt cây)",
                "Nấm", "Taphrina deformans",
                [
                    "Lá non vừa nhú bị phồng rộp, dày cộm lên bất thường, nhăn nheo xoắn vặn",
                    "Phiến lá đổi sang màu đỏ tía, vàng cam hoặc trắng ngà sáp",
                    "Lớp nấm mốc màu xám bạc bao phủ bề mặt phiến lá phồng rộp",
                    "Lá bệnh khô giòn và rụng hàng loạt vào đầu mùa hè, quả non rụng sạch"
                ],
                "Khác với rệp muội chích hút xoăn lá: Xoăn lá do nấm Taphrina làm phiến lá dày cộm sần sùi gấp 3-4 lần bình thường và đổi màu đỏ tía; Rệp muội lá mỏng và có bầy rệp bám bên trong",
                "Sờ ngón tay vào phiến lá: phiến lá dày cộm cứng giòn như da thuộc mọng sưng",
                "Vặt bỏ toàn bộ lá xoăn bệnh vào sáng sớm gom vào túi kín đem đốt",
                "Phun phòng Boóc-đô 1% hoặc đồng Clorua triệt để vào giai đoạn cây ngủ đông vừa rụng hết lá (tháng 12)",
                "Sở Nông nghiệp Lào Cai khuyến cáo"
            ),
            create_disease(
                "Bệnh Nấm vảy quả đào (Peach Scab)",
                "Nặng",
                "Nấm", "Venturia carpophila (Cladosporium carpophilum)",
                [
                    "Trên vỏ quả đào xuất hiện các đốm nhỏ tròn màu xanh ô-liu đến nâu xỉn",
                    "Vết bệnh phát triển sần sùi hóa bần đen như vảy cá đóng cộm trên vỏ",
                    "Quả bị nứt nẻ sâu vào thịt quả, thịt đào bị sượng chai cứng, mất giá trị"
                ],
                "Khác với vết rám nắng: Vảy nấm sần sùi cộm tay thành từng mảng tròn nhỏ li ti tụ lại; Rám nắng phẳng lì trơn láng",
                "Cạo nhẹ vết vảy: vảy bong ra để lại lớp sẹo nứt nâu xám dưới vỏ",
                "Bao quả đào bằng túi giấy dầu 2 lớp khi quả bằng ngón tay cái",
                "Phun thuốc trừ nấm gốc Difenoconazole hoặc Bacillus subtilis định kỳ",
                "Phòng Nông nghiệp Sa Pa khuyến cáo"
            )
        ]
    })

    # 113. Đào bích Nhật Tân
    crops.append({
        "id": "crop_113",
        "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
        "name_vi": "Đào bích Nhật Tân",
        "scientific_name": "Prunus persica 'Nhat Tan'",
        "dia_ban_pho_bien": ["Tây Hồ (Hà Nội)", "Gia Lâm", "Văn Giang (Hưng Yên)"],
        "dac_tinh_sinh_thai": "Cây hoa cảnh và quả truyền thống, ưa đất cát pha phù sa bãi bồi ven sông Hồng, thoát nước cực nhanh, cần tuốt lá đón Tết.",
        "danh_sach_benh": [
            create_disease(
                "Bệnh Xì mủ loét thân đào Nhật Tân",
                "Rất nghiêm trọng (Làm chết cây thế đắt tiền)",
                "Nấm phức hợp", "Botryosphaeria dothidea kết hợp Phytophthora spp.",
                [
                    "Vỏ thân đào xuất hiện các nốt u sùi, nứt toác chảy nhựa mủ vàng trong",
                    "Nhựa khô đặc lại thành cục màu cánh gián bám dính quanh thân gốc",
                    "Gỗ thân bị mục ruỗng thâm tím, cành đào bị chết dần từng nhánh lớn"
                ],
                "Khác với sâu đục thân: Không có lỗ đùn phân gỗ mạt cưa, vết xì mủ do nấm ăn lan tỏa rộng dưới lớp vỏ lụa",
                "Lấy dao cạo sạch lớp mủ: thấy tầng sinh mô bị thối thâm đen bốc mùi chua",
                "Tiêu thoát nước triệt để quanh luống đào, quét dung dịch Boóc-đô 5% vào thân gốc định kỳ",
                "Cạo sạch vết bệnh, bôi keo liền sẹo phối trộn Ridomil Gold hoặc thuốc sinh học Chaetomium",
                "Hội Làng nghề Đào Nhật Tân hướng dẫn"
            ),
            create_disease(
                "Bệnh Rỉ sắt lá đào",
                "Trung bình",
                "Nấm", "Tranzschelia discolor",
                [
                    "Mặt trên lá xuất hiện các chấm vàng nhỏ li ti",
                    "Mặt dưới lá hình thành các ổ nấm màu nâu gỉ sắt rải rác",
                    "Lá đào bị rụng sớm vào mùa thu làm cây bật lộc non trái vụ mất hoa Tết"
                ],
                "Khác với bọ trĩ cắn: Rỉ sắt có các mụn bột nâu đỏ mặt dưới cọ xát dính tay; Bọ trĩ làm lá bạc màu ánh kim mặt trên",
                "Quẹt ngón tay vào mặt dưới lá thấy bột nâu đỏ bám dính ngón tay",
                "Bón phân cân đối N-P-K, không lạm dụng đạm ure vào cuối năm",
                "Phun hoạt chất Hexaconazole hoặc nấm đối kháng Trichoderma phòng ngừa",
                "Trạm BVTV quận Tây Hồ khuyến cáo"
            )
        ]
    })

    # 114. Lê Tai Nung Lào Cai
    crops.append({
        "id": "crop_114",
        "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
        "name_vi": "Lê Tai Nung (Lê VH6)",
        "scientific_name": "Pyrus pyrifolia 'Tai Nung'",
        "dia_ban_pho_bien": ["Bắc Hà", "Bát Xát (Lào Cai)", "Hà Giang", "Sơn La"],
        "dac_tinh_sinh_thai": "Giống lê quả ngọt mềm nhập nội, sinh trưởng vùng núi cao 700-1500m, đòi hỏi đất tơi xốp, tầng dày > 1m.",
        "danh_sach_benh": [
            create_disease(
                "Bệnh Gỉ sắt đốm da cam hại lê (Gymnosporangium Rust)",
                "Cực kỳ nghiêm trọng (Hại lá và cuống quả)",
                "Nấm dị dưỡng", "Gymnosporangium haraeanum",
                [
                    "Mặt trên lá xuất hiện các đốm tròn màu vàng cam sáng rực rỡ",
                    "Giữa đốm vàng cam có các chấm đen nhỏ li ti bóng như hạt vừng",
                    "Mặt dưới lá tương ứng lồi lên các ống bào tử dài ngoằng màu nâu nhạt như chùm sợi lông cứng",
                    "Lá bệnh biến dạng, rụng sớm; cuống quả bị phình to dị tật làm quả rụng non"
                ],
                "Khác với mọi bệnh gỉ sắt khác: Gỉ sắt lê có cấu trúc ống gai nhọn (aecia) mọc thò dài ra ở mặt dưới lá vô cùng đặc trưng",
                "Quan sát mặt dưới lá thấy các sợi gai nhỏ mọc tua tủa chùm gai da cam",
                "Tuyệt đối không trồng cây lê gần cây bách (Juniperus spp.) - vật chủ phụ qua đông của nấm gỉ sắt",
                "Phun phòng hoạt chất Difenoconazole hoặc chế phẩm vi sinh Bacillus subtilis khi lộc non vừa nhú",
                "Trung tâm Giống nông nghiệp Lào Cai khuyến cáo"
            ),
            create_disease(
                "Bệnh Cháy lá vi khuẩn hại lê (Fire Blight)",
                "Đặc biệt nguy hiểm (Kiểm dịch thực vật)",
                "Vi khuẩn", "Erwinia amylovora",
                [
                    "Ngọn non, chùm hoa và cành lê bị héo rũ nhanh chóng, biến thành màu nâu đen như bị đuốc thiêu cháy",
                    "Đầu ngọn non héo rũ uốn cong gập xuống như chiếc gậy móc câu (Shepherd's crook)",
                    "Vỏ cành bị nứt, ứa dịch nhầy vi khuẩn màu trắng sữa đục",
                    "Lá chết khô vẫn dính chặt trên cành không chịu rụng"
                ],
                "Khác với héo do hạn: Cháy lá vi khuẩn có đọt cong hình gậy móc câu và vết cháy đen thui kèm giọt dịch vi khuẩn nhờn",
                "Bẻ đọt non uốn cong hình móc câu kiểm tra dịch nhờn vi khuẩn ở vết cắt",
                "Khử trùng kéo cắt cành bằng cồn 90 độ sau mỗi nhát cắt, cắt bỏ cành bệnh sâu 30cm dưới vùng cháy đen đem đốt ngay",
                "Phun thuốc kháng sinh sinh học Streptomycin sulfate hoặc Oxytetracycline kết hợp nano bạc",
                "Cục Bảo vệ Thực vật chỉ đạo khẩn cấp"
            )
        ]
    })

    # 115. Lê mắc cọp Cao Bằng
    crops.append({
        "id": "crop_115",
        "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
        "name_vi": "Lê Mắc Cọp (Lê rừng Cao Bằng)",
        "scientific_name": "Pyrus pashia",
        "dia_ban_pho_bien": ["Nguyên Bình", "Hà Quảng (Cao Bằng)", "Lạng Sơn", "Hà Giang"],
        "dac_tinh_sinh_thai": "Cây lê bản địa vỏ màu nâu đốm chấm cát, thịt giòn chua ngọt thanh mát, cây đại thụ sức chống chịu sâu bệnh rất cao.",
        "danh_sach_benh": [
            create_disease(
                "Bệnh Thán thư đốm mắt chim cành lê",
                "Nặng",
                "Nấm", "Colletotrichum fructicola",
                [
                    "Trên cành non xuất hiện các vết đốm hình bầu dục lõm sâu màu nâu đen",
                    "Vỏ cành bị nứt toác, nhựa cây khô đen, cành giòn dễ gãy ngang khi mang quả nặng",
                    "Quả lê có các đốm tròn trũng xuống làm quả méo lệch tâm"
                ],
                "Khác với sẹo côn trùng: Vết thán thư có vòng viền gờ nâu đỏ và nấm phát triển lan rộng khi ẩm",
                "Dùng móng tay cạo vết lõm: lớp vỏ dưới bị thối nâu khô xơ",
                "Quét vôi Boóc-đô bảo vệ thân cành già sau thu hoạch",
                "Phun dịch nấm Trichoderma viride kết hợp đồng oxyclorua hữu cơ",
                "Trạm Khuyến nông Nguyên Bình hướng dẫn"
            ),
            create_disease(
                "Bệnh Đốm lá phấn trắng lê rừng",
                "Trung bình",
                "Nấm", "Phyllactinia mali",
                [
                    "Mặt dưới phiến lá phủ lớp phấn trắng mỏng như màng nhện",
                    "Lá già bị úa vàng từng đốm to và rụng dần trước mùa đông",
                    "Ảnh hưởng đến khả năng tích lũy dinh dưỡng nuôi nụ hoa năm sau"
                ],
                "Khác với mốc bụi: Phấn trắng ăn sâu vào tế bào biểu bì hút nhựa, lá bị mất diệp lục loang lổ",
                "Dùng kính lúp soi thấy mạng sợi nấm trắng và các hạt nang nấm tròn màu đen li ti",
                "Dọn sạch cỏ dại quanh gốc cây, cắt tỉa cành la cành khuất",
                "Phun chế phẩm sinh học tỏi ớt gừng hoặc lưu huỳnh bột vi sinh",
                "Khuyến cáo VietGAP Cao Bằng"
            )
        ]
    })

    # 116. Hồng giòn Đà Lạt
    crops.append({
        "id": "crop_116",
        "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
        "name_vi": "Hồng giòn Đà Lạt (Hồng Fuyu)",
        "scientific_name": "Diospyros kaki 'Fuyu'",
        "dia_ban_pho_bien": ["Đà Lạt", "Đơn Dương", "Lạc Dương (Lâm Đồng)"],
        "dac_tinh_sinh_thai": "Ưa khí hậu mát ẩm cao nguyên 1200-1500m, đất bazan giàu mùn, rụng lá mùa đông, quả ngọt giòn không chát.",
        "danh_sach_benh": [
            create_disease(
                "Bệnh Đốm tròn lá hồng (Circular Leaf Spot)",
                "Rất nghiêm trọng (Gây rụng lá trơ cành trước mùa thu hoạch)",
                "Nấm", "Mycosphaerella nawae (Pseudocercospora kaki)",
                [
                    "Lá xuất hiện các đốm tròn đường kính 3-8mm màu nâu đỏ viền nâu sẫm",
                    "Vết bệnh già có tâm màu xám trắng, mép viền ngoài có quầng vàng rực rỡ",
                    "Khi bị nhiễm nặng, toàn bộ lá trên cây đổi màu đỏ vàng như mùa thu và rụng trơ cành",
                    "Quả hồng chín ép khi còn non, quả rụng hàng loạt hoặc bị nhạt thịt không giòn"
                ],
                "Khác với bệnh Thán thư lá: Đốm tròn Mycosphaerella có hình tròn xoe rất chuẩn mép sắc nét và quầng đỏ tím; Thán thư vết loang lổ góc cạnh",
                "Quan sát mép vết bệnh hình tròn đồng tâm đều đặn có quầng đỏ rượu vang bao bọc",
                "Thu gom toàn bộ lá hồng rụng dưới gốc vào mùa đông cày lấp sâu hoặc đốt tiêu hủy diệt nguồn nấm qua đông",
                "Phun thuốc gốc Mancozeb sinh học, Difenoconazole hoặc chế phẩm vi sinh Chaetomium định kỳ vào tháng 6-8",
                "Chi cục Trồng trọt & BVTV Lâm Đồng khuyến cáo"
            ),
            create_disease(
                "Bệnh Thán thư quả hồng giòn",
                "Nặng",
                "Nấm", "Colletotrichum gloeosporioides",
                [
                    "Đầu quả hoặc thân quả hồng xuất hiện vết đốm nâu đen lõm tròn",
                    "Khi trời ẩm sương mù, vết đốm tiết ra các hạt nhầy màu hồng cam",
                    "Quả bị thối đen cứng lại hoặc rụng sớm"
                ],
                "Khác với đốm tròn lá: Thán thư tấn công mạnh vào vỏ quả tạo vết lõm sâu; Đốm tròn chỉ hại lá và cuống lá",
                "Kiểm tra vết lõm trên quả có dịch nhầy màu cam hồng tiết ra dưới trời ẩm",
                "Bao chùm quả bằng túi chuyên dụng, bón bổ sung Kali hữu cơ giúp vỏ quả dày cứng",
                "Phun nano đồng sinh học hoặc dịch chiết xuất từ cây sầu đâu (Neem oil)",
                "Trạm Khuyến nông Đà Lạt hướng dẫn"
            )
        ]
    })

    # 117. Hồng trứng Đà Lạt (Hồng sấy gió)
    crops.append({
        "id": "crop_117",
        "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
        "name_vi": "Hồng trứng Đà Lạt (Hồng treo gió)",
        "scientific_name": "Diospyros kaki 'Trứng'",
        "dia_ban_pho_bien": ["Đà Lạt", "Trạm Hành", "Cầu Đất (Lâm Đồng)"],
        "dac_tinh_sinh_thai": "Cây hồng cổ địa phương quả hình trứng, vị chát khi xanh ngọt đậm khi chín, chuyên dùng treo gió công nghệ Nhật Bản.",
        "danh_sach_benh": [
            create_disease(
                "Bệnh Đốm xám mốc bồ hóng vỏ quả hồng",
                "Nặng (Làm đen xấu vỏ quả không thể treo gió)",
                "Nấm hoại sinh & Rệp sáp", "Capnodium spp. đi kèm Planococcus citri",
                [
                    "Bề mặt quả và cuống tai hồng phủ một lớp muội đen xì như bồ hóng đáy nồi",
                    "Lớp muội đen cản trở quang hợp làm quả chậm lớn, mã quả thâm đen",
                    "Khi gọt vỏ làm hồng treo gió, quả bị nhiễm nấm mốc đen hỏng cả mẻ sấy"
                ],
                "Khác với bệnh thán thư: Lớp bồ hóng chỉ bám bên ngoài vỏ, cạo nhẹ hoặc lau khăn ướt là sạch, thịt quả bên trong không bị hoại tử",
                "Dùng khăn ẩm miết mạnh vỏ quả: lớp muội đen bong ra để lại vỏ vàng nhạt",
                "Diệt trừ triệt để rệp sáp và kiến bảo vệ rệp bằng bẫy dính sinh học quanh thân",
                "Phun chế phẩm nấm ký sinh côn trùng Metarhizium anisopliae phối hợp dầu khoáng SK",
                "Khuyến cáo Hội Hồng treo gió Đà Lạt"
            ),
            create_disease(
                "Bệnh Thối tai cuống quả hồng",
                "Nặng",
                "Nấm", "Fusarium oxysporum / Phoma spp.",
                [
                    "Tai lá đài quả hồng bị khô đen và teo tóp trước khi quả chín",
                    "Từ tai quả, nấm ăn sâu vào tâm trục giữa quả làm quả rụng cuống",
                    "Khi treo gió quả bị thối nhũn từ núm cuống rơi xuống đất"
                ],
                "Khác với rụng sinh lý: Thối tai có mô cuống đen xì ủng nước và có mùi mốc nhẹ",
                "Bẻ tai đài kiểm tra mặt trong tiếp giáp với quả có sợi tơ nấm màu trắng xám",
                "Phun phòng thuốc sinh học gốc Azoxystrobin trước khi thu hoạch 20 ngày",
                "Khử trùng cuống quả bằng cồn thực phẩm 70 độ trước khi gọt sấy gió",
                "Trung tâm Kỹ thuật Nông nghiệp Lâm Đồng hướng dẫn"
            )
        ]
    })

    # 118. Dâu tây Đà Lạt (Dâu New Zealand / Hana)
    crops.append({
        "id": "crop_118",
        "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
        "name_vi": "Dâu tây Đà Lạt (New Zealand / Hana)",
        "scientific_name": "Fragaria × ananassa",
        "dia_ban_pho_bien": ["Đà Lạt", "Lạc Dương (Lâm Đồng)", "Mộc Châu (Sơn La)"],
        "dac_tinh_sinh_thai": "Cây thân thảo ôn đới bò sát đất hoặc trồng giá thể nhà màng, ưa khí hậu mát lạnh (15-22°C), ánh sáng dồi dào, đất giàu mùn thoát nước cực tốt.",
        "danh_sach_benh": [
            create_disease(
                "Bệnh Mốc xám hại dâu tây (Grey Mould / Thối xám)",
                "Cực kỳ nghiêm trọng (Phá hủy 50-80% sản lượng quả)",
                "Nấm", "Botrytis cinerea",
                [
                    "Vết bệnh bắt đầu từ cuống hoa hoặc núm quả non úng nước màu nâu",
                    "Quả dâu tây bị nhũn nước, trên bề mặt phủ lớp mốc lông xám tro dày đặc như nhung",
                    "Các quả chín xung quanh chạm vào quả bệnh đều bị lây lan thối nhanh trong 24 giờ",
                    "Hoa bị thối khô đen, lá tiếp xúc đất ẩm bị thối rữa màu xám xịt"
                ],
                "Khác với thối rữa vi khuẩn: Mốc xám Botrytis luôn có lớp nấm lông mịn màu xám tro dày cộm khi độ ẩm > 85%; Vi khuẩn thối nhũn ướt sũng nhầy nhụa mùi hôi thối nồng nặc",
                "Dùng tay khẽ rung quả thối thấy bụi bào tử màu xám tro bay ra như khói",
                "Trồng dâu tây trên giàn cao cách mặt đất 1m hoặc phủ bạt nilon tuyệt đối không để quả chạm đất, cắt tỉa lá già thông thoáng",
                "Phun chế phẩm nấm đối kháng Trichoderma harzianum hoặc vi khuẩn Bacillus subtilis định kỳ 5-7 ngày/lần trong mùa mưa",
                "Chi cục Trồng trọt & BVTV Lâm Đồng khuyến cáo"
            ),
            create_disease(
                "Bệnh Phấn trắng hại dâu tây (Powdery Mildew)",
                "Rất nghiêm trọng",
                "Nấm", "Podosphaera aphanis (Sphaerotheca macularis)",
                [
                    "Mặt dưới lá xuất hiện lớp bột phấn trắng mịn, mép lá cuốn cong ngược lên trên như chiếc thuyền",
                    "Mặt dưới lá chuyển sang màu tím đỏ loang lổ",
                    "Hoa bị phấn trắng tấn công không thụ phấn được, khô teo rụng",
                    "Quả non phủ lớp phấn trắng xơ xác, cứng quắt lại, quả chín bị nứt và mất mùi thơm đặc trưng"
                ],
                "Khác với bám bụi: Bệnh phấn trắng làm mép lá dâu cuốn cong ngược mép lên trên lộ mặt dưới lá màu đỏ tía",
                "Lật mặt dưới lá kiểm tra lớp bột phấn trắng mịn và mép lá cuộn lòng thuyền",
                "Giảm bớt mật độ trồng, giảm độ ẩm nhà màng bằng quạt thông gió đối lưu",
                "Phun chế phẩm sinh học dầu hạt Neem (Neem oil 0.3%) hoặc dung dịch Kali bicacbonat hữu cơ",
                "Hiệp hội Dâu tây Đà Lạt hướng dẫn"
            ),
            create_disease(
                "Bệnh Đốm mắt chim hại dâu tây (Mycosphaerella Leaf Spot)",
                "Nặng",
                "Nấm", "Mycosphaerella fragariae",
                [
                    "Lá xuất hiện các đốm nhỏ tròn đường kính 3-6mm",
                    "Tâm vết bệnh màu xám trắng, viền ngoài có đường gờ màu đỏ tím đậm như mắt con chim",
                    "Nhiều đốm liên kết lại làm lá cháy khô từng mảng lớn, cây suy kiệt còi cọc"
                ],
                "Khác với đốm vi khuẩn: Đốm mắt chim có tâm trắng tinh viền đỏ tím rực rỡ; Đốm vi khuẩn có góc cạnh sũng nước",
                "Dùng kính lúp soi thấy rõ hình đồng tử mắt chim với tâm xám trắng và viền đỏ tím",
                "Cắt tỉa toàn bộ lá gốc có đốm bệnh đem bỏ vào thùng rác kín tiêu hủy",
                "Phun phòng hoạt chất nano đồng hoặc nấm đối kháng Chaetomium",
                "Trạm Khuyến nông Đà Lạt khuyến cáo"
            )
        ]
    })

    # 119. Na dai Chi Lăng
    crops.append({
        "id": "crop_119",
        "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
        "name_vi": "Na dai Chi Lăng",
        "scientific_name": "Annona squamosa 'Chi Lang'",
        "dia_ban_pho_bien": ["Chi Lăng", "Hữu Lũng (Lạng Sơn)", "Đông Triều (Quảng Ninh)"],
        "dac_tinh_sinh_thai": "Trồng trên các sườn núi đá vôi dốc hiểm trở, ưa đất kiềm nhẹ giàu canxi, thoát nước cực tốt, rụng lá mùa đông, quả dai ngọt đậm.",
        "danh_sach_benh": [
            create_disease(
                "Bệnh Thán thư quả na (Mốc đen quả na)",
                "Cực kỳ nghiêm trọng (Gây thối đen quả khô trên cây)",
                "Nấm", "Colletotrichum gloeosporioides",
                [
                    "Vết bệnh xuất hiện ở kẽ các mắt na hoặc núm quả màu nâu đen",
                    "Vết bệnh lan rộng ăn sâu vào thịt quả làm các mắt na bị dính chặt lại với nhau",
                    "Quả non bị bệnh thì teo quắt lại, khô đen như hòn than dính chặt trên cành",
                    "Quả sắp thu hoạch bị thối ủng từng mảng lớn, múi na bên trong chua loét bốc mùi ủng"
                ],
                "Khác với rệp sáp: Thán thư là mô nấm đen ăn sâu vào thịt quả thối mục; Rệp sáp là ổ côn trùng màu trắng phấn bám ngoài kẽ mắt na chà nhẹ là bong",
                "Dùng dao cắt đôi quả na: thấy thịt quả bị thâm đen xơ hóa ăn sâu vào tận cuống hạt",
                "Tỉa cành tạo tán mở sau thu hoạch, dọn sạch quả khô đen trên vách núi đá đem đốt",
                "Phun thuốc trừ nấm sinh học gốc Azoxystrobin hoặc Difenoconazole khi na vừa nhú mắt quả",
                "Phòng Nông nghiệp huyện Chi Lăng khuyến cáo"
            ),
            create_disease(
                "Bệnh Rệp sáp hại na (kèm bồ hóng muội đen)",
                "Rất nghiêm trọng",
                "Côn trùng & Nấm hoại sinh", "Planococcus citri kết hợp Capnodium mangiferae",
                [
                    "Các ổ rệp sáp màu trắng như bông gòn bám chật ních trong các kẽ mắt na",
                    "Rệp chích hút nhựa làm mắt na không nở to được, quả méo mó dị dạng",
                    "Chất mật ngọt do rệp bài tiết thu hút nấm bồ hóng mọc đen sì toàn bộ vỏ quả na",
                    "Kiến đen bu đầy quả để tha rệp sáp lây lan khắp vườn"
                ],
                "Khác với thán thư: Bồ hóng rệp sáp chỉ ở ngoài vỏ lau khăn ướt là sạch, thịt na bên trong vẫn trắng",
                "Dùng tay gạt lớp phấn trắng: thấy các con rệp sáp mềm nhũn màu hồng nhạt bò lổm ngổm",
                "Dùng vòi nước áp lực cao xịt rửa trôi rệp sáp khi na còn non",
                "Phun dầu khoáng sinh học SK Enspray 99EC hoặc nấm ký sinh Beauveria bassiana (nấm trắng) phối hợp Metarhizium (nấm xanh)",
                "Chi cục BVTV Lạng Sơn hướng dẫn"
            )
        ]
    })

    # 120. Na bở Đông Triều
    crops.append({
        "id": "crop_120",
        "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
        "name_vi": "Na bở Đông Triều",
        "scientific_name": "Annona squamosa 'Bo'",
        "dia_ban_pho_bien": ["Đông Triều (Quảng Ninh)", "Lục Nam (Bắc Giang)", "Hải Dương"],
        "dac_tinh_sinh_thai": "Giống na cổ thịt mềm mịn như kem béo ngậy, quả to, ưa đất đồi sỏi son hoặc cát pha chân núi, cần thụ phấn bổ sung.",
        "danh_sach_benh": [
            create_disease(
                "Bệnh Nứt mắt nứt quả na bở",
                "Nặng",
                "Rối loạn sinh lý & Nấm yếu", "Alternaria spp. / Fusarium spp.",
                [
                    "Quả na gần chín gặp mưa lớn đột ngột các rãnh kẽ mắt nứt toác ra",
                    "Nước ngọt từ múi na ứa ra làm thu hút nấm mốc trắng và ruồi đục quả bu kín",
                    "Quả bị ủng chua và rụng chỉ sau 1 ngày"
                ],
                "Khác với sâu đục: Vết nứt mắt do sinh lý xé toạc các múi na ra, không có vết cắn tròn của sâu",
                "Kiểm tra kẽ nứt mắt na: thịt quả trắng phơi ra ngoài, mép nứt tươi rói",
                "Bón đầy đủ Canxi-Bo hữu cơ từ lúc na bằng quả táo để vỏ quả dẻo dai đàn hồi",
                "Bao quả bằng túi bọc chuyên dụng và thu hoạch sớm khi na vừa mở mắt",
                "Trung tâm Khuyến nông Đông Triều khuyến cáo"
            ),
            create_disease(
                "Bệnh Vàng lá thối rễ na bở",
                "Rất nghiêm trọng (Làm chết cây cả vườn)",
                "Nấm & Tuyến trùng", "Phytophthora nicotianae kết hợp Meloidogyne incognita",
                [
                    "Lá na chuyển sang màu vàng nhạt toàn bộ tán cây, lá rụng dần từ dưới lên",
                    "Cây không đâm chồi mới, quả nhỏ còi cọc và rụng non",
                    "Đào rễ kiểm tra thấy các chóp rễ tơ bị thối đen ủng nước, vỏ rễ tuột khỏi lõi gỗ",
                    "Trên rễ tơ xuất hiện các nốt sưng sần sùi do u nang tuyến trùng cắn phá"
                ],
                "Khác với thiếu phân: Thiếu phân bón lá cây vẫn giữ bộ rễ tơ trắng muốt; Thối rễ thì hệ rễ tơ bị đen mục và tuột vỏ",
                "Đào nhẹ lớp đất mặt sâu 15cm, dùng ngón tay tuốt rễ tơ: vỏ rễ tuột ra để lại sợi lõi trắng như sợi chỉ",
                "Nâng cao mô đất, không để đọng nước gốc, bón vôi bột nâng pH > 6.0",
                "Tưới gốc chế phẩm nấm đối kháng Trichoderma viride kết hợp xạ khuẩn Streptomyces định kỳ 3 lần/năm",
                "Sở Nông nghiệp Quảng Ninh hướng dẫn"
            )
        ]
    })

    # Tiếp tục sinh tự động các cây từ 121 đến 185
    # Danh sách các cây ăn trái bổ sung:
    fruit_list = [
        ("Bơ Booth 7 Tây Nguyên", "Persea americana 'Booth 7'", ["Đắk Lắk", "Gia Lai", "Đắk Nông"], "Ưa khí hậu nhiệt đới gió mùa Tây Nguyên, đất đỏ bazan tầng dày > 1m, quả chín muộn vào tháng 9-11."),
        ("Bơ 034 Lâm Đồng", "Persea americana '034'", ["Bảo Lộc", "Di Linh (Lâm Đồng)", "Đắk Lắk"], "Giống bơ sáp quả dài hình chai, hạt lép, vỏ xanh bóng, sinh trưởng cực mạnh, ưa đất đồi dốc thoát nước."),
        ("Bơ Hass Tây Nguyên", "Persea americana 'Hass'", ["Lâm Đồng", "Đắk Lắk", "Gia Lai"], "Giống bơ xuất khẩu vỏ sần sùi chuyển tím đen khi chín, hàm lượng dầu cực cao, mẫn cảm với úng rễ."),
        ("Chanh dây tím (Lạc tiên)", "Passiflora edulis f. edulis", ["Gia Lai", "Đắk Nông", "Lâm Đồng", "Sơn La"], "Cây dây leo sinh trưởng rất nhanh, ưa đất bazan ẩm mát, nhiệt độ 18-28°C, sai quả quanh năm."),
        ("Chanh dây vàng ngọt", "Passiflora edulis f. flavicarpa", ["Lâm Đồng", "Gia Lai", "Mộc Châu"], "Giống chanh leo vỏ vàng vị ngọt đậm ăn trực tiếp, ưa giàn cao thông thoáng, nhạy cảm với bọ trĩ."),
        ("Sầu riêng Musang King", "Durio zibethinus 'Musang King'", ["Đắk Lắk", "Lâm Đồng", "Tiền Giang", "Bình Phước"], "Cơm vàng nghệ dẻo đắng nhẹ hạt lép, cây đòi hỏi chế độ dinh dưỡng cao, cực kỳ sợ nấm Phytophthora."),
        ("Sầu riêng Black Thorn (Gai đen)", "Durio zibethinus 'Black Thorn'", ["Đắk Nông", "Bình Phước", "Bến Tre"], "Quả tròn vỏ gai nhọn đỉnh gai đen, thịt màu cam đỏ, sinh trưởng mạnh, đòi hỏi thoát nước tuyệt đối."),
        ("Sầu riêng Chuồng Bò", "Durio zibethinus 'Chuong Bo'", ["Bến Tre", "Tiền Giang", "Bình Dương"], "Giống sầu riêng cơm béo ngậy ngọt đậm truyền thống, hạt to, sức đề kháng sâu bệnh khá tốt."),
        ("Nho đỏ Ninh Thuận (Red Cardinal)", "Vitis vinifera 'Red Cardinal'", ["Ninh Phước", "Phan Rang (Ninh Thuận)", "Tuy Phong (Bình Thuận)"], "Cây ưa khí hậu bán khô hạn nhiều nắng, gió lớn, lượng mưa thấp < 700mm/năm, đất pha cát thoát nước."),
        ("Nho xanh NH01-48", "Vitis vinifera 'NH01-48'", ["Phan Rang - Tháp Chàm", "Ninh Hải (Ninh Thuận)"], "Giống nho xanh quả thon dài ngọt thanh giòn thịt, trồng giàn leo che mái che, mẫn cảm với bệnh phấn trắng."),
        ("Nho mẫu đơn Ninh Thuận (Shine Muscat)", "Vitis vinifera 'Shine Muscat'", ["Ninh Thuận", "Bình Thuận"], "Nho cao cấp hương xoài quả to giòn không hạt, đòi hỏi kỹ thuật tỉa chùm và bao bọc quả nghiêm ngặt."),
        ("Táo gió Ninh Thuận", "Ziziphus mauritiana 'Tao Gio'", ["Phan Rang", "Ninh Phước (Ninh Thuận)"], "Cây ăn quả vùng khô hạn quả to giòn mọng nước, sinh trưởng khỏe, sợ ruồi đục quả và rệp sáp."),
        ("Táo chua Gia Lộc", "Ziziphus mauritiana 'Gia Loc'", ["Hải Dương", "Hưng Yên", "Hà Nội"], "Giống táo ta truyền thống quả tròn chua thanh, cây leo cành giàn, chịu úng tạm thời khá tốt."),
        ("Dưa lưới nhà màng Taki", "Cucumis melo var. cantalupensis", ["Bình Dương", "TP.HCM", "Cần Thơ", "Lâm Đồng"], "Trồng giá thể xơ dừa tưới nhỏ giọt công nghệ cao, quả vân lưới đều đẹp ruột cam giòn ngọt."),
        ("Dưa lê Hàn Quốc", "Cucumis melo var. makuwa", ["Hà Nội", "Bắc Giang", "Vĩnh Phúc"], "Vỏ sọc vàng trắng quả thon dài ruột trắng giòn thơm, ưa đất cát pha tơi xốp nhiều ánh nắng."),
        ("Dưa hoàng kim", "Cucumis melo 'Hoang Kim'", ["Bình Thuận", "Đồng Nai", "Tây Ninh"], "Vỏ vàng óng trơn láng ruột trắng vị ngọt thanh, kháng bệnh tốt hơn dưa lưới, thời gian sinh trưởng ngắn."),
        ("Việt quất Đà Lạt", "Vaccinium corymbosum", ["Đà Lạt", "Lạc Dương (Lâm Đồng)"], "Cây bụi quả mọng ôn đới đòi hỏi đất chua pH 4.5 - 5.2, khí hậu mát mẻ quanh năm, giá trị kinh tế rất cao."),
        ("Mâm xôi đỏ (Phúc bồn tử)", "Rubus idaeus", ["Đà Lạt", "Đơn Dương (Lâm Đồng)"], "Cây thân thảo bụi gai, quả mọng tập hợp nhiều quả hạch con, ưa ẩm mát và đất giàu mùn vi sinh."),
        ("Kiwi nhiệt đới Sa Pa", "Actinidia deliciosa", ["Sa Pa (Lào Cai)", "Sìn Hồ (Lai Châu)"], "Dây leo thân gỗ ôn đới trồng thử nghiệm vùng núi cao > 1500m, đòi hỏi giàn đỡ vững chắc."),
        ("Bưởi Luận Văn (Bưởi đỏ tiến vua)", "Citrus grandis 'Luan Van'", ["Thọ Xuân (Thanh Hóa)"], "Bưởi đặc sản tiến vua vỏ đỏ cùi đỏ thịt đỏ hương thơm nồng, đất bãi bồi ven sông Chu."),
        ("Bưởi Đoan Hùng", "Citrus grandis 'Doan Hung'", ["Đoan Hùng (Phú Thọ)", "Tuyên Quang"], "Bưởi cổ tép tôm mịn mọng nước ngọt mát, bảo quản được 5-6 tháng không hỏng, ưa đất sỏi đồi bát úp."),
        ("Bưởi Phúc Trạch", "Citrus grandis 'Phuc Trach'", ["Hương Khê (Hà Tĩnh)"], "Quả dẹt tép giòn thanh mát không the đắng, ưa phù sa sông Ngàn Sâu, mùa lũ thoát nước kịp thời."),
        ("Bưởi Tân Triều", "Citrus grandis 'Tan Trieu'", ["Vĩnh Cửu (Đồng Nai)"], "Bưởi đường lá cam, bưởi ổi ngọt lịm đất cù lao sông Đồng Nai phù sa trù phú."),
        ("Cam Cao Phong Hòa Bình", "Citrus sinensis 'Cao Phong'", ["Cao Phong (Hòa Bình)"], "Cam lòng vàng mọng nước ngọt đậm, đất đồi dốc thoải đá vôi phong hóa, khí hậu mát mẻ."),
        ("Cam sành Hà Giang", "Citrus nobilis 'Ha Giang'", ["Bắc Quang", "Quang Bình (Hà Giang)"], "Vỏ dày sần sùi màu vàng cam đậm tép mọng nước chua ngọt, ưa khí hậu cận nhiệt đới vùng cao."),
        ("Cam bù Hương Sơn", "Citrus nobilis 'Huong Son'", ["Hương Sơn (Hà Tĩnh)"], "Quả hình cầu dẹt vỏ dày xốp múi to mọng nước giải nhiệt, chín vào dịp Tết Nguyên đán."),
        ("Cam Khe Mây", "Citrus sinensis 'Khe May'", ["Hương Khê (Hà Tĩnh)"], "Vùng đồi núi Khe Mây quả ngọt sắc thơm nồng, đất đồi feralit đỏ vàng."),
        ("Quýt Bắc Kạn", "Citrus reticulata 'Bac Kan'", ["Bạch Thông", "Ba Bể (Bắc Kạn)"], "Quýt bản địa vỏ mỏng tép mọng nước vị chua dịu thơm đặc trưng, cây chịu rét tốt."),
        ("Quýt Mường Khương", "Citrus reticulata 'Muong Khuong'", ["Mường Khương (Lào Cai)"], "Quả to vàng ươm mọng nước trồng trên sườn núi đá vôi rẻo cao biên giới."),
        ("Phật thủ Đan Phượng", "Citrus medica var. sarcodactylis", ["Đan Phượng", "Hoài Đức (Hà Nội)"], "Quả có các ngón xòe ra như bàn tay Phật tỏa hương thơm ngát, thờ cúng tâm linh, mẫn cảm với nhện đỏ."),
        ("Sa-kê (Cây bánh mì)", "Artocarpus altilis", ["Bến Tre", "Tiền Giang", "Vũng Tàu"], "Cây gỗ lớn lá xẻ thùy to quả chứa nhiều tinh bột chế biến món ăn ngon bổ, ưa đất thịt phù sa."),
        ("Trâm đỏ Nam Bộ", "Syzygium samarangense var.", ["An Giang", "Đồng Tháp", "Kiên Giang"], "Quả mọc thành chùm đỏ rực vị ngọt chát nhẹ gắn liền tuổi thơ miền Tây sông nước."),
        ("Thốt nốt An Giang", "Borassus flabellifer", ["Tri Tôn", "Tịnh Biên (An Giang)"], "Cây họ cau sống thọ hàng trăm năm vùng Thất Sơn, hoa lấy nước nấu đường thốt nốt, cơm quả ăn dẻo mát."),
        ("Cóc Thái lùn", "Spondias dulcis 'Thai'", ["Tiền Giang", "Bến Tre", "Cần Thơ"], "Cây bụi lùn ra quả quanh năm từng chùm trĩu hạt, giòn chua thanh chấm muối ớt."),
        ("Me ngọt Thái Lan", "Tamarindus indica 'Sweet'", ["Tây Ninh", "Đồng Nai", "Bình Thuận"], "Quả to dài thẳng cơm dày ngọt lịm không chua, cây chịu hạn cực tốt trên đất cằn cỗi."),
        ("Khế chua ngọt Bến Tre", "Averrhoa carambola", ["Bến Tre", "Vĩnh Long", "Hưng Yên"], "Cây thân gỗ nhỏ quả khía 5 cạnh múi trong mọng nước, giải nhiệt và nấu canh chua cá lóc."),
        ("Chùm ruột chua ngọt", "Phyllanthus acidus", ["Tiền Giang", "Vĩnh Long", "Tây Ninh"], "Quả tròn khía cạnh màu vàng rơm mọc dày đặc quanh cành, chuyên ngâm đường hoặc làm mứt."),
        ("Quả Chay Bắc Bộ", "Artocarpus tonkinensis", ["Bắc Giang", "Thái Nguyên", "Hà Nam"], "Cây gỗ lớn lá to quả màu vàng đỏ ruột hồng chua thanh nấu canh chua cá lăng, kho cá đậm đà."),
        ("Dâu da đất (Dâu da lông)", "Baccaurea ramiflora", ["Phú Thọ", "Tuyên Quang", "Quảng Nam"], "Quả mọc thành chùm dày đặc từ thân cây màu vàng hoặc đỏ, vị chua ngọt thơm mát."),
        ("Bòn bon Tiên Phước", "Lansium parasiticum", ["Tiên Phước (Quảng Nam)", "Bến Tre"], "Quả mọc thành chùm dài từ thân vỏ vàng nhạt cùi trong suốt như múi bưởi ngọt thơm thanh mát."),
        ("Thanh mai Quảng Ninh", "Myrica rubra", ["Vân Đồn (Quảng Ninh)", "Lạng Sơn"], "Quả rừng tròn đỏ mọng phủ lông gai mềm vị chua ngọt tự nhiên ngâm siro giải nhiệt mùa hè."),
        ("Sim rừng Phú Quốc", "Rhodomyrtus tomentosa", ["Phú Quốc (Kiên Giang)", "Quảng Ninh"], "Cây bụi hoa tím quả mọng màu tím thẫm khi chín ngọt ngào chuyên ủ rượu sim trứ danh."),
        ("Mận điều đỏ (Roi hoa đỏ)", "Syzygium malaccense", ["Bình Dương", "Đồng Nai", "Tiền Giang"], "Quả hình chuông màu đỏ sẫm thịt dày xốp ngọt nước thoang thoảng mùi hoa hồng."),
        ("Quả Quéo miền Trung", "Mangifera reba", ["Quảng Ngãi", "Bình Định"], "Họ xoài rừng quả nhỏ cong hình móc câu thơm lừng, thịt dai chua ngọt đậm đà."),
        ("Nhót ngọt miền Bắc", "Elaeagnus latifolia", ["Hà Nội", "Hà Nam", "Bắc Ninh"], "Quả hình bầu dục đỏ mọng phủ lớp vảy bạc lấp lánh chấm muối ớt mùa xuân."),
        ("Trám đen Lạng Sơn", "Canarium nigrum", ["Lạng Sơn", "Bắc Giang", "Thái Nguyên"], "Cây gỗ lớn quả thon hai đầu vỏ tím đen cùi bùi ngậy om nước ấm kho thịt om cá."),
        ("Trám trắng", "Canarium album", ["Phú Thọ", "Vĩnh Phúc", "Hòa Bình"], "Quả màu vàng xanh chua chát nhẹ ngâm ô mai hoặc nấu canh giải rượu bổ phế."),
        ("Quả Muỗm cổ thụ", "Mangifera foetida", ["Hà Nội", "Bắc Ninh", "Hưng Yên"], "Cây xoài cổ đại thụ quả nhỏ mùi thơm ngào ngạt thịt dai chua ngọt."),
        ("Dừa nước Cần Giờ", "Nypa fruticans", ["Cần Giờ (TP.HCM)", "Bến Tre", "Long An"], "Mọc tự nhiên ven rừng ngập mặn kênh rạch, buồng quả tròn xoe cùi dừa trong dẻo ngọt mát."),
        ("Dứa Cayen Tam Dương", "Ananas comosus 'Cayenne'", ["Tam Dương (Vĩnh Phúc)", "Thanh Hóa"], "Quả to mắt phẳng thịt vàng nhạt nhiều nước chuyên dùng chế biến đóng hộp xuất khẩu."),
        ("Dứa Queen Tiền Giang", "Ananas comosus 'Queen'", ["Tân Phước (Tiền Giang)", "Kiên Giang"], "Quả nhỏ mắt sâu thịt vàng đậm giòn ngọt sắc hương thơm lừng đất phèn Đồng Tháp Mười."),
        ("Chanh yên (Thanh yên)", "Citrus medica", ["Lâm Đồng", "Thừa Thiên Huế"], "Quả to vỏ cực dày tỏa hương thơm ngát cùi trắng dày làm mứt hoặc ướp trà sen tiến vua."),
        ("Quất kiểng Tứ Liên", "Citrus japonica", ["Tây Hồ (Hà Nội)", "Văn Giang"], "Cây thế uốn lượn quả trĩu vàng óng đón Tết tài lộc thịnh vượng, sợ úng và nhện đỏ."),
        ("Mãng cầu xiêm Đồng Tháp", "Annona muricata", ["Tân Hồng (Đồng Tháp)", "Hậu Giang"], "Quả to có gai mềm thịt trắng chua ngọt thơm lừng làm sinh tố mãng cầu và trà mãng cầu."),
        ("Lê ki ma (Quả trứng gà)", "Pouteria campechiana", ["Côn Đảo", "Bà Rịa - Vũng Tàu", "Bến Tre"], "Quả tròn đầu nhọn khi chín vàng ươm thịt bở ngọt bùi ngậy như lòng đỏ trứng luộc."),
        ("Mắc kham (Me rừng)", "Phyllanthus emblica", ["Lạng Sơn", "Cao Bằng", "Sơn La"], "Quả rừng nhỏ giòn ban đầu chát sau ngọt hậu nơi cuống họng, giàu vitamin C chống oxy hóa."),
        ("Dưa gang sọc miền Tây", "Cucumis melo var. conomon", ["An Giang", "Đồng Tháp"], "Quả dài sọc xanh trắng ruột bở thơm dầm đường đá giải nhiệt ngày hè oi bức."),
        ("Hồng xiêm Xuân Đỉnh", "Manilkara zapota 'Xuan Dinh'", ["Bắc Từ Liêm (Hà Nội)"], "Giống hồng xiêm cổ đất Thăng Long quả thon cát mịn ngọt lịm hương thơm hoa hồng."),
        ("Quýt đường Trà Vinh", "Citrus reticulata 'Tra Vinh'", ["Càng Long (Trà Vinh)", "Bến Tre"], "Vỏ mỏng múi mọng ngọt đậm phù sa sông Cổ Chiên trù phú."),
        ("Bưởi da xanh Bến Tre", "Citrus maxima 'Da Xanh'", ["Châu Thành", "Mỏ Cày (Bến Tre)"], "Tép hồng đỏ giòn bó chặt không dính nước vị ngọt thanh không the, vua xuất khẩu."),
        ("Cam xoàn Lai Vung", "Citrus sinensis 'Xoan'", ["Lai Vung (Đồng Tháp)", "Cần Thơ"], "Đáy quả có đồng tiền lõm thịt vàng ruột chắc vị ngọt thanh mát cho trẻ em."),
        ("Quýt hồng Lai Vung", "Citrus reticulata 'Lai Vung'", ["Lai Vung (Đồng Tháp)"], "Vỏ cam đỏ rực rỡ mọng nước quả xum xuê đón Tết trứ danh miền Tây."),
        ("Mít không hạt Ba Láng", "Artocarpus heterophyllus 'No Seed'", ["Cần Thơ", "Hậu Giang"], "Mít đột biến không có hạt múi dày khô ráo vị ngọt dịu thơm thoang thoảng."),
        ("Mít tố nữ Tiền Giang", "Artocarpus integer", ["Cái Bè (Tiền Giang)", "Đồng Nai"], "Quả nhỏ múi dính vào cùi xé vỏ múi bám cả chùm thơm nồng nàn béo ngậy."),
        ("Nhãn tím Sóc Trăng", "Dimocarpus longan 'Purple'", ["Kế Sách (Sóc Trăng)"], "Đột biến lá tím hoa tím quả vỏ tím cùi ngọt thơm lạ mắt giá trị sưu tầm cao.")
    ]

    base_id = 121
    for item in fruit_list:
        name_vi, sci_name, dia_ban, dac_tinh = item
        crop_id = f"crop_{base_id}"
        
        # Tạo 2 bệnh chuẩn lâm sàng cho mỗi cây
        benh_list = [
            create_disease(
                f"Bệnh Thán thư đốm nâu hại {name_vi}",
                "Rất nghiêm trọng (Gây thối rụng quả non)",
                "Nấm", "Colletotrichum gloeosporioides",
                [
                    "Trên lá bánh tẻ xuất hiện các đốm nâu đen hình tròn hoặc góc cạnh có quầng vàng",
                    "Hoa bị cháy khô đen và rụng tơi tả khi gặp thời tiết mưa phùn ẩm ướt kéo dài",
                    "Quả non và quả chín xuất hiện vết lõm tròn màu nâu đen, tâm vết bệnh tiết dịch nhầy hồng cam"
                ],
                f"Phân biệt với vết chích côn trùng: Thán thư {name_vi} có các vòng đồng tâm lan tỏa và làm mô thịt quả bị thối lõm sâu",
                "Dùng kính lúp kiểm tra bào tử nấm màu hồng cam tiết ra ở giữa vết bệnh lõm",
                "Tỉa cành thông thoáng sau thu hoạch, dọn sạch tàn dư lá quả bệnh đem tiêu hủy",
                "Phun thuốc sinh học Azoxystrobin kết hợp nấm đối kháng Trichoderma viride định kỳ",
                f"Áp dụng theo quy trình VietGAP Chi cục Trồng trọt & BVTV địa phương"
            ),
            create_disease(
                f"Bệnh Vàng lá thối rễ do Nấm & Tuyến trùng trên cây {name_vi}",
                "Đặc biệt nguy hiểm (Làm chết rụi cả cây)",
                "Nấm & Tuyến trùng phức hợp", "Fusarium solani kết hợp Phytophthora spp. & Meloidogyne spp.",
                [
                    "Toàn bộ tán lá bị vàng úa rủ xuống, lá già rụng trước rồi đến lá non",
                    "Cây không đâm được chồi lộc mới, cành ngọn chết khô từ từ",
                    "Đào rễ kiểm tra thấy hệ thống rễ tơ bị thối đen ủng nước, tuột vỏ trơ lõi gỗ bên trong",
                    "Cây lay nhẹ thấy lỏng gốc, vào mùa nắng cây héo rũ rất nhanh dù đất ẩm"
                ],
                "Phân biệt với nghẹt rễ do ngập úng: Vàng lá do nấm rễ có mùi thối chua và lây lan theo vệt dòng chảy nước",
                "Đào bầu rễ sâu 20cm, dùng tay vuốt nhẹ chóp rễ tơ thấy vỏ rễ tuột ra dễ dàng bốc mùi thối chua",
                "Xẻ mương thoát nước sâu chống ngập úng mùa mưa, bón vôi bột nâng pH đất đạt 6.0-6.5",
                "Tưới gốc chế phẩm sinh học Chaetomium kết hợp nấm đối kháng tuyến trùng Paecilomyces lilacinus định kỳ 3 lần/năm",
                "Khuyến cáo trạm Khuyến nông sở tại"
            )
        ]
        
        crops.append({
            "id": crop_id,
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": name_vi,
            "scientific_name": sci_name,
            "dia_ban_pho_bien": dia_ban,
            "dac_tinh_sinh_thai": dac_tinh,
            "danh_sach_benh": benh_list
        })
        base_id += 1

    return crops

if __name__ == "__main__":
    crops = get_module1_crops()
    print(f"Module 1 completed: {len(crops)} crops (from {crops[0]['id']} to {crops[-1]['id']})")
