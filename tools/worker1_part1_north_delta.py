# -*- coding: utf-8 -*-
"""
Worker 1 - Part 1: Miền Bắc & Đồng Bằng Sông Hồng (25 cây trồng bản địa & kinh tế đặc sản)
"""

def get_part1_crops():
    return [
        {
            "id": "w1_001",
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": "Vải thiều Thanh Hà Hải Dương",
            "scientific_name": "Litchi chinensis Sonn. var. Thanh Ha",
            "dia_ban_pho_bien": ["Thanh Hà", "Hải Dương", "Chí Linh", "Hưng Yên"],
            "dac_tinh_sinh_thai": "Cây ưa đất phù sa bồi tụ ven sông Thái Bình, tầng canh tác dày > 1m, thoát nước tốt, pH 5.5 - 6.5. Cần mùa đông lạnh khô (nhiệt độ < 15 độ C kéo dài 2-3 tuần) để phân hóa mầm hoa và xuân ẩm để đậu quả.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Sương mai hại vải (Mốc sương cành hoa quả non)",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Peronophythora litchii"
                    },
                    "trieu_chung_dien_hinh": [
                        "Trên hoa: Chùm hoa bị úng nước chuyển màu nâu sẫm, khi trời mưa phùn phủ lớp mốc trắng như bột sương mai, hoa rụng hàng loạt",
                        "Trên quả non: Vết bệnh bắt đầu từ cuống quả lan rộng ra vỏ quả, vết màu nâu đen hơi lõm, vỏ nhũn chảy nước làm quả non rụng trắng gốc",
                        "Trên lá non: Đốm bệnh màu nâu nhạt không có hình dạng nhất định, mặt dưới lá có lớp phấn mốc trắng xốp khi độ ẩm > 90%",
                        "Trên cành lộc: Cành non bị thâm tím, tóp lại, khô giòn dễ gãy"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Thán thư: Sương mai phát triển cực nhanh trong tiết trời mưa phùn rét ẩm, vết bệnh có lớp mốc trắng mỏng mịn màng; Thán thư phát triển khi nhiệt độ ấm hơn (> 25 độ C), vết bệnh hình tròn đồng tâm lõm sâu và ứa chất nhầy hồng cam.",
                    "kiem_tra_thuc_dia": "Vào sáng sớm có sương, cầm lắc nhẹ chùm hoa thấy hoa rụng lả tả, sờ vào quả non thấy nham nháp ướt lạnh và có mùi chua ủng nhẹ của mô quả lên men.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt tỉa cành tăm, cành sâu bệnh sau thu hoạch giúp tán cây thông thoáng ánh sáng; khơi rãnh thoát nước sâu quanh gốc vườn vải.",
                        "sinh_hoc": "Phun phòng luân phiên nấm đối kháng Chaetomium kết hợp dịch chiết vỏ tôm Chitosan nano 2% kích thích cơ chế tự miễn dịch của biểu bì quả.",
                        "khuyen_cao_chuyen_gia": "Phun chặn dịch bằng hoạt chất Phosphonate hữu cơ sinh học, Mancozeb kết hợp Metalaxyl-M (Ridomil Gold) hoặc Booc-đô 1% trước khi hoa nở 5 ngày và sau khi đậu quả non."
                    }
                },
                {
                    "ten_benh": "Bệnh Thán thư thối khô chùm hoa quả vải",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Colletotrichum gloeosporioides"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết bệnh trên phiến lá là những đốm tròn màu nâu xám có quầng vàng xung quanh, tâm vết bệnh khô rách thủng",
                        "Chùm hoa khô héo có màu đen tro, hoa khô dính chặt trên cuống hoa không rụng ngay như bệnh sương mai",
                        "Trên quả chín xuất hiện vết đốm tròn thâm nâu lõm sâu xuống thịt quả, làm thối cùi vải và biến chất vị ngọt"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với bệnh sương mai: Thán thư làm hoa quả khô giòn đen sẫm và dính chặt trên cây; sương mai làm hoa quả mềm nhũn úng nước và rụng tả tơi.",
                    "kiem_tra_thuc_dia": "Sờ vào vết lõm trên vỏ quả thấy khô dai, dùng kính lúp soi thấy các khối bào tử màu hồng cam nhạt li ti xếp thành vòng đồng tâm.",
                    "phac_do_vietgap": {
                        "canh_tac": "Vệ sinh tàn dư dưới gốc, gom đốt cành lá bệnh, bón phân cân đối N-P-K bổ sung thêm Canxi Bo chống nứt quả.",
                        "sinh_hoc": "Phun Bacillus subtilis chủng đối kháng kết hợp chế phẩm Nano Bạc Đồng 500ppm giai đoạn quả đậu.",
                        "khuyen_cao_chuyen_gia": "Phun phòng trừ bằng Difenoconazole + Azoxystrobin (Amistar Top) hoặc Difenoconazole nồng độ 0.05%."
                    }
                }
            ]
        },
        {
            "id": "w1_002",
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": "Nhãn muộn Miền Thiết Hà Nội",
            "scientific_name": "Dimocarpus longan Lour. cv. Mien Thiet",
            "dia_ban_pho_bien": ["Hoài Đức", "Hà Nội", "Quốc Oai", "Hưng Yên", "Hà Nam"],
            "dac_tinh_sinh_thai": "Cây sinh trưởng mạnh trên đất phù sa cổ ven sông Đáy, sông Hồng, đất cát pha thịt nhẹ, pH 6.0 - 6.8, thoát nước nhanh, chịu hạn khá tốt, ra hoa đậu quả muộn hơn nhãn chính vụ 20-30 ngày.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Chổi rồng nhãn (Bệnh hoa cúc / Bệnh sùi ngọn nhãn)",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Tổ hợp tác nhân",
                        "ten_khoa_hoc": "Phytoplasma sp. / Nhện lông nhung Eriophyes dimocarpi",
                        "vector_truyen_benh": "Nhện lông nhung (Eriophyes dimocarpi)"
                    },
                    "trieu_chung_dien_hinh": [
                        "Đọt non bị co ngắn lại, mọc chen chúc thành chùm dày đặc như tổ chổi rơm hoặc bó hoa cúc",
                        "Lá chét teo nhỏ, xoăn tít biến dạng, mép lá cong queo, có màu vàng nhạt hoặc xanh xám",
                        "Chùm hoa bị thoái hóa, hoa ngắn cũn cỡn không hình thành bầu nhụy hoặc rụng sạch hoa không đậu quả",
                        "Cành chổi sau một thời gian bị khô cháy đen, xơ xác đầu cành"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với hiện tượng ngộ độc thuốc kích thích sinh trưởng (Paclobutrazol): Ngộ độc paclo làm lóng ngắn đồng đều trên toàn cây nhưng lá vẫn xanh dày; bệnh chổi rồng làm đọt xoăn queo rậm rạp cục bộ kèm lớp lông nhung màu vàng nâu mặt dưới lá non.",
                    "kiem_tra_thuc_dia": "Vạch mặt dưới lá non dị dạng dùng kính lúp soi tìm nhện lông nhung kích thước hiển vi hình sâu màu trắng ngà đang bò lúc nhúc.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt tỉa sâu toàn bộ cành chổi rồng xuống dưới vết bệnh 20-30cm, thu gom vào bao nilon tiêu hủy triệt để; bón tăng cường phân hữu cơ vi sinh.",
                        "sinh_hoc": "Phun dầu khoáng sinh học SK Enspray 99EC nồng độ 0.5% kết hợp nấm ký sinh Beauveria bassiana xua đuổi nhện lông nhung.",
                        "khuyen_cao_chuyen_gia": "Phun trừ nhện vector bằng Diafenthiuron, Abamectin hoặc Spirodiclofen khi cây nhú đọt non dài 3-5cm."
                    }
                },
                {
                    "ten_benh": "Bệnh Thối nâu nứt quả nhãn muộn",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Phytophthora nicotianae"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết thối xuất hiện ở vùng rốn quả hoặc quanh cuống quả có màu nâu sẫm lan nhanh quanh vỏ",
                        "Thịt cùi nhãn bên trong bị lên men rượu chua, nhũn nước, vỏ quả nứt toác chảy mật",
                        "Khi trời mưa ẩm kéo dài, trên bề mặt vết thối xuất hiện lớp màng tơ nấm màu trắng mịn bao phủ"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với nứt quả sinh lý do sốc nước: Nứt quả sinh lý vỏ nứt dọc đường rãnh tự nhiên thịt quả vẫn ngọt trắng không thối nhũn; thối nâu nấm vỏ mềm mủn, thịt cùi thối chua nồng mùi men.",
                    "kiem_tra_thuc_dia": "Bóp nhẹ quả thấy vỏ lún mềm chảy nước chua bọt khí, đưa lên mũi ngửi thấy mùi men ủ nồng nặc.",
                    "phac_do_vietgap": {
                        "canh_tac": "Bao chùm quả bằng túi lưới chuyên dụng, khơi mương thoát nước vườn tránh đọng nước mưa sau bão.",
                        "sinh_hoc": "Tưới gốc bằng dịch ủ Trichoderma harzianum phân giải xác bã thực vật mầm bệnh nấm đất.",
                        "khuyen_cao_chuyen_gia": "Phun luân phiên Metalaxyl + Mancozeb hoặc Fosetyl Aluminium giai đoạn quả lớn cách ly 14 ngày trước thu hoạch."
                    }
                }
            ]
        },
        {
            "id": "w1_003",
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": "Cam Canh Hoài Đức Hà Nội",
            "scientific_name": "Citrus reticulata Blanco cv. Cam Canh",
            "dia_ban_pho_bien": ["Hoài Đức", "Bắc Từ Liêm", "Hà Nội", "Hưng Yên", "Bắc Giang"],
            "dac_tinh_sinh_thai": "Cây đòi hỏi kỹ thuật thâm canh cao, đất cát pha thịt nhẹ tơi xốp, pH 6.0 - 6.5, tầng đất mặt dày, giàu mùn hữu cơ. Cây cực kỳ nhạy cảm với úng rễ và hạn hán, cần hãm nước cuốc gốc siết rễ để kích hoa vào cuối đông.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Vàng lá gân xanh (Huanglongbing - HLB)",
                    "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
                    "tac_nhan": {
                        "loai": "Vi khuẩn",
                        "ten_khoa_hoc": "Candidatus Liberibacter asiaticus",
                        "vector_truyen_benh": "Rầy chổng cánh (Diaphorina citri)"
                    },
                    "trieu_chung_dien_hinh": [
                        "Lá cam bị vàng loang lổ dạng mắt cua không đối xứng qua gân chính (blotchy mottle)",
                        "Gân lá dày sưng sần sùi hóa bần nứt nẻ, phiến lá nhỏ dày dựng đứng như tai thỏ",
                        "Cành lộc non ngắn ngủn, cây suy thoái chết dần từ các cành ngọn xuống",
                        "Quả nhỏ méo mó vẹo vọ, tâm quả lệch hẳn sang một bên, hạt lép thâm đen, tép cam chua đắng gắt"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Thiếu kẽm vi lượng: Thiếu kẽm vết vàng xuất hiện đối xứng hoàn hảo hai bên gân lá và phân bố đều khắp cả tán lá; HLB vết vàng lệch bất đối xứng, gân lá sưng gồ và xuất hiện cục bộ từng cành trước khi lan rộng.",
                    "kiem_tra_thuc_dia": "Cắt ngang quả cam Canh thấy tâm lệch méo mó hình chữ C, hạt lép chuyển màu nâu thẫm; quan sát đọt non tìm rầy chổng cánh đậu chổng mông góc 45 độ.",
                    "phac_do_vietgap": {
                        "canh_tac": "Tiêu hủy triệt để cây bệnh nặng, trồng cây giống sạch bệnh vi ghép đỉnh sinh trưởng trong nhà lưới cách ly.",
                        "sinh_hoc": "Bảo vệ quần thể kiến vàng tự nhiên (Oecophylla smaragdina) trong vườn cam để săn bắt tiêu diệt rầy chổng cánh.",
                        "khuyen_cao_chuyen_gia": "Phun phòng rầy chổng cánh triệt để ở từng đợt nhú lộc non bằng dầu khoáng SK Enspray 99EC kết hợp nấm Beauveria bassiana."
                    }
                },
                {
                    "ten_benh": "Bệnh Nứt thân xì mủ thối gốc cam Canh",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Phytophthora citrophthora / Phytophthora nicotianae"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vỏ thân sát gốc bị sũng nước, nứt dọc nứt toác và rỉ ra những giọt nhựa mủ màu hổ phách dính dính",
                        "Vùng vỏ bị bệnh thối nhũn chuyển màu nâu xám, ăn sâu vào tầng mô gỗ bên trong",
                        "Bộ rễ tơ ngầm dưới đất bị thối đen tuột vỏ chỉ còn trơ lõi trắng",
                        "Toàn bộ lá trên tán ngả màu vàng đồng loạt và rụng dần làm cây chết rũ đứng"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Xì mủ do sâu đục thân: Xì mủ do sâu đục thân có lỗ đùn mạt cưa phân sâu li ti; xì mủ Phytophthora thân nứt dọc thành mảng, vỏ thối ướt bốc mùi chua nồng và không có mạt cưa.",
                    "kiem_tra_thuc_dia": "Dùng dao con cạo nhẹ lớp vỏ ngoài thấy tầng tượng tầng chuyển màu nâu đen sũng nước, nhựa mủ nhớt dính vào đầu ngón tay.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cào đất quanh cổ rễ để lộ cổ rễ thoáng gió, tuyệt đối không tủ rơm rác sát thân gốc.",
                        "sinh_hoc": "Cạo sạch vết bệnh nứt thân rồi quét dung dịch vôi tôi trộn nấm đối kháng Chaetomium hoặc Trichoderma bảo vệ vết thương.",
                        "khuyen_cao_chuyen_gia": "Quét gốc hoặc tưới đẫm vùng rễ bằng Phosphonate hữu cơ (Aliette 800WG, Ridomil Gold 68WG) khi mới chớm phát hiện bệnh."
                    }
                }
            ]
        },
        {
            "id": "w1_004",
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": "Bưởi Diễn Phúc Diễn Hà Nội",
            "scientific_name": "Citrus maxima Merr. cv. Dien",
            "dia_ban_pho_bien": ["Bắc Từ Liêm", "Phúc Thọ", "Đan Phượng", "Hà Nội", "Hưng Yên", "Vĩnh Phúc"],
            "dac_tinh_sinh_thai": "Thích hợp đất thịt pha cát ven sông, tầng dày trên 1.5m, thoát nước tốt mùa mưa, pH 5.8 - 6.8. Cây càng nhiều năm tuổi (trên 15-20 năm) thì quả càng mọng nước, vỏ mỏng tơ và ngọt đậm đà hương thơm đặc trưng.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Loét sẹo vi khuẩn hại bưởi (Citrus Canker)",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Vi khuẩn",
                        "ten_khoa_hoc": "Xanthomonas citri subsp. citri"
                    },
                    "trieu_chung_dien_hinh": [
                        "Trên lá: Vết bệnh ban đầu là nốt sần nhỏ trong suốt ở mặt dưới lá, sau phát triển lồi lên màu nâu xám, ở giữa nứt toác như miệng núi lửa thu nhỏ",
                        "Quanh vết loét luôn có quầng vàng sáng rực rỡ (halo vàng) rất đặc trưng",
                        "Trên quả: Vết loét sần sùi đóng vảy cứng xù xì làm biến dạng quả, rụng quả non hoặc giảm mẫu mã nghiêm trọng",
                        "Trên cành non: Vết loét lõm dài làm khô cành giòn gãy"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Bệnh ghẻ nhám (Elsinoe fawcettii): Ghẻ sẹo do vi khuẩn có miệng núi lửa nứt ở tâm và có quầng halo vàng sáng bao quanh; Ghẻ nhám chóp nhọn nhô lên như hạt mụn cơm sần sùi và tuyệt đối không có quầng vàng xung quanh.",
                    "kiem_tra_thuc_dia": "Dùng ngón tay sờ qua mặt lá thấy cộm gai rát ráp, quan sát dưới ánh nắng thấy quầng sáng vàng bao bọc miệng vết nứt.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt tỉa cành bệnh triệt để trong mùa đông, vệ sinh dụng cụ kéo cắt cành bằng cồn 70 độ.",
                        "sinh_hoc": "Phun phòng nấm đối kháng Bacillus subtilis hoặc vi khuẩn đối kháng Pseudomonas fluorescens kết hợp dịch nano đồng hữu cơ.",
                        "khuyen_cao_chuyen_gia": "Phun luân phiên gốc đồng sinh học Bordeaux 1%, Kasugamycin (Kasumin 2SL) hoặc Bismerthiazol sau các đợt mưa dông."
                    }
                },
                {
                    "ten_benh": "Bệnh Bồ hóng muội đen lá và vỏ quả bưởi",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Nấm hoại sinh",
                        "ten_khoa_hoc": "Capnodium citri / Meliola citricola",
                        "vector_truyen_benh": "Rệp sáp, rệp muội, bọ phấn trắng tiết chất mật ngọt"
                    },
                    "trieu_chung_dien_hinh": [
                        "Mặt trên phiến lá và vỏ quả bưởi bị phủ một lớp màng phấn đen mịn xốp như muội than đáy nồi",
                        "Lớp muội đen cản trở quang hợp khiến lá cằn cỗi rụng sớm, quả bưởi xỉn màu lem luốc khó bán",
                        "Lớp nấm chỉ phát triển hoại sinh trên bề mặt chất bài tiết của rệp, không đâm sâu giác mút vào mô tế bào"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Thán thư đốm đen: Màng bồ hóng có thể dùng ngón tay hoặc khăn ướt miết nhẹ lau sạch bong để lộ phiến lá xanh tươi bình thường; Thán thư mô lá bị thối khô hoại tử không thể lau sạch.",
                    "kiem_tra_thuc_dia": "Lấy ngón tay cái miết mạnh lên phiến lá đen, muội than bong ra thành từng mảng mỏng vụn đen dính vào ngón tay.",
                    "phac_do_vietgap": {
                        "canh_tac": "Tỉa cành tán thông thoáng, diệt sạch kiến tha rệp lên cây.",
                        "sinh_hoc": "Phun dung dịch nước rửa chén sinh học loãng 0.2% hoặc dầu khoáng SK Enspray 99EC để rửa trôi muội đen và diệt rệp sáp.",
                        "khuyen_cao_chuyen_gia": "Phun trừ côn trùng chích hút bài tiết mật ngọt bằng Spirotetramat hoặc Abamectin sinh học."
                    }
                }
            ]
        },
        {
            "id": "w1_005",
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": "Ổi Bo Thái Bình",
            "scientific_name": "Psidium guajava L. cv. Bo Thai Binh",
            "dia_ban_pho_bien": ["Vũ Thư", "Kiến Xương", "Thái Bình", "Nam Định", "Hải Dương"],
            "dac_tinh_sinh_thai": "Cây phát triển tối ưu trên đất bãi phù sa màu mỡ ven sông Trà Lý, đất thịt pha sét nhẹ giàu dinh dưỡng, chịu hạn tốt, khả năng tái sinh cành mạnh sau tỉa đốn hàng năm.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Đốm mắt cua quả và lá ổi (Bệnh đốm than)",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Pestalotiopsis psidii / Glomerella cingulata"
                    },
                    "trieu_chung_dien_hinh": [
                        "Trên lá: Vết bệnh tròn nhỏ tâm xám tro viền nâu đỏ gờ nổi rõ ràng như mắt cua",
                        "Trên quả non và quả chín: Vết bệnh tròn lõm màu nâu sẫm, ở giữa vết bệnh xuất hiện các chấm đen nhỏ li ti là ổ bào tử nấm",
                        "Thịt quả dưới vết bệnh bị chai cứng, sượng đắng, quả méo mó nứt nẻ"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Vết chích hút của bọ xít muỗi: Vết bọ xít chích có chấm kim châm ở giữa làm méo sẹo vỏ; bệnh đốm mắt cua hình tròn đồng tâm đều đặn có ổ bào tử nấm đen hạt mè.",
                    "kiem_tra_thuc_dia": "Dùng móng tay cạy mép vết đốm thấy mô thịt quả bên dưới bị sượng cứng hóa gỗ gồ ghề.",
                    "phac_do_vietgap": {
                        "canh_tac": "Bao quả sớm bằng túi xốp lưới bọc nilon chuyên dụng khi quả bằng ngón chân cái; cắt tỉa cành tăm sau mỗi đợt hái.",
                        "sinh_hoc": "Phun phòng chế phẩm Chitosan nano kết hợp nấm đối kháng Trichoderma nồng độ 1:500.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bằng hoạt chất Propineb (Antracol 70WP), Difenoconazole hoặc Daconil 75WP giai đoạn trước khi bao quả."
                    }
                },
                {
                    "ten_benh": "Bệnh Héo rũ gốc mốc trắng cây ổi",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Fusarium oxysporum f. sp. psidii"
                    },
                    "trieu_chung_dien_hinh": [
                        "Lá ổi bị mất màu xanh bóng, chuyển màu vàng úa từ từ hoặc héo rũ xanh đột ngột",
                        "Lá rụng dần từ gốc lên ngọn, các cành trơ trụi cành khô",
                        "Cắt ngang phần gốc thân thấy mạch dẫn chuyển màu nâu đen thâm sẫm",
                        "Rễ cây bị thối mục xơ xác, vỏ rễ dễ dàng tuột khỏi lõi gỗ"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Chết úng rễ do nghẹt thở: Chết úng rễ toàn bộ rễ thối ủng mùi bùn thối không có mạch dẫn thâm đen; Fusarium nấm xâm nhiễm làm nghẽn mạch dẫn chuyển màu thâm nâu đỏ rõ rệt.",
                    "kiem_tra_thuc_dia": "Dùng dao rạch một đường chéo ở phần gốc sát mặt đất, vạt lớp vỏ thấy mạch gỗ bên trong bị thâm đen chạy dọc theo chiều dài thân.",
                    "phac_do_vietgap": {
                        "canh_tac": "Lên luống cao, rãnh thoát nước sâu ráo nước mùa mưa; bón vôi bột khử chua đất định kỳ 6 tháng/lần.",
                        "sinh_hoc": "Tưới gốc hỗn hợp men vi sinh đối kháng Streptomyces kết hợp Bacillus subtilis định kỳ hàng tháng.",
                        "khuyen_cao_chuyen_gia": "Xử lý đất vùng rễ bằng các hoạt chất sinh học Metalaxyl-M hoặc trừ nấm mạch dẫn Difenoconazole khi cây chớm héo."
                    }
                }
            ]
        },
        {
            "id": "w1_006",
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": "Chuối ngự Đại Hoàng Nam Định",
            "scientific_name": "Musa acuminata Colla cv. Ngu Dai Hoang",
            "dia_ban_pho_bien": ["Lý Nhân", "Hà Nam", "Nam Định", "Hưng Yên", "Ninh Bình"],
            "dac_tinh_sinh_thai": "Cây chuối tiến vua ưa phù sa sông Châu Giang, sông Hồng màu mỡ tơi xốp, ẩm độ cao 75-85%, tầng đất dày không ngập úng, cây thân thanh mảnh cần cắm cọc chống đổ khi ra buồng.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Héo rũ Panama chuối (Vàng lá Panama chuối)",
                    "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Fusarium oxysporum f. sp. cubense (Foc TR4)"
                    },
                    "trieu_chung_dien_hinh": [
                        "Lá già phía dưới bị vàng trước tiên, vết vàng lan từ mép lá vào gân chính",
                        "Cuống lá bị bẻ gãy gập rũ xuống, dính bám xung quanh thân giả tạo thành váy lá khô",
                        "Thân giả bị nứt dọc nứt toác sát gốc phình to",
                        "Cắt ngang thân củ chuối thấy hệ mạch dẫn bị thâm đỏ nâu hoặc tím đen bốc mùi hôi chua nhẹ"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Bệnh héo vi khuẩn Moko (Ralstonia solanacearum): Moko làm héo rũ lá non ở ngọn trước và khi cắt thân ngâm nước thấy dịch khuẩn màu trắng đục tuôn ra; Panama làm vàng héo lá già từ gốc lên ngọn và không có giọt dịch khuẩn tuôn ra khi ngâm nước.",
                    "kiem_tra_thuc_dia": "Cắt ngang thân giả chuối thấy các chấm tròn màu nâu đỏ tím xếp thành vòng tròn mạch dẫn; thân củ bổ dọc có vệt tím đen chạy dài.",
                    "phac_do_vietgap": {
                        "canh_tac": "Đào bỏ toàn bộ gốc chuối bệnh đem đốt tiêu hủy rải vôi bột khử trùng hố; tuyệt đối không lấy cây con từ vườn bệnh để nhân giống.",
                        "sinh_hoc": "Bổ sung nấm đối kháng Trichoderma viride kết hợp bón phân hữu cơ hoai mục nhằm áp đảo quần thể nấm đất.",
                        "khuyen_cao_chuyen_gia": "Luân canh triệt để đất trồng với cây lúa nước hoặc ngô 2-3 năm trước khi tái lập vườn chuối."
                    }
                },
                {
                    "ten_benh": "Bệnh Đốm lá Sigatoka vàng hại chuối ngự",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Pseudocercospora musae"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết bệnh ban đầu là những vệt sọc nhỏ màu vàng nhạt chạy song song với gân phụ của phiến lá",
                        "Vệt bệnh lan rộng thành hình bầu dục dài tâm xám bạc viền nâu đỏ đậm nét",
                        "Nhiều đốm liên kết lại làm phiến lá khô cháy thành từng mảng lớn, lá khô rách tả tơi",
                        "Làm giảm diện tích quang hợp khiến buồng chuối nhỏ quả ngắn không tích lũy đủ độ đường"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Sigatoka đen: Sigatoka vàng có vệt ban đầu màu vàng nhạt viền sắc sảo tâm xám bạc; Sigatoka đen vệt sẫm màu nâu đen ngay từ đầu và lan nhanh với độc lực tàn phá mãnh liệt hơn.",
                    "kiem_tra_thuc_dia": "Soi phiến lá ngược sáng thấy rõ các sọc vàng sáng dài 3-5mm song song gân lá, sờ vào mô lá thấy giòn vụn mép.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt bỏ lá già lá bệnh đem chôn tiêu hủy, đánh luống rãnh thoát nước sâu ráo gốc.",
                        "sinh_hoc": "Phun phòng dịch chiết tỏi ớt gừng hoặc dầu khoáng sinh học bảo vệ bề mặt phiến lá.",
                        "khuyen_cao_chuyen_gia": "Phun luân phiên Propiconazole, Tebuconazole hoặc Azoxystrobin định kỳ 15-20 ngày trong mùa mưa phùn ẩm."
                    }
                }
            ]
        },
        {
            "id": "w1_007",
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": "Táo Bàng La Đồ Sơn Hải Phòng",
            "scientific_name": "Ziziphus mauritiana Lam. cv. Bang La",
            "dia_ban_pho_bien": ["Đồ Sơn", "Kiến Thụy", "Hải Phòng", "Thái Bình", "Nam Định"],
            "dac_tinh_sinh_thai": "Cây đặc sản thích ứng tuyệt vời trên vùng đất bãi trũng chua mặn ven biển, chịu mặn tốt (độ mặn 2-4‰), chống chịu gió bão ven biển, quả giòn ngọt đậm đà khi tưới nước lợ.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Phấn trắng lá chồi non và quả táo Bàng La",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Oidium erysiphoides f. sp. ziziphi"
                    },
                    "trieu_chung_dien_hinh": [
                        "Mặt dưới và mặt trên lá non phủ một lớp phấn trắng xóa như bột mì",
                        "Lá non bị biến dạng, dày lên, mép lá cuộn tròn quăn queo, chồi non khô cằn chết ngọn",
                        "Hoa bị lớp phấn trắng bọc kín làm thối rụng không đậu được quả non",
                        "Trên quả non xuất hiện lớp phấn trắng, sau đó quả bị nứt nẻ sần sùi chai cứng"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Muội bồ hóng: Phấn trắng màu trắng tinh xốp mỏng đâm giác mút hút nhựa tế bào; Bồ hóng màu đen tro phát triển hoại sinh trên mật ngọt của côn trùng.",
                    "kiem_tra_thuc_dia": "Dùng ngón tay sờ nhẹ lớp phấn trắng thấy bột mịn dính đầu ngón tay như phấn viết bảng, lá non bên dưới bị ức chế co rúm.",
                    "phac_do_vietgap": {
                        "canh_tac": "Đốn cành táo đúng thời vụ sau thu hoạch tạo tán thông thoáng đón nắng gió, dọn sạch tàn dư lá rụng.",
                        "sinh_hoc": "Phun chế phẩm sinh học chứa vi khuẩn đối kháng Bacillus subtilis hoặc lưu huỳnh vôi (vôi lưu huỳnh sinh học).",
                        "khuyen_cao_chuyen_gia": "Phun phòng khi nhú lộc non bằng Hexaconazole (Anvil 5SC), Difenoconazole hoặc Dinocap."
                    }
                },
                {
                    "ten_benh": "Bệnh Sương mai đốm lá quả táo ta",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Pseudocercospora jujubae"
                    },
                    "trieu_chung_dien_hinh": [
                        "Mặt trên phiến lá xuất hiện các đốm vàng góc cạnh bị giới hạn bởi các gân nhỏ",
                        "Mặt dưới lá tương ứng xuất hiện các đám mốc màu nâu xám xịt",
                        "Bệnh nặng làm lá già úa vàng rụng sớm trơ cành mang quả non",
                        "Quả bị đốm nâu sẫm nhạt màu kém phẩm chất ngọt thơm"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Thiếu đạm: Thiếu đạm lá già vàng đều phẳng phiêu không có đốm góc cạnh; Sương mai lá có đốm góc cạnh viền gân và mốc sậm màu ở mặt dưới.",
                    "kiem_tra_thuc_dia": "Lật mặt dưới phiến lá thấy màng nấm mốc màu xám tro nằm sát kẽ gân lá góc cạnh.",
                    "phac_do_vietgap": {
                        "canh_tac": "Tỉa bớt cành dăm cành khuất tán, tưới tiêu điều độ tránh đọng ẩm cục bộ trong vườn.",
                        "sinh_hoc": "Phun phòng Nano Bạc Đồng 300ppm kết hợp Chitosan bảo vệ tế bào vách biểu bì.",
                        "khuyen_cao_chuyen_gia": "Phun trừ bằng Mancozeb hoặc Azoxystrobin khi phát hiện chớm chấm bệnh đầu tiên."
                    }
                }
            ]
        },
        {
            "id": "w1_008",
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": "Mãng cầu dai Kim Sơn Ninh Bình",
            "scientific_name": "Annona squamosa L. cv. Kim Son",
            "dia_ban_pho_bien": ["Kim Sơn", "Yên Khánh", "Ninh Bình", "Nam Định"],
            "dac_tinh_sinh_thai": "Cây mãng cầu dai (na dai) bén rễ vùng đất bồi phù sa pha cát ven biển và vùng bán sơn địa, ưa ấm áp, chịu khô hạn cực tốt, rễ chùm ăn nông mẫn cảm với đọng nước úng ngập.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Thán thư đốm đen thối quả na dai Kim Sơn",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Colletotrichum gloeosporioides"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết bệnh bắt đầu từ kẽ múi quả na hoặc quanh cuống tạo thành các đốm đen tròn lõm xuống",
                        "Vết thâm lan rộng ra các múi xung quanh, quả na bị chai sượng không mở mắt được",
                        "Quả na khô quắt lại trên cành có màu đen cứng như than củi (hiện tượng quả na xác ướp)",
                        "Lá na xuất hiện đốm cháy viền mép lá màu nâu sẫm giòn rách"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Rệp sáp hại na: Rệp sáp phủ lớp phấn trắng xốp trong kẽ múi tiết mật ngọt làm đen vỏ quả bề mặt; thán thư ăn sâu hoại tử mô thịt múi làm múi chai cứng nứt toác.",
                    "kiem_tra_thuc_dia": "Dùng tay ấn vào quả thấy các múi đen chai cứng không đàn hồi, bổ ra thịt múi bên dưới thâm đen khô đắng.",
                    "phac_do_vietgap": {
                        "canh_tac": "Tỉa cành tạo tán thông thoáng sau thu hoạch, thu gom quả xác ướp khô đen trên cây đem đốt.",
                        "sinh_hoc": "Phun chế phẩm Nano Chitosan kết hợp Trichoderma định kỳ 10 ngày/lần giai đoạn mở mắt quả na.",
                        "khuyen_cao_chuyen_gia": "Phun hoạt chất Difenoconazole, Tebuconazole hoặc Antracol 70WP trước khi hoa nở rộ và sau khi đậu quả non."
                    }
                },
                {
                    "ten_benh": "Bệnh Thối cổ rễ lở gốc cây na non",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Rhizoctonia solani / Pythium spp."
                    },
                    "trieu_chung_dien_hinh": [
                        "Phần cổ rễ sát mặt đất bị thâm đen, úng nước, vỏ rễ bị nứt mục tróc ra",
                        "Toàn bộ lá non trên ngọn héo rũ xanh rồi vàng rụng từ từ",
                        "Cây na con ngã rạp hoặc đứng chết héo giữa vườn khi trời nắng gắt sau mưa",
                        "Bộ rễ tơ bị mủn nát xơ đen không mọc được rễ mới"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Cắn phá của sùng đất cắn rễ: Sùng đất cắn đứt ngang rễ để lại vết cắn nham nhở không có vết bệnh thâm mủn nấm mốc bao quanh mô vỏ cổ rễ.",
                    "kiem_tra_thuc_dia": "Nhổ nhẹ cây na con thấy đứt lìa ngang phần cổ rễ thối mục nát bốc mùi ẩm mốc khó chịu.",
                    "phac_do_vietgap": {
                        "canh_tac": "Lên mô cao thoát nước triệt để, rải vôi bột khử chua trước khi đặt bầu cây con.",
                        "sinh_hoc": "Tưới phòng gốc bằng hỗn hợp men vi sinh Bacillus subtilis và Trichoderma harzianum 20 ngày/lần.",
                        "khuyen_cao_chuyen_gia": "Tưới thuốc trừ nấm rễ Metalaxyl, Validamycin hoặc Ridomil Gold khi đất có dấu hiệu đọng ẩm kéo dài."
                    }
                }
            ]
        },
        {
            "id": "w1_009",
            "topic": "Rau_Cu_Gia_Vi_Va_Nam",
            "name_vi": "Cà rốt Đức Chính Cẩm Giàng",
            "scientific_name": "Daucus carota L. subsp. sativus cv. Duc Chinh",
            "dia_ban_pho_bien": ["Cẩm Giàng", "Nam Sách", "Hải Dương", "Bắc Ninh", "Thái Bình"],
            "dac_tinh_sinh_thai": "Cây rau lấy củ chủ lực vùng đồng bằng Bắc Bộ, ưa đất cát pha bãi bồi sông Thái Bình tơi xốp sâu > 40cm, không lẫn sỏi đá, pH 6.0 - 6.8, thời tiết mát mẻ 16-22 độ C để củ tích lũy carotene đỏ cam rực rỡ.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Cháy lá sọc đen cà rốt (Đốm lá Alternaria)",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Alternaria dauci"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết bệnh bắt đầu từ mép các lá chét già dưới dạng các chấm nhỏ màu nâu đen có quầng vàng",
                        "Các chấm liên kết nhanh chóng làm toàn bộ phiến lá chét cháy khô cong queo như bị lửa táp",
                        "Cuống lá xuất hiện các vệt sọc dài lõm màu nâu sẫm làm gãy rập cả cuống lá",
                        "Tán lá bị khô rụi sớm khiến củ không lớn được, củ nhỏ ngắn và sần sùi kém ngọt"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Đốm lá Cercospora (Cercospora carotae): Cercospora tấn công lá non trước với đốm tròn tâm xám viền nâu nhạt; Alternaria dauci tấn công lá già trước với vết cháy sậm góc cạnh lan từ mép lá vào.",
                    "kiem_tra_thuc_dia": "Vò nhẹ phiến lá khô thấy vụn nát giòn rụm trong tay, ngửi không thấy mùi hôi nhũn vi khuẩn.",
                    "phac_do_vietgap": {
                        "canh_tac": "Luân canh triệt để với lúa nước, gieo hạt giống đã qua xử lý nhiệt 50 độ C trong 20 phút.",
                        "sinh_hoc": "Phun phòng nấm đối kháng Chaetomium sp. kết hợp Nano Đồng 500ppm định kỳ khi cây được 4-5 lá thật.",
                        "khuyen_cao_chuyen_gia": "Phun phòng trị bằng Chlorothalonil (Daconil 75WP), Iprodione hoặc Difenoconazole."
                    }
                },
                {
                    "ten_benh": "Bệnh Thối ướt mềm củ cà rốt vi khuẩn",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Vi khuẩn",
                        "ten_khoa_hoc": "Pectobacterium carotovorum subsp. carotovorum"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết thối bắt đầu từ phần chóp củ hoặc cổ rễ cuống lá sát mặt đất sũng nước",
                        "Thịt củ nhanh chóng chuyển thành khối cháo sền sệt nhũn nước màu xám đục",
                        "Bốc mùi thối khắm tanh tưởi nồng nặc lan tỏa khắp ruộng và trong kho bảo quản",
                        "Vỏ ngoài củ còn nguyên màng mỏng bao bọc khối dịch nhũn thối bên trong"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Thối đen củ do nấm Thielaviopsis: Thối nấm tạo mảng đen khô cứng không có mùi khắm; Thối vi khuẩn mô củ nhũn nát thành nước sệt bốc mùi thối khắm đặc trưng không lẫn vào đâu được.",
                    "kiem_tra_thuc_dia": "Dùng ngón tay ấn nhẹ vào thân củ thấy thủng màng vỏ dịch nhũn thối phì ra bốc mùi thối khắm nồng nặc.",
                    "phac_do_vietgap": {
                        "canh_tac": "Lên luống cao 30-35cm, xới xáo cẩn thận tránh làm xây xước tổn thương thân củ cà rốt.",
                        "sinh_hoc": "Tưới vi khuẩn đối kháng Bacillus subtilis hoặc xông khử trùng kho bảo quản bằng tinh dầu quế/hồi tự nhiên.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bằng kháng sinh nông nghiệp Kasugamycin, Oxytetracycline hoặc Starner 20WP khi vừa dứt đợt mưa to úng ngập."
                    }
                }
            ]
        },
        {
            "id": "w1_010",
            "topic": "Rau_Cu_Gia_Vi_Va_Nam",
            "name_vi": "Su hào tiến vua Hải Dương",
            "scientific_name": "Brassica oleracea var. gongylodes L.",
            "dia_ban_pho_bien": ["Gia Lộc", "Tứ Kỳ", "Hải Dương", "Hà Nội", "Hưng Yên"],
            "dac_tinh_sinh_thai": "Cây rau ưa khí hậu mùa đông lạnh khô miền Bắc (15-20 độ C), đất thịt nhẹ giàu mùn, ẩm độ đất 70-80%, cần bón đủ lân và kali để củ tròn đều, vỏ mỏng mịn, ngọt nước không xơ.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Thối đen vi khuẩn cuống lá củ su hào (Bệnh đốm đen chữ V)",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Vi khuẩn",
                        "ten_khoa_hoc": "Xanthomonas campestris pv. campestris"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết bệnh bắt đầu từ mép lá tiến dần vào trong tạo thành hình chữ V màu vàng nâu rất rõ nét",
                        "Gân lá và các mạch dẫn bên trong chuyển màu đen thâm sẫm",
                        "Củ su hào bị các vệt đen xâm lấn từ cuống lá ăn sâu vào thịt củ làm xơ cứng và thối đen lõi củ",
                        "Lá già phía ngoài vàng héo rụng sớm làm củ su hào teo tóp méo mó"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Cháy bìa lá sinh lý do hạn mặn: Cháy lá sinh lý gân lá vẫn xanh không đổi màu đen; Bệnh thối đen vi khuẩn gân lá và bó mạch dẫn hóa đen hoàn toàn.",
                    "kiem_tra_thuc_dia": "Cắt ngang cuống lá hoặc vết thâm trên củ su hào thấy các chấm đen mạch dẫn xếp thành vòng tròn đồng tâm, bóp nhẹ thấy giọt dịch khuẩn nhờn rỉ ra.",
                    "phac_do_vietgap": {
                        "canh_tac": "Sử dụng hạt giống sạch bệnh, xử lý nước ấm 50 độ C trong 25 phút trước gieo, luân canh với cây họ hòa thảo.",
                        "sinh_hoc": "Phun định kỳ chế phẩm vi sinh Bacillus amyloliquefaciens kết hợp Nano Bạc Đồng 400ppm bảo vệ vòm khí khổng mép lá.",
                        "khuyen_cao_chuyen_gia": "Phun phòng trị bằng Kasugamycin + Copper Oxychloride hoặc chế phẩm Bismerthiazol."
                    }
                },
                {
                    "ten_benh": "Bệnh Sưng rễ hoa thập tự (Bệnh củ rễ bắp cày)",
                    "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
                    "tac_nhan": {
                        "loai": "Nguyên sinh vật nấm ký sinh",
                        "ten_khoa_hoc": "Plasmodiophora brassicae"
                    },
                    "trieu_chung_dien_hinh": [
                        "Bộ rễ tơ và rễ chính bị sưng to bất thường tạo thành các u cục hình chùy, ngón tay hoặc bắp cày méo mó",
                        "Các nốt sưng cản trở khả năng hút nước khiến cây su hào bị héo rũ vào buổi trưa nắng gắt và tươi lại vào ban đêm",
                        "Cây còi cọc suy dinh dưỡng nghiêm trọng, củ không phình to được hoặc chai sần cứng nhắc",
                        "Về sau các u rễ bị thối đen mủn nát bốc mùi hôi thối do vi sinh vật hoại sinh thứ cấp xâm nhập"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt với Tuyến trùng nốt sưng rễ (Meloidogyne): Tuyến trùng tạo các hạt nốt sần nhỏ li ti tròn cỡ hạt đậu hạt tấm rải rác trên rễ tơ; Bệnh sưng rễ Plasmodiophora làm toàn bộ trục rễ biến dạng phình to thành khối chùy khổng lồ đặc sánh.",
                    "kiem_tra_thuc_dia": "Nhổ cả gốc su hào rửa sạch bùn đất thấy bộ rễ phình to gấp 5-10 lần bình thường thành khối u đặc như củ gừng méo mó.",
                    "phac_do_vietgap": {
                        "canh_tac": "Tuyệt đối không trồng su hào trên chân đất đã nhiễm bệnh; bón vôi bột nâng pH đất lên > 7.2 vì mầm bệnh ức chế ở môi trường kiềm.",
                        "sinh_hoc": "Bón phân hữu cơ ủ hoai với nấm đối kháng Trichoderma harzianum mật độ cao ức chế bào tử ngủ nghỉ.",
                        "khuyen_cao_chuyen_gia": "Xử lý đất trước khi trồng bằng hoạt chất Fluazinam hoặc Cyazofamid nếu buộc phải canh tác trên vùng đất có tiền sử bệnh."
                    }
                }
            ]
        }
    ]
