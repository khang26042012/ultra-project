# -*- coding: utf-8 -*-
"""
Worker 1 - Part 2: Tây Bắc (Crops 26 to 37)
Sơn La, Điện Biên, Lai Châu, Hòa Bình, Lào Cai, Yên Bái
"""

def get_part2_crops():
    return [
        {
            "id": "w1_026",
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": "Mận hậu Chiềng Cọ Sơn La",
            "scientific_name": "Prunus salicina Lindl. cv. Chieng Co",
            "dia_ban_pho_bien": ["Chiềng Cọ", "Mộc Châu", "Sơn La", "Bắc Hà", "Lào Cai"],
            "dac_tinh_sinh_thai": "Cây ăn quả ôn đới vùng núi cao 600 - 1.200m, cần thời gian tích lũy nhiệt độ thấp mùa đông (< 7.2 độ C đủ 300-400 giờ) để phân hóa mầm hoa rực rỡ, đất mùn Feralit đỏ vàng trên đá vôi thoát nước tốt, pH 5.5 - 6.5.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Thủng lá đốm nâu vi khuẩn mận hậu",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Vi khuẩn",
                        "ten_khoa_hoc": "Xanthomonas arboricola pv. pruni"
                    },
                    "trieu_chung_dien_hinh": [
                        "Trên lá: Vết bệnh ban đầu là chấm nhỏ ngậm nước ở mặt dưới lá, sau chuyển thành đốm nâu tím góc cạnh đường kính 1-3mm",
                        "Phần mô hoại tử khô teo và tách rời rụng ra ngoài để lại vô số lỗ thủng tròn méo mó như bị đạn súng hoa cải bắn thủng",
                        "Trên quả mận: Vết bệnh là những nốt nứt nẻ sần sùi màu đen lõm sâu rỉ giọt gôm mủ trong suốt",
                        "Cành non xuất hiện các vệt loét nứt vỏ màu nâu tím làm cành khô chết ngọn"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Bệnh thủng lá do nấm Clasterosporium: Bệnh vi khuẩn có quầng halo vàng mỏng ngậm nước và vết loét trên quả nứt toác chảy mủ kẹo dẻo; Nấm Clasterosporium vết đốm tròn có quầng đỏ tươi bao quanh và không có dịch khuẩn nhờn.",
                    "kiem_tra_thuc_dia": "Cầm phiến lá soi ngược ánh nắng thấy rõ các lỗ thủng viền nâu tím sắc cạnh, sờ mặt quả thấy cộm ráp vảy nứt gôm dính.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt tỉa cành la, cành khô sau thu hoạch giúp tán cây hứng trọn ánh nắng vùng cao, khử trùng kéo cắt cành bằng cồn.",
                        "sinh_hoc": "Phun phòng định kỳ bằng Bacillus subtilis chủng chuyên tính kết hợp dung dịch Nano Đồng hữu cơ 400ppm.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bằng hoạt chất Kasugamycin (Kasumin 2SL), Oxytetracycline hoặc Bordeaux 1% vào giai đoạn sau đốn tỉa và trước khi hoa nở bung."
                    }
                },
                {
                    "ten_benh": "Bệnh Xì gôm chảy nhựa cành mận hậu",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Leucostoma cinctum (Valsa cincta) / Botryosphaeria dothidea"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vỏ thân và cành mẹ bị nứt nẻ, chảy ra các cục gôm nhựa màu vàng hổ phách hoặc nâu sẫm dẻo quánh",
                        "Mô vỏ dưới vết gôm bị thối nâu đen, khô lại và bong tróc làm tắc hoàn toàn dòng nhựa luyện nuôi cành",
                        "Lá trên cành bị héo rũ vàng úa đột ngột, quả non trên cành teo quắt teo tóp dính chặt trên cây",
                        "Cành mận bị chết khô giòn dễ gãy trong mùa đông sương muối"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Xì gôm sinh lý do thừa nước hay sốc nhiệt: Xì gôm sinh lý vỏ thân bên dưới vẫn tươi trắng không bị hoại tử thối nâu; Xì gôm do nấm mô vỏ bên dưới thối đen mục rỗng có các ổ nấm đen li ti.",
                    "kiem_tra_thuc_dia": "Lấy dao gạt cục gôm nhựa thấy vết nứt sâu vào tận lớp gỗ, mô gỗ xung quanh đổi màu nâu xám sũng nước.",
                    "phac_do_vietgap": {
                        "canh_tac": "Quét vôi trắng trộn thuốc trừ nấm gốc đồng vào thân cây cao 1m trước mùa đông sương muối để chống nứt vỏ thân.",
                        "sinh_hoc": "Cạo sạch cục gôm nhựa và mô vỏ thối rồi quét chế phẩm nấm đối kháng Chaetomium kết hợp Chitosan đặc.",
                        "khuyen_cao_chuyen_gia": "Phun và quét vết thương bằng Thiophanate-Methyl, Tebuconazole hoặc Booc-đô 2%."
                    }
                }
            ]
        },
        {
            "id": "w1_027",
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": "Sơn tra Tây Bắc / Táo mèo Mù Cang Chải",
            "scientific_name": "Docynia indica (Wall.) Decne.",
            "dia_ban_pho_bien": ["Mù Cang Chải", "Yên Bái", "Bắc Yên", "Sơn La", "Mường Tè", "Lai Châu"],
            "dac_tinh_sinh_thai": "Cây gỗ bán rụng lá mọc hoang dã và trồng thành rừng ở độ cao 1.000 - 2.500m, chịu được băng giá sương muối mùa đông Tây Bắc, đất dốc sườn núi Feralit mùn thô giàu chất hữu cơ, quả có vị chua chát thanh ngọt rất giàu tanin và flavonoid quý.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Gỉ sắt táo mèo đốm cam rực rỡ",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Gymnosporangium yamadae"
                    },
                    "trieu_chung_dien_hinh": [
                        "Mặt trên phiến lá xuất hiện các đốm tròn màu vàng cam sáng rực rỡ rực lửa, ở giữa có các chấm đen li ti",
                        "Mặt dưới lá tương ứng sưng gồ lên thành các cụm gai nhọn hình ống tua tủa màu nâu xám giải phóng bụi phấn nấm",
                        "Quả non bị nhiễm bệnh sưng u méo mó, trên vỏ quả mọc các túm gai ống màu cam làm rụng quả hàng loạt",
                        "Cây bị rụng lá trơ trụi cành giảm năng suất và phẩm chất quả ngâm rượu"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Bệnh đốm mắt chim: Đốm mắt chim vết phẳng lì tâm xám tro viền nâu; Bệnh gỉ sắt Gymnosporangium mặt dưới sưng u nhô các tua ống gai nhọn đặc thù như lông nhím.",
                    "kiem_tra_thuc_dia": "Lật mặt dưới lá thấy các túm sợi gai nhọn hình trụ dài 2-4mm tua tủa, sờ vào thấy bóp ra bột phấn màu vàng cam sáng.",
                    "phac_do_vietgap": {
                        "canh_tac": "Chặt bỏ các bụi cây bách, trắc bách diệp mọc gần vườn táo mèo (vì nấm gỉ sắt ký sinh chuyển vật chủ qua lại giữa táo mèo và cây bách).",
                        "sinh_hoc": "Phun chế phẩm Nano Bạc Đồng 500ppm kết hợp Chitosan bảo vệ bề mặt lộc non lúc nhú mầm hoa.",
                        "khuyen_cao_chuyen_gia": "Phun trừ bằng hoạt chất Difenoconazole, Tebuconazole hoặc Myclobutanil khi vừa kết thúc đợt hoa nở rộ."
                    }
                },
                {
                    "ten_benh": "Bệnh Ghẻ sẹo quả táo mèo (Bệnh vảy quả sơn tra)",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Venturia inaequalis f. sp. docyniae"
                    },
                    "trieu_chung_dien_hinh": [
                        "Trên lá: Vết bệnh màu xanh ô liu dạng nhung mịn, sau chuyển thành đốm đen xám cứng",
                        "Trên quả: Xuất hiện các vết sẹo tròn sần sùi màu nâu đen hóa bần cứng ngắc như vảy cóc",
                        "Vỏ quả bị nứt toác theo các vệt ghẻ sẹo, quả méo mó cằn cỗi tích tụ nhiều vị chát đắng",
                        "Quả bị thối rụng khi gặp mưa ẩm kéo dài vùng núi cao"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Trầy xước do gió va đập vào gai cành: Trầy xước cơ giới vết phẳng liền sẹo màu trắng xám không có lớp nhung nấm ô liu; Bệnh ghẻ vảy nấm sần sùi gồ ghề viền nứt toác có tơ nấm mịn màu xanh đen ô liu.",
                    "kiem_tra_thuc_dia": "Lấy móng tay cạo nhẹ mảng ghẻ thấy lớp vỏ bần cứng bong ra, bên dưới mô thịt quả sượng chai cứng.",
                    "phac_do_vietgap": {
                        "canh_tac": "Thu gom lá rụng và quả rụng bị bệnh đem chôn sâu tiêu hủy nguồn bào tử nang qua đông.",
                        "sinh_hoc": "Phun phòng bằng men vi sinh đối kháng Bacillus subtilis định kỳ hàng tháng.",
                        "khuyen_cao_chuyen_gia": "Phun luân phiên Mancozeb, Difenoconazole hoặc Kresoxim-methyl giai đoạn quả non bằng ngón tay."
                    }
                }
            ]
        },
        {
            "id": "w1_028",
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": "Xoài tròn Yên Châu Sơn La",
            "scientific_name": "Mangifera indica L. cv. Tron Yen Chau",
            "dia_ban_pho_bien": ["Yên Châu", "Mai Sơn", "Sơn La", "Mường La"],
            "dac_tinh_sinh_thai": "Giống xoài bản địa độc đáo quả nhỏ tròn xoe vỏ xanh bóng thịt vàng rực thơm ngào ngạt, ưa thung lũng khô nóng đặc trưng của lòng chảo Yên Châu, đất Feralit trên nền đá vôi giàu canxi, chịu hạn chịu gió lào khô nóng cực giỏi.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Thán thư đen hoa và quả non xoài tròn",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Colletotrichum acutatum / Colletotrichum gloeosporioides"
                    },
                    "trieu_chung_dien_hinh": [
                        "Chùm hoa xoài bị các chấm đen nhỏ li ti, sau lan nhanh làm toàn bộ hoa khô cháy đen thui rụng ráo trọi",
                        "Quả non bị đốm đen lõm sâu làm quả rụng hàng loạt hoặc quả lớn bị méo mó thâm đen vỏ",
                        "Lá non xuất hiện các đốm góc cạnh màu nâu đen thủng rách phiến lá",
                        "Trên quả chín xuất hiện các đốm đen tròn đồng tâm thịt quả bên dưới bị thối nhũn chua"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Bọ trĩ chích hút hoa xoài: Bọ trĩ làm hoa khô teo màu nâu nhạt không có đốm đen lõm sâu và không tiết chất nhầy bào tử hồng cam khi trời mưa ẩm.",
                    "kiem_tra_thuc_dia": "Lắc nhẹ chùm hoa thấy hoa đen rụng lả tả, đưa quả non thâm đen soi kính lúp thấy các giọt nhầy bào tử màu cam hồng tiết ra ở tâm vết lõm.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt tỉa cành thông thoáng sau thu hoạch, dọn sạch cỏ rác dưới tán cây đón nắng gió khô nóng lòng chảo Yên Châu.",
                        "sinh_hoc": "Phun phòng định kỳ chế phẩm sinh học Trichoderma kết hợp Chitosan nano kích kháng màng tế bào biểu bì hoa quả non.",
                        "khuyen_cao_chuyen_gia": "Phun phòng ngừa bằng Azoxystrobin + Difenoconazole (Amistar Top 325SC) hoặc Antracol 70WP trước khi hoa bung nở và sau khi đậu quả non."
                    }
                },
                {
                    "ten_benh": "Bệnh Đốm vi khuẩn chảy mủ đen cành lá xoài tròn",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Vi khuẩn",
                        "ten_khoa_hoc": "Xanthomonas campestris pv. mangiferaeindicae"
                    },
                    "trieu_chung_dien_hinh": [
                        "Trên lá: Vết bệnh là những đốm nhỏ góc cạnh màu đen nổi gồ lên như mắt cua, có quầng sáng vàng bao quanh",
                        "Trên cành non: Vết nứt dọc màu nâu đen rỉ giọt dịch mủ vi khuẩn màu đen dính nhớt",
                        "Trên vỏ quả: Vết bệnh nứt nẻ hình sao màu đen sâu hoại tử mô thịt quả",
                        "Bệnh lây lan rất nhanh theo các vết thương cơ giới sau những trận giông gió lốc mùa hè"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Thán thư: Vết vi khuẩn nổi gồ như vảy mụn có quầng vàng trong suốt và vết nứt vỏ hình sao chảy mủ đen; Thán thư vết lõm sâu đồng tâm không có mủ đen nhờn.",
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
            "id": "w1_029",
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": "Nhãn ghép Sông Mã Sơn La",
            "scientific_name": "Dimocarpus longan Lour. cv. Song Ma",
            "dia_ban_pho_bien": ["Sông Mã", "Sốp Cộp", "Mai Sơn", "Sơn La", "Điện Biên"],
            "dac_tinh_sinh_thai": "Cây ăn quả chủ lực ven sông Mã biên giới Việt Lào, đất phù sa bãi bồi ven sông pha cát sỏi thoát nước cực nhanh, tiểu khí hậu nhiệt đới gió mùa núi cao nắng nhiều biên độ nhiệt ngày đêm lớn giúp cùi nhãn dày, giòn ráo nước và ngọt lịm.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Sương mai hoa mốc trắng nhãn Sông Mã",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Peronophythora litchii"
                    },
                    "trieu_chung_dien_hinh": [
                        "Chùm hoa nhãn bị sũng nước chuyển màu nâu đen, khi trời sương mù ẩm phủ lớp màng mốc trắng như bột sương",
                        "Hoa rụng trắng gốc, chùm hoa trơ cuống đen sì không đậu được quả nào",
                        "Quả non bị thối nâu từ cuống quả lan rộng ra vỏ làm quả non rụng hàng loạt",
                        "Lá non bị thâm tím khô giòn mép lá"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Cháy hoa do sương muối: Sương muối làm cháy khô vàng đồng loạt toàn bộ hoa trong một đêm; Sương mai nấm lây lan từ từ có màng mốc trắng ẩm ướt bao bọc từng nhánh hoa.",
                    "kiem_tra_thuc_dia": "Sáng sớm có sương, vạch chùm hoa thấy lớp nấm trắng mịn như bột mì phủ quanh cuống hoa mềm nhũn.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt tỉa cành thông thoáng, hun khói xua sương muối và tăng nhiệt độ vườn nhãn vào rạng sáng.",
                        "sinh_hoc": "Phun dịch chiết vỏ tôm Chitosan nano 2% kích thích tính kháng bệnh của cánh hoa và quả non.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bằng Ridomil Gold 68WG (Metalaxyl-M + Mancozeb) hoặc Aliette 800WG trước khi hoa nở 7 ngày."
                    }
                },
                {
                    "ten_benh": "Bệnh Đốm xám vỏ quả xơ chai nhãn",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Pestalotiopsis longanae"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vỏ quả nhãn xuất hiện những đốm tròn màu xám tro viền nâu đen",
                        "Vỏ quả dưới vết đốm bị chai cứng nứt nẻ, cùi nhãn teo dính sát vào vỏ khó bóc",
                        "Thịt cùi bị mất nước khô xơ, vị nhạt nhẽo biến chất",
                        "Lá già xuất hiện các vệt cháy loang lổ màu xám bạc thủng lỗ chỗ"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Vỏ sém nắng sinh lý: Sém nắng vỏ có mảng vàng nâu khô phẳng chỉ ở phía hứng nắng; Đốm xám nấm xuất hiện ở cả mặt khuất bóng có chấm đen bào tử li ti.",
                    "kiem_tra_thuc_dia": "Bóc quả nhãn thấy vỏ dính chặt vào cùi thịt ở vết đốm xám, mô cùi bị teo khô màu nâu nhạt.",
                    "phac_do_vietgap": {
                        "canh_tac": "Bao chùm quả bằng túi lưới chuyên dụng, bón phân cân đối N-P-K bổ sung thêm Canxi và Silic sinh học làm dày vỏ quả.",
                        "sinh_hoc": "Phun chế phẩm vi sinh Bacillus subtilis phòng trừ mầm nấm bề mặt quả.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bằng Difenoconazole, Tebuconazole hoặc Antracol 70WP giai đoạn quả bắt đầu vào đường."
                    }
                }
            ]
        },
        {
            "id": "w1_030",
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": "Mắc cọp rừng Sa Pa / Bát Xát",
            "scientific_name": "Pyrus pyrifolia (Burm.f.) Nakai",
            "dia_ban_pho_bien": ["Sa Pa", "Bát Xát", "Lào Cai", "Sơn La", "Hà Giang"],
            "dac_tinh_sinh_thai": "Giống lê rừng bản địa vùng núi cao hiểm trở Hoàng Liên Sơn (> 1.200m), vỏ quả màu nâu đốm hạt cát sần sùi giòn tan mọng nước chua ngọt thanh mát, cây cực kỳ khỏe mạnh chịu rét và sương giá giỏi.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Đốm đen đốm sao lá lê rừng (Bệnh Alternaria lê)",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Alternaria kikuchiana"
                    },
                    "trieu_chung_dien_hinh": [
                        "Phiến lá xuất hiện những đốm đen tròn nhỏ, sau lan rộng thành hình sao góc cạnh màu nâu đen đồng tâm",
                        "Xung quanh vết đốm có quầng vàng nhạt, mô lá bị khô rách thủng lỗ",
                        "Lá già bị úa vàng rụng sớm hàng loạt vào giữa mùa hè làm trơ cành cây",
                        "Quả non bị đốm đen lõm sâu nứt toác chảy dịch quả làm quả còi cọc chai sần"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Đốm gỉ sắt: Gỉ sắt có cụm mụn gai màu vàng cam mặt dưới lá; Đốm Alternaria màu đen xám phẳng lì có vòng đồng tâm rách thủng.",
                    "kiem_tra_thuc_dia": "Lấy tay bóp nhẹ vào đốm đen trên quả thấy vỏ lõm cứng có vết nứt hình chữ thập hoặc hình sao.",
                    "phac_do_vietgap": {
                        "canh_tac": "Thu gom lá rụng và quả thối đem chôn sâu, đốn tỉa cành tăm cành sâu bệnh sau vụ hái quả.",
                        "sinh_hoc": "Phun phòng men vi sinh Chaetomium kết hợp Nano Bạc Đồng 400ppm định kỳ hàng tháng.",
                        "khuyen_cao_chuyen_gia": "Phun luân phiên Difenoconazole, Polyoxin AL hoặc Iprodione khi cây vừa nhú đợt lộc xuân."
                    }
                },
                {
                    "ten_benh": "Bệnh Rỉ sắt nấm chén quả và lá lê rừng",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Gymnosporangium haraeanum"
                    },
                    "trieu_chung_dien_hinh": [
                        "Mặt trên lá xuất hiện các đốm vàng cam rực rỡ có các chấm đen li ti",
                        "Mặt dưới lá sưng phồng lên tạo thành các túm ống hình chén tua tủa màu xám nâu giải phóng bụi phấn vàng",
                        "Quả non mắc cọp bị dị dạng méo mó, mọc các u nhú gỉ sắt làm quả rụng non",
                        "Cuống quả và cành non bị sưng gồ cong queo dễ gãy"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bệnh đốm mắt cua: Mắt cua không bao giờ có các cụm nấm hình ống chén tua tủa nhô cao ở mặt dưới lá như gỉ sắt Gymnosporangium.",
                    "kiem_tra_thuc_dia": "Lật mặt dưới lá thấy các ống gai nấm chén mọc chùm tua tủa dài 2-3mm, xoa tay thấy bụi bột cam vàng bay ra.",
                    "phac_do_vietgap": {
                        "canh_tac": "Tránh trồng lê rừng gần các đồi cây tùng bách (vật chủ phụ của nấm rỉ sắt).",
                        "sinh_hoc": "Phun phòng dịch chiết tỏi ớt kết hợp tinh dầu quế sinh học xua đuổi bào tử nấm.",
                        "khuyen_cao_chuyen_gia": "Phun phòng ngừa bằng Myclobutanil, Hexaconazole hoặc Tebuconazole khi lộc non mới bung nở."
                    }
                }
            ]
        },
        {
            "id": "w1_031",
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": "Đào phai Mộc Châu Sơn La",
            "scientific_name": "Prunus persica (L.) Batsch cv. Phai Moc Chau",
            "dia_ban_pho_bien": ["Mộc Châu", "Vân Hồ", "Sơn La", "Sa Pa", "Lào Cai"],
            "dac_tinh_sinh_thai": "Cây ăn quả và hoa cảnh ôn đới nức tiếng thảo nguyên Mộc Châu (cao 1.050m), ưa đất Feralit nâu đỏ bazan màu mỡ tơi xốp, thời tiết đông chí rét căm căm giúp hoa đào phai cánh dày thắm sắc và quả đào lông giòn ngọt thơm nức mũi.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Xoăn phồng đỏ lá đào (Bệnh quăn lá Taphrina)",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Taphrina deformans"
                    },
                    "trieu_chung_dien_hinh": [
                        "Lá non mới nhú bị dày cộm lên bất thường, nhăn nheo, xoăn tít vặn vẹo biến dạng hoàn toàn",
                        "Phiến lá phồng rộp chuyển từ màu xanh nõn chuối sang màu đỏ tươi hoặc đỏ tía rực rỡ",
                        "Về sau bề mặt lá phồng rộp phủ lớp màng mốc màu xám bạc xỉn, lá khô giòn chuyển màu nâu và rụng hàng loạt",
                        "Chồi non bị chùn lại phình to mềm yếu, hoa đào bị thui chột không đậu được quả non"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Bọ trĩ hay Rầy mềm chích hút làm xoăn lá: Côn trùng chích hút làm mép lá xoăn quăn queo nhưng phiến lá vẫn mỏng manh và không phồng rộp biến thành màu đỏ tươi; Nấm Taphrina làm mô tế bào lá phì đại dày cộp gấp 3-4 lần và chuyển màu đỏ rực rỡ đặc trưng.",
                    "kiem_tra_thuc_dia": "Lấy tay sờ vào lá đào thấy dày cộp, giòn cứng, phiến lá phồng rộp như da cóc màu đỏ tía, vò nhẹ thấy gãy giòn mọng nước.",
                    "phac_do_vietgap": {
                        "canh_tac": "Ngắt bỏ và tiêu hủy ngay các chồi lá xoăn phồng màu đỏ khi vừa chớm xuất hiện đầu xuân.",
                        "sinh_hoc": "Phun phòng bằng chế phẩm vi sinh Bacillus amyloliquefaciens kết hợp Nano Đồng sinh học trước khi cây nảy lộc.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bắt buộc vào giai đoạn ngủ đông (rụng sạch lá) và trước khi mầm hoa nứt vỏ bằng Bordeaux 2%, Chlorothalonil hoặc Difenoconazole."
                    }
                },
                {
                    "ten_benh": "Bệnh Thối nâu hoa quả đào mốc xám",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Monilinia fructicola"
                    },
                    "trieu_chung_dien_hinh": [
                        "Hoa đào bị thâm nâu héo rũ dính bết vào cành như bị luộc nước sôi",
                        "Trên quả đào non và quả chín xuất hiện vết đốm tròn màu nâu nhạt lan cực nhanh ra toàn bộ quả",
                        "Trên vết thối xuất hiện các đệm nấm màu xám tro hoặc nâu nhạt xếp thành các vòng tròn đồng tâm",
                        "Quả bị thối nhũn sau đó khô quắt lại thành các 'quả xác ướp' màu đen cứng dính chặt trên cành cây"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Thối nhũn do vi khuẩn Rhizopus: Rhizopus sợi nấm bồng bềnh như bông chấm đen li ti thối chảy nước nhanh; Monilinia tạo các đệm nấm tro xám dạng bột hạt xếp vòng đồng tâm hoàn hảo và làm quả teo quắt xác ướp.",
                    "kiem_tra_thuc_dia": "Cầm quả đào thối thấy các vòng đệm nấm xám tro tròn đồng tâm, bóp nhẹ thấy thịt quả bên dưới mềm nhão lên men.",
                    "phac_do_vietgap": {
                        "canh_tac": "Thu dọn sạch toàn bộ quả xác ướp khô đen còn treo trên cành hoặc rơi dưới gốc đem chôn sâu tiêu hủy.",
                        "sinh_hoc": "Phun chế phẩm Nano Bạc Chitosan phòng trừ mầm nấm hoa và quả non.",
                        "khuyen_cao_chuyen_gia": "Phun phòng ngừa bằng Tebuconazole, Cyprodinil hoặc Iprodione giai đoạn hoa nở rộ và 2 tuần trước khi thu hoạch."
                    }
                }
            ]
        },
        {
            "id": "w1_032",
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": "Chanh leo ngọt Mộc Châu",
            "scientific_name": "Passiflora ligularis Juss.",
            "dia_ban_pho_bien": ["Mộc Châu", "Yên Châu", "Sơn La", "Sa Pa", "Lào Cai"],
            "dac_tinh_sinh_thai": "Cây chanh leo vỏ vàng hạt ngọt thơm mùi hoa quả cao cấp, sinh trưởng tối ưu ở độ cao 800 - 1.400m khí hậu mát mẻ, đất Feralit tơi xốp giàu mùn thoát nước nhanh, giàn leo thông thoáng.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Cứng quả đốm dầu virus chanh leo",
                    "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
                    "tac_nhan": {
                        "loai": "Virus",
                        "ten_khoa_hoc": "Passion fruit woodiness virus (PWV)",
                        "vector_truyen_benh": "Rệp muội (Aphis gossypii, Myzus persicae)"
                    },
                    "trieu_chung_dien_hinh": [
                        "Lá chanh leo bị khảm đốm vàng loang lổ xen kẽ xanh đậm, phiến lá gồ ghề dày cộp xoăn mép",
                        "Quả bị biến dạng dị dạng méo mó gồ ghề u nốt như quả cóc",
                        "Vỏ quả chai cứng như gỗ đá, vỏ rất dày trong khi ruột rỗng lép không có dịch mật ngọt",
                        "Dây leo bị chùn đọt ngừng vươn cành, cây suy tàn nhanh chóng"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Thiếu Bo làm méo quả: Thiếu Bo quả méo cục bộ nhưng lá không bị khảm vàng gồ ghề dày cộp; Nhiễm virus PWV lá khảm vàng biến dạng rất nặng và vỏ quả hóa gỗ cứng ngắc toàn bộ.",
                    "kiem_tra_thuc_dia": "Dùng dao bổ quả chanh leo thấy vỏ quả dày cộp xơ cứng như gỗ lim, ruột quả khô khốc teo tóp không có nước cốt thơm.",
                    "phac_do_vietgap": {
                        "canh_tac": "Chặt bỏ nhổ gốc cây bệnh nặng cho vào bao nilon đem đốt tiêu hủy; dùng cây giống sạch bệnh nuôi cấy mô.",
                        "sinh_hoc": "Nuôi bọ rùa ăn rệp, phun dầu khoáng sinh học SK Enspray 99EC diệt rệp muội vector truyền bệnh.",
                        "khuyen_cao_chuyen_gia": "Phun trừ côn trùng chích hút bằng Abamectin hoặc Spirotetramat khi phát hiện rệp muội ở đọt non."
                    }
                },
                {
                    "ten_benh": "Bệnh Thối thân cổ rễ chanh leo tím",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Fusarium solani f. sp. passiflorae / Phytophthora nicotianae"
                    },
                    "trieu_chung_dien_hinh": [
                        "Phần cổ rễ sát mặt đất và gốc thân dây leo bị úng nước thâm đen, vỏ rễ nứt mục tróc mảng",
                        "Lá trên toàn giàn bị héo rũ xanh rất nhanh, lá héo rũ nhưng vẫn bám chặt trên giàn",
                        "Cắt ngang phần gốc thân thấy mạch dẫn bị thâm nâu tím bốc mùi chua nồng",
                        "Hệ rễ cọc và rễ tơ bị thối mục mủn nát, dây leo chết đứng hàng loạt"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bệnh héo vi khuẩn (Ralstonia): Héo vi khuẩn khi cắt ngang gốc nhúng vào ly nước trong thấy giọt dịch khuẩn màu trắng đục tuôn ra như khói thuốc lá; Nấm Fusarium không có dịch khuẩn tuôn ra mà chỉ có mạch thâm tím sẫm.",
                    "kiem_tra_thuc_dia": "Dùng móng tay cạo nhẹ phần gốc sát mặt đất thấy vỏ tróc lở từng mảng mục nát, mô gỗ bên dưới có màu nâu đen thâm sẫm.",
                    "phac_do_vietgap": {
                        "canh_tac": "Lên giàn cao ráo, tạo rãnh thoát nước sâu giữa các hàng chanh leo, không vun đất quá cao trùm kín cổ rễ.",
                        "sinh_hoc": "Tưới gốc hỗn hợp nấm đối kháng Trichoderma kết hợp vi khuẩn Bacillus subtilis định kỳ 20 ngày/lần.",
                        "khuyen_cao_chuyen_gia": "Tưới gốc bằng Phosphonate sinh học hoặc Ridomil Gold 68WG ngay khi chớm có dấu hiệu héo đọt non."
                    }
                }
            ]
        },
        {
            "id": "w1_033",
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": "Dâu tây giống Chika Mộc Châu",
            "scientific_name": "Fragaria × ananassa Duchesne cv. Chika",
            "dia_ban_pho_bien": ["Mộc Châu", "Vân Hồ", "Sơn La", "Sa Pa", "Lào Cai"],
            "dac_tinh_sinh_thai": "Giống dâu tây Nhật Bản cao cấp trồng trên giá thể xơ dừa hữu cơ nhà màng công nghệ cao Mộc Châu, ưa nhiệt độ mát mẻ 15-22 độ C, chênh lệch nhiệt ngày đêm lớn giúp quả đỏ mọng nước, thơm lừng vị ngọt thanh đậm đà.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Mốc xám thối quả dâu tây (Bệnh thối Botrytis)",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Botrytis cinerea"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết bệnh bắt đầu từ đài hoa hoặc điểm tiếp xúc giữa quả với giá thể ướt dưới dạng chấm nâu nhạt sũng nước",
                        "Vết thối lan cực nhanh làm toàn bộ quả dâu tây bị nhũn nát chảy nước",
                        "Bề mặt quả bị bao phủ bởi một lớp nấm mốc màu xám tro dày đặc bồng bềnh",
                        "Khi chạm vào hoặc có gió thổi, lớp phấn mốc xám bay mù mịt phát tán bào tử lây nhiễm khắp luống dâu"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Thối da nấm Phytophthora: Phytophthora quả bị dai dai màu nâu da bò không có mốc xám tro bồng bềnh; Botrytis quả thối mềm chảy nước nhũn và phủ lớp lông mốc xám tro dày cộp.",
                    "kiem_tra_thuc_dia": "Lấy tay khẽ chạm vào quả dâu thối thấy bột bụi phấn xám tro bay ra như khói bụi, quả dâu bên dưới xẹp nhão nhoét.",
                    "phac_do_vietgap": {
                        "canh_tac": "Trải màng phủ nông nghiệp hoặc nâng quả trên lưới giá thể không để quả chạm đất/giá thể ẩm ướt; ngắt bỏ quả hoa thối ngay lập tức.",
                        "sinh_hoc": "Phun phòng nấm đối kháng Trichoderma harzianum hoặc vi khuẩn Bacillus subtilis chuyên tính.",
                        "khuyen_cao_chuyen_gia": "Phun luân phiên Iprodione (Rovral 50WP), Fenhexamid hoặc Boscalid giai đoạn ra hoa rộ cách ly nghiêm ngặt 3 ngày trước hái."
                    }
                },
                {
                    "ten_benh": "Bệnh Phấn trắng lá quả dâu tây",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Podosphaera aphanis"
                    },
                    "trieu_chung_dien_hinh": [
                        "Mặt dưới lá dâu tây xuất hiện những đốm trắng mỏng manh như bột phấn, sau lan ra mặt trên phiến lá",
                        "Mép phiến lá bị cuộn ngược lên trên làm lộ rõ mặt dưới phủ phấn trắng xóa",
                        "Hoa bị lớp phấn trắng bọc kín làm thâm đen khô héo không thụ phấn được",
                        "Quả non bị bao phủ bởi lớp phấn trắng, quả bị chai sượng sần sùi không lớn được và chín ép"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Nhện đỏ cắn hại: Nhện đỏ làm lá lốm đốm trắng li ti có màng tơ mỏng không cuộn cong mép lá hình lòng chảo; Phấn trắng lá cuộn ngược mép lộ màng bột trắng xóa.",
                    "kiem_tra_thuc_dia": "Lật phiến lá dâu thấy mép lá cong cong hình lòng máng, bề mặt phủ lớp bột trắng mịn xoa tay thấy dính bột.",
                    "phac_do_vietgap": {
                        "canh_tac": "Hạ độ ẩm nhà màng thông gió tối đa, duy trì khoảng cách chậu thông thoáng đón nắng.",
                        "sinh_hoc": "Phun phòng dung dịch baking soda sinh học loãng 0.3% hoặc chế phẩm nấm đối kháng Ampelomyces quisqualis.",
                        "khuyen_cao_chuyen_gia": "Phun luân phiên Difenoconazole, Myclobutanil hoặc Azoxystrobin định kỳ 10 ngày trong điều kiện hanh khô mát mẻ."
                    }
                }
            ]
        },
        {
            "id": "w1_034",
            "topic": "Cay_Cong_Nghiep_Xuat_Khau",
            "name_vi": "Chè tuyết Suối Giàng cổ thụ Yên Bái",
            "scientific_name": "Camellia sinensis var. assamica (J.W.Mast.) Kitam.",
            "dia_ban_pho_bien": ["Văn Chấn", "Suối Giàng", "Yên Bái", "Tủa Chùa", "Điện Biên"],
            "dac_tinh_sinh_thai": "Cây chè Shan tuyết cổ thụ hàng trăm năm tuổi cao lớn như cổ thụ ở độ cao 1.300 - 1.800m quanh năm mây mù bao phủ, đất mùn trên núi đá tơi xốp giàu khoáng chất tự nhiên, búp chè phủ lớp lông tơ trắng muốt như tuyết đượm hương vị đại ngàn.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Phồng lá chè búp tuyết",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Exobasidium vexans"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết bệnh bắt đầu từ các chấm nhỏ trong suốt như giọt sương trên phiến lá non và búp tôm",
                        "Mô lá bị sưng phồng lên tạo thành các đốm lõm ở mặt trên và lồi phồng ở mặt dưới như chiếc chén úp",
                        "Vết phồng chuyển sang màu trắng sữa phủ lớp bột phấn mịn như nhung (chính là lớp bào tử nấm)",
                        "Búp chè bị dị dạng biến chất thâm đen khô héo làm mất trắng phẩm chất chè búp tuyết đặc sản"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bệnh sùi cành nốt sần vi khuẩn: Vi khuẩn sùi cành làm sùi u cục cứng ở vỏ cành gỗ; Nấm Exobasidium chỉ tấn công lá non búp non làm phiến lá phồng rộp mọng nước có lớp bột trắng nhung như phấn bánh bao.",
                    "kiem_tra_thuc_dia": "Lấy tay bóp vết phồng trên lá non thấy giòn mềm mọng nước, bột phấn trắng mịn dính vào tay mát lạnh.",
                    "phac_do_vietgap": {
                        "canh_tac": "Hái chạy búp chè đúng lứa không để búp quá lứa, phát quang cây bụi che rợp quanh gốc cổ thụ.",
                        "sinh_hoc": "Phun phòng bằng chế phẩm Nano Bạc Đồng 500ppm kết hợp Chitosan bảo vệ bề mặt búp tuyết an toàn cho trà hữu cơ.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bằng Bordeaux 1% hoặc đồng sinh học Copper Oxychloride khi sương mù ẩm ướt kéo dài."
                    }
                },
                {
                    "ten_benh": "Bệnh Chấm xám đốm mắt cua búp chè cổ thụ",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Pestalotiopsis theae"
                    },
                    "trieu_chung_dien_hinh": [
                        "Phiến lá xuất hiện những đốm tròn màu nâu xám có vân đồng tâm gợn sóng rõ rệt",
                        "Tâm vết bệnh hóa màu xám tro bạc, rải rác có các chấm đen li ti là ổ bào tử nấm",
                        "Mép và chóp lá bị cháy khô cong queo giòn rách",
                        "Cành búp chè bị còi cọc đâm chồi chậm làm giảm năng suất thu hái chè búp"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Cháy nắng lá chè: Cháy nắng vết màu vàng rơm đồng nhất không có vân đồng tâm và không có chấm đen li ti ổ bào tử nấm.",
                    "kiem_tra_thuc_dia": "Vò nhẹ vết đốm xám trên lá thấy giòn vụn, soi kính lúp thấy các chấm đen nhỏ nổi gồ trên nền lá bạc.",
                    "phac_do_vietgap": {
                        "canh_tac": "Đốn tỉa cành thông thoáng vào mùa đông, bón bổ sung phân hữu cơ vi sinh và bột đá vôi tự nhiên.",
                        "sinh_hoc": "Phun phòng nấm đối kháng Bacillus subtilis định kỳ 15 ngày/lần.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bằng Antracol 70WP hoặc Difenoconazole giai đoạn sau đốn lộc non."
                    }
                }
            ]
        },
        {
            "id": "w1_035",
            "topic": "Cay_Cong_Nghiep_Xuat_Khau",
            "name_vi": "Chè Ô Long Mộc Sương Sơn La",
            "scientific_name": "Camellia sinensis (L.) Kuntze cv. Oolong Jin Xuan",
            "dia_ban_pho_bien": ["Mộc Châu", "Vân Hồ", "Sơn La", "Bảo Lộc", "Lâm Đồng"],
            "dac_tinh_sinh_thai": "Giống chè Kim Tuyên/Thanh Tâm du nhập chế biến trà Ô Long thượng hạng, trồng trên sườn đồi cao 1.100m mát lạnh, đất Feralit bazan màu mỡ, cần thu hái búp đạt chuẩn 1 tôm 2-3 lá để lên men bán phần tạo hương sữa hoa quả độc đáo.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Thối búp nâu chè Ô Long",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Colletotrichum camelliae"
                    },
                    "trieu_chung_dien_hinh": [
                        "Búp tôm non và lá non mới mở xuất hiện các chấm nâu thâm ủng nước",
                        "Vết bệnh lan nhanh làm toàn bộ búp non bị thâm đen, khô tóp quắt queo",
                        "Lá chè già xuất hiện các mảng cháy thán thư màu nâu đỏ viền lượn sóng",
                        "Làm mất trắng lứa hái búp đặc sản, chè chế biến bị đắng khét không dậy mùi thơm"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Rầy xanh chích hút: Rầy xanh chích mép lá bị cháy khô màu vàng nâu hình tam giác (cháy bìa lá); Thán thư làm cả búp non thâm đen nhũn tóp từ đọt xuống.",
                    "kiem_tra_thuc_dia": "Cầm búp chè thối thấy mềm nhũn dính bết ngón tay, ngửi thấy mùi thối mục của mô búp bị nấm phân hủy.",
                    "phac_do_vietgap": {
                        "canh_tac": "Hái búp sạch sẽ triệt để theo chu kỳ sinh trưởng, tạo rãnh thoát nước luống chè.",
                        "sinh_hoc": "Phun Nano Bạc Đồng 500ppm kết hợp chế phẩm sinh học Chitosan kích kháng bảo vệ búp non.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bằng hoạt chất Azoxystrobin hoặc Difenoconazole ngay sau mỗi đợt hái búp 3 ngày."
                    }
                },
                {
                    "ten_benh": "Bệnh Rầy xanh chích hút búp chè Ô Long",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Côn trùng chích hút",
                        "ten_khoa_hoc": "Empoasca flavescens"
                    },
                    "trieu_chung_dien_hinh": [
                        "Mép lá chè non bị khô cháy màu vàng nâu cong queo hình chữ V hoặc hình tam giác từ mép vào trong gân",
                        "Búp chè bị cằn cỗi chùn đọt, búp ngắn tũn cứng đờ (hiện tượng búp măng tây/búp ngủ)",
                        "Lá chè già bị khô giòn mép lá, tán cây cằn cỗi trơ trụi cành",
                        "Chè mất phẩm chất nghiêm trọng, nước trà chát đắng màu đen đục"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Cháy lá do sương muối: Sương muối cháy phẳng trên mặt lá hứng gió; Rầy xanh chích mép lá quăn queo và nhìn thấy rầy non màu xanh lá chuối non bò ngang thoăn thoắt ở mặt dưới lá.",
                    "kiem_tra_thuc_dia": "Lật mặt dưới lá non vỗ nhẹ thấy những con rầy nhỏ li ti màu xanh lục bò ngang sang bên rất nhanh như con cua.",
                    "phac_do_vietgap": {
                        "canh_tac": "Hái chạy búp chè sớm diệt trừ bớt trứng rầy bám trên cuống búp.",
                        "sinh_hoc": "Phun chế phẩm nấm ký sinh côn trùng Metarhizium anisopliae kết hợp nấm Beauveria bassiana.",
                        "khuyen_cao_chuyen_gia": "Phun trừ bằng thuốc trừ sâu sinh học Abamectin hoặc Emamectin benzoate an toàn cách ly 3-5 ngày."
                    }
                }
            ]
        },
        {
            "id": "w1_036",
            "topic": "Cay_Luong_Thuc_Va_Hoa_Mau",
            "name_vi": "Gạo nếp Khẩu Tan Đón Mường Luân Điện Biên",
            "scientific_name": "Oryza sativa L. var. glutinosa cv. Khau Tan Don",
            "dia_ban_pho_bien": ["Điện Biên Đông", "Mường Luân", "Điện Biên", "Tuần Giáo"],
            "dac_tinh_sinh_thai": "Giống lúa nếp tan cổ truyền quý báu của đồng bào dân tộc Thái ven dòng sông Mã, cấy ruộng bậc thang bồi đắp phù sa đỏ màu mỡ mát lành, hạt gạo thon tròn trắng ngà như ngọc, xôi thơm nức nở để 2 ngày vẫn mềm dẻo như mới đồ.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Tiêm hạch thối thân nếp nương",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Sclerotium oryzae (Magnaporthe salvinii)"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết bệnh xuất hiện ở bẹ lá sát mặt nước ruộng bậc thang dưới dạng các chấm đen nhỏ hình bầu dục",
                        "Nấm ăn sâu vào bên trong thân lúa làm gióng thân bị thối đen mủn nát rỗng ruột",
                        "Bên trong ruột thân chứa đầy các hạch nấm tròn nhỏ li ti màu đen nhánh như hạt bụi than",
                        "Cây lúa nếp bị gãy đổ gập ngang thân sát mặt nước khi lúa đang làm đòng trỗ bông"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Sâu đục thân hại lúa: Sâu đục thân để lại lỗ đục có phân sâu mạt cưa; Bệnh tiêm hạch bẹ lá và gióng thân thối đen có vô số hạt hạch nấm đen bóng li ti bên trong ruột rỗng.",
                    "kiem_tra_thuc_dia": "Bẻ đôi dảnh lúa bị gãy sát gốc thấy ruột thân đen sì chứa hàng trăm viên hạch nấm đen bóng lấp lánh như hạt cát đen.",
                    "phac_do_vietgap": {
                        "canh_tac": "Rút cạn nước phơi ruộng nứt chân chim giai đoạn đẻ nhánh rộ để ức chế nấm phát triển.",
                        "sinh_hoc": "Phun phòng men vi sinh đối kháng Bacillus subtilis hoặc Trichoderma vào gốc rễ.",
                        "khuyen_cao_chuyen_gia": "Phun trừ bằng hoạt chất Validamycin A hoặc Hexaconazole khi phát hiện các chấm thâm đen đầu tiên ở bẹ lá."
                    }
                },
                {
                    "ten_benh": "Bệnh Bạc lá vi khuẩn nếp đặc sản Điện Biên",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Vi khuẩn",
                        "ten_khoa_hoc": "Xanthomonas oryzae pv. oryzae"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết bệnh bắt đầu từ mép lá hoặc chóp lá đòng loang dần xuống dưới theo hình gợn sóng màu xanh tái ngậm nước",
                        "Sau vết bệnh chuyển sang màu trắng bạc hoặc vàng rơm khô xác",
                        "Buổi sáng ẩm ướt trên mặt vết bệnh tiết ra các giọt dịch khuẩn nhỏ li ti màu vàng hổ phách, khô lại thành hạt tròn cứng",
                        "Lá đòng bị khô bạc hoàn toàn làm lúa trỗ nghẹt hạt lép lửng nặng nề"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bệnh khô đầu lá sinh lý do gió lốc: Khô sinh lý mép lá thẳng màu vàng đều không có vân gợn sóng và không có giọt dịch vi khuẩn hạt tròn hổ phách.",
                    "kiem_tra_thuc_dia": "Lấy tay miết dọc mép lá thấy các hạt giọt dịch tròn cứng như hạt cát vàng rơi vào lòng bàn tay.",
                    "phac_do_vietgap": {
                        "canh_tac": "Không bón thừa phân đạm ure, tăng cường bón kali và tro bếp giúp cứng cây chống đổ.",
                        "sinh_hoc": "Phun phòng bằng chế phẩm Nano Bạc Đồng 400ppm bảo vệ khí khổng mép lá đòng.",
                        "khuyen_cao_chuyen_gia": "Phun phòng trừ ngay bằng Bismerthiazol, Oxolinic acid hoặc Kasugamycin khi vừa dứt đợt mưa bão gió giật."
                    }
                }
            ]
        },
        {
            "id": "w1_037",
            "topic": "Cay_Luong_Thuc_Va_Hoa_Mau",
            "name_vi": "Gạo nếp nương Mường Khương Lào Cai",
            "scientific_name": "Oryza sativa L. cv. Nep Nuong Muong Khuong",
            "dia_ban_pho_bien": ["Mường Khương", "Si Ma Cai", "Bắc Hà", "Lào Cai", "Lai Châu"],
            "dac_tinh_sinh_thai": "Giống lúa nếp rẫy gieo trồng trên nương đồi đất dốc đá vôi không cần dẫn nước ngập, chịu hạn và sương mù cực tốt, hạt nếp to tròn đều thơm đậm hương rừng Tây Bắc, dùng nấu xôi ngũ sắc nổi tiếng.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Lem lép hạt lúa nương Mường Khương",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Tổ hợp nấm bệnh",
                        "ten_khoa_hoc": "Bipolaris oryzae / Fusarium moniliforme / Curvularia lunata"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vỏ trấu hạt lúa xuất hiện các chấm đốm nhỏ màu nâu tím, nâu sẫm hoặc xám đen loang lổ",
                        "Hạt lúa bị lửng lép, phôi hạt bên trong bị teo tóp đen xì hoặc biến dạng",
                        "Hạt gạo bị gãy nát khi xay xát, cơm xôi bị đổi màu và giảm độ dẻo thơm",
                        "Bông lúa bị nhiễm bệnh nhẹ dựng đứng không uốn câu được"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bọ xít dài chích hạt non: Bọ xít chích để lại một vết kim châm nhỏ quanh hạt có quầng thâm; Lem lép hạt do nấm vết bệnh loang lổ khắp bề mặt vỏ trấu thành mảng đen xám.",
                    "kiem_tra_thuc_dia": "Tách vỏ trấu hạt lúa thấy phôi hạt gạo bên trong teo nhỏ màu nâu xỉn có màng nấm bao quanh.",
                    "phac_do_vietgap": {
                        "canh_tac": "Xử lý hạt giống trước khi tra hạt trên nương bằng nước ấm 54 độ C trong 15 phút.",
                        "sinh_hoc": "Phun phòng bằng chế phẩm nấm đối kháng Chaetomium kết hợp dịch chiết Nano Chitosan.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bắt buộc vào giai đoạn trước trỗ 5-7 ngày và sau khi lúa trỗ thoát hoàn toàn bằng Difenoconazole + Propiconazole (Tilt Super) hoặc Tricyclazole."
                    }
                },
                {
                    "ten_benh": "Bệnh Đạo ôn lá lúa rẫy vùng cao",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Pyricularia oryzae"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết bệnh ban đầu là chấm thâm nhỏ hình kim cương hoặc hình mắt thoi",
                        "Vết bệnh lan rộng hai đầu nhọn tâm xám trắng viền nâu đậm có quầng vàng bao quanh",
                        "Nhiều vết liên kết làm toàn bộ phiến lá lúa nương bị khô cháy quăn queo (cháy lá)",
                        "Ruộng lúa nương bị lụi tàn từng chòm xơ xác làm giảm quang hợp nuôi đòng"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Đốm nâu Cercospora: Đốm nâu hình bầu dục dài tròn hai đầu màu nâu đỏ đều đặn; Đạo ôn vết hình thoi sắc nhọn hai đầu có tâm xám bạc đặc trưng.",
                    "kiem_tra_thuc_dia": "Nhìn phiến lá thấy rõ vết bệnh hình con thoi nhọn hai đầu tâm bạc mỏng manh, sờ vào thấy giòn rách.",
                    "phac_do_vietgap": {
                        "canh_tac": "Chọn giống kháng bệnh, không gieo tra quá dày trên nương đồi.",
                        "sinh_hoc": "Phun phòng bằng men vi sinh Bacillus subtilis kết hợp dịch tỏi ớt xua đuổi mầm bệnh.",
                        "khuyen_cao_chuyen_gia": "Phun trừ bằng Tricyclazole (Beam 75WP) hoặc Isoprothiolane khi chớm thấy vết chấm kim hình thoi."
                    }
                }
            ]
        }
    ]
