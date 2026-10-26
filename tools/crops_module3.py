# -*- coding: utf-8 -*-
"""
Module 3: 55 Staple & Food Crops (Cay_Luong_Thuc_Va_Hoa_Mau)
Crops: crop_246 to crop_300
"""

def get_module3_crops():
    crops = [
        {
            "id": "crop_246",
            "topic": "Cay_Luong_Thuc_Va_Hoa_Mau",
            "name_vi": "Lúa Nếp Cái Hoa Vàng",
            "scientific_name": "Oryza sativa L. var. glutinosa",
            "dia_ban_pho_bien": ["Bắc Ninh", "Hải Dương", "Hà Nội", "Ninh Bình", "Nam Định"],
            "dac_tinh_sinh_thai": "Giống lúa nếp truyền thống hạt tròn mẩy, thân cao 120-145cm, cảm quang mạnh, thích hợp vụ Mùa ở đồng bằng Bắc Bộ, chịu rét khá, hạt gạo dẻo thơm ngát.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Đạo ôn lá và Cổ bông (Rice Blast)",
                    "muc_do_nguy_hiem": "Rất cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Magnaporthe oryzae (Pyricularia oryzae)"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết bệnh trên phiến lá ban đầu là chấm kim nâu xám, sau lan rộng thành hình mắt én hai đầu nhọn, tâm xám trắng viền nâu đậm",
                        "Cổ bông bị nấm tấn công chuyển sang màu nâu sẫm, teo tóp thắt nghẽn làm toàn bộ bông lúa gãy gục và lép trắng hoàn toàn",
                        "Trên đốt thân xuất hiện đốm đen làm thân lúa giòn rụm, dễ đổ non khi gặp gió lớn"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với bệnh đốm nâu lá (Cochliobolus miyabeanus): Đạo ôn có vết bệnh hình mắt én nhọn hai đầu tâm bạc trắng; đốm nâu tròn bầu dục nhỏ, tâm nâu nhạt viền vàng hẹp và không làm gãy gục cổ bông.",
                    "kiem_tra_thuc_dia": "Sờ nắn vào đoạn cổ bông bị thâm thấy mô vỏ khô quắt xơ xác, xoay nhẹ bông lúa bị gãy ngang khớp cổ bông, buổi sáng ẩm ướt có lớp mốc xám mịn bám trên vết thắt.",
                    "phac_do_vietgap": {
                        "canh_tac": "Không bón thừa đạm Ure trong giai đoạn phân hóa đòng; bổ sung phân Silic và Kali trắng để làm dày thành tế bào biểu bì lúa; giữ mực nước mặt ruộng nông 3-5cm.",
                        "sinh_hoc": "Phun phòng chế phẩm sinh học nấm đối kháng Chaetomium cupreum hoặc vi khuẩn đối kháng Bacillus amyloliquefaciens ở giai đoạn trỗ lẹt xẹt và trỗ đều.",
                        "khuyen_cao_chuyen_gia": "Khi tỷ lệ lá nhiễm đạo ôn trên 5%, lập tức giữ nước ruộng và phun luân phiên hoạt chất Tricyclazole, Fenoxanil hoặc Isoprothiolane theo đúng nồng độ 4 đúng."
                    }
                },
                {
                    "ten_benh": "Bệnh Khô vằn lúa nếp (Sheath Blight)",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Rhizoctonia solani"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết đốm hình vân mây màu xám xanh hoặc lục nhạt xuất hiện ở bẹ lá sát mặt nước ruộng",
                        "Vết bệnh lan dần lên bẹ lá phía trên và phiến lá, hình thành các mảng loang lổ dạng da hổ viền nâu thẫm",
                        "Hạch nấm hình cầu dẹt màu nâu sẫm như hạt cải dính chặt vào bẹ lá bị bệnh"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với thối thân lúa (Sclerotium oryzae): Khô vằn có vân mây rõ nét dợn sóng hình da hổ trên bẹ ngoài; thối thân làm mô bẹ sũng nước màu đen nhớt và hạch nấm nhỏ li ti nằm sâu bên trong ruột rỗng.",
                    "kiem_tra_thuc_dia": "Bóc nhẹ bẹ lá phía ngoài quan sát mảng vân mây, dùng đầu móng tay cạy hạch nấm tròn cứng màu nâu sẫm rụng rơi dễ dàng, mô bẹ bị teo nhưng không có mùi chua.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cấy mật độ vừa phải 35-40 khóm/m2, làm sạch cỏ bờ ruộng; rút nước phơi ruộng nứt chân chim ở cuối đẻ nhánh để ức chế hạch nấm nổi mặt nước.",
                        "sinh_hoc": "Phun nấm đối kháng Trichoderma harzianum hoặc chế phẩm sinh học chứa Validamycin nguồn gốc lên men tự nhiên.",
                        "khuyen_cao_chuyen_gia": "Phun thuốc gốc Validamycin A, Hexaconazole hoặc Azoxystrobin tập trung vào gốc lúa khi bệnh chớm xuất hiện ở bẹ chân."
                    }
                }
            ]
        },
        {
            "id": "crop_247",
            "topic": "Cay_Luong_Thuc_Va_Hoa_Mau",
            "name_vi": "Lúa Séng Cù Mường Lò",
            "scientific_name": "Oryza sativa L.",
            "dia_ban_pho_bien": ["Yên Bái", "Lào Cai", "Điện Biên", "Lai Châu"],
            "dac_tinh_sinh_thai": "Lúa thuần đặc sản thung lũng Mường Lò và Mường Khương, sinh trưởng trong biên độ nhiệt ngày đêm lớn, nguồn nước suối núi cao giàu khoáng, cơm dẻo đậm đà hương cốm.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Bạc lá vi khuẩn lúa (Bacterial Leaf Blight)",
                    "muc_do_nguy_hiem": "Rất cao",
                    "tac_nhan": {
                        "loai": "Vi khuẩn",
                        "ten_khoa_hoc": "Xanthomonas oryzae pv. oryzae"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết bệnh bắt đầu từ mép lá hoặc chóp lá lan dần vào phiến lá theo hình gợn sóng màu xanh xám tái",
                        "Mô lá bị cháy khô bạc trắng như mảnh giấy dó phơi nắng, ranh giới giữa phần xanh và phần cháy gợn sóng lượn vàng",
                        "Sáng sớm trời ẩm có các giọt dịch vi khuẩn màu vàng đục ứa ra trên mép lá khô lại thành hạt tròn"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với bệnh đốm sọc vi khuẩn (Xanthomonas oryzae pv. oryzicola): Bạc lá chạy dọc rìa mép lá tạo mảng cháy lớn mép gợn sóng; đốm sọc tạo các vệt sọc hẹp dài giữa các gân phụ trong phiến lá.",
                    "kiem_tra_thuc_dia": "Cắt đoạn lá chuyển tiếp giữa vùng xanh và bạc nhúng vào cốc nước trong, sau 2-3 phút thấy dòng mây dịch vi khuẩn màu trắng đục tuôn ra từ bó mạch dẫn.",
                    "phac_do_vietgap": {
                        "canh_tac": "Tuyệt đối ngừng bón đạm khi phát hiện chớm bệnh; bổ sung lân và tro bếp giàu kali; không để mực nước ngập sâu sau mưa dông gió lốc.",
                        "sinh_hoc": "Phun chế phẩm sinh học dịch chiết tỏi ớt gừng hoặc vi khuẩn đối kháng Bacillus subtilis.",
                        "khuyen_cao_chuyen_gia": "Phun ngay các hoạt chất đặc trị vi khuẩn như Bronopol, Bismerthiazol hoặc Oxolinic acid khi lá chớm có gợn sóng tái xanh mép lá."
                    }
                },
                {
                    "ten_benh": "Bệnh Lem lép hạt lúa Séng Cù (Grain Discoloration)",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Tổ hợp nấm Fusarium spp., Bipolaris oryzae, Curvularia lunata"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vỏ trấu hạt lúa xuất hiện các đốm nâu đen, xám tro hoặc loang lổ sẫm màu trong giai đoạn ngậm sữa và chín sáp",
                        "Hạt lép lửng hoặc lép hoàn toàn, phôi hạt bị nấm xâm nhiễm làm thối mầm hoặc gạo xay xát bị đục nát vỡ vụn",
                        "Bông lúa đứng thẳng không cong cong oằn hạt do trọng lượng hạt lép nhẹ"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với hạt lép do bọ xít hôi chích hút: Lem lép nấm có vết đốm lan rộng loang lổ viền xám tro không có vết kim chích; vết bọ xít có đốm kim đen tròn ở giữa xung quanh có quầng xám nhạt.",
                    "kiem_tra_thuc_dia": "Tách vỏ trấu hạt lúa bệnh kiểm tra phôi nhũ bên trong, phôi teo tóp có bột phấn nấm xám đen hoặc hạt gạo bị đổi màu nâu sẫm, ngửi có mùi hôi mốc nhẹ.",
                    "phac_do_vietgap": {
                        "canh_tac": "Xử lý hạt giống trước khi gieo mạ bằng nước ấm 3 sôi 2 lạnh hoặc dung dịch muối 15%; bón phân NPK cân đối theo từng thời kỳ.",
                        "sinh_hoc": "Phun nấm đối kháng Chaetomium và kích kháng chitosan nano trước khi lúa trỗ đòng 5 ngày.",
                        "khuyen_cao_chuyen_gia": "Phun phòng trừ kép 2 lần bằng hoạt chất Difenoconazole + Propiconazole hoặc Tebuconazole + Trifloxystrobin ở thời điểm lúa chuẩn bị trỗ và sau khi trỗ thoát đều."
                    }
                }
            ]
        },
        {
            "id": "crop_248",
            "topic": "Cay_Luong_Thuc_Va_Hoa_Mau",
            "name_vi": "Lúa Nếp Tú Lệ",
            "scientific_name": "Oryza sativa L. var. glutinosa",
            "dia_ban_pho_bien": ["Văn Chấn - Yên Bái", "Mù Cang Chải", "Nghĩa Lộ"],
            "dac_tinh_sinh_thai": "Giống nếp tan nương hạt to bầu dục, hương vị cốm ngọt thanh, sinh trưởng trên thung lũng đất pha cát sỏi bồi tụ từ dòng suối Nậm Thia dưới chân đèo Khau Phạ.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Than vàng lúa nếp (False Smut / Bệnh hoa cúc)",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Ustilaginoidea virens (Villosiclava virens)"
                    },
                    "trieu_chung_dien_hinh": [
                        "Hạt lúa riêng lẻ trên bông bị phồng to gấp đôi gấp ba kích thước hạt bình thường",
                        "Màng vỏ trấu bung nứt làm lộ ra khối nấm hình cầu màu vàng cam như cánh hoa cúc",
                        "Về sau khối bột bào tử chuyển sang màu xanh ôliu đậm rồi đen sẫm, phát tán độc tố vào các hạt lúa lân cận"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với bệnh than đen (Tilletia horrida): Than vàng tạo khối cầu lớn xốp phồng xòe ra ngoài vỏ trấu; than đen giữ nguyên hình dạng vỏ trấu bên trong chứa bột than màu đen như muội đèn.",
                    "kiem_tra_thuc_dia": "Dùng tay sờ vào hạt hoa cúc thấy màng nhung mịn dính bột vàng phấn bám đầy ngón tay, bóp nhẹ thấy nhân bên trong rắn xốp màu trắng phấn viền vàng.",
                    "phac_do_vietgap": {
                        "canh_tac": "Không bón quá nhiều đạm vào giai đoạn nuôi đòng; vệ sinh đồng ruộng và thu gom các bông lúa có hạt hoa cúc đem tiêu hủy xa ruộng.",
                        "sinh_hoc": "Phun chế phẩm vi sinh kháng nấm Streptomyces trước khi trỗ đòng rộ.",
                        "khuyen_cao_chuyen_gia": "Phun phòng hoạt chất chứa Đồng Hydroxide hoặc Hexaconazole, Copper Oxychloride trước khi bao bông nứt vỏ 7 ngày."
                    }
                },
                {
                    "ten_benh": "Bệnh Vàng lá vi khuẩn (Bacterial Leaf Streak)",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Vi khuẩn",
                        "ten_khoa_hoc": "Xanthomonas oryzae pv. oryzicola"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết bệnh là các sọc nhỏ hẹp chạy dài giữa các gân lá song song lúc đầu màu xanh trong thấu quang",
                        "Vết sọc chuyển dần sang màu vàng cam rồi nâu đỏ sẫm, lá lúa bị khô héo từng dải sọc",
                        "Mặt dưới phiến lá ứa ra các hạt giọt keo vi khuẩn tròn nhỏ li ti màu vàng óng như hạt hổ phách"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với vết sọc do rầy chích hút: Đốm sọc vi khuẩn có bờ mép gân lá giữ lại thẳng tắp và có hạt giọt sáp vàng ứa ra; vết chích hút rầy có quầng thâm tròn và không rỉ sáp dịch.",
                    "kiem_tra_thuc_dia": "Đưa phiến lá soi ngược ánh sáng mặt trời nhìn thấy rõ các sọc mảnh trong suốt chạy dọc gân lá, vuốt ngón tay cảm nhận các hạt sáp sần sùi bám dính nhẹ.",
                    "phac_do_vietgap": {
                        "canh_tac": "Thoát nước cạn ruộng khi chớm thấy sọc lá; rải vôi bột khử trùng mặt ruộng tỷ lệ 15-20kg/sào Bắc Bộ.",
                        "sinh_hoc": "Phun dung dịch sinh học Nano Đồng Chitosan tăng cường kháng thể bề mặt biểu bì lá.",
                        "khuyen_cao_chuyen_gia": "Phun thuốc đặc trị gốc Oxolinic acid, Thiodiazole copper hoặc Ningnanmycin khi tỷ lệ dải sọc lan rộng trên 10% diện tích tán lá."
                    }
                }
            ]
        },
        {
            "id": "crop_249",
            "topic": "Cay_Luong_Thuc_Va_Hoa_Mau",
            "name_vi": "Lúa Tám Xoan Hải Hậu",
            "scientific_name": "Oryza sativa L.",
            "dia_ban_pho_bien": ["Nam Định", "Thái Bình", "Ninh Bình"],
            "dac_tinh_sinh_thai": "Lúa mùa truyền thống ven biển phù sa châu thổ sông Hồng, vỏ trấu màu vàng mơ, hạt cơm thon nhỏ màu trắng trong bóng, thơm tự nhiên đậm đà.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Lùn sọc đen phương Nam (Southern Rice Black-streaked Dwarf)",
                    "muc_do_nguy_hiem": "Rất cao",
                    "tac_nhan": {
                        "loai": "Virus",
                        "ten_khoa_hoc": "Southern rice black-streaked dwarf virus (SRBSDV)",
                        "vector_truyen_benh": "Rầy lưng trắng (Sogatella furcifera)"
                    },
                    "trieu_chung_dien_hinh": [
                        "Cây lúa bị lùn còi nghiêm trọng, lá màu xanh đậm bất thường và phiến lá ngắn dựng đứng cứng đờ",
                        "Dọc theo gân mặt sau của bẹ lá và thân cây xuất hiện các u bướu sần sùi hoặc vệt sọc đen dài 1-3mm",
                        "Lúa không trỗ được bông hoặc bông trỗ nghẹn bên trong bẹ lá, hạt lép đen hoàn toàn"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với bệnh vàng lùn (RGSV do rầy nâu truyền): Lùn sọc đen lá màu xanh thẫm dày cứng và có u sần sọc đen ở gân thân lá; vàng lùn lá úa vàng cam từ ngọn xuống và không có u bướu gân lá.",
                    "kiem_tra_thuc_dia": "Dùng ngón tay miết dọc theo bẹ lá và lóng thân thấy cảm giác gồ ghề vấp tay ở các u bướu sần màu trắng đục sau hóa đen.",
                    "phac_do_vietgap": {
                        "canh_tac": "Gieo cấy né rầy tập trung; che chắn nilon mạ non tránh rầy lưng trắng xâm nhập; tiêu hủy triệt để khóm lúa bệnh bằng cách nhổ vùi sâu dưới bùn.",
                        "sinh_hoc": "Bảo vệ các loài thiên địch tự nhiên như bọ xít nước, nhện Lycosa, bọ rùa đỏ trên ruộng.",
                        "khuyen_cao_chuyen_gia": "Xử lý hạt giống bằng hoạt chất Thiamethoxam; phun trừ rầy lưng trắng bằng Pymetrozine hoặc Dinotefuran giai đoạn mạ và lúa đẻ nhánh."
                    }
                },
                {
                    "ten_benh": "Bệnh Đốm nâu lá lúa Tám Xoan (Brown Spot)",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Bipolaris oryzae (Cochliobolus miyabeanus)"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết bệnh trên phiến lá hình tròn hoặc bầu dục nhỏ màu nâu thẫm phân bố rải rác",
                        "Xung quanh đốm nâu có quầng tròn màu vàng sáng rõ rệt như mắt mè",
                        "Khi bệnh nặng các đốm liên kết làm toàn bộ phiến lá úa vàng khô lụi sớm, cây suy kiệt"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với bệnh đạo ôn: Đốm nâu hình bầu dục đều tròn cạnh có quầng vàng nhạt; đạo ôn hình mắt én hai đầu nhọn hoắt và tâm màu trắng xám tro.",
                    "kiem_tra_thuc_dia": "Nhìn mặt đất ruộng thấy thường xảy ra ở vùng chân ruộng trũng phèn chua hoặc đất cát pha nghèo mùn; cạy rễ lúa thấy rễ bị đen đầu rễ do ngộ độc axit hữu cơ.",
                    "phac_do_vietgap": {
                        "canh_tac": "Rải vôi bột khử chua hạ phèn; bón phân hữu cơ hoai mục và lân nung chảy để kích rễ phát triển; không để đất ruộng bị khô nứt hạn hán.",
                        "sinh_hoc": "Tưới bổ sung chế phẩm vi sinh phân giải phèn lân Pseudomonas putida kết hợp Trichoderma.",
                        "khuyen_cao_chuyen_gia": "Phun hoạt chất Mancozeb, Iprodione hoặc Difenoconazole khi xuất hiện nhiều chấm mè nâu trên lá công năng."
                    }
                }
            ]
        },
        {
            "id": "crop_250",
            "topic": "Cay_Luong_Thuc_Va_Hoa_Mau",
            "name_vi": "Lúa Nếp Cẩm Tây Bắc",
            "scientific_name": "Oryza sativa L. var. glutinosa",
            "dia_ban_pho_bien": ["Sơn La", "Điện Biên", "Hòa Bình", "Hà Giang"],
            "dac_tinh_sinh_thai": "Lúa nếp than truyền thống vùng núi cao Tây Bắc, sắc tố anthocyanin màu tím đen sẫm giàu chất chống oxy hóa, thân lá màu tím tía nhẹ, gạo dẻo béo ngậy.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Đốm sọc gân lá lúa Nếp Cẩm (Narrow Brown Leaf Spot)",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Cercospora janseana (Sphaerulina oryzina)"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết bệnh là các vệt sọc hẹp ngắn màu nâu đỏ hoặc nâu tím chạy dọc song song giữa các gân lá",
                        "Vết sọc có kích thước 2-10mm dài, chiều ngang rất hẹp chỉ 1mm",
                        "Khi bệnh rộ vào thời điểm lúa trỗ chín, toàn bộ phiến lá chuyển màu nâu xỉn khô cháy từ chóp lá"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với bệnh đốm sọc vi khuẩn: Đốm sọc Cercospora có màu nâu sẫm khô ráp và không có dịch vi khuẩn ứa ra giọt sáp vàng khi trời ẩm ướt.",
                    "kiem_tra_thuc_dia": "Quan sát mặt lá thấy các vệt chỉ màu nâu đỏ khô gọn, bẻ gập phiến lá thấy giòn vụn ở vùng tập trung nhiều vệt sọc sẫm.",
                    "phac_do_vietgap": {
                        "canh_tac": "Bón bổ sung phân Kali và phân trung vi lượng Kẽm - Bo; tránh bón thừa đạm đơn độc.",
                        "sinh_hoc": "Phun dung dịch lên men tỏi gừng ớt kết hợp chế phẩm sinh học đối kháng Bio-Trichoderma.",
                        "khuyen_cao_chuyen_gia": "Phun phòng hoạt chất Azoxystrobin + Difenoconazole vào thời kỳ làm đòng và trỗ lẹt xẹt."
                    }
                },
                {
                    "ten_benh": "Bệnh Thối bẹ cờ lúa Nếp Cẩm (Sheath Rot)",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Sarocladium oryzae"
                    },
                    "trieu_chung_dien_hinh": [
                        "Bẹ lá bao quanh đòng cờ xuất hiện các mảng thối màu nâu xám bất định",
                        "Bông lúa không thoát trỗi ra ngoài được, bị nghẹn dính chặt bên trong bẹ lá ẩm ướt",
                        "Bên trong bẹ bao phủ lớp nấm trắng xốp mỏng, hạt lúa bên trong bị thối nâu lép xỉn"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với nghẹn đòng do nhện gié: Thối bẹ Sarocladium có mảng thối lớn ẩm nhầy viền nâu sẫm bao phủ bột phấn trắng; nhện gié cắn tạo vệt cạo màu bã trầu dạng vệt dài khô ráp.",
                    "kiem_tra_thuc_dia": "Dùng dao lam rạch dọc bẹ lá đòng cờ bị nghẹn thấy các hạt bên trong bị thối nhũn nâu đen và có mùi chua nồng của nấm phân hủy.",
                    "phac_do_vietgap": {
                        "canh_tac": "Làm sạch cỏ dại bờ mương và cây ký chủ phụ; gieo cấy mật độ hợp lý đảm bảo ruộng thông thoáng ánh sáng.",
                        "sinh_hoc": "Phun nấm đối kháng Chaetomium globosum giai đoạn ôm đòng non.",
                        "khuyen_cao_chuyen_gia": "Phun thuốc gốc Carbendazim hoặc Propiconazole trực tiếp vào bẹ lá cờ khi bẹ đòng phình to."
                    }
                }
            ]
        }
    ]
    
    # Generate remaining crops: crop_251 to crop_300 (50 crops)
    additional_crops_data = [
        ("crop_251", "Lúa Đen Brieng Kon Tum", "Oryza sativa L.", ["Kon Tum", "Gia Lai", "Đắk Lắk"],
         "Giống lúa rẫy cổ truyền của đồng bào Ba Na và Gia Rai, chịu hạn vượt trội trên đất dốc ba-zan, hạt gạo màu đen tuyền giàu dinh dưỡng.",
         "Bệnh Cháy lá đốm mắt chim lúa rẫy", "Nấm", "Bipolaris oryzae", "Cao",
         "Vết bệnh hình tròn viền nâu đỏ tâm xám nhạt như mắt chim trên phiến lá lúa rẫy.",
         "Phân biệt với rầy chích: Mắt chim có viền sắc nét quầng vàng rộng quanh tâm xám đục.",
         "Sờ mặt lá nhám ráp ở vùng đốm nâu khô.",
         "Phun phòng hoạt chất Difenoconazole kết hợp bón vôi hạ chua đất dốc nương rẫy."),
        
        ("crop_252", "Lúa Rẫy Ê Đê Đắk Lắk", "Oryza sativa L.", ["Đắk Lắk", "Đắk Nông", "Lâm Đồng"],
         "Lúa rẫy vùng đất đỏ cao nguyên, canh tác hoàn toàn nhờ nước trời, bộ rễ ăn sâu cắm chặt vào tầng đất bazan, chịu hạn phi thường.",
         "Bệnh Đốm gỉ sắt lúa rẫy", "Nấm", "Puccinia spp.", "Trung bình",
         "Các chấm mụn nhỏ li ti màu vàng cam rỉ sắt nổi gồ trên mặt phiến lá lúa rẫy.",
         "Phân biệt với đốm nâu: Gỉ sắt có ổ bào tử nổi cộm bóp ra bột mịn màu da cam rỉ sắt.",
         "Miết ngón tay lên lá dính bột vàng rỉ sét rõ rệt.",
         "Phun dung dịch sinh học Nano Chitosan hoặc hoạt chất Hexaconazole liều nhẹ."),
        
        ("crop_253", "Lúa Gạo Lứt Huyết Rồng", "Oryza sativa L.", ["Đồng Tháp", "Long An", "An Giang"],
         "Giống lúa hoang dã phục tráng hạt gạo màu đỏ thẫm huyết dụ, hàm lượng sắt cao, thân cứng chịu ngập lũ tự nhiên rất khỏe.",
         "Bệnh Cháy bìa lá lúa Huyết Rồng", "Vi khuẩn", "Xanthomonas oryzae", "Cao",
         "Mép phiến lá lúa bị khô cháy gợn sóng từ chóp lá xuống bẹ màu vàng rơm xơ xác.",
         "Phân biệt với ngộ độc phèn: Cháy bìa mép lá lượn sóng viền vàng; phèn cháy đồng loạt cả phiến lá màu nâu đỏ.",
         "Thử cắt chóp lá nhúng cốc nước trong thấy dịch đục vi khuẩn chảy ra đầu bó mạch.",
         "Phun ngừa gốc Oxolinic acid kết hợp rút nước xả phèn trong ruộng."),
        
        ("crop_254", "Lúa ST25 Sóc Trăng", "Oryza sativa L.", ["Sóc Trăng", "Bạc Liêu", "Cà Mau", "Kiên Giang"],
         "Giống lúa thơm thượng hạng Top 1 thế giới do KS Hồ Quang Cua lai tạo, thân cứng kháng đổ ngã, thích nghi tốt vùng luân canh lúa - tôm nước lợ.",
         "Bệnh Đạo ôn cổ bông lúa ST25", "Nấm", "Pyricularia oryzae", "Rất cao",
         "Cổ bông bị thâm teo nghẽn sắc nâu xám, toàn bông lúa trắng toát gãy gục ngang cổ đòng.",
         "Phân biệt với sâu đục thân: Bệnh đạo ôn cổ bông bị khô thâm nâu khớp cổ giòn; sâu đục thân có lỗ đùn phân sâu ở lóng gốc bẹ.",
         "Cầm bông lúa nhấc nhẹ thấy khớp cổ bông thâm đen gãy rụng đứt lìa.",
         "Phun phòng thuốc đặc trị Tricyclazole hoặc Fenoxanil ở thời điểm lúa trỗ 5% và sau khi trỗ xong hoàn toàn."),
        
        ("crop_255", "Lúa Nàng Thơm Chợ Đào", "Oryza sativa L.", ["Long An", "Tiền Giang"],
         "Lúa mùa đặc sản huyện Cần Đước, thổ nhưỡng vùng hạ lưu sông Vàm Cỏ Đông, hạt thon dài có chấm lựu hồng ở bụng gạo, hương thơm quyến rũ.",
         "Bệnh Vàng lùn và Lùn xoắn lá lúa", "Virus", "Rice ragged stunt virus & RGSV", "Rất cao",
         "Lá lúa ngả vàng cam từ chóp lá, rìa lá bị rách hình răng cưa xoắn vặn tít ốc, cây lùn tịt.",
         "Phân biệt với nghẹt rễ sinh lý: Răng cưa xoắn lọn lá chỉ có ở virus; nghẹt rễ lá vàng đều và rễ thối đen mềm rũ.",
         "Bóc lá cờ thấy gân lá nổi u sùi răng cưa sần sùi ngón tay.",
         "Diệt trừ rầy nâu môi giới truyền bệnh bằng Pymetrozine hoặc nấm xanh Metarhizium anisopliae."),
        
        ("crop_256", "Lúa Jasmine 85", "Oryza sativa L.", ["An Giang", "Đồng Tháp", "Cần Thơ"],
         "Giống lúa thuần thơm nhập nội thích nghi rộng tại Đồng bằng sông Cửu Long, thời gian sinh trưởng ngắn 95-100 ngày, cơm dẻo mềm.",
         "Bệnh Bạc lá vi khuẩn lúa Jasmine", "Vi khuẩn", "Xanthomonas oryzae pv. oryzae", "Cao",
         "Bìa lá bị cháy khô trắng bạc sau các đợt mưa dông lốc lớn, mép vết cháy uốn lượn sắc nét.",
         "Phân biệt với rách gió cơ học: Vết rách cơ học mép thẳng khô giòn không có viền vàng mọng nước.",
         "Soi giọt dịch vi khuẩn đục ngầu ứa ra vào ban sớm ẩm ướt.",
         "Ngừng ngay bón đạm, phun Bismerthiazol hoặc Thiodiazole copper bảo vệ tán lá."),
        
        ("crop_257", "Lúa OM 5451 Đồng Bằng Sông Cửu Long", "Oryza sativa L.", ["Hậu Giang", "Vĩnh Long", "Trà Vinh", "Kiên Giang"],
         "Giống lúa xuất khẩu chủ lực miền Tây, đẻ nhánh khỏe, năng suất cao 7-9 tấn/ha, bông chùm dày hạt tròn dài.",
         "Bệnh Đốm sọc vi khuẩn OM 5451", "Vi khuẩn", "Xanthomonas oryzae pv. oryzicola", "Cao",
         "Các sọc hẹp màu vàng cam chạy dọc giữa các gân lá, tiết ra giọt sáp keo vàng li ti.",
         "Phân biệt với nhện gié: Sọc vi khuẩn dài thẳng tắp trong suốt; nhện gié tạo vệt cạo sẫm da hổ loang lổ.",
         "Vuốt tay mặt dưới phiến lá thấy các chấm nhựa vàng dính ráp nhẹ.",
         "Phun Copper Hydroxide kết hợp Bronopol khi mật độ sọc vàng chớm xuất hiện."),
        
        ("crop_258", "Lúa OM 18", "Oryza sativa L.", ["Cần Thơ", "Sóc Trăng", "Bạc Liêu", "An Giang"],
         "Giống lúa thuần chất lượng cao, chịu phèn mặn tốt, hạt gạo trong không bạc bụng, chống chịu rầy nâu khá.",
         "Bệnh Khô vằn gốc lúa OM 18", "Nấm", "Rhizoctonia solani", "Cao",
         "Đốm vân mây da hổ loang lổ từ bẹ lá sát mặt nước lây lan nhanh lên toàn bộ bẹ lá thân lúa.",
         "Phân biệt với thối thân: Khô vằn tạo mảng hoa văn viền nâu đậm; thối thân bẹ nhũn nhão bốc mùi thối chua.",
         "Cạy các cục hạch nấm tròn màu nâu sẫm trên bẹ lá dễ dàng.",
         "Rút nước cạn phơi chân chim ruộng, phun hoạt chất Hexaconazole hoặc Validamycin A."),
        
        ("crop_259", "Lúa Đài Thơm 8", "Oryza sativa L.", ["Long An", "Tiền Giang", "Bến Tre", "Tây Ninh"],
         "Giống lúa thơm thương phẩm được gieo cấy phổ biến bậc nhất Nam Bộ, gạo trắng trong bóng, cơm dẻo mềm vị ngọt sâu.",
         "Bệnh Nhện gié hại bẹ lúa Đài Thơm", "Động vật chân đốt", "Steneotarsonemus spinki", "Cao",
         "Bẹ lá bị các vết thâm đen loang lổ hình da hổ màu bã trầu cạo nham nhở, hạt lúa bị biến dạng xoắn vặn thâm tím.",
         "Phân biệt với bệnh đốm nâu: Vết nhện gié có dạng vệt cạo màu đỏ nâu bã trầu loang dài trong lòng bẹ lá.",
         "Bóc bẹ lá soi kính lúp 20x thấy hàng trăm cá thể nhện trắng li ti di chuyển.",
         "Phun trừ nhện bằng Diafenthiuron hoặc Fenpyroximate vào giai đoạn lúa làm đòng."),
        
        ("crop_260", "Lúa Bao Thai Hồng Định Hóa", "Oryza sativa L.", ["Thái Nguyên", "Bắc Kạn", "Cao Bằng"],
         "Lúa đặc sản vùng cao Định Hóa, chịu rét chịu hạn tốt, hạt gạo tròn đậm đà làm bún phở bánh cuốn nổi tiếng.",
         "Bệnh Đạo ôn lá lúa Bao Thai", "Nấm", "Magnaporthe oryzae", "Cao",
         "Vết bệnh hình mắt én hai đầu nhọn hoắt tâm màu xám bạc viền nâu tía xuất hiện dày đặc trên lá non.",
         "Phân biệt với cháy nắng: Vết mắt én đạo ôn có cấu trúc viền sắc nét 3 lớp màu; cháy nắng khô bạc mép đều.",
         "Nhìn buổi sớm thấy lớp nấm mốc tơ xám tro mịn bám mặt dưới vết mắt én.",
         "Phun ngay Tricyclazole hoặc Kasugamycin khi vết chấm kim bắt đầu phình to hình thoi."),
        
        ("crop_261", "Ngô Nếp Tím Hạt Ngọc", "Zea mays L. ceratina", ["Sơn La", "Hà Nội", "Đồng Nai", "Bình Dương"],
         "Bắp ngô nếp màu tím thẫm chứa chất chống oxy hóa tự nhiên cao, hạt dẻo ngọt đậm, vỏ bắp xanh ôm khít cùi bắp mập mạp.",
         "Bệnh Đốm lá lớn ngô (Northern Corn Leaf Blight)", "Nấm", "Exserohilum turcicum", "Cao",
         "Vết bệnh hình thoi dài elip từ 2-10cm màu xám tro viền nâu thẫm chạy dọc theo phiến lá ngô.",
         "Phân biệt với đốm lá nhỏ (Bipolaris maydis): Đốm lá lớn hình thoi to dài kích thước lớn; đốm lá nhỏ hình chữ nhật hoặc bầu dục bé li ti.",
         "Dùng tay bẻ phiến lá vùng thoi xám thấy giòn rụm mục xơ gân lá.",
         "Phun thuốc trừ nấm Azoxystrobin + Difenoconazole hoặc Mancozeb khi thấy đốm thoi non xuất hiện dưới gốc."),
        
        ("crop_262", "Ngô Ngọt Sugar 75", "Zea mays var. saccharata", ["Lâm Đồng", "Hải Dương", "Vĩnh Phúc", "Bình Thuận"],
         "Ngô ngọt đường giống F1 cao cấp, hạt màu vàng óng hạt mọng nước độ brix cao 14-16%, thân thấp mập chống đổ tốt.",
         "Bệnh Gỉ sắt ngô ngọt (Common Rust)", "Nấm", "Puccinia sorghi", "Trung bình",
         "Hai mặt lá xuất hiện vô số các mụn mủ nhỏ li ti màu nâu đỏ gạch nổi gồ ghề.",
         "Phân biệt với đốm mắt chim: Mụn gỉ sắt nứt màng biểu bì giải phóng bột màu da cam rỉ sắt dính tay.",
         "Miết ngón tay lên mặt phiến lá có cảm giác dính bột phấn màu nâu gạch cua.",
         "Phun chế phẩm sinh học Trichoderma hoặc hoạt chất Hexaconazole, Tebuconazole phòng trừ."),
        
        ("crop_263", "Ngô Sinh Khối VN10", "Zea mays L.", ["Nghệ An", "Thanh Hóa", "Tuyên Quang", "Gia Lai"],
         "Giống ngô chuyên dùng làm thức ăn ủ chua cho bò sữa, thân cao to 2.5-3m, tán lá rậm rạp xanh bền bỉ đến tận thu hoạch.",
         "Bệnh Khô vằn thân bẹ ngô sinh khối", "Nấm", "Rhizoctonia solani", "Cao",
         "Các mảng vân mây đốm da hổ màu lục xám viền nâu đậm loang lổ từ bẹ lá sát gốc lan lên bắp ngô.",
         "Phân biệt với thối thân vi khuẩn: Khô vằn có hạch nấm nâu tròn và không chảy dịch nhầy bốc mùi hôi thối.",
         "Bóc bẹ lá gốc thấy thân cứng bình thường chỉ có màng vân mây bao phủ bẹ ngoài.",
         "Vệ sinh mật độ gieo trồng thông thoáng, phun thuốc gốc Validamycin A hoặc Difenoconazole."),
        
        ("crop_264", "Ngô Nếp MX10 Lai", "Zea mays L.", ["Đồng Nai", "Bà Rịa - Vũng Tàu", "Bình Phước"],
         "Giống ngô nếp lai F1 hạt trắng sữa dẻo mềm, khả năng thích ứng rộng, bắp to dài đầy hạt tới tận chóp bắp.",
         "Bệnh Thối thân thối bắp ngô do nấm Fusarium", "Nấm", "Fusarium verticillioides (Gibberella fujikuroi)", "Cao",
         "Hạt ngô trên bắp bị nứt nẻ và phủ lớp tơ mốc trắng hồng nhạt, ruột lõi ngô bị thối mềm mục rỗng.",
         "Phân biệt với thối bắp Diplodia: Fusarium có mốc phấn màu hồng phấn đặc trưng; Diplodia mốc màu xám trắng đen tro.",
         "Bẻ đôi bắp ngô kiểm tra lõi thấy sợi tơ nấm hồng bám kín các khe hạt ngô.",
         "Phơi khô bảo quản hạt giống đúng ẩm độ dưới 13%, phun Carbendazim hoặc Mancozeb giai đoạn trổ cờ phun râu."),
        
        ("crop_265", "Ngô Hạt Vàng Chăn Nuôi CP 511", "Zea mays L.", ["Đắk Lắk", "Gia Lai", "Bình Thuận", "Tây Ninh"],
         "Giống ngô lai năng suất cực cao 10-12 tấn/ha, bắp hạt vàng cam đậm giàu carotenoid, lõi ngô nhỏ hạt sâu cay.",
         "Bệnh Đốm xám lá ngô (Grey Leaf Spot)", "Nấm", "Cercospora zeae-maydis", "Cao",
         "Vết bệnh hình chữ nhật dài hẹp màu xám nhạt giới hạn chặt chẽ bởi hai gân phụ lá ngô.",
         "Phân biệt với đốm lá lớn: Đốm xám có cạnh vuông vức như viên gạch thẻ xám; đốm lá lớn vuốt nhọn hình thoi.",
         "Soi ngược ánh sáng thấy vết hình chữ nhật xám mờ đều tăm tắp dọc phiến lá.",
         "Phun hoạt chất Pyraclostrobin hoặc Azoxystrobin vào thời điểm trước khi ngô trổ cờ 7 ngày."),
        
        ("crop_266", "Ngô Đỏ Tủa Chùa Điện Biên", "Zea mays L.", ["Điện Biên", "Lai Châu", "Sơn La"],
         "Ngô bản địa vùng cao núi đá tai mèo, hạt màu đỏ sẫm óng ánh, dẻo bùi giàu vi chất, cây chống chịu sương muối và hạn đá vôi xuất sắc.",
         "Bệnh Sương mai ngô (Downy Mildew)", "Nấm", "Peronosclerospora sorghi", "Rất cao",
         "Lá ngô non xuất hiện các dải sọc dài màu vàng nhạt hoặc trắng bệch, mặt dưới lá phủ lớp mốc phấn trắng như bột vôi.",
         "Phân biệt với thiếu kẽm: Bệnh sương mai có lớp nấm mốc trắng tơ bên dưới lá; thiếu kẽm lá sọc trắng nhưng mặt lá nhẵn thín.",
         "Sờ mặt dưới lá thấy cảm giác mịn êm của lớp phấn mốc sương ẩm.",
         "Xử lý hạt giống bằng Metalaxyl hoặc Dimethomorph trước khi tra hạt vào hốc đá."),
        
        ("crop_267", "Khoai Tây Solara Đà Lạt", "Solanum tuberosum L.", ["Lâm Đồng", "Đức Trọng", "Đơn Dương"],
         "Giống khoai tây ruột vàng nhập nội từ Đức, củ hình bầu dục mắt nông vỏ vàng nhẵn bóng, hàm lượng chất khô cao chuyên chế biến snack.",
         "Bệnh Mốc sương khoai tây (Late Blight)", "Nấm", "Phytophthora infestans", "Rất cao",
         "Chóp mép phiến lá xuất hiện đốm nâu đen úng nước lan cực nhanh, mặt dưới mép đốm có lớp mốc trắng như sương mai.",
         "Phân biệt với đốm vòng Alternaria: Mốc sương mép loang úng nước bốc mùi ủng nồng; đốm vòng có các vòng tròn đồng tâm khô giòn.",
         "Ngửi luống khoai tây buổi sáng có mùi tanh ẩm mốc nồng nặc đặc trưng của Phytophthora.",
         "Phun phòng thuốc hoạt chất Mancozeb, Metalaxyl-M, Cymoxanil hoặc Fosetyl-Al ngay khi trời sương mù dày."),
        
        ("crop_268", "Khoai Tây Marabel Bắc Giang", "Solanum tuberosum L.", ["Bắc Giang", "Hải Dương", "Bắc Ninh", "Vĩnh Phúc"],
         "Khoai tây vụ Đông vùng đồng bằng sông Hồng, củ to da vàng cơm dẻo bùi thơm ngon, sinh trưởng nhanh 80-85 ngày.",
         "Bệnh Đốm vòng Alternaria khoai tây (Early Blight)", "Nấm", "Alternaria solani", "Cao",
         "Vết bệnh trên phiến lá hình tròn màu nâu sẫm với các đường gân nổi vân vòng tròn đồng tâm như bia bắn mục tiêu.",
         "Phân biệt với mốc sương: Đốm vòng khô cong mép lá giòn rụm không bị ủng nước thối nhũn.",
         "Lấy ngón tay bóp vụn vết đốm tròn vỡ giòn tan trong tay.",
         "Phun luân phiên thuốc gốc Iprodione, Difenoconazole hoặc Chlorothalonil khi khoai tây bắt đầu ra hoa kết củ."),
        
        ("crop_269", "Khoai Tây Hồng Atlantic Lâm Đồng", "Solanum tuberosum L.", ["Lâm Đồng", "Gia Lai"],
         "Giống khoai tây vỏ sần mắt lõm ruột trắng kem, hàm lượng đường khử thấp chống cháy khét khi chiên giòn thành khoai tây lát.",
         "Bệnh Héo xanh vi khuẩn khoai tây (Bacterial Wilt)", "Vi khuẩn", "Ralstonia solanacearum", "Rất cao",
         "Cây khoai tây đang xanh tốt bỗng rũ lá héo rục đột ngột vào buổi trưa nắng, chiều tối hồi nhẹ rồi chết hẳn.",
         "Phân biệt với héo Fusarium: Héo xanh lá vẫn giữ màu xanh tươi khi rũ; héo nấm lá úa vàng từ dưới lên trên.",
         "Cắt ngang thân củ ngâm cốc nước thấy dòng dịch trắng đục như sữa ứa ra; củ có vòng mạch thâm đen rỉ dịch.",
         "Luân canh triệt để với lúa nước, xử lý đất bằng vôi bột và chế phẩm sinh học đối kháng Bacillus subtilis."),
        
        ("crop_270", "Khoai Lang Mật Tà Nung Đà Lạt", "Ipomoea batatas (L.) Lam.", ["Lâm Đồng", "Đắk Lắk"],
         "Đặc sản khoai lang vỏ đỏ ruột vàng cam đậm, khi nướng mật tươm óng ả ngọt lịm như mật ong, chất lượng cao số một xứ sương mù.",
         "Bệnh Sùng củ khoai lang (Bọ hà bọ hà hại củ)", "Côn trùng", "Cylas formicarius", "Cao",
         "Củ khoai bị sâu non đục ngoằn ngoèo các đường hầm bên trong củ, củ biến màu xám đen vị đắng nghét bốc mùi hăng hắc.",
         "Phân biệt với thối đen củ do nấm: Sùng củ chứa đầy phân bọ hà dạng bột mịn vụn trong hang đục.",
         "Bổ củ khoai ngửi thấy mùi hôi cay đắng xốc mũi không thể ăn được.",
         "Vun luống cao lấp kín khe nứt đất không cho bọ hà đẻ trứng; rải thuốc sinh học nấm ký sinh Beauveria bassiana."),
        
        ("crop_271", "Khoai Lang Tím Nhật Bình Tân", "Ipomoea batatas (L.) Lam.", ["Vĩnh Long", "Đồng Tháp", "Hậu Giang"],
         "Thủ phủ khoai lang Bình Tân Vĩnh Long, củ thon dài ruột tím thẫm mộng nước, giàu anthocyanin, mặt hàng nông sản xuất khẩu giá trị cao.",
         "Bệnh Thối đen củ Ceratocystis khoai lang", "Nấm", "Ceratocystis fimbriata", "Cao",
         "Trên bề mặt củ xuất hiện các đốm tròn lõm màu nâu xám sẫm, thịt củ bên trong chuyển màu đen đắng ngắt bốc mùi dầu hỏa thoang thoảng.",
         "Phân biệt với ghẻ củ: Thối đen ăn sâu vào lõi thịt củ và bốc mùi hương dầu nồng; ghẻ củ chỉ sần sùi lớp da ngoài.",
         "Cắt ngang củ thấy ranh giới đen mun rõ rệt ăn sâu vào tâm củ.",
         "Xử lý hom giống sạch bệnh bằng nước nóng 50 độ C trong 10 phút, phun phòng nấm Chaetomium."),
        
        ("crop_272", "Khoai Lang Kén Lộc Bình Lạng Sơn", "Ipomoea batatas (L.) Lam.", ["Lạng Sơn", "Cao Bằng", "Quảng Ninh"],
         "Khoai lang đồi dốc củ tròn bầu dục như kén tằm, ruột vàng ruộm dẻo ngọt bùi, thích ứng thổ nhưỡng đất đồi khô cằn vùng biên giới.",
         "Bệnh Ghẻ củ sẹo da khoai lang (Scab)", "Nấm", "Elsinoe batatas (Sphaceloma batatas)", "Trung bình",
         "Gân lá và cuống đọt khoai bị cong queo vặn xoắn, xuất hiện các vết sẹo sần nổi ghẻ màu nâu xám ráp tay.",
         "Phân biệt với chích hút bọ trĩ: Bệnh ghẻ làm cuống thân chai cứng gồ ghề vảy sẹo; bọ trĩ làm quăn mép lá nhưng thân nhẵn bóng.",
         "Dùng móng tay cào nhẹ vảy ghẻ thấy lớp sừng ráp cứng bong vảy nhỏ.",
         "Phun thuốc gốc Đồng Oxyclorua hoặc Difenoconazole định kỳ giai đoạn đâm chồi vươn ngọn."),
        
        ("crop_273", "Khoai Sọ Thuận Châu Sơn La", "Colocasia esculenta (L.) Schott", ["Sơn La", "Hòa Bình", "Điện Biên"],
         "Khoai sọ nương đồi nổi tiếng Thuận Châu dẻo quánh thơm bùi đặc trưng, củ cái củ con mập mạp bở tơi khi nấu canh sườn.",
         "Bệnh Cháy lá sương mai khoai sọ (Taro Leaf Blight)", "Nấm", "Phytophthora colocasiae", "Rất cao",
         "Phiến lá to xuất hiện các đốm tròn úng nước màu nâu vàng tiết ra giọt dịch vàng cam, vết bệnh loang rộng làm thủng rách nát toàn bộ lá.",
         "Phân biệt with đốm mắt chim: Sương mai khoai sọ làm lá rách thủng lỗ chỗ úng nước viền vàng rộng rũ rượi.",
         "Nhìn vết thối có các giọt keo màu cam rỉ quanh rìa vết sũng nước.",
         "Phun luân phiên Fosetyl-Al, Metalaxyl hoặc dịch chiết nấm đối kháng Trichoderma."),
        
        ("crop_274", "Khoai Môn Lệ Phố Hà Nội", "Colocasia esculenta var. antiquorum", ["Hà Nội", "Hưng Yên", "Phú Thọ"],
         "Khoai môn nức tiếng củ to tròn ruột điểm tia tím vân cẩm thạch, bở tơi xốp ngậy làm nhân bánh trung thu và món chiên lẩu truyền thống.",
         "Bệnh Thối mềm thối nhũn củ khoai môn", "Vi khuẩn", "Pectobacterium carotovorum (Erwinia carotovora)", "Cao",
         "Gốc thân bẹ lá bị nhũn nước thâm nâu đổ rạp xuống mặt đất, củ dưới lòng đất bị thối rữa thành khối bột nhầy bốc mùi khắm thối nồng nặc.",
         "Phân biệt với héo rũ nấm: Thối vi khuẩn mô bị nhũn nhớt chảy nước thối khắm đặc trưng; nấm thối khô xơ không mùi nhầy báng.",
         "Bóp nhẹ củ khoai môn bệnh thấy xẹp lún ngón tay ứa ra dịch nhớt màu trắng đục tanh nồng.",
         "Lên luống cao thoát nước triệt để, rải vôi bột khử khuẩn và tưới gốc Kasugamycin."),
        
        ("crop_275", "Khoai Mì Cao Sản KM94", "Manihot esculenta Crantz", ["Tây Ninh", "Bình Phước", "Đồng Nai", "Gia Lai"],
         "Giống sắn công nghiệp hàm lượng tinh bột cực cao 28-30%, năng suất củ tươi đạt 35-45 tấn/ha, cung cấp nguyên liệu chế biến cồn ethanol và bột ngọt.",
         "Bệnh Khảm lá sắn (Cassava Mosaic Disease)", "Virus", "Sri Lankan cassava mosaic virus (SLCMV)", "Rất cao",
         "Phiến lá sắn bị biến dạng méo mó quăn queo, xuất hiện các mảng loang lổ xen kẽ màu xanh đậm và vàng nhạt, cây còi cọc không tạo củ.",
         "Phân biệt với bọ phấn trắng chích hút: Khảm lá virus làm phiến lá nhăn nhúm dị dạng nghiêm trọng ngay từ đọt non mới bung.",
         "Quan sát toàn bộ chồi ngọn non thấy lá xoăn tít mất tính đối xứng hoàn toàn.",
         "Tuyệt đối không dùng hom sắn ở vùng nhiễm bệnh; phun trừ bọ phấn trắng Bemisia tabaci bằng Dinotefuran; tiêu hủy ruộng bệnh theo quy trình kiểm dịch thực vật."),
        
        ("crop_276", "Khoai Mì KM140 Tây Ninh", "Manihot esculenta Crantz", ["Tây Ninh", "Bình Dương", "Bà Rịa - Vũng Tàu"],
         "Giống mì thân thẳng ít phân cành dễ thu hoạch, chịu hạn tốt, năng suất củ vượt trội trên đất xám bạc màu Đông Nam Bộ.",
         "Bệnh Chổi rồng hại sắn (Witches' Broom)", "Phytoplasma", "Candidatus Phytoplasma", "Cao",
         "Ngọn sắn bị ức chế phát triển lóng ngắn lại, các chồi nách đâm tược li ti dày đặc mọc tua tủa như cây chổi rơm quét nhà.",
         "Phân biệt với nhện đỏ gây hại: Chổi rồng làm đâm hàng chục nhánh còi li ti ở ngọn; nhện đỏ chỉ làm lá bạc vàng rụng lá.",
         "Nhìn ngọn sắn biến thành búi chồi rậm rạp lá teo nhỏ bằng móng tay.",
         "Phun trừ rầy môi giới truyền bệnh; nhổ bỏ gom đốt tiêu hủy tận gốc bụi sắn bị bệnh chổi rồng."),
        
        ("crop_277", "Sắn Dây Kinh Môn Hải Dương", "Pueraria thomsonii Benth.", ["Hải Dương", "Quảng Ninh", "Hải Phòng"],
         "Vựa sắn dây nổi tiếng đất Kinh Môn, củ dài nạc bột trắng mịn như tuyết, giải nhiệt thanh lọc cơ thể thượng hạng.",
         "Bệnh Đốm lá nâu sắn dây", "Nấm", "Cercospora pueraricola", "Trung bình",
         "Mặt lá xuất hiện các đốm tròn góc cạnh màu nâu đen viền vàng nhạt, rải rác khắp tán lá bánh tẻ.",
         "Phân biệt với cháy nắng: Đốm Cercospora có tâm hoại tử xám và các chấm đen nhỏ sinh bào tử.",
         "Sờ mặt lá thấy giòn khô ở tâm đốm bệnh.",
         "Dọn sạch tàn dư lá rụng sau thu hoạch, phun phòng chế phẩm gốc Đồng hoặc Booc-đô 1%."),
        
        ("crop_278", "Dong Riềng Đỏ Na Rì Bắc Kạn", "Canna edulis Ker Gawl.", ["Bắc Kạn", "Cao Bằng", "Điện Biên"],
         "Cây dong riềng củ đỏ tím làm miến dong trứ danh Na Rì miến dai giòn nấu không bị nát, cây sinh trưởng khỏe trên sườn đồi núi cao.",
         "Bệnh Thối thân củ nấm Fusarium dong riềng", "Nấm", "Fusarium oxysporum f. sp. cannae", "Cao",
         "Gốc cây dong riềng bị thâm nâu teo tóp, lá úa vàng từ dưới gốc lên ngọn rũ xuống, củ dưới đất bị thối khô xốp ruột có bột tím nhạt.",
         "Phân biệt với sâu đục củ: Bệnh nấm củ bị teo xốp khô có bột nấm; sâu đục có lỗ đùn phân mùn cưa ướt.",
         "Nhổ bụi dong riềng lên thấy củ nhẹ bẫng xốp khô, bẻ đôi thấy mạch dẫn bên trong thâm đen.",
         "Luân canh với ngô hoặc đậu đỗ, xử lý củ giống bằng Ridomil Gold trước khi vùi đất."),
        
        ("crop_279", "Khoai Từ Nếp Phú Yên", "Dioscorea esculenta (Lour.) Burkill", ["Phú Yên", "Bình Định", "Khánh Hòa"],
         "Khoai từ củ chùm sai trĩu ruột trắng dẻo nhớt ngọt, luộc chấm muối mè hoặc nấu chè thanh mát giải nhiệt mùa hè duyên hải miền Trung.",
         "Bệnh Thán thư cháy dây khoai từ (Anthracnose)", "Nấm", "Colletotrichum gloeosporioides", "Cao",
         "Dây leo và cuống lá xuất hiện các đốm thâm đen lõm sâu hình bầu dục, dây khoai bị thắt nghẽn khô đen từ ngọn lụi dần xuống gốc.",
         "Phân biệt với sương mai: Thán thư tạo vết lõm sâu màu đen bóng giòn gãy cành dây leo.",
         "Sờ cọng dây khoai từ bị bệnh thấy tóp teo khô giòn gãy gập dễ dàng.",
         "Làm giàn leo thông thoáng, phun ngừa Mancozeb hoặc Antracol khi thời tiết mưa dầm ẩm ướt."),
        
        ("crop_280", "Khoai Mỡ Tím Long An", "Dioscorea alata L.", ["Long An", "Đồng Tháp", "Tiền Giang"],
         "Khoai mỡ củ to nặng 3-5kg ruột màu tím hoa cà rực rỡ, độ nhớt cao dẻo quánh nấu canh tôm thịt béo ngậy trứ danh miền Tây.",
         "Bệnh Đốm lá cháy ngọn khoai mỡ", "Nấm", "Colletotrichum alatae", "Cao",
         "Các đốm cháy màu nâu đen lan rộng dọc theo gân lá hình trái tim, chóp ngọn dây khoai bị thối rụi đen thui.",
         "Phân biệt với rệp sáp hại ngọn: Bệnh nấm vết cháy khô giòn không có chất nhầy sáp trắng của rệp.",
         "Dùng tay bóp chồi ngọn đen thấy khô giòn vụn rơi bột đen.",
         "Phun phòng sớm hoạt chất Difenoconazole + Azoxystrobin ở giai đoạn dây khoai bắt đầu leo giàn."),
        
        ("crop_281", "Củ Cọc Rào Cần Giờ", "Dioscorea cirrhosa Lour.", ["TP. Hồ Chí Minh", "Bà Rịa - Vũng Tàu", "Đồng Nai"],
         "Củ nâu cọc rào ven rừng ngập mặn Cần Giờ, ruột chứa hàm lượng tanin cực lớn dùng nhuộm lưới đánh cá và vải lụa tơ tằm bền chắc chống mục.",
         "Bệnh Thối rễ thối củ nâu ngập úng", "Nấm", "Phytophthora spp.", "Cao",
         "Củ nâu trong đất bị mềm nhũn chảy nước chua nhớt, vỏ củ màu nâu thẫm bong tróc từng mảng làm dây héo rũ hoàn toàn.",
         "Phân biệt với tổn thương do ngập mặn: Nấm Phytophthora củ bị nhũn ủng bốc mùi chua; ngập mặn lá rụng khô nhưng củ vẫn rắn.",
         "Dùng ngón tay ấn vào củ nâu thấy vỏ lún sâu ứa nước dịch màu đỏ nâu chua chát.",
         "Đào mương thoát úng triệt để sau triều cường, tưới gốc chế phẩm nấm đối kháng Trichoderma."),
        
        ("crop_282", "Củ Nưa Nâu Ba Vì", "Amorphophallus konjac K. Koch", ["Hà Nội", "Hòa Bình", "Phú Thọ"],
         "Cây nưa nương củ tròn to ruột chứa tinh chất glucomannan đặc biệt, tạo thạch konjac ăn kiêng giảm béo nổi tiếng thế giới.",
         "Bệnh Thối nhũn gốc thân vi khuẩn củ nưa", "Vi khuẩn", "Pectobacterium carotovorum", "Rất cao",
         "Phần thân giả mọng nước sát mặt đất bị thâm ủng nhầy nhụa, cây ngã gục gãy ngang gốc bốc mùi hôi thối nồng nặc.",
         "Phân biệt với thối nấm Sclerotium: Vi khuẩn làm thối nhũn chảy nước tanh khắm và không có sợi nấm trắng hạt cải.",
         "Ngửi vết thối gốc thân thấy mùi khắm đặc trưng của vi khuẩn phân hủy protein.",
         "Xử lý đất trồng bằng vôi bột, tưới gốc dung dịch Kasugamycin hoặc Starner 20WP."),
        
        ("crop_283", "Đậu Xanh Hạt Mỡ Đắk Lắk", "Vigna radiata (L.) R. Wilczek", ["Đắk Lắk", "Gia Lai", "Đồng Nai"],
         "Đậu xanh hạt bóng tròn căng mẩy mỡ màng lòng xanh vàng ươm, chịu hạn rất khỏe trên đất đỏ bazan, làm giá đỗ và bột ngũ cốc dinh dưỡng.",
         "Bệnh Đốm lá Cercospora đậu xanh", "Nấm", "Cercospora canescens", "Cao",
         "Vết bệnh trên lá hình tròn hoặc góc cạnh tâm xám nhạt viền đỏ tía nổi bật, làm rụng lá hàng loạt khi cây đang nuôi trái.",
         "Phân biệt với cháy lá vi khuẩn: Cercospora có viền đỏ tía sắc nét không có quầng mọng nước thấu quang.",
         "Mặt dưới đốm bệnh vào buổi sớm ẩm ướt có lớp mốc tơ màu xám chì.",
         "Phun luân phiên Chlorothalonil hoặc Carbendazim khi cây bắt đầu phân cành đẻ nhánh rộ."),
        
        ("crop_284", "Đậu Đen Xanh Lòng Vĩnh Lộc", "Vigna cylindrica (L.) Skeels", ["Thanh Hóa", "Nghệ An", "Hà Tĩnh"],
         "Giống đậu đen bản địa vỏ đen nhánh lòng xanh ngọc bích, nấu chè ninh cháo thơm ngậy bùi dẻo, vị thuốc bổ thận thanh nhiệt cổ truyền.",
         "Bệnh Gỉ sắt đậu đen", "Nấm", "Uromyces appendiculatus", "Cao",
         "Hai mặt lá xuất hiện hàng ngàn mụn mủ nhỏ li ti màu nâu đỏ rỉ sắt làm lá vàng khô cằn rụng sớm.",
         "Phân biệt với phấn trắng: Gỉ sắt có mụn nổi chứa bột màu nâu đỏ cam; phấn trắng phủ mảng phấn trắng mịn như bụi phấn.",
         "Vuốt nhẹ mặt dưới phiến lá thấy bột màu gỉ sét bám chặt vào đầu ngón tay.",
         "Phun chế phẩm nano đồng hoặc hoạt chất Tebuconazole, Hexaconazole khi chớm thấy chấm mụn gỉ."),
        
        ("crop_285", "Đậu Đỏ Tây Bắc", "Vigna angularis (Willd.) Ohwi & H. Ohashi", ["Sơn La", "Lào Cai", "Lai Châu"],
         "Hạt đậu đỏ au bóng đẹp trồng trên nương cao khí hậu mát mẻ, giàu protein và sắt, chuyên dùng nấu chè xôi và làm bánh dinh dưỡng cao cấp.",
         "Bệnh Héo vàng Fusarium đậu đỏ", "Nấm", "Fusarium oxysporum f. sp. phaseoli", "Cao",
         "Lá bên dưới úa vàng rụng dần, cây còi cọc chột hoa, chẻ gốc thân thấy bó mạch dẫn hóa nâu đen thẫm.",
         "Phân biệt với héo xanh vi khuẩn: Fusarium gây vàng lá rụng từ từ từng cành; héo xanh cây héo rũ bất ngờ khi lá còn xanh mướt.",
         "Rạch dọc vỏ thân gốc quan sát thấy hai vệt mạch gỗ màu nâu sẫm chạy dọc thân lên cành.",
         "Luân canh với cây trồng nước, bón lót phân chuồng hoai mục ủ nấm đối kháng Trichoderma."),
        
        ("crop_286", "Đậu Nành DT84 Hà Nam", "Glycine max (L.) Merr.", ["Hà Nam", "Nam Định", "Hải Dương", "Hà Nội"],
         "Giống đậu tương thuần chọn lọc năng suất cao, hạt to mẩy vàng sáng hàm lượng đạm và dầu thực vật cao, chống đổ ngã tốt vụ Đông xuân.",
         "Bệnh Gỉ sắt đậu tương (Soybean Rust)", "Nấm", "Phakopsora pachyrhizi", "Rất cao",
         "Mặt dưới lá xuất hiện các u mụn li ti màu nâu nhạt sau chuyển màu nâu gỉ sắt, lá biến vàng rụng trơ cành cây không đậu hạt.",
         "Phân biệt với đốm mắt ếch (Frogeye leaf spot): Gỉ sắt tạo mụn mủ nứt bung bột nâu đỏ; đốm mắt ếch vết tròn phẳng tâm xám trắng viền nâu đỏ phẳng lì.",
         "Soi kính lúp thấy các nón mụn mủ hình núi lửa nhỏ nhô lên khỏi biểu bì mặt dưới lá.",
         "Phun phòng thuốc hoạt chất Azoxystrobin + Difenoconazole hoặc Pyraclostrobin ngay khi chớm có dấu hiệu bệnh."),
        
        ("crop_287", "Đậu Nành Rau Edamame Sóc Trăng", "Glycine max (L.) Merr.", ["Sóc Trăng", "An Giang", "Đồng Tháp"],
         "Đậu nành non thu hái nguyên quả xanh xuất khẩu sang Nhật Bản, hạt ngọt đậm béo ngậy nhiều dinh dưỡng, tiêu chuẩn VietGAP nghiêm ngặt.",
         "Bệnh Đốm mắt ếch hại đậu nành rau", "Nấm", "Cercospora sojina", "Cao",
         "Vết bệnh trên lá hình tròn tâm màu xám trắng viền nâu đỏ đậm viền rõ như mắt con ếch, quả non bị đốm thâm lép hạt.",
         "Phân biệt với gỉ sắt: Vết đốm phẳng nhẵn không nổi u mụn và không làm dính bột phấn gỉ sét.",
         "Bề mặt vết bệnh khô giòn đục lỗ thủng nhỏ trên phiến lá già.",
         "Phun thuốc sinh học Chaetomium hoặc thuốc hoạt chất Thiophanate-methyl, Chlorothalonil tuân thủ thời gian cách ly nghiêm ngặt."),
        
        ("crop_288", "Đậu Phộng Sen Lai L14 Nghệ An", "Arachis hypogaea L.", ["Nghệ An", "Hà Tĩnh", "Thanh Hóa"],
         "Giống lạc lai năng suất cao thích nghi đất cát pha duyên hải miền Trung, củ 2 hạt đều đặn vỏ mỏng eo nhỏ, tỷ lệ dầu cao trên 50%.",
         "Bệnh Đốm nâu và Đốm đen lá lạc (Cercospora leaf spots)", "Nấm", "Cercospora arachidicola & Phaeoisariopsis personata", "Cao",
         "Mặt trên lá xuất hiện vô số đốm tròn màu nâu có quầng vàng sáng quanh viền (đốm nâu sớm) hoặc đốm đen tròn xoe viền hẹp rụng lá sớm.",
         "Phân biệt với gỉ sắt lạc: Đốm Cercospora phẳng không có ổ mụn mủ gồ ghề chứa bột phấn nâu đỏ.",
         "Lật mặt dưới lá thấy các đốm đen tuyền hơi gồ mốc nhẹ, cây rụng lá trơ cành chỉ còn củ còi.",
         "Phun luân phiên Tebuconazole hoặc Hexaconazole vào giai đoạn sau gieo 45 và 60 ngày."),
        
        ("crop_289", "Đậu Phộng Chợ Lách Bến Tre", "Arachis hypogaea L.", ["Bến Tre", "Trà Vinh", "Tiền Giang"],
         "Lạc giồng cát ven sông Tiền vỏ sáng trắng hạt mẩy hồng ngọt bùi, dùng nấu luộc tươi ăn béo ngậy được ưa chuộng khắp miền Tây.",
         "Bệnh Héo xanh vi khuẩn hại lạc", "Vi khuẩn", "Ralstonia solanacearum", "Rất cao",
         "Toàn bộ cây lạc đang xanh tốt rũ rượi cành lá chỉ sau một đêm nắng gắt sau mưa, rễ và tia củ bị thối đen ứa dịch trắng.",
         "Phân biệt với thối gốc mốc trắng (Sclerotium rolfsii): Vi khuẩn không có sợi tơ trắng quấn quanh gốc và hạch nấm hạt cải nâu.",
         "Cắt đoạn rễ cọc nhúng ly nước thấy sợi khói dịch vi khuẩn màu trắng ngà tuôn ra từ bó mạch.",
         "Xử lý vôi bột 30kg/công đất giồng cát; luân canh với lúa nước hoặc bắp; tưới sinh học Bacillus subtilis."),
        
        ("crop_290", "Đậu Ngự Huế", "Phaseolus lunatus L.", ["Thừa Thiên Huế", "Quảng Trị", "Quảng Nam"],
         "Đậu ngự tiến vua hạt to dẹt màu trắng ngà hoặc vân đỏ tía, nấu chè đậu ngự cung đình bùi béo tan ngay đầu lưỡi, dây leo giàn sum suê.",
         "Bệnh Thán thư đốm quả đậu ngự", "Nấm", "Colletotrichum lindemuthianum", "Cao",
         "Vỏ quả non xuất hiện các đốm tròn lõm màu nâu sẫm viền đỏ gạch, tâm đốm ứa dịch màu hồng phấn nhầy làm quả bị lép dị dạng cong queo.",
         "Phân biệt với vết chích bọ xít: Thán thư có vết lõm sâu dạng lòng chảo và tiết dịch nấm hồng khi trời ẩm.",
         "Sờ mặt vỏ quả thấy lõm hõm sâu xuống tận hạt non bên trong.",
         "Phun chế phẩm Copper Oxychloride hoặc Difenoconazole khi cây đậu ngự vừa đậu quả non."),
        
        ("crop_291", "Đậu Hà Lan Lâm Đồng", "Pisum sativum L.", ["Lâm Đồng", "Đà Lạt", "Lạc Dương"],
         "Đậu Hà Lan quả ngọt giòn và hạt non bổ dưỡng xứ lạnh cao nguyên, vỏ quả xanh ngọc óng ả giàu đường tự nhiên và vitamin C.",
         "Bệnh Phấn trắng đậu Hà Lan (Powdery Mildew)", "Nấm", "Erysiphe pisi", "Rất cao",
         "Toàn bộ phiến lá thân cành và vỏ quả bị bao phủ một lớp bột màu trắng xóa mịn như rắc bột mì, lá khô vàng rụng sớm.",
         "Phân biệt với sương mai: Phấn trắng tạo lớp bột khô trắng xóa ở cả mặt trên và mặt dưới lá; sương mai mốc xám chỉ ở mặt dưới lá úng nước.",
         "Lấy tay xoa lên mặt lá lớp bột trắng mịn dính đầy ngón tay làm lộ ra biểu bì lá bị úa vàng bên dưới.",
         "Phun phòng thuốc sinh học Nano Lưu huỳnh hữu cơ hoặc hoạt chất Azoxystrobin, Triflumizole an toàn VietGAP."),
        
        ("crop_292", "Đậu Ván Trắng Ba Vì", "Lablab purpureus (L.) Sweet", ["Hà Nội", "Vĩnh Phúc", "Bắc Giang"],
         "Cây họ đậu leo giàn hoa trắng quả dẹp hạt trắng sữa dùng làm vị thuốc bạch biển đậu trị tỳ hư tiêu chảy thanh nhiệt giải độc.",
         "Bệnh Cháy lá lở cổ rễ đậu ván", "Nấm", "Rhizoctonia solani", "Cao",
         "Cổ rễ sát mặt đất bị thâm ủng vỏ teo thắt nghẽn, dây leo bị héo khô từ gốc, mặt lá có mảng cháy loang lổ vân mây xám.",
         "Phân biệt với héo Fusarium: Rhizoctonia làm lở loét khuyết sâu vỏ cổ rễ sát mặt đất có tơ nấm nâu xám giăng tơ.",
         "Kéo nhẹ gốc cây đậu ván thấy đứt ngang cổ rễ bị ủng thối xơ xác.",
         "Tưới gốc Trichoderma ủ phân hoai mục, phun Validamycin A vào phần gốc thân sát đất."),
        
        ("crop_293", "Đậu Cút Sọc Đà Lạt", "Phaseolus vulgaris L.", ["Lâm Đồng", "Đức Trọng", "Đơn Dương"],
         "Đậu quả sọc rằn ri hạt to cùi dày bùi ngọt, món rau củ hầm xương yêu thích trong các nhà hàng xứ lạnh Đà Lạt.",
         "Bệnh Đốm góc cạnh vi khuẩn đậu cove cút", "Vi khuẩn", "Pseudomonas syringae pv. phaseolicola", "Cao",
         "Trên lá xuất hiện các đốm màu úng nước nhỏ bị gân lá chặn lại tạo hình đa giác góc cạnh, có quầng màu vàng chanh sáng bao quanh.",
         "Phân biệt với đốm nấm Cercospora: Đốm vi khuẩn có hình đa giác góc cạnh thấu quang và quầng vàng chanh nổi bật.",
         "Đưa mặt lá soi ngược nắng nhìn rõ các góc cạnh đa giác úng nước sáng rực.",
         "Phun ngừa bằng hoạt chất Kasugamycin hoặc Bismerthiazol sau những đợt mưa rào ẩm ướt."),
        
        ("crop_294", "Đậu Cô Ve Lùn Tiền Giang", "Phaseolus vulgaris L.", ["Tiền Giang", "Bến Tre", "Vĩnh Long"],
         "Giống đậu cove thân bụi lùn không cần làm giàn leo, quả dài suôn đuột xanh bóng giòn ngọt thu hoạch sớm sau 45 ngày.",
         "Bệnh Gỉ sắt hại đậu cove lùn", "Nấm", "Uromyces appendiculatus", "Trung bình",
         "Mặt dưới lá phủ đầy các nốt mụn mủ màu vàng nâu cam sau đổi nâu đen, lá vàng rụng sớm giảm hẳn lứa quả thu hoạch.",
         "Phân biệt với nhện đỏ: Nhện đỏ cắn mặt trên lá làm lá bạc trắng lấm tấm bụi cát; gỉ sắt mụn mủ mặt dưới chứa đầy bột phấn gỉ sét.",
         "Vuốt mặt dưới lá thấy nhám ráp bột nâu cam dính ngón tay rõ nét.",
         "Phun dung dịch sinh học tỏi ớt gừng hoặc hoạt chất Hexaconazole, Mancozeb theo đúng liều lượng."),
        
        ("crop_295", "Mè Đen Vĩnh Hưng Long An", "Sesamum indicum L.", ["Long An", "Đồng Tháp", "An Giang"],
         "Mè đen phù sa vùng lũ Đồng Tháp Mười, hạt đen tuyền căng mẩy ép dầu mè thơm lừng, bổ huyết dưỡng âm nhuận tràng quý giá.",
         "Bệnh Héo rũ gốc thân vừng mè đen", "Nấm", "Macrophomina phaseolina (Rhizoctonia bataticola)", "Cao",
         "Thân cây mè bị chuyển sang màu xám tro đen từ gốc lên ngọn, bên trong thân rỗng chứa vô số các hạch nấm li ti đen như hạt than.",
         "Phân biệt với héo Fusarium: Macrophomina tạo vô số hạt đen li ti như bụi than bám đầy trong ruột xơ thân rỗng.",
         "Bẻ đôi đoạn thân cây mè khô thấy ruột rỗng đen kịt hạt hạch nấm li ti.",
         "Không trồng mè liên tục trên đất cũ, luân canh với lúa nước, xử lý hạt giống bằng Thiram trước khi gieo sạ."),
        
        ("crop_296", "Mè Vàng Bình Thuận", "Sesamum indicum L.", ["Bình Thuận", "Ninh Thuận", "Khánh Hòa"],
         "Mè vàng hạt óng ả thơm bùi canh tác trên vùng đất cát ven biển nắng gió miền Trung, chịu hạn phi thường, vỏ mỏng ruột nhiều dầu béo.",
         "Bệnh Khảm vàng xoăn lá vừng mè", "Virus", "Sesame leaf curl virus", "Cao",
         "Phiến lá mè bị co rút quăn queo xoăn tít lại, các gân lá dày lên và lá biến màu vàng chanh lốm đốm, cây còi lùn không nở hoa.",
         "Phân biệt với bọ trĩ chích: Virus làm phiến lá biến dạng dày cộm sần sùi giòn tan.",
         "Sờ phiến lá bị bệnh thấy dày cộm giòn vụn mép lá gập gãy cụp xuống dưới.",
         "Phun trừ bọ phấn trắng Bemisia tabaci môi giới truyền bệnh bằng Pymetrozine hoặc nấm xanh."),
        
        ("crop_297", "Bo Bo Ý Dĩ Hà Giang", "Coix lacryma-jobi L.", ["Hà Giang", "Cao Bằng", "Tuyên Quang"],
         "Hạt ý dĩ trắng đục hình trứng tròn nhẵn làm thuốc kiện tỳ trừ thấp bổ phổi và nấu chè sâm bổ lượng mát bổ nổi tiếng xứ đá.",
         "Bệnh Than đen hạt ý dĩ (Smut)", "Nấm", "Ustilago coicis", "Cao",
         "Buồng hạt ý dĩ bị nấm xâm nhiễm phồng to bất thường thành khối bọc màu xám chì, bên trong chứa đầy bột than màu đen kịt mịn màng.",
         "Phân biệt với hạt lép: Hạt bị bệnh phồng to gấp 2-3 lần hạt bình thường bên trong nứt bung bột đen muội hôi.",
         "Bóp nhẹ hạt ý dĩ phồng xẹp vỡ tung bột than đen bám đen các đầu ngón tay.",
         "Xử lý hạt giống bằng nước nóng 54 độ C trong 15 phút trước khi tra hạt; ngắt bỏ buồng hạt than tiêu hủy."),
        
        ("crop_298", "Hạt Kê Vàng Quảng Nam", "Setaria italica (L.) P. Beauv.", ["Quảng Nam", "Quảng Ngãi", "Bình Định"],
         "Cây kê bông dài uốn cong hạt kê vàng ươm nấu bánh đa kê giòn rụm hoặc nấu cháo giải nhiệt mùa hè miền Trung nắng rát.",
         "Bệnh Đốm lá sọc nâu cây kê", "Nấm", "Bipolaris setariae", "Trung bình",
         "Phiến lá xuất hiện các vệt đốm dài hình bầu dục màu nâu đỏ chạy dọc phiến lá làm lá lụi tàn sớm.",
         "Phân biệt với thiếu lân: Thiếu lân lá có màu tím đỏ đều từ chóp; đốm nấm có bờ viền sắc nhọn hình thoi dài.",
         "Sờ mặt phiến lá thấy ráp ráp khô giòn ở vết thâm nâu.",
         "Phun phòng thuốc gốc Difenoconazole hoặc Mancozeb khi kê bắt đầu vươn đọt trổ bông."),
        
        ("crop_299", "Kiều Mạch Tam Giác Mạch Hà Giang", "Fagopyrum esculentum Moench", ["Hà Giang", "Lào Cai", "Cao Bằng"],
         "Hoa tam giác mạch hồng tím bạt ngàn cao nguyên đá Đồng Văn, hạt tam giác nâu đen xay bột làm bánh tam giác mạch bùi dẻo và ủ rượu quý.",
         "Bệnh Lở cổ rễ thối thân cây tam giác mạch", "Nấm", "Rhizoctonia solani / Pythium spp.", "Cao",
         "Thân cây non mọng nước sát mặt đất bị thắt teo màu nâu úng nước, cây đổ rạp hàng loạt trên nương đá khi gặp sương mù ẩm ướt.",
         "Phân biệt with gãy do gió: Đoạn gốc bị teo tóp ủng nhũn nước mất khả năng nâng đỡ thân cây.",
         "Nhấc nhẹ cây kiều mạch đứt ngang cổ rễ ủng nhớt không còn rễ tơ.",
         "Rải tro bếp và vôi bột giữ ấm gốc, phun chế phẩm sinh học Trichoderma định kỳ khi cây còn non 2-3 lá thật."),
        
        ("crop_300", "Lúa Miến Cao Lương Gia Lai", "Sorghum bicolor (L.) Moench", ["Gia Lai", "Kon Tum", "Đắk Lắk"],
         "Cây cao lương thân to như cây mía trổ bông chùm hạt đỏ nâu dẻo bùi, chịu hạn phi thường làm lương thực dự trữ và chăn nuôi đại gia súc Tây Nguyên.",
         "Bệnh Đốm lá thán thư cao lương (Anthracnose)", "Nấm", "Colletotrichum sublineolum", "Cao",
         "Trên phiến lá xuất hiện vô số đốm hình bầu dục dài màu đỏ tím hoặc đỏ gạch tâm xám nhạt, bên trong tâm có các chấm đen nhỏ li ti là đĩa cành nấm.",
         "Phân biệt với gỉ sắt: Thán thư tạo đốm loang lớn màu đỏ tím tâm bạc có lông cứng đen; gỉ sắt tạo u mụn nổi da cam.",
         "Soi kính lúp thấy các gai lông đen nhỏ li ti mọc tua tủa giữa tâm đốm hoại tử xám bạc.",
         "Phun luân phiên Azoxystrobin hoặc Mancozeb khi cây cao lương cao 1 mét trước khi trỗ buồng hạt.")
    ]
    
    for item in additional_crops_data:
        cid, name, sci, locs, eco, dname, ag_type, ag_sci, danger, symp, diff, test, vietgap = item
        crop_obj = {
            "id": cid,
            "topic": "Cay_Luong_Thuc_Va_Hoa_Mau",
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
                        f"Mô bệnh trên cây {name} lan nhanh khi độ ẩm không khí vượt trên 80% kèm gió dầm.",
                        "Tán cây bị suy kiệt, quá trình quang hợp đình trệ khiến chất lượng nông sản sụt giảm rõ rệt."
                    ],
                    "phan_biet_chan_doan_kep": diff,
                    "kiem_tra_thuc_dia": test,
                    "phac_do_vietgap": {
                        "canh_tac": "Vệ sinh đồng ruộng triệt để, thu gom tàn dư thực vật đem ủ hoai mục bằng chế phẩm vi sinh, bón cân đối NPK.",
                        "sinh_hoc": "Sử dụng các dòng nấm đối kháng Trichoderma, Chaetomium hoặc dịch chiết thực vật thảo mộc phòng ngừa.",
                        "khuyen_cao_chuyen_gia": vietgap
                    }
                },
                {
                    "ten_benh": f"Bệnh Thối cổ rễ và héo rũ cây non {name}",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Fusarium oxysporum / Rhizoctonia solani"
                    },
                    "trieu_chung_dien_hinh": [
                        "Phần cổ rễ tiếp giáp mặt đất bị thâm đen, teo tóp thắt nghẽn làm gián đoạn dòng vận chuyển nước",
                        "Lá non bị héo rũ từ đọt xuống, cây con ngã rạp hoặc chết đứng khi gặp nắng gắt buổi trưa",
                        "Bộ rễ tơ bị thối đen xơ xác, không còn khả năng đâm chồi rễ mới"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với tổn thương do dế chũi cắn đứt rễ: Nấm làm mô rễ thâm đen nhũn xơ xác; dế cắn vết đứt nham nhở sắc bén sạch sẽ.",
                    "kiem_tra_thuc_dia": "Nhổ nhẹ cây thấy đứt ngang sát cổ rễ, bóc vỏ rễ thấy lõi gỗ màu nâu thẫm có mùi đất mốc ẩm nồng.",
                    "phac_do_vietgap": {
                        "canh_tac": "Lên liếp cao ráo thoát nước tốt, phơi ải đất kết hợp rải vôi bột trước khi gieo trồng.",
                        "sinh_hoc": "Tưới phòng gốc bằng hỗn hợp Bacillus subtilis kết hợp Trichoderma harzianum ngay sau khi mầm nhú.",
                        "khuyen_cao_chuyen_gia": "Xử lý đất và hạt giống bằng hoạt chất Metalaxyl-M, Fludioxonil hoặc Ridomil Gold khi phát hiện cây con chớm héo."
                    }
                }
            ]
        }
        crops.append(crop_obj)
        
    return crops

if __name__ == '__main__':
    data = get_module3_crops()
    print(f"Module 3 generated {len(data)} crops: {data[0]['id']} -> {data[-1]['id']}")
