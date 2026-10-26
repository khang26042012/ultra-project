# -*- coding: utf-8 -*-
"""
Worker 1 - Part 5b: Tây Nguyên tiếp theo (Crops 114 to 125)
Chuối Laba, Phúc bồn tử, Việt quất, Sâm đất, Sa nhân Sa Thầy, Nấm linh chi, Nấm đông cô, Bời lời đỏ, Muồng đen, Gỗ trắc đỏ, Cẩm lai, Thông ba lá
"""

def get_part5b_crops():
    return [
        {
            "id": "w1_114",
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": "Chuối Laba Đơn Dương Lâm Đồng",
            "scientific_name": "Musa acuminata Colla cv. Laba Da Lat",
            "dia_ban_pho_bien": ["Đơn Dương", "Đức Trọng", "Lâm Hà", "Lâm Đồng"],
            "dac_tinh_sinh_thai": "Giống chuối tiến vua trứ danh xứ sở ngàn hoa cao nguyên 800 - 1.200m, buồng chuối to khổng lồ quả thon dài hơi cong, vỏ dày màu vàng tươi khi chín, thịt chuối vàng đậm dẻo quánh ngọt lịm thơm ngát hương vị mật ong rừng.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Chùn đọt lùn đầu chuối Laba (Bunchy Top)",
                    "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
                    "tac_nhan": {
                        "loai": "Virus",
                        "ten_khoa_hoc": "Banana bunchy top virus (BBTV)",
                        "vector_truyen_benh": "Rầy mềm đen chuối (Pentalonia nigronervosa)"
                    },
                    "trieu_chung_dien_hinh": [
                        "Các lá non mới nhú bị ngắn ngủn, phiến lá hẹp dựng đứng mép lá uốn cong lượn sóng",
                        "Các cuống lá mọc chụm lại ở đỉnh ngọn thân giả tạo thành hình chiếc tổ chim hoặc bó hoa cúc (chùn đọt)",
                        "Dọc các gân lá xuất hiện các vệt chấm sọc màu xanh đậm ngắt đoạn hình dấu chấm gạch mã morse",
                        "Cây bị lùn tịt không trổ buồng được hoặc buồng chuối nghẹt cứng dị dạng quả ngắn cũn cỡn chát đắng"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Nghẹt đọt do rét buốt: Rét buốt lá chỉ ngắn lại tạm thời nhưng không có các vệt chấm gạch mã morse màu xanh đậm dọc gân lá; Virus BBTV có sọc mã morse đặc trưng không thể nhầm lẫn.",
                    "kiem_tra_thuc_dia": "Soi phiến lá non ngược sáng thấy rõ các chuỗi chấm gạch ngắt đoạn màu xanh đậm li ti dọc theo gân phụ.",
                    "phac_do_vietgap": {
                        "canh_tac": "Đào bỏ gốc chuối bệnh tiêm thuốc diệt cây triệt để cho vào bao nilon tiêu hủy; chỉ trồng cây giống cấy mô sạch bệnh.",
                        "sinh_hoc": "Phun dầu khoáng sinh học SK Enspray 99EC loãng diệt trừ rầy mềm đen vector truyền bệnh.",
                        "khuyen_cao_chuyen_gia": "Phun trừ rầy mềm ở các nách bẹ lá bằng thuốc sinh học Abamectin hoặc Spirotetramat."
                    }
                },
                {
                    "ten_benh": "Bệnh Héo rũ vàng lá Panama TR4 chuối Laba",
                    "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Fusarium oxysporum f. sp. cubense (Foc TR4)"
                    },
                    "trieu_chung_dien_hinh": [
                        "Lá già phía dưới bị vàng úa trước tiên, vết vàng lan từ rìa mép lá vào gân chính",
                        "Cuống lá bị bẻ gãy gập rũ xuống, dính bám xung quanh thân giả tạo thành váy lá khô",
                        "Thân giả bị nứt dọc nứt toác sát gốc phình to",
                        "Cắt ngang thân củ chuối thấy hệ mạch dẫn bị thâm đỏ nâu hoặc tím đen bốc mùi hôi chua nhẹ"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bệnh héo vi khuẩn Moko: Moko héo lá non trước và khi cắt thân ngâm nước thấy dịch khuẩn tuôn ra như khói trắng; Panama TR4 vàng lá già từ gốc lên ngọn và không có giọt dịch khuẩn tuôn ra.",
                    "kiem_tra_thuc_dia": "Cắt ngang thân giả chuối thấy các chấm tròn màu nâu đỏ tím xếp thành vòng tròn mạch dẫn; thân củ bổ dọc có vệt tím đen chạy dài.",
                    "phac_do_vietgap": {
                        "canh_tac": "Đào bỏ toàn bộ gốc chuối bệnh đem đốt tiêu hủy rải vôi bột khử trùng hố; tuyệt đối không lấy cây con từ vườn bệnh để nhân giống.",
                        "sinh_hoc": "Bổ sung nấm đối kháng Trichoderma viride kết hợp bón phân hữu cơ hoai mục nhằm áp đảo quần thể nấm đất.",
                        "khuyen_cao_chuyen_gia": "Luân canh triệt để đất trồng với cây lúa nước hoặc ngô 2-3 năm trước khi tái lập vườn chuối."
                    }
                }
            ]
        },
        {
            "id": "w1_115",
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": "Phúc bồn tử / Mâm xôi đen Đơn Dương Lâm Đồng",
            "scientific_name": "Rubus occidentalis L. cv. Don Duong",
            "dia_ban_pho_bien": ["Đơn Dương", "Đà Lạt", "Lạc Dương", "Lâm Đồng"],
            "dac_tinh_sinh_thai": "Cây ăn quả mọng ôn đới cao cấp trồng trong nhà kính công nghệ cao ở độ cao 1.000 - 1.500m, quả mọng màu tím đen óng ả gồm nhiều múi hạch nhỏ kết tụ lại, vị chua ngọt thanh mát cực kỳ giàu chất chống oxy hóa anthocyanin và axit ellagic bảo vệ sức khỏe.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Mốc xám quả chín phúc bồn tử",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Botrytis cinerea"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vết thối bắt đầu từ các múi hạch nhỏ của quả mọng dưới dạng chấm nâu nhạt ngậm nước",
                        "Vết thối lan cực nhanh làm toàn bộ quả mâm xôi bị nhũn nát chảy nước dính bết",
                        "Bề mặt quả bị bao phủ bởi lớp nấm mốc màu xám tro dày đặc bồng bềnh",
                        "Lây lan nhanh chóng sang cả chùm quả chín làm mất trắng sản lượng thu hái đóng hộp"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Thối mềm Rhizopus: Rhizopus sợi nấm bồng bềnh có các đầu hạt đen li ti; Botrytis lớp lông nhung xám tro đều đặn bay bụi phấn mốc khi chạm vào.",
                    "kiem_tra_thuc_dia": "Khẽ chạm ngón tay vào quả mâm xôi thối thấy đám bụi mốc xám bay lên như khói bụi, quả bên dưới xẹp nhão nhoét.",
                    "phac_do_vietgap": {
                        "canh_tac": "Thu hoạch quả nhẹ nhàng vào sáng sớm, ngắt bỏ quả thối ngay khi phát hiện; giữ độ ẩm nhà kính < 75%.",
                        "sinh_hoc": "Phun phòng bằng nấm đối kháng Trichoderma harzianum hoặc vi khuẩn Bacillus subtilis chuyên tính.",
                        "khuyen_cao_chuyen_gia": "Phun phòng ngừa bằng Iprodione (Rovral 50WP), Fenhexamid hoặc Boscalid giai đoạn ra hoa rộ cách ly nghiêm ngặt 3 ngày trước hái."
                    }
                },
                {
                    "ten_benh": "Bệnh Cháy đốm thân gai mâm xôi",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Didymella applanata"
                    },
                    "trieu_chung_dien_hinh": [
                        "Xung quanh các mắt chồi và cuống lá trên thân gai xuất hiện các vệt loét màu nâu tím dài",
                        "Mô vỏ thân dưới vết loét bị nứt nẻ khô xám bạc, các chồi nách bị thui chột không đâm cành quả được",
                        "Lá trên cành bị úa vàng khô cháy từ rìa mép lá vào gân chính",
                        "Cành mang quả bị chết khô giòn gãy trong mùa đông"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Vết cào rách gai cọ xát: Vết cọ xát cơ giới phẳng liền sẹo trắng; Didymella tạo mảng tím thẫm loang quanh nách mắt chồi có chấm đen quả cành li ti.",
                    "kiem_tra_thuc_dia": "Quan sát thân cành thấy các mảng màu tím sẫm bao quanh các mắt đốt chồi nách, cạo nhẹ thấy mô vỏ bị khô mục.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt bỏ cành già sau thu hoạch sát mặt đất đem tiêu hủy, tỉa thưa giàn cành đón gió.",
                        "sinh_hoc": "Phun phòng bằng Nano Bạc Chitosan bảo vệ bề mặt thân cành sau đốn tỉa.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bằng Booc-đô 1% hoặc Difenoconazole giai đoạn cành non mới vươn dài."
                    }
                }
            ]
        },
        {
            "id": "w1_116",
            "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
            "name_vi": "Việt quất nhà màng Lạc Dương Lâm Đồng",
            "scientific_name": "Vaccinium corymbosum L. cv. Lac Duong",
            "dia_ban_pho_bien": ["Lạc Dương", "Đà Lạt", "Đơn Dương", "Lâm Đồng"],
            "dac_tinh_sinh_thai": "Cây bụi ăn quả mọng ôn đới 'Siêu thực phẩm' trồng trên giá thể mùn than bùn hữu cơ axit cao (pH 4.5 - 5.2) trong nhà màng công nghệ cao cao nguyên 1.500m, quả mọng tròn màu xanh lam đậm phủ lớp phấn sáp trắng bạc quý phái, vị ngọt thanh chua dịu giàu anthocyanin chống lão hóa tế bào tuyệt đỉnh.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Thối thân khô héo cành việt quất",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Botryosphaeria corticis"
                    },
                    "trieu_chung_dien_hinh": [
                        "Trên thân cành xuất hiện các vết loét hình bầu dục sưng phồng lên nứt nẻ màu nâu đỏ",
                        "Mô vỏ dưới vết loét bị thối khô làm tắc nghẽn hoàn toàn mạch dẫn nuôi cành",
                        "Lá trên cành bị héo rũ chuyển sang màu nâu đỏ và dính chặt trên cây không rụng",
                        "Cành việt quất bị chết khô giòn gãy làm mất đi các cành mang quả chủ lực"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Khô cành do thiếu nước giá thể: Khô hạn toàn bộ cành héo mềm đồng loạt; Botryosphaeria chỉ chết khô cục bộ từng cành có vết loét sưng nứt vỏ thân.",
                    "kiem_tra_thuc_dia": "Quan sát thân cành thấy các nốt sưng u nứt toác màu nâu đỏ, cạo vỏ thấy thớ gỗ bên trong chuyển màu nâu đen.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt bỏ cành bệnh sâu dưới vết loét 15cm đem tiêu hủy; khử trùng kéo cắt bằng cồn y tế.",
                        "sinh_hoc": "Phun phòng bằng chế phẩm vi sinh Bacillus subtilis kết hợp Nano Đồng hữu cơ 400ppm.",
                        "khuyen_cao_chuyen_gia": "Phun luân phiên Thiophanate-Methyl, Difenoconazole hoặc Antracol 70WP giai đoạn sau đốn cành."
                    }
                },
                {
                    "ten_benh": "Bệnh Đốm lá sương mai việt quất",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Septoria albopunctata"
                    },
                    "trieu_chung_dien_hinh": [
                        "Phiến lá xuất hiện những đốm tròn nhỏ tâm xám trắng viền nâu đỏ sẫm rất sắc nét",
                        "Trên vết bệnh có các hạt nhỏ màu đen li ti là các quả cành chứa bào tử nấm",
                        "Lá già bị úa vàng rụng sớm hàng loạt làm trơ cành mang quả mọng",
                        "Cây suy kiệt quang hợp kém làm quả việt quất nhỏ bé ít ngọt"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Đốm thán thư: Thán thư đốm lớn lõm sâu có vòng đồng tâm màu nâu đen; Septoria đốm nhỏ tâm trắng bạc như hạt vừng viền tím đỏ sắc sảo.",
                    "kiem_tra_thuc_dia": "Soi lá ngược ánh sáng thấy các đốm nhỏ trong suốt tâm trắng bạc viền nâu đỏ nổi bật trên nền lá xanh.",
                    "phac_do_vietgap": {
                        "canh_tac": "Duy trì độ ẩm nhà màng thông thoáng, tỉa cành thưa đón ánh sáng mặt trời.",
                        "sinh_hoc": "Phun phòng bằng chế phẩm nấm đối kháng Chaetomium kết hợp Nano Chitosan.",
                        "khuyen_cao_chuyen_gia": "Phun phòng ngừa bằng Mancozeb, Difenoconazole hoặc Chlorothalonil khi độ ẩm không khí tăng cao."
                    }
                }
            ]
        },
        {
            "id": "w1_117",
            "topic": "Rau_Cu_Gia_Vi_Va_Nam",
            "name_vi": "Củ sâm đất / Hoàng sin cô Đắk Glong Đắk Nông",
            "scientific_name": "Smallanthus sonchifolius (Poepp.) H.Rob.",
            "dia_ban_pho_bien": ["Đắk Glong", "Đắk Song", "Đắk Nông", "Lạc Dương", "Lâm Đồng"],
            "dac_tinh_sinh_thai": "Cây thảo nguồn gốc từ dãy núi Andes Nam Mỹ thích ứng hoàn hảo trên cao nguyên bazan 900 - 1.500m mát lạnh, củ rễ phình to mọng nước giòn ngọt thanh mát như quả lê chứa nhiều đường FOS (Fructooligosaccharide) tự nhiên cực tốt cho người tiểu đường và giảm cân.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Thối nhũn củ ngầm bảo quản sâm đất",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Sclerotinia sclerotiorum"
                    },
                    "trieu_chung_dien_hinh": [
                        "Củ sâm đất trong kho hoặc dưới đất ẩm bị sũng nước mềm nhũn chảy nước",
                        "Trên bề mặt củ mọc lên một lớp màng tơ nấm màu trắng muốt như bông tuyết",
                        "Bên trong lớp tơ nấm hình thành các hạch nấm lớn màu đen nhánh như phân chuột",
                        "Thịt củ mọng nước bên trong bị rữa nát thành chất lỏng hôi chua thối mục"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Thối vi khuẩn: Thối vi khuẩn mô nhũn nát có mùi khắm tanh tưởi không có hạch nấm màu đen; Nấm Sclerotinia có mạng tơ trắng muốt và vô số hạch nấm đen nhánh như hạt phân chuột.",
                    "kiem_tra_thuc_dia": "Bẻ đôi củ sâm thối thấy màng tơ nấm trắng đan kín và các cục hạch nấm cứng màu đen nhánh nằm sâu trong ruột củ.",
                    "phac_do_vietgap": {
                        "canh_tac": "Thu hoạch củ vào ngày nắng ráo, để củ se khô vết thương trước khi xếp vào sọt bảo quản thoáng gió.",
                        "sinh_hoc": "Tưới phòng gốc bằng hỗn hợp men vi sinh Bacillus subtilis kết hợp Trichoderma harzianum định kỳ hàng tháng.",
                        "khuyen_cao_chuyen_gia": "Xử lý đất và tưới gốc bằng Iprodione hoặc Fludioxonil khi chớm phát hiện hạch nấm."
                    }
                },
                {
                    "ten_benh": "Bệnh Đốm nâu tròn phiến lá sâm đất",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Cercospora sp."
                    },
                    "trieu_chung_dien_hinh": [
                        "Phiến lá lớn hình tim xuất hiện những đốm tròn màu nâu xám có viền đậm",
                        "Tâm vết bệnh bị khô giòn rách thủng lỗ chỗ, mép lá bị cháy khô cong queo",
                        "Lá già bị úa vàng rụng sớm từ gốc lên ngọn làm trơ thân cây",
                        "Cây giảm quang hợp tích lũy chất khô nuôi củ sâm mọng nước"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Cháy nắng lá: Cháy nắng vết màu vàng rơm khô phẳng lì; Cercospora là các đốm tròn đồng tâm sắc nét rải rác khắp bề mặt phiến lá.",
                    "kiem_tra_thuc_dia": "Vò nhẹ mép lá thấy mô lá giòn rụm thủng lỗ rách, soi kính lúp thấy các đốm tròn đồng tâm sắc sảo.",
                    "phac_do_vietgap": {
                        "canh_tac": "Lên luống cao, làm cỏ thông thoáng gốc, bón phân hữu cơ vi sinh cân đối.",
                        "sinh_hoc": "Phun phòng bằng chế phẩm Nano Bạc Đồng 400ppm kết hợp vi khuẩn đối kháng Bacillus subtilis.",
                        "khuyen_cao_chuyen_gia": "Phun phòng trừ bằng Mancozeb hoặc Antracol 70WP khi mưa dầm kéo dài."
                    }
                }
            ]
        },
        {
            "id": "w1_118",
            "topic": "Cay_Lam_Nghiep_Duoc_Lieu_Quy",
            "name_vi": "Sa nhân tím Sa Thầy Kon Tum",
            "scientific_name": "Wurfbainia villosa (Lour.) Skornick. & A.D.Poulsen cv. Sa Thay",
            "dia_ban_pho_bien": ["Sa Thầy", "Đăk Hà", "Kon Tum", "Chư Păh", "Gia Lai"],
            "dac_tinh_sinh_thai": "Cây thảo dược liệu dưới tán rừng khộp và rừng ẩm nhiệt đới vùng biên giới Tây Nguyên 600 - 1.200m, thân rễ bò ngang nhiều đốt, chùm quả gai mềm màu tím đỏ mọc sát gốc thơm nồng cay ngọt chứa tinh dầu borneol và camphor quý báu.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Thối gốc lụi dảnh ngập nước sa nhân",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Pythium debaryanum / Rhizoctonia solani"
                    },
                    "trieu_chung_dien_hinh": [
                        "Gốc dảnh thân và thân rễ sát mặt đất bị sũng nước thâm đen mục nát",
                        "Lá sa nhân ngả màu vàng úa héo rũ, dảnh thân ngã rạp xuống thảm thực vật",
                        "Chùm hoa và chùm quả non sát đất bị thối nhũn chảy nước bốc mùi chua",
                        "Bệnh lây lan rất nhanh theo dòng nước mưa chảy tràn dưới tán rừng"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Dảnh già tự thoái hóa: Dảnh già thân vàng khô tự nhiên vỏ dai chắc; Thối gốc nấm bẹ thân mềm nhũn thối đen chảy nhớt và đứt lìa nhẹ nhàng khi cầm kéo.",
                    "kiem_tra_thuc_dia": "Cầm dảnh sa nhân kéo nhẹ thấy gốc đứt lìa ngang mặt đất, ngửi thấy mùi hôi chua mục nát của mô thân bị nấm thủy sinh phân hủy.",
                    "phac_do_vietgap": {
                        "canh_tac": "Khơi thông dòng chảy ven suối, không để nước tù đọng lâu quanh bụi sa nhân; tỉa bỏ các dảnh già thoái hóa.",
                        "sinh_hoc": "Rải chế phẩm nấm đối kháng Trichoderma harzianum phân tán đều quanh gốc bụi sa nhân định kỳ đầu mùa mưa.",
                        "khuyen_cao_chuyen_gia": "Tưới gốc bằng Phosphonate sinh học hoặc Ridomil Gold khi chớm phát hiện chòm cây bị héo rũ."
                    }
                },
                {
                    "ten_benh": "Bệnh Đốm khô mắt cua lá chét sa nhân tím",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Colletotrichum sp. / Pestalotiopsis sp."
                    },
                    "trieu_chung_dien_hinh": [
                        "Phiến lá xuất hiện những đốm tròn nhỏ li ti tâm xám bạc viền nâu đỏ sẫm như mắt cua",
                        "Các đốm bệnh lan rộng làm mép lá bị cháy khô rách thủng từng mảng",
                        "Lá già bị úa vàng rụng sớm làm trơ bụi sa nhân",
                        "Cây quang hợp kém làm thân rễ còi cọc đâm ít chồi mầm hoa"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bọ xít chích hút lá: Bọ xít chích để lại chấm kim châm nhỏ không có quầng viền tía đỏ tròn đồng tâm sắc sảo.",
                    "kiem_tra_thuc_dia": "Soi phiến lá dưới ánh nắng thấy các chấm đốm nhỏ trong suốt viền nâu đỏ nổi bật trên nền lá xanh.",
                    "phac_do_vietgap": {
                        "canh_tac": "Phát tỉa bớt tán cây che bóng nếu quá rậm rạp, thu dọn lá khô rụng quanh gốc sa nhân.",
                        "sinh_hoc": "Phun phòng bằng chế phẩm Nano Bạc Đồng 300ppm kết hợp Chitosan kích kháng màng tế bào.",
                        "khuyen_cao_chuyen_gia": "Phun phòng trừ bằng Antracol 70WP hoặc Mancozeb khi mưa phùn kéo dài."
                    }
                }
            ]
        },
        {
            "id": "w1_119",
            "topic": "Rau_Cu_Gia_Vi_Va_Nam",
            "name_vi": "Nấm linh chi đỏ Lạc Dương Lâm Đồng",
            "scientific_name": "Ganoderma lucidum (Curtis) P.Karst. cv. Lac Duong",
            "dia_ban_pho_bien": ["Lạc Dương", "Đà Lạt", "Đức Trọng", "Lâm Đồng", "Đắk Lắk"],
            "dac_tinh_sinh_thai": "Nấm dược liệu quý nuôi trồng trên mùn cưa cây cao su hữu cơ trong nhà trại kiểm soát vi khí hậu mát mẻ quanh năm 20-26 độ C độ ẩm 80-90%, tai nấm hình quạt dày dặn màu đỏ cánh gián sáng bóng như quét sơn vecni, giàu triterpenoid và beta-glucan bồi bổ sức khỏe kéo dài tuổi thọ.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Nấm mốc xanh cạnh tranh bịch phôi linh chi",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Nấm tạp cạnh tranh dinh dưỡng",
                        "ten_khoa_hoc": "Trichoderma harzianum / Trichoderma viride"
                    },
                    "trieu_chung_dien_hinh": [
                        "Bên trong bịch mùn cưa xuất hiện những đốm màu xanh lá cây hoặc xanh lục đậm lan rộng cực nhanh",
                        "Sợi tơ nấm mốc xanh ăn lấn át và tiêu diệt hoàn toàn hệ sợi tơ trắng tinh khiết của nấm linh chi",
                        "Bịch phôi bị chua, mùn cưa bị phân hủy thành khối ướt thối rữa nát",
                        "Cổ nút bịch phôi bị phủ bột phấn màu xanh lục mù mịt không ra được mầm tai nấm linh chi"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Hệ sợi tơ linh chi già đổi màu: Sợi tơ linh chi già chuyển sang màu vàng ngà hoặc nâu nhạt đồng nhất; Nấm mốc xanh có màu xanh lá cây đậm dạng bột phấn bám dính dày đặc.",
                    "kiem_tra_thuc_dia": "Nhìn qua lớp nilon bịch phôi thấy các mảng màu xanh lá cây loang lổ cạnh tranh trực tiếp với tơ nấm trắng muốt của linh chi.",
                    "phac_do_vietgap": {
                        "canh_tac": "Hấp tiệt trùng mùn cưa ở nhiệt độ 100 độ C trong 10-12 giờ hoặc nồi áp suất 121 độ C trong 90 phút.",
                        "sinh_hoc": "Khử trùng phòng cấy giống bằng đèn cực tím UV và cấy giống trong tủ cấy vô trùng lase.",
                        "khuyen_cao_chuyen_gia": "Cách ly và tiêu hủy ngay các bịch phôi nhiễm mốc xanh ra khỏi nhà trại nuôi trồng."
                    }
                },
                {
                    "ten_benh": "Bệnh Mốc cam Neurospora phôi linh chi",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm mốc tạp",
                        "ten_khoa_hoc": "Neurospora sitophila"
                    },
                    "trieu_chung_dien_hinh": [
                        "Tại cổ nút bông gòn xuất hiện những đám mốc màu cam rực rỡ xốp bồng bềnh như bọt xà phòng",
                        "Mốc cam phát triển cực nhanh chỉ sau một đêm bao phủ kín miệng bịch phôi",
                        "Giải phóng hàng tỷ bào tử màu cam bay lơ lửng trong không khí lây nhiễm khắp trại nấm",
                        "Bịch phôi bị thối mục làm sợi nấm linh chi chết nghẹt"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bào tử nấm linh chi tự phát tán: Bào tử nấm linh chi có màu nâu đỏ hạt bụi bám mịn trên mặt tai nấm; Mốc cam có màu vàng cam sáng rực rỡ mọc thành khối xốp bồng bềnh tại nút cổ bông.",
                    "kiem_tra_thuc_dia": "Khẽ chạm vào nút bông thấy bụi phấn màu cam bay mù mịt bám đầy vào tay.",
                    "phac_do_vietgap": {
                        "canh_tac": "Xử lý nút bông sạch sẽ khô ráo, không để nút bông bị ướt nước khi tưới phun sương.",
                        "sinh_hoc": "Phun cồn 70 độ sát khuẩn vùng cổ nút bông ngay khi phát hiện đốm cam nhỏ.",
                        "khuyen_cao_chuyen_gia": "Đưa bịch phôi nhiễm mốc cam cho vào bao nilon nhẹ nhàng đem đốt tiêu hủy cách ly xa trại nấm."
                    }
                }
            ]
        },
        {
            "id": "w1_120",
            "topic": "Rau_Cu_Gia_Vi_Va_Nam",
            "name_vi": "Nấm đông cô rừng Kon Plông Kon Tum",
            "scientific_name": "Lentinula edodes (Berk.) Singer cv. Kon Plong",
            "dia_ban_pho_bien": ["Kon Plông", "Măng Đen", "Kon Tum", "Lạc Dương", "Lâm Đồng"],
            "dac_tinh_sinh_thai": "Nấm hương đông cô cao cấp nuôi cấy trên khúc gỗ sồi dẻ hoặc mùn cưa trong rừng thông Măng Đen mát lạnh 16-22 độ C quanh năm sương phủ, mũ nấm dày dặn màu nâu đen có các vết nứt hoa văn màu trắng tuyệt đẹp, mùi thơm ngát ngào ngạt giàu lentinan chống khối u.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Thối ướt mũ nấm mốc trắng đông cô",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm ký sinh",
                        "ten_khoa_hoc": "Trichoderma viride / Cladobotryum mycophilum"
                    },
                    "trieu_chung_dien_hinh": [
                        "Mũ nấm đông cô xuất hiện các đốm nâu sũng nước mềm nhũn",
                        "Sau đó trên vết thối mọc lên một lớp mạng tơ nấm màu trắng muốt như bông gòn bao phủ",
                        "Tai nấm bị biến dạng thối rữa nát thành chất lỏng nhầy nhớt bốc mùi chua hôi",
                        "Lây lan nhanh chóng sang các tai nấm xung quanh trên khúc gỗ mục"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Thối nhũn vi khuẩn: Vi khuẩn làm tai nấm thối chảy nước tanh khắm không có màng tơ bông trắng bao phủ.",
                    "kiem_tra_thuc_dia": "Cầm tai nấm thấy mềm nhũn nước trơn tuột, lớp tơ nấm trắng muốt bao bọc kín mũ nấm.",
                    "phac_do_vietgap": {
                        "canh_tac": "Hạ độ ẩm nhà trại thông gió tối đa sau các đợt tưới đón nấm, hái nấm đúng lứa khi mép mũ còn cụp.",
                        "sinh_hoc": "Phun dung dịch Nano Bạc hữu cơ 200ppm sát khuẩn bề mặt khúc gỗ sau mỗi lứa thu hái.",
                        "khuyen_cao_chuyen_gia": "Cách ly và tiêu hủy tai nấm bệnh, quét vôi bột khử trùng vết cắt tai nấm trên khúc gỗ."
                    }
                },
                {
                    "ten_benh": "Bệnh Đốm thâm đen vi khuẩn mặt nấm đông cô",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Vi khuẩn",
                        "ten_khoa_hoc": "Pseudomonas tolaasii"
                    },
                    "trieu_chung_dien_hinh": [
                        "Mặt trên mũ nấm xuất hiện những đốm nhỏ màu nâu vàng ngậm nước hơi nhầy nhớt",
                        "Các đốm bệnh lan rộng làm mặt mũ nấm bị thâm đen bóng nhờn dính tay",
                        "Tai nấm bị mất mùi thơm tự nhiên biến thành mùi tanh tanh khó chịu",
                        "Làm giảm mạnh phẩm cấp xuất khẩu của nấm hương đông cô cao cấp"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Màu nâu đen tự nhiên của mũ nấm: Màu tự nhiên khô ráo mịn màng sờ không dính nhớt; Bệnh vi khuẩn vết thâm sũng nước bóng loáng nhớt trơn dính tay.",
                    "kiem_tra_thuc_dia": "Lấy ngón tay miết nhẹ mặt mũ nấm thấy trơn nhớt dính nhờn, ngửi thấy mùi tanh ngai ngái.",
                    "phac_do_vietgap": {
                        "canh_tac": "Không tưới nước trực tiếp lên mũ nấm trước khi thu hoạch 6-8 giờ, tạo gió lưu thông làm khô bề mặt mũ nấm.",
                        "sinh_hoc": "Tưới nước đã qua xử lý lọc tia cực tím UV khử sạch vi khuẩn gây hại.",
                        "khuyen_cao_chuyen_gia": "Phun sương dung dịch nước vôi trong loãng pH 8.0 để ức chế vi khuẩn phát triển trên bề mặt tai nấm."
                    }
                }
            ]
        },
        {
            "id": "w1_121",
            "topic": "Cay_Lam_Nghiep_Duoc_Lieu_Quy",
            "name_vi": "Cây bời lời đỏ Ia Grai Gia Lai",
            "scientific_name": "Litsea glutinosa (Lour.) C.B.Rob. cv. Ia Grai",
            "dia_ban_pho_bien": ["Ia Grai", "Chư Prông", "Chư Păh", "Gia Lai", "Kon Tum"],
            "dac_tinh_sinh_thai": "Cây gỗ lâm nghiệp tiên phong bản địa cao 10-15m lớn nhanh trên đất đỏ bazan và đất đồi nghèo kiệt, vỏ và gỗ chứa chất nhầy dính đặc biệt chuyên dùng làm keo dán tự nhiên sản xuất hương thắp truyền thống và keo ép gỗ xuất khẩu giá trị cao.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Sâu cuốn tổ ăn trụi lá bời lời đỏ",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Côn trùng gây hại",
                        "ten_khoa_hoc": "Lygropia quaternalis"
                    },
                    "trieu_chung_dien_hinh": [
                        "Sâu non nhả tơ cuốn gập mép phiến lá bời lời lại làm thành tổ kén ẩn nấp bên trong",
                        "Ăn khuyết thịt lá chỉ để lại lớp biểu bì màng mỏng màu trắng bạc",
                        "Nhiều tổ kén dính bết lại làm cả tán cây bời lời bị cháy khô xơ xác trơ que",
                        "Cây bị suy kiệt giảm khả năng quang hợp làm vỏ cây mỏng dính ít chất keo dính"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bệnh cháy lá do nấm: Cháy nấm lá phẳng khô giòn không cuộn tổ; Sâu cuốn tổ lá bị cuốn tròn thành ống có sợi tơ nhện kết dính và có sâu non bên trong.",
                    "kiem_tra_thuc_dia": "Gỡ tổ lá cuốn thấy con sâu non màu xanh lục có đầu màu nâu đen đang cử động ngo ngoe bên trong.",
                    "phac_do_vietgap": {
                        "canh_tac": "Bảo vệ các loài chim sâu và kiến vàng tự nhiên trong rừng bời lời.",
                        "sinh_hoc": "Phun chế phẩm sinh học vi khuẩn Bacillus thuringiensis (Bt) hoặc nấm ký sinh Beauveria bassiana.",
                        "khuyen_cao_chuyen_gia": "Phun trừ bằng thuốc sinh học Emamectin benzoate hoặc Abamectin khi sâu non mới nở."
                    }
                },
                {
                    "ten_benh": "Bệnh Đốm nâu khô cành vỏ bời lời lấy keo",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Pestalotiopsis sp."
                    },
                    "trieu_chung_dien_hinh": [
                        "Vỏ cành và thân non xuất hiện những đốm nâu đen nhỏ hơi lõm xuống",
                        "Mô vỏ dưới vết đốm bị chai sượng nứt nẻ làm suy giảm hàm lượng chất nhầy tạo keo",
                        "Lá già xuất hiện các vệt cháy thán thư màu xám tro rách thủng mép lá",
                        "Cành non bị khô tóp từ ngọn xuống làm chùn đọt ngừng sinh trưởng"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Vết bóc vỏ cơ giới: Vết bóc cơ giới đường cắt phẳng liền sẹo mịn màng; Nấm bệnh mép nứt nham nhở thối mục nát bốc mùi hôi chua.",
                    "kiem_tra_thuc_dia": "Lấy dao cạo nhẹ vết nứt thân thấy lớp vỏ bên dưới bị thâm đen ướt nhầy mất độ dính keo tự nhiên.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt tỉa cành thông thoáng, dọn sạch tàn dư dưới gốc cây bời lời đỏ.",
                        "sinh_hoc": "Phun phòng bằng chế phẩm nấm đối kháng Chaetomium kết hợp Nano Bạc Đồng 400ppm.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bằng Mancozeb hoặc Antracol 70WP khi độ ẩm không khí tăng cao."
                    }
                }
            ]
        },
        {
            "id": "w1_122",
            "topic": "Cay_Lam_Nghiep_Duoc_Lieu_Quy",
            "name_vi": "Cây muồng đen chắn gió cà phê Tây Nguyên",
            "scientific_name": "Senna siamea (Lam.) H.S.Irwin & Barneby",
            "dia_ban_pho_bien": ["Cư M'gar", "Buôn Ma Thuột", "Đắk Lắk", "Gia Lai", "Đắk Nông"],
            "dac_tinh_sinh_thai": "Cây gỗ lâm nghiệp che bóng và đai rừng chắn gió số một cho vườn cà phê và tiêu Tây Nguyên, rễ cọc đâm sâu không cạnh tranh dinh dưỡng tầng mặt, rụng lá tạo thảm mùn hữu cơ màu mỡ, gỗ lõi màu đen mun cứng như sắt rất giá trị kinh tế.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Gỉ sắt đốm nâu vàng lá chét muồng đen",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Ravenelia tephrosiae"
                    },
                    "trieu_chung_dien_hinh": [
                        "Mặt dưới lá chét xuất hiện các nốt mụn sưng nhỏ li ti màu nâu vàng như gỉ sắt",
                        "Mặt trên lá tương ứng xuất hiện các đốm vàng nhạt hơi nhô gồ ghề",
                        "Bột phấn nấm màu nâu vàng phát tán dính vào tay khi chạm vào",
                        "Lá già bị úa vàng rụng sớm hàng loạt làm trơ cành cây chắn gió"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bệnh cháy lá do khô hạn: Cháy hạn lá khô giòn viền mép đồng loạt; Bệnh rỉ sắt là các ổ mụn nâng cao bề mặt giải phóng bụi phấn nấm màu nâu vàng đặc thù.",
                    "kiem_tra_thuc_dia": "Lấy tay quẹt nhẹ qua đám mụn mặt dưới lá thấy bụi phấn màu nâu vàng dính đầy trên đầu ngón tay.",
                    "phac_do_vietgap": {
                        "canh_tac": "Tỉa bớt cành nhánh thông thoáng định kỳ trước mùa mưa.",
                        "sinh_hoc": "Phun phòng bằng chế phẩm nấm đối kháng Trichoderma kết hợp Nano Bạc Đồng 300ppm.",
                        "khuyen_cao_chuyen_gia": "Phun trừ bằng Hexaconazole (Anvil 5SC) hoặc Difenoconazole khi phát hiện các mụn rỉ sắt đầu tiên."
                    }
                },
                {
                    "ten_benh": "Bệnh Sâu đục thân xén tóc muồng đen",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Côn trùng gây hại",
                        "ten_khoa_hoc": "Batocera sp."
                    },
                    "trieu_chung_dien_hinh": [
                        "Ấu trùng sâu non đục sâu vào lõi gỗ thân cây muồng đen tạo thành các đường hầm khổng lồ ngoằn ngoèo",
                        "Tại các lỗ đục trên thân cây rỉ nhựa và đùn ra từng đống mạt cưa phân sâu màu nâu nhạt",
                        "Cành lớn trên tán bị khô héo lá và chết khô từng phần",
                        "Thân cây bị rỗng ruột dễ dàng gãy đổ khi có gió bão lớn làm gãy đổ đè hỏng vườn cà phê bên dưới"
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
            "id": "w1_123",
            "topic": "Cay_Lam_Nghiep_Duoc_Lieu_Quy",
            "name_vi": "Gỗ trắc đỏ Tây Nguyên",
            "scientific_name": "Dalbergia cochinchinensis Pierre",
            "dia_ban_pho_bien": ["Ea H'leo", "Buôn Đôn", "Đắk Lắk", "Chư Prông", "Gia Lai", "Kon Tum"],
            "dac_tinh_sinh_thai": "Cây gỗ quý hiếm nhóm 1A cực kỳ đắt giá mọc trong rừng khộp và rừng nửa rụng lá Tây Nguyên, lớn chậm lõi gỗ giác đỏ thẫm có vân cẩm thạch tuyệt đẹp thớ gỗ mịn màng chứa nhiều tinh dầu thơm mùi chua nhẹ không bao giờ mối mọt.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Phấn trắng lá con vườn ươm trắc đỏ",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Phyllactinia dalbergiae"
                    },
                    "trieu_chung_dien_hinh": [
                        "Mặt dưới phiến lá chét trắc đỏ phủ một lớp màng phấn trắng xóa mỏng manh như tơ",
                        "Lá chét non bị quăn queo, mép lá cong rụt lại, lá vàng úa và rụng hàng loạt",
                        "Cây trắc non trong vườn ươm bị chùn đọt ngừng phát triển chiều cao",
                        "Cành non bị khô tóp từ ngọn xuống làm chết cây con giống quý hiếm"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bụi đất bám: Bụi đất rửa nước trôi sạch ngay; Phấn trắng nấm có sợi tơ giác mút bám chặt vào biểu bì lá rửa nước không trôi.",
                    "kiem_tra_thuc_dia": "Lấy ngón tay miết nhẹ thấy phấn trắng mịn dính tay, phiến lá bên dưới bị mất diệp lục chuyển màu vàng nhạt.",
                    "phac_do_vietgap": {
                        "canh_tac": "Kê luống vườn ươm thoáng gió, giảm độ che bóng khi cây đã bén rễ cứng cáp.",
                        "sinh_hoc": "Phun chế phẩm sinh học Bacillus subtilis hoặc dung dịch tỏi ớt gừng xua đuổi mầm bệnh.",
                        "khuyen_cao_chuyen_gia": "Phun phòng bằng Hexaconazole (Anvil 5SC) hoặc Difenoconazole định kỳ 10 ngày trong mùa mưa."
                    }
                },
                {
                    "ten_benh": "Bệnh Thối rễ lở cổ rễ cây con trắc đỏ",
                    "muc_do_nguy_hiem": "Rất cao (Nguy hiểm)",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Fusarium solani / Rhizoctonia solani"
                    },
                    "trieu_chung_dien_hinh": [
                        "Phần cổ rễ sát mặt bầu đất bị thâm đen úng nước teo thắt vỏ tróc mục nát",
                        "Lá trắc đỏ con bị héo rũ xanh rất nhanh, lá héo nhưng vẫn còn bám chặt trên thân",
                        "Cây con trong vườn ươm ngã rạp chết hàng loạt sau các cơn mưa dông lớn",
                        "Hệ rễ tơ ngầm bị thối mục mủn nát tuột vỏ chỉ còn trơ lõi rễ"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Chết khô do thiếu nước: Thiếu nước lá khô giòn vàng đều; Bệnh nấm lở cổ rễ mô vỏ thối đen rữa nát tuột khỏi lõi gỗ bốc mùi ẩm mốc khó chịu.",
                    "kiem_tra_thuc_dia": "Nhổ nhẹ cây trắc con thấy đứt lìa ngang cổ rễ thối mục đen, bóp nhẹ thấy trơn tuột nhớt nước.",
                    "phac_do_vietgap": {
                        "canh_tac": "Xử lý đất giá thể bầu ươm bằng vôi bột hoặc nhiệt độ trước khi đóng bầu gieo hạt.",
                        "sinh_hoc": "Tưới phòng gốc bằng hỗn hợp men vi sinh Bacillus subtilis kết hợp Trichoderma harzianum định kỳ hàng tháng.",
                        "khuyen_cao_chuyen_gia": "Tưới thuốc trừ nấm rễ Validamycin A hoặc Metalaxyl-M (Ridomil Gold) khi chớm có dấu hiệu héo đọt non."
                    }
                }
            ]
        },
        {
            "id": "w1_124",
            "topic": "Cay_Lam_Nghiep_Duoc_Lieu_Quy",
            "name_vi": "Cẩm lai Đắk Tô Kon Tum",
            "scientific_name": "Dalbergia oliveri Gamble ex Prain",
            "dia_ban_pho_bien": ["Đắk Tô", "Ngọc Hồi", "Kon Tum", "Chư Prông", "Gia Lai"],
            "dac_tinh_sinh_thai": "Cây gỗ lâm nghiệp nhóm 1A cực kỳ quý báu cao 25-30m thân tròn thẳng đứng trong rừng rậm nhiệt đới Tây Nguyên, lõi gỗ giác màu nâu hồng có vân đen tím huyền ảo thớ mịn đanh chắc như đá chịu lực uốn nắn và gia công đồ mỹ nghệ cao cấp.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Đốm lá sương mai cẩm lai non",
                    "muc_do_nguy_hiem": "Trung bình",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Cercospora sp."
                    },
                    "trieu_chung_dien_hinh": [
                        "Phiến lá chét xuất hiện những đốm tròn nhỏ li ti tâm xám bạc viền nâu đỏ sẫm như mắt cua",
                        "Các đốm bệnh lan rộng làm mép lá bị cháy khô rách thủng từng mảng",
                        "Lá già bị úa vàng rụng sớm làm trơ cành cây con",
                        "Cây con trong vườn ươm sinh trưởng chậm chùn đọt lộc"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Bọ xít chích hút lá: Bọ xít chích để lại chấm kim châm nhỏ không có quầng viền tía đỏ tròn đồng tâm sắc sảo.",
                    "kiem_tra_thuc_dia": "Soi phiến lá dưới ánh nắng thấy các chấm đốm nhỏ trong suốt viền nâu đỏ nổi bật trên nền lá xanh.",
                    "phac_do_vietgap": {
                        "canh_tac": "Làm luống vườn ươm thông thoáng đón gió, tỉa bớt cỏ dại quanh gốc bầu.",
                        "sinh_hoc": "Phun phòng bằng chế phẩm Nano Bạc Đồng 300ppm kết hợp Chitosan kích kháng màng tế bào.",
                        "khuyen_cao_chuyen_gia": "Phun phòng trừ bằng Antracol 70WP hoặc Mancozeb khi mưa phùn kéo dài."
                    }
                },
                {
                    "ten_benh": "Bệnh Mọt đục thân cành cây cẩm lai",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Côn trùng gây hại",
                        "ten_khoa_hoc": "Xyleborus perforans"
                    },
                    "trieu_chung_dien_hinh": [
                        "Mọt cánh cứng nhỏ li ti đục hàng ngàn lỗ nhỏ tròn như đầu tăm trên thân cành cây cẩm lai",
                        "Tại các lỗ đục rỉ dịch nhựa cây và đùn ra các sợi bột gỗ trắng li ti như sợi chỉ",
                        "Mọt mang theo nấm cộng sinh Ambrosiella làm thâm đen mục rỗng thớ gỗ quý",
                        "Cành cây bị gãy đổ đột ngột làm hỏng vân gỗ cẩm lai vô giá"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Sâu đục thân xén tóc: Xén tóc lỗ đục lớn đường kính 5-10mm đùn đống mạt cưa to; Mọt đục lỗ tí hon như đầu tăm đùn sợi bột gỗ trắng như phấn.",
                    "kiem_tra_thuc_dia": "Quan sát thân cành thấy chi chít lỗ nhỏ li ti như rây bột có bột gỗ trắng đùn ra thành sợi chỉ nhỏ bám quanh lỗ.",
                    "phac_do_vietgap": {
                        "canh_tac": "Cắt bỏ cành khô cành chết chứa mọt đem đốt tiêu hủy ngay lập tức.",
                        "sinh_hoc": "Quét vôi tôi trộn lưu huỳnh lên thân cây cao 2m để ngăn mọt xâm nhập.",
                        "khuyen_cao_chuyen_gia": "Phun quét thuốc trừ sâu sinh học Abamectin hoặc Chlorpyrifos Ethyl nồng độ cao vào thân cây khi phát hiện mọt đục rộ."
                    }
                }
            ]
        },
        {
            "id": "w1_125",
            "topic": "Cay_Lam_Nghiep_Duoc_Lieu_Quy",
            "name_vi": "Thông ba lá Lang Biang Lâm Đồng",
            "scientific_name": "Pinus kesiya Royle ex Gordon cv. Lang Biang",
            "dia_ban_pho_bien": ["Đà Lạt", "Lạc Dương", "Đơn Dương", "Lâm Đồng"],
            "dac_tinh_sinh_thai": "Loài thông biểu tượng của thành phố ngàn hoa Đà Lạt và cao nguyên Lang Biang 1.000 - 2.000m, lá kim mọc thành chùm 3 lá dài 15-20cm, thân gỗ lớn cao 25-35m vỏ nứt nẻ sâu màu nâu xám, rừng thông bạt ngàn reo vi vu trong gió lạnh điều hòa khí hậu và che phủ đầu nguồn lưu vực sông Đồng Nai.",
            "danh_sach_benh": [
                {
                    "ten_benh": "Bệnh Rơm rụng lá kim thông nấm mốc (Lophodermium needle cast)",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Lophodermium pinastri"
                    },
                    "trieu_chung_dien_hinh": [
                        "Trên lá kim xuất hiện những đốm nhỏ màu vàng nhạt, sau chuyển sang màu nâu đỏ gỉ sắt",
                        "Trên lá kim khô xuất hiện các vệt vạch ngang màu đen và các quả cành hình bầu dục màu đen nhánh",
                        "Lá kim bị khô cháy chuyển màu vàng rơm và rụng hàng loạt từ dưới lên trên (hiện tượng rơm rụng)",
                        "Tán rừng thông bị xơ xác trơ que làm giảm khả năng quang hợp và trữ nước ngầm"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with Rụng lá kim sinh lý mùa khô: Rụng sinh lý lá kim vàng đều tự rụng không có các vệt vạch ngang màu đen và quả cành đen nhánh trên lá; Lophodermium có các vạch đen ngăn cách rõ rệt như đốt tre.",
                    "kiem_tra_thuc_dia": "Nhặt lá kim khô rụng soi kính lúp thấy các vạch ngang màu đen tuyền và các hạt nang nấm màu đen hình bầu dục xếp dọc lá kim.",
                    "phac_do_vietgap": {
                        "canh_tac": "Dọn dẹp thực bì phòng chống cháy rừng thông, tỉa cành thông thoáng cành la sát đất.",
                        "sinh_hoc": "Phun phòng bằng chế phẩm vi sinh Bacillus subtilis kết hợp Nano Bạc Đồng 400ppm ở các vườn ươm cây giống thông.",
                        "khuyen_cao_chuyen_gia": "Phun phòng ngừa bằng Mancozeb, Chlorothalonil hoặc Booc-đô 1% giai đoạn đầu mùa mưa sương mù ẩm ướt."
                    }
                },
                {
                    "ten_benh": "Bệnh Rỉ sắt đốm u cành thông ba lá",
                    "muc_do_nguy_hiem": "Cao",
                    "tac_nhan": {
                        "loai": "Nấm",
                        "ten_khoa_hoc": "Cronartium flaccidum"
                    },
                    "trieu_chung_dien_hinh": [
                        "Vỏ thân và cành non bị sưng phồng u cục dị dạng hình con thoi nứt nẻ",
                        "Vào mùa xuân từ các khe nứt sưng phồng giải phóng từng túi bột phấn màu vàng cam sáng rực rỡ",
                        "Mô vỏ dưới vết sưng bị thối chết làm rỉ nhựa thông dính quánh",
                        "Cành thông phía trên khối u bị héo lá kim chuyển màu đỏ nâu và chết khô dễ gãy đổ"
                    ],
                    "phan_biet_chan_doan_kep": "Phân biệt with U sưng do sâu đục thân: Sâu đục thân có lỗ đùn mạt cưa; Nấm gỉ sắt Cronartium nứt toác giải phóng túi bụi phấn màu vàng cam sáng rực rỡ không có mạt cưa.",
                    "kiem_tra_thuc_dia": "Quan sát cành non thấy các khối u sưng hình con thoi nứt nẻ, gạt tay thấy bột phấn màu vàng cam rực rỡ dính đầy vào tay.",
                    "phac_do_vietgap": {
                        "canh_tac": "Chặt tỉa bỏ các cành thông bị khối u sưng đem đốt tiêu hủy cách ly nguồn bệnh.",
                        "sinh_hoc": "Phun chế phẩm Nano Đồng hữu cơ 500ppm bảo vệ cành non vườn ươm.",
                        "khuyen_cao_chuyen_gia": "Quét hoặc phun thân bằng Triadimefon, Hexaconazole hoặc Tebuconazole vào mùa xuân nảy chồi."
                    }
                }
            ]
        }
    ]
