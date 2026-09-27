# -*- coding: utf-8 -*-
"""
Worker 1 - Part 5: Tây Nguyên (Crops 101 to 113)
Kon Tum, Gia Lai, Đắk Lắk, Đắk Nông, Lâm Đồng
"""

def get_part5_crops():
    return [
        {
            "id": "w1_101",
            "topic": "Cay_Cong_Nghiep_Xuat_Khau",
            "name_vi": "Cà phê Robusta Buôn Ma Thuột Đắk Lắk",
            "scientific_name": "Coffea canephora Pierre ex A.Froehner cv. Buon Ma Thuot",
            "dia_ban_pho_bien": ["Buôn Ma Thuột", "Cư M'gar", "Krông Pắc", "Đắk Lắk", "Gia Lai", "Đắk Nông"],
            "dac_tinh_sinh_thai": "Thủ phủ cà phê Việt Nam trên cao nguyên bazan màu mỡ tầng dày > 2m độ cao 500 - 800m, khí hậu nhiệt đới gió mùa có hai mùa mưa nắng rõ rệt, hạt cà phê tròn mẩy hàm lượng caffeine đậm đặc 2-2.5% vị đắng đậm sánh ngậy béo hương sôcôla quyến rũ toàn cầu.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Rỉ sắt bụi phấn vàng cam lá cà phê",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Hemileia vastatrix"
                    },
                    "trieu_chung_dien_hinh": [
                        "Mặt dưới phiến lá xuất hiện những đốm tròn nhỏ màu vàng nhạt, sau phủ lớp bột phấn mịn như phấn rỉ sắt màu vàng cam óng ả",
                        "Mặt trên lá tương ứng xuất hiện các đốm vàng nhạt hơi nhô gồ ghề sau chuyển sang màu nâu xám cháy khô",
                        "Lá bị khô cháy từng mảng lớn và rụng hàng loạt làm trơ trụi cành mang quả",
                        "Cành cà phê bị khô kiệt trơ que (hiện tượng khô cành khô ngọn) làm mất mùa nghiêm trọng các vụ sau"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Đốm mắt cua Cercospora: Đốm Cercospora có tâm xám bạc viền nâu đỏ sắc nét và không có lớp bụi phấn nấm màu vàng cam ở mặt dưới như nấm Hemileia vastatrix.",
                    "kiem_tra_thuc_dia": "Lấy ngón tay miết nhẹ vào mặt dưới lá thấy bột phấn màu vàng cam óng dính đầy trên đầu ngón tay như nhũ vàng.",
                    "phac_do_vietgap": {
                        "canh_tac": "Trồng cây che bóng hợp lý (muồng đen, sầu riêng), tỉa cành thông thoáng sau thu hoạch, bón phân cân đối N-P-K tăng kali.",
                        "sinh_hoc": "Phun phòng bằng chế phẩm nấm đối kháng Bacillus subtilis kết hợp Nano Bạc Đồng 500ppm.",
                        "khuyen_cao_chuyen_gia": "Phun luân phiên các hoạt chất trừ rỉ sắt chuyên tính Hexaconazole (Anvil 5SC), Cyproconazole hoặc Azoxystrobin khi chớm nhú chấm vàng cam đầu mùa mưa."
                    }
                },
                {
                    "ten_benh": "Bệnh Khô cành khô quả thán thư chùm cà phê",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Colletotrichum kahawae / Colletotrichum gloeosporioides"
                    },
                    "trieu_chung_dien_hinh": [
                        "Trên đốt cành non xuất hiện các vết lõm hình thoi màu nâu đen làm teo thắt đốt cành",
                        "Phần cành phía trên vết bệnh bị héo lá và khô chết giòn gãy",
                        "Trên quả cà phê non và quả chín xuất hiện các đốm đen tròn lõm sâu làm thối đen nhân hạt",
                        "Quả cà phê bị khô đen teo tóp dính chặt trên chùm không rụng làm giảm nghiêm trọng sản lượng nhân xô"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Khô cành do thiếu dinh dưỡng hay quá tải quả: Khô sinh lý cả cành khô đều màu từ đầu ngọn vào trong; Thán thư có các vết lõm thâm đen hình thoi rõ nét ở các đốt cành có ổ nấm li ti.",
                    "kiem_tra_thuc_dia": "Dùng tay bẻ đoạn cành khô thấy gãy giòn rụm tại đúng vết lõm thâm đen, cạo vỏ thấy mô mạch dẫn bên dưới đen sì.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt bỏ cành khô cành bệnh đem tiêu hủy, bón bổ sung phân hữu cơ vi sinh và vôi bột nâng pH đất bazan lên 5.5 - 6.5.",
                        "sinh_hoc": "Phun chế phẩm Nano Chitosan kết hợp nấm đối kháng Chaetomium bảo vệ chùm quả giai đoạn nuôi hạt.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bằng Antracol 70WP, Amistar Top 325SC hoặc Booc-đô 1% giai đoạn đầu và giữa mùa mưa."
                    }
                },
                {
                    "ten_benh": "Bệnh Nấm hồng thắt nghẽn cành cà phê",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Corticium salmonicolor (Erythricium salmonicolor)"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết bệnh bắt đầu từ các chẽ ba cành hoặc kẽ nách cuống quả dưới dạng mạng tơ nấm màu trắng bạc mỏng",
                        "Sau đó mạng nấm dày lên chuyển sang màu hồng phấn hoặc cam nhạt như màu cá hồi bao bọc kín chu vi cành",
                        "Mô vỏ cành dưới màng nấm hồng bị nứt nẻ thối mục làm tắc hoàn toàn dòng nhựa dẫn",
                        "Toàn bộ lá và chùm quả trên cành bị héo khô chuyển sang màu nâu vàng và chết rũ dính trên cây"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Nấm rỉ sắt: Rỉ sắt chỉ tấn công phiến lá có mụn bột cam rơi rụng; Nấm hồng tạo màng tơ nhung màu hồng phấn bao bọc kín cả cành gỗ lớn làm chết cả cành.",
                    "kiem_tra_thuc_dia": "Vạch tán lá thấy cành bị bao bọc bởi một lớp bột mịn màng màu hồng phấn rất đẹp mắt, dùng móng tay cạo nhẹ thấy lớp vỏ cành bên dưới bị thối mục đen.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt tỉa cành la sát đất, tạo độ thông thoáng trong tán cây cà phê vào mùa mưa dầm Tây Nguyên.",
                        "sinh_hoc": "Quét dung dịch Nano Đồng hữu cơ 1000ppm vào các chẽ ba cành để phòng ngừa màng nấm phát triển.",
                        "khuyen_cao_chuyen_gia": "Quét hoặc phun trừ bằng hoạt chất Validamycin A, Hexaconazole (Anvil 5SC) hoặc dung dịch Booc-đô 1% khi chớm xuất hiện mảng hồng."
                    }
                }
            ]
        },
        {
            "id": "w1_102",
            "topic": "Cay_Cong_Nghiep_Xuat_Khau",
            "name_vi": "Cà phê Arabica Cầu Đất Đà Lạt",
            "scientific_name": "Coffea arabica L. cv. Bourbon/Typica Cau Dat",
            "dia_ban_pho_bien": ["Cầu Đất", "Trạm Hành", "Đà Lạt", "Lạc Dương", "Lâm Đồng"],
            "dac_tinh_sinh_thai": "Hoàng hậu cà phê Việt Nam trồng ở độ cao 1.400 - 1.650m trên đất đỏ bazan dốc thoải, quanh năm khí hậu ôn đới se lạnh mây mù mờ ảo, hạt cà phê Arabica Typica và Bourbon thơm nức hương hoa quả vị chua thanh quý phái hậu vị ngọt ngào sâu lắng làm say đắm giới mộ điệu quốc tế.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Đốm mắt cua tròn lá cà phê chè",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Cercospora coffeicola"
                    },
                    "trieu_chung_dien_hinh": [
                        "Phiến lá xuất hiện những đốm tròn nhỏ tâm xám bạc viền nâu đỏ sẫm gờ nổi rõ ràng như mắt cua",
                        "Quanh vết đốm luôn có một quầng halo vàng sáng rất đặc trưng",
                        "Lá già bị úa vàng rụng sớm hàng loạt làm trơ cành mang quả",
                        "Trên quả cà phê chè xuất hiện các đốm nâu đen lõm sâu làm vỏ dính chặt vào nhân hạt khó xát vỏ tươi"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bệnh rỉ sắt: Rỉ sắt có bột phấn vàng cam mặt dưới lá; Cercospora vết đốm tròn phẳng tâm bạc có quầng halo vàng sáng chói không có bụi bột nấm.",
                    "kiem_tra_thuc_dia": "Soi lá ngược ánh sáng thấy rõ quầng tròn vàng rực rỡ bao quanh tâm xám bạc như mắt chim.",
                    "phac_do_vietgap": {
                        "canh_tac": "Trồng cây che bóng điều tiết ánh sáng tán xạ 40%, bón phân hữu cơ vi sinh cân đối N-P-K.",
                        "sinh_hoc": "Phun phòng định kỳ Nano Bạc Đồng 400ppm kết hợp vi khuẩn đối kháng Bacillus subtilis.",
                        "khuyen_cao_chuyen_gia": "Phun phòng ngừa bằng Mancozeb, Difenoconazole hoặc Antracol 70WP giai đoạn đầu mùa mưa Cầu Đất."
                    }
                },
                {
                    "ten_benh": "Bệnh Thối lở cổ rễ chết nghẹt rễ tơ",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Tổ hợp nấm và tuyến trùng",
                        "ten_khoa_hoc": "Rhizoctonia solani / Fusarium oxysporum / Pratylenchus coffeae"
                    },
                    "trieu_chung_dien_hinh": [
                        "Phần cổ rễ sát mặt đất bị thâm đen úng nước teo thắt vỏ tróc mục nát",
                        "Bộ rễ tơ ngầm bị tuyến trùng đục khoét tạo nốt sưng u thối đen tuột vỏ",
                        "Lá cà phê chè bị héo vàng rũ xanh đột ngột hoặc úa vàng từ từ rồi chết đứng",
                        "Cây cà phê con trong vườn ươm và cây mới trồng ngoài vườn ngã rạp chết hàng loạt"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Chết khô do nghẹt rễ đất sét nén chặt: Đất nén rễ cọc bị cong queo nhưng vỏ rễ không thối mủn; Bệnh nấm lở cổ rễ mô vỏ thối đen rữa nát tuột khỏi lõi gỗ bốc mùi ẩm mốc khó chịu.",
                    "kiem_tra_thuc_dia": "Nhổ nhẹ cây cà phê con thấy đứt lìa ngang cổ rễ thối mục đen, bóp nhẹ thấy trơn tuột nhớt nước.",
                    "phac_do_vietgap": {
                        "canh_tac": "Lên luống cao thoát nước, rải vôi bột khử chua đất bazan trước khi đặt bầu cây con.",
                        "sinh_hoc": "Tưới phòng gốc bằng hỗn hợp men vi sinh Bacillus subtilis kết hợp Trichoderma harzianum định kỳ 1 tháng/lần.",
                        "khuyen_cao_chuyen_gia": "Tưới thuốc trừ nấm rễ Validamycin A hoặc Metalaxyl-M (Ridomil Gold) khi chớm có dấu hiệu héo đọt non."
                    }
                }
            ]
        },
        {
            "id": "w1_103",
            "topic": "Cay_Cong_Nghiep_Xuat_Khau",
            "name_vi": "Cà phê Liberica Cư M'gar Đắk Lắk",
            "scientific_name": "Coffea liberica Bull. ex Hiern cv. Cu Mgar",
            "dia_ban_pho_bien": ["Cư M'gar", "Buôn Đôn", "Đắk Lắk", "Đắk Mil", "Đắk Nông"],
            "dac_tinh_sinh_thai": "Cây cà phê mít cổ thụ thân gỗ cao lớn 10-15m tán lá khổng lồ xanh mướt, rễ cọc đâm sâu chịu hạn chịu gió bão giỏi nhất trong các loài cà phê, quả to như quả mận chín đỏ mọng, vị chua thanh đậm đà hương vị hoa quả rừng nhiệt đới chuyên dùng phối trộn tạo gu cà phê độc đáo.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Đốm vòng nâu xám lá cà phê mít",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Pestalotiopsis coffeae"
                    },
                    "trieu_chung_dien_hinh": [
                        "Phiến lá lớn dày cộp xuất hiện những đốm tròn màu nâu xám có vân đồng tâm gờ nổi",
                        "Tâm vết bệnh bị khô xám bạc, có các chấm đen nhỏ li ti là ổ bào tử nấm",
                        "Mép và chóp lá bị cháy khô cong queo giòn rách làm giảm quang hợp",
                        "Cành cà phê mít bị còi cọc đâm ít chồi hoa non"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Cháy nắng phiến lá: Cháy nắng vết màu vàng rơm khô phẳng lì; Pestalotiopsis có vân đồng tâm gợn sóng sắc nét và chấm đen ổ bào tử nấm li ti.",
                    "kiem_tra_thuc_dia": "Vò nhẹ mép lá thấy giòn vụn rách toạc, soi kính lúp thấy các chấm bào tử nấm li ti trên nền lá bạc.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt tỉa cành thông thoáng sau thu hoạch, dọn sạch tàn dư dưới gốc cây cổ thụ.",
                        "sinh_hoc": "Phun phòng bằng chế phẩm nấm đối kháng Chaetomium kết hợp Nano Bạc Đồng 400ppm.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bằng Mancozeb hoặc Antracol 70WP khi độ ẩm không khí tăng cao."
                    }
                },
                {
                    "ten_benh": "Bệnh Nấm muội đen vỏ quả dính hạt",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Nấm hoại sinh",
                        "ten_khoa_hoc": "Capnodium spp. / Coccus viridis",
                        "vector_truyen_benh": "Rệp sáp vảy xanh tiết mật ngọt"
                    },
                    "trieu_chung_dien_hinh": [
                        "Mặt vỏ quả và phiến lá cà phê mít bị phủ một lớp màng đen như muội than đáy nồi",
                        "Lớp muội đen làm vỏ quả bị lem nhem dính chặt vào cùi quả khó phơi khô và tách hạt",
                        "Dưới lớp muội đen ở kẽ cuống quả bám đầy các ổ rệp vảy xanh tiết dịch mật ngọt",
                        "Cây bị suy giảm khả năng quang hợp tích lũy chất khô cho nhân hạt"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Thán thư thối đen quả: Muội bồ hóng lấy khăn ướt lau sạch bong để lộ vỏ quả lành lặn; Thán thư ăn sâu hoại tử mô thịt quả không thể lau sạch.",
                    "kiem_tra_thuc_dia": "Lấy ngón tay miết mạnh lớp đen trên vỏ quả thấy bột than đen dính vào tay, vỏ quả bên dưới vẫn vàng bóng bình thường.",
                    "phac_do_vietgap": {
                        "canh_tac": "Tỉa cành thông thoáng, bắt diệt kiến đen tha rệp lên cây.",
                        "sinh_hoc": "Phun dung dịch nước rửa chén sinh học loãng 0.2% hoặc dầu khoáng SK Enspray 99EC diệt rệp và rửa trôi muội đen.",
                        "khuyen_cao_chuyen_gia": "Phun trừ rệp bằng Spirotetramat hoặc Abamectin sinh học giai đoạn nuôi quả non."
                    }
                }
            ]
        },
        {
            "id": "w1_104",
            "topic": "Cay_Cong_Nghiep_Xuat_Khau",
            "name_vi": "Tiêu đen Chư Sê Gia Lai cao sản",
            "scientific_name": "Piper nigrum L. cv. Vinh Linh Chu Se",
            "dia_ban_pho_bien": ["Chư Sê", "Chư Pưh", "Đắk Đoa", "Gia Lai", "Đắk Song", "Đắk Nông"],
            "dac_tinh_sinh_thai": "Thủ phủ hồ tiêu lớn nhất Tây Nguyên trên trụ sống muồng đen đất đỏ bazan màu mỡ, rễ ăn nổi cần thoát nước tuyệt hảo mùa mưa dầm, chuỗi tiêu dài hạt mẩy chắc nịch hàm lượng piperine cay nồng đậm đặc hương thơm nức tiếng xuất khẩu khắp năm châu.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Chết nhanh thối ướt dây tiêu (Bệnh Phytophthora)",
                    "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Phytophthora capsici"
                    },
                    "trieu_chung_dien_hinh": [
                        "Cổ rễ sát mặt đất và hệ rễ tơ ngầm bị sũng nước thối đen mục nát trong vòng 5-7 ngày",
                        "Lá tiêu trên toàn bộ trụ tiêu bị héo rũ xanh rất nhanh, lá rụng lả tả trắng gốc trụ chỉ trong vài ngày như bị dội nước sôi",
                        "Gốc thân chính bị nứt mục tróc vỏ bốc mùi chua nồng, các đốt thân tiêu bị rụng lả tả từng đoạn",
                        "Lây lan cực nhanh theo dòng nước mưa chảy tràn làm chết trắng hàng loạt vườn tiêu bạc tỷ"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bệnh Chết chậm (Fusarium): Chết chậm lá vàng úa từ từ qua nhiều tháng rồi mới rụng; Chết nhanh lá héo rũ xanh rụng sạch chỉ trong 1-2 tuần và gốc thân thối ướt nhầy nhụa.",
                    "kiem_tra_thuc_dia": "Cào đất quanh cổ rễ thấy mô vỏ rễ thối đen ướt nhầy bốc mùi hôi thối mục nát, cầm dải rễ vuốt nhẹ thấy tuột vỏ chỉ còn trơ lõi chỉ trắng.",
                    "phac_do_vietgap": {
                        "canh_tac": "Đào mương thoát nước sâu 50-60cm giữa các hàng tiêu chống ngập úng mùa mưa, tuyệt đối không để nước chảy tràn giữa các bồn tiêu.",
                        "sinh_hoc": "Tưới phòng gốc định kỳ bằng hỗn hợp men vi sinh đối kháng Trichoderma harzianum kết hợp xạ khuẩn Streptomyces và Bacillus subtilis.",
                        "khuyen_cao_chuyen_gia": "Tưới gốc và phun thân luân phiên bằng Phosphonate hữu cơ (Aliette 800WG, Ridomil Gold 68WG) 3 lần vào đầu, giữa và cuối mùa mưa."
                    }
                },
                {
                    "ten_benh": "Bệnh Chết chậm vàng lá u sưng rễ tiêu",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Tổ hợp tuyến trùng và nấm",
                        "ten_khoa_hoc": "Meloidogyne incognita / Fusarium solani"
                    },
                    "trieu_chung_dien_hinh": [
                        "Tuyến trùng chui vào rễ tơ đục khoét làm rễ sưng u cục méo mó như chuỗi hạt cườm",
                        "Vết thương hở do tuyến trùng tạo điều kiện cho nấm Fusarium xâm nhập làm thối đen rễ cọc và rễ dẫn",
                        "Lá tiêu chuyển màu vàng úa từ từ từ tầng dưới lên tầng trên, đọt non ngừng sinh trưởng",
                        "Cây suy kiệt rụng lá dần dần kéo dài từ vài tháng đến 1-2 năm rồi mới chết khô đứng trên trụ"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Thiếu đạm hoặc hạn: Thiếu đạm lá vàng đều nhưng rễ tơ hoàn toàn lành lặn không có u sưng; Chết chậm rễ có vô số nốt u sần chuỗi cườm và thối đen lõi rễ.",
                    "kiem_tra_thuc_dia": "Bới rễ tơ tiêu lên rửa sạch thấy hàng loạt nốt u sần tròn nhỏ như hạt kê hạt đỗ dính liền trên rễ, rễ tơ bị thối đen xơ xác.",
                    "phac_do_vietgap": {
                        "canh_tac": "Trồng cỏ cúc lạc hoặc cúc vạn thọ quanh bồn tiêu để tiết chất ức chế tuyến trùng tự nhiên; bón tăng cường phân chuồng hoai mục.",
                        "sinh_hoc": "Tưới chế phẩm nấm ký sinh tuyến trùng Paecilomyces lilacinus kết hợp bã bánh dầu neem định kỳ 2 tháng/lần.",
                        "khuyen_cao_chuyen_gia": "Tưới xử lý đất bằng hoạt chất trừ tuyến trùng sinh học Abamectin hoặc Fluopyram kết hợp thuốc trừ nấm rễ."
                    }
                }
            ]
        },
        {
            "id": "w1_105",
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": "Sầu riêng Ri6 Ea H'leo Đắk Lắk",
            "scientific_name": "Durio zibethinus Rumph. ex Murray cv. Ri6 Ea Hleo",
            "dia_ban_pho_bien": ["Ea H'leo", "Krông Pắc", "Cư Kuin", "Đắk Lắk", "Đắk Mil", "Đắk Nông"],
            "dac_tinh_sinh_thai": "Cây ăn quả tỷ đô Tây Nguyên trên đất đỏ bazan tơi xốp màu mỡ, cơm sầu riêng vàng ươm hạt lép béo ngậy ngọt đậm đà không xơ sượng, cây sinh trưởng cực khỏe nhưng rất mẫn cảm với úng rễ và nấm nứt thân xì mủ mùa mưa dầm.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Nứt thân xì mủ thối gốc rễ sầu riêng (Bệnh xì mủ Phytophthora)",
                    "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Phytophthora palmivora"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vỏ thân chính và cổ rễ sát mặt đất xuất hiện những vết nứt dọc sũng nước màu nâu đen",
                        "Tại vết nứt ứa ra những giọt nhựa mủ màu cánh gián dẻo quánh dính nhớt",
                        "Mô vỏ dưới vết nứt bị thối nâu đen ăn sâu vào lớp gỗ bên trong bít tắc mạch dẫn",
                        "Bộ rễ tơ và rễ cọc bị thối đen tuột vỏ, lá vàng đồng loạt và rụng dần làm cây chết rũ đứng giữa vườn",
                        "Trên quả sầu riêng xuất hiện vết thối nâu đen tròn lõm sâu làm thối cơm sầu riêng và rụng non"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Xì mủ do mọt đục cành: Mọt đục cành có lỗ nhỏ tròn như đầu tăm đùn mạt cưa phân sâu li ti; Phytophthora thân nứt toác thành mảng thối ướt bốc mùi chua nồng không có mạt cưa.",
                    "kiem_tra_thuc_dia": "Dùng dao bén cạo nhẹ lớp vỏ ngoài thấy tầng tượng tầng chuyển màu nâu đen sũng nước, nhựa mủ dính vào đầu ngón tay.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cào đất quanh cổ rễ để lộ cổ rễ thoáng gió, tuyệt đối không tủ rơm rác cỏ sát thân gốc sầu riêng.",
                        "sinh_hoc": "Cạo sạch mô vỏ thối rồi quét chế phẩm nấm đối kháng Chaetomium kết hợp Nano Đồng đặc.",
                        "khuyen_cao_chuyen_gia": "Quét gốc hoặc tiêm thân bằng Phosphonate hữu cơ (Aliette, Agrifos 400) kết hợp tưới gốc Ridomil Gold định kỳ trong mùa mưa."
                    }
                },
                {
                    "ten_benh": "Bệnh Cháy lá chết đọt non nấm Rhizoctonia",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Rhizoctonia solani"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết bệnh bắt đầu từ các lá non ở chùm đọt dưới dạng mảng úng nước màu xanh xám loang lổ",
                        "Nhiều lá non bị dính bết lại với nhau bởi mạng tơ nấm màu nâu nhạt như tổ nhện",
                        "Lá bị khô cháy chuyển sang màu nâu vàng rơm và rụng hàng loạt để lại cành đọt khô que đen sì (chết đọt)",
                        "Đọt non bị thối đen khô quắt không bung đợt cơi đọt mới được"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Rầy nhảy (rầy phấn trắng) chích đọt non: Rầy nhảy làm đọt teo xoăn quăn queo và nhìn thấy rầy phấn trắng nhảy tanh tách; Nấm Rhizoctonia lá dính bết thành chùm bởi màng tơ nhện nâu tro và cháy loang mảng lớn.",
                    "kiem_tra_thuc_dia": "Vạch chùm lá đọt non thấy các phiến lá dính chặt vào nhau bởi sợi tơ nấm nâu nhạt, gỡ ra thấy lá mục nát giòn rụm.",
                    "phac_do_vietgap": {
                        "canh_tac": "Tỉa cành thông thoáng, hạn chế bón thừa phân đạm ure trong mùa mưa dầm.",
                        "sinh_hoc": "Phun phòng bằng chế phẩm vi sinh Bacillus subtilis kết hợp Nano Bạc Đồng 500ppm.",
                        "khuyen_cao_chuyen_gia": "Phun trừ bằng hoạt chất Validamycin A, Hexaconazole (Anvil 5SC) hoặc Azoxystrobin khi chớm xuất hiện mảng lá dính bết."
                    }
                }
            ]
        },
        {
            "id": "w1_106",
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": "Bơ Booth 7 Cư Kuin Đắk Lắk",
            "scientific_name": "Persea americana Mill. cv. Booth 7",
            "dia_ban_pho_bien": ["Cư Kuin", "Krông Pắc", "Đắk Lắk", "Đắk Song", "Đắk Nông"],
            "dac_tinh_sinh_thai": "Giống bơ sáp chín muộn nhập khẩu từ Mỹ phát triển rực rỡ trên cao nguyên bazan, quả tròn xoe vỏ xanh đậm dày sần sùi, cơm bơ vàng óng dẻo quánh béo ngậy không xơ chứa nhiều axit béo không no omega 3-6-9 tốt cho tim mạch, thu hoạch muộn tháng 9-11 bán giá rất cao.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Thối rễ xì mủ vỏ gốc bơ Booth",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Phytophthora cinnamomi"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vỏ thân sát gốc và cổ rễ bị sũng nước nứt toác từng vệt dài, ứa ra những giọt nhựa mủ dẻo màu cánh gián",
                        "Mô vỏ dưới vết nứt bị thối đen ăn sâu vào tầng mô gỗ bên trong bốc mùi chua nồng",
                        "Tán lá bơ ngả màu vàng nhạt đồng loạt và rụng dần làm cành trơ que khô",
                        "Hệ rễ tơ ngầm bị thối tuột vỏ chỉ còn trơ lõi chỉ trắng xơ xác, cây chết đứng giữa vườn"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Sâu đục thân xì mủ: Sâu đục thân có lỗ đùn mạt cưa phân sâu li ti; Phytophthora nứt dọc thành mảng thối ướt không có mạt cưa.",
                    "kiem_tra_thuc_dia": "Dùng dao con cạo nhẹ lớp vỏ thấy tầng tượng tầng chuyển màu nâu đen sũng nước, nhựa mủ dính vào đầu ngón tay.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cào đất quanh cổ rễ để lộ cổ rễ thoáng gió, quét vôi trắng thân cây cao 1m trước mùa mưa lũ.",
                        "sinh_hoc": "Cạo sạch mô vỏ thối rồi quét chế phẩm nấm đối kháng Chaetomium kết hợp Nano Đồng đặc.",
                        "khuyen_cao_chuyen_gia": "Quét gốc hoặc tưới đẫm vùng rễ bằng Phosphonate hữu cơ hoặc Aliette 800WG định kỳ trong mùa mưa."
                    }
                },
                {
                    "ten_benh": "Bệnh Thán thư thối đen cuống quả bơ vỏ dày",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Colletotrichum gloeosporioides"
                    },
                    "trieu_chung_dien_hinh": [
                        "Cuống quả và vỏ quả bơ xuất hiện những chấm nâu đen nhỏ lõm sâu",
                        "Vết thâm lan rộng làm cuống quả bị thắt nghẽn thối đen, quả bơ non bị rụng lả tả trắng gốc",
                        "Trên quả chín xuất hiện các đốm tròn thâm nâu đồng tâm ăn sâu vào thịt cơm bơ làm thối nhũn chua",
                        "Lá già xuất hiện các vệt cháy thán thư màu nâu đỏ làm rách thủng phiến lá"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bọ xít muỗi chích hút: Bọ xít chích có chấm thủng nhỏ li ti rỉ giọt nhựa trong; Nấm thán thư là vết lõm sâu hình tròn đồng tâm lan rộng vào thịt quả cơm bơ.",
                    "kiem_tra_thuc_dia": "Dùng ngón tay ấn vào đốm đen trên quả thấy vỏ lõm mềm, thịt cơm bên dưới thâm đen nhũn bốc mùi men chua.",
                    "phac_do_vietgap": {
                        "canh_tac": "Tỉa cành thông thoáng, dọn sạch tàn dư dưới gốc cây bơ.",
                        "sinh_hoc": "Phun Nano Bạc Chitosan phòng trừ mầm nấm bề mặt quả giai đoạn nuôi quả non.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bằng Azoxystrobin, Difenoconazole hoặc Antracol 70WP giai đoạn đậu quả non."
                    }
                }
            ]
        },
        {
            "id": "w1_107",
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": "Bơ 034 Bảo Lộc Lâm Đồng quả dài",
            "scientific_name": "Persea americana Mill. cv. 034 Bao Loc",
            "dia_ban_pho_bien": ["Bảo Lộc", "Bảo Lâm", "Di Linh", "Lâm Đồng", "Đắk Nông"],
            "dac_tinh_sinh_thai": "Giống bơ sáp bản địa đột biến quả dài ngoằng 30-40cm hình ngón tay uốn cong duyên dáng, vỏ quả xanh bóng mỏng dính, cơm bơ vàng ươm dẻo quánh béo ngậy hạt siêu nhỏ, cây ra hoa đậu quả rải vụ quanh năm tại vùng cao nguyên mát mẻ Bảo Lộc.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Sẹo ghẻ nhám lồi vỏ quả bơ dài",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Sphaceloma perseae (Elsinoë perseae)"
                    },
                    "trieu_chung_dien_hinh": [
                        "Trên vỏ quả bơ dài xuất hiện những nốt mụn sẹo nhỏ lồi lên màu nâu xám sần sùi như da cóc",
                        "Các nốt sẹo liên kết thành từng mảng lớn làm vỏ quả nứt nẻ sần sùi méo mó cong queo",
                        "Lá non bị các nốt mụn sưng gồ làm phiến lá nhăn nheo biến dạng cong queo hình thìa",
                        "Quả bơ bị giảm phẩm cấp thương phẩm nghiêm trọng không thể xuất khẩu"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Trầy xước do gió cọ xát vào cành: Trầy xước vết phẳng liền sẹo trắng xám; Ghẻ nhám chóp nhọn nhô lồi sần sùi gồ ghề như da cóc.",
                    "kiem_tra_thuc_dia": "Lấy tay sờ qua mặt quả thấy cộm gai rát ráp như giấy ráp, móng tay cạo nhẹ tróc vảy bần cứng.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt tỉa cành thông thoáng sau thu hoạch, vệ sinh dụng cụ kéo tỉa cành.",
                        "sinh_hoc": "Phun phòng bằng nấm đối kháng Bacillus subtilis kết hợp Nano Chitosan.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bằng Booc-đô 1%, Difenoconazole hoặc Antracol 70WP giai đoạn lộc non nhú 2-3cm."
                    }
                },
                {
                    "ten_benh": "Bệnh Thối ngọn khô cành bơ sáp",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Botryosphaeria dothidea"
                    },
                    "trieu_chung_dien_hinh": [
                        "Đọt non và cành non mới nhú xuất hiện các chấm thâm nâu sũng nước",
                        "Vết bệnh lan nhanh làm toàn bộ đọt non bị thâm đen, khô tóp quắt queo cong gập hình móc câu",
                        "Lá già xuất hiện các mảng cháy thán thư màu nâu đỏ làm rách thủng phiến lá",
                        "Cành non bị khô chết ngọn làm cây còi cọc chùn tán"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Sâu đục ngọn: Sâu đục ngọn để lại lỗ đục có phân sâu đùn ra; Nấm thối ngọn làm cả đoạn ngọn mềm nhũn thối đen khô quắt không có lỗ đục cơ giới.",
                    "kiem_tra_thuc_dia": "Cầm ngọn bơ thối thấy mềm nhũn dính bết ngón tay, ngửi thấy mùi chua mục của mô bị nấm phân hủy.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt bỏ cành khô dưới vết nứt 10cm đem đốt, khử trùng vết cắt bằng cồn hoặc keo liền sẹo.",
                        "sinh_hoc": "Phun Nano Bạc Đồng 500ppm kết hợp chế phẩm sinh học Chitosan kích kháng bảo vệ đọt non.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bằng hoạt chất Azoxystrobin hoặc Difenoconazole khi cây bắt đầu bung nhú đợt lộc non."
                    }
                }
            ]
        },
        {
            "id": "w1_108",
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": "Mắc ca Đắk Song Đắk Nông",
            "scientific_name": "Macadamia integrifolia Maiden & Betche cv. Dak Song",
            "dia_ban_pho_bien": ["Đắk Song", "Tuy Đức", "Đắk Nông", "Lâm Hà", "Lâm Đồng"],
            "dac_tinh_sinh_thai": "Cây ăn hạt 'Nữ hoàng hạt khô' nguồn gốc từ Úc thích ứng kỳ diệu trên cao nguyên bazan Đắk Nông độ cao 700 - 1.000m mát mẻ, nhân hạt tròn căng mọng màu trắng sữa béo ngậy giòn tan giàu dinh dưỡng và dầu béo chưa bão hòa cao cấp, cây che bóng và chắn gió tuyệt vời cho cà phê tiêu.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Đốm mắt chim vỏ xanh quả mắc ca",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Pestalotiopsis sp."
                    },
                    "trieu_chung_dien_hinh": [
                        "Vỏ xanh bên ngoài quả mắc ca xuất hiện những đốm tròn nhỏ màu nâu đen có quầng vàng",
                        "Vết đốm lan rộng tâm hóa xám tro lõm sâu làm nứt nẻ lớp vỏ quả ngoài",
                        "Quả non bị chai sượng còi cọc và rụng sớm làm giảm năng suất thu hoạch hạt",
                        "Lá già xuất hiện các vệt cháy loang lổ mép lá"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Vết ong chích quả non: Vết ong chích có chấm thủng cơ giới nhỏ rỉ giọt nhựa trong; Nấm bệnh là vết lõm tròn đồng tâm màu nâu đen lan rộng ra mô vỏ xanh.",
                    "kiem_tra_thuc_dia": "Dùng tay sờ vào đốm đen trên vỏ xanh thấy cộm cứng, soi kính lúp thấy các chấm đen ổ bào tử nấm li ti.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt tỉa cành thông thoáng, dọn sạch tàn dư dưới gốc cây.",
                        "sinh_hoc": "Phun phòng bằng chế phẩm nấm đối kháng Chaetomium kết hợp Nano Chitosan.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bằng Antracol 70WP hoặc Mancozeb khi mưa phùn kéo dài."
                    }
                },
                {
                    "ten_benh": "Bệnh Thối hoa khô rụng chùm non mắc ca",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Tổ hợp nấm",
                        "ten_khoa_hoc": "Botrytis cinerea / Phytophthora spp."
                    },
                    "trieu_chung_dien_hinh": [
                        "Chùm hoa chuỗi dài của mắc ca bị sũng nước chuyển màu nâu sẫm",
                        "Khi trời mưa phùn sương mù ẩm phủ lớp mốc mịn màu xám tro dày đặc bốc mùi chua",
                        "Hoa bị thối rụng hàng loạt, chùm hoa trơ cuống đen sì không đậu được quả non nào",
                        "Quả non mới đậu bị thâm đen teo tóp rụng trắng gốc cây"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Rụng hoa sinh lý do gió lốc khô: Gió lốc hoa khô vàng rụng tự nhiên không có lớp mốc xám tro bồng bềnh; Bệnh nấm chùm hoa ẩm ướt thối mục phủ màng mốc xám tro dày đặc.",
                    "kiem_tra_thuc_dia": "Lắc nhẹ chùm hoa thấy hoa rụng lả tả, đưa tay chạm vào chùm hoa thấy dính bết màng tơ mốc xám tro.",
                    "phac_do_vietgap": {
                        "canh_tac": "Tỉa cành tạo tán thông thoáng đón nắng gió, khơi rãnh thoát nước sâu quanh gốc cây.",
                        "sinh_hoc": "Phun Nano Bạc Chitosan phòng trừ mầm nấm bề mặt chùm hoa giai đoạn trước khi hoa nở rộ.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bằng Iprodione (Rovral 50WP), Difenoconazole hoặc Amistar Top khi chùm hoa vừa nhú dài 5-10cm."
                    }
                }
            ]
        },
        {
            "id": "w1_109",
            "topic": "Cay_Cong_Nghiep_Xuat_Khau",
            "name_vi": "Ca cao Ea Kar Đắk Lắk hữu cơ",
            "scientific_name": "Theobroma cacao L. cv. Ea Kar",
            "dia_ban_pho_bien": ["Ea Kar", "Krông Pắc", "Đắk Lắk", "Đạ Huoai", "Lâm Đồng"],
            "dac_tinh_sinh_thai": "Cây công nghiệp trồng xen dưới tán điều và dừa trên đất bazan màu mỡ, quả to mọc từ thân cành vỏ quả màu vàng cam hoặc đỏ tía rực rỡ, hạt ca cao lên men đạt chuẩn hương vị sôcôla tinh tế thượng hạng xuất khẩu sang Nhật Bản và châu Âu.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Thối đen vỏ quả ca cao nấm sương (Bệnh thối quả Phytophthora)",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Phytophthora palmivora"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết bệnh bắt đầu từ cuống quả hoặc chóp quả dưới dạng đốm nâu sẫm ngậm nước",
                        "Vết thâm lan cực nhanh làm toàn bộ vỏ quả ca cao bị đen sì nhũn mềm",
                        "Trên bề mặt vỏ quả phủ một lớp màng tơ nấm màu trắng mịn như sương muối khi trời mưa dầm",
                        "Nấm ăn sâu vào bên trong làm thối đen rữa nát toàn bộ khối hạt ca cao bốc mùi thối chua",
                        "Quả bị thối khô quắt lại thành quả xác ướp màu đen dính chặt trên thân cây"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bọ xít muỗi chích quả: Bọ xít chích để lại các chấm đen nhỏ li ti sần sùi ở vỏ quả ngoài không ăn sâu vào hạt; Phytophthora làm quả đen sì toàn bộ và hạt ca cao bên trong bị thối rữa nát hoàn toàn.",
                    "kiem_tra_thuc_dia": "Dùng dao bổ quả ca cao thối đen thấy lớp hạt bên trong bị thối nhũn chảy nước chua bốc mùi men nồng nặc.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt tỉa cành thông thoáng, hạ thấp độ che bóng của cây tầng trên xuống 30-40% vào mùa mưa; thu gom toàn bộ quả xác ướp đem tiêu hủy.",
                        "sinh_hoc": "Phun phòng bằng chế phẩm nấm đối kháng Chaetomium kết hợp Nano Bạc Đồng 500ppm.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bắt buộc vào đầu và giữa mùa mưa bằng Booc-đô 1%, Ridomil Gold 68WG hoặc Aliette 800WG."
                    }
                },
                {
                    "ten_benh": "Bệnh Khô cành vệt sọc chết ngọn ca cao",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Oncobasidium theobromae"
                    },
                    "trieu_chung_dien_hinh": [
                        "Lá trên cành non bị vàng úa loang lổ có các đốm xanh rải rác, sau đó rụng sớm từ gốc cành lên ngọn",
                        "Cành non bị khô chết từ ngọn xuống làm trơ que que đen sì (hiện tượng khô cành que)",
                        "Cắt dọc cành bệnh thấy các vệt sọc màu nâu đen chạy dài trong tầng mô gỗ mạch dẫn",
                        "Cây ca cao bị suy tàn rụng lá xơ xác làm giảm mạnh năng suất đậu quả"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Khô cành do thiếu nước: Khô hạn cành khô đều từ ngoài vào trong không có vệt sọc nâu đen trong mạch gỗ; Bệnh Oncobasidium có vệt sọc nâu đen chạy dài trong lõi gỗ mạch dẫn.",
                    "kiem_tra_thuc_dia": "Dùng dao rạch dọc lớp vỏ cành non thấy các vệt sọc đen dài chạy dọc thớ gỗ, vết cắt ngang có các chấm đen mạch dẫn.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt bỏ cành bệnh sâu dưới vết sọc đen 20-30cm đem đốt tiêu hủy; chọn giống ca cao kháng bệnh ghép chồi.",
                        "sinh_hoc": "Phun phòng bằng men vi sinh Bacillus subtilis kết hợp Nano Chitosan bảo vệ đọt non.",
                        "khuyen_cao_chuyen_gia": "Phun phòng trừ bằng Tebuconazole, Difenoconazole hoặc Booc-đô 1% giai đoạn đầu mùa mưa."
                    }
                }
            ]
        },
        {
            "id": "w1_110",
            "topic": "Cay_Cong_Nghiep_Xuat_Khau",
            "name_vi": "Cao su tiểu điền Chư Păh Gia Lai",
            "scientific_name": "Hevea brasiliensis (Willd. ex A.Juss.) Müll.Arg.",
            "dia_ban_pho_bien": ["Chư Păh", "Ia Grai", "Gia Lai", "Ea H'leo", "Đắk Lắk"],
            "dac_tinh_sinh_thai": "Cây công nghiệp lấy mủ 'Vàng trắng' bạt ngàn Tây Nguyên trên đất đỏ bazan tầng dày thoát nước tốt, thân gỗ lớn cao 20-30m, mủ cao su thiên nhiên chất lượng tuyệt hảo chế biến săm lốp xuất khẩu toàn cầu, mùa đông rụng lá thay áo mới tuyệt đẹp.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Nấm hồng vỏ thân cành cao su",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Corticium salmonicolor"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết bệnh bắt đầu từ các chẽ ba cành hoặc kẽ vỏ thân dưới dạng giọt mủ trắng rỉ ra",
                        "Sau đó mạng sợi nấm phát triển dày đặc phủ lớp màng nhung màu hồng phấn hoặc cam nhạt như màu cá hồi bao quanh thân cành",
                        "Mô vỏ dưới màng nấm hồng bị nứt toác thối mục làm tắc hoàn toàn dòng nhựa mủ",
                        "Cành lớn phía trên vết bệnh bị héo lá và khô chết giòn gãy, tán cây bị trơ que xơ xác"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bệnh loét sọc cạo: Loét sọc chỉ xuất hiện trên miệng cạo mủ; Nấm hồng xuất hiện ở chẽ ba cành và thân trên cao phủ lớp màng nhung màu hồng phấn đặc thù.",
                    "kiem_tra_thuc_dia": "Quan sát thân cành thấy mảng màng nấm nhung màu hồng phấn bao bọc cành, cạo nhẹ thấy mô vỏ bên dưới thối đen mục nát.",
                    "phac_do_vietgap": {
                        "canh_tac": "Tỉa cành tạo tán thông thoáng, quét thuốc phòng ngừa lên các chẽ ba cành trước mùa mưa dầm Tây Nguyên.",
                        "sinh_hoc": "Quét dung dịch Nano Đồng hữu cơ 1000ppm vào các chẽ ba cành để ức chế màng nấm phát triển.",
                        "khuyen_cao_chuyen_gia": "Quét hoặc phun trừ bằng hoạt chất Validamycin A, Hexaconazole (Anvil 5SC) hoặc dung dịch Booc-đô 1% khi chớm xuất hiện mảng hồng."
                    }
                },
                {
                    "ten_benh": "Bệnh Loét sọc cạo mặt miệng mủ cao su",
                    "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Phytophthora botryosa / Phytophthora palmivora"
                    },
                    "trieu_chung_dien_hinh": [
                        "Trên mặt cạo mủ xuất hiện các sọc nhỏ màu nâu đen chạy dọc thẳng đứng theo thớ gỗ",
                        "Mô vỏ nguyên sinh bị thối đen nhũn nước mủn rữa, mủ cao su bị đông vón cục đen sì",
                        "Miệng cạo bị loét nứt toác mủ rỉ loang lổ làm hỏng hoàn toàn tầng sinh mô tái sinh vỏ",
                        "Cây cao su bị mất mủ hoàn toàn (hiện tượng khô miệng cạo) buộc phải bỏ cạo"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Khô miệng cạo sinh lý: Khô sinh lý mặt cạo khô ráo không có sọc đen và không có mủn mục mô vỏ; Loét sọc nấm có các sọc đen ngậm nước và mô vỏ thối nhũn chảy nước mủ hôi thối.",
                    "kiem_tra_thuc_dia": "Dùng dao cạo nhẹ lớp vỏ trên mặt cạo thấy các vệt sọc đen chạy dọc thẳng đứng ăn sâu vào tận lớp gỗ tượng tầng.",
                    "phac_do_vietgap": {
                        "canh_tac": "Ngừng cạo mủ ngay khi phát hiện bệnh, vệ sinh dao cạo bằng cồn y tế sau mỗi cây cạo.",
                        "sinh_hoc": "Quét dung dịch Nano Bạc Đồng 1000ppm bảo vệ mặt cạo định kỳ sau mỗi lứa cạo mùa mưa.",
                        "khuyen_cao_chuyen_gia": "Quét dung dịch Metalaxyl-M (Ridomil Gold) hoặc Aliette 800WG lên mặt cạo 3-5 ngày/lần cho đến khi vết sọc khô lành sẹo."
                    }
                }
            ]
        },
        {
            "id": "w1_111",
            "topic": "Cay_Cong_Nghiep_Xuat_Khau",
            "name_vi": "Điều ghép cao sản Ea Súp Đắk Lắk",
            "scientific_name": "Anacardium occidentale L. cv. AB05 Ea Sup",
            "dia_ban_pho_bien": ["Ea Súp", "Buôn Đôn", "Ea H'leo", "Đắk Lắk", "Đắk R'lấp", "Đắk Nông"],
            "dac_tinh_sinh_thai": "Cây công nghiệp xuất khẩu 'Hạt ngọc vàng' trên vùng đất khô hạn bán sa mạc biên giới Ea Súp, chịu nắng nóng hạn hán khốc liệt cực giỏi nhờ rễ cọc đâm sâu, hạt điều to tròn mẩy chắc nhân hạt béo ngậy ngọt bùi giòn rụm xuất khẩu số một thế giới.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Thán thư đen hoa cuống quả điều",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Colletotrichum gloeosporioides"
                    },
                    "trieu_chung_dien_hinh": [
                        "Chùm hoa điều xuất hiện các chấm nâu đen nhỏ li ti, sau lan nhanh làm toàn bộ hoa khô cháy đen thui rụng ráo trọi",
                        "Quả giả và hạt điều non bị đốm đen lõm sâu làm hạt teo tóp chai sượng rụng hàng loạt",
                        "Chồi non bị thâm đen cong gập hình móc câu (chết chồi)",
                        "Làm mất trắng mùa điều khi gặp các cơn mưa trái mùa vào dịp tết nguyên đán"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bọ xít muỗi chích chùm hoa: Bọ xít chích có chấm kim châm rỉ giọt nhựa trong; Nấm thán thư làm cả chùm hoa nhũn đen tóp lại và có dịch bào tử hồng cam khi trời ẩm.",
                    "kiem_tra_thuc_dia": "Lắc nhẹ chùm hoa thấy hoa đen rụng lả tả, đưa quả non thâm đen soi kính lúp thấy các giọt nhầy bào tử màu cam hồng tiết ra ở tâm vết lõm.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt tỉa cành thông thoáng sau thu hoạch, dọn sạch cỏ rác dưới tán cây đón ánh nắng mặt trời.",
                        "sinh_hoc": "Phun phòng định kỳ chế phẩm sinh học Trichoderma kết hợp Chitosan nano kích kháng màng tế bào biểu bì hoa quả non.",
                        "khuyen_cao_chuyen_gia": "Phun phòng ngừa bằng Azoxystrobin + Difenoconazole (Amistar Top 325SC) hoặc Antracol 70WP trước khi hoa bung nở và sau khi đậu hạt non."
                    }
                },
                {
                    "ten_benh": "Bệnh Bọ xít muỗi chích chùy hoa non điều",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Côn trùng chích hút",
                        "ten_khoa_hoc": "Helopeltis theivora"
                    },
                    "trieu_chung_dien_hinh": [
                        "Bọ xít muỗi dùng vòi chích hút nhựa non ở chùy hoa, cuống quả và đọt non cây điều",
                        "Tại vết chích xuất hiện các chấm nhỏ màu nâu đen sũng nước sau khô tóp lại làm chùy hoa bị khô đen rụng sạch",
                        "Đọt non bị cháy đen cong queo, lá non bị thủng lỗ rỗ như bị đạn hoa cải bắn",
                        "Hạt điều non bị các nốt ghẻ thâm đen sần sùi chai cứng teo tóp hạt"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bệnh thán thư: Bọ xít muỗi chích để lại các chấm đen kim châm rải rác quanh cuống chồi và nhìn thấy bọ xít muỗi có kim nhọn dựng đứng trên lưng bay lượn lúc sáng sớm.",
                    "kiem_tra_thuc_dia": "Sáng sớm vạch chùm hoa thấy bọ xít muỗi có chân dài mảnh khảnh màu nâu đỏ đang chích hút chùy hoa non.",
                    "phac_do_vietgap": {
                        "canh_tac": "Phát quang bụi rậm quanh vườn điều, hun khói xua đuổi bọ xít muỗi vào sáng sớm khi điều nhú chùy hoa.",
                        "sinh_hoc": "Nuôi thả kiến vàng tự nhiên trong vườn điều để khống chế bọ xít muỗi.",
                        "khuyen_cao_chuyen_gia": "Phun trừ bằng thuốc trừ sâu sinh học Alpha-cypermethrin hoặc Abamectin vào sáng sớm hoặc chiều mát khi bọ xít muỗi hoạt động mạnh."
                    }
                }
            ]
        },
        {
            "id": "w1_112",
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": "Chanh dây tím Đắk Đoa Gia Lai",
            "scientific_name": "Passiflora edulis Sims cv. Dak Doa",
            "dia_ban_pho_bien": ["Đắk Đoa", "Mang Yang", "Chư Păh", "Gia Lai", "Đắk R'lấp", "Đắk Nông"],
            "dac_tinh_sinh_thai": "Cây ăn quả xuất khẩu chủ lực trên đất bazan Gia Lai độ cao 600 - 900m, giàn leo xanh mướt ra hoa đậu quả quanh năm, quả tròn màu tím thẫm ruột vàng ươm mọng nước chua ngọt thanh mát thơm nức mũi xuất khẩu dịch chanh dây sang châu Âu.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Bã trầu đốm dầu thối quả chanh dây",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Vi khuẩn",
                        "ten_khoa_hoc": "Pseudomonas syringae pv. passiflorae"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết bệnh ban đầu là những đốm nhỏ ngậm nước màu xanh tối như giọt dầu loang trên vỏ quả",
                        "Sau đó vết bệnh lan rộng chuyển sang màu nâu đỏ như bã trầu ăn sâu vào trong vỏ",
                        "Vỏ quả bị nhăn nheo lõm sâu, thịt dịch quả bên trong bị thối nhũn chua loãng",
                        "Lá xuất hiện các đốm góc cạnh màu bã trầu có quầng halo vàng sáng bao quanh"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Thán thư nấm: Thán thư đốm tròn đồng tâm có ổ bào tử màu hồng cam; Bã trầu vi khuẩn vết loang như giọt dầu màu nâu đỏ bã trầu viền quầng vàng sáng chói.",
                    "kiem_tra_thuc_dia": "Dùng tay ấn vào đốm bã trầu thấy vỏ lõm mềm sũng nước, ngửi thấy mùi chua ủng của dịch vi khuẩn.",
                    "phac_do_vietgap": {
                        "canh_tac": "Làm giàn chữ T hoặc giàn chữ I thông thoáng đón gió, tỉa bớt lá già rậm rạp che khuất quả.",
                        "sinh_hoc": "Phun phòng bằng vi khuẩn đối kháng Bacillus subtilis kết hợp Nano Bạc Đồng 500ppm.",
                        "khuyen_cao_chuyen_gia": "Phun phòng trừ bằng Kasugamycin (Kasumin 2SL), Oxytetracycline hoặc Bismerthiazol sau các đợt mưa bão."
                    }
                },
                {
                    "ten_benh": "Bệnh Đốm dầu loang thối tím quả chanh dây",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Phytophthora nicotianae"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết bệnh bắt đầu từ điểm tiếp xúc giữa các quả hoặc giọt nước đọng dưới dạng đốm nâu xám sũng nước",
                        "Vết thối lan cực nhanh làm toàn bộ quả chanh dây bị nhũn nát chảy nước",
                        "Bề mặt quả bị bao phủ bởi lớp màng tơ nấm màu trắng mịn như sương muối khi trời mưa dầm",
                        "Quả bị thối rụng hàng loạt lây lan khắp giàn leo"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bệnh bã trầu vi khuẩn: Vi khuẩn không sinh màng tơ nấm trắng muốt mịn màng trên vỏ quả khi trời ẩm ướt.",
                    "kiem_tra_thuc_dia": "Cầm quả chanh dây thối thấy nhũn nát chảy nước chua, lớp sợi tơ nấm trắng mịn phủ kín vết thối.",
                    "phac_do_vietgap": {
                        "canh_tac": "Tỉa bớt cành nhánh thông thoáng, khơi rãnh thoát nước luống không để đọng nước mưa.",
                        "sinh_hoc": "Phun nấm đối kháng Trichoderma kết hợp Chitosan nano kích kháng bảo vệ quả non.",
                        "khuyen_cao_chuyen_gia": "Phun phòng ngừa bằng Aliette 800WG, Ridomil Gold hoặc Mancozeb khi mưa dầm kéo dài."
                    }
                }
            ]
        },
        {
            "id": "w1_113",
            "topic": "Cay_Cong_Nghiep_Xuat_Khau",
            "name_vi": "Dâu tằm tơ Bảo Lộc Lâm Đồng",
            "scientific_name": "Morus alba L. cv. Bao Loc",
            "dia_ban_pho_bien": ["Bảo Lộc", "Lâm Hà", "Đức Trọng", "Lâm Đồng", "Đắk Nông"],
            "dac_tinh_sinh_thai": "Thủ phủ tơ tằm lớn nhất Việt Nam trên cao nguyên bazan màu mỡ mát lạnh 800 - 1.000m, lá dâu to dày mọng nước giàu protein nuôi tằm nhả tơ óng ả làm nên những tấm lụa tơ tằm Bảo Lộc trứ danh xuất khẩu toàn cầu.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Đốm trắng lá dâu tằm",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Pseudocercospora mori"
                    },
                    "trieu_chung_dien_hinh": [
                        "Phiến lá xuất hiện những đốm tròn nhỏ li ti màu nâu đen, sau tâm hóa xám trắng có viền nâu đỏ sẫm",
                        "Mặt dưới lá tương ứng xuất hiện các chấm mốc mịn màu tro xám",
                        "Lá dâu già bị úa vàng khô giòn mép lá rụng sớm",
                        "Lá bị nhiễm bệnh giảm sút chất lượng dinh dưỡng làm tằm ăn vào bị bệnh đường ruột không nhả tơ được"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Cháy lá sinh lý: Cháy lá sinh lý viền lá khô đều từ ngoài vào; Đốm trắng là các chấm tròn đồng tâm rải rác khắp bề mặt phiến lá.",
                    "kiem_tra_thuc_dia": "Soi lá ngược ánh sáng thấy các chấm đốm nhỏ trong suốt tâm trắng bạc viền nâu đỏ nổi bật.",
                    "phac_do_vietgap": {
                        "canh_tac": "Đốn dâu đúng thời vụ tạo tán thông thoáng, dọn sạch lá rụng dưới gốc vườn dâu.",
                        "sinh_hoc": "Phun phòng bằng chế phẩm vi sinh Bacillus subtilis kết hợp Nano Bạc Đồng 300ppm (an toàn tuyệt đối cho tằm sau 5 ngày).",
                        "khuyen_cao_chuyen_gia": "Phun phòng trừ bằng Booc-đô 1% hoặc Mancozeb giai đoạn sau khi đốn cành ra lộc non."
                    }
                },
                {
                    "ten_benh": "Bệnh Rầy bông dâu tằm tiết nhựa dính",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Côn trùng chích hút",
                        "ten_khoa_hoc": "Anomoneura mori"
                    },
                    "trieu_chung_dien_hinh": [
                        "Ấu trùng rầy bông phủ lớp sáp trắng xốp như sợi bông gòn bám dày đặc ở ngọn non và mặt dưới phiến lá",
                        "Chích hút dịch nhựa non làm lá dâu bị xoăn queo vàng úa, ngọn dâu bị chùn lại còi cọc",
                        "Tiết ra dịch mật ngọt làm nấm muội đen bồ hóng phát triển phủ kín tán lá",
                        "Lá dâu bị dính bết sáp trắng và muội đen tằm không ăn được làm thất thu sản lượng lá dâu tơ tằm"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Rệp sáp: Rầy bông có sợi sáp dài lòng thòng như bông sợi mềm mại và con trưởng thành có cánh nhảy bay tanh tách khi rung cành.",
                    "kiem_tra_thuc_dia": "Vạch ngọn non thấy các chùm sợi sáp trắng bồng bềnh như bông gòn, gạt ra thấy ấu trùng rầy màu xanh vàng bên trong.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt bỏ các ngọn dâu bị nhiễm rầy bông cho vào bao nilon đem tiêu hủy.",
                        "sinh_hoc": "Phun dầu khoáng sinh học SK Enspray 99EC loãng kết hợp nấm ký sinh Beauveria bassiana.",
                        "khuyen_cao_chuyen_gia": "Phun trừ bằng thuốc trừ sâu sinh học Abamectin khi mật độ rầy cao, cách ly ít nhất 7-10 ngày trước khi hái lá cho tằm ăn."
                    }
                }
            ]
        }
    ]
