# -*- coding: utf-8 -*-
"""
Worker Subagent 3 - Part 1: High-Value Imported & High-Tech Crops in Vietnam
Crops 1 to 20: Direct coverage of required flagship imported crops.
"""

CROPS_PART1 = [
  {
    "id": "imp_crop_001",
    "topic": "Cay_Nhap_Khau_Kinh_Te_Cao",
    "name_vi": "Việt quất nhiệt đới (Southern Highbush)",
    "scientific_name": "Vaccinium darrowii × corymbosum",
    "dia_ban_pho_bien": ["Đà Lạt", "Lạc Dương (Lâm Đồng)", "Mộc Châu (Sơn La)", "Măng Đen (Kon Tum)"],
    "dac_tinh_sinh_thai": "Cây bụi lâu năm, yêu cầu nhà màng công nghệ cao, giá thể mùn xơ dừa bóc vỏ phối trộn perlite hoặc than bùn rêu peatmoss, đất chua nghiêm ngặt với độ pH từ 4.5 - 5.2, không chịu được úng rễ hoặc nước tưới nhiễm mặn.",
    "danh_sach_benh": [
      {
        "ten_benh": "Bệnh thối lở cổ rễ và héo xanh rũ ngọn (Phytophthora Root Rot)",
        "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Phytophthora cinnamomi"
        },
        "trieu_chung_dien_hinh": [
          "Lá chuyển từ xanh bóng sang vàng úa rồi ngả màu nâu đồng đỏ cháy, teo héo rũ từ chóp cành non xuống thân chính",
          "Các chồi sinh trưởng còi cọc, ngừng bung đọt mới, hoa rụng sớm trơ cuống khô",
          "Bộ rễ tơ hút dinh dưỡng bị thối mủn đen, vỏ rễ tuột khỏi lõi gỗ khi kéo nhẹ, phần cổ rễ sát giá thể có vết thâm ướt đổi màu nâu sẫm"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với ngộ độc dinh dưỡng hoặc cháy rễ do phân bón EC cao: Ngộ độc phân bón làm cháy rìa lá màu nâu giòn đồng loạt cả chậu nhưng lõi thân không thâm nâu; bệnh Phytophthora gây thối lõi cổ rễ ướt thối và rũ từng nhánh một.",
        "kiem_tra_thuc_dia": "Nhấc chậu cây kiểm tra chùm rễ tơ dưới đáy: rễ khỏe có màu trắng ngà hoặc vàng rơm sáng, rễ nhiễm bệnh có màu nâu thối đen, bốc mùi hôi mốc ủ nước, dùng dao cạo vỏ cổ rễ thấy mạch gỗ chuyển màu nâu sô-cô-la.",
        "phac_do_vietgap": {
          "canh_tac": "Kê cao chậu thoát nước triệt để, kiểm tra hệ thống châm phân nhỏ giọt định kỳ tránh tích đọng ẩm độ cục bộ, duy trì độ ẩm giá thể 60 - 70%.",
          "sinh_hoc": "Tưới định kỳ 15 ngày/lần chế phẩm nấm đối kháng Trichoderma asperellum kết hợp xạ khuẩn Streptomyces và tưới phòng hoạt chất sinh học Metalaxyl-M hoặc Phosphonate sinh học.",
          "khuyen_cao_chuyen_gia": "Liên hệ Trung tâm Khuyến nông & Dịch vụ Nông nghiệp Lâm Đồng để xét nghiệm mẫu mô rễ nếu phát hiện tỷ lệ héo rũ vượt 5% trong nhà kính."
        }
      },
      {
        "ten_benh": "Bệnh thán thư thối khô quả non và đốm cành (Anthracnose Fruit Rot)",
        "muc_do_nguy_hiem": "Nặng",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Colletotrichum gloeosporioides / Colletotrichum acutatum"
        },
        "trieu_chung_dien_hinh": [
          "Quả việt quất chín hoặc gần chín xuất hiện các đốm tròn hơi lõm, vỏ quả nhăn nheo co rúm lại như hạt nho khô",
          "Trong điều kiện sương mù ẩm ướt trong nhà màng, trên bề mặt vết lõm ứa ra các giọt chất nhờn màu cam cá hồi hoặc hồng san hô chứa bào tử nấm",
          "Lá non xuất hiện các đốm hoại tử màu nâu tròn viền đỏ tím, cuống chùm quả bị thâm đen làm cả chùm teo tóp"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với bệnh mốc xám Botrytis: Thán thư tạo khối giọt bào tử nhầy sền sệt màu cam hồng khi ẩm; trong khi mốc xám Botrytis tạo lớp lông nhung sợi nấm màu tro xám khô xốp.",
        "kiem_tra_thuc_dia": "Dùng ngón tay sờ vào chùm quả mềm nhũn, miết nhẹ thấy dịch nhầy màu cam dính tay; quan sát kính lúp 20x thấy các ổ nấm mọc vòng đồng tâm trên vỏ quả.",
        "phac_do_vietgap": {
          "canh_tac": "Tỉa thông thoáng tán cây sau mỗi đợt hái quả, kiểm soát độ ẩm nhà màng dưới 80% bằng hệ thống quạt đối lưu, thu gom toàn bộ quả mummified (quả khô teo) đem đốt bỏ.",
          "sinh_hoc": "Phun phòng luân phiên nấm vi sinh Bacillus amyloliquefaciens (D747) kết hợp Nano Bạc Đồng sinh học và chiết xuất tinh dầu vỏ quế.",
          "khuyen_cao_chuyen_gia": "Phun phòng ngừa trước giai đoạn nở hoa và giai đoạn quả xanh chuyển màu quả chín theo chuẩn GlobalGAP/VietGAP."
        }
      },
      {
        "ten_benh": "Bệnh phấn trắng lá việt quất (Powdery Mildew)",
        "muc_do_nguy_hiem": "Trung bình",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Microsphaera vaccinii / Erysiphe vaccinii"
        },
        "trieu_chung_dien_hinh": [
          "Bề mặt trên và dưới phiến lá phủ một lớp bột mịn màu trắng như rắc bột mì, thường phát triển mạnh trên lộc non",
          "Lá non bị biến dạng, mép lá cuộn ngược lên trên, mặt sau phiến lá đôi khi có các vệt màu tím đỏ thâm quầng",
          "Cây giảm quang hợp trầm trọng, đọt non chùn ngắn, quả chậm lớn và mất lớp phấn sáp tự nhiên"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với cặn muối khoáng phân bón lá: Phấn trắng cạo nhẹ thấy sợi tơ nấm bám vào mô lá bên dưới bị thâm nhạt; cặn muối khoáng lau sạch bằng nước lá vẫn phẳng xanh bình thường.",
        "kiem_tra_thuc_dia": "Dùng tay xoa nhẹ lên phiến lá phủ bột trắng, bột dính vào tay như bụi phấn, lá bên dưới có quầng đỏ tím nhẹ.",
        "phac_do_vietgap": {
          "canh_tac": "Tăng cường chiếu sáng trong nhà màng, ngắt bớt lá già gốc tăng độ thông thoáng, tránh bón thừa đạm nitrate.",
          "sinh_hoc": "Phun chế phẩm sinh học Bacillus subtilis kết hợp dầu khoáng nông nghiệp hữu cơ SK Enspray 99EC hoặc Kali Phosphite nồng độ 0.2%.",
          "khuyen_cao_chuyen_gia": "Can thiệp sớm ngay khi tỷ lệ chồi non nhiễm phấn trắng chớm đạt 2 - 3% diện tích tán."
        }
      }
    ]
  },
  {
    "id": "imp_crop_002",
    "topic": "Cay_Nhap_Khau_Kinh_Te_Cao",
    "name_vi": "Dâu tây New Zealand / Hàn Quốc (Hana, Maehyang, Tochiotome)",
    "scientific_name": "Fragaria × ananassa",
    "dia_ban_pho_bien": ["Đà Lạt (Lâm Đồng)", "Mộc Châu (Sơn La)", "Măng Đen (Kon Tum)", "Sa Pa (Lào Cai)"],
    "dac_tinh_sinh_thai": "Cây thân thảo lâu năm, canh tác công nghệ cao trên giàn thủy canh giá thể xơ dừa cao 1m hoặc luống phủ bạt nhà kính, nhiệt độ ngày 20 - 24°C, đêm 12 - 16°C, pH giá thể tối ưu 5.8 - 6.2, EC dung dịch tưới 1.2 - 1.6 mS/cm.",
    "danh_sach_benh": [
      {
        "ten_benh": "Bệnh mốc xám thối nhũn quả dâu tây (Gray Mold Fruit Rot)",
        "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Botrytis cinerea"
        },
        "trieu_chung_dien_hinh": [
          "Vết bệnh bắt đầu từ đài hoa hoặc vùng tiếp xúc giữa quả với giá thể ẩm ướt thành đốm úng nước màu nâu nhạt",
          "Thịt quả nhanh chóng bị nhũn nát, biến màu nâu thối, sau đó toàn bộ bề mặt quả bao phủ một lớp sợi nấm và bào tử màu xám tro dày đặc như nhung",
          "Chùm quả lây lan chéo dữ dội, cuống hoa bị cháy đen làm teo héo toàn bộ các nụ bên cạnh"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với bệnh thối nhũn vi khuẩn: Mốc xám có màng lông nhung bào tử màu xám bốc khói bụi khi gõ nhẹ; thối nhũn vi khuẩn quả chảy nước nhớt nhầy bốc mùi hôi thối nồng nặc không có màng lông.",
        "kiem_tra_thuc_dia": "Gõ nhẹ vào quả dâu bệnh: thấy đám bụi bào tử màu xám bay lơ lửng trong không khí; phần thịt quả bên trong nhũn nhưng không dính nhớt hôi.",
        "phac_do_vietgap": {
          "canh_tac": "Tỉa bỏ toàn bộ lá già, lá sát gốc và quả dị hình; không tưới phun mưa lên tán hoa; duy trì độ ẩm nhà màng dưới 75% bằng quạt hút.",
          "sinh_hoc": "Phun định kỳ nấm đối kháng Chaetomium cupreum kết hợp vi khuẩn Bacillus subtilis chủng QST 713 và dịch chiết tỏi ớt lên chùm hoa quả non.",
          "khuyen_cao_chuyen_gia": "Áp dụng biện pháp ngắt lá bệnh vào buổi trưa khô ráo và cho vào túi nilon buộc kín mang ra khỏi vườn tiêu hủy."
        }
      },
      {
        "ten_benh": "Bệnh đốm mắt cua dâu tây (Common Leaf Spot)",
        "muc_do_nguy_hiem": "Cao",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Mycosphaerella fragariae (anamorph: Ramularia tulasnei)"
        },
        "trieu_chung_dien_hinh": [
          "Vết bệnh trên phiến lá dâu tây ban đầu là chấm nhỏ màu nâu đỏ tím",
          "Vết đốm lan rộng từ 3 - 6mm, phần tâm hoại tử khô chuyển sang màu trắng xám hoặc trắng bạc, viền xung quanh có gờ sắc nét màu đỏ tía hoặc tím thẫm rất rõ hình mắt chim/mắt cua",
          "Nhiều đốm liên kết lại làm lá khô cháy rách từng mảng, cuống lá và ngó dâu bị thâm lõm dài"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với Đốm góc lá vi khuẩn (Angular Leaf Spot): Đốm mắt cua có tâm trắng bạc viền đỏ tròn; Đốm góc lá vi khuẩn bị chặn bởi gân lá tạo góc đa giác và ngậm nước soi ngược sáng.",
        "kiem_tra_thuc_dia": "Quan sát tâm đốm bệnh bằng kính lúp thấy tâm trắng sáng rực, viền đỏ tím gờ nổi rõ ràng không bị giới hạn bởi gân lá nhánh.",
        "phac_do_vietgap": {
          "canh_tac": "Vệ sinh giàn dâu định kỳ, ngắt sạch lá già tầng đáy, tránh mật độ cây quá dày trên chậu máng.",
          "sinh_hoc": "Phun phòng dịch nano đồng Chitosan kết hợp nấm Trichoderma harzianum nồng độ 0.3%.",
          "khuyen_cao_chuyen_gia": "Tuân thủ cách ly phân bón lá có hàm lượng đạm cao khi thời tiết chuyển lạnh có sương đọng ban đêm."
        }
      },
      {
        "ten_benh": "Bệnh xì mủ đốm góc lá vi khuẩn dâu tây (Angular Leaf Spot)",
        "muc_do_nguy_hiem": "Nặng",
        "tac_nhan": {
          "loai": "Vi khuẩn",
          "ten_khoa_hoc": "Xanthomonas fragariae"
        },
        "trieu_chung_dien_hinh": [
          "Mặt dưới lá xuất hiện các vết đốm sũng nước hình góc cạnh nhỏ, bị giới hạn hoàn toàn bởi các gân phụ của lá dâu tây",
          "Khi đưa phiến lá soi ngược lên ánh sáng mặt trời, vết bệnh có màu xanh lục nhạt bán trong suốt dạng ngậm dầu mỡ bóng loáng",
          "Sáng sớm hoặc khi trời ẩm ướt, mặt dưới vết bệnh ứa ra các giọt dịch vi khuẩn nhầy màu trắng đục dính nhớt, khi khô lại tạo lớp vảy sáng bóng như keo nến",
          "Đài hoa bị thâm đen cháy xém làm quả non dị hình teo tóp"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với nấm đốm mắt cua: Đốm vi khuẩn có hình đa giác góc cạnh ngậm nước soi ngược sáng thấy thấu quang; mắt cua hình tròn có tâm trắng viền đỏ không thấu quang.",
        "kiem_tra_thuc_dia": "Đặt phiến lá lên lòng bàn tay soi ngược nguồn sáng nhà kính: thấy các ô đa giác xanh trong ngậm nước sáng rực; dùng ngón tay quẹt mặt dưới khi ẩm thấy nhớt dính.",
        "phac_do_vietgap": {
          "canh_tac": "Sử dụng ngó giống dâu tây cấy mô sạch bệnh F0, tiệt trùng kéo tỉa bằng cồn 70 độ giữa các khóm cây, tuyệt đối không tưới phun mưa áp lực cao.",
          "sinh_hoc": "Phun kháng sinh sinh học nguồn gốc vi sinh Kasugamycin kết hợp Nano Bạc và chủng vi khuẩn Bacillus amyloliquefaciens.",
          "khuyen_cao_chuyen_gia": "Báo cáo Trạm Trồng trọt & BVTV địa phương khi phát hiện ổ bệnh lây lan ngó giống mới nhập khẩu."
        }
      }
    ]
  },
  {
    "id": "imp_crop_003",
    "topic": "Cay_Nhap_Khau_Kinh_Te_Cao",
    "name_vi": "Nho mẫu đơn Nhật Bản (Shine Muscat Grape)",
    "scientific_name": "Vitis vinifera 'Shine Muscat'",
    "dia_ban_pho_bien": ["Đà Lạt (Lâm Đồng)", "Đơn Dương (Lâm Đồng)", "Ninh Phước (Ninh Thuận)", "Tuy Phong (Bình Thuận)"],
    "dac_tinh_sinh_thai": "Cây thân leo gỗ cao cấp du nhập từ Nhật Bản, bắt buộc canh tác trong nhà màng vòm thông gió cao che mưa tuyệt đối, đất phù sa pha cát hoặc đất đỏ bazan thoát nước cực tốt, giàn chữ Y hoặc giàn ngang thông thoáng, pH đất 6.0 - 6.8.",
    "danh_sach_benh": [
      {
        "ten_benh": "Bệnh sương mai hại nho mẫu đơn (Downy Mildew)",
        "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Plasmopara viticola"
        },
        "trieu_chung_dien_hinh": [
          "Mặt trên phiến lá xuất hiện các vệt loang màu vàng nhạt như vết dầu loang (oil spots), ranh giới không rõ ràng",
          "Mặt dưới phiến lá đối diện ngay vết loang mọc lên một lớp lông tơ nấm màu trắng như bông tuyết mịn",
          "Vết bệnh nhanh chóng chuyển sang màu nâu đỏ làm lá khô cháy giòn từ mép vào, rụng sớm hàng loạt trơ cành",
          "Chùm hoa và quả nho non bị nhiễm bệnh cong queo lại, chuyển màu nâu xám và khô cứng rụng rụi"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với bệnh phấn trắng: Sương mai có lớp tơ nấm tập trung mặt dưới lá kèm vết loang dầu vàng ở mặt trên; phấn trắng phủ bột trắng phấn xám ở cả 2 mặt lá và làm nứt toác vỏ quả chín.",
        "kiem_tra_thuc_dia": "Lật mặt dưới lá non vào sáng sớm: dùng ngón tay vuốt nhẹ thấy lớp lông nhung trắng mượt như bông gòn ướt, lá mềm giòn bất thường.",
        "phac_do_vietgap": {
          "canh_tac": "Bảo dưỡng mái che ni lông nhà màng không bị rách dột nước mưa; cắt tỉa lách chồi nách tạo độ thoáng gió tuyệt đối; bao chùm quả bằng túi chuyên dụng Nhật Bản.",
          "sinh_hoc": "Phun phòng Phosphonate sinh học (Kali Phosphite), Nano Đồng sinh học kết hợp chế phẩm nấm đối kháng Trichoderma định kỳ 10 ngày/lần trong mùa ẩm.",
          "khuyen_cao_chuyen_gia": "Phun phòng chủ động giai đoạn nho nhú chùm hoa đến khi quả bằng hạt ngô, đảm bảo cách ly VietGAP."
        }
      },
      {
        "ten_benh": "Bệnh phấn trắng nứt vỏ quả nho mẫu đơn (Powdery Mildew)",
        "muc_do_nguy_hiem": "Nặng",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Erysiphe necator (syn. Uncinula necator)"
        },
        "trieu_chung_dien_hinh": [
          "Các chồi non, cành mang quả và cuống lá phủ một lớp bột màu trắng xám tro, ngửi thấy mùi mốc tanh nhẹ",
          "Quả nho mẫu đơn non bị bao phủ bởi lớp phấn trắng, biểu bì quả bị chai cứng mất đàn hồi",
          "Khi ruột quả bên trong lớn nhanh mà vỏ ngoài bị chai, quả nho bị nứt toác dọc để lộ hạt và múi thịt, vi khuẩn hoại sinh nhanh chóng làm thối rữa cả chùm"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với nứt quả sinh lý do sốc nước: Nứt quả sinh lý mép vết nứt tươi xanh sạch sẽ; nứt do phấn trắng luôn có lớp bột nấm mốc trắng xám bao quanh và vết nứt chai bần sần sùi.",
        "kiem_tra_thuc_dia": "Miết ngón tay lên vỏ quả non: thấy lớp bột xám dính chặt, làm lộ mảng sẹo rám màu xám chì bên dưới vỏ quả.",
        "phac_do_vietgap": {
          "canh_tac": "Tỉa bỏ bớt lá che khuất chùm quả đón ánh nắng tán xạ đồng đều, ngắt tỉa quả non đạt mật độ 35 - 45 quả/chùm tiêu chuẩn.",
          "sinh_hoc": "Phun phòng chế phẩm lưu huỳnh sinh học vi mịn (Wettable Sulfur) hoặc chế phẩm vi sinh Bacillus subtilis trước khi bao trái 3 ngày.",
          "khuyen_cao_chuyen_gia": "Không phun lưu huỳnh khi nhiệt độ nhà kính vượt quá 32°C vì dễ gây cháy biểu bì quả non."
        }
      },
      {
        "ten_benh": "Bệnh thán thư sẹo quả đen sùi (Black Rot / Anthracnose)",
        "muc_do_nguy_hiem": "Cao",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Elsinoë ampelina / Guignardia bidwellii"
        },
        "trieu_chung_dien_hinh": [
          "Trên cành non xuất hiện các vết lõm hình bầu dục tròn viền đen sẫm gờ nổi cao, tâm vết lõm màu xám tro",
          "Trên vỏ quả nho xuất hiện vết đốm tròn trũng sâu màu nâu đen có viền tím đậm xung quanh như vết 'mắt chim' (bird's eye rot)",
          "Thịt quả chỗ vết đốm bị chai cứng, quả teo quắt lại thành hòn đá đen cứng gắn chặt trên cuống chùm"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với vết bọ trĩ chích: Vết bọ trĩ cào rách biểu bì tạo mạng lưới sẹo sần sùi màu da lươn màu nâu vàng nông trên bề mặt vỏ; sẹo thán thư lõm sâu hình miệng bát tròn viền đen tím rõ.",
        "kiem_tra_thuc_dia": "Dùng móng tay ấn vào mép vết đốm quả: mô thịt chai cứng trơ lì, viền nổi gờ nhô cao sắc nét màu tím than.",
        "phac_do_vietgap": {
          "canh_tac": "Quét vôi tôi pha đồng sulfat khử trùng thân nho già sau khi cắt cành ngủ đông tỉa cành.",
          "sinh_hoc": "Sử dụng chế phẩm sinh học kháng nấm Chitosan phối hợp dung dịch vi sinh đối kháng Streptomyces lydicus.",
          "khuyen_cao_chuyen_gia": "Tuân thủ nghiêm ngặt kỹ thuật tỉa chùm và bao bọc chùm nho bằng giấy chuyên dụng nhập khẩu có tẩm vi sinh bảo vệ."
        }
      }
    ]
  },
  {
    "id": "imp_crop_004",
    "topic": "Rau_Cu_Gia_Vi_Va_Nam",
    "name_vi": "Măng tây xanh công nghệ cao (Green Asparagus)",
    "scientific_name": "Asparagus officinalis",
    "dia_ban_pho_bien": ["Ninh Phước (Ninh Thuận)", "Bắc Bình (Bình Thuận)", "Đơn Dương (Lâm Đồng)", "Củ Chi (TP.HCM)", "Trà Ôn (Vĩnh Long)"],
    "dac_tinh_sinh_thai": "Cây rau kinh tế cao lâu năm, ưa đất cát pha phù sa thoát nước nhanh, độ dày tầng canh tác sâu > 50cm, pH đất từ 6.5 - 7.5, rất sợ úng ngập rễ dù chỉ 24 giờ, đòi hỏi công nghệ tưới ngầm nhỏ giọt kết hợp bón phân hòa tan.",
    "danh_sach_benh": [
      {
        "ten_benh": "Bệnh thối khô gốc thân và thối rễ măng tây (Fusarium Crown and Root Rot)",
        "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Fusarium oxysporum f. sp. asparagi"
        },
        "trieu_chung_dien_hinh": [
          "Các chồi măng mới nhú bị teo tóp, cong queo hình móc câu, đầu ngọn chồi khô quắt và chuyển sang màu nâu đen",
          "Gốc thân cây mẹ sát mặt đất xuất hiện các vệt loét khô màu nâu đỏ, mạch dẫn bên trong gốc thân bị thâm hóa gỗ",
          "Toàn bộ cành tán lá kim phía trên bị vàng rực từ gốc lên ngọn rồi héo rũ, bộ rễ củ ngầm bị thối rỗng ruột trơ sợi xơ"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với măng bị sâu cắn gốc: Cây bị sâu cắn có vết gặm khuyết cơ học nham nhở tươi mép; cây bị Fusarium mạch dẫn gốc thâm nâu đen lan dần từ rễ lên, mô nứt nẻ có sợi nấm trắng hồng mịn.",
        "kiem_tra_thuc_dia": "Dùng dao rạch dọc gốc thân sát cổ rễ: thấy các bó mạch dẫn dẫn nước hóa nâu đen chạy dài theo thân; bới rễ ngầm thấy rễ mủn xốp đứt đoạn.",
        "phac_do_vietgap": {
          "canh_tac": "Lên liếp cao tối thiểu 30 - 40cm, tạo rãnh thoát nước sâu giữa các hàng măng; thay thế bụi măng bệnh nặng bằng đất mới tiệt trùng vôi tả.",
          "sinh_hoc": "Xử lý đất định kỳ hàng tháng bằng nấm đối kháng Trichoderma viride kết hợp xạ khuẩn phân giải cellulose Streptomyces và vi khuẩn phân giải lân.",
          "khuyen_cao_chuyen_gia": "Khử trùng hệ thống tưới nhỏ giọt bằng Hydrogen Peroxide nông nghiệp nồng độ 100ppm định kỳ chống đóng cặn nấm bệnh."
        }
      },
      {
        "ten_benh": "Bệnh gỉ sắt măng tây (Asparagus Rust)",
        "muc_do_nguy_hiem": "Nặng",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Puccinia asparagi"
        },
        "trieu_chung_dien_hinh": [
          "Trên cành nhỏ và lá kim xuất hiện các ổ nổi mụn sần sùi hình bầu dục màu vàng cam hoặc nâu đỏ như bột gỉ sắt",
          "Biểu bì cây bị nứt toác giải phóng vô số bụi phấn bào tử màu nâu đỏ bám dính vào quần áo công nhân",
          "Cuối vụ bào tử chuyển sang màu đen sẫm (bào tử đông), làm cành lá măng tây khô cháy trơ trụi như bị lửa đốt, giảm 70% năng suất chồi vụ sau"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với bệnh đốm tím Stemphylium: Gỉ sắt có ổ mụn nổi gờ cộm nứt giải phóng bụi phấn bột dính tay; Stemphylium chỉ là vết đốm trơn phẳng màu tím không có bột phấn gỉ bám dính.",
        "kiem_tra_thuc_dia": "Dùng ngón tay miết dọc thân cành măng tây: thấy bột màu nâu đỏ gỉ sắt dính đầy đầu ngón tay như phấn hoa khô ráp.",
        "phac_do_vietgap": {
          "canh_tac": "Sau mỗi chu kỳ thu hoạch 60 - 75 ngày, cắt xả toàn bộ cây mẹ già đem đốt tiêu hủy cách ly khỏi nông trại.",
          "sinh_hoc": "Phun phòng luân phiên các dòng vi sinh đối kháng Bacillus subtilis kết hợp tinh dầu tỏi quế và hoạt chất đồng sinh học hữu cơ.",
          "khuyen_cao_chuyen_gia": "Cắt bớt mật độ thân mẹ giữ 3 - 5 thân khỏe/bụi để gió lưu thông làm khô nhanh sương sáng sớm đọng trên cành tán lá kim."
        }
      },
      {
        "ten_benh": "Bệnh đốm tím thắt ngọn măng tây (Purple Spot)",
        "muc_do_nguy_hiem": "Cao",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Stemphylium vesicarium"
        },
        "trieu_chung_dien_hinh": [
          "Trên thân mồi non xuất hiện các đốm nhỏ hình thoi dài màu tím thẫm hoặc tím nâu, tâm hơi lõm xuống",
          "Vết đốm phát triển bao quanh chu vi thân làm thân măng bị thắt nghẽn, gãy gập ngang thân khi có gió nhẹ",
          "Các chồi măng thu hoạch bị sẹo tím lốm đốm làm mất hoàn toàn giá trị thương phẩm xuất khẩu"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với vết xước cơ học do gió quẹt cát: Vết xước cát cọ phẳng xơ xác không có viền tím đậm; Stemphylium có viền tím sẫm hình thoi đồng tâm lõm giữa ranh giới rất sắc sảo.",
        "kiem_tra_thuc_dia": "Quan sát thân chồi măng non: thấy các vết thắt hình thoi màu tím than lõm nhẹ, nắn thấy mô chỗ vết thắt giòn rụm dễ gãy.",
        "phac_do_vietgap": {
          "canh_tac": "Trồng hàng cây chắn gió quanh trang trại cát pha ven biển để ngăn hạt cát quất xước biểu bì tạo cửa ngõ xâm nhiễm.",
          "sinh_hoc": "Phun nano Chitosan kích kháng dày biểu bì kết hợp phun nấm Chaetomium liều lượng 2g/lít nước.",
          "khuyen_cao_chuyen_gia": "Phun sau mỗi đợt mưa rào kết hợp cắt tỉa ngọn măng gãy để tránh lây lan qua giọt nước bắn."
        }
      }
    ]
  },
  {
    "id": "imp_crop_005",
    "topic": "Cay_Nhap_Khau_Kinh_Te_Cao",
    "name_vi": "Phong lan Vanilla / Hương Vani nhiệt đới (Vanilla Orchid)",
    "scientific_name": "Vanilla planifolia",
    "dia_ban_pho_bien": ["Đà Lạt (Lâm Đồng)", "Phú Quốc (Kiên Giang)", "Đắk Lắk", "Gia Lai", "Bình Dương"],
    "dac_tinh_sinh_thai": "Dây leo biểu sinh thuộc họ Lan, trồng trong nhà lưới che 50 - 60% ánh sáng, cần trụ sống hoặc trụ bê tông bọc xơ dừa, giá thể thảm mục giàu hữu cơ, lá mục hoai mục phối mùn dừa xốp, độ ẩm không khí cao 75 - 85%, pH giá thể 5.5 - 6.5.",
    "danh_sach_benh": [
      {
        "ten_benh": "Bệnh thối thân đen lụi rễ Vani (Fusarium Stem and Root Rot)",
        "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Fusarium oxysporum f. sp. vanillae"
        },
        "trieu_chung_dien_hinh": [
          "Các rễ bám trên trụ và rễ đất bị thối nhũn, chuyển màu nâu đen rồi khô quắt teo rỗng ruột",
          "Thân leo tại các đốt xuất hiện vết úng nước thâm đen, sau đó mô thân bị teo tóp, nhăn nheo, gãy gập",
          "Đoạn thân phía trên vị trí thối bị mất nguồn cung cấp nước, lá ngả vàng héo rũ, quả vani non bị rụng cuống hoàng loạt"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với bệnh cháy nắng thân leo: Vết cháy nắng khô màu trắng bạc chỉ ở mặt hướng sáng và không lây dọc thân; bệnh Fusarium làm thâm đen cả chu vi thân và thối rỗng lõi mạch dẫn từ dưới lên.",
        "kiem_tra_thuc_dia": "Bóp nhẹ vào đốt thân bị bệnh: thân rỗng xốp nhũn mềm xẹp lép, ngửi thấy mùi chua ẩm ốc đặc trưng của nấm Fusarium mục rễ.",
        "phac_do_vietgap": {
          "canh_tac": "Cắt bỏ ngay đoạn thân thối dưới mắt khỏe 2 đốt, sát trùng vết cắt bằng vôi nhão hoặc cồn 70 độ; thay thảm mục giá thể quanh gốc nhiễm bệnh.",
          "sinh_hoc": "Tưới ướt đẫm trụ leo dung dịch nấm đối kháng Trichoderma virens kết hợp vi khuẩn đối kháng Bacillus subtilis định kỳ 20 ngày/lần.",
          "khuyen_cao_chuyen_gia": "Khử trùng giống dây lan bằng dung dịch Nano Bạc 20ppm trước khi đem buộc cố định vào trụ trồng mới."
        }
      },
      {
        "ten_benh": "Bệnh thán thư đốm cháy lá và vỏ quả Vani (Anthracnose)",
        "muc_do_nguy_hiem": "Nặng",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Colletotrichum orchidophilum / Colletotrichum gloeosporioides"
        },
        "trieu_chung_dien_hinh": [
          "Trên phiến lá dày của lan Vani xuất hiện các đốm tròn trũng sâu màu nâu đậm có các vòng tròn đồng tâm",
          "Khi trời nồm ẩm, tâm vết bệnh tiết ra các chấm nhỏ lấm tấm chất nhờn màu hồng cam chứa khối bào tử",
          "Trái vani đang trong giai đoạn phát triển xuất hiện các vệt thâm đen dọc quả, làm quả bị chai nứt và rụng sớm làm giảm nghiêm trọng hàm lượng hương vanillin"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với vết xước cọ gai do cột dây: Vết xước chỉ để lại sẹo khô màu vàng nâu không lan rộng; thán thư có đốm lõm vòng tròn đồng tâm ứa nhầy màu cam hồng.",
        "kiem_tra_thuc_dia": "Dùng kính lúp soi bề mặt vết thâm quả vani: thấy các đốm chấm đen li ti xếp thành vòng tròn đồng tâm, cạo nhẹ thấy mô thịt thối nâu.",
        "phac_do_vietgap": {
          "canh_tac": "Hạ bớt mật độ dây quấn quanh trụ, tạo khoảng thông thoáng giữa các tán lá dây leo, không để nước tưới đọng qua đêm trên nách lá.",
          "sinh_hoc": "Phun chế phẩm sinh học Chitosan 2% kết hợp dịch chiết nấm men kích kháng SAR tự nhiên của cây họ Lan.",
          "khuyen_cao_chuyen_gia": "Phun phòng sớm giai đoạn thụ phấn nhân tạo hoa vani thành công đến khi quả đạt kích thước tối đa."
        }
      }
    ]
  },
  {
    "id": "imp_crop_006",
    "topic": "Cay_Nhap_Khau_Kinh_Te_Cao",
    "name_vi": "Nghệ tây Saffron trồng container lạnh (Saffron Crocus)",
    "scientific_name": "Crocus sativus",
    "dia_ban_pho_bien": ["Đà Lạt (Lâm Đồng)", "Sa Pa (Lào Cai)", "Hà Nội (Trang trại Container Smart-Farm)"],
    "dac_tinh_sinh_thai": "Cây thân thảo có củ ngầm cao cấp nhập khẩu từ Tây Á/Địa Trung Hải, trồng trong phòng sạch công nghệ cao điều hòa nhiệt độ (nhiệt độ lạnh kích hoa 10 - 15°C, chu kỳ sáng tối nghiêm ngặt), giá thể đất sạch hoặc giá thể vô trùng perlite + xơ dừa, pH 6.0 - 7.0, kỵ ẩm ngập ứ đọng nước tuyệt đối.",
    "danh_sach_benh": [
      {
        "ten_benh": "Bệnh thối khô củ nghệ tây Fusarium (Fusarium Corm Rot)",
        "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Fusarium oxysporum f. sp. gladioli"
        },
        "trieu_chung_dien_hinh": [
          "Bóc lớp vỏ bọc xơ bên ngoài củ củ nghệ tây thấy bề mặt củ xuất hiện các vết đốm trũng sâu màu nâu đỏ hoặc đen mun",
          "Củ bị thối khô từ ngoài vào tâm, thịt củ xốp khô mục nát, có mùi hôi hắc ẩm mốc",
          "Các mầm hoa và lá kim không bật lên được, hoặc nếu nhú lên thì ngọn mầm bị thâm đen quắt queo rồi lụi tàn"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với củ cạn kiệt năng lượng tự nhiên sau khi ra hoa: Củ cạn tự teo tóp khô đồng đều màu vàng nâu sạch sẽ; củ bệnh Fusarium có các hốc lõm thâm đen thối rỗng và có lớp mốc hồng xốp bám bên trong.",
        "kiem_tra_thuc_dia": "Cắt đôi củ nghệ tây kiểm tra: thấy phần thịt củ có các vòng thâm đen đồng tâm lan tỏa từ gốc củ lên mầm sinh trưởng.",
        "phac_do_vietgap": {
          "canh_tac": "Khử trùng khay trồng và phòng lạnh bằng khí Ozone hoặc đèn cực tím UV-C trước khi xếp củ giống vào phòng ươm.",
          "sinh_hoc": "Ngâm xử lý củ giống 20 phút trước khi vào khay bằng dung dịch nấm đối kháng Trichoderma harzianum nồng độ 10^8 bào tử/ml kết hợp Nano Bạc 15ppm.",
          "khuyen_cao_chuyen_gia": "Loại bỏ triệt để và đốt cách ly các củ có vết thâm ngay từ khâu phân loại kiểm dịch nhập khẩu ban đầu."
        }
      },
      {
        "ten_benh": "Bệnh thối hạch trắng đáy củ nghệ tây (Sclerotium White Rot)",
        "muc_do_nguy_hiem": "Nặng",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Sclerotium rolfsii / Stromatinia gladioli"
        },
        "trieu_chung_dien_hinh": [
          "Phần đế củ và rễ mầm xuất hiện lớp sợi nấm màu trắng muốt như bông gòn bao phủ dày đặc",
          "Mô củ sát đáy bị thối mục ướt mềm, sau đó lớp sợi nấm kết tụ lại thành các hạch nấm tròn nhỏ màu nâu sẫm như hạt cải bắp",
          "Lá kim nhú lên bị vàng vọt từ gốc và nhổ bật lên rất dễ dàng vì phần củ bên dưới đã mục nát hoàn toàn"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với sợi nấm có ích mycorrhiza: Nấm có ích sợi mảnh màu trắng xám bám rễ không làm thối củ; Sclerotium làm thối nhũn mô củ và bắt buộc tạo các hạch nấm tròn cứng như hạt cải.",
        "kiem_tra_thuc_dia": "Dùng panh kẹp nhấc củ lên: thấy các hạt nhỏ hình tròn màu nâu bóng kích thước 1 - 2mm bám dày đặc quanh vùng rễ đáy củ bị thối mủn.",
        "phac_do_vietgap": {
          "canh_tac": "Kiểm soát độ ẩm giá thể khay trồng dưới 60%, không để rò rỉ nước từ dàn máy lạnh nhỏ xuống khay trồng củ.",
          "sinh_hoc": "Xử lý giá thể bằng chế phẩm vi sinh hữu cơ chứa xạ khuẩn Streptomyces và vi khuẩn Bacillus amyloliquefaciens.",
          "khuyen_cao_chuyen_gia": "Cách ly toàn bộ khay ươm bị nhiễm bệnh ra khỏi container thông minh, tiêu độc khử trùng toàn bộ phòng sinh trưởng."
        }
      }
    ]
  },
  {
    "id": "imp_crop_007",
    "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
    "name_vi": "Nho thân gỗ Nam Mỹ Jaboticaba (Jabuticaba)",
    "scientific_name": "Plinia cauliflora (syn. Myrciaria cauliflora)",
    "dia_ban_pho_bien": ["Đà Lạt (Lâm Đồng)", "Buôn Ma Thuột (Đắk Lắk)", "Gia Lai", "Bình Dương", "Bình Phước", "Vĩnh Long"],
    "dac_tinh_sinh_thai": "Cây ăn trái thân gỗ lâu năm nguồn gốc Nam Mỹ, hoa và quả mọc trực tiếp từ thân cây gỗ, sinh trưởng chậm, ưa đất thịt giàu hữu cơ tầng canh tác dày, hơi chua nhẹ pH 5.5 - 6.5, chịu được biên độ nhiệt rộng nhưng nhạy cảm với đất kiềm vôi cao.",
    "danh_sach_benh": [
      {
        "ten_benh": "Bệnh gỉ sắt hoa và quả nho thân gỗ (Jaboticaba Rust)",
        "muc_do_nguy_hiem": "Nặng",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Puccinia psidii"
        },
        "trieu_chung_dien_hinh": [
          "Bụi hoa và quả non bám trên thân cây xuất hiện các mụn nhỏ sần sùi màu vàng huỳnh quang sáng chói",
          "Lớp bột phấn bào tử màu vàng chanh bám dày đặc trên cuống hoa và bề mặt quả non",
          "Quả non bị chai sần, ngừng lớn, vỏ sần sùi biến dạng và rụng hàng loạt khỏi thân gỗ, chồi non biến dạng quăn queo"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với phấn hoa tự nhiên của hoa nho: Phấn hoa nằm ở đầu nhụy màu trắng ngà rụng tự nhiên sau khi thụ phấn; mụn gỉ sắt màu vàng nghệ sặc sỡ bám chặt vào vỏ quả non và cành lộc non gây chai cứng mục thịt quả.",
        "kiem_tra_thuc_dia": "Dùng ngón tay chạm vào đám quả non trên thân: bột vàng huỳnh quang bám dính dày đặc vào đầu ngón tay, quả non bị mềm nhăn hoặc chai đen.",
        "phac_do_vietgap": {
          "canh_tac": "Cắt tỉa các cành tăm, cành vượt mọc rậm rạp trong lòng tán để thân chính nhận đủ ánh nắng tán xạ mặt trời.",
          "sinh_hoc": "Phun phòng luân phiên nấm đối kháng Chaetomium kết hợp dịch Nano Đồng hữu cơ 500ppm ngay khi hoa nhú mầm mắt cua trên thân.",
          "khuyen_cao_chuyen_gia": "Ngừng phun mọi hoạt chất sinh học trước ngày thu hái quả chín mọng tối thiểu 7 ngày."
        }
      },
      {
        "ten_benh": "Bệnh nấm bồ hóng muội đen quả và thân cây (Sooty Mold)",
        "muc_do_nguy_hiem": "Trung bình",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Capnodium citri / Meliola spp."
        },
        "trieu_chung_dien_hinh": [
          "Vỏ thân cây và bề mặt vỏ quả chín bị bao phủ bởi một màng mỏng màu đen nhánh như nhọ nồi",
          "Màng nấm không đâm sâu vào tế bào thịt cây mà phát triển ký sinh trên chất mật ngọt do rệp sáp, rầy mềm bài tiết ra",
          "Làm quả nho thân gỗ mất màu đen tím bóng bẩy quyến rũ, cản trở quang hợp của lớp vỏ thân non"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với thán thư vỏ: Bồ hóng dùng khăn ướt lau mạnh sẽ bong tróc sạch để lộ vỏ quả tươi bóng nguyên vẹn bên dưới; thán thư ăn sâu hoại tử mô thịt không thể lau sạch.",
        "kiem_tra_thuc_dia": "Dùng khăn ướt miết nhẹ lên vùng vỏ quả bị đen: mảng đen bong ra dễ dàng như nhọ nồi dính vào khăn, quả bên dưới hoàn toàn lành lặn không sẹo lõm.",
        "phac_do_vietgap": {
          "canh_tac": "Diệt trừ triệt để kiến đen và rệp sáp môi giới truyền chất mật ngọt bằng cách quét vôi quanh gốc thân cây.",
          "sinh_hoc": "Phun trừ rệp sáp bằng chế phẩm nấm ký sinh côn trùng Beauveria bassiana kết hợp dầu khoáng SK Enspray 99EC nồng độ 0.5% để rửa trôi muội than.",
          "khuyen_cao_chuyen_gia": "Dùng vòi nước áp lực vừa phải rửa sạch tán thân sau khi xử lý triệt để ổ rệp sáp."
        }
      }
    ]
  },
  {
    "id": "imp_crop_008",
    "topic": "Cay_Nhap_Khau_Kinh_Te_Cao",
    "name_vi": "Táo đỏ lùn hữu cơ Tân Cương (Organic Jujube / Chinese Date)",
    "scientific_name": "Ziziphus jujuba",
    "dia_ban_pho_bien": ["Ninh Phước (Ninh Thuận)", "Bắc Bình (Bình Thuận)", "Đắk Lắk", "Gia Lai", "Lạng Sơn"],
    "dac_tinh_sinh_thai": "Cây ăn quả ôn đới & cận nhiệt đới du nhập, ưa khí hậu khô nóng nhiều nắng, chịu hạn cực tốt, chịu rét mùa đông, ưa đất phù sa ven sông hoặc đất cát pha sỏi đồi núi, pH thích hợp từ 6.5 - 8.0, kỵ đất trũng ngập nước.",
    "danh_sach_benh": [
      {
        "ten_benh": "Bệnh chổi phù thủy táo đỏ (Jujube Witches' Broom - JWB)",
        "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
        "tac_nhan": {
          "loai": "Phytoplasma",
          "ten_khoa_hoc": "Candidatus Phytoplasma ziziphi",
          "vector_truyen_benh": "Rầy xanh lá mạ (Hishimonus chinensis)"
        },
        "trieu_chung_dien_hinh": [
          "Các chồi ngủ trên cành đồng loạt bung ra vô số chồi nách nhỏ li ti dày đặc mọc túm tụm như cái chổi quét nhà",
          "Lá non teo nhỏ như vảy cá, vàng úa mất diệp lục, phiến lá cong queo dị hình",
          "Cành hoa bị biến đổi thành dạng cành lá sinh dưỡng (hiện tượng hóa lá hoa), không thể đậu quả, cây suy kiệt kiệt quệ và chết khô sau 2 - 3 năm"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với đột biến chồi non do sốc thuốc cỏ: Sốc thuốc cỏ chỉ làm quéo đầu ngọn một đợt rồi phục hồi; bệnh do Phytoplasma lây lan khắp toàn bộ hệ thống mạch dẫn và mọc cụm chổi vĩnh viễn không thể phục hồi.",
        "kiem_tra_thuc_dia": "Quan sát cấu trúc cụm cành: hàng chục chồi tăm đâm ra từ một mắt đốt duy nhất chen chúc nhau, hoa biến thành chùm lá xanh tí hon dị dạng.",
        "phac_do_vietgap": {
          "canh_tac": "Cắt tỉa triệt để và cưa bỏ cành chổi phù thủy sâu vào phần gỗ khỏe 30cm, đốt tiêu hủy cách ly ngay lập tức; không nhân giống từ cây mẹ có triệu chứng nghi ngờ.",
          "sinh_hoc": "Phun phòng trừ rầy môi giới bằng nấm ký sinh Metarhizium anisopliae (nấm xanh) kết hợp chiết xuất tinh dầu Neem hữu cơ.",
          "khuyen_cao_chuyen_gia": "Tiêm kháng sinh sinh học Oxytetracycline vào thân cây đầu mùa xuân để ức chế Phytoplasma đối với cây cổ thụ có giá trị kinh tế cao theo hướng dẫn của chuyên gia lâm sàng BVTV."
        }
      },
      {
        "ten_benh": "Bệnh gỉ sắt hại lá táo đỏ (Jujube Rust)",
        "muc_do_nguy_hiem": "Cao",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Phakopsora zizyphi-vulgaris"
        },
        "trieu_chung_dien_hinh": [
          "Mặt dưới phiến lá xuất hiện các đốm nhỏ màu vàng sáng, sau đó hình thành các mụn nổi nhỏ màu nâu vàng gỉ sắt",
          "Bào tử nấm phát tán bụi phấn vàng bám dính dày đặc mặt dưới phiến lá táo đỏ",
          "Lá bị nhiễm nặng ngả màu vàng úa, khô giòn và rụng sớm hàng loạt trút sạch lá làm quả non bị chai sượng rụng theo"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với nhện đỏ gây hại: Nhện đỏ tạo lớp tơ mịn bám mặt dưới lá và di chuyển được khi soi kính lúp, lá có màu bạc lấm tấm; gỉ sắt tạo các mụn nổi cố định chứa bụi phấn màu nâu vàng gỉ sắt.",
        "kiem_tra_thuc_dia": "Dùng ngón tay vuốt mặt dưới lá táo: lớp bụi vàng gỉ sắt bám dính vào tay, mô lá mặt trên tương ứng có chấm vàng nhạt lõm nhẹ.",
        "phac_do_vietgap": {
          "canh_tac": "Quét vôi gốc cây vào mùa thu đông, dọn sạch lá rụng dưới gốc xới đất nhẹ để vùi lấp tàn dư bào tử nấm đông.",
          "sinh_hoc": "Phun định kỳ dung dịch Nano Bạc Đồng sinh học nồng độ 30ppm kết hợp chế phẩm Bacillus subtilis khi lá thành thục chuyển bánh tẻ.",
          "khuyen_cao_chuyen_gia": "Can thiệp sớm trước mùa mưa ẩm kéo dài, phun kỹ ướt đẫm cả mặt dưới của tán lá táo đỏ."
        }
      }
    ]
  },
  {
    "id": "imp_crop_009",
    "topic": "Rau_Cu_Gia_Vi_Va_Nam",
    "name_vi": "Wasabi / Mù tạt tươi Nhật Bản Đà Lạt (Japanese Wasabi)",
    "scientific_name": "Eutrema japonicum (syn. Wasabia japonica)",
    "dia_ban_pho_bien": ["Đà Lạt (Lâm Đồng)", "Lạc Dương (Lâm Đồng)", "Sa Pa (Lào Cai)"],
    "dac_tinh_sinh_thai": "Cây gia vị thảo mộc cao cấp bản địa Nhật Bản, trồng bán thủy canh dưới dòng suối nhân tạo nước lạnh chảy liên tục hoặc nhà màng kiểm soát khí hậu lạnh nghiêm ngặt (12 - 18°C), nước giàu oxy hòa tan, kỵ nhiệt độ > 22°C, giá thể sỏi cuội cát núi lửa rửa sạch vô trùng, pH nước 6.5 - 7.0.",
    "danh_sach_benh": [
      {
        "ten_benh": "Bệnh sọc đen thối lõi củ Wasabi (Black Leg / Phoma Stem Rot)",
        "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Phoma wasabiae"
        },
        "trieu_chung_dien_hinh": [
          "Bó mạch dẫn bên trong thân củ wasabi bị hóa đen hoàn toàn dọc theo chiều dài củ",
          "Lá wasabi bị vàng từ mép lá, cuống lá xuất hiện các sọc dài màu nâu đen lõm nhẹ",
          "Thịt củ bên trong chuyển màu xám đen, mất hoàn toàn vị cay nồng sực mũi đặc trưng của hợp chất allyl isothiocyanate, củ bị rỗng ruột và thối mục nát"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với củ bị thâm do thiếu oxy rễ: Thiếu oxy làm thối nhũn vỏ củ từ ngoài vào trong có mùi hôi húng; Phoma wasabiae phá hủy có chọn lọc các bó mạch dẫn trung tâm củ tạo thành các chấm đen hoặc vệt sọc đen sắc nét bên trong thịt củ.",
        "kiem_tra_thuc_dia": "Cắt một lát mỏng ngang thân củ Wasabi: thấy các vòng chấm đen như mực tàu sắp xếp thành vòng tròn dọc theo hệ thống mạch dẫn lõi củ.",
        "phac_do_vietgap": {
          "canh_tac": "Giữ nhiệt độ nước dòng chảy luôn dưới 16°C bằng hệ thống làm lạnh Chiller, tăng cường sục khí oxy hòa tan > 8 mg/lít.",
          "sinh_hoc": "Khử trùng nước hồi lưu bằng hệ thống đèn cực tím tia UV và sục khí Ozone, bổ sung định kỳ vi khuẩn Bacillus amyloliquefaciens ức chế nấm nước.",
          "khuyen_cao_chuyen_gia": "Tiêu hủy ngay các cây có triệu chứng sọc đen cuống lá để ngăn nấm lây lan theo dòng nước chảy tuần hoàn trong trang trại."
        }
      },
      {
        "ten_benh": "Bệnh thối mềm ướt thân rễ Wasabi vi khuẩn (Bacterial Soft Rot)",
        "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
        "tac_nhan": {
          "loai": "Vi khuẩn",
          "ten_khoa_hoc": "Pectobacterium carotovorum subsp. carotovorum"
        },
        "trieu_chung_dien_hinh": [
          "Phần cổ rễ sát giá thể cuội sỏi bị úng nước màu nâu nhạt rồi nhanh chóng mềm nhũn chảy nước nhầy",
          "Toàn bộ tán lá hình trái tim của Wasabi bị rũ gục xuống chỉ sau một đêm dù giá thể vẫn ướt đẫm",
          "Thịt củ biến thành khối cháo sền sệt bốc mùi hôi thối nồng nặc khó chịu"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với bệnh thối do nấm Phoma: Nấm Phoma gây thối khô lõi củ không bốc mùi hôi thối; vi khuẩn Pectobacterium phá hủy thành tế bào tạo khối nhớt lỏng bốc mùi thối khắm đặc trưng của vi khuẩn thối rữa rau củ.",
        "kiem_tra_thuc_dia": "Dùng ngón tay bóp nhẹ vào thân củ Wasabi: ngón tay lún sâu vào trong củ làm dịch nhớt tanh hôi phì ra ngoài, mô cây nhũn nát hoàn toàn.",
        "phac_do_vietgap": {
          "canh_tac": "Tránh làm trầy xước rễ củ khi thao tác vệ sinh hoặc thu hoạch tỉa lá, kiểm soát mật độ ốc sên và sâu hại cắn phá biểu bì củ.",
          "sinh_hoc": "Xử lý nguồn nước bằng Nano Bạc nồng độ 10ppm kết hợp chế phẩm sinh học Kasugamycin nguồn gốc vi nấm.",
          "khuyen_cao_chuyen_gia": "Tháo cạn luống sỏi bị nhiễm, ngâm sát trùng luống bằng dung dịch Cloramin B hoặc vôi bột 24 giờ trước khi thả cây giống đợt kế tiếp."
        }
      }
    ]
  },
  {
    "id": "imp_crop_010",
    "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
    "name_vi": "Chà là Trung Đông ăn tươi (Barhi Date Palm)",
    "scientific_name": "Phoenix dactylifera cv. Barhi",
    "dia_ban_pho_bien": ["Bình Thuận", "Ninh Thuận", "Sa Đéc (Đồng Tháp)", "Trà Ôn (Vĩnh Long)", "Bến Tre", "Tây Ninh"],
    "dac_tinh_sinh_thai": "Cây cọ thân cột cao cấp nhập khẩu từ Trung Đông, ưa nắng trực tiếp 100%, chịu hạn và chịu mặn rất tốt, sinh trưởng tối ưu trên đất thịt pha cát hoặc đất phù sa bồi cao ráo, pH thích hợp từ 6.5 - 8.0, kỵ ngập úng đỉnh sinh trưởng cổ hũ.",
    "danh_sach_benh": [
      {
        "ten_benh": "Bệnh thối đen đọt non chà là (Black Scorch Disease)",
        "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Thielaviopsis paradoxa (syn. Ceratocystis paradoxa)"
        },
        "trieu_chung_dien_hinh": [
          "Các tàu lá đọt non mới bung có màu nâu đen cháy xém như bị hơ trên ngọn lửa",
          "Bẹ lá bị biến dạng uốn cong queo gãy gập sang một bên, phần mô sát cổ hũ bị thối khô màu đen mun",
          "Nếu nấm ăn sâu vào đỉnh sinh trưởng trung tâm, toàn bộ bó đọt non bị rút rời khỏi thân cây bốc mùi men chua, cây chết đứng hoàn toàn"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với bọ dừa cắn phá: Bọ dừa cắn rách phiến lá thành các dải xơ xác song song dạng răng lược cơ học; Thielaviopsis làm mô thối đen cháy rụi và lan tỏa vào lõi cổ hũ có mùi thơm lên men rượu nhẹ.",
        "kiem_tra_thuc_dia": "Nắm lấy bó ngọn đọt non kéo nhẹ: đọt non bị tuột gốc rời ra dễ dàng, phần gốc đọt thâm đen ngậm nước bốc mùi rượu chua thoang thoảng.",
        "phac_do_vietgap": {
          "canh_tac": "Tránh tưới nước thẳng từ trên ngọn xuống búp đọt non vào buổi chiều tối; khử trùng dụng cụ cắt tỉa tàu dừa bằng cồn hoặc lửa.",
          "sinh_hoc": "Phun tưới đẫm vào cổ hũ đọt non chế phẩm Trichoderma asperellum kết hợp Nano Đồng hữu cơ 400ppm định kỳ vào đầu mùa mưa.",
          "khuyen_cao_chuyen_gia": "Cắt bỏ ngay các tàu lá đọt bị cháy xém và quét keo liền sẹo pha đồng đỏ lên vết cắt ngăn nấm xâm nhập lõi sinh trưởng."
        }
      },
      {
        "ten_benh": "Bệnh đốm lá sần sùi Graphiola chà là (Graphiola Leaf Spot / False Smut)",
        "muc_do_nguy_hiem": "Cao",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Graphiola phoenicis"
        },
        "trieu_chung_dien_hinh": [
          "Cả 2 mặt của các tàu lá già xuất hiện vô số các nốt sần nhỏ màu vàng rồi chuyển sang đen cứng như hạt vừng",
          "Khi hạt sần chín, đỉnh hạt nứt ra giải phóng một sợi lông tơ trắng dài chứa khối bụi bào tử nấm màu vàng nhạt",
          "Tàu lá bị nhiễm dày đặc sẽ chuyển sang màu vàng xỉn, khô giòn từ chóp lá và chết non sớm làm giảm khả năng nuôi buồng quả"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với đốm gỉ sắt: Gỉ sắt tạo mụn bột mịn màu nâu đỏ không có sợi lông tơ; Graphiola tạo các mụn sần chai cứng như đá đen nhỏ và bật ra sợi lông tơ màu trắng ngà từ đỉnh mụn.",
        "kiem_tra_thuc_dia": "Dùng móng tay cào vào nốt sần đen trên lá chà là: nốt sần cộm cứng trơ ra như hạt sỏi nhỏ bám chắc vào biểu bì lá gai dầy.",
        "phac_do_vietgap": {
          "canh_tac": "Cắt tỉa toàn bộ các tàu lá già tầng sát đất bị nhiễm nặng đem gom đốt tiêu hủy, tạo độ thoáng quanh gốc cây.",
          "sinh_hoc": "Phun phòng nấm đối kháng Chaetomium kết hợp dầu khoáng SK Enspray 99EC nồng độ 0.5% để bịt kín ổ mụn sần.",
          "khuyen_cao_chuyen_gia": "Giữ khoảng cách trồng tối thiểu 7m x 7m để đảm bảo ánh nắng chiếu rọi xuyên qua tán lá chà là."
        }
      }
    ]
  },
  {
    "id": "imp_crop_011",
    "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi",
    "name_vi": "Cherry nhiệt đới Surinam / Sơ ri Brazil (Surinam Cherry)",
    "scientific_name": "Eugenia uniflora",
    "dia_ban_pho_bien": ["Đà Lạt (Lâm Đồng)", "Long Khánh (Đồng Nai)", "Bình Phước", "Vĩnh Long", "Cần Thơ"],
    "dac_tinh_sinh_thai": "Cây bụi thân gỗ sống lâu năm nguồn gốc Nam Mỹ, quả có 8 múi khía hình lồng đèn đỏ rực rỡ, thích nghi tốt từ vùng khí hậu mát ôn đới đến nhiệt đới gió mùa, đất phù sa bồi hoặc đất đỏ bazan giàu mùn, pH đất 5.5 - 6.5, chịu hạn khá tốt.",
    "danh_sach_benh": [
      {
        "ten_benh": "Bệnh thán thư đốm lá và thối nứt quả cherry Surinam (Anthracnose)",
        "muc_do_nguy_hiem": "Cao",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Colletotrichum gloeosporioides"
        },
        "trieu_chung_dien_hinh": [
          "Trên phiến lá bóng xuất hiện các chấm nâu tròn sau lan rộng thành mảng cháy khô màu xám tro có viền đỏ đậm",
          "Quả cherry có múi hình múi khế xuất hiện các vết đốm tròn trũng trũng màu nâu đen, vỏ quả bị nứt nẻ chảy dịch ngọt",
          "Quả non bị chai sượng rụng sớm, quả chín bị thối nhũn một bên múi làm mất giá trị thương phẩm"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với ruồi đục quả chích: Ruồi đục quả có lỗ kim chích rất nhỏ ở tâm và bên trong có dòi giòi bò ngoe nguẩy; thán thư không có dòi mà mô thịt thối lõm hình chén có khối bào tử màu hồng cam khi ẩm.",
        "kiem_tra_thuc_dia": "Dùng kính lúp kiểm tra vết đốm trên múi quả cherry: thấy các vòng tròn chấm đen đồng tâm lõm sâu, không thấy vết lỗ thủng do ruồi chích.",
        "phac_do_vietgap": {
          "canh_tac": "Cắt tỉa thông thoáng cành tăm trong tán, quét dọn sạch quả rụng dưới tán gốc gom tiêu hủy.",
          "sinh_hoc": "Phun phòng chế phẩm vi sinh Bacillus subtilis kết hợp Nano Bạc Đồng 20ppm định kỳ 15 ngày/lần từ khi cây nở hoa.",
          "khuyen_cao_chuyen_gia": "Bao bọc chùm quả bằng túi lưới thoáng khí chuyên dụng ngăn côn trùng và nấm xâm nhiễm mùa mưa ẩm."
        }
      },
      {
        "ten_benh": "Bệnh đốm vi khuẩn xì mủ lá non Cherry (Bacterial Leaf Spot)",
        "muc_do_nguy_hiem": "Trung bình",
        "tac_nhan": {
          "loai": "Vi khuẩn",
          "ten_khoa_hoc": "Pseudomonas syringae pv. syringae"
        },
        "trieu_chung_dien_hinh": [
          "Lá non mới nhú xuất hiện các đốm nhỏ sũng nước màu xanh đậm, sau chuyển sang màu nâu đen",
          "Xung quanh vết đốm luôn có quầng vàng sáng rõ bao bọc, đọt non bị chùn lại cong queo",
          "Khi trời mưa phùn sương đêm, các đốm bệnh ứa ra các giọt dịch màu trắng đục dính bám"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với bệnh đốm nấm Cercospora: Đốm vi khuẩn có quầng vàng trong suốt ngậm nước xung quanh và ứa giọt dịch nhớt; đốm nấm khô giòn và không ngậm nước.",
        "kiem_tra_thuc_dia": "Soi ngược phiến lá dưới ánh nắng mặt trời: quầng vàng sáng rực bao quanh vết nâu sũng nước nhìn thấy rất rõ nét.",
        "phac_do_vietgap": {
          "canh_tac": "Không bón phân đạm quá mức trong giai đoạn cây bung đọt non; duy trì mật độ tán cây đón nắng tốt.",
          "sinh_hoc": "Phun kháng sinh sinh học Kasugamycin kết hợp chế phẩm sinh học Chitosan 1.5% phòng ngừa đợt lộc non.",
          "khuyen_cao_chuyen_gia": "Tuân thủ thời gian cách ly sinh học 3 - 5 ngày trước thu hoạch an toàn."
        }
      }
    ]
  },
  {
    "id": "imp_crop_012",
    "topic": "Cay_Nhap_Khau_Kinh_Te_Cao",
    "name_vi": "Cây hạt dẻ cười nhập ngoại (Pistachio Tree)",
    "scientific_name": "Pistacia vera",
    "dia_ban_pho_bien": ["Bình Thuận", "Ninh Thuận", "Gia Lai", "Đắk Lắk"],
    "dac_tinh_sinh_thai": "Cây thân gỗ lấy hạt nhập khẩu từ Trung Đông/Địa Trung Hải, ưa khí hậu bán khô hạn mùa hè nóng khô mùa đông có tích lũy giờ lạnh, đất sỏi đồi cát pha đá vôi thoát nước cực nhanh, pH đất 7.0 - 8.2, rất nhạy cảm với úng rễ và ẩm độ không khí cao.",
    "danh_sach_benh": [
      {
        "ten_benh": "Bệnh cháy đọt và đốm mắt chùm quả hạt dẻ cười (Panicle and Shoot Blight)",
        "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Botryosphaeria dothidea"
        },
        "trieu_chung_dien_hinh": [
          "Các chùm hoa và chùm hạt non đang phát triển đột ngột bị khô héo, chuyển sang màu nâu sẫm rồi đen mun",
          "Chùm hạt dẻ bị chết khô dính chặt trên cành không chịu rụng suốt cả mùa đông",
          "Các cành mang quả xuất hiện các vết loét hình thoi thâm đen, nhựa gôm ứa ra làm khô chết toàn bộ phần cành phía trên"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với khô chùm do thiếu vi lượng Boron: Thiếu Boron làm rụng hoa thụ phấn kém không hình thành hạt; Botryosphaeria làm cả chùm hạt đã hình thành bị đen khô mủn và kèm theo vết loét xì mủ trên cành gỗ.",
        "kiem_tra_thuc_dia": "Cắt ngang cành bị khô: lớp mô vỏ và tầng sinh mô mạch dẫn dưới vỏ bị thâm đen hoàn toàn, cành khô giòn gãy rụm.",
        "phac_do_vietgap": {
          "canh_tac": "Cắt tỉa triệt để toàn bộ các cành bị loét và chùm quả khô sót lại đem đốt tiêu hủy cách ly.",
          "sinh_hoc": "Phun nấm đối kháng Trichoderma harzianum kết hợp dịch chiết nấm men kích kháng SAR vào giai đoạn bung nụ hoa.",
          "khuyen_cao_chuyen_gia": "Phun bảo vệ chùm quả sau các trận mưa rào bất thường trong mùa khô hanh bằng dung dịch Nano Bạc Đồng sinh học."
        }
      },
      {
        "ten_benh": "Bệnh héo rũ Verticillium tắc mạch dẫn (Verticillium Wilt)",
        "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Verticillium dahliae"
        },
        "trieu_chung_dien_hinh": [
          "Các lá trên một hoặc một vài cành bị biến vàng từ mép lá, sau đó khô giòn cong queo rũ xuống",
          "Triệu chứng lan dần theo từng cành đơn lẻ (hiện tượng héo một bên tán) trước khi làm chết cả cây",
          "Mạch gỗ bên trong cành thân cây hạt dẻ cười bị biến màu nâu đen sẫm chạy dọc theo thớ gỗ"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với bệnh thối rễ Phytophthora: Phytophthora làm vàng héo đồng loạt cả cây và rễ tơ thối nhũn đen; Verticillium héo khô từng cành riêng biệt trong khi bộ rễ tơ ban đầu trông vẫn nguyên vẹn.",
        "kiem_tra_thuc_dia": "Dùng dao vát một mảnh vỏ cành bị héo: thấy các vệt sọc màu nâu sẫm chạy dài theo thớ gỗ mạch dẫn bên dưới lớp giác gỗ.",
        "phac_do_vietgap": {
          "canh_tac": "Sử dụng gốc ghép kháng bệnh Verticillium (như dòng Pistacia integerrima Pioneer Gold 1); không luân canh hoặc trồng xen với cây họ Cà (cà chua, ớt, khoai tây).",
          "sinh_hoc": "Tưới gốc định kỳ chế phẩm vi khuẩn đối kháng Bacillus subtilis phân lập cao kết hợp xạ khuẩn Streptomyces.",
          "khuyen_cao_chuyen_gia": "Tiêu hủy cây chết và phơi đất xử lý phủ bạt năng lượng mặt trời (soil solarization) nhiệt độ cao tiêu diệt hạch nấm trong đất."
        }
      }
    ]
  },
  {
    "id": "imp_crop_013",
    "topic": "Cay_Nhap_Khau_Kinh_Te_Cao",
    "name_vi": "Mắc ca Tây Nguyên cao sản (Macadamia)",
    "scientific_name": "Macadamia integrifolia",
    "dia_ban_pho_bien": ["Đắk Lắk", "Lâm Đồng (Đơn Dương, Lâm Hà)", "Gia Lai", "Đắk Nông", "Sơn La (Mai Sơn)"],
    "dac_tinh_sinh_thai": "Cây thân gỗ lấy hạt 'nữ hoàng các loại hạt' nguồn gốc Úc, ưa đất đỏ bazan sâu xốp màu mỡ, thoát nước tốt, pH đất 5.5 - 6.5, cần thời tiết se lạnh khô ráo để phân hóa mầm hoa (15 - 18°C), hoa dạng chuỗi dài rất nhạy cảm với sương muối và nấm ẩm.",
    "danh_sach_benh": [
      {
        "ten_benh": "Bệnh thán thư rụng chuỗi hoa và thối nứt quả non Mắc ca (Raceme Blight / Anthracnose)",
        "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Colletotrichum acutatum / Colletotrichum gloeosporioides"
        },
        "trieu_chung_dien_hinh": [
          "Chuỗi hoa mắc ca đang nở bị thâm đen từ ngọn chuỗi hoặc cuống hoa nhỏ, nụ hoa bị thối nhũn rụng lả tả",
          "Khi trời có sương mù ẩm ướt, cả chuỗi hoa dính bết lại thành một búi màu nâu đen bốc mùi mốc, không thể thụ phấn đậu quả",
          "Vỏ quả non xuất hiện các đốm tròn trũng sâu màu nâu đậm, quả bị teo thắt và rụng non hàng loạt"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với hoa rụng do gió khô nóng hoặc thiếu nước: Rụng do thời tiết hoa khô giòn tự nhiên màu vàng nhạt; thán thư hoa thâm đen dính bết lại thành chùm bốc mùi mốc nấm có chấm nhầy màu cam hồng.",
        "kiem_tra_thuc_dia": "Rung nhẹ cành hoa: nụ hoa rơi rụng lả tả xuống đất, cuống hoa sót lại trên cành bị thâm đen có chất dịch dính ngón tay.",
        "phac_do_vietgap": {
          "canh_tac": "Tỉa cành tạo tán hình nấm thông thoáng ngay sau vụ thu hoạch, đón ánh nắng chiếu sâu vào tâm tán cây.",
          "sinh_hoc": "Phun phòng luân phiên nấm đối kháng Chaetomium kết hợp chế phẩm sinh học vi khuẩn Bacillus amyloliquefaciens nồng độ 0.2% giai đoạn hoa nhú mầm mắt cua 3 - 5cm.",
          "khuyen_cao_chuyen_gia": "Tuyệt đối không phun thuốc trừ sâu hóa học giai đoạn hoa nở rộ làm chết ong mật thụ phấn hoa mắc ca."
        }
      },
      {
        "ten_benh": "Bệnh xì mủ thối loét thân gốc Phytophthora (Phytophthora Trunk Canker)",
        "muc_do_nguy_hiem": "Nặng",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Phytophthora cinnamomi"
        },
        "trieu_chung_dien_hinh": [
          "Phần vỏ thân sát mặt đất xuất hiện các vết loét thâm ướt, nhựa mủ màu nâu đỏ ứa ra rỉ chảy dọc theo thân",
          "Vỏ cây chỗ loét bị nứt nẻ, bong tróc ra, cạo lớp vỏ thấy lớp tầng sinh mô mạch gỗ bên dưới có màu nâu đỏ sẫm như thịt bò ôi",
          "Tán lá phía trên bị vàng úa rụng lác đác, cành khô dần từ ngọn xuống và cây có thể chết đứng sau 1 - 2 mùa mưa"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với vết xì mủ do mọt đục thân cành: Mọt đục có lỗ đùn mùn cưa mịn màu trắng ngà ra ngoài vỏ thân; Phytophthora không có mùn cưa mà là mủ nhựa tự nhiên rỉ ra từ vết nứt vỏ thâm ướt rộng.",
        "kiem_tra_thuc_dia": "Dùng dao cạo nhẹ lớp biểu bì vỏ thân chỗ ứa mủ: thấy mô vỏ bên trong thối nhũn màu nâu đỏ đậm có ranh giới rõ ràng với phần mô gỗ khỏe màu trắng kem.",
        "phac_do_vietgap": {
          "canh_tac": "Làm sạch cỏ dại quanh gốc bán kính 1m, không vun đất quá cao vào cổ rễ cây mắc ca, khơi thông rãnh thoát nước vườn.",
          "sinh_hoc": "Cạo sạch vết loét đến phần gỗ khỏe rồi quét dung dịch Nano Bạc Đồng sinh học kết hợp chế phẩm Trichoderma paste đặc lên miệng vết thương.",
          "khuyen_cao_chuyen_gia": "Quét vôi tôi pha đồng sunfat quanh gốc thân cao 1m định kỳ vào đầu mùa mưa để bảo vệ cổ rễ."
        }
      }
    ]
  },
  {
    "id": "imp_crop_014",
    "topic": "Cay_Nhap_Khau_Kinh_Te_Cao",
    "name_vi": "Cà chua thân gỗ Tamarillo (Tree Tomato Tamarillo)",
    "scientific_name": "Solanum betaceum (syn. Cyphomandra betacea)",
    "dia_ban_pho_bien": ["Đà Lạt (Lâm Đồng)", "Lạc Dương (Lâm Đồng)", "Sa Pa (Lào Cai)"],
    "dac_tinh_sinh_thai": "Cây thân gỗ nhỏ lâu năm họ Cà nguồn gốc dãy Andes Nam Mỹ, thích hợp vùng cao 1.000 - 2.000m khí hậu mát mẻ quanh năm (15 - 22°C), rễ ăn nông rất nhạy cảm với ngập úng và gió bão, đất đỏ bazan hoặc đất mùn hữu cơ thoát nước tốt, pH 5.8 - 6.5.",
    "danh_sach_benh": [
      {
        "ten_benh": "Bệnh mốc sương thối lá quả Tamarillo (Late Blight)",
        "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Phytophthora infestans"
        },
        "trieu_chung_dien_hinh": [
          "Mép phiến lá lớn xuất hiện các vết đốm ủng nước màu xanh xám loang nhanh thành mảng cháy khô màu nâu đen",
          "Khi trời nhiều sương mù mặt dưới phiến lá phủ một lớp màng mốc tơ màu trắng xám bao quanh ranh giới vết bệnh",
          "Quả cà chua thân gỗ xuất hiện các vệt loang màu nâu sô-cô-la cứng sần sùi, quả bị thối khô teo tóp dính trên cành"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với bệnh đốm vòng Alternaria: Mốc sương lây lan nhanh như lửa cháy mô bị sũng nước và có lớp màng nấm trắng ở mặt dưới lá; Alternaria phát triển chậm có các vòng tròn đồng tâm khô giòn rõ rệt.",
        "kiem_tra_thuc_dia": "Lật mặt dưới lá non vào sáng sớm: thấy lớp màng mốc trắng xám mịn như bụi tuyết giăng quanh mép vết cháy sũng nước.",
        "phac_do_vietgap": {
          "canh_tac": "Cố định cọc chống đỡ cành tránh gió quật đổ gãy tán cây; ngắt sạch lá già tầng đáy cách mặt đất 50cm.",
          "sinh_hoc": "Phun phòng luân phiên nấm vi sinh đối kháng Chaetomium kết hợp chế phẩm Nano Bạc Đồng 35ppm và Phosphonate sinh học.",
          "khuyen_cao_chuyen_gia": "Phun phòng sớm trước các đợt áp thấp nhiệt đới gây mưa dầm kéo dài tại vùng núi cao Đà Lạt."
        }
      },
      {
        "ten_benh": "Bệnh héo xanh vi khuẩn Tamarillo (Bacterial Wilt)",
        "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
        "tac_nhan": {
          "loai": "Vi khuẩn",
          "ten_khoa_hoc": "Ralstonia solanacearum"
        },
        "trieu_chung_dien_hinh": [
          "Cây đang xanh tốt đột ngột bị rũ gục các đọt non và lá vào ban ngày khi trời nắng gắt",
          "Ban đêm cây hơi gượng lại, nhưng chỉ sau 2 - 3 ngày toàn bộ cây cà chua thân gỗ héo rũ hoàn toàn trong khi lá vẫn giữ màu xanh lục",
          "Gốc thân cây sát cổ rễ bị sũng nước nhẹ, rễ tơ bị thối mục mủn đen"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với bệnh héo vàng Fusarium: Héo vàng lá vàng rực từ gốc lên ngọn rụng dần từng lá; héo xanh cây gục đột ngột khi lá vẫn còn xanh tươi nguyên vẹn trên cành.",
        "kiem_tra_thuc_dia": "Cắt một đoạn thân bánh tẻ cắm vào cốc nước thủy tinh trong suốt: sau 1 - 2 phút các dòng dịch vi khuẩn màu trắng sữa đùn ra từ bó mạch dẫn chìm dần xuống đáy cốc (thử nghiệm dòng dịch vi khuẩn).",
        "phac_do_vietgap": {
          "canh_tac": "Nhổ bỏ cây bệnh nặng và đào toàn bộ bầu rễ cho vào bao nilon tiêu hủy; rải vôi bột khử trùng hố trồng.",
          "sinh_hoc": "Tưới phòng gốc định kỳ nấm đối kháng Trichoderma phối hợp chủng vi khuẩn đối kháng Bacillus subtilis và chế phẩm sinh học Kasugamycin.",
          "khuyen_cao_chuyen_gia": "Tuyệt đối không luân canh hoặc trồng xen Tamarillo trên đất vừa canh tác cà chua, ớt, khoai tây vụ trước."
        }
      }
    ]
  },
  {
    "id": "imp_crop_015",
    "topic": "Rau_Cu_Gia_Vi_Va_Nam",
    "name_vi": "Nấm mối đen nông nghiệp công nghệ cao (Black Termite Mushroom)",
    "scientific_name": "Oudemansiella radicata (syn. Xerula radicata)",
    "dia_ban_pho_bien": ["Đà Lạt (Lâm Đồng)", "Củ Chi (TP.HCM)", "Long Khánh (Đồng Nai)", "Bình Phước", "Tam Bình (Vĩnh Long)"],
    "dac_tinh_sinh_thai": "Nấm ăn đặc sản kinh tế cao nuôi trồng công nghệ cao trong nhà lạnh khép kín, cơ chất mùn cưa cao su đóng bịch phối trộn cám bắp cám gạo dinh dưỡng, phủ lớp giá thể đất sạch hoặc cát khoáng sau khi ươm tơ, nhiệt độ nuôi trồng 24 - 28°C, độ ẩm không khí 85 - 95%, kỵ ánh sáng trực tiếp.",
    "danh_sach_benh": [
      {
        "ten_benh": "Bệnh mốc xanh cạnh tranh giá thể bịch phôi nấm (Green Mold)",
        "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Trichoderma harzianum / Trichoderma viride"
        },
        "trieu_chung_dien_hinh": [
          "Bên trong bịch phôi mùn cưa xuất hiện các đám sợi nấm màu trắng mịn sau nhanh chóng biến thành màu xanh lục đậm hoặc xanh lá mạ",
          "Tơ nấm mối đen bị bao vây, tiết ra dịch màu vàng cam rồi teo lụi biến mất hoàn toàn",
          "Bịch phôi bị mốc xanh hoàn toàn không thể bật mầm quả thể nấm mối đen, bốc mùi chua nồng của nấm hoại sinh"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với màu dịch tiết sinh lý bình thường của tơ nấm mối đen: Tơ nấm khỏe tiết dịch màu hổ phách nâu nhạt nhưng cơ chất vẫn trắng ngà; mốc xanh tạo đám bột màu xanh lục bám thành mảng lớn phá hủy toàn bộ mạng tơ nấm.",
        "kiem_tra_thuc_dia": "Quan sát qua màng nilon bịch phôi: thấy các mảng bột phấn màu xanh lục mạ lan rộng nhanh chóng, bóp nhẹ thấy mùn cưa nhão nát có mùi chua.",
        "phac_do_vietgap": {
          "canh_tac": "Hấp tiệt trùng cơ chất bịch phôi đạt nhiệt độ 100°C trong 10 - 12 giờ hoặc nồi áp suất 121°C trong 90 phút; phòng cấy giống vô trùng bằng đèn UV-C.",
          "sinh_hoc": "Sử dụng giống nấm mối đen thuần chủng khỏe tơ; vệ sinh định kỳ nhà nuôi bằng cồn y tế hoặc vôi bột rải nền nhà.",
          "khuyen_cao_chuyen_gia": "Cách ly và mang ngay các bịch nhiễm mốc xanh ra khỏi phòng nuôi để tránh phát tán bào tử sang các bịch lân cận."
        }
      },
      {
        "ten_benh": "Bệnh đốm thâm nứt mũ nấm mối đen vi khuẩn (Bacterial Blotch)",
        "muc_do_nguy_hiem": "Nặng",
        "tac_nhan": {
          "loai": "Vi khuẩn",
          "ten_khoa_hoc": "Pseudomonas tolaasii"
        },
        "trieu_chung_dien_hinh": [
          "Trên tai nấm mối đen xuất hiện các đốm trũng màu vàng nâu rồi chuyển sang màu nâu đen ướt nhờn",
          "Vết bệnh lan rộng làm mũ nấm bị méo mó, nứt nẻ, chảy dịch nhờn dính",
          "Cuống nấm bị thâm đen và nhũn nát từ chân nấm lên, tai nấm bốc mùi chua tanh làm mất hoàn toàn giá trị thương phẩm xuất khẩu"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với đốm do giọt nước đọng trên mũ nấm: Giọt nước đọng lau khô mũ nấm vẫn bóng láng chắc thịt; đốm vi khuẩn làm mũ nấm bị lõm sâu trơn nhớt dính tay và thịt nấm biến màu xám đen.",
        "kiem_tra_thuc_dia": "Chạm ngón tay vào đốm nâu trên tai nấm: thấy dịch nhờn trơn trượt dính vào ngón tay, ngửi thấy mùi tanh tanh của vi khuẩn phân hủy protein nấm.",
        "phac_do_vietgap": {
          "canh_tac": "Không tưới phun sương trực tiếp hạt nước to lên tai nấm khi sắp thu hoạch; kiểm soát hệ thống tạo ẩm siêu âm hạt mịn < 5 micron; duy trì quạt thông khí nhẹ.",
          "sinh_hoc": "Phun sương phòng ngừa bằng dung dịch Nano Bạc nồng độ 5ppm hoặc chế phẩm vi sinh đối kháng Bacillus subtilis.",
          "khuyen_cao_chuyen_gia": "Hạ độ ẩm nhà nấm xuống 80% trong 2 - 3 giờ sau mỗi lần tưới ẩm để bề mặt tai nấm khô ráo nước tự do."
        }
      }
    ]
  },
  {
    "id": "imp_crop_016",
    "topic": "Rau_Cu_Gia_Vi_Va_Nam",
    "name_vi": "Nấm hầu thủ / Nấm đầu khỉ công nghệ cao (Lion's Mane Mushroom)",
    "scientific_name": "Hericium erinaceus",
    "dia_ban_pho_bien": ["Đà Lạt (Lâm Đồng)", "Mộc Châu (Sơn La)", "Hà Nội", "TP.HCM"],
    "dac_tinh_sinh_thai": "Nấm dược liệu quý nhập ngoại có hình dáng như chùm tua gai màu trắng ngà của bờm sư tử, nuôi trồng phòng lạnh công nghệ cao, cơ chất mùn cưa gỗ mềm phối bột ngô cám gạo, nhiệt độ nuôi sợi 20 - 24°C, nhiệt độ kích quả thể lạnh 16 - 20°C, độ ẩm 85 - 90%, cần ánh sáng tán xạ nhẹ.",
    "danh_sach_benh": [
      {
        "ten_benh": "Bệnh vàng ố và thối nhầy tua nấm hầu thủ vi khuẩn (Bacterial Yellowing and Rot)",
        "muc_do_nguy_hiem": "Nặng",
        "tac_nhan": {
          "loai": "Vi khuẩn",
          "ten_khoa_hoc": "Pseudomonas tolaasii / Pseudomonas gingeri"
        },
        "trieu_chung_dien_hinh": [
          "Các tua gai trắng muốt của nấm hầu thủ đột ngột chuyển sang màu vàng rơm, vàng cam ố bẩn",
          "Đầu các sợi tua gai bị nhũn nước, dính bết lại với nhau thành từng búi nhờn dính",
          "Quả thể nấm teo tóp biến dạng, bốc mùi hôi thối khó chịu, không thể chiết xuất hoạt chất hericenone và erinacine"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với nấm già tự nhiên đổi màu: Nấm hầu thủ già chuyển sang màu vàng ngà khô ráo tự nhiên; nấm nhiễm vi khuẩn biến màu vàng ố ướt nhầy thối rữa và có giọt dịch nhầy dính bết các tua nấm.",
        "kiem_tra_thuc_dia": "Dùng tay sờ vào chùm tua nấm: các sợi gai nhũn dính bết vào tay, bóp nhẹ thấy dịch nhớt rỉ ra bốc mùi chua nồng.",
        "phac_do_vietgap": {
          "canh_tac": "Tránh để giọt nước ngưng tụ trên trần nhà lạnh nhỏ giọt trực tiếp xuống tai nấm; điều chỉnh hệ thống thông gió đối lưu nhẹ.",
          "sinh_hoc": "Khử trùng không khí nhà nuôi định kỳ bằng đèn tia cực tím UV và máy tạo khí ozone loãng khi chưa treo nấm; phun dung dịch Nano Bạc nồng độ 5ppm.",
          "khuyen_cao_chuyen_gia": "Thu hoạch sớm ngay khi phát hiện chớm vàng đầu gai để hạn chế tổn thất kinh tế."
        }
      },
      {
        "ten_benh": "Bệnh mốc cam phấn phủ bề mặt phôi nấm (Orange Bread Mold)",
        "muc_do_nguy_hiem": "Cao",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Chrysonilia sitophila (syn. Neurospora sitophila)"
        },
        "trieu_chung_dien_hinh": [
          "Trên cổ nút bông và bề mặt bịch phôi nấm hầu thủ xuất hiện lớp sợi nấm màu cam đào hoặc hồng phấn phát triển cực nhanh",
          "Lớp nấm mốc bung ra vô số bụi bào tử màu cam rực rỡ bay lơ lửng khắp không gian nhà nuôi",
          "Sợi nấm mốc cam ăn sâu chiếm đoạt toàn bộ dưỡng chất của bịch phôi làm tơ nấm hầu thủ ngạt thở chết nghẽn"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với sắc tố tự nhiên của phôi nấm: Nấm hầu thủ tơ thuần khiết màu trắng ngà sạch sẽ; mốc Neurospora có màu cam sáng rực rỡ và phát tán bụi phấn bào tử mịn màng vào không khí.",
        "kiem_tra_thuc_dia": "Chạm nhẹ vào cổ nút bông: thấy đám bụi phấn màu cam bay túa ra như khói bụi màu gạch non.",
        "phac_do_vietgap": {
          "canh_tac": "Kiểm tra kỹ nút bông không để bị ẩm ướt trong quá trình hấp khử trùng; vứt bỏ ngay bịch nhiễm ra khỏi phòng lạnh trước khi bào tử bung tỏa.",
          "sinh_hoc": "Vệ sinh giàn kệ bằng dung dịch cồn y tế 70 độ kết hợp phun xịt Nano Bạc sát khuẩn bề mặt kệ định kỳ.",
          "khuyen_cao_chuyen_gia": "Giảm bớt tỷ lệ cám bắp thừa trong công thức phối trộn cơ chất mùa hè ẩm ướt."
        }
      }
    ]
  },
  {
    "id": "imp_crop_017",
    "topic": "Cay_Nhap_Khau_Kinh_Te_Cao",
    "name_vi": "Nấm đông trùng hạ thảo nhân tạo nuôi phòng lạnh (Cordyceps)",
    "scientific_name": "Cordyceps militaris",
    "dia_ban_pho_bien": ["Đà Lạt (Lâm Đồng)", "Thủ Đức (TP.HCM)", "Hà Nội", "Cần Thơ", "Vĩnh Long"],
    "dac_tinh_sinh_thai": "Dược liệu quý cao cấp nuôi trồng nhân tạo trong phòng sạch vô trùng đạt chuẩn Cleanroom, cơ chất gạo lứt bổ sung nước cốt dừa, dịch nhộng tằm, peptone và khoáng vi lượng, nhiệt độ ươm sợi 20 - 22°C (tối), nhiệt độ kích sáng tạo quả thể 18 - 20°C (độ ẩm 80 - 90%, ánh sáng 1.000 lux chu kỳ 12h/12h).",
    "danh_sach_benh": [
      {
        "ten_benh": "Bệnh mốc xanh lục bội nhiễm cơ chất gạo lứt (Green Mold Contamination)",
        "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Penicillium digitatum / Aspergillus flavus"
        },
        "trieu_chung_dien_hinh": [
          "Bên trong hộp hoặc lọ thủy tinh nuôi cấy xuất hiện các đốm mốc màu xanh lục hoặc vàng hoa cau trên bề mặt khối gạo lứt",
          "Sợi nấm đông trùng hạ thảo màu cam bị ức chế, không thể bật lên các ngọn quả thể nấm dạng ngón tay",
          "Khối cơ chất bị thối nhão chuyển sang màu xám đen, bốc mùi ẩm mốc khó chịu và có nguy cơ sinh độc tố mycotoxin"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với nấm đông trùng hạ thảo tơ màu cam thuần khiết: Nấm Cordyceps có màu cam cà rốt đồng nhất; mốc tạp nhiễm có màu xanh lục ô-liu hoặc xanh lá mạ bao phủ cơ chất dạng bột mịn.",
        "kiem_tra_thuc_dia": "Soi đáy hộp nuôi cấy dưới ánh đèn LED kiểm tra: thấy cơ chất gạo lứt bị đổi màu xanh xám loang lổ và sợi nấm cam bị teo quắt.",
        "phac_do_vietgap": {
          "canh_tac": "Thực hiện nghiêm ngặt quy trình hấp autoclave cơ chất ở 121°C trong 45 phút; thao tác cấy truyền giống trong tủ cấy vô trùng Clean Bench thổi khí Laminar màng lọc HEPA.",
          "sinh_hoc": "Sử dụng nguồn giống thuần chủng đời F1 khỏe mạnh; vệ sinh phòng cấy định kỳ bằng cồn 70 độ và khử trùng buồng nuôi bằng khí Ozone trước mỗi mẻ cấy mới.",
          "khuyen_cao_chuyen_gia": "Tiêu hủy triệt để các lọ nhiễm mốc bằng cách hấp tiệt trùng trước khi rửa bình để tránh phát tán bào tử mốc ra môi trường xung quanh."
        }
      },
      {
        "ten_benh": "Bệnh thối nhũn teo ngọn quả thể vi khuẩn (Bacterial Soft Rot of Fruiting Bodies)",
        "muc_do_nguy_hiem": "Nặng",
        "tac_nhan": {
          "loai": "Vi khuẩn",
          "ten_khoa_hoc": "Bacillus amyloliquefaciens hoang dã / Pseudomonas spp."
        },
        "trieu_chung_dien_hinh": [
          "Các ngọn nấm màu cam đang vươn cao đột ngột bị nhũn nước ở phần chóp ngọn, chuyển sang màu nâu đen ướt nhờn",
          "Thân cây nấm bị gục ngã ngang trên bề mặt cơ chất, dịch nhờn tiết ra làm dính bết các cây nấm xung quanh",
          "Mùi hôi chua nồng bốc lên khi mở nắp hộp kiểm tra, hàm lượng cordycepin và adenosine bị phân hủy hoàn toàn"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với hiện tượng ngọn nấm bị cháy khô do quá nhiệt bóng đèn: Cháy nhiệt làm ngọn nấm khô quắt màu nâu đỏ không chảy nước nhờn; nhiễm khuẩn làm ngọn nấm nhũn nát chảy dịch nhớt thối rữa.",
        "kiem_tra_thuc_dia": "Dùng panh vô trùng gắp nhẹ ngọn nấm: thân nấm đứt rời nhũn nát như cọng bún thiu, dịch nhớt dính chặt vào đầu panh.",
        "phac_do_vietgap": {
          "canh_tac": "Không để đọng nước trên nắp hộp cấy nhỏ giọt xuống quả thể; duy trì nhiệt độ phòng nuôi ổn định 18 - 20°C không để sốc nhiệt > 23°C.",
          "sinh_hoc": "Khử trùng nắp hộp và màng thoáng khí bằng cồn y tế; kiểm tra định kỳ chỉ số vô trùng buồng nuôi cấy.",
          "khuyen_cao_chuyen_gia": "Hạ độ ẩm phòng xuống 75% trong 24 giờ ngay khi phát hiện chớm nhũn ngọn để ngăn vi khuẩn lây lan."
        }
      }
    ]
  },
  {
    "id": "imp_crop_018",
    "topic": "Cay_Nhap_Khau_Kinh_Te_Cao",
    "name_vi": "Quả mâm xôi đỏ / Phúc bồn tử Đà Lạt (Red Raspberry)",
    "scientific_name": "Rubus idaeus",
    "dia_ban_pho_bien": ["Đà Lạt (Lâm Đồng)", "Lạc Dương (Lâm Đồng)", "Mộc Châu (Sơn La)", "Sa Pa (Lào Cai)"],
    "dac_tinh_sinh_thai": "Cây bụi thân gai ôn đới cao cấp, trồng trong nhà màng che mưa trên luống cao hoặc chậu giá thể xơ dừa cao 40cm, ưa khí hậu mát lạnh (18 - 24°C), giá thể tơi xốp giàu hữu cơ, thoát nước tuyệt hảo, pH giá thể 5.5 - 6.5, cực kỳ mẫn cảm với đọng nước chân rễ.",
    "danh_sach_benh": [
      {
        "ten_benh": "Bệnh thối xám nát quả mâm xôi (Botrytis Gray Mold)",
        "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Botrytis cinerea"
        },
        "trieu_chung_dien_hinh": [
          "Các múi nhỏ của quả phúc bồn tử chín mọng bị úng nước màu nâu nhạt, sau đó quả bị mềm nhũn chảy nước",
          "Bao phủ toàn bộ quả là một lớp sợi nấm và chùm bào tử màu xám tro dày đặc như lớp nỉ",
          "Quả khô quắt lại trên cành thành quả xác ướp (mummy), lây lan sang các quả xanh bên cạnh làm thối toàn bộ chùm"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với bệnh thối quả Rhizopus: Rhizopus sợi nấm màu trắng dài có các đầu chấm đen như đầu đinh ghim phát triển cực nhanh trong vài giờ; Botrytis có lớp lông ngắn màu xám tro phát tán bụi khói khi chạm nhẹ.",
        "kiem_tra_thuc_dia": "Dùng tay gõ nhẹ vào cành mang quả bệnh: một đám bụi khói bào tử màu xám tro bay mù mịt trong không khí; quả thối nhũn dính bết vào ngón tay.",
        "phac_do_vietgap": {
          "canh_tac": "Buộc cố định các cành mâm xôi vào giàn dây chữ V giúp tán thông thoáng; hái quả vào buổi sáng ráo sương; loại bỏ ngay quả thối ra túi rác.",
          "sinh_hoc": "Phun phòng định kỳ nấm đối kháng Chaetomium kết hợp vi khuẩn Bacillus subtilis chủng đặc hiệu và chế phẩm Nano Bạc hữu cơ.",
          "khuyen_cao_chuyen_gia": "Giữ ẩm độ không khí nhà màng < 75% bằng quạt thông gió công nghiệp trong giai đoạn thu hoạch rộ."
        }
      },
      {
        "ten_benh": "Bệnh đốm mắt cua nứt thân cành Rubus (Spur Blight / Cane Spot)",
        "muc_do_nguy_hiem": "Nặng",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Elsinoë veneta (syn. Didymella applanata)"
        },
        "trieu_chung_dien_hinh": [
          "Trên thân cành non xuất hiện các vết đốm nhỏ hình tròn lõm sâu màu tím hoặc nâu đỏ",
          "Tâm vết đốm chuyển sang màu xám tro, mép gờ nổi cao màu tím thẫm rất sắc nét",
          "Nhiều vết đốm liên kết lại làm vỏ cành bị nứt nẻ sâu vào tầng gỗ, cành bị khô giòn dễ gãy, các chồi nách mang hoa vụ sau bị teo chết hoàn toàn"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với vết xước gai tự nhiên: Gai cào xước chỉ để lại vệt xơ mỏng màu nâu nhạt; nấm Elsinoë tạo các vết lõm tròn tâm xám bạc gờ tím nổi cao và làm nứt toác lớp vỏ gỗ.",
        "kiem_tra_thuc_dia": "Dùng móng tay miết dọc thân cành mâm xôi: cảm giác lồi lõm sần sùi cộm tay rõ rệt, nắn nhẹ cành giòn gãy ngang mắt đốt.",
        "phac_do_vietgap": {
          "canh_tac": "Cắt tỉa triệt để các cành đã cho quả vụ trước sát mặt đất ngay sau thu hoạch; dọn sạch tàn dư lá bệnh.",
          "sinh_hoc": "Phun dung dịch Nano Đồng Chitosan kích kháng dày vỏ cành kết hợp chế phẩm sinh học Trichoderma.",
          "khuyen_cao_chuyen_gia": "Quét dung dịch vôi pha đồng sunfat lên thân cành già vào giai đoạn ngủ nghỉ tỉa cành."
        }
      }
    ]
  },
  {
    "id": "imp_crop_019",
    "topic": "Cay_Nhap_Khau_Kinh_Te_Cao",
    "name_vi": "Dưa lưới Musk Melon Nhật Bản (Japanese Musk Melon)",
    "scientific_name": "Cucumis melo var. reticulatus",
    "dia_ban_pho_bien": ["Đà Lạt (Lâm Đồng)", "Củ Chi (TP.HCM)", "Ninh Thuận", "Bình Dương", "Vĩnh Long", "Tây Ninh"],
    "dac_tinh_sinh_thai": "Cây ăn quả dây leo giá trị kinh tế cực cao, bắt buộc canh tác nhà màng ứng dụng công nghệ tưới nhỏ giọt Fertigation trên giá thể xơ dừa, thụ phấn nhân tạo, mỗi cây nuôi đúng 1 quả đạt vân lưới nổi đều dày, pH giá thể 6.0 - 6.8, EC 1.8 - 2.5 mS/cm.",
    "danh_sach_benh": [
      {
        "ten_benh": "Bệnh nứt thân xì mủ bã kẹo gôm dưa lưới (Gummy Stem Blight)",
        "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Didymella bryoniae (anamorph: Phoma cucurbitacearum)"
        },
        "trieu_chung_dien_hinh": [
          "Phần gốc thân sát mặt giá thể hoặc các nách cành xuất hiện vết úng nước thâm đen, sau đó vỏ thân bị nứt nẻ dọc theo thớ",
          "Từ vết nứt ứa ra chất dịch mủ màu nâu đỏ quánh đặc như bã kẹo cao su hoặc giọt gôm mật ong",
          "Trên bề mặt vết loét khô xuất hiện lấm tấm vô số chấm đen nhỏ li ti (bọc quả thể nấm), toàn bộ dây dưa phía trên bị héo rũ nhanh chóng khi quả đang lên vân lưới"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với bệnh héo xanh vi khuẩn: Héo vi khuẩn thân không nứt nẻ xì mủ quánh nâu đỏ và không có các chấm đen li ti trên vỏ; Didymella bắt buộc có vết nứt dài xì gôm nâu dẻo quánh và hạt đen li ti.",
        "kiem_tra_thuc_dia": "Sờ tay vào vết nứt gốc thân dưa lưới: giọt mủ nâu đỏ dính dẻo quánh vào đầu ngón tay như nhựa kẹo; dùng kính lúp soi thấy các hạt chấm đen li ti rải rác quanh vết nứt.",
        "phac_do_vietgap": {
          "canh_tac": "Tỉa chồi nách vào buổi sáng khô ráo nắng to để vết thương mau se lành; khử trùng kéo bấm chồi bằng cồn 70 độ.",
          "sinh_hoc": "Quét trực tiếp thuốc sinh học Trichoderma dạng paste đặc trộn Nano Bạc Đồng 100ppm lên vết nứt thân; phun phòng toàn bộ tán lá định kỳ 7 ngày/lần.",
          "khuyen_cao_chuyen_gia": "Kiểm soát độ ẩm nhà màng dưới 80% bằng quạt đối lưu, không để nước tưới nhỏ giọt văng trúng cổ thân cây dưa."
        }
      },
      {
        "ten_benh": "Bệnh phấn trắng phủ vân lưới nứt nẻ (Powdery Mildew)",
        "muc_do_nguy_hiem": "Nặng",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Golovinomyces cichoracearum (syn. Erysiphe cichoracearum) / Podosphaera xanthii"
        },
        "trieu_chung_dien_hinh": [
          "Mặt trên và mặt dưới phiến lá dưa lưới xuất hiện các đốm bột màu trắng như rắc phấn mì",
          "Vết phấn lan nhanh bao phủ toàn bộ phiến lá và cuống lá, lá bị vàng xỉn, khô cháy giòn từ lá gốc lên ngọn",
          "Vỏ quả dưa lưới bị chai sượng, các đường vân lưới phát triển méo mó đứt đoạn, quả không tích lũy được độ ngọt Brix chuẩn Nhật Bản"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với bệnh sương mai: Phấn trắng tạo lớp bột phấn trắng xốp như phấn viết bảng ở cả 2 mặt lá; sương mai tạo các vết cháy màu vàng nâu hình góc cạnh bị chặn bởi gân lá mặt dưới có lớp tơ xám.",
        "kiem_tra_thuc_dia": "Miết ngón tay lên phiến lá dưa: lớp bột phấn trắng dính dính đầy ngón tay, mô lá bên dưới hơi vàng úa xơ xác.",
        "phac_do_vietgap": {
          "canh_tac": "Thu dọn triệt để lá già dưới gốc mang ra khỏi nhà màng tiêu hủy; tăng cường thông gió giảm tích tụ ẩm.",
          "sinh_hoc": "Phun phòng luân phiên chế phẩm sinh học vi khuẩn Bacillus subtilis chủng QST 713 kết hợp dầu khoáng hữu cơ SK Enspray 99EC nồng độ 0.3%.",
          "khuyen_cao_chuyen_gia": "Phun kỹ cả mặt trên và mặt dưới của các tầng lá phía dưới tán dưa nơi mầm nấm xuất hiện đầu tiên."
        }
      },
      {
        "ten_benh": "Bệnh sương mai bã chè cháy lá góc cạnh (Downy Mildew)",
        "muc_do_nguy_hiem": "Nặng",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Pseudoperonospora cubensis"
        },
        "trieu_chung_dien_hinh": [
          "Mặt trên lá xuất hiện các đốm màu vàng tươi có hình đa giác góc cạnh rõ rệt do bị chặn lại bởi các gân phụ của phiến lá dưa",
          "Sáng sớm lật mặt dưới lá thấy một lớp tơ nấm mịn màu xám tím hoặc nâu xám bao phủ vết bệnh",
          "Các vết góc cạnh nhanh chóng liên kết lại làm toàn bộ lá khô cháy giòn như bã chè khô, cuộn mép lên trên nhưng lá vẫn treo lủng lẳng trên dây"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với bệnh cháy lá do thiếu Magie: Thiếu Magie vàng ở phần thịt giữa các gân chính không có hình đa giác góc cạnh sắc sảo và mặt dưới lá sạch bong không có lớp tơ xám tím.",
        "kiem_tra_thuc_dia": "Soi ngược phiến lá lên trần nhà màng: thấy các ô hình đa giác góc cạnh màu vàng nâu sắc nét như ô cờ caro; mặt dưới ẩm có lớp mốc xám.",
        "phac_do_vietgap": {
          "canh_tac": "Bảo dưỡng màng mái không để dột nước mưa tạo giọt nhỏ xuống lá dưa; không tưới phun mưa.",
          "sinh_hoc": "Phun dung dịch Nano Đồng sinh học kết hợp Phosphonate sinh học (Kali Phosphite) nồng độ 0.2%.",
          "khuyen_cao_chuyen_gia": "Can thiệp ngay khi thấy xuất hiện đốm đa giác vàng đầu tiên trên các tầng lá dưới gốc."
        }
      }
    ]
  },
  {
    "id": "imp_crop_020",
    "topic": "Rau_Cu_Gia_Vi_Va_Nam",
    "name_vi": "Bí ngô khổng lồ Atlantic Giant Đà Lạt (Atlantic Giant Pumpkin)",
    "scientific_name": "Cucurbita maxima 'Atlantic Giant'",
    "dia_ban_pho_bien": ["Đà Lạt (Lâm Đồng)", "Đơn Dương (Lâm Đồng)"],
    "dac_tinh_sinh_thai": "Giống bí ngô kỷ lục thế giới nhập ngoại cho quả nặng từ 50kg đến hàng trăm kg, trồng trong nhà kính công nghệ cao, cần diện tích bò > 30m2/gốc, chế độ bón phân giàu kali và hữu cơ vi sinh, đệm rơm hoặc xốp cách ly quả khổng lồ khỏi mặt đất ẩm, pH đất 6.5 - 7.2.",
    "danh_sach_benh": [
      {
        "ten_benh": "Bệnh thối thâm cuống và thối ruột quả khổng lồ (Choanephora Wet Rot)",
        "muc_do_nguy_hiem": "Cực kỳ nghiêm trọng (Hiểm nghèo)",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Choanephora cucurbitarum"
        },
        "trieu_chung_dien_hinh": [
          "Bắt đầu từ vết đài hoa héo hoặc cuống quả bí ngô khổng lồ xuất hiện vết úng nước thâm nhũn",
          "Nấm phát triển cực nhanh tạo ra một lớp sợi nấm màu trắng mang vô số đầu bào tử màu đen như đầu đinh ghim li ti bao phủ vùng cuống quả",
          "Vỏ và thịt quả bí ngô nặng hàng chục kg bị thối nhũn chảy nước vàng nhầy, quả bị sụp đổ xẹp lép từ bên trong bốc mùi thối chua nồng"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với bệnh nứt quả do tưới nước quá nhiều: Nứt do thừa nước mép vết nứt khô cứng có mô sẹo màu trắng; thối Choanephora có lớp sợi nấm tua tủa gắn hạt đen như đầu đinh ghim và mô thịt quả nhũn chảy nước lỏng.",
        "kiem_tra_thuc_dia": "Dùng kính lúp soi vùng cuống quả bị thối: thấy các sợi nấm mảnh trắng vươn cao mang các hạt tròn nhỏ màu đen lấp lánh như rừng đinh ghim mini.",
        "phac_do_vietgap": {
          "canh_tac": "Lót đệm mút xốp hoặc tấm pallet nhựa cao ráo dưới đáy quả bí ngô khổng lồ; ngắt bỏ hoa đực hoa cái đã tàn sau thụ phấn tránh ẩm mốc cuống.",
          "sinh_hoc": "Rắc bột vôi tôi khử trùng quanh cuống kết hợp phun dung dịch Nano Bạc 30ppm và vi khuẩn Bacillus subtilis bảo vệ vùng rốn quả.",
          "khuyen_cao_chuyen_gia": "Quạt gió trực tiếp vào vùng cuống quả khổng lồ sau các cơn mưa dông để làm khô nhanh độ ẩm đọng tại kẽ cuống."
        }
      },
      {
        "ten_benh": "Bệnh lở cổ rễ thối thắt thân chính bí ngô (Fusarium Crown and Foot Rot)",
        "muc_do_nguy_hiem": "Nặng",
        "tac_nhan": {
          "loai": "Nấm",
          "ten_khoa_hoc": "Fusarium solani f. sp. cucurbitae"
        },
        "trieu_chung_dien_hinh": [
          "Đoạn thân gốc chính sát mặt đất bị sũng nước thâm đen, vỏ thân nứt nẻ và hóa bần",
          "Mô gốc thân bị teo thắt lại, khi trời ẩm xuất hiện lớp nấm mốc màu trắng hồng bám xung quanh vết nứt",
          "Toàn bộ dàn lá khổng lồ phía trên bị héo rũ từ từ, quả non bị teo tóp không thể tăng trọng lượng"
        ],
        "phan_biet_chan_doan_kep": "Phân biệt với dế hoặc chuột cắn thân: Chuột cắn có dấu răng gặm nham nhở; Fusarium làm thối mục mạch dẫn từ bên trong rỉ nhựa vàng và có sợi mốc hồng.",
        "kiem_tra_thuc_dia": "Bới nhẹ lớp đất cổ rễ: thấy phần gốc thắt eo nhỏ lại so với thân trên, cạo vỏ thấy lớp nấm mốc màu hồng phấn mịn bám trong thớ gỗ thối mục.",
        "phac_do_vietgap": {
          "canh_tac": "Lên mô cao ráo trước khi đặt cây giống; không tưới nước thẳng vào gốc thân bí ngô.",
          "sinh_hoc": "Tưới đẫm vùng rễ nấm đối kháng Trichoderma asperellum kết hợp vi khuẩn đối kháng Streptomyces định kỳ 15 ngày/lần.",
          "khuyen_cao_chuyen_gia": "Xử lý đất hố trồng bằng chế phẩm sinh học Chitosan kích kháng rễ phát triển sâu rộng."
        }
      }
    ]
  }
]
