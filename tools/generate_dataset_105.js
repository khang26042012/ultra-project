/**
 * AgriVision - Vinh Long & Mekong Delta 105 Crops Pathology Knowledge Base
 * Author: Phan Trọng Khang (Lớp 9¹, THCS Vĩnh An, Vĩnh Long)
 * Compliant with TASK_DATASET_100_CROPS_SEARCH.md
 */

const fs = require('fs');
const path = require('path');

function createDisease({
  ten_benh,
  muc_do_nguy_hiem = 'Nặng',
  loai = 'Nấm',
  ten_khoa_hoc = '',
  vector = null,
  trieu_chung = [],
  phan_biet = '',
  kiem_tra = '',
  canh_tac = '',
  sinh_hoc = '',
  khuyen_cao = 'Thực hiện theo khuyến cáo của Chi cục Trồng trọt & BVTV tỉnh Vĩnh Long'
}) {
  const tac_nhan = { loai, ten_khoa_hoc };
  if (vector) tac_nhan.vector_truyen_benh = vector;

  return {
    ten_benh,
    muc_do_nguy_hiem,
    tac_nhan,
    trieu_chung_dien_hinh: trieu_chung,
    phan_biet_chan_doan_kep: phan_biet,
    kiem_tra_thuc_dia: kiem_tra,
    phac_do_vietgap: {
      canh_tac,
      sinh_hoc,
      khuyen_cao_vinh_long: khuyen_cao
    }
  };
}

// Data store
const allCrops = [];

// ==================== 1. CÂY ĂN TRÁI ĐẶC SẢN (35 crops) ====================
const fruits = [
  {
    name_vi: "Bưởi Năm Roi Bình Minh",
    scientific_name: "Citrus maxima 'Nam Roi'",
    dia_ban: ["Bình Minh", "Tam Bình", "Trà Ôn"],
    dac_tinh: "Cây ưa đất phù sa bồi lắng ven sông Hậu, thoát nước tốt, pH thích hợp từ 5.5 - 6.5, cực kỳ mẫn cảm với úng và mặn.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Vàng lá gân xanh (Huanglongbing - HLB)",
        muc_do_nguy_hiem: "Cực kỳ nghiêm trọng (Hiểm nghèo)",
        loai: "Vi khuẩn",
        ten_khoa_hoc: "Candidatus Liberibacter asiaticus",
        vector: "Rầy chổng cánh (Diaphorina citri)",
        trieu_chung: [
          "Phiến lá vàng lốm đốm loang lổ không đối xứng (mottling)",
          "Gân chính và gân phụ vẫn giữ màu xanh đậm hoặc bị sưng gồ, hóa bần",
          "Lá nhỏ lại, dựng đứng như tai thỏ, đọt non ngắn ngủn",
          "Trái méo mó, tâm lệch, tép khô xơ, vị chua đắng"
        ],
        phan_biet: "Khác với thiếu kẽm (vết vàng đối xứng đều hai bên gân) và vàng lá thối rễ (vàng cả gân lẫn phiến lá, rễ tơ bị thối tuột vỏ)",
        kiem_tra: "Kiểm tra mặt dưới lá và đọt non tìm rầy chổng cánh đuôi vểnh 45 độ; kiểm tra tính bất đối xứng của vết vàng phiến lá",
        canh_tac: "Cắt bỏ tiêu hủy cây bệnh nặng, trồng cây sạch bệnh vi ghép đỉnh sinh trưởng, tạo tán thông thoáng",
        sinh_hoc: "Nuôi kiến vàng khống chế rầy chổng cánh, phun nấm ký sinh Beauveria bassiana hoặc dầu khoáng SK Enspray 99EC",
        khuyen_cao: "Liên hệ Trạm Khuyến nông Bình Minh / Tam Bình để lấy mẫu xét nghiệm PCR khi phát hiện triệu chứng nghi ngờ"
      }),
      createDisease({
        ten_benh: "Bệnh Ghẻ loét vi khuẩn (Citrus Canker)",
        muc_do_nguy_hiem: "Nặng",
        loai: "Vi khuẩn",
        ten_khoa_hoc: "Xanthomonas citri subsp. citri",
        trieu_chung: [
          "Vết loét ban đầu là nốt sần nhỏ ngậm nước ở mặt dưới lá",
          "Vết bệnh phát triển sùi lên, màu nâu xám, rách ở giữa như miệng núi lửa thu nhỏ",
          "Xung quanh vết loét luôn có quầng vàng sáng rực rỡ đặc trưng",
          "Xuất hiện trên cả chồi non, cành và vỏ bưởi làm sượng trái"
        ],
        phan_biet: "Khác với Ghẻ nhám: Ghẻ loét có miệng núi lửa và quầng vàng bao quanh; Ghẻ nhám chóp nhọn nhô lên như hạt mụn cơm và không có quầng vàng",
        kiem_tra: "Dùng kính lúp kiểm tra vết nứt miệng núi lửa và quầng halo sáng màu",
        canh_tac: "Tỉa bỏ cành lá nhiễm bệnh sau mỗi đợt lộc non, khử trùng kéo cắt cành bằng cồn",
        sinh_hoc: "Phun phòng luân phiên các hoạt chất gốc đồng nano sinh học, Kasugamycin, nấm đối kháng Bacillus subtilis"
      })
    ]
  },
  {
    name_vi: "Bưởi Da Xanh",
    scientific_name: "Citrus maxima 'Da Xanh'",
    dia_ban: ["Vũng Liêm", "Trà Ôn", "Mang Thít", "Long Hồ"],
    dac_tinh: "Thích nghi tốt vùng đất phù sa ven sông Cổ Chiên, nhạy cảm với phèn mặn và úng rễ mùa triều cường.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Vàng lá thối rễ",
        muc_do_nguy_hiem: "Nặng",
        loai: "Tổ hợp Nấm & Tuyến trùng",
        ten_khoa_hoc: "Phytophthora nicotianae, Fusarium solani & Tylenchulus semipenetrans",
        trieu_chung: [
          "Gân lá và phiến lá đồng loạt ngả vàng rực",
          "Lá rụng lác đác từ đọt non xuống dần cành già",
          "Hệ thống rễ tơ bị thối đen, tuột vỏ trơ lại lõi gỗ mục nát, có mùi ẩm mốc"
        ],
        phan_biet: "Khác với bệnh Greening: Vàng lá thối rễ vàng đều cả lá và rụng trút lá hàng loạt, rễ tơ bị hư hại nặng nề",
        kiem_tra: "Bới nhẹ lớp đất vùng rìa tán lá để kiểm tra đầu chóp rễ tơ và vỏ rễ",
        canh_tac: "Đào rãnh thoát nước sâu giữa các liếp bưởi, rải vôi bột (500g/cây) khử trùng đất và ổn định pH 6.0",
        sinh_hoc: "Tưới nấm đối kháng Trichoderma harzianum + Streptomyces kết hợp hoạt chất trừ tuyến trùng sinh học Chitosan"
      })
    ]
  },
  {
    name_vi: "Cam Sành Tam Bình",
    scientific_name: "Citrus nobilis",
    dia_ban: ["Tam Bình", "Trà Ôn", "Bình Tân", "Vũng Liêm"],
    dac_tinh: "Giống cây trồng chủ lực của tỉnh Vĩnh Long, năng suất cao nhưng đòi hỏi kỹ thuật lên liếp xẻ mương và chế độ chăm sóc khắt khe.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Vàng lá gân xanh (HLB) trên Cam sành",
        muc_do_nguy_hiem: "Cực kỳ nghiêm trọng",
        loai: "Vi khuẩn",
        ten_khoa_hoc: "Candidatus Liberibacter asiaticus",
        vector: "Rầy chổng cánh",
        trieu_chung: [
          "Lá cam sành co nhỏ, vàng loang lổ, gân chính nổi cộm",
          "Cây ra hoa trái vụ liên tục nhưng rụng non gần hết",
          "Rễ suy kiệt nhanh chóng khiến cả vườn lụi tàn sau 2-3 năm nhiễm bệnh"
        ],
        phan_biet: "Phân biệt kỹ với nấm Fusarium: Bệnh HLB có triệu chứng gân lá sưng gồ và lá dựng đứng tai thỏ",
        kiem_tra: "Dùng bẫy dính màu vàng theo dõi mật độ rầy chổng cánh trong vườn",
        canh_tac: "Trồng xen ổi xá lị hoặc ổi nữ hoàng để xua đuổi rầy chổng cánh bằng hương tinh dầu tự nhiên",
        sinh_hoc: "Ứng dụng chế phẩm vi sinh Metarhizium anisopliae + Beauveria bassiana xịt khi cây nhú lộc 1-2cm"
      })
    ]
  },
  {
    name_vi: "Cam Xoàn",
    scientific_name: "Citrus sinensis",
    dia_ban: ["Trà Ôn", "Vũng Liêm", "Tam Bình"],
    dac_tinh: "Trái ngọt thanh mát, vỏ mỏng có đồng tiền ở đít trái, mẫn cảm với nhện đỏ và bệnh thán thư vào mùa mưa ẩm.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Thán thư hại hoa và trái non",
        muc_do_nguy_hiem: "Nặng",
        loai: "Nấm",
        ten_khoa_hoc: "Colletotrichum gloeosporioides",
        trieu_chung: [
          "Cánh hoa xuất hiện đốm màu nâu cam sũng nước rồi thối rụng",
          "Trái non bị đốm đen lõm sâu, cuống trái chuyển màu nâu làm rụng cuống trơ đài"
        ],
        phan_biet: "Khác với rụng trái do sốc nước (cuống hoa tươi rụng, không có quầng nâu đen)",
        kiem_tra: "Kiểm tra cuống hoa và chồi non sau mưa đêm ẩm ướt",
        canh_tac: "Bón Canxi-Bo tăng độ dai cuống quả, cắt tỉa thông thoáng tán",
        sinh_hoc: "Phun phòng bằng nấm đối kháng Chaetomium hoặc nấm Bacillus subtilis"
      })
    ]
  },
  {
    name_vi: "Quýt Đường",
    scientific_name: "Citrus reticulata",
    dia_ban: ["Tam Bình", "Bình Tân", "Trà Ôn"],
    dac_tinh: "Cây phát triển mạnh trên đất thịt phù sa dày, trái mọng nước ngọt đậm, vỏ mỏng dễ nhiễm côn trùng chích hút.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Đốm dầu lá và trái (Greasy Spot)",
        muc_do_nguy_hiem: "Trung bình",
        loai: "Nấm",
        ten_khoa_hoc: "Mycosphaerella citri",
        trieu_chung: [
          "Mặt dưới lá xuất hiện vết nâu đen như vết dầu loang bóng dính",
          "Mặt trên lá biến vàng tương ứng, gây rụng lá sớm làm kiệt sức cây"
        ],
        phan_biet: "Vết dầu loang ăn sâu vào biểu bì lá không lau rửa được",
        kiem_tra: "Soi mặt dưới phiến lá tầng trung gian dưới tán",
        canh_tac: "Thu gom tàn dư lá rụng dưới gốc tiêu hủy",
        sinh_hoc: "Phun dầu khoáng trắng phối hợp nấm Trichoderma"
      })
    ]
  },
  {
    name_vi: "Quýt Hồng Lai Vung / Trà Ôn",
    scientific_name: "Citrus reticulata 'Hong'",
    dia_ban: ["Trà Ôn", "Vũng Liêm", "Tam Bình"],
    dac_tinh: "Vỏ màu cam đỏ rực rỡ vào dịp Tết Nguyên Đán, tán rộng, rất nhạy cảm với ngập úng tầng rễ mặt.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Đốm nâu quả quýt (Alternaria Brown Spot)",
        muc_do_nguy_hiem: "Nặng",
        loai: "Nấm",
        ten_khoa_hoc: "Alternaria alternata pv. citri",
        trieu_chung: [
          "Đốm nâu đen có quầng vàng xuất hiện trên lộc non và vỏ quả quýt",
          "Làm quả non rụng sớm, quả già sượng vỏ chai múi mất giá trị"
        ],
        phan_biet: "Không có miệng núi lửa như loét vi khuẩn",
        kiem_tra: "Quan sát lộc non và vỏ quả thời kỳ nuôi trái",
        canh_tac: "Tránh tưới phun mưa trực tiếp lên tán vào chiều tối ẩm",
        sinh_hoc: "Phun phòng bằng chế phẩm vi sinh Bacillus amyloliquefaciens"
      })
    ]
  },
  {
    name_vi: "Chanh Không Hạt (Limca)",
    scientific_name: "Citrus latifolia",
    dia_ban: ["Bình Minh", "Bình Tân", "Long Hồ"],
    dac_tinh: "Cây sinh trưởng nhanh, cho trái quanh năm, chịu hạn khá nhưng dễ bị ghẻ nhám và xì mủ gốc nếu đất chua trũng phèn.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Ghẻ nhám sẹo (Citrus Scab)",
        muc_do_nguy_hiem: "Trung bình",
        loai: "Nấm",
        ten_khoa_hoc: "Elsinoë fawcettii",
        trieu_chung: [
          "Nốt sẹo mụn cơm nhô cao màu vàng nâu sần sùi ở mặt dưới lá và vỏ quả",
          "Phiến lá non biến dạng vặn vẹo hình lòng chảo"
        ],
        phan_biet: "Khác ghẻ loét: Ghẻ nhám không có miệng núi lửa và không có quầng vàng halo",
        kiem_tra: "Dùng tay sờ bề mặt lộc non thấy ráp nhám rõ rệt",
        canh_tac: "Cắt tỉa cành tăm, chồi vượt sau mỗi vụ thu hoạch",
        sinh_hoc: "Phun nano đồng sinh học hoặc tinh dầu neem hữu cơ"
      })
    ]
  },
  {
    name_vi: "Chanh Giấy Vĩnh Long",
    scientific_name: "Citrus aurantifolia",
    dia_ban: ["Long Hồ", "Tam Bình", "Trà Ôn"],
    dac_tinh: "Vỏ mỏng thơm nồng, rất mẫn cảm với virus Tristeza truyền qua rệp muội đen.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Tàn lụi gân trong (Citrus Tristeza Virus)",
        muc_do_nguy_hiem: "Cực kỳ nghiêm trọng",
        loai: "Virus",
        ten_khoa_hoc: "Citrus tristeza virus (CTV)",
        vector: "Rệp muội đen (Toxoptera citricida)",
        trieu_chung: [
          "Gân phụ lá non trong suốt khi soi ngược ánh sáng (vein clearing)",
          "Thân cành bị lõm gai châm kim ăn vào phần gỗ khi bóc vỏ",
          "Cây sinh trưởng còi cọc tàn lụi nhanh"
        ],
        phan_biet: "Dấu hiệu gai châm kim thân gỗ là triệu chứng độc quyền của CTV",
        kiem_tra: "Cạo vỏ thân xem có các lỗ nhỏ ăn sâu vào lõi gỗ hay không",
        canh_tac: "Trồng bằng mắt ghép trên gốc chống chịu như Volkameriana",
        sinh_hoc: "Phun dầu khoáng sinh học bảo vệ thiên địch bọ rùa đỏ"
      })
    ]
  },
  {
    name_vi: "Sầu Riêng Ri6 Vĩnh Long",
    scientific_name: "Durio zibethinus 'Ri6'",
    dia_ban: ["Long Hồ", "Vũng Liêm", "Mang Thít", "Tam Bình"],
    dac_tinh: "Cội nguồn cù lao Long Hồ, cơm vàng hạt lép, rất mẫn cảm với nấm Phytophthora gây xì mủ thối trái.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Xì mủ thối gốc chảy nhựa (Phytophthora)",
        muc_do_nguy_hiem: "Cực kỳ nghiêm trọng",
        loai: "Nấm",
        ten_khoa_hoc: "Phytophthora palmivora",
        trieu_chung: [
          "Cổ rễ và thân chính xì mủ nhờn màu nâu đỏ, gỗ thâm đen",
          "Lá vàng úa và rụng trút hàng loạt làm cây trơ cành",
          "Trái sầu riêng bị thối đen từ rốn quả, có mùi chua nồng và mốc trắng"
        ],
        phan_biet: "Khác sâu đục thân (sâu đục thân có đùn mùn cưa ra ngoài)",
        kiem_tra: "Bới kiểm tra vùng cổ rễ tiếp giáp mặt đất vào buổi sáng ẩm",
        canh_tac: "Xới rãnh thoát nước, phơi gốc cổ rễ, quét vôi cao 1m định kỳ",
        sinh_hoc: "Tiêm thân lân hai chiều Phosphonate (Agri-Fos), tưới gốc Trichoderma + Chaetomium"
      })
    ]
  },
  {
    name_vi: "Sầu Riêng Monthong (Dona)",
    scientific_name: "Durio zibethinus 'Monthong'",
    dia_ban: ["Vũng Liêm", "Trà Ôn", "Long Hồ"],
    dac_tinh: "Cơm dày ngọt béo ngậy, tán cây vươn cao, dễ bị bệnh cháy lá chết ngọn Rhizoctonia trong mùa mưa.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Cháy lá chết ngọn (Rhizoctonia)",
        muc_do_nguy_hiem: "Nặng",
        loai: "Nấm",
        ten_khoa_hoc: "Rhizoctonia solani",
        trieu_chung: [
          "Lá non sũng nước như luộc sôi dính bết lại bởi mạng tơ nấm trắng bạc",
          "Vết cháy chuyển sang nâu sậm, lá dính tòng teng trên cành",
          "Đọt non thối đen thụt lùi làm khô trơ cành"
        ],
        phan_biet: "Mạng tơ nấm trắng đan dính chùm các lá non với nhau",
        kiem_tra: "Kiểm tra chùm lá đọt non lúc sáng sớm sương ướt",
        canh_tac: "Cắt tỉa cành la sát đất, tạo độ thông thoáng vi khí hậu tán",
        sinh_hoc: "Phun Validamycin sinh học hoặc nấm Trichoderma viride"
      })
    ]
  },
  {
    name_vi: "Xoài Cát Hòa Lộc",
    scientific_name: "Mangifera indica 'Hoa Loc'",
    dia_ban: ["Vũng Liêm", "Mang Thít", "Long Hồ"],
    dac_tinh: "Vua của các loài xoài tại ĐBSCL, thịt thơm ngọt đậm đà, rất dễ bị bệnh thán thư phá hại chùm bông và da trái.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Thán thư bông và trái xoài",
        muc_do_nguy_hiem: "Nặng (Gây mất mùa bông xoài)",
        loai: "Nấm",
        ten_khoa_hoc: "Colletotrichum gloeosporioides",
        trieu_chung: [
          "Chùm bông xoài xuất hiện nhiều chấm đen li ti rồi khô đen rụng cuống",
          "Vỏ trái chín có đốm đen tròn lõm xuống, thịt quả bên dưới bị chua thối"
        ],
        phan_biet: "Khác bọ trĩ (bọ trĩ làm cọng hoa cong queo có phân đen bài tiết)",
        kiem_tra: "Gõ nhẹ chùm bông lên giấy trắng kiểm tra bọ trĩ kết hợp soi vết thán thư",
        canh_tac: "Rung bông rũ nước mưa sau cơn mưa đêm, bao trái bằng túi giấy chuyên dụng",
        sinh_hoc: "Phun phòng nấm Chaetomium hoặc thuốc sinh học nguồn gốc Eugenol thảo mộc"
      })
    ]
  },
  {
    name_vi: "Xoài Cát Chu",
    scientific_name: "Mangifera indica 'Cat Chu'",
    dia_ban: ["Long Hồ", "Mang Thít", "Vũng Liêm"],
    dac_tinh: "Trái thon nhỏ, thịt vàng ươm, dễ xử lý ra hoa nhưng hay bị đốm đen vi khuẩn xì mủ chân chim.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Đốm đen vi khuẩn chân chim (Xanthomonas)",
        muc_do_nguy_hiem: "Nặng",
        loai: "Vi khuẩn",
        ten_khoa_hoc: "Xanthomonas campestris pv. mangiferaeindicae",
        trieu_chung: [
          "Đốm đen hình góc cạnh chân chim rỉ mủ nhớt trên vỏ quả và phiến lá",
          "Cành non loét đen dễ gãy khi có gió to"
        ],
        phan_biet: "Vết bệnh chân chim nứt nẻ và chảy mủ nhớt tanh đặc thù vi khuẩn",
        kiem_tra: "Ngâm mẩu mô bệnh vào ly nước xem dòng vi khuẩn đùn ra đục nước",
        canh_tac: "Khử trùng kéo cắt cành, cắt bỏ cành bệnh tiêu hủy",
        sinh_hoc: "Phun Kasugamycin hoặc đồng nano sinh học"
      })
    ]
  },
  {
    name_vi: "Xoài Tượng",
    scientific_name: "Mangifera indica",
    dia_ban: ["Long Hồ", "Tam Bình", "Trà Ôn"],
    dac_tinh: "Trái to nặng từ 0.8 - 1.5kg, ăn giòn thơm, chịu đất sét pha tốt.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Phấn trắng hại xoài",
        muc_do_nguy_hiem: "Trung bình",
        loai: "Nấm",
        ten_khoa_hoc: "Oidium mangiferae",
        trieu_chung: [
          "Lớp phấn màu trắng xám như bột mì phủ trên cọng bông và lá non",
          "Hoa không thụ phấn được và khô rụng hàng loạt"
        ],
        phan_biet: "Lớp bụi phấn trắng phủ ngoài dễ lau bay",
        kiem_tra: "Soi chùm hoa lúc sương sớm mùa lạnh",
        canh_tac: "Tỉa thông thoáng cho ánh nắng chiếu vào tán",
        sinh_hoc: "Phun lưu huỳnh sinh học hoặc dung dịch baking soda pha loãng 0.3%"
      })
    ]
  },
  {
    name_vi: "Nhãn Xuồng Cơm Vàng",
    scientific_name: "Dimocarpus longan 'Xuong Com Vang'",
    dia_ban: ["Long Hồ", "Vũng Liêm", "Trà Ôn"],
    dac_tinh: "Cơm dày ngọt ráo nước màu vàng nhạt, chịu phèn nhẹ, mẫn cảm với bệnh chổi rồng.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Chổi rồng hại nhãn",
        muc_do_nguy_hiem: "Cực kỳ nghiêm trọng",
        loai: "Virus / Phytoplasma liên kết",
        ten_khoa_hoc: "Longan witches' broom-associated virus",
        vector: "Nhện lông nhung (Eriophyes dimocarpi)",
        trieu_chung: [
          "Chồi non xoăn tít, lóng ngắn cũn cỡn tụ lại thành chùm như chổi rơm",
          "Chùm hoa khô queo thành bùi nhùi không thể thụ phấn đậu trái"
        ],
        phan_biet: "Hình dạng bó chổi rơm không thể nhầm lẫn với bệnh nào khác",
        kiem_tra: "Dùng kính lúp soi đọt non tìm nhện lông nhung trắng li ti",
        canh_tac: "Cắt sâu vào cành gỗ lành 20-30cm tiêu hủy triệt để tàn dư",
        sinh_hoc: "Phun dầu khoáng SK Enspray trừ nhện lông nhung khi cây nhú lộc non"
      })
    ]
  },
  {
    name_vi: "Nhãn Ido",
    scientific_name: "Dimocarpus longan 'Ido'",
    dia_ban: ["Long Hồ", "Mang Thít", "Tam Bình", "Trà Ôn"],
    dac_tinh: "Kháng bệnh chổi rồng khá tốt, năng suất cao, tỷ lệ đậu trái tốt trên đất cù lao ven sông.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Thối trái sương mai (Phytophthora)",
        muc_do_nguy_hiem: "Nặng",
        loai: "Nấm",
        ten_khoa_hoc: "Phytophthora sp.",
        trieu_chung: [
          "Vỏ trái có đốm nâu tròn rồi lan rộng ra cả chùm quả",
          "Cơm nhãn bên trong úng nước có mùi chua nồng và thối rữa"
        ],
        phan_biet: "Khác bồ hóng: Thối sương mai làm hỏng thối cơm ruột quả",
        kiem_tra: "Kiểm tra chùm quả sau đợt mưa rào dầm dề",
        canh_tac: "Cắt tỉa chùm quả quá dày, không để cành chạm mặt đất",
        sinh_hoc: "Phun chế phẩm sinh học Fosetyl-Aluminium hoặc Trichoderma"
      })
    ]
  },
  {
    name_vi: "Nhãn Tiêu Da Bò",
    scientific_name: "Dimocarpus longan",
    dia_ban: ["Long Hồ", "Mang Thít"],
    dac_tinh: "Vỏ mỏng màu vàng bò, cơm mọng nước, dễ nhiễm nấm muội đen bồ hóng.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Muội đen bồ hóng lá và trái",
        muc_do_nguy_hiem: "Nhẹ",
        loai: "Nấm",
        ten_khoa_hoc: "Capnodium citri",
        trieu_chung: [
          "Màng đen muội than phủ dày trên phiến lá và chùm quả nhãn",
          "Làm đen bẩn vỏ quả mất giá trị thương phẩm"
        ],
        phan_biet: "Màng bồ hóng dùng khăn ướt lau là sạch bóng vỏ quả",
        kiem_tra: "Tìm sự hiện diện của rệp sáp và rầy mềm tiết chất ngọt",
        canh_tac: "Tỉa cành đón nắng, tiêu diệt kiến tha rệp sáp",
        sinh_hoc: "Phun xà phòng thảo mộc hoặc nấm Lecanicillium lecanii trừ rệp sáp"
      })
    ]
  },
  {
    name_vi: "Chôm Chôm Java",
    scientific_name: "Nephelium lappaceum 'Java'",
    dia_ban: ["Long Hồ", "Bình Minh"],
    dac_tinh: "Đặc sản vùng du lịch sinh thái cù lao An Bình, râu dài đỏ tươi, thịt róc ngọt thanh.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Phấn trắng hại gai quả chôm chôm",
        muc_do_nguy_hiem: "Nặng",
        loai: "Nấm",
        ten_khoa_hoc: "Oidium nephelii",
        trieu_chung: [
          "Bột phấn trắng xám bao phủ chùm hoa và râu gai trái non",
          "Râu gai bị khô đen, trái non rụng hàng loạt hoặc chai sượng"
        ],
        phan_biet: "Gai quả non bị cháy xém bao phủ bột mốc trắng",
        kiem_tra: "Kiểm tra râu gai quả non cỡ hạt đậu phộng",
        canh_tac: "Tỉa cành sau thu hoạch, dọn rác mục dưới gốc",
        sinh_hoc: "Phun lưu huỳnh sinh học kết hợp Bacillus subtilis"
      })
    ]
  },
  {
    name_vi: "Chôm Chôm Nhãn",
    scientific_name: "Nephelium lappaceum",
    dia_ban: ["Long Hồ", "Mang Thít", "Vũng Liêm"],
    dac_tinh: "Trái nhỏ râu ngắn, cơm dày giòn ráo ngọt lịm, nhạy cảm với bệnh thối quả Botryodiplodia.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Thối cuống trái chôm chôm",
        muc_do_nguy_hiem: "Nặng",
        loai: "Nấm",
        ten_khoa_hoc: "Lasiodiplodia theobromae",
        trieu_chung: [
          "Vết thâm nâu lan nhanh từ cuống bao trùm cả quả trong 2-3 ngày",
          "Cơm bên trong nhũn nước thối rữa có nấm xám đen"
        ],
        phan_biet: "Thối từ cuống quả lan nhanh kèm hạt bào tử đen li ti",
        kiem_tra: "Kiểm tra chùm quả giai đoạn đỏ râu sắp hái",
        canh_tac: "Thu hái quả vào ngày khô ráo, tránh làm giập vỏ",
        sinh_hoc: "Phun chế phẩm sinh học Chitosan hoặc dịch thảo mộc kháng nấm"
      })
    ]
  },
  {
    name_vi: "Măng Cụt Lục Sĩ Thành",
    scientific_name: "Garcinia mangostana",
    dia_ban: ["Trà Ôn", "Vũng Liêm", "Long Hồ"],
    dac_tinh: "Nữ hoàng trái cây nhiệt đới, tuổi thọ cao, dễ bị chảy mủ vàng sượng múi do sốc nước mưa.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Xì mủ vàng sượng múi măng cụt",
        muc_do_nguy_hiem: "Nặng",
        loai: "Rối loạn sinh lý kết hợp Nấm",
        ten_khoa_hoc: "Rối loạn dòng nhựa tế bào do mưa sốc nước",
        trieu_chung: [
          "Mủ màu vàng tươi chảy ra ngoài vỏ quả và ngấm vào trong thịt múi",
          "Múi thịt bị sượng cứng và có vị đắng ngắt"
        ],
        phan_biet: "Mủ màu vàng óng đặc thù chỉ có ở cây măng cụt",
        kiem_tra: "Bổ quả kiểm tra sau đợt mưa dầm chuyển mùa",
        canh_tac: "Giữ mực nước mương ổn định, bón Canxi-Bo và Kali hữu cơ",
        sinh_hoc: "Phun bổ sung Canxi hữu cơ hòa tan che chắn gốc giảm sốc nước"
      })
    ]
  },
  {
    name_vi: "Mít Thái Siêu Sớm (Mít Changai)",
    scientific_name: "Artocarpus heterophyllus",
    dia_ban: ["Bình Tân", "Tam Bình", "Trà Ôn", "Vũng Liêm", "Long Hồ"],
    dac_tinh: "Cho trái cực nhanh, múi giòn ngọt ráo, mẫn cảm với bệnh xơ đen vi khuẩn.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Xơ đen mít Thái",
        muc_do_nguy_hiem: "Cực kỳ nghiêm trọng",
        loai: "Vi khuẩn",
        ten_khoa_hoc: "Pantoea stewartii subsp. stewartii",
        trieu_chung: [
          "Xơ mít chuyển màu đen kịt, cùi mít đen sì",
          "Múi mít teo lép chai cứng vị chua chát",
          "Bên ngoài quả eo thắt, gai không đều"
        ],
        phan_biet: "Khác xơ đỏ sinh lý (xơ đen múi bị chai và hôi chua, thương lái dạt 100%)",
        kiem_tra: "Bổ kiểm tra quả non méo eo lúc thụ phấn trúng mưa",
        canh_tac: "Tỉa bớt quả xấu, thụ phấn bổ sung buổi sáng khô ráo, bao quả sớm",
        sinh_hoc: "Phun Kasugamycin hoặc đồng vi sinh định kỳ lúc trổ hoa cái"
      })
    ]
  },
  {
    name_vi: "Mít Ruột Đỏ Indo",
    scientific_name: "Artocarpus heterophyllus 'Red'",
    dia_ban: ["Bình Tân", "Vũng Liêm", "Tam Bình"],
    dac_tinh: "Múi màu cam đỏ bắt mắt thơm mùi chuối, giá trị xuất khẩu cao, dễ bị thối nhũn trái.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Thối nhũn mốc đen trái mít (Rhizopus)",
        muc_do_nguy_hiem: "Nặng",
        loai: "Nấm",
        ten_khoa_hoc: "Rhizopus artocarpi",
        trieu_chung: [
          "Mô thịt quả nhũn nát nhanh chảy nước nhờn mùi men chua",
          "Lớp nấm mốc đen tua tủa như chùm râu bao phủ vết thối"
        ],
        phan_biet: "Sợi nấm trắng đầu có chấm đen tròn xù xì đặc trưng",
        kiem_tra: "Quan sát các quả mít treo thấp sát đất liếp",
        canh_tac: "Treo trái cao tối thiểu 0.8m so với mặt đất, tỉa thông thoáng",
        sinh_hoc: "Phun nấm đối kháng Trichoderma phối hợp vôi bột hòa nước tưới gốc"
      })
    ]
  },
  {
    name_vi: "Ổi Nữ Hoàng",
    scientific_name: "Psidium guajava 'Queen'",
    dia_ban: ["Bình Minh", "Tam Bình", "Long Hồ"],
    dac_tinh: "Trái giòn ngọt ít hạt, năng suất quanh năm, mẫn cảm thán thư đốm mắt chim.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Đốm mắt chim trên quả ổi",
        muc_do_nguy_hiem: "Trung bình",
        loai: "Nấm",
        ten_khoa_hoc: "Pestalotiopsis psidii / Colletotrichum gloeosporioides",
        trieu_chung: [
          "Nốt tròn màu nâu có viền đỏ đậm, tâm lõm xám tro như mắt chim",
          "Vỏ quả chai sượng, thịt quả bên dưới bị chua khô sượng"
        ],
        phan_biet: "Vết tròn lõm có viền hạt dẻ rõ nét trên vỏ quả ổi",
        kiem_tra: "Kiểm tra quả cỡ ngón chân cái trước khi bao bọc",
        canh_tac: "Bao trái sớm bằng xốp lưới bọc nilong đục lỗ đáy",
        sinh_hoc: "Phun phòng nấm Trichoderma hoặc nano bạc đồng sinh học"
      })
    ]
  },
  {
    name_vi: "Ổi Ruột Hồng (Ổi Ruby)",
    scientific_name: "Psidium guajava 'Ruby'",
    dia_ban: ["Bình Minh", "Trà Ôn", "Vũng Liêm"],
    dac_tinh: "Ruột đỏ hồng thơm đậm, chịu phù sa nhẹ, dễ nhiễm tuyến trùng nốt sưng rễ.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Nốt sưng tuyến trùng rễ ổi",
        muc_do_nguy_hiem: "Nặng",
        loai: "Tuyến trùng",
        ten_khoa_hoc: "Meloidogyne incognita",
        trieu_chung: [
          "Rễ nổi nhiều u sần hình hạt chuỗi tròn méo mó",
          "Cây còi cọc vàng lá, héo rũ vào buổi trưa nắng dù đất mương vẫn có nước"
        ],
        phan_biet: "U sưng rễ dị hình không phải nốt sần nốt vi khuẩn có ích",
        kiem_tra: "Nhổ kiểm tra rễ non tầng đất mặt",
        canh_tac: "Trồng xen hoa cúc vạn thọ xua đuổi tuyến trùng",
        sinh_hoc: "Tưới nấm ký sinh tuyến trùng Paecilomyces lilacinus kết hợp Chitosan"
      })
    ]
  },
  {
    name_vi: "Mận An Phước",
    scientific_name: "Syzygium samarangense",
    dia_ban: ["Bình Minh", "Tam Bình", "Long Hồ"],
    dac_tinh: "Trái đỏ sẫm ngọt mọng nước, mẫn cảm thối nhũn quả mùa mưa.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Thối nhũn quả mận mùa mưa",
        muc_do_nguy_hiem: "Nặng",
        loai: "Nấm",
        ten_khoa_hoc: "Phomopsis sp. & Colletotrichum gloeosporioides",
        trieu_chung: [
          "Rốn đít quả mận bị sũng nước thâm đen lan nhanh",
          "Trái rụng tả tơi khắp mặt đất, lên men chua thối nát"
        ],
        phan_biet: "Khác dòi đục (dòi đục có lỗ châm kim và dòi bò bên trong)",
        kiem_tra: "Bóp nhẹ phần rốn đít quả kiểm tra độ mềm nhũn",
        canh_tac: "Trùm lưới cước toàn vườn hoặc bao chùm từng chùm quả mận",
        sinh_hoc: "Phun chế phẩm sinh học Bacillus subtilis, thu gom tiêu hủy quả rụng"
      })
    ]
  },
  {
    name_vi: "Vú Sữa Lò Rèn",
    scientific_name: "Chrysophyllum cainito",
    dia_ban: ["Vũng Liêm", "Mang Thít", "Long Hồ"],
    dac_tinh: "Dòng sữa trắng ngọt ngào hương vani, cây cổ thụ nhưng dễ nhiễm thán thư quả.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Thán thư đốm mắt cua quả vú sữa",
        muc_do_nguy_hiem: "Trung bình",
        loai: "Nấm",
        ten_khoa_hoc: "Colletotrichum gloeosporioides",
        trieu_chung: [
          "Đốm tròn màu nâu lõm nhẹ vào thịt quả",
          "Trái chín bị chai cứng một bên má và giảm vị béo ngọt"
        ],
        phan_biet: "Khác rám nắng (thán thư có vòng đồng tâm và viền đen sẫm)",
        kiem_tra: "Kiểm tra chùm trái khi vỏ chuyển màu ửng tía",
        canh_tac: "Bao trái bằng túi giấy bọc chuyên dụng",
        sinh_hoc: "Phun phòng dung dịch thảo mộc tỏi ớt hoặc nấm Chaetomium"
      })
    ]
  },
  {
    name_vi: "Vú Sữa Hoàng Kim (Abiu)",
    scientific_name: "Pouteria caimito",
    dia_ban: ["Long Hồ", "Tam Bình", "Trà Ôn"],
    dac_tinh: "Vỏ vàng óng ả, thịt thạch dẻo ngọt, ưa đất ẩm giàu mùn ven sông.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Đốm đen thối chóp trái Hoàng Kim",
        muc_do_nguy_hiem: "Nặng",
        loai: "Nấm",
        ten_khoa_hoc: "Lasiodiplodia theobromae",
        trieu_chung: [
          "Chóp nhọn đuôi trái bị thâm đen khô sần lan rộng",
          "Thịt thạch bên trong sượng cứng chuyển nâu đục"
        ],
        phan_biet: "Đốm tập trung ở phần chóp nhọn phía đáy do đọng nước",
        kiem_tra: "Kiểm tra chóp đáy quả lúc sáng sớm sương đọng",
        canh_tac: "Bao quả bằng bao màng thoát ẩm không đọng giọt nước đáy",
        sinh_hoc: "Phun phòng nấm Trichoderma hoặc nano đồng định kỳ"
      })
    ]
  },
  {
    name_vi: "Thanh Long Ruột Đỏ",
    scientific_name: "Hylocereus costaricensis",
    dia_ban: ["Bình Tân", "Trà Ôn", "Tam Bình"],
    dac_tinh: "Cây họ xương rồng chịu hạn giỏi nhưng cực kỳ mẫn cảm bệnh đốm nâu tắc kè.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Đốm nâu đốm tắc kè thanh long",
        muc_do_nguy_hiem: "Cực kỳ nghiêm trọng",
        loai: "Nấm",
        ten_khoa_hoc: "Neoscytalidium dimidiatum",
        trieu_chung: [
          "Nốt sần màu nâu đỏ gồ ghề như da con tắc kè trên cành và vỏ quả",
          "Làm cành thối nát, vỏ quả sẹo mụn chai sượng thương lái loại bỏ"
        ],
        phan_biet: "Nốt sần tắc kè sần sùi đặc thù không nhầm lẫn",
        kiem_tra: "Quan sát các tai cành non và tai quả",
        canh_tac: "Cắt bỏ cành bệnh chôn sâu rải vôi bột (không vứt xuống mương)",
        sinh_hoc: "Phun nấm đối kháng Chaetomium phối hợp nano bạc đồng"
      })
    ]
  },
  {
    name_vi: "Thanh Long Ruột Trắng",
    scientific_name: "Hylocereus undatus",
    dia_ban: ["Bình Tân", "Trà Ôn"],
    dac_tinh: "Thịt trắng giòn chua ngọt thanh mát, dễ bị vi khuẩn thối mềm cành.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Thối mềm nhũn cành thanh long",
        muc_do_nguy_hiem: "Nặng",
        loai: "Vi khuẩn",
        ten_khoa_hoc: "Pectobacterium carotovorum",
        trieu_chung: [
          "Mô thịt cành ủng nước nhũn nát bốc mùi hôi thối khó chịu",
          "Thịt cành tan rữa trơ lại lõi trụ gỗ trắng"
        ],
        phan_biet: "Mùi thối chua nồng nặc và chảy nước dịch nhờn vi khuẩn",
        kiem_tra: "Bóp ngón tay thấy thịt cành mềm nhũn chảy nước đục",
        canh_tac: "Gọt sạch phần thịt nhũn tới lõi gỗ bôi vôi đặc",
        sinh_hoc: "Phun Kasugamycin hoặc đồng oxyclorua phòng ngừa"
      })
    ]
  },
  {
    name_vi: "Đu Đủ Ruột Vàng / Đài Loan",
    scientific_name: "Carica papaya",
    dia_ban: ["Bình Tân", "Long Hồ", "Tam Bình"],
    dac_tinh: "Cây thân thảo mau cho trái, mẫn cảm virus đốm vòng PRSV.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Đốm vòng virus đu đủ (PRSV)",
        muc_do_nguy_hiem: "Cực kỳ nghiêm trọng",
        loai: "Virus",
        ten_khoa_hoc: "Papaya ringspot virus",
        vector: "Rệp muội",
        trieu_chung: [
          "Lá non biến dạng co rúm chỉ còn gân như bàn tay ếch",
          "Vỏ quả nổi các vòng tròn đồng tâm như mắt kính, quả sượng đắng"
        ],
        phan_biet: "Vòng tròn đồng tâm trên vỏ quả và lá biến dạng bàn tay ếch",
        kiem_tra: "Kiểm tra mặt dưới lá tìm rệp muội truyền bệnh",
        canh_tac: "Nhổ tiêu hủy ngay cây chớm bệnh, không chiết ghép cây bệnh",
        sinh_hoc: "Phun dầu khoáng sinh học ngăn rệp chích hút truyền virus"
      })
    ]
  },
  {
    name_vi: "Dừa Xiêm Xanh",
    scientific_name: "Cocos nucifera 'Xiêm Xanh'",
    dia_ban: ["Vũng Liêm", "Trà Ôn", "Mang Thít", "Long Hồ", "Tam Bình"],
    dac_tinh: "Nước ngọt thanh, cây bờ kênh mương, dễ bị nấm thối đọt non chết cây.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Thối đọt dừa non chết điểm sinh trưởng",
        muc_do_nguy_hiem: "Cực kỳ nghiêm trọng",
        loai: "Nấm",
        ten_khoa_hoc: "Phytophthora palmivora",
        trieu_chung: [
          "Lá bẹ đọt chính ở giữa ngọn bị vàng héo gục gãy",
          "Củ hũ non bên trong thối nhũn bốc mùi hôi thối mục nát",
          "Rút nhẹ bẹ đọt non tuột ra dễ dàng, cây chết hoàn toàn"
        ],
        phan_biet: "Khác bọ dừa (bọ dừa cắn tạo vệt sọc chứ không làm thối củ hũ)",
        kiem_tra: "Kiểm tra đỉnh sinh trưởng nơi cổ bẹ đọt non đầu mùa mưa",
        canh_tac: "Vệ sinh dọn sạch rác bẹ dừa khô quanh ngọn định kỳ",
        sinh_hoc: "Bỏ muối hột trộn lưu huỳnh hoặc gói Trichoderma vào kẽ bẹ ngọn dừa"
      })
    ]
  },
  {
    name_vi: "Dừa Mã Lai (Dừa Dứa)",
    scientific_name: "Cocos nucifera 'Malay'",
    dia_ban: ["Trà Ôn", "Vũng Liêm", "Long Hồ"],
    dac_tinh: "Thân lùn mau cho trái, buồng sai trĩu, chịu mặn tốt, dễ bị cháy lá Pestalotia.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Đốm xám cháy lá dừa (Pestalotiopsis)",
        muc_do_nguy_hiem: "Trung bình",
        loai: "Nấm",
        ten_khoa_hoc: "Pestalotiopsis palmarum",
        trieu_chung: [
          "Đốm bầu dục màu nâu vàng tâm xám tro viền nâu đậm",
          "Các đốm liên kết làm cả tàu dừa bị cháy xém khô giòn"
        ],
        phan_biet: "Tâm đốm màu xám tro có hạt đen li ti viền đậm rõ rệt",
        kiem_tra: "Quan sát các tàu lá dừa phía dưới sát gốc",
        canh_tac: "Rọc bỏ tàu dừa sâu bệnh tiêu hủy, bón đủ Kali và phân chuồng hoai",
        sinh_hoc: "Phun nano đồng sinh học hoặc nấm Chaetomium"
      })
    ]
  },
  {
    name_vi: "Dừa Sáp Cầu Kè / Trà Ôn",
    scientific_name: "Cocos nucifera 'Makapuno'",
    dia_ban: ["Trà Ôn", "Vũng Liêm"],
    dac_tinh: "Cơm đặc dẻo sánh kem béo ngậy, giá trị cao kỷ lục, dễ rụng trái non do nấm.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Rụng cuống trái non dừa sáp",
        muc_do_nguy_hiem: "Nặng",
        loai: "Nấm kết hợp Dinh dưỡng",
        ten_khoa_hoc: "Colletotrichum gloeosporioides",
        trieu_chung: [
          "Trái dừa non bằng quả trứng bị nứt cuống đài sũng nước thâm đen",
          "Trái rụng hàng loạt dù buồng dừa đậu rất nhiều hoa"
        ],
        phan_biet: "Vết đốm đen quanh cuống đài hoa",
        kiem_tra: "Kiểm tra liên kết giữa đài hoa và cuống trái non",
        canh_tac: "Giữ ẩm đều đặn tránh sốc nước, bón Bo - Kẽm",
        sinh_hoc: "Phun nấm đối kháng Bacillus subtilis hoặc dịch chiết rong biển"
      })
    ]
  },
  {
    name_vi: "Chuối Già Nam Mỹ (Cavendish)",
    scientific_name: "Musa acuminata 'Cavendish'",
    dia_ban: ["Bình Tân", "Trà Ôn", "Tam Bình", "Long Hồ"],
    dac_tinh: "Trồng xuất khẩu thâm canh, đối tượng chính của bệnh héo vàng Panama TR4.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Héo rũ Panama (Fusarium oxysporum TR4)",
        muc_do_nguy_hiem: "Cực kỳ nghiêm trọng (Hủy diệt đất)",
        loai: "Nấm",
        ten_khoa_hoc: "Fusarium oxysporum f. sp. cubense (TR4)",
        trieu_chung: [
          "Lá già vàng từ mép vào gân rồi gãy gục bám quanh thân giả",
          "Cắt ngang thân giả thấy mạch dẫn chuyển màu nâu đỏ hoặc đen bầm",
          "Củ chuối thối nâu từ ngoài vào trong, cây chết khô đứng"
        ],
        phan_biet: "Mạch dẫn thân giả nâu đỏ là dấu hiệu kinh điển của Panama TR4",
        kiem_tra: "Cắt ngang thân giả cách gốc 30cm kiểm tra vòng mạch dẫn",
        canh_tac: "Đào tiêu hủy cả bụi chuối bằng vôi bột, cách ly mương nước, không trồng lại chuối",
        sinh_hoc: "Bón lót Trichoderma số lượng lớn kết hợp vi khuẩn Pseudomonas putida"
      })
    ]
  },
  {
    name_vi: "Chuối Xiêm (Chuối Sứ)",
    scientific_name: "Musa balbisiana",
    dia_ban: ["Mang Thít", "Long Hồ", "Tam Bình", "Vũng Liêm"],
    dac_tinh: "Chuối dân dã bờ ao ruộng vườn, dễ bị virus chùn đọt BBTV.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Chùn đọt chuối (Bunchy Top Virus)",
        muc_do_nguy_hiem: "Cực kỳ nghiêm trọng",
        loai: "Virus",
        ten_khoa_hoc: "Banana bunchy top virus (BBTV)",
        vector: "Rệp muội đen (Pentalonia nigronervosa)",
        trieu_chung: [
          "Lá mới ngắn ngủn dựng đứng xếp xít hình quạt ở ngọn",
          "Gân lá có các sọc đứt quãng màu xanh đậm hình chữ J hoặc dấu chấm",
          "Cây lùn tịt không trổ buồng được"
        ],
        phan_biet: "Đọt chuối chùn lại bó quạt rất đặc thù",
        kiem_tra: "Soi nách bẹ lá tìm rệp muội đen bám dày đặc",
        canh_tac: "Đào bỏ cả bụi tiêu hủy, không lấy giống từ bụi bệnh",
        sinh_hoc: "Phun xà phòng sinh học thảo mộc trừ rệp muội đen"
      })
    ]
  },
  {
    name_vi: "Sapôchê (Hồng Xiêm Mặc Bắc)",
    scientific_name: "Manilkara zapota",
    dia_ban: ["Mang Thít", "Tam Bình", "Vũng Liêm"],
    dac_tinh: "Cây gỗ bền bỉ chịu mặn và ngập khá tốt, dễ bị nấm đốm mắt chim trên lá.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Đốm lá Sapôchê (Phaeophleospora)",
        muc_do_nguy_hiem: "Trung bình",
        loai: "Nấm",
        ten_khoa_hoc: "Phaeophleospora indica",
        trieu_chung: [
          "Đốm tròn nhỏ li ti màu nâu đỏ tâm xám bạc trên lá già",
          "Lá bị khô giòn từng mảng rồi rụng sớm làm suy giảm quang hợp"
        ],
        phan_biet: "Đốm nhỏ li ti tập trung ở tầng lá già",
        kiem_tra: "Quan sát mặt trên phiến lá già dưới tán",
        canh_tac: "Quét dọn tiêu hủy lá rụng quanh gốc, bón phân chuồng hoai mục",
        sinh_hoc: "Phun thuốc gốc đồng sinh học hoặc nấm Chaetomium định kỳ"
      })
    ]
  }
];

fruits.forEach((c, idx) => {
  allCrops.push({
    id: `crop_${String(allCrops.length + 1).padStart(3, '0')}`,
    topic: "Cay_An_Trai_Dac_San",
    name_vi: c.name_vi,
    scientific_name: c.scientific_name,
    dia_ban_pho_bien: c.dia_ban,
    dac_tinh_sinh_thai: c.dac_tinh,
    danh_sach_benh: c.benh
  });
});

console.log(`Added Fruit crops. Total now: ${allCrops.length}`);

// ==================== 2. CÂY LƯƠNG THỰC & HOA MÀU (20 crops: 36 -> 55) ====================
const foodCrops = [
  {
    name_vi: "Lúa OM5451 (Hè Thu / Đông Xuân)",
    scientific_name: "Oryza sativa 'OM5451'",
    dia_ban: ["Bình Tân", "Tam Bình", "Trà Ôn", "Vũng Liêm", "Long Hồ"],
    dac_tinh: "Giống lúa thuần hạt dài cho năng suất cao thích nghi rộng khắp các cánh đồng Vĩnh Long, mẫn cảm đạo ôn và rầy nâu.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Đạo ôn lá và cổ bông (Magnaporthe oryzae)",
        muc_do_nguy_hiem: "Cực kỳ nghiêm trọng (Cháy rụi lá và lép trắng bông)",
        loai: "Nấm",
        ten_khoa_hoc: "Magnaporthe oryzae (Pyricularia oryzae)",
        trieu_chung: [
          "Vết bệnh trên lá hình mắt én (hình thoi) rộng ở giữa nhọn hai đầu",
          "Tâm vết bệnh màu xám tro, viền ngoài màu nâu đỏ đậm",
          "Cổ bông bị thâm đen sưng tóp làm cả bông lúa gãy gục hạt lép trắng 100%"
        ],
        phan_biet: "Hình mắt én đặc trưng phân biệt rõ với đốm sọc vi khuẩn (vết sọc thẳng dài ngấm nước)",
        kiem_tra: "Quan sát chóp lá non vào sáng sớm lúc có sương mù ẩm ướt",
        canh_tac: "Gieo sạ mật độ vừa phải 80-100kg/ha, giảm đạm bón tăng Kali và Silic",
        sinh_hoc: "Phun phòng bằng nấm đối kháng Chaetomium hoặc thuốc sinh học nguồn gốc Tricyclazole / Kasugamycin"
      }),
      createDisease({
        ten_benh: "Bệnh Cháy bìa lá do vi khuẩn (Bacterial Leaf Blight)",
        muc_do_nguy_hiem: "Nặng",
        loai: "Vi khuẩn",
        ten_khoa_hoc: "Xanthomonas oryzae pv. oryzae",
        trieu_chung: [
          "Vết bệnh bắt đầu từ chóp hoặc mép lá lúa rồi cháy dọc theo bìa lá uốn lượn gợn sóng",
          "Vết cháy màu vàng rơm viền xanh đậm sũng nước",
          "Sáng sớm có giọt dịch vi khuẩn đùn ra đọng ở mép lá khô lại thành hạt tròn màu hổ phách"
        ],
        phan_biet: "Mép lá cháy gợn sóng và có hạt dịch vi khuẩn vàng khô đọng ở mép",
        kiem_tra: "Cắt mẩu lá bệnh nhúng vào nước xem dịch vi khuẩn đùn ra đục như sữa",
        canh_tac: "Tháo cạn nước trong ruộng, tuyệt đối ngưng bón phân đạm và phân bón lá khi thấy chớm bệnh",
        sinh_hoc: "Phun thuốc sinh học vi khuẩn đối kháng Bacillus subtilis hoặc Kasugamycin"
      })
    ]
  },
  {
    name_vi: "Lúa Đài Thơm 8",
    scientific_name: "Oryza sativa 'Dai Thom 8'",
    dia_ban: ["Bình Tân", "Tam Bình", "Trà Ôn", "Mang Thít"],
    dac_tinh: "Cơm dẻo thơm ngon hạt gạo trong đẹp xuất khẩu, cứng cây chịu đổ ngã khá nhưng dễ bị khô vằn và lem lép hạt.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Khô vằn hại lúa (Đốm vằn)",
        muc_do_nguy_hiem: "Nặng",
        loai: "Nấm",
        ten_khoa_hoc: "Rhizoctonia solani",
        trieu_chung: [
          "Vết bệnh hình bầu dục đốm vằn da hổ màu xám xanh xuất hiện ở bẹ lá sát mặt nước",
          "Vết vằn loang dần lên các bẹ lá trên và phiến lá cờ",
          "Hạch nấm màu nâu tròn như hạt cải bám chặt trên bẹ lá"
        ],
        phan_biet: "Vết loang vằn vện da hổ và có hạch nấm tròn màu nâu hạt cải",
        kiem_tra: "Vạch gốc lúa sát mặt nước kiểm tra chân bẹ lá giai đoạn làm đòng",
        canh_tac: "Không sạ quá dày, vệ sinh dọn vớt hạch nấm trôi nổi trên mặt nước khi bừa trục",
        sinh_hoc: "Phun Validamycin sinh học hoặc nấm Trichoderma viride"
      })
    ]
  },
  {
    name_vi: "Lúa ST25 (Gạo ngon nhất thế giới)",
    scientific_name: "Oryza sativa 'ST25'",
    dia_ban: ["Vũng Liêm", "Trà Ôn", "Bình Tân"],
    dac_tinh: "Gạo đặc sản thượng hạng, thân cao lá dày, đòi hỏi quản lý rầy nâu và bệnh vàng lùn nghiêm ngặt.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Vàng lùn và Lùn xoắn lá (Rice Grassy Stunt / Ragged Stunt)",
        muc_do_nguy_hiem: "Cực kỳ nghiêm trọng (Hủy diệt cả cánh đồng)",
        loai: "Virus",
        ten_khoa_hoc: "Rice grassy stunt virus (RGSV) & Rice ragged stunt virus (RRSV)",
        vector: "Rầy nâu (Nilaparvata lugens)",
        trieu_chung: [
          "Cây lúa lùn tịt, đâm nhiều chồi vô hiệu mọc lùm bụi cỏ",
          "Lá lúa ngắn cứng, ngả vàng cam từ chóp lá lan dần vào trong",
          "Rìa lá bị rách khuyết răng cưa, gân lá có các u bướu sần sùi, nghẹn đòng không trổ được"
        ],
        phan_biet: "Khuyết mép lá và gân lá nổi u bướu sần sùi đặc thù của virus RRSV",
        kiem_tra: "Vạch gốc lúa kiểm tra mật độ rầy nâu cám và rầy cánh dài",
        canh_tac: "Tuân thủ lịch gieo sạ né rầy đồng loạt của Chi cục BVTV Vĩnh Long",
        sinh_hoc: "Bảo tồn thiên địch nhện lycosa, bọ xít nước và nấm ký sinh Metarhizium anisopliae"
      })
    ]
  },
  {
    name_vi: "Lúa Jasmine 85",
    scientific_name: "Oryza sativa 'Jasmine 85'",
    dia_ban: ["Tam Bình", "Trà Ôn", "Long Hồ"],
    dac_tinh: "Lúa thơm hạt dài truyền thống ĐBSCL, dễ nhiễm bệnh lem lép hạt trong mùa mưa rào rộ.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Lem lép hạt lúa mùa mưa",
        muc_do_nguy_hiem: "Nặng",
        loai: "Tổ hợp Nấm & Vi khuẩn",
        ten_khoa_hoc: "Fusarium sp., Bipolaris oryzae, Curvularia sp. & Pseudomonas glumae",
        trieu_chung: [
          "Vỏ trấu hạt lúa xuất hiện các đốm nâu đen lốm đốm hoặc thâm đen hoàn toàn",
          "Hạt gạo bên trong bị lép rỗng hoặc biến màu đen, gãy nát khi xay xát"
        ],
        phan_biet: "Hạt bị đen lép lốm đốm trên cả bông lúa khi vừa trổ thoát",
        kiem_tra: "Kiểm tra bông lúa khi vừa trổ lẹt xẹt và trổ đều",
        canh_tac: "Bón phân đợt đón đòng đúng tỷ lệ, không bón đạm muộn",
        sinh_hoc: "Phun phòng bằng nấm đối kháng Bacillus kết hợp hoạt chất sinh học Chitosan 2 lần (trổ lẹt xẹt và trổ đều)"
      })
    ]
  },
  {
    name_vi: "Lúa OM18",
    scientific_name: "Oryza sativa 'OM18'",
    dia_ban: ["Bình Tân", "Tam Bình", "Trà Ôn", "Vũng Liêm"],
    dac_tinh: "Chống chịu phèn mặn khá tốt, bông to hạt sáng chắc, kháng đạo ôn vừa nhưng dễ nhiễm đốm sọc vi khuẩn.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Đốm sọc vi khuẩn (Bacterial Leaf Streak)",
        muc_do_nguy_hiem: "Trung bình",
        loai: "Vi khuẩn",
        ten_khoa_hoc: "Xanthomonas oryzae pv. oryzicola",
        trieu_chung: [
          "Các sọc hẹp màu nâu sẫm chạy dọc theo giữa hai gân phụ lá lúa",
          "Khi đưa lên soi trước ánh sáng thấy vệt sọc trong suốt ngấm nước",
          "Có hạt dịch vi khuẩn màu vàng óng tròn li ti đọng trên mặt vết sọc"
        ],
        phan_biet: "Sọc hẹp bị giới hạn giữa 2 gân lá, khác với cháy bìa lá chạy dọc mép",
        kiem_tra: "Soi lá lúa ngược ánh sáng mặt trời để thấy vệt sọc trong suốt",
        canh_tac: "Tránh bón thừa đạm khi thời tiết mưa gió dập lá",
        sinh_hoc: "Phun thuốc gốc đồng sinh học hoặc Kasugamycin"
      })
    ]
  },
  {
    name_vi: "Lúa Nếp Sáp ĐBSCL",
    scientific_name: "Oryza sativa var. glutinosa",
    dia_ban: ["Bình Tân", "Tam Bình"],
    dac_tinh: "Hạt gạo nếp dẻo thơm đặc sản làm bánh truyền thống, thân mềm dễ đổ ngã và dễ nhiễm hoa cúc than vàng.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Than vàng lúa nếp (Bệnh hoa cúc / False Smut)",
        muc_do_nguy_hiem: "Trung bình",
        loai: "Nấm",
        ten_khoa_hoc: "Ustilaginoidea virens",
        trieu_chung: [
          "Hạt nếp biến thành một khối tròn phồng to bọc màng vàng cam như hoa cúc",
          "Màng vỡ ra giải phóng vô số bụi bào tử màu xanh đen than bám bẩn cả bông lúa"
        ],
        phan_biet: "Khối u tròn màu hoa cúc vàng cam rất đặc trưng",
        kiem_tra: "Quan sát bông lúa giai đoạn ngậm sữa và chín sáp",
        canh_tac: "Sử dụng giống nếp sạch bệnh, bón cân đối N-P-K",
        sinh_hoc: "Phun phòng hoạt chất gốc đồng hoặc Validamycin trước khi trổ đòng"
      })
    ]
  },
  {
    name_vi: "Khoai Lang Tím Nhật Bình Tân",
    scientific_name: "Ipomoea batatas 'Murasaki'",
    dia_ban: ["Bình Tân", "Bình Minh", "Tam Bình"],
    dac_tinh: "Đặc sản nức tiếng thủ phủ khoai lang Bình Tân - Vĩnh Long, ruột tím ngọt bùi xuất khẩu, chịu áp lực bọ hà và chết dây lỡ cổ rễ.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Chết dây lỡ cổ rễ khoai lang (Héo dây Fusarium)",
        muc_do_nguy_hiem: "Cực kỳ nghiêm trọng (Mất trắng cả ruộng)",
        loai: "Nấm",
        ten_khoa_hoc: "Fusarium oxysporum f. sp. batatas",
        trieu_chung: [
          "Dây khoai bị nứt nẻ và teo thắt ở đoạn sát gốc tiếp giáp mặt đất giồng",
          "Phần vỏ cổ dây chuyển sang màu nâu đen, lá chuyển vàng rồi héo rũ toàn bộ dây",
          "Cắt vát dây thấy mạch dẫn truyền bên trong thâm đen, củ dưới đất bị thối khô"
        ],
        phan_biet: "Đoạn cổ dây sát mặt giồng bị nứt bần thâm đen và bó mạch thâm",
        kiem_tra: "Vạch bụi khoai kiểm tra đoạn dây tiếp giáp đỉnh giồng",
        canh_tac: "Lên giồng cao thoát nước, luân canh ngập nước trồng lúa để diệt mầm nấm Fusarium trong đất",
        sinh_hoc: "Xử lý hom giống bằng dung dịch nấm đối kháng Trichoderma harzianum trước khi cắm giồng",
        khuyen_cao: "Áp dụng nghiêm quy trình luân canh Lúa - Khoai lang của Phòng NN&PTNT huyện Bình Tân"
      }),
      createDisease({
        ten_benh: "Bệnh Bọ hà (Sùng khoai lang) đục củ xì mủ đắng",
        muc_do_nguy_hiem: "Nặng",
        loai: "Côn trùng gây hại tạo điều kiện Nấm xâm nhập",
        ten_khoa_hoc: "Cylas formicarius",
        trieu_chung: [
          "Củ khoai xuất hiện các lỗ đục nhỏ tròn xì mủ đen",
          "Bên trong củ có các đường hầm ngoằn ngoèo chứa ấu trùng sùng trắng",
          "Thịt củ khoai biến thành màu nâu xám bốc mùi hôi chua hăng hắc và đắng ngắt"
        ],
        phan_biet: "Mùi hôi đắng đặc thù của củ bị sùng hà đục",
        kiem_tra: "Kiểm tra vết nứt nẻ đất giồng khoai lang",
        canh_tac: "Vun giồng cao và lấp kín các khe nứt không để bọ hà chui xuống đẻ trứng vào củ",
        sinh_hoc: "Tưới nấm ký sinh côn trùng Beauveria bassiana hoặc Metarhizium vào đất giồng"
      })
    ]
  },
  {
    name_vi: "Khoai Lang Bí (Bí Đường)",
    scientific_name: "Ipomoea batatas",
    dia_ban: ["Bình Tân", "Bình Minh"],
    dac_tinh: "Ruột màu vàng cam ngọt đậm dẻo thơm, dễ nhiễm nấm thối đen Ceratocystis.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Thối đen củ khoai lang (Black Rot)",
        muc_do_nguy_hiem: "Nặng",
        loai: "Nấm",
        ten_khoa_hoc: "Ceratocystis fimbriata",
        trieu_chung: [
          "Đốm tròn màu nâu xám hơi lõm trên vỏ củ khoai",
          "Vết bệnh ăn sâu vào thịt củ biến thịt thành màu đen cứng có vị đắng ngắt"
        ],
        phan_biet: "Thịt củ đen cứng và có vị đắng nồng nặc",
        kiem_tra: "Cạo vỏ củ kiểm tra màu sắc mô thịt bên dưới",
        canh_tac: "Tránh làm trầy xước củ khi thu hoạch, bảo quản nơi thoáng mát",
        sinh_hoc: "Ngâm củ giống trong chế phẩm nấm đối kháng Trichoderma"
      })
    ]
  },
  {
    name_vi: "Khoai Lang Trắng Sữa",
    scientific_name: "Ipomoea batatas",
    dia_ban: ["Bình Tân", "Tam Bình"],
    dac_tinh: "Ruột trắng bột nhiều giàu tinh bột, chịu khô hạn khá nhưng dễ nhiễm virus khảm lá chùn đọt.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Khảm lá virus khoai lang (Sweet Potato Feathery Mottle Virus - SPFMV)",
        muc_do_nguy_hiem: "Trung bình",
        loai: "Virus",
        ten_khoa_hoc: "Sweet potato feathery mottle virus (SPFMV)",
        vector: "Bọ phấn trắng và Rệp muội",
        trieu_chung: [
          "Lá non bị khảm các đốm vàng loang lổ dạng lông vũ dọc gân lá",
          "Dây còi cọc chùn ngọn, củ nhỏ méo mó xơ xác"
        ],
        phan_biet: "Vết khảm hình lông vũ dọc theo hai bên gân lá",
        kiem_tra: "Quan sát ngọn dây khoai non vào sáng sớm",
        canh_tac: "Chọn hom giống sạch bệnh từ các ruộng khỏe mạnh",
        sinh_hoc: "Phun xịt dầu khoáng xua đuổi bọ phấn trắng và rệp muội"
      })
    ]
  },
  {
    name_vi: "Bắp Lai Sinh Học (Ngô lai)",
    scientific_name: "Zea mays",
    dia_ban: ["Bình Minh", "Bình Tân", "Trà Ôn", "Vũng Liêm"],
    dac_tinh: "Cây trồng cạn luân canh mùa khô trên đất lúa, năng suất sinh khối bắp hạt lớn, dễ bị rỉ sắt lá và đốm lá lớn.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Rỉ sắt hại lá bắp (Puccinia sorghi)",
        muc_do_nguy_hiem: "Trung bình",
        loai: "Nấm",
        ten_khoa_hoc: "Puccinia sorghi",
        trieu_chung: [
          "Các mụn nhỏ li ti màu nâu đỏ như bột rỉ sắt xuất hiện ở cả hai mặt phiến lá bắp",
          "Lá bị khô cháy từng mảng, cây còi cọc hạt bắp không no mẩy"
        ],
        phan_biet: "Mụn bột màu nâu đỏ rỉ sắt miết ngón tay dính bột nâu",
        kiem_tra: "Miết ngón tay lên mặt lá kiểm tra bột rỉ sắt",
        canh_tac: "Vệ sinh đồng ruộng, trồng giống bắp lai kháng bệnh",
        sinh_hoc: "Phun lưu huỳnh sinh học hoặc nano bạc đồng"
      })
    ]
  },
  {
    name_vi: "Bắp Nếp Nữ Hoàng (Ngô nếp tím)",
    scientific_name: "Zea mays var. ceratina",
    dia_ban: ["Bình Minh", "Long Hồ"],
    dac_tinh: "Hạt màu tím dẻo ngọt ăn sống hoặc luộc thơm ngon giàu anthocyanin, mẫn cảm khô vằn bắp.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Đốm lá lớn hại bắp (Helminthosporium maydis)",
        muc_do_nguy_hiem: "Nặng",
        loai: "Nấm",
        ten_khoa_hoc: "Helminthosporium maydis (Bipolaris maydis)",
        trieu_chung: [
          "Vết bệnh hình thoi dài màu nâu xám chạy song song với gân lá",
          "Các vết liên kết làm toàn bộ phiến lá bị khô cháy rách tơi tả"
        ],
        phan_biet: "Vết bệnh hình thoi dài dọc theo phiến lá bắp",
        kiem_tra: "Quan sát lá bắp tầng dưới chân gốc giai đoạn trổ cờ",
        canh_tac: "Bóc bỏ bớt lá chân khô héo, bón đủ phân lân và kali",
        sinh_hoc: "Phun chế phẩm sinh học Chaetomium hoặc Trichoderma"
      })
    ]
  },
  {
    name_vi: "Bắp Mỹ Ngọt (Sweet Corn)",
    scientific_name: "Zea mays var. saccharata",
    dia_ban: ["Bình Minh", "Bình Tân", "Trà Ôn"],
    dac_tinh: "Hạt vàng óng mọng nước ngọt thanh, dễ bị sâu keo mùa thu và thối thân vi khuẩn.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Thối thân bắp vi khuẩn (Pectobacterium)",
        muc_do_nguy_hiem: "Nặng",
        loai: "Vi khuẩn",
        ten_khoa_hoc: "Pectobacterium carotovorum subsp. carotovorum",
        trieu_chung: [
          "Các lóng thân phía dưới bị sũng nước thâm đen, bốc mùi hôi thối khó chịu",
          "Thân cây bị gục ngã ngang, lá chuyển vàng héo rũ"
        ],
        phan_biet: "Thân mềm nhũn chảy nước bốc mùi hôi tanh khó ngửi",
        kiem_tra: "Ngửi và bóp nhẹ đoạn thân bắp sát mặt đất",
        canh_tac: "Tránh tưới ngập gốc vào ngày nắng nóng gay gắt",
        sinh_hoc: "Phun Kasugamycin hoặc đồng oxyclorua phòng ngừa"
      })
    ]
  },
  {
    name_vi: "Khoai Mì (Sắn KM94)",
    scientific_name: "Manihot esculenta",
    dia_ban: ["Trà Ôn", "Vũng Liêm"],
    dac_tinh: "Cây lấy củ giàu tinh bột công nghiệp, đối tượng số một của bệnh khảm lá virus sắn nguy hiểm.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Khảm lá virus sắn (Sri Lankan Cassava Mosaic Virus - SLCMV)",
        muc_do_nguy_hiem: "Cực kỳ nghiêm trọng (Hủy diệt vùng nguyên liệu)",
        loai: "Virus",
        ten_khoa_hoc: "Sri Lankan cassava mosaic virus (SLCMV)",
        vector: "Bọ phấn trắng (Bemisia tabaci)",
        trieu_chung: [
          "Lá non bị khảm vàng loang lổ xen kẽ xanh đậm, phiến lá xoăn tít biến dạng nhăn nheo",
          "Cây lùn còi cọc không phát triển củ được, củ teo tóp trơ lõi xơ"
        ],
        phan_biet: "Lá khảm xoăn tít quăn queo biến dạng bàn tay co rút",
        kiem_tra: "Vạch mặt dưới lá ngọn tìm bọ phấn trắng bay vụt lên",
        canh_tac: "Tuyệt đối không dùng hom giống từ vùng nhiễm bệnh, tiêu hủy triệt để cây bệnh",
        sinh_hoc: "Phun dầu khoáng sinh học xua đuổi bọ phấn trắng",
        khuyen_cao: "Thực hiện nghiêm công điện phòng chống dịch khảm lá sắn của Cục Trồng trọt"
      })
    ]
  },
  {
    name_vi: "Mía Đường ROC",
    scientific_name: "Saccharum officinarum",
    dia_ban: ["Trà Ôn", "Vũng Liêm"],
    dac_tinh: "Cây công nghiệp mía đường ven sông rạch, mẫn cảm bệnh thối đỏ thân mía Colletotrichum.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Thối đỏ ruột mía (Red Rot)",
        muc_do_nguy_hiem: "Nặng",
        loai: "Nấm",
        ten_khoa_hoc: "Colletotrichum falcatum",
        trieu_chung: [
          "Bổ dọc thân mía thấy ruột mía chuyển màu đỏ thẫm có các vệt ngang màu trắng",
          "Nước mía bị lên men chua bốc mùi cồn, hàm lượng đường tụt giảm nghiêm trọng",
          "Lá ngọn bị khô vàng từ chóp xuống"
        ],
        phan_biet: "Ruột mía đỏ rực xen kẽ vệt trắng ngang như vạch sơn",
        kiem_tra: "Chẻ dọc thân mía nghi ngờ kiểm tra màu sắc tủy ruột",
        canh_tac: "Chọn hom mía sạch bệnh, luân canh đất sau 2-3 vụ mía lưu gốc",
        sinh_hoc: "Xử lý hom giống bằng Trichoderma trước khi đặt rãnh"
      })
    ]
  },
  {
    name_vi: "Khoai Môn Lệ Phố / Môn Nước",
    scientific_name: "Colocasia esculenta",
    dia_ban: ["Tam Bình", "Long Hồ", "Mang Thít"],
    dac_tinh: "Cây ưa đất sình lầy ngập nước bờ mương vườn, củ dẻo thơm, dễ bị cháy lá sương mai Phytophthora.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Đốm mắt cua sương mai khoai môn",
        muc_do_nguy_hiem: "Nặng",
        loai: "Nấm",
        ten_khoa_hoc: "Phytophthora colocasiae",
        trieu_chung: [
          "Đốm tròn màu nâu sũng nước xuất hiện giữa phiến lá môn to bản",
          "Vết bệnh loang rộng có các vòng đồng tâm màu nâu vàng ứa giọt nước vàng óng",
          "Lá bị thối rách thủng lỗ to, củ môn bị thối úng nhũn dưới bùn"
        ],
        phan_biet: "Vết thối rách thủng lỗ to có vòng đồng tâm rỉ giọt nước vàng",
        kiem_tra: "Quan sát phiến lá to bản sau đợt mưa rào ẩm thấp",
        canh_tac: "Trồng mật độ vừa phải, tháo bớt nước mương không để ngập úng gốc kéo dài",
        sinh_hoc: "Phun chế phẩm sinh học Fosetyl-Aluminium hoặc nấm Chaetomium"
      })
    ]
  },
  {
    name_vi: "Khoai Từ",
    scientific_name: "Dioscorea esculenta",
    dia_ban: ["Bình Tân", "Trà Ôn"],
    dac_tinh: "Cây dây leo có gai, củ nhỏ ăn thơm ngọt thanh mát, dễ bị nấm thán thư cháy lá.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Thán thư cháy đen dây khoai từ",
        muc_do_nguy_hiem: "Trung bình",
        loai: "Nấm",
        ten_khoa_hoc: "Colletotrichum gloeosporioides",
        trieu_chung: [
          "Lá xuất hiện đốm đen góc cạnh rồi lan rộng làm cháy khô cả lá",
          "Dây leo bị thâm đen và chết rụi từ ngọn lùi dần xuống gốc"
        ],
        phan_biet: "Dây leo thâm đen khô giòn làm củ dưới đất ngừng lớn",
        kiem_tra: "Kiểm tra ngọn dây leo vào mùa mưa ẩm",
        canh_tac: "Cắm chà giàn leo cao ráo thoáng gió",
        sinh_hoc: "Phun nấm đối kháng Trichoderma hoặc đồng nano sinh học"
      })
    ]
  },
  {
    name_vi: "Khoai Mỡ Tím",
    scientific_name: "Dioscorea alata",
    dia_ban: ["Bình Tân", "Tam Bình", "Trà Ôn"],
    dac_tinh: "Củ to nhiều tinh bột tím nấu canh thơm dẻo, chịu phèn khá tốt, mẫn cảm thối khô củ do tuyến trùng.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Thối khô da củ khoai mỡ do tuyến trùng",
        muc_do_nguy_hiem: "Nặng",
        loai: "Tuyến trùng",
        ten_khoa_hoc: "Scutellonema bradys",
        trieu_chung: [
          "Lớp da ngoài củ khoai mỡ bị nứt nẻ sần sùi màu nâu đen",
          "Dưới lớp vỏ xuất hiện lớp mô thịt khô xơ màu nâu xám dày 1-2cm không ăn được"
        ],
        phan_biet: "Lớp mô thịt dưới vỏ bị khô xơ nâu đen như bã mía",
        kiem_tra: "Gọt nhẹ lớp vỏ củ kiểm tra mô thịt sát bìa",
        canh_tac: "Lựa củ giống không bị nứt sần, luân canh với lúa nước",
        sinh_hoc: "Tưới nấm ký sinh tuyến trùng Paecilomyces lilacinus vào giồng đất"
      })
    ]
  },
  {
    name_vi: "Củ Dong Riềng (Bình Tinh)",
    scientific_name: "Canna edulis",
    dia_ban: ["Mang Thít", "Vũng Liêm", "Long Hồ"],
    dac_tinh: "Cây lấy củ mài tinh bột làm miến dong bánh lọt, ưa ẩm bờ kênh, dễ bị nấm đốm rỉ lá.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Rỉ lá đốm nâu dong riềng (Puccinia thaliae)",
        muc_do_nguy_hiem: "Nhẹ",
        loai: "Nấm",
        ten_khoa_hoc: "Puccinia thaliae",
        trieu_chung: [
          "Mặt dưới lá xuất hiện các chấm mụn rỉ sắt màu vàng cam",
          "Lá nhanh vàng và khô cháy sớm làm giảm kích thước củ"
        ],
        phan_biet: "Mụn phấn vàng cam ở mặt dưới lá dong",
        kiem_tra: "Lật mặt dưới phiến lá dong riềng kiểm tra",
        canh_tac: "Cắt bỏ lá già sát gốc tiêu hủy, bón phân chuồng",
        sinh_hoc: "Phun lưu huỳnh vôi hoặc nano bạc sinh học"
      })
    ]
  },
  {
    name_vi: "Lạc / Đậu Phộng ĐBSCL",
    scientific_name: "Arachis hypogaea",
    dia_ban: ["Bình Minh", "Bình Tân", "Trà Ôn"],
    dac_tinh: "Cây họ đậu làm giàu đạm cho đất bãi bồi ven sông, dễ bị héo xanh vi khuẩn và đốm lá Cercospora.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Héo xanh vi khuẩn đậu phộng (Ralstonia)",
        muc_do_nguy_hiem: "Cực kỳ nghiêm trọng",
        loai: "Vi khuẩn",
        ten_khoa_hoc: "Ralstonia solanacearum",
        trieu_chung: [
          "Cây đang xanh tươi bỗng héo rũ cụp xuống trong 1-2 ngày mà lá vẫn còn giữ màu xanh",
          "Cổ rễ thâm đen ủng nước, cắt ngang nhúng vào ly nước thấy dòng vi khuẩn trắng đùn ra như khói thuốc lá"
        ],
        phan_biet: "Cây chết khi lá vẫn xanh tươi; dòng dịch khuẩn trắng đùn ra trong nước",
        kiem_tra: "Thử nghiệm ngâm gốc cây héo vào ly nước trong suốt kiểm tra dòng khuẩn",
        canh_tac: "Luân canh triệt để với lúa nước, không trồng đậu phộng liên tục nhiều vụ",
        sinh_hoc: "Tưới vi khuẩn đối kháng Bacillus subtilis hoặc chế phẩm Kasugamycin"
      })
    ]
  },
  {
    name_vi: "Đậu Nành / Đậu Tương",
    scientific_name: "Glycine max",
    dia_ban: ["Bình Minh", "Bình Tân"],
    dac_tinh: "Cây họ đậu lấy hạt giàu đạm thực vật, dễ nhiễm bệnh rỉ sắt Phakopsora gây rụng lá hàng loạt.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Rỉ sắt đậu nành (Phakopsora pachyrhizi)",
        muc_do_nguy_hiem: "Nặng",
        loai: "Nấm",
        ten_khoa_hoc: "Phakopsora pachyrhizi",
        trieu_chung: [
          "Các mụn nhỏ li ti màu nâu đỏ xuất hiện ở mặt dưới lá đậu nành",
          "Lá bị biến vàng khô cháy và rụng trút sớm làm trái lép hạt"
        ],
        phan_biet: "Mặt dưới lá phủ đầy mụn bột màu nâu rỉ sét",
        kiem_tra: "Soi mặt dưới phiến lá đậu nành thời kỳ trổ hoa làm quả",
        canh_tac: "Trồng đúng mật độ, bón đủ lân và kali",
        sinh_hoc: "Phun phòng bằng nấm đối kháng Chaetomium hoặc thuốc sinh học nguồn gốc nano đồng"
      })
    ]
  }
];

foodCrops.forEach((c) => {
  allCrops.push({
    id: `crop_${String(allCrops.length + 1).padStart(3, '0')}`,
    topic: "Cay_Luong_Thuc_Mau",
    name_vi: c.name_vi,
    scientific_name: c.scientific_name,
    dia_ban_pho_bien: c.dia_ban,
    dac_tinh_sinh_thai: c.dac_tinh,
    danh_sach_benh: c.benh
  });
});

console.log(`Added Food crops. Total now: ${allCrops.length}`);

// ==================== 3. RAU ĂN LÁ & ĂN QUẢ (35 crops: 56 -> 90) ====================
const vegList = [
  { name: "Cà Chua Bi / Cà Chua Leo", sci: "Solanum lycopersicum", benh_chinh: "Mốc sương sương mai (Phytophthora infestans)" },
  { name: "Ớt Chỉ Thiên Vĩnh Long", sci: "Capsicum annuum", benh_chinh: "Thán thư ớt thối ướt (Colletotrichum capsici)" },
  { name: "Ớt Sừng Vàng", sci: "Capsicum frutescens", benh_chinh: "Khảm lá virus ớt do bọ phấn (Chilli Veinal Mottle Virus)" },
  { name: "Cà Tím Dài", sci: "Solanum melongena", benh_chinh: "Héo xanh vi khuẩn cà tím (Ralstonia solanacearum)" },
  { name: "Dưa Hấu Mặt Trời Đỏ", sci: "Citrullus lanatus", benh_chinh: "Nứt thân chảy mủ dưa hấu (Didymella bryoniae)" },
  { name: "Dưa Leo / Dưa Chuột Baby", sci: "Cucumis sativus", benh_chinh: "Sương mai giả dưa leo (Pseudoperonospora cubensis)" },
  { name: "Khổ Qua (Mướp Đắng Rừng)", sci: "Momordica charantia", benh_chinh: "Phấn trắng hại khổ qua (Podosphaera xanthii)" },
  { name: "Bầu Sao Vĩnh Long", sci: "Lagenaria siceraria", benh_chinh: "Bệnh Khảm lá virus bầu (Cucumber Mosaic Virus - CMV)" },
  { name: "Bí Đao Chanh (Bí Sáp)", sci: "Benincasa hispida", benh_chinh: "Bệnh Thối hoa thối ngọn bí đao (Choanephora cucurbitarum)" },
  { name: "Bí Đỏ / Bí Hạt Đậu", sci: "Cucurbita moschata", benh_chinh: "Bệnh Đốm phấn vàng lá bí đỏ (Pseudoperonospora cubensis)" },
  { name: "Mướp Hương", sci: "Luffa cylindrica", benh_chinh: "Bệnh Bọ trĩ xoăn đọt mướp hương (Thrips palmi)" },
  { name: "Đậu Bắp Cao Sản", sci: "Abelmoschus esculentus", benh_chinh: "Bệnh Khảm vàng gân lá đậu bắp (Bhendi Yellow Vein Mosaic Virus)" },
  { name: "Đậu Cô Ve Lùn", sci: "Phaseolus vulgaris", benh_chinh: "Bệnh Rỉ sắt lá đậu cô ve (Uromyces appendiculatus)" },
  { name: "Đậu Đũa Hạt Đen", sci: "Vigna unguiculata subsp. sesquipedalis", benh_chinh: "Bệnh Héo vàng rụng lá Fusarium (Fusarium oxysporum)" },
  { name: "Rau Muống Nước / Muống Ruộng", sci: "Ipomoea aquatica", benh_chinh: "Bệnh Rỉ trắng rau muống (Albugo ipomoeae-aquaticae)" },
  { name: "Cải Xanh Mỡ", sci: "Brassica juncea", benh_chinh: "Bệnh Thối nhũn bẹ cải xanh vi khuẩn (Pectobacterium carotovorum)" },
  { name: "Cải Ngọt Ăn Lá", sci: "Brassica integrifolia", benh_chinh: "Bệnh Chết rạp cây con nấm (Pythium debaryanum)" },
  { name: "Cải Thìa / Cải Chíp", sci: "Brassica rapa subsp. chinensis", benh_chinh: "Bệnh Đốm vòng đen Alternaria (Alternaria brassicae)" },
  { name: "Cải Bắp Trắng", sci: "Brassica oleracea var. capitata", benh_chinh: "Bệnh Đốm đen chân bắp cải (Phoma lingam)" },
  { name: "Cải Thảo Xoăn", sci: "Brassica rapa subsp. pekinensis", benh_chinh: "Bệnh Thối hạch sương nấm trắng (Sclerotinia sclerotiorum)" },
  { name: "Xà Lách Búp Mỡ", sci: "Lactuca sativa", benh_chinh: "Bệnh Cháy rìa lá sinh lý thiếu canxi (Tipburn)" },
  { name: "Xà Lách Romaine", sci: "Lactuca sativa var. longifolia", benh_chinh: "Bệnh Đốm vi khuẩn xà lách (Xanthomonas campestris pv. vitians)" },
  { name: "Hành Lá Gốc Trắng", sci: "Allium fistulosum", benh_chinh: "Bệnh Thối gốc hành lá mốc trắng (Sclerotium cepivorum)" },
  { name: "Hẹ Ăn Lá Vĩnh Long", sci: "Allium tuberosum", benh_chinh: "Bệnh Đốm tím lá hẹ (Alternaria porri)" },
  { name: "Rau Ngót / Bồ Ngót", sci: "Sauropus androgynus", benh_chinh: "Bệnh Xoăn lá chùn ngọn rau ngót do bọ trĩ" },
  { name: "Rau Mồng Tơi", sci: "Basella alba", benh_chinh: "Bệnh Đốm mắt cua lá mồng tơi (Cercospora basellae)" },
  { name: "Rau Đay Quả Dài", sci: "Corchorus olitorius", benh_chinh: "Bệnh Cháy lá đốm nâu rau đay (Rhizoctonia solani)" },
  { name: "Rau Càng Cua", sci: "Peperomia pellucida", benh_chinh: "Bệnh Thối nhũn ướt thân mềm rau càng cua (Pectobacterium)" },
  { name: "Rau Má Bờ Ruộng", sci: "Centella asiatica", benh_chinh: "Bệnh Đốm lá tròn rau má (Cercospora centellae)" },
  { name: "Rau Diếp Cá", sci: "Houttuynia cordata", benh_chinh: "Bệnh Thối gốc lở cổ rễ diếp cá (Rhizoctonia)" },
  { name: "Cần Tây ĐBSCL", sci: "Apium graveolens", benh_chinh: "Bệnh Đốm lá sương mai cần tây (Septoria apiicola)" },
  { name: "Cần Nước Vĩnh Long", sci: "Oenanthe javanica", benh_chinh: "Bệnh Rỉ sắt lá cần nước (Puccinia oenanthes)" },
  { name: "Rau Đắng Đất / Rau Đắng Biển", sci: "Glinus oppositifolius", benh_chinh: "Bệnh Thối nhũn thân rau đắng sau mưa" },
  { name: "Bạc Hà / Dọc Mùng", sci: "Alocasia odora", benh_chinh: "Bệnh Thối nhũn bẹ bạc hà (Pythium sp.)" },
  { name: "Ngò Gai / Mùi Tàu", sci: "Eryngium foetidum", benh_chinh: "Bệnh Thối thâm tim lá ngò gai vi khuẩn" }
];

vegList.forEach((v) => {
  allCrops.push({
    id: `crop_${String(allCrops.length + 1).padStart(3, '0')}`,
    topic: "Rau_An_La_An_Qua",
    name_vi: v.name,
    scientific_name: v.sci,
    dia_ban_pho_bien: ["Bình Tân", "Bình Minh", "Long Hồ", "Tam Bình", "TP. Vĩnh Long"],
    dac_tinh_sinh_thai: "Rau màu phát triển trên đất phù sa nhẹ tơi xốp ven sông, yêu cầu tưới ẩm tiêu úng tức thì, luân canh liên tục để hạn chế tích lũy mầm bệnh đất.",
    danh_sach_benh: [
      createDisease({
        ten_benh: v.benh_chinh,
        muc_do_nguy_hiem: "Nặng",
        loai: v.benh_chinh.includes("vi khuẩn") ? "Vi khuẩn" : v.benh_chinh.includes("Virus") ? "Virus" : "Nấm",
        ten_khoa_hoc: v.benh_chinh.split('(')[1] ? v.benh_chinh.split('(')[1].replace(')', '') : "Tổ hợp vi sinh vật gây hại",
        trieu_chung: [
          `Triệu chứng điển hình gây hại bộ phận lá, chồi hoặc thân cây ${v.name}`,
          "Mô bào bị ngậm nước, biến màu nâu xám hoặc vàng úa, làm giảm nhanh khả năng quang hợp",
          "Cây suy kiệt, lá rụng hoặc thân bị đổ rạp gục ngã"
        ],
        phan_biet: "Phân biệt triệu chứng nấm (có lớp mốc tơ) với vi khuẩn (mùi hôi tanh sũng nước) hoặc virus (khảm lá xoăn ngọn)",
        kiem_tra: `Quan sát phiến lá và vùng cổ rễ cây ${v.name} vào buổi sáng sớm`,
        canh_tac: "Lên liếp cao ráo, phủ bạt nilon nông nghiệp, bón vôi bột khử trùng đất trước khi xuống giống",
        sinh_hoc: "Tưới nấm đối kháng Trichoderma harzianum hoặc phun chế phẩm sinh học Bacillus subtilis định kỳ 7-10 ngày/lần"
      })
    ]
  });
});

console.log(`Added Vegetable crops. Total now: ${allCrops.length}`);

// ==================== 4. CÂY CÔNG NGHIỆP & DƯỢC LIỆU (15 crops: 91 -> 105) ====================
const indAndMed = [
  { name: "Sen Đồng Tháp Mười / Trà Ôn", sci: "Nelumbo nucifera", benh: "Bệnh Thối ngó thối củ sen (Pythium / Fusarium)" },
  { name: "Nấm Rơm Rơm Cấy Vĩnh Long", sci: "Volvariella volvacea", benh: "Bệnh Nấm mốc xanh thối meo nấm rơm (Trichoderma viride mọc dại)" },
  { name: "Nấm Mèo / Mộc Nhĩ", sci: "Auricularia auricula-judae", benh: "Bệnh Mốc đen mốc thoi mộc nhĩ (Aspergillus niger)" },
  { name: "Gừng Dé / Gừng Trâu", sci: "Zingiber officinale", benh: "Bệnh Thối củ gừng vi khuẩn héo xanh (Ralstonia solanacearum)" },
  { name: "Nghệ Vàng Củ", sci: "Curcuma longa", benh_chinh: "Bệnh Đốm mắt cua lá nghệ (Colletotrichum curcumae)" },
  { name: "Sả Chanh ĐBSCL", sci: "Cymbopogon citratus", benh_chinh: "Bệnh Rỉ sắt lá sả (Puccinia nakanishikii)" },
  { name: "Đinh Lăng Lá Xẻ (Sâm Nam)", sci: "Polyscias fruticosa", benh_chinh: "Bệnh Thối đen rễ củ đinh lăng (Fusarium oxysporum)" },
  { name: "Nha Đam / Lô Hội Mỹ", sci: "Aloe vera", benh_chinh: "Bệnh Đốm đen thối nhũn lá nha đam (Aloe Black Spot)" },
  { name: "Cà Gai Leo Vĩnh Long", sci: "Solanum procumbens", benh_chinh: "Bệnh Lở cổ rễ cà gai leo con (Rhizoctonia solani)" },
  { name: "Trà Hoa Vàng", sci: "Camellia chrysantha", benh_chinh: "Bệnh Thán thư cháy lá búp trà hoa vàng" },
  { name: "Mã Đề / Xa Tiền Tử", sci: "Plantago major", benh_chinh: "Bệnh Đốm phấn sương mai mã đề" },
  { name: "Chùm Ngây Dinh Dưỡng", sci: "Moringa oleifera", benh_chinh: "Bệnh Đốm lá đốm nâu chùm ngây" },
  { name: "Cỏ Ngọt Stevia", sci: "Stevia rebaudiana", benh_chinh: "Bệnh Héo rũ gốc mốc trắng cỏ ngọt (Sclerotium rolfsii)" },
  { name: "Kim Ngân Hoa Dược Liệu", sci: "Lonicera japonica", benh_chinh: "Bệnh Phấn trắng lá hoa kim ngân (Microsphaera lonicerae)" },
  { name: "Dâu Tằm Ăn Quả (Morus)", sci: "Morus alba", benh_chinh: "Bệnh Rỉ sắt đốm nâu lá dâu tằm (Aecidium mori)" }
];

indAndMed.forEach((item) => {
  allCrops.push({
    id: `crop_${String(allCrops.length + 1).padStart(3, '0')}`,
    topic: "Cay_Cong_Nghiep_Duoc_Lieu",
    name_vi: item.name,
    scientific_name: item.sci,
    dia_ban_pho_bien: ["Trà Ôn", "Vũng Liêm", "Long Hồ", "Mang Thít", "Bình Tân"],
    dac_tinh_sinh_thai: "Cây công nghiệp ngắn ngày và cây dược liệu có giá trị kinh tế cao, yêu cầu đất giàu hữu cơ thoát nước tốt, hạn chế tối đa dư lượng hóa chất theo tiêu chuẩn VietGAP/GACP-WHO.",
    danh_sach_benh: [
      createDisease({
        ten_benh: item.benh || item.benh_chinh,
        muc_do_nguy_hiem: "Nặng",
        loai: (item.benh || item.benh_chinh).includes("vi khuẩn") ? "Vi khuẩn" : "Nấm",
        ten_khoa_hoc: (item.benh || item.benh_chinh).split('(')[1] ? (item.benh || item.benh_chinh).split('(')[1].replace(')', '') : "Tổ hợp nấm bệnh đặc hữu",
        trieu_chung: [
          `Triệu chứng tổn thương mô rễ, thân củ hoặc lá của cây dược liệu ${item.name}`,
          "Vết bệnh chuyển thâm đen thối rữa hoặc nứt nẻ, cản trở tổng hợp hoạt chất dược tính",
          "Cây suy kiệt rụng lá, củ bị thối úng mục nát"
        ],
        phan_biet: "Khác với thiếu chất sinh lý (vết bệnh nấm có bào tử hoặc tơ sợi, vi khuẩn có mùi tanh thối)",
        kiem_tra: `Kiểm tra rễ củ và phiến lá ${item.name}`,
        canh_tac: "Trồng mật độ chuẩn, nâng luống cao ráo thoát nước triệt để trong mùa mưa bão",
        sinh_hoc: "Tưới nấm đối kháng Trichoderma phối hợp nấm cộng sinh rễ Glomus intraradices (Mycorrhiza)"
      })
    ]
  });
});

console.log(`Generated total crops: ${allCrops.length}`);

// Output JSON file
const outputPath = path.join(__dirname, '..', 'src', 'data', 'vinh_long_plant_pathology_100_crops.json');
fs.writeFileSync(outputPath, JSON.stringify(allCrops, null, 2), 'utf-8');
console.log(`Successfully wrote ${allCrops.length} crops to ${outputPath}`);
