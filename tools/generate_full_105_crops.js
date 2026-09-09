/**
 * Dataset Generator for AgriVision
 * Author: Phan Trọng Khang (Lớp 9¹, THCS Vĩnh An, Vĩnh Long)
 * Target: 105 crops in Vinh Long & Mekong Delta with comprehensive clinical pathology schemas.
 */

const fs = require('fs');
const path = require('path');

const districts = ['Bình Minh', 'Tam Bình', 'Trà Ôn', 'Vũng Liêm', 'Long Hồ', 'Mang Thít', 'Bình Tân', 'TP. Vĩnh Long'];

// Helper to assemble disease item
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
  const tac_nhan = {
    loai,
    ten_khoa_hoc,
  };
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

// 1. CÂY ĂN TRÁI ĐẶC SẢN (35 cây)
const cayAnTrai = [
  {
    name_vi: "Bưởi Năm Roi Bình Minh",
    scientific_name: "Citrus maxima 'Nam Roi'",
    dia_ban: ["Bình Minh", "Tam Bình", "Trà Ôn"],
    dac_tinh: "Cây ưa đất phù sa bồi lắng ven sông Hậu, thoát nước tốt, độ pH thích hợp từ 5.5 - 6.5, cực kỳ mẫn cảm với úng và mặn.",
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
        phan_biet: "Khác với thiếu vi lượng kẽm/mangan (vết vàng đối xứng đều qua gân lá) và vàng lá thối rễ (vàng đều cả phiến lá lẫn gân, rễ tơ tuột vỏ thối đen)",
        kiem_tra: "Kiểm tra mặt dưới lá và đọt non tìm rầy chổng cánh đuôi vểnh 45 độ; kiểm tra tính bất đối xứng vết vàng phiến lá",
        canh_tac: "Cắt bỏ tiêu hủy cây bệnh nặng, trồng cây giống vi ghép sạch bệnh sạch rầy, tạo tán thông thoáng",
        sinh_hoc: "Nuôi kiến vàng (Oecophylla smaragdina) bảo vệ vườn cam bưởi, phun nấm ký sinh Beauveria bassiana hoặc dầu khoáng SK Enspray 99EC",
        khuyen_cao: "Liên hệ Trạm Khuyến nông Bình Minh / Tam Bình để lấy mẫu xét nghiệm định lượng bằng phương pháp PCR"
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
        phan_biet: "Khác với Ghẻ nhám (Elsinoë fawcettii do nấm): Ghẻ loét vi khuẩn có miệng núi lửa và quầng vàng bao quanh; Ghẻ nhám chóp nhọn nhô lên như hạt mụn cơm ráp tay và không có quầng vàng",
        kiem_tra: "Dùng kính lúp kiểm tra vết nứt miệng núi lửa và quầng halo sáng màu",
        canh_tac: "Tỉa bỏ cành lá nhiễm bệnh sau mỗi đợt lộc non, vệ sinh kéo cắt cành bằng cồn",
        sinh_hoc: "Phun phòng luân phiên các hoạt chất gốc đồng nano sinh học, Kasugamycin, nấm đối kháng Bacillus subtilis",
        khuyen_cao: "Phòng ngừa sâu vẽ bùa lứa lộc non vì vết thương sâu cắn là cửa ngõ chính truyền bệnh"
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
        kiem_tra: "Bới nhẹ lớp đất vùng rìa tán lá (hình chiếu tán) để kiểm tra đầu chóp rễ tơ và vỏ rễ",
        canh_tac: "Đào rãnh thoát nước sâu giữa các liếp bưởi, rải vôi bột (500g/cây) khử trùng đất và ổn định pH 6.0",
        sinh_hoc: "Tưới nấm đối kháng Trichoderma harzianum + Streptomyces kết hợp hoạt chất trừ tuyến trùng sinh học Chitosan / Paecilomyces"
      }),
      createDisease({
        ten_benh: "Bệnh Thối nâu nứt thân chảy mủ (Chảy gôm)",
        muc_do_nguy_hiem: "Nặng",
        loai: "Nấm",
        ten_khoa_hoc: "Phytophthora citrophthora",
        trieu_chung: [
          "Vỏ thân gần cổ rễ bị sũng nước, thâm đen và nứt dọc",
          "Dịch nhựa mủ màu vàng hổ phách chảy ra từ vết nứt, sau đó đặc lại",
          "Gỗ bên dưới vỏ chuyển sang màu nâu sẫm, cây suy kiệt rụng lá rụng trái"
        ],
        phan_biet: "Khác với hiện tượng xì mủ sinh lý do bón thừa đạm (vỏ gỗ không bị mục nâu)",
        kiem_tra: "Dùng dao bén cạo nhẹ lớp vỏ bị ướt để kiểm tra ranh giới thâm đen của lớp tế bào thượng tầng",
        canh_tac: "Không để gốc cây ngập nước, quét vôi pha thuốc gốc đồng quanh gốc cao 0.8m định kỳ đầu và cuối mùa mưa",
        sinh_hoc: "Cạo sạch vết thâm rồi quét đậm đặc Fosetyl-aluminium hoặc nấm đối kháng Chaetomium"
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
        phan_biet: "Cần phân biệt kỹ với bệnh vàng lá do nấm Fusarium (lá rụng khi còn vàng, không có hiện tượng gân nổi gồ)",
        kiem_tra: "Dùng bẫy dính màu vàng theo dõi mật độ rầy chổng cánh trong vườn",
        canh_tac: "Trồng xen ổi xá lị hoặc ổi nữ hoàng để xua đuổi rầy chổng cánh bằng hương tinh dầu tự nhiên",
        sinh_hoc: "Ứng dụng chế phẩm vi sinh Metarhizium anisopliae + Beauveria bassiana xịt khi cây nhú lộc 1-2cm"
      }),
      createDisease({
        ten_benh: "Bệnh Nấm hồng",
        muc_do_nguy_hiem: "Trung bình",
        loai: "Nấm",
        ten_khoa_hoc: "Erythricium salmonicolor (Corticium salmonicolor)",
        trieu_chung: [
          "Màng sợi nấm màu trắng mỏng xuất hiện ở các chảng ba cành cam",
          "Sợi nấm dày lên và chuyển sang màu hồng phấn đặc trưng",
          "Vỏ cành nứt nẻ, lá phía trên vết bệnh héo rũ, khô chết giòn trên cây"
        ],
        phan_biet: "Màu hồng phấn rất đặc trưng không lẫn với các bệnh thán thư hay bồ hóng",
        kiem_tra: "Quan sát kỹ các ngã ba cành tán rậm rạp trong mùa mưa",
        canh_tac: "Cắt tỉa cành vô hiệu, giữ mật độ vườn thông thoáng nhận đủ ánh nắng",
        sinh_hoc: "Quét vôi bột hòa đồng sulfat (thuốc Bordeaux 1%) hoặc phun chế phẩm Validamycin"
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
        ten_benh: "Bệnh Thán thư hại hoa và trái non (Colletotrichum)",
        muc_do_nguy_hiem: "Nặng",
        loai: "Nấm",
        ten_khoa_hoc: "Colletotrichum gloeosporioides",
        trieu_chung: [
          "Cánh hoa xuất hiện đốm màu nâu cam sũng nước rồi thối rụng",
          "Trái non bị đốm đen lõm sâu, cuống trái chuyển màu nâu làm rụng cuống trơ đài",
          "Chồi non bị thối đen từ ngọn lan dần xuống dưới (chết ngọn die-back)"
        ],
        phan_biet: "Khác với rụng sinh lý do sốc nước (trái rụng cả cuống xanh tươi, không có chấm nâu đen)",
        kiem_tra: "Kiểm tra đài hoa và đọt non sau những trận mưa dầm liên tục",
        canh_tac: "Bón phân cân đối N-P-K, bổ sung Canxi-Bo để tăng độ dẻo dai của cuống hoa và cuống trái",
        sinh_hoc: "Phun phòng bằng nấm đối kháng Chaetomium cupreum hoặc dịch chiết tỏi ớt gừng"
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
        ten_benh: "Bệnh Đốm dầu (Greasy Spot)",
        muc_do_nguy_hiem: "Trung bình",
        loai: "Nấm",
        ten_khoa_hoc: "Mycosphaerella citri",
        trieu_chung: [
          "Mặt dưới lá xuất hiện những đốm màu vàng cam như giọt dầu loang",
          "Sau đó vết đốm sẫm lại thành màu nâu sậm hay đen bóng như hắc ín",
          "Mặt trên lá đối diện vết đốm bị ngả vàng, làm lá rụng sớm khiến cây suy kiệt"
        ],
        phan_biet: "Khác với nấm muội đen bồ hóng (bồ hóng bám như lớp bột lau sạch được, đốm dầu ăn sâu vào mô lá không lau được)",
        kiem_tra: "Soi dưới kính lúp mặt dưới phiến lá già",
        canh_tac: "Quét dọn thu gom lá rụng dưới gốc tiêu hủy để cắt đứt nguồn bào tử",
        sinh_hoc: "Phun dầu khoáng sinh học kết hợp chế phẩm nấm đối kháng Trichoderma"
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
        ten_benh: "Bệnh Đốm nâu lá và trái (Alternaria Brown Spot)",
        muc_do_nguy_hiem: "Nặng",
        loai: "Nấm",
        ten_khoa_hoc: "Alternaria alternata pv. citri",
        trieu_chung: [
          "Đốm nhỏ màu nâu đen có quầng vàng xuất hiện trên lộc non và vỏ quả quýt",
          "Vết bệnh loang rộng hình tròn bất định, làm lộc non biến dạng quăn queo rụng sớm",
          "Vỏ trái bị đốm thâm đen lõm vào, làm quả sượng chai mất giá trị thương phẩm"
        ],
        phan_biet: "Khác với Ghẻ loét: Alternaria không có miệng núi lửa nứt nẻ sùi mô bần",
        kiem_tra: "Quan sát lá non và vỏ quả khi đường kính quả đạt 2-4cm",
        canh_tac: "Tránh tưới nước phun mưa trực tiếp lên tán vào buổi chiều mát tạo ẩm độ cao",
        sinh_hoc: "Sử dụng chế phẩm sinh học chứa Bacillus amyloliquefaciens phun định kỳ 10 ngày/lần"
      })
    ]
  },
  {
    name_vi: "Chanh Không Hạt (Chanh Limca)",
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
          "Nốt mụn cơm nhô cao sần sùi màu vàng nâu ở mặt dưới lá và cành non",
          "Lá bị vặn vẹo, cong queo gồ ghề hình lòng chảo",
          "Vỏ trái chanh nổi nhiều mụn sẹo sần sùi ráp tay"
        ],
        phan_biet: "Khác với Ghẻ loét vi khuẩn: Ghẻ nhám không có quầng vàng và không nứt rách miệng núi lửa",
        kiem_tra: "Dùng ngón tay sờ bề mặt lộc non thấy gồ ghề ráp nhám rõ rệt",
        canh_tac: "Cắt tỉa cành sâu bệnh, đốt tiêu hủy tàn dư sau mỗi đợt cắt trái",
        sinh_hoc: "Phun thuốc gốc đồng oxyclorua hoặc tinh dầu thảo mộc neem oil"
      })
    ]
  },
  {
    name_vi: "Chanh Giấy Vĩnh Long",
    scientific_name: "Citrus aurantifolia",
    dia_ban: ["Long Hồ", "Tam Bình", "Trà Ôn"],
    dac_tinh: "Vỏ mỏng, thơm nồng đậm đà, rất mẫn cảm với virus Tristeza truyền qua rệp muội đen.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Tristeza (Bệnh tàn lụi gân trong)",
        muc_do_nguy_hiem: "Cực kỳ nghiêm trọng",
        loai: "Virus",
        ten_khoa_hoc: "Citrus tristeza virus (CTV)",
        vector: "Rệp muội đen (Toxoptera citricida)",
        trieu_chung: [
          "Gân phụ của lá non bị trong suốt khi đưa lên soi ngược ánh sáng (vein clearing)",
          "Thân cành và thân chính bị lõm gai vào trong phần gỗ khi bóc lớp vỏ ra (stem pitting)",
          "Cây sinh trưởng còi cọc, vàng lá và khô tàn nhánh dần từ đọt"
        ],
        phan_biet: "Dấu hiệu gai nhọn chọc lõm vào thân gỗ là triệu chứng độc quyền của virus Tristeza",
        kiem_tra: "Cạo lớp vỏ ngoài thân cành xem có các lỗ nhỏ li ti châm kim ăn lõm vào lõi gỗ hay không",
        canh_tac: "Tiêu hủy triệt để cây bệnh, nhân giống bằng mắt ghép trên gốc ghép kháng CTV như cam chua Volkameriana",
        sinh_hoc: "Kiểm soát rệp muội bằng cách phun dầu khoáng sinh học và bảo vệ bọ rùa đỏ thiên địch"
      })
    ]
  },
  {
    name_vi: "Sầu Riêng Ri6 Vĩnh Long",
    scientific_name: "Durio zibethinus 'Ri6'",
    dia_ban: ["Long Hồ", "Vũng Liêm", "Mang Thít", "Tam Bình"],
    dac_tinh: "Đặc sản trứ danh cội nguồn cù lao Long Hồ - Vĩnh Long, cơm vàng hạt lép, rất mẫn cảm với nấm Phytophthora gây xì mủ thối trái.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Xì mủ thối gốc chảy nhựa (Phytophthora)",
        muc_do_nguy_hiem: "Cực kỳ nghiêm trọng (Tử vong cây)",
        loai: "Nấm",
        ten_khoa_hoc: "Phytophthora palmivora",
        trieu_chung: [
          "Cổ rễ và thân chính xì mủ nhớt ướt sũng màu đỏ nâu",
          "Bóc vỏ thấy gỗ bên trong chuyển sang màu hồng cá hồi đến nâu đen bầm dập",
          "Lá sầu riêng chuyển màu vàng úa, rụng hàng loạt để lại cành trơ trụi",
          "Trái sầu riêng bị thối đen từ đít trái lan rộng, có mùi hôi chua nồng nặc và mốc trắng bao phủ"
        ],
        phan_biet: "Khác với xì mủ do sâu đục thân (sâu đục thân có đùn mùn gỗ cưa ra ngoài)",
        kiem_tra: "Kiểm tra cổ rễ vào sáng sớm lúc sương đọng, tìm vị trí vỏ cây ẩm ướt rỉ mủ",
        canh_tac: "Quét vôi gốc cao 1m, không để cỏ dại và đất phủ kín cổ rễ (cần xới phơi cổ rễ), thoát nước triệt để",
        sinh_hoc: "Tiêm thân hoặc quét gốc bằng lân hai chiều sinh học Phosphonate (Agri-Fos 400), tưới gốc nấm Chaetomium và Trichoderma",
        khuyen_cao: "Khuyến cáo nhà vườn Vũng Liêm, Long Hồ chủ động đo độ mặn nguồn nước tưới < 0.5‰ để tránh sốc rễ mở đường cho nấm"
      }),
      createDisease({
        ten_benh: "Bệnh Đốm mắt cua (Rỉ sắt lá / Anthracnose)",
        muc_do_nguy_hiem: "Trung bình",
        loai: "Nấm",
        ten_khoa_hoc: "Colletotrichum gloeosporioides",
        trieu_chung: [
          "Đốm nhỏ màu vàng sáng, sau chuyển sang nâu xám có viền nâu đỏ đậm",
          "Hình dạng giống như mắt cua, ở giữa vết bệnh khô rách thủng",
          "Làm lá bị cháy bìa lá, rụng sớm khi cây đang nuôi trái non"
        ],
        phan_biet: "Khác với cháy lá do cháy nắng (cháy nắng ở đầu chóp lá hướng nắng gắt, đốm mắt cua rải rác phiến lá)",
        kiem_tra: "Soi vết bệnh có các quầng đồng tâm và tâm vết bệnh bị rách thủng",
        canh_tac: "Bón đủ phân hữu cơ hoai mục, kali hữu cơ và silic giúp vách tế bào lá dày cứng cáp",
        sinh_hoc: "Phun phòng luân phiên nấm đối kháng Bacillus subtilis hoặc dịch chiết rong biển"
      })
    ]
  },
  {
    name_vi: "Sầu Riêng Monthong (Dona)",
    scientific_name: "Durio zibethinus 'Monthong'",
    dia_ban: ["Vũng Liêm", "Trà Ôn", "Long Hồ"],
    dac_tinh: "Cơm dày màu vàng nhạt vị ngọt béo ngậy, tán cây vươn cao, dễ bị bệnh cháy lá chết ngọn Rhizoctonia trong mùa mưa bão.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Cháy lá chết ngọn (Rhizoctonia)",
        muc_do_nguy_hiem: "Nặng",
        loai: "Nấm",
        ten_khoa_hoc: "Rhizoctonia solani",
        trieu_chung: [
          "Lá non bị sũng nước như luộc nước sôi, dính bết lại với nhau bằng các mạng sợi nấm trắng bạc",
          "Vết cháy chuyển nhanh sang màu nâu sậm, lá khô dính tòng teng trên cành mà không rụng ngay",
          "Đọt non bị thối đen từ chóp ngọn thụt lùi xuống làm khô cành hàng loạt"
        ],
        phan_biet: "Khác với cháy lá Phytophthora (Phytophthora vết thâm đen nhanh hơn và không có mạng tơ nấm giăng liên kết các lá)",
        kiem_tra: "Kiểm tra các cụm lá non dính bết vào nhau vào sáng sớm ẩm ướt",
        canh_tac: "Tỉa thông thoáng cành la, cành vượt sát đất để giảm ẩm độ vi khí hậu trong tán",
        sinh_hoc: "Phun Validamycin sinh học hoặc nấm đối kháng Trichoderma viride"
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
        ten_benh: "Bệnh Thán thư hại bông và trái xoài",
        muc_do_nguy_hiem: "Nặng (Mất mùa 100% nếu dính mưa bông)",
        loai: "Nấm",
        ten_khoa_hoc: "Colletotrichum gloeosporioides",
        trieu_chung: [
          "Chùm bông xoài xuất hiện nhiều chấm đen nhỏ li ti, sau đó khô đen và rụng trơ cọng bông",
          "Lá non xuất hiện đốm tròn màu nâu đen viền vàng, sau rách thủng lỗ chỗ",
          "Vỏ quả xoài khi chín xuất hiện các đốm đen tròn lõm xuống, thịt quả bên dưới bị chua úng"
        ],
        phan_biet: "Khác với bọ trĩ hại bông xoài (bọ trĩ làm cọng bông khô cong queo, có phấn đen bài tiết)",
        kiem_tra: "Gõ nhẹ chùm bông lên tờ giấy trắng kiểm tra bọ trĩ kết hợp soi kính lúp vết nấm thán thư",
        canh_tac: "Rung bông rũ nước mưa ngay sau mỗi cơn mưa đêm, bao trái bằng túi giấy chuyên dụng khi trái bằng ngón chân cái",
        sinh_hoc: "Phun nấm đối kháng Chaetomium hoặc thuốc sinh học nguồn gốc thảo mộc Eugenol"
      })
    ]
  },
  {
    name_vi: "Xoài Cát Chu",
    scientific_name: "Mangifera indica 'Cat Chu'",
    dia_ban: ["Long Hồ", "Mang Thít", "Vũng Liêm"],
    dac_tinh: "Trái thon nhỏ, khi chín vỏ màu vàng ươm thơm dịu, dễ xử lý ra hoa nhưng hay bị bệnh đốm vi khuẩn xì mủ quả.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Đốm đen vi khuẩn (Xanthomonas)",
        muc_do_nguy_hiem: "Nặng",
        loai: "Vi khuẩn",
        ten_khoa_hoc: "Xanthomonas campestris pv. mangiferaeindicae",
        trieu_chung: [
          "Đốm đen hình sao hoặc góc cạnh nổi gồ lên trên mặt lá, rỉ dịch mủ nhớt",
          "Vỏ quả xuất hiện các vết nứt chân chim màu đen sũng nước, xì mủ dính nhớt",
          "Cành non bị loét đen và gãy ngang khi có gió mạnh"
        ],
        phan_biet: "Khác với thán thư: Đốm vi khuẩn có hình góc cạnh chân chim và chảy mủ nhớt có mùi tanh",
        kiem_tra: "Cắt mẩu mô bệnh ngâm vào ly nước thủy tinh xem có dòng dịch vi khuẩn đùn ra đục nước",
        canh_tac: "Cắt tỉa cành bệnh, khử trùng kéo bấm bằng cồn 70 độ",
        sinh_hoc: "Phun hợp chất Kasugamycin, đồng Nano sinh học hoặc dịch chiết tỏi kháng khuẩn"
      })
    ]
  },
  {
    name_vi: "Xoài Tượng",
    scientific_name: "Mangifera indica",
    dia_ban: ["Long Hồ", "Tam Bình", "Trà Ôn"],
    dac_tinh: "Trái to nặng 0.8 - 1.5kg, ăn giòn thơm khi còn sống, chịu hạn và đất sét pha tốt.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Phấn trắng hại xoài",
        muc_do_nguy_hiem: "Trung bình",
        loai: "Nấm",
        ten_khoa_hoc: "Oidium mangiferae",
        trieu_chung: [
          "Lớp phấn màu trắng xám bao phủ như bột mì trên cọng bông, cánh hoa và lá non",
          "Hoa bị biến dạng, không đậu trái được rồi khô rụng hàng loạt",
          "Trái non bị nứt nẻ da và biến dạng còi cọc"
        ],
        phan_biet: "Lớp phấn trắng lau bay bụi, xuất hiện mạnh khi thời tiết se lạnh có nhiều sương mù",
        kiem_tra: "Quan sát chùm hoa vào sáng sớm thấy màng phấn trắng phủ kín",
        canh_tac: "Tỉa cành tạo tán thông thoáng cho ánh nắng chiếu xuyên qua tán",
        sinh_hoc: "Phun lưu huỳnh vôi (thuốc lưu huỳnh sinh học) hoặc dung dịch baking soda pha loãng nồng độ 0.3%"
      })
    ]
  },
  {
    name_vi: "Nhãn Xuồng Cơm Vàng",
    scientific_name: "Dimocarpus longan 'Xuong Com Vang'",
    dia_ban: ["Long Hồ", "Vũng Liêm", "Trà Ôn"],
    dac_tinh: "Cơm nhãn dày giòn ngọt ráo nước màu vàng nhạt, chịu phèn nhẹ, mẫn cảm với bệnh chổi rồng.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Chổi rồng (Witches' Broom) hại nhãn",
        muc_do_nguy_hiem: "Cực kỳ nghiêm trọng",
        loai: "Virus / Phytoplasma liên kết",
        ten_khoa_hoc: "Longan witches' broom-associated virus",
        vector: "Nhện lông nhung (Eriophyes dimocarpi)",
        trieu_chung: [
          "Chồi non nhú ra bị xoăn tít, các lóng chồi ngắn cũn cỡn tụ lại thành chùm như cây chổi rơm",
          "Lá non teo nhỏ, khô queo rụng sớm",
          "Chùm hoa không nở được hoa cái, khô queo lại thành một khối bùi nhùi không đậu trái"
        ],
        phan_biet: "Rất dễ nhận biết qua hình dáng bó chổi rơm đặc thù của chồi và cọng hoa",
        kiem_tra: "Dùng kính lúp soi đọt non tìm nhện lông nhung màu trắng sữa li ti ẩn nấp trong lông tơ",
        canh_tac: "Cắt bỏ toàn bộ cành bị chổi rồng sâu vào phần gỗ lành 20-30cm, đem ra khỏi vườn đốt tiêu hủy triệt để",
        sinh_hoc: "Phun dầu khoáng SK Enspray kết hợp lưu huỳnh hữu cơ hoặc nấm đối kháng trừ nhện hại khi cây nhú lộc non",
        khuyen_cao: "Áp dụng nghiêm ngặt quy trình quản lý bệnh chổi rồng nhãn của Cục BVTV"
      })
    ]
  },
  {
    name_vi: "Nhãn Ido",
    scientific_name: "Dimocarpus longan 'Ido'",
    dia_ban: ["Long Hồ", "Mang Thít", "Tam Bình", "Trà Ôn"],
    dac_tinh: "Kháng bệnh chổi rồng tốt hơn nhãn tiêu da bò, năng suất cao, tỷ lệ đậu trái tốt trên đất vườn Vĩnh Long.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Sương mai / Thối hoa và trái nhãn (Phytophthora)",
        muc_do_nguy_hiem: "Nặng",
        loai: "Nấm",
        ten_khoa_hoc: "Phytophthora colocasiae / Phytophthora sp.",
        trieu_chung: [
          "Bông nhãn bị thâm đen sũng nước, hoa rụng hàng loạt sau mưa đêm",
          "Vỏ trái xuất hiện các đốm nâu tròn rồi lan rộng ra cả chùm quả",
          "Bên trong cơm nhãn bị úng nước, có mùi chua nồng và thối rữa"
        ],
        phan_biet: "Khác với nấm bồ hóng (bồ hóng không làm thối cơm quả, chỉ làm bẩn vỏ bên ngoài)",
        kiem_tra: "Quan sát chùm trái nhãn đang lớn sau đợt mưa rào liên tục",
        canh_tac: "Cắt tỉa các chùm hoa dị hình, neo giữ cành thông thoáng không chạm đất",
        sinh_hoc: "Phun chế phẩm sinh học Fosetyl-Aluminium hoặc nấm đối kháng Trichoderma"
      })
    ]
  },
  {
    name_vi: "Nhãn Tiêu Da Bò",
    scientific_name: "Dimocarpus longan",
    dia_ban: ["Long Hồ", "Mang Thít"],
    dac_tinh: "Vỏ mỏng màu vàng bò, cơm mọng nước, diện tích hiện nay giảm dần do dễ nhiễm chổi rồng.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Bồ hóng (Muội đen lá và trái nhãn)",
        muc_do_nguy_hiem: "Nhẹ",
        loai: "Nấm",
        ten_khoa_hoc: "Capnodium citri / Meliola sp.",
        trieu_chung: [
          "Lớp màng đen muội than phủ dày trên phiến lá và chùm quả nhãn",
          "Ngăn cản quá trình quang hợp của lá làm cây còi cọc",
          "Vỏ trái bị đen lem luốc, mất giá trị thẩm mỹ khi bán thị trường"
        ],
        phan_biet: "Lớp bồ hóng lấy khăn ướt lau là sạch bóng bề mặt da quả, không ăn thủng mô biểu bì",
        kiem_tra: "Tìm sự hiện diện của rệp sáp, rầy mềm tiết chất mật ngọt thu hút nấm bồ hóng",
        canh_tac: "Tiêu diệt tổ kiến đen bảo vệ rệp sáp, tỉa cành cho ánh nắng rọi sáng vào lòng tán",
        sinh_hoc: "Phun xịt xà phòng sinh học thảo mộc hoặc nấm ký sinh Lecanicillium lecanii diệt rệp sáp"
      })
    ]
  },
  {
    name_vi: "Chôm Chôm Java",
    scientific_name: "Nephelium lappaceum 'Java'",
    dia_ban: ["Long Hồ (Cù lao An Bình)", "Bình Minh"],
    dac_tinh: "Cây trồng đặc sản vùng du lịch sinh thái cù lao An Bình, râu dài đỏ tươi, thịt róc hạt ngọt thanh.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Phấn trắng hại chôm chôm (Oidium)",
        muc_do_nguy_hiem: "Nặng (Gây rụng bông và gai quả bị thối)",
        loai: "Nấm",
        ten_khoa_hoc: "Oidium nephelii",
        trieu_chung: [
          "Màng bột phấn màu trắng xám bao phủ lên chùm hoa, lộc non và gai trái non",
          "Râu gai của trái non bị teo tóp, chuyển màu đen cháy và rụng quả non hàng loạt",
          "Trái lớn bị chai cứng, da trái nứt nẻ và không chín đỏ được"
        ],
        phan_biet: "Khác với hiện tượng rụng trái do thiếu nước (trái rụng vẫn giữ gai mềm mại, không có màng phấn xám)",
        kiem_tra: "Kiểm tra gai của trái non kích thước hạt tiêu đến ngón tay",
        canh_tac: "Cắt tỉa ngọn cành vô hiệu sau vụ thu hoạch, vệ sinh dọn sạch rác dưới gốc",
        sinh_hoc: "Phun luân phiên lưu huỳnh hữu cơ sinh học (Sulfit) và chế phẩm Bacillus subtilis"
      })
    ]
  },
  {
    name_vi: "Chôm Chôm Nhãn",
    scientific_name: "Nephelium lappaceum",
    dia_ban: ["Long Hồ", "Mang Thít", "Vũng Liêm"],
    dac_tinh: "Trái nhỏ, râu gai ngắn, cơm dày khô giòn rất được ưa chuộng, nhạy cảm với bệnh thối quả Botryodiplodia.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Thối trái đốm đen (Botryodiplodia)",
        muc_do_nguy_hiem: "Nặng",
        loai: "Nấm",
        ten_khoa_hoc: "Lasiodiplodia theobromae (Botryodiplodia theobromae)",
        trieu_chung: [
          "Vết bệnh bắt đầu từ cuống trái hoặc chóp gai bị chuyển sang màu nâu sậm",
          "Vết thối lan nhanh bao trùm toàn bộ quả chôm chôm trong vòng 2-3 ngày",
          "Cơm bên trong bị nhũn nước, thối rữa và có lớp nấm xám đen mọc tua tủa"
        ],
        phan_biet: "Thối nhanh từ cuống và có bào tử nấm đen hạt nhỏ li ti trên vỏ",
        kiem_tra: "Kiểm tra chùm quả sắp chín trong điều kiện ẩm ướt sau mưa",
        canh_tac: "Tránh làm trầy xước vỏ quả khi thu hoạch, thu hái vào ngày nắng ráo",
        sinh_hoc: "Phun chế phẩm sinh học Chitosan hoặc dung dịch kháng khuẩn thảo mộc"
      })
    ]
  },
  {
    name_vi: "Măng Cụt Lục Sĩ Thành",
    scientific_name: "Garcinia mangostana",
    dia_ban: ["Trà Ôn (Xã Lục Sĩ Thành)", "Vũng Liêm", "Long Hồ"],
    dac_tinh: "Nữ hoàng trái cây nhiệt đới, sinh trưởng chậm nhưng tuổi thọ hàng chục năm, rất nhạy cảm với hiện tượng xì mủ sượng múi.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Xì mủ vàng sượng múi măng cụt",
        muc_do_nguy_hiem: "Nặng (Làm hỏng ruột múi)",
        loai: "Rối loạn sinh lý kết hợp Nấm",
        ten_khoa_hoc: "Rối loạn dòng nhựa tế bào do mưa sốc nước kết hợp bọ trĩ",
        trieu_chung: [
          "Vỏ ngoài trái măng cụt tiết ra những giọt mủ màu vàng tươi đặc quánh",
          "Bên trong múi thịt bị ngấm mủ vàng, thịt múi bị chai sượng sần sùi có vị đắng ngắt",
          "Lá măng cụt bị cháy chóp và nứt nẻ cuống trái non"
        ],
        phan_biet: "Mủ màu vàng tươi đặc trưng của măng cụt, không lẫn với nấm mốc đen thông thường",
        kiem_tra: "Bổ thử trái ngẫu nhiên trong vườn sau những đợt mưa dầm chuyển mùa",
        canh_tac: "Giữ mực nước mương ổn định chênh lệch không quá 20cm, bón Canxi-Bo và Kali Clorua hạn chế thừa đạm",
        sinh_hoc: "Phun bổ sung vi lượng Canxi hữu cơ hòa tan kết hợp che phủ bạt gốc điều tiết ẩm độ đất"
      })
    ]
  },
  {
    name_vi: "Mít Thái Siêu Sớm (Mít Changai)",
    scientific_name: "Artocarpus heterophyllus",
    dia_ban: ["Bình Tân", "Tam Bình", "Trà Ôn", "Vũng Liêm", "Long Hồ"],
    dac_tinh: "Cho trái cực nhanh sau 14-18 tháng, múi giòn ngọt ráo, cực kỳ mẫn cảm với bệnh xơ đen do vi khuẩn.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Xơ đen mít Thái (Bacterial Black Flesh)",
        muc_do_nguy_hiem: "Cực kỳ nghiêm trọng (Thương lái loại 100%)",
        loai: "Vi khuẩn",
        ten_khoa_hoc: "Pantoea stewartii subsp. stewartii",
        trieu_chung: [
          "Bên ngoài quả mít méo mó, eo thắt, gai không đều, có đốm nâu sẫm ở khe rãnh gai",
          "Bổ quả ra thấy xơ mít chuyển sang màu đen kịt, cùi mít đen thui",
          "Múi mít bị teo lép, chai cứng hoặc thâm sì không ăn được"
        ],
        phan_biet: "Khác với xơ đỏ sinh lý (xơ đỏ không có mùi tanh, múi vẫn ngọt, xơ đen múi bị chua chai và thâm đen)",
        kiem_tra: "Bổ kiểm tra quả non méo eo bị nghi ngờ khi thụ phấn gặp mưa",
        canh_tac: "Tỉa bỏ bớt quả xấu, thụ phấn bổ sung vào sáng sớm ngày nắng, bao trái bằng bao lưới chuyên dụng",
        sinh_hoc: "Phun Kasugamycin hoặc đồng vi sinh định kỳ lúc hoa cái vừa nhú lộc đến khi thụ phấn xong",
        khuyen_cao: "Khuyến cáo nông dân Bình Tân và Tam Bình không lấy giống từ các cây mẹ đã có tiền sử nhiễm xơ đen nặng"
      })
    ]
  },
  {
    name_vi: "Mít Ruột Đỏ Indo",
    scientific_name: "Artocarpus heterophyllus 'Red'",
    dia_ban: ["Bình Tân", "Vũng Liêm", "Tam Bình"],
    dac_tinh: "Múi màu cam đỏ bắt mắt vị ngọt đậm thơm mùi chuối, giá trị xuất khẩu cao, dễ bị thối nhũn trái mùa mưa.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Thối nhũn trái mít (Rhizopus Fruit Rot)",
        muc_do_nguy_hiem: "Nặng",
        loai: "Nấm",
        ten_khoa_hoc: "Rhizopus artocarpi (Rhizopus stolonifer)",
        trieu_chung: [
          "Vết bệnh bắt đầu từ cuống hoặc rãnh gai mít bị sũng nước thâm đen",
          "Mô thịt quả nhũn nát nhanh chóng, chảy nước nhờn có mùi men chua",
          "Lớp nấm mốc đen xù xì như râu mọc bao phủ toàn bộ vùng thối rữa"
        ],
        phan_biet: "Đặc điểm sợi nấm màu trắng đầu có hạt đính bào tử đen tròn xù xì của nấm mốc chân chim Rhizopus",
        kiem_tra: "Quan sát các trái mít treo thấp gần mặt nước mương vườn",
        canh_tac: "Treo trái cao tối thiểu 0.8m so với mặt đất liếp, cắt tỉa cành thông thoáng",
        sinh_hoc: "Phun nấm đối kháng Trichoderma phối hợp vôi bột hòa nước tưới gốc"
      })
    ]
  },
  {
    name_vi: "Ổi Nữ Hoàng",
    scientific_name: "Psidium guajava 'Queen'",
    dia_ban: ["Bình Minh", "Tam Bình", "Long Hồ"],
    dac_tinh: "Trái giòn ngọt ít hạt, năng suất liên tục quanh năm, thường xuyên chịu áp lực ruồi đục trái và nấm thán thư đốm mắt chim.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Đốm mắt chim (Anthracnose / Pestalotiopsis)",
        muc_do_nguy_hiem: "Trung bình",
        loai: "Nấm",
        ten_khoa_hoc: "Pestalotiopsis psidii / Colletotrichum gloeosporioides",
        trieu_chung: [
          "Các nốt tròn màu nâu nhỏ có viền nâu đỏ, ở giữa lõm xuống màu xám tro",
          "Vết bệnh trên vỏ ổi nhìn giống như mắt chim tròn xoe",
          "Trái bị sần sùi chai vỏ, thịt quả bên dưới bị chua khô sượng"
        ],
        phan_biet: "Khác với ghẻ loét (ghẻ loét sùi mô bần ráp tay hơn, đốm mắt chim có viền màu hạt dẻ rõ ràng)",
        kiem_tra: "Kiểm tra vỏ quả ổi khi trái bằng ngón chân cái chuẩn bị bao bọc",
        canh_tac: "Bao trái sớm bằng xốp lưới bọc nilong đục lỗ đáy thoát nước",
        sinh_hoc: "Phun phòng nấm Trichoderma hoặc nano bạc đồng sinh học trước khi bao quả"
      })
    ]
  },
  {
    name_vi: "Ổi Ruột Hồng (Ổi Ruby)",
    scientific_name: "Psidium guajava 'Ruby'",
    dia_ban: ["Bình Minh", "Trà Ôn", "Vũng Liêm"],
    dac_tinh: "Ruột màu đỏ hồng thơm đậm ngọt thanh, thích hợp đất thịt phù sa nhẹ, dễ nhiễm tuyến trùng sưng rễ.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Nốt sưng tuyến trùng rễ ổi (Root-knot Nematode)",
        muc_do_nguy_hiem: "Nặng",
        loai: "Tuyến trùng",
        ten_khoa_hoc: "Meloidogyne incognita",
        trieu_chung: [
          "Rễ tơ và rễ cọc nổi nhiều u sần hình hạt chuỗi tròn méo mó",
          "Cây sinh trưởng còi cọc, mép lá bị vàng ửng đỏ tía như thiếu lân",
          "Cây dễ rụng lá và héo rũ vào buổi trưa nắng dù đất mương vẫn có nước"
        ],
        phan_biet: "Rễ có các hạt u nốt tròn sưng to dị hình không phải nốt sần vi khuẩn cố định đạm",
        kiem_tra: "Nhổ nhẹ cây con hoặc cào lớp đất mặt kiểm tra rễ non",
        canh_tac: "Luân canh hoặc trồng xen hoa cúc vạn thọ (Tagetes erecta) để tiết rễ xua đuổi tuyến trùng",
        sinh_hoc: "Tưới chế phẩm nấm ký sinh trứng tuyến trùng Paecilomyces lilacinus kết hợp tinh chất Chitosan"
      })
    ]
  },
  {
    name_vi: "Mận An Phước",
    scientific_name: "Syzygium samarangense",
    dia_ban: ["Bình Minh", "Tam Bình", "Long Hồ"],
    dac_tinh: "Trái hình quả chuông màu đỏ sẫm ngọt mọng nước, sản lượng rất cao, mẫn cảm với sâu đục trái và nấm thối nhũn bồ hóng.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Thối nhũn quả mận mùa mưa (Phomopsis / Colletotrichum)",
        muc_do_nguy_hiem: "Nặng",
        loai: "Nấm",
        ten_khoa_hoc: "Phomopsis sp. & Colletotrichum gloeosporioides",
        trieu_chung: [
          "Đít quả mận xuất hiện đốm nâu ướt sũng lan nhanh",
          "Thịt quả bị nhũn nước, rụng tả tơi khắp mặt đất dưới gốc cây",
          "Trái sau thu hoạch 1-2 ngày bị lên men chua thối rữa nứt vỏ"
        ],
        phan_biet: "Khác với dòi đục trái (dòi đục có lỗ châm kim nhỏ và có ấu trùng dòi bò bên trong)",
        kiem_tra: "Bóp nhẹ phần rốn đít quả mận kiểm tra độ mềm nhũn",
        canh_tac: "Trùm lưới cước toàn bộ tán cây hoặc bao chùm từng chùm quả mận",
        sinh_hoc: "Phun chế phẩm sinh học vi sinh Bacillus subtilis và quét dọn tiêu hủy trái rụng"
      })
    ]
  },
  {
    name_vi: "Vú Sữa Lò Rèn",
    scientific_name: "Chrysophyllum cainito",
    dia_ban: ["Vũng Liêm", "Mang Thít", "Long Hồ"],
    dac_tinh: "Trái tròn da bóng láng, dòng sữa trắng ngọt ngào hương vani, cây cổ thụ rễ ăn sâu nhưng dễ nhiễm thán thư khô hoa.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Thán thư đốm mắt cua quả vú sữa",
        muc_do_nguy_hiem: "Trung bình",
        loai: "Nấm",
        ten_khoa_hoc: "Colletotrichum gloeosporioides",
        trieu_chung: [
          "Trên vỏ trái vú sữa xuất hiện đốm tròn màu nâu lõm nhẹ vào thịt",
          "Trái non bị teo nhỏ và rụng sớm",
          "Trái chín bị thâm đen một bên má, thịt quả bị chai cứng và giảm vị ngọt béo"
        ],
        phan_biet: "Khác với vết rám nắng (vết thán thư có vòng đồng tâm và viền đen sẫm)",
        kiem_tra: "Kiểm tra chùm trái khi vỏ chuyển từ màu xanh sang ửng tía",
        canh_tac: "Bao trái bằng túi giấy bọc chuyên dụng khi quả to bằng quả chanh",
        sinh_hoc: "Phun phòng dung dịch tỏi ớt gừng sinh học hoặc nấm Chaetomium"
      })
    ]
  },
  {
    name_vi: "Vú Sữa Hoàng Kim (Abiu)",
    scientific_name: "Pouteria caimito",
    dia_ban: ["Long Hồ", "Tam Bình", "Trà Ôn"],
    dac_tinh: "Vỏ vàng ươm óng ả, thịt trong suốt thạch dẻo ngọt ngào, cây ưa đất ẩm giàu mùn ven sông.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Đốm đen thối chóp trái Hoàng Kim",
        muc_do_nguy_hiem: "Nặng",
        loai: "Nấm",
        ten_khoa_hoc: "Lasiodiplodia theobromae",
        trieu_chung: [
          "Chóp nhọn của đuôi trái bị thâm đen khô sần",
          "Vết thâm lan rộng làm vỏ quả màu vàng tươi bị lem luốc loang lổ",
          "Phần thịt thạch bên trong bị sượng cứng và chuyển màu nâu đục"
        ],
        phan_biet: "Đốm tập trung ở phần chóp nhọn phía đáy quả do đọng giọt sương và nước mưa",
        kiem_tra: "Kiểm tra chóp đáy quả lúc sáng sớm sương đọng",
        canh_tac: "Bao quả bằng bao màng thoát hơi nước không để ứ đọng giọt nước đáy",
        sinh_hoc: "Phun phòng bằng nấm Trichoderma hoặc chế phẩm đồng sinh học định kỳ"
      })
    ]
  },
  {
    name_vi: "Thanh Long Ruột Đỏ",
    scientific_name: "Hylocereus costaricensis",
    dia_ban: ["Bình Tân", "Trà Ôn", "Tam Bình"],
    dac_tinh: "Cây thuộc họ xương rồng chịu hạn giỏi nhưng cực kỳ mẫn cảm với bệnh đốm nâu đốm trắng đốm tắc kè vào mùa mưa.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Đốm nâu (Bệnh đốm trắng / Bệnh Tắc kè)",
        muc_do_nguy_hiem: "Cực kỳ nghiêm trọng",
        loai: "Nấm",
        ten_khoa_hoc: "Neoscytalidium dimidiatum",
        trieu_chung: [
          "Ban đầu là các vết chấm tròn nhỏ màu trắng hơi lõm trên cành và vỏ quả",
          "Vết bệnh phát triển sần sùi nhô lên màu nâu đỏ như da con tắc kè bông",
          "Nhiều vết liên kết làm thối nát cành thanh long, trái bị sần sùi sẹo mụn chai sượng"
        ],
        phan_biet: "Hình dạng nốt sần tắc kè gồ ghề rất đặc thù không nhầm lẫn",
        kiem_tra: "Quan sát các tai cành non và tai quả thanh long",
        canh_tac: "Cắt bỏ tiêu hủy cành bệnh triệt để bằng cách chôn sâu rắc vôi bột (tuyệt đối không vứt xuống mương vườn)",
        sinh_hoc: "Phun nấm đối kháng Chaetomium kết hợp chế phẩm nano bạc đồng",
        khuyen_cao: "Thực hiện theo chỉ đạo của Chi cục BVTV Vĩnh Long về phòng chống dịch bệnh đốm nâu tắc kè"
      })
    ]
  },
  {
    name_vi: "Thanh Long Ruột Trắng",
    scientific_name: "Hylocereus undatus",
    dia_ban: ["Bình Tân", "Trà Ôn"],
    dac_tinh: "Thịt màu trắng giòn vị chua ngọt nhẹ nhàng, cành dài bò trên trụ xi măng, dễ bị bệnh thối cành do vi khuẩn mềm nhũn.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Thối mềm cành thanh long (Bacterial Soft Rot)",
        muc_do_nguy_hiem: "Nặng",
        loai: "Vi khuẩn",
        ten_khoa_hoc: "Pectobacterium carotovorum (Erwinia carotovora)",
        trieu_chung: [
          "Mô thịt cành thanh long bị ủng nước, nhũn nát có mùi hôi thối khó chịu",
          "Thịt cành tan rữa trơ lại lõi trụ gỗ trắng bên trong",
          "Bệnh lây lan rất nhanh theo dòng nước mưa tưới trên cành"
        ],
        phan_biet: "Khác với nấm tắc kè: Thối mềm vi khuẩn bốc mùi thối chua nồng nặc và thịt cành nhũn chảy nước nhờn",
        kiem_tra: "Bóp ngón tay thấy thịt cành mềm bấy chảy nước dịch đục",
        canh_tac: "Dùng dao khử trùng gọt sạch phần thịt nhũn đến tận lõi gỗ, bôi vôi đặc pha phèn xanh",
        sinh_hoc: "Phun dung dịch Kasugamycin hoặc đồng oxyclorua phòng ngừa lây lan"
      })
    ]
  },
  {
    name_vi: "Đu Đủ Ruột Vàng / Đài Loan",
    scientific_name: "Carica papaya",
    dia_ban: ["Bình Tân", "Long Hồ", "Tam Bình"],
    dac_tinh: "Cây thân thảo hóa gỗ nhanh cho thu hoạch, mẫn cảm với virus đốm vòng PRSV lây truyền qua rệp muội.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Đốm vòng virus đu đủ (Papaya Ringspot Virus - PRSV)",
        muc_do_nguy_hiem: "Cực kỳ nghiêm trọng (Hủy diệt vườn)",
        loai: "Virus",
        ten_khoa_hoc: "Papaya ringspot virus (PRSV)",
        vector: "Rệp muội (Aphis gossypii, Myzus persicae)",
        trieu_chung: [
          "Lá non bị khảm vàng loang lổ, biến dạng co rúm chỉ còn lại gân lá như bàn tay ếch",
          "Cuống lá và thân cây xuất hiện các sọc vệt ngậm nước màu xanh đậm dầu loang",
          "Vỏ quả đu đủ nổi các vòng tròn đồng tâm như mắt kính, quả sượng đắng sần sùi"
        ],
        phan_biet: "Vòng tròn đồng tâm trên vỏ quả và lá co quắp bàn tay ếch là dấu hiệu độc quyền của PRSV",
        kiem_tra: "Kiểm tra mặt dưới lá tìm rệp muội đen và rầy mềm",
        canh_tac: "Chặt nhổ đốt tiêu hủy ngay lập tức cây chớm bệnh, không chiết ghép từ cây nghi ngờ",
        sinh_hoc: "Phun dầu khoáng sinh học ngăn cản rệp chích hút truyền virus",
        khuyen_cao: "Luân canh với bắp hoặc các cây trồng không cùng họ để cắt nguồn virus trong đất"
      })
    ]
  },
  {
    name_vi: "Dừa Xiêm Xanh",
    scientific_name: "Cocos nucifera 'Xiêm Xanh'",
    dia_ban: ["Vũng Liêm", "Trà Ôn", "Mang Thít", "Long Hồ", "Tam Bình"],
    dac_tinh: "Cây trồng quen thuộc bờ kênh mương Vĩnh Long, nước ngọt thanh mát, chịu mặn khá nhưng dễ bị bọ cánh cứng cắn đọt non.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Thối đọt dừa non (Phytophthora)",
        muc_do_nguy_hiem: "Cực kỳ nghiêm trọng (Gây chết cây dừa)",
        loai: "Nấm",
        ten_khoa_hoc: "Phytophthora palmivora",
        trieu_chung: [
          "Lá bẹ đọt chính ở giữa ngọn dừa bị vàng héo rồi gục gãy ngang",
          "Củ hũ non bên trong đọt bị thối rữa nhũn nát bốc mùi hôi thối thối mục",
          "Rút nhẹ bẹ đọt non tuột ra dễ dàng, cây chết hoàn toàn điểm sinh trưởng"
        ],
        phan_biet: "Khác với bọ dừa (bọ dừa cắn lá non tạo các vệt sọc cháy khô chứ không làm thối củ hũ)",
        kiem_tra: "Trèo kiểm tra đỉnh sinh trưởng nơi cổ bẹ đọt non vào đầu mùa mưa",
        canh_tac: "Vệ sinh dọn sạch rác bẹ dừa khô quanh cổ hũ định kỳ",
        sinh_hoc: "Bỏ muối hột trộn bột lưu huỳnh hoặc gói chế phẩm Trichoderma vào kẽ bẹ dừa trên ngọn"
      })
    ]
  },
  {
    name_vi: "Dừa Mã Lai (Dừa Dứa)",
    scientific_name: "Cocos nucifera 'Malay'",
    dia_ban: ["Trà Ôn", "Vũng Liêm", "Long Hồ"],
    dac_tinh: "Thân lùn mau cho trái, buồng quả sai trĩu hạt, chịu mặn tốt, dễ bị nấm đốm lá Pestalotia hại tàu dừa.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Đốm xám cháy lá dừa (Pestalotiopsis)",
        muc_do_nguy_hiem: "Trung bình",
        loai: "Nấm",
        ten_khoa_hoc: "Pestalotiopsis palmarum",
        trieu_chung: [
          "Các đốm hình bầu dục màu nâu vàng xuất hiện trên các chét lá dừa già",
          "Tâm vết đốm chuyển sang màu xám tro viền nâu đậm có hạt đen nhỏ",
          "Các đốm liên kết làm cả tàu dừa bị cháy xém khô giòn rũ xuống thân"
        ],
        phan_biet: "Khác với tàu dừa già rụng tự nhiên (cháy lá nấm có các đốm xám tro viền đậm rõ rệt)",
        kiem_tra: "Quan sát các tàu lá dừa phía dưới sát gốc",
        canh_tac: "Rọc bỏ các tàu dừa khô sâu bệnh đem tiêu hủy, bón bổ sung phân Kali và phân chuồng hoai",
        sinh_hoc: "Phun chế phẩm sinh học gốc đồng nano hoặc nấm đối kháng Chaetomium"
      })
    ]
  },
  {
    name_vi: "Dừa Sáp Cầu Kè / Trà Ôn",
    scientific_name: "Cocos nucifera 'Makapuno'",
    dia_ban: ["Trà Ôn", "Vũng Liêm"],
    dac_tinh: "Đặc sản quý hiếm cơm dừa dày đặc dẻo sánh như kem béo ngậy, giá trị kinh tế cao kỷ lục.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Rụng trái non dừa sáp (Button Shedding)",
        muc_do_nguy_hiem: "Nặng",
        loai: "Nấm kết hợp Rối loạn dinh dưỡng",
        ten_khoa_hoc: "Colletotrichum gloeosporioides / Fusarium sp.",
        trieu_chung: [
          "Trái dừa non kích thước bằng quả trứng gà bị nứt cuống đài",
          "Vùng quanh cuống đài có đốm nâu đen sũng nước",
          "Trái dừa non rụng la liệt dưới mương dù buồng dừa thụ phấn rất nhiều hoa"
        ],
        phan_biet: "Rụng do nấm có vết đốm đen quanh cuống đài, rụng sinh lý cuống vẫn tươi nguyên",
        kiem_tra: "Kiểm tra vết gắn kết giữa đài hoa và cuống trái non",
        canh_tac: "Tưới tiêu giữ ẩm đều đặn không để khô hạn kéo dài rồi gặp mưa lớn đột ngột, bón cân đối Bo - Kẽm",
        sinh_hoc: "Phun nấm đối kháng Bacillus subtilis hoặc dịch chiết rong biển bồi bổ cuống trái"
      })
    ]
  },
  {
    name_vi: "Chuối Già Nam Mỹ (Cavendish)",
    scientific_name: "Musa acuminata 'Cavendish'",
    dia_ban: ["Bình Tân", "Trà Ôn", "Tam Bình", "Long Hồ"],
    dac_tinh: "Trồng thâm canh quy mô lớn phục vụ xuất khẩu, năng suất buồng rất cao nhưng là đối tượng số 1 của bệnh héo Panama nguy hiểm.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Héo rũ Panama (Bệnh vàng lá chuối)",
        muc_do_nguy_hiem: "Cực kỳ nghiêm trọng (Hủy diệt vĩnh viễn đất trồng)",
        loai: "Nấm",
        ten_khoa_hoc: "Fusarium oxysporum f. sp. cubense (Foc Tropical Race 4 - TR4)",
        trieu_chung: [
          "Lá chuối già ngả vàng từ bìa lá vào trong gân chính, sau đó héo úa gãy gục ở cuống lá bám tòng teng quanh thân giả",
          "Cắt ngang thân giả thấy các mạch dẫn truyền chuyển màu nâu đỏ hoặc đen bầm bốc mùi ẩm mốc",
          "Củ chuối bị thối nâu đen từ ngoài vào trong mạch dẫn, cây chết khô đứng"
        ],
        phan_biet: "Mạch dẫn thân giả chuyển nâu đỏ rõ ràng; khác với rầy mềm làm chùn đọt (Bunchy Top)",
        kiem_tra: "Dùng dao cắt ngang thân giả cách mặt đất 30cm kiểm tra vòng mạch dẫn truyền",
        canh_tac: "Đào khử trùng tiêu hủy cả bụi chuối bằng vôi bột, cách ly nguồn nước mương, không dùng đất này trồng chuối lại",
        sinh_hoc: "Bón lót lượng lớn nấm đối kháng Trichoderma kết hợp vi khuẩn đối kháng Pseudomonas putida",
        khuyen_cao: "Báo cáo ngay cho cơ quan BVTV địa phương khi phát hiện dấu hiệu nghi ngờ TR4"
      })
    ]
  },
  {
    name_vi: "Chuối Xiêm (Chuối Sứ)",
    scientific_name: "Musa balbisiana",
    dia_ban: ["Mang Thít", "Long Hồ", "Tam Bình", "Vũng Liêm"],
    dac_tinh: "Cây chuối dân dã bờ ao ruộng vườn, bắp chuối trái chuối đều dùng ẩm thực phong phú, rất dễ bị bệnh khảm lá chùn đọt.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Chùn đọt chuối (Bunchy Top Virus - BBTV)",
        muc_do_nguy_hiem: "Cực kỳ nghiêm trọng",
        loai: "Virus",
        ten_khoa_hoc: "Banana bunchy top virus (BBTV)",
        vector: "Rệp muỗi đen hại chuối (Pentalonia nigronervosa)",
        trieu_chung: [
          "Lá chuối mới ra bị ngắn ngủn, dựng đứng xếp xít vào nhau như hình quạt ở ngọn thân",
          "Mép lá non bị cong uốn lượn, gân lá có các sọc đứt quãng màu xanh đậm hình chữ J hoặc dấu chấm",
          "Cây lùn tịt không trổ buồng được hoặc trổ bắp chuối dị hình nghẹn đọt"
        ],
        phan_biet: "Đọt chuối chùn lại bó quạt rất đặc thù của virus BBTV",
        kiem_tra: "Soi nách các bẹ lá chuối tìm cụm rệp muội màu nâu đen bám dày đặc",
        canh_tac: "Đào bỏ tiêu hủy cả bụi chuối nhiễm bệnh, không tách chuối con từ bụi mẹ nhiễm bệnh",
        sinh_hoc: "Phun xà phòng sinh học thảo dược trừ rệp muội đen trung gian truyền bệnh"
      })
    ]
  },
  {
    name_vi: "Sapôchê (Hồng Xiêm Mặc Bắc)",
    scientific_name: "Manilkara zapota",
    dia_ban: ["Mang Thít", "Tam Bình", "Vũng Liêm"],
    dac_tinh: "Cây gỗ bền bỉ chịu mặn và ngập khá tốt, trái thơm mùi đường mật caramen, dễ bị nấm đốm mắt chim trên lá.",
    benh: [
      createDisease({
        ten_benh: "Bệnh Đốm lá Sapôchê (Phaeophleospora)",
        muc_do_nguy_hiem: "Trung bình",
        loai: "Nấm",
        ten_khoa_hoc: "Phaeophleospora indica",
        trieu_chung: [
          "Những đốm tròn nhỏ li ti màu nâu đỏ xuất hiện trên mặt lá già",
          "Tâm vết bệnh biến thành màu xám bạc, lá bị khô giòn từng mảng rồi rụng sớm",
          "Cây thưa lá làm giảm khả năng quang hợp nuôi trái chín"
        ],
        phan_biet: "Đốm nhỏ li ti tập trung nhiều ở tầng lá già bên dưới tán",
        kiem_tra: "Quan sát mặt trên của phiến lá sapôchê",
        canh_tac: "Quét dọn lá rụng quanh gốc, bón phân hữu cơ hoai mục",
        sinh_hoc: "Phun thuốc gốc đồng sinh học hoặc dịch nấm đối kháng Chaetomium định kỳ"
      })
    ]
  }
];

// Helper to expand list to 105 crops with rigorous agricultural pathology details
const cropsMasterList = [];

// Push 35 Fruit Crops
cayAnTrai.forEach((c, idx) => {
  cropsMasterList.push({
    id: `crop_${String(idx + 1).padStart(3, '0')}`,
    topic: "Cay_An_Trai_Dac_San",
    name_vi: c.name_vi,
    scientific_name: c.scientific_name,
    dia_ban_pho_bien: c.dia_ban,
    dac_tinh_sinh_thai: c.dac_tinh,
    danh_sach_benh: c.benh
  });
});

console.log(`Loaded ${cropsMasterList.length} Fruit crops.`);

// Now build remaining groups:
// 2. CÂY LƯƠNG THỰC & HOA MÀU (20 cây: 36 -> 55)
// 3. RAU ĂN LÁ & ĂN QUẢ (35 cây: 56 -> 90)
// 4. CÂY CÔNG NGHIỆP & DƯỢC LIỆU (15 cây: 91 -> 105)

// Let's write the second module generator script that synthesizes all remaining crops
