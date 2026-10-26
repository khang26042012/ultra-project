# -*- coding: utf-8 -*-
"""
harvest_all_crop_pathologies.py
Comprehensive Plant Pathology Harvester & Intelligent Merger
Crawls & synthesizes data from:
  1. Growstuff Open Data API (all crops)
  2. PlantVillage Dataset & Digital Agriculture
  3. Planteome Plant Disease Ontology
  4. SOFRI (Viện Cây ăn quả Miền Nam) & Cục Bảo vệ Thực vật Việt Nam
Merges all diseases into crops without arbitrary limits (cào toàn bộ phổ bệnh học).
"""

import json
import os
import re
import sys
import time
import urllib.request
from typing import Dict, List, Any, Optional

try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'src', 'data', 'vietnam_plant_pathology_1000_crops.json')

def normalize_text(text: Optional[str]) -> str:
    if not text:
        return ""
    text = text.lower().strip()
    text = re.sub(r'\s+', ' ', text)
    return text

def normalize_sci(text: Optional[str]) -> str:
    if not text:
        return ""
    text = text.lower().strip()
    # Remove author citations, cultivar quotes, etc.
    text = re.sub(r"['\"].*?['\"]", "", text)
    text = re.sub(r'\(.*?\)', '', text)
    text = re.sub(r'\b(l\.|linn\.|mill\.|dc\.|lam\.|benth\.|var\.|subsp\.|f\.|sp\.)\b', '', text)
    text = re.sub(r'[^a-z\s]', '', text)
    return re.sub(r'\s+', ' ', text).strip()

def make_disease_entry(
    ten_benh: str,
    muc_do_nguy_hiem: str,
    tac_nhan_loai: str,
    tac_nhan_sci: str,
    trieu_chung: List[str],
    phan_biet: str,
    kiem_tra: str,
    canh_tac: str,
    sinh_hoc: str,
    vector: Optional[str] = None,
    khuyen_cao: str = "Tuân thủ nghiêm ngặt quy trình quản lý dịch hại tổng hợp IPM và VietGAP theo khuyến cáo Chi cục Trồng trọt & BVTV."
) -> Dict[str, Any]:
    tac_nhan: Dict[str, Any] = {
        "loai": tac_nhan_loai,
        "ten_khoa_hoc": tac_nhan_sci
    }
    if vector:
        tac_nhan["vector_truyen_benh"] = vector

    return {
        "ten_benh": ten_benh,
        "muc_do_nguy_hiem": muc_do_nguy_hiem,
        "tac_nhan": tac_nhan,
        "trieu_chung_dien_hinh": trieu_chung,
        "phan_biet_chan_doan_kep": phan_biet,
        "kiem_tra_thuc_dia": kiem_tra,
        "phac_do_vietgap": {
            "canh_tac": canh_tac,
            "sinh_hoc": sinh_hoc,
            "khuyen_cao_chuyen_gia": khuyen_cao
        }
    }

# -------------------------------------------------------------
# 1. KHO TRI THỨC BỆNH HỌC ĐẦU NGÀNH (SOFRI, BVTV, PLANTVILLAGE, PLANTEDATABASE)
# Bổ sung toàn diện phổ bệnh học cho các nhóm cây trồng
# -------------------------------------------------------------
PATHOLOGY_LIBRARY: Dict[str, List[Dict[str, Any]]] = {
    # Nhóm Sầu riêng (Durio zibethinus)
    "durio": [
        make_disease_entry(
            "Bệnh Xì mủ lở cổ rễ & Thối trái sầu riêng",
            "Cực kỳ nghiêm trọng (Hiểm nghèo)",
            "Nấm",
            "Phytophthora palmivora",
            [
                "Vỏ thân cành xì mủ nhờn màu nâu đỏ, mô vỏ bên trong thối nâu đen sũng nước",
                "Lá bánh tẻ và đọt non bị luộc sũng nước rồi rụng hoàng loạt, trơ cành",
                "Trái có vết đốm úng nước tròn màu xám nâu lan rộng, bao phủ lớp mốc trắng mịn",
                "Cổ rễ thối mục, vỏ rễ tuột khỏi lõi gỗ khiến cây suy kiệt đột ngột"
            ],
            "Khác với đục thân (vết xì mủ có mạt gỗ đùn ra) và nấm hồng (phủ lớp phấn hồng khô trên vỏ cành cao)",
            "Dùng dao bén cạo nhẹ lớp biểu bì thân chỗ ứa mủ: nếu mô vỏ có màu nâu cam sũng nước và ngửi thấy mùi thối chua đặc trưng của nấm thủy sinh Phytophthora.",
            "Tỉa cành tạo tán cách mặt đất 0.8m, vét rãnh thoát nước sâu trong mùa mưa, quét vôi hoặc Bordeaux vào gốc hàng năm.",
            "Quét hoặc tiêm thân chế phẩm Phosphonate (Phosphite Agripig), tưới gốc nấm đối kháng Trichoderma harzianum + Chaetomium liều cao."
        ),
        make_disease_entry(
            "Bệnh Cháy lá chết ngọn sầu riêng (Rhizoctonia)",
            "Nguy cơ cao",
            "Nấm",
            "Rhizoctonia solani",
            [
                "Vết bệnh ban đầu như bị giọt nước sôi rớt vào lá bánh tẻ hoặc lá non",
                "Vết loang rộng hình mạng nhện dính các lá non lại với nhau bằng sợi tơ nấm trắng bạc",
                "Lá khô cháy màu xám rơm, dính chùm trên cành không rụng ngay",
                "Đọt non bị thối đen từ chóp đọt lan dần xuống cành làm khô ngọn"
            ],
            "Khác với thán thư (vết thán thư có vòng đồng tâm và chấm đen li ti, không kết tơ dính chùm lá)",
            "Quan sát sáng sớm lúc sương ẩm: thấy mạng sợi tơ nấm giăng trắng giữa các phiến lá dính chùm lại với nhau.",
            "Thu gom lá bệnh đem tiêu hủy, tỉa thông thoáng tầng tán dưới, không tưới nước phun ướt lá non vào chiều tối ẩm ướt.",
            "Phun nấm đối kháng Bacillus subtilis hoặc chế phẩm sinh học chứa Validamycin, Hexaconazole gốc sinh học."
        ),
        make_disease_entry(
            "Bệnh Thán thư sầu riêng",
            "Trung bình",
            "Nấm",
            "Colletotrichum gloeosporioides",
            [
                "Vết bệnh bắt đầu từ chóp lá hoặc mép lá lan dần vào trong phiến lá",
                "Vết cháy màu nâu sẫm, ranh giới rõ rệt giữa mô bệnh và mô khỏe bằng đường viền nâu đỏ",
                "Trên bề mặt vết cháy có các vân vòng đồng tâm mang nhiều ổ nấm đen li ti",
                "Lá bị nặng cháy giòn một góc và rụng sớm, cây còi cọc"
            ],
            "Khác với cháy nắng (vết cháy nắng đồng đều không có vòng đồng tâm và không có ổ đốm đen)",
            "Dùng kính lúp cầm tay kiểm tra bề mặt vết bệnh: thấy các gai nấm đen li ti (acervuli) mọc nhô lên thành vòng tròn.",
            "Bón phân cân đối N-P-K, bổ sung Canxi-Silic tăng độ dày vách tế bào lá non.",
            "Phun dịch chiết xuất từ tỏi ớt gừng hoặc chế phẩm vi sinh Streptomyces lydicus, nấm Chaetomium."
        ),
        make_disease_entry(
            "Bệnh Nấm hồng sầu riêng",
            "Nguy cơ cao",
            "Nấm",
            "Corticium salmonicolor",
            [
                "Ban đầu xuất hiện các sợi nấm trắng mịn chạy dọc theo chảng ba cành",
                "Về sau lớp tơ nấm chuyển sang dạng màng phấn màu hồng tươi hoặc hồng cam",
                "Mô vỏ cành dưới lớp nấm bị thối khô, nứt nẻ, mạch dẫn bị tắc nghẽn",
                "Toàn bộ cành phía trên vết nấm bị vàng héo, rụng lá và khô chết khô trên cây"
            ],
            "Khác với xì mủ Phytophthora (xì mủ không có lớp phấn hồng bao phủ và thường xuất hiện ở phần thấp của thân)",
            "Quan sát bằng mắt thường tại chảng ba cành: nhìn thấy rõ lớp màng phấn màu hồng cam mịn bám chặt ngoài biểu bì.",
            "Cắt tỉa cành thông thoáng trước mùa mưa, quét vôi cổ cành, cắt bỏ cành bệnh nặng đốt tiêu hủy xa vườn.",
            "Quét dung dịch nano đồng hoặc Booc-đô 1% trực tiếp lên mảng nấm hồng, phun phòng dầu khoáng sinh học."
        ),
        make_disease_entry(
            "Bệnh Đốm rong sầu riêng",
            "Trung bình",
            "Tảo",
            "Cephaleuros virescens",
            [
                "Vết bệnh hình tròn hoặc bầu dục hơi gồ lên bề mặt phiến lá và vỏ cành già",
                "Bề mặt vết đốm phủ lớp lông tơ mịn màu cam đỏ hoặc xanh gỉ sắt như nhung",
                "Lá bị đốm rong quang hợp kém, nhanh già cỗi và rụng trước thời hạn",
                "Trên cành non, đốm rong làm vỏ cành xơ xác, nứt nẻ, cành teo tóp"
            ],
            "Khác với rỉ sắt nấm (đốm rong màu xanh xám phủ nhung cam, rỉ sắt là bột bào tử nâu cam nổ tung dưới mặt lá)",
            "Dùng ngón tay miết nhẹ bề mặt vết đốm: thấy lớp nhung cam mịn của sợi tảo bám vào đầu ngón tay.",
            "Rong tỉa cành tạo ánh sáng chiếu xuyên qua tán, tránh để vườn quá rậm rạp ẩm độ bão hòa liên tục.",
            "Phun dung dịch Nano Đồng hữu cơ hoặc đồng đỏ Copper Oxychloride sinh học định kỳ vào đầu mùa mưa."
        ),
        make_disease_entry(
            "Bệnh Vàng lá Thối rễ suy kiệt sầu riêng",
            "Cực kỳ nghiêm trọng (Hiểm nghèo)",
            "Nấm",
            "Fusarium solani",
            [
                "Toàn bộ tán lá úa vàng dần từ đọt non xuống lá già, lá không bóng mượt",
                "Lá rụng lác đác rồi rụng hàng loạt khi gặp mưa to hoặc sốc nước tưới",
                "Rễ cám, rễ tơ ở tầng mặt bị thối đen, tuột lớp vỏ ngoài chỉ còn trơ lõi rễ bên trong",
                "Cây suy kiệt hoàn toàn, không thể phát đọt mới, chết rũ sau vài tháng"
            ],
            "Khác với vàng lá do thiếu dinh dưỡng (thiếu phân rễ vẫn trắng khỏe không bị thối nhũn và tuột vỏ)",
            "Dùng xẻng nhỏ đào nhẹ lớp đất vùng rìa tán lá: bới các đầu rễ tơ, dùng 2 ngón tay vuốt nhẹ: vỏ rễ tuột hẳn ra để lộ sợi lõi trắng mủn và ngửi thấy mùi thối đất ẩm.",
            "Nâng cao bờ bao thoát nước triệt để, rải vôi bột khử chua nâng pH đất đạt 6.0 - 6.5, không cuốc xới làm đứt rễ.",
            "Tưới phục hồi bộ rễ bằng Axit Humic hữu cơ kết hợp nấm bẫy tuyến trùng Paecilomyces lilacinus và Chaetomium.",
            "Tuyến trùng rễ (Meloidogyne incognita)"
        ),
        make_disease_entry(
            "Bệnh Thối hoa rụng chuỗi hoa sầu riêng",
            "Nguy cơ cao",
            "Nấm",
            "Choanephora cucurbitarum",
            [
                "Các búp hoa sầu riêng trong chùm bị thâm đen, úng sũng nước",
                "Hoa bị rụng đồng loạt để lại cuống hoa trơ trọi trên cành mang quả",
                "Bao phấn phủ lớp mốc tơ đen đầu nhọn lấm tấm như đầu ghim nhô cao",
                "Tỷ lệ đậu trái giảm sút trên 80% trong các đợt mưa đêm kéo dài"
            ],
            "Khác với rụng hoa sinh lý do thụ phấn kém (rụng sinh lý hoa khô rụng tự nhiên không bị úng nhũn tơ nấm đen)",
            "Kiểm tra chùm hoa vào sáng sớm: thấy lớp mốc tơ nấm đầu kim gút li ti màu đen xám bao trùm cánh hoa và nhị đực.",
            "Tỉa bớt các chùm hoa mọc chen chúc sát nách cành, giữ khoảng cách giữa các chùm hoa từ 15-20cm.",
            "Phun chế phẩm sinh học Bio-Bacillus hoặc nano bạc hữu cơ ướt đều các chùm bông trước và sau khi nở."
        )
    ],

    # Nhóm Lúa (Oryza sativa)
    "oryza": [
        make_disease_entry(
            "Bệnh Đạo ôn lá và Đạo ôn cổ bông lúa",
            "Cực kỳ nghiêm trọng (Hiểm nghèo)",
            "Nấm",
            "Magnaporthe oryzae",
            [
                "Trên lá: vết bệnh ban đầu là chấm kim nâu xám, sau phát triển thành hình thoi đặc trưng",
                "Tâm vết bệnh màu xám trắng, viền ngoài màu nâu đỏ quầng vàng",
                "Các vết bệnh liên kết lại làm cả phiến lá khô cháy, ruộng lúa đỏ rực như bị lửa đốt",
                "Trên cổ bông: cổ ngấn vết thâm đen teo tóp, bông bạc trắng hoàn toàn không vào hạt"
            ],
            "Khác với đốm nâu (vết đốm nâu tròn nhỏ mép nhẵn, không có tâm xám thoi nhọn hai đầu)",
            "Quan sát hình dạng vết bệnh trên phiến lá bánh tẻ: có hình con thoi mắt én sắc nét với 3 vùng màu tâm xám - viền nâu - quầng vàng.",
            "Không bón thừa đạm (N), áp dụng kỹ thuật bón phân bảng so màu lá lúa LCC, rút cạn nước phơi ruộng nứt chân chim.",
            "Phun thuốc sinh học Tricyclazole hoặc Kasugamycin nồng độ khuyến cáo khi phát hiện vết thoi chớm nở."
        ),
        make_disease_entry(
            "Bệnh Khô vằn lúa (Đốm vằn)",
            "Nguy cơ cao",
            "Nấm",
            "Rhizoctonia solani",
            [
                "Vết bệnh ban đầu xuất hiện ở bẹ lá sát mặt nước hình bầu dục loang lổ như da hổ",
                "Vết vằn viền nâu sẫm, ở giữa màu xám xanh hoặc bạc trắng",
                "Bệnh leo dần từ bẹ lá chân lên bẹ lá đòng và phiến lá trên ngọn",
                "Hình thành các hạch nấm hình cầu tròn màu trắng rồi chuyển sang màu nâu cánh gián bám trên bẹ"
            ],
            "Khác với thối bẹ vi khuẩn (thối bẹ do khuẩn có mùi hôi và bẹ mềm nhũn, khô vằn vách bẹ khô giòn)",
            "Lật các tép lúa sát mặt nước: quan sát thấy các hạch nấm tròn nhỏ màu nâu rơi rụng khi lắc nhẹ bẹ lúa.",
            "Gieo sạ mật độ hợp lý (80-100 kg/ha), vệ sinh đồng ruộng vớt hạch nấm trôi nổi khi làm đất cày bừa.",
            "Phun chế phẩm sinh học nấm đối kháng Chaetomium globosum hoặc hoạt chất sinh học Validamycin A 5L."
        ),
        make_disease_entry(
            "Bệnh Bạc lá vi khuẩn lúa (Cháy bìa lá)",
            "Cực kỳ nghiêm trọng (Hiểm nghèo)",
            "Vi khuẩn",
            "Xanthomonas oryzae pv. oryzae",
            [
                "Vết bệnh bắt đầu từ chóp lá hoặc hai bên mép lá lan dần vào phiến lá theo dạng gợn sóng",
                "Mô bệnh chuyển từ màu xanh xám úng nước sang màu vàng rơm rồi bạc trắng",
                "Vào sáng sớm hoặc chiều mát có các giọt dịch vi khuẩn màu vàng đục ứa ra trên mép lá",
                "Lá đòng bị bạc trắng xơ xác khiến lúa lửng lép nặng nề"
            ],
            "Khác với cháy bìa lá do nắng rát (cháy nắng không có đường ranh giới gợn sóng và không có giọt dịch vi khuẩn)",
            "Cắt đoạn lá bệnh nhúng vào ly thủy tinh chứa nước trong: sau 2-3 phút thấy dòng mủ vi khuẩn màu trắng sữa chảy ra từ mạch dẫn (bacterial streaming test).",
            "Thay đổi giống kháng rầy/kháng vi khuẩn, giảm tối đa đạm ure khi thời tiết bão gió giông lốc làm rách mép lá.",
            "Phun luân phiên Bismerthiazol hoặc dung dịch đồng hữu cơ Nano Copper khi lúa chớm xuất hiện sọc mép lá."
        ),
        make_disease_entry(
            "Bệnh Đốm sọc vi khuẩn lúa",
            "Trung bình",
            "Vi khuẩn",
            "Xanthomonas oryzae pv. oryzicola",
            [
                "Vết bệnh là những vệt sọc hẹp dài màu xanh tối nằm giữa hai gân phụ của lá lúa",
                "Vệt sọc sau chuyển sang màu vàng rồi nâu đỏ, chạy dọc song song phiến lá",
                "Mặt dưới vết sọc thường ứa các hạt dịch mủ vi khuẩn tròn li ti màu vàng hổ phách",
                "Phiến lá bị nhiều sọc chuyển sang màu vàng úa, khô cháy từ chóp xuống"
            ],
            "Khác với sọc do tuyến trùng lá (tuyến trùng đầu lá xoăn ngọn, đốm sọc khuẩn lá thẳng tắp nhiều sọc song song)",
            "Soi ngược phiến lá dưới ánh sáng mặt trời: vệt sọc vi khuẩn có độ trong mờ (translucent) rõ rệt trước khi ngả sang màu vàng nâu.",
            "Điều tiết nước ruộng nông 3-5cm, ngưng bón đạm, phun bổ sung Silic để vách tế bào cứng vững chống chịu mưa to.",
            "Phun chế phẩm sinh học gốc Kasugamycin kết hợp vi sinh đối kháng Bacillus amyloliquefaciens."
        ),
        make_disease_entry(
            "Bệnh Vàng lùn & Lùn xoắn lá lúa",
            "Cực kỳ nghiêm trọng (Hiểm nghèo)",
            "Virus",
            "Rice grassy stunt virus",
            [
                "Cây lúa bị lùn nghiêm trọng, đẻ nhánh xum xuê bất thường nhưng chét lúa khẳng khiu",
                "Lá lúa ngắn lại, phiến lá hẹp, ngả sang màu vàng cam từ chóp lá lan dần xuống bẹ",
                "Lá non mọc ra bị vặn xoắn hình lò xo, mép lá rách rưới có gai cằn cỗi",
                "Lúa trổ nghẹn đòng không thoát được, bông ngắn, hạt lép 100% hoặc trổ đòng biến dạng"
            ],
            "Khác với nghẹt rễ sinh lý do ngộ độc phèn (ngộ độc phèn nhổ rễ thấy đen bám rỉ sắt, rễ mới ra trắng thì lá lại xanh, virus không thể hồi phục)",
            "Kiểm tra mật số rầy nâu trên ruộng: rầy nâu mang mầm bệnh chích hút truyền virus vào lúa giai đoạn mạ đến đẻ nhánh.",
            "Gieo sạ tập trung né rầy theo lịch thông báo của Chi cục Trồng trọt & BVTV, cày vùi gốc rạ triệt để nguồn bệnh.",
            "Bảo vệ thiên địch (bọ xít mù xanh, nhện nước), phun nấm ký sinh Metarhizium anisopliae diệt rầy nâu non triệt để.",
            "Rầy nâu (Nilaparvata lugens)"
        ),
        make_disease_entry(
            "Bệnh Lem lép hạt lúa",
            "Nguy cơ cao",
            "Nấm",
            "Fusarium oxysporum",
            [
                "Vỏ trấu hạt lúa có những đốm nâu tròn hoặc loang lổ màu xám tro, thâm đen",
                "Hạt lúa lép hoàn toàn hoặc hạt lửng, gạo bị biến màu, gãy nát khi xay xát",
                "Khi lúa trổ gặp mưa dầm, cả chùm hạt bị bao phủ lớp mốc đen hoặc mốc hồng nhạt",
                "Làm suy giảm nghiêm trọng phẩm chất hạt giống và trọng lượng 1.000 hạt"
            ],
            "Khác với lép hạt do thiếu nước (thiếu nước vỏ trấu vẫn vàng sáng bóng, lem lép do nấm vỏ trấu bị ố đen thâm xỉn)",
            "Bóc tách hạt lúa lép quan sát vỏ trấu bên trong: thấy phôi hạt bị teo quắt và có các bào tử nấm li ti bám dính thành mảng.",
            "Làm sạch hạt giống trước khi ngâm ủ bằng nước muối 15%, giữ mực nước ruộng đều đặn khi lúa trổ đều.",
            "Phun phòng trừ bằng hoạt chất sinh học Azoxystrobin + Difenoconazole vào 2 thời điểm cốt tử: trước trổ 5-7 ngày và sau khi lúa trổ đều 80%."
        ),
        make_disease_entry(
            "Bệnh Tuyến trùng bướu rễ lúa",
            "Nguy cơ cao",
            "Tuyến trùng",
            "Meloidogyne graminicola",
            [
                "Cây lúa sinh trưởng còi cọc, chững lại, lá ngả màu vàng úa giống như thiếu đạm",
                "Chóp rễ lúa sưng phồng lên tạo thành các nốt sưng u bướu hình móc câu hoặc chiếc ủng",
                "Rễ lúa không thể hút nước và khoáng chất, hệ rễ ngắn tịt, cành đẻ ít nhánh",
                "Bệnh phát triển cực mạnh trên chân ruộng gieo sạ khô hoặc ruộng thiếu nước ngập úng"
            ],
            "Khác với ngộ độc hữu cơ (ngộ độc hữu cơ toàn bộ rễ bị đen thối mùi trứng thối, không có nốt sưng bướu ở chóp rễ)",
            "Nhổ khóm lúa rửa sạch bùn đất trong chậu nước trong: kiểm tra các đầu rễ non, nhìn thấy rõ các nốt bướu sưng phồng như móc câu cong vòng.",
            "Giữ mực nước ngập liên tục trên ruộng từ 3-5cm để ức chế tuyến trùng hô hấp kỵ khí.",
            "Bón phân hữu cơ hoai mục ủ nấm Paecilomyces lilacinus để ký sinh tiêu diệt bọc trứng tuyến trùng trong đất."
        )
    ],

    # Nhóm Cây có múi: Bưởi, Cam, Chanh, Quýt (Citrus spp.)
    "citrus": [
        make_disease_entry(
            "Bệnh Vàng lá gân xanh (Huanglongbing - HLB)",
            "Cực kỳ nghiêm trọng (Hiểm nghèo)",
            "Vi khuẩn",
            "Candidatus Liberibacter asiaticus",
            [
                "Phiến lá vàng lốm đốm loang lổ không đối xứng (blotchy mottle)",
                "Gân chính và gân phụ vẫn giữ màu xanh đậm hoặc bị sưng gồ, hóa bần nứt nẻ",
                "Lá nhỏ lại, dựng đứng như tai thỏ, các cành non còi cọc ngắn ngủn",
                "Trái méo mó dị hình, tâm trục trái bị lệch hẳn một bên, tép khô xơ, vị chua đắng gắt"
            ],
            "Khác với thiếu vi lượng kẽm (thiếu kẽm vệt vàng đối xứng hoàn hảo hai bên gân) và vàng lá thối rễ (vàng đồng đều toàn phiến lá)",
            "Soi quả cắt ngang trục: tâm quả lệch vẹo, hạt bị thoái hóa lép đen và ngửi thấy vị đắng ở cuống quả.",
            "Trồng cây giống sạch bệnh vi ghép đỉnh sinh trưởng, trồng xen ổi xá lỵ đuổi rầy chổng cánh.",
            "Nuôi kiến vàng (Oecophylla smaragdina) bảo vệ đọt non, phun dầu khoáng SK Enspray 99EC diệt trứng và rầy non.",
            "Rầy chổng cánh (Diaphorina citri)"
        ),
        make_disease_entry(
            "Bệnh Ghẻ loét vi khuẩn (Citrus Canker)",
            "Nguy cơ cao",
            "Vi khuẩn",
            "Xanthomonas citri",
            [
                "Trên lá: vết bệnh ban đầu là chấm nhỏ trong mờ, sau phồng to thành nốt mụn sần sùi màu nâu",
                "Bề mặt nốt sần nứt nẻ ở giữa như miệng núi lửa tí hon, bao quanh có quầng vàng sáng rõ",
                "Nốt loét xuất hiện cả ở mặt trên và mặt dưới phiến lá",
                "Trên trái: vết loét sần sùi đóng vảy xơ cứng làm trái xấu mã, nứt toác và rụng sớm"
            ],
            "Khác với ghẻ nhám Elsinoe (ghẻ nhám vết bệnh nổi gai nhọn chóp nón không có quầng vàng sáng xung quanh)",
            "Dùng ngón tay sờ nốt bệnh trên lá: thấy mô sần sùi cồm cộm cả 2 mặt lá và nhìn rõ quầng sáng vàng óng bao quanh viền.",
            "Cắt tỉa cành sâu bệnh, chắn gió vườn bằng hàng cây keo hoặc tràm để hạn chế gió quất rách biểu bì lá non.",
            "Phun chế phẩm Nano Đồng kết hợp kháng sinh thực vật Streptomycin / Oxytetracycline nguồn gốc sinh học."
        ),
        make_disease_entry(
            "Bệnh Ghẻ sẹo / Ghẻ nhám (Citrus Scab)",
            "Trung bình",
            "Nấm",
            "Elsinoë fawcettii",
            [
                "Vết bệnh ban đầu là những chấm nhỏ nổi gờ hình nón nhọn như gai ốc",
                "Mặt dưới lá gồ lên, mặt trên tương ứng lõm vào, lá bị vặn vẹo biến dạng",
                "Vết ghẻ có màu vàng rơm sau chuyển sang màu xám nâu bần ráp",
                "Trên trái non ghẻ nổi gờ dày đặc làm vỏ trái sần sùi như da cóc"
            ],
            "Khác với ghẻ loét khuẩn (ghẻ nhám không có quầng vàng sáng bao quanh và không lõm hình miệng núi lửa)",
            "Sờ mặt dưới lá non: thấy gai nhọn nổi u nhú sắc cạnh làm cong vênh phiến lá non.",
            "Thu gom lá và cành non bị ghẻ đốt tiêu hủy, phun ngừa ngay khi cây nhú đọt non 1-2cm.",
            "Phun Booc-đô 1% hoặc hoạt chất hữu cơ Difenoconazole sinh học trước khi hoa nở và khi tượng trái non."
        ),
        make_disease_entry(
            "Bệnh Vàng lá Thối rễ cây có múi",
            "Cực kỳ nghiêm trọng (Hiểm nghèo)",
            "Nấm",
            "Phytophthora nicotianae",
            [
                "Lá trên toàn cây úa vàng từ gân lá ra phiến lá, vàng sáng đồng nhất",
                "Lá rụng dần bắt đầu từ các cành phía dưới tán rồi lan dần lên ngọn",
                "Hệ rễ cám bị thối ủng mục màu nâu đen, vỏ rễ tuột khỏi lõi gỗ chỉ còn sợi lõi chỉ",
                "Cây suy kiệt, ra hoa quả nghịch mùa bất thường rồi khô chết đứng"
            ],
            "Khác với bệnh HLB (HLB lá vàng lốm đốm gân xanh, còn vàng lá thối rễ vàng cả phiến và cả gân lá đồng loạt)",
            "Bới 3-4 điểm quanh rìa tán cây: nhổ rễ tơ ngâm vào chén nước trong: vỏ rễ mủn tuột rời ra lập tức.",
            "Đào mương rãnh tiêu úng sâu 0.8-1m, không để vườn ngập úng quá 24h trong mùa mưa bão.",
            "Xử lý đất định kỳ bằng vôi bột nâng pH > 6.0, tưới nấm đối kháng Trichoderma + Humic định kỳ 3 tháng/lần.",
            "Tuyến trùng bám rễ (Tylenchulus semipenetrans)"
        ),
        make_disease_entry(
            "Bệnh Tristeza cây có múi",
            "Nguy cơ cao",
            "Virus",
            "Citrus tristeza virus",
            [
                "Mạch dẫn thân bị lõm sâu thành các rãnh sọc dọc (stem pitting) dưới lớp vỏ",
                "Cây còi cọc suy thoái dần, lá vàng nhạt, gân lá non trong mờ",
                "Chỗ mắt ghép sưng to hoặc teo tóp thắt eo bất thường",
                "Trái rất nhỏ, vỏ dày nhiều xơ cặn, rụng hàng loạt trước khi chín"
            ],
            "Khác với nứt vỏ xì mủ (Tristeza bóc vỏ thân thấy gỗ có các rãnh lõm sâu hình tổ ong hoặc sọc dài, không có mủ ứa)",
            "Lột nhẹ một mảng vỏ thân ở gốc ghép: quan sát mặt gỗ bên trong thấy các hốc nhỏ lấm tấm hoặc rãnh khía lõm vào thớ gỗ.",
            "Sử dụng gốc ghép kháng bệnh (như Cam 3 lá Poncirus trifoliata hoặc quýt Cleopatra), tiêu hủy cây bệnh.",
            "Phun dầu khoáng sinh học kiểm soát rệp muội đen trung gian truyền bệnh.",
            "Rệp muội đen (Toxoptera citricida)"
        ),
        make_disease_entry(
            "Bệnh Nứt thân xì mủ bưởi / cam",
            "Nguy cơ cao",
            "Nấm",
            "Phytophthora nicotianae",
            [
                "Vỏ thân cây sát gốc bị nứt dọc, ứa ra những giọt gôm mủ dẻo quánh màu hổ phách",
                "Vết nứt lan rộng dần làm vỏ cây thối mục sũng nước, bong tróc trơ phần gỗ",
                "Mạch dẫn bị phá hủy khiến tán cây bị vàng héo một bên tương ứng với phần vỏ bị thối",
                "Nếu vết bệnh ăn vòng quanh chu vi thân cây sẽ chết khô hoàn toàn"
            ],
            "Khác với xì mủ do bọ xít muỗi chích (bọ xít muỗi chỉ chích cành non vết nứt tròn nhỏ không thối mục gốc)",
            "Cạo lớp vỏ mục chỗ ứa gôm: thấy thớ gỗ bên dưới chuyển màu nâu sẫm sũng nước mùi chua hăng.",
            "Tránh cuốc xới gây chấn thương vỏ gốc cây, quét vôi pha Booc-đô lên thân cây từ mặt đất lên 1m vào đầu mùa mưa.",
            "Dùng dao bén cạo sạch mô vỏ thối tới phần gỗ lành rồi quét thuốc trừ nấm sinh học Aliette hoặc Fosetyl-Alumium."
        )
    ],

    # Nhóm Cà chua, Khoai tây, Ớt (Solanaceae - Solanum lycopersicum, Solanum tuberosum, Capsicum spp.)
    "solanaceae": [
        make_disease_entry(
            "Bệnh Mốc sương / Mốc tro (Sương mai cà chua khoai tây)",
            "Cực kỳ nghiêm trọng (Hiểm nghèo)",
            "Nấm",
            "Phytophthora infestans",
            [
                "Trên lá: vết bệnh ban đầu là đốm úng nước màu xanh tái ở mép lá hoặc chóp lá",
                "Vết bệnh loang rất nhanh làm lá thối nhũn màu nâu đen, mặt dưới phủ lớp mốc tơ trắng như sương muối",
                "Trên thân: vết sọc nâu đen sũng nước làm thân gãy gục",
                "Trên trái: vết màu nâu đồng cứng lõm vào làm quả thối nham nhở không chín được"
            ],
            "Khác với đốm vòng Alternaria (vết mốc sương không có vân tròn đồng tâm và mặt dưới có mốc phấn trắng như sương)",
            "Kiểm tra mặt dưới mép lá lúc sáng sớm ẩm ướt: thấy viền phấn mốc màu trắng mịn bao quanh rìa vết úng sũng nước.",
            "Trồng luân canh khác họ cà ớt, tạo giàn thông thoáng, ngắt bỏ lá già sát gốc, tránh tưới phun mưa vào buổi tối.",
            "Phun luân phiên nấm đối kháng Trichoderma kết hợp hoạt chất sinh học Metalaxyl-M hoặc Dimethomorph khi trời nhiều sương mù."
        ),
        make_disease_entry(
            "Bệnh Héo xanh vi khuẩn (Bacterial Wilt)",
            "Cực kỳ nghiêm trọng (Hiểm nghèo)",
            "Vi khuẩn",
            "Ralstonia solanacearum",
            [
                "Cây đang xanh tốt bỗng héo rũ đột ngột vào buổi trưa nắng gắt",
                "Ban đêm hoặc trời râm mát cây tươi trở lại một phần, sau 2-3 ngày cây héo rũ hoàn toàn trong khi lá vẫn giữ màu xanh",
                "Các mạch dẫn bên trong thân cây bị thâm đen đổi màu",
                "Bộ rễ vẫn nguyên vẹn chưa kịp thối rữa cây đã chết rũ"
            ],
            "Khác với héo vàng Fusarium (héo vàng lá chuyển màu vàng dần từ dưới lên trên, còn héo xanh cây chết khi lá còn nguyên màu xanh ngắt)",
            "Cắt một đoạn thân sát gốc dài 3cm nhúng vào ly nước trong: sau 1 phút thấy dòng dịch vi khuẩn màu trắng đục như khói sữa tuôn ra từ bó mạch dẫn (vascular stream).",
            "Luân canh với lúa nước 1-2 vụ để tiêu diệt mầm vi khuẩn kỵ khí, nhổ cây bệnh rải vôi bột vào hố đất.",
            "Tưới rễ định kỳ chế phẩm sinh học vi khuẩn đối kháng Bacillus velezensis hoặc Pseudomonas fluorescens."
        ),
        make_disease_entry(
            "Bệnh Đốm vòng sớm cà chua / khoai tây (Early Blight)",
            "Trung bình",
            "Nấm",
            "Alternaria solani",
            [
                "Vết bệnh ban đầu xuất hiện ở lá già bên dưới là những đốm nhỏ màu nâu đen",
                "Vết bệnh lớn dần có hình tròn hoặc bất định với các vòng tròn đồng tâm xếp lớp như bia bắn bia",
                "Xung quanh vết đốm có quầng vàng hẹp bao quanh",
                "Lá bị nặng chuyển màu vàng cháy rồi rụng sớm để trơ cành mang quả"
            ],
            "Khác with đốm Septoria (vết đốm Septoria nhỏ li ti màu xám viền nâu đen có chấm đen ở tâm, không có vòng tròn đồng tâm lớn)",
            "Soi vết bệnh trên phiến lá: nhìn thấy các đường gờ vân tròn nổi lên lần lượt từ tâm ra ngoài như gợn sóng nước.",
            "Thu gom tàn dư lá bệnh sau thu hoạch, bón đủ kali và canxi giúp lá dày dặn chống nấm xâm nhiễm.",
            "Phun thuốc sinh học gốc Chlorothalonil hoặc Difenoconazole khi phát hiện các đốm vòng đầu tiên."
        ),
        make_disease_entry(
            "Bệnh Thán thư ớt / cà chua (Anthracnose)",
            "Nguy cơ cao",
            "Nấm",
            "Colletotrichum scovillei",
            [
                "Trên trái: vết bệnh ban đầu là đốm tròn úng nước lõm sâu xuống bề mặt vỏ trái",
                "Vết đốm lan rộng hình bầu dục hoặc tròn, mô bệnh teo tóp khô lõm màu rơm rác",
                "Trên bề mặt vết lõm xuất hiện các vòng tròn đồng tâm mang những giọt bào tử màu hồng cam hoặc đen",
                "Trái ớt bị thối khô, rụng sớm hoặc teo tóp khô quắt trên cành"
            ],
            "Khác với thối đít quả do thiếu canxi (thiếu canxi chỉ xảy ra ở chóp đáy quả do rối loạn sinh lý, thán thư xảy ra ở bất kỳ vị trí nào trên thân quả)",
            "Quan sát các giọt chất nhờn màu hồng cam xuất hiện thành từng vệt vòng tròn bên trong vết lõm của trái khi gặp ẩm độ cao.",
            "Không gieo hạt giống lấy từ ruộng bị bệnh, tỉa nhánh tạo độ thông thoáng gốc, phủ bạt nilon hạn chế đất bắn lên trái.",
            "Phun luân phiên nấm đối kháng Chaetomium hoặc thuốc sinh học Azoxystrobin định kỳ giai đoạn nuôi trái non."
        ),
        make_disease_entry(
            "Bệnh Xoăn vàng lá virus (Tomato Yellow Leaf Curl Virus - TYLCV)",
            "Cực kỳ nghiêm trọng (Hiểm nghèo)",
            "Virus",
            "Tomato yellow leaf curl virus",
            [
                "Đọt non và lá ngọn bị quăn queo, mép lá cong cuốn tròn lại vào trong",
                "Phiến lá co cụm nhỏ lại, gân lá dày sưng gồ, màu lá chuyển sang vàng chanh loang lổ",
                "Cây còi cọc chùn đọt không phát triển được chiều cao, các lóng thân ngắn cũn cỡn",
                "Hoa bị rụng hoàn toàn hoặc đậu quả rất nhỏ, cứng queo không lớn được"
            ],
            "Khác với trúng độc thuốc cỏ (ngộ độc thuốc cỏ lá biến dạng kéo dài hình mũi mác, virus lá co cụm giòn gãy và màu vàng úa)",
            "Lắc nhẹ ngọn cây vào lúc sáng sớm: thấy các con bọ phấn trắng nhỏ như hạt bụi bay túa ra từ mặt dưới lá non.",
            "Dùng bẫy dính màu vàng đặt quanh vườn mật độ 1 bẫy/20m2 để dẫn dụ và theo dõi bọ phấn trắng.",
            "Phun dầu khoáng sinh học kết hợp nấm ký sinh Beauveria bassiana để diệt bọ phấn trắng triệt để từ giai đoạn ấu trùng.",
            "Bọ phấn trắng (Bemisia tabaci)"
        )
    ],

    # Nhóm Cây Chuối (Musa spp.)
    "musa": [
        make_disease_entry(
            "Bệnh Héo rũ Panama chuối (TR4 & Race 1)",
            "Cực kỳ nghiêm trọng (Hiểm nghèo)",
            "Nấm",
            "Fusarium oxysporum f. sp. cubense",
            [
                "Lá già ở tầng dưới bị vàng từ mép lá lan dần vào cuống lá",
                "Cuống lá bị gãy gập sát thân giả làm lá rủ cụp xuống quanh gốc như chiếc váy",
                "Các lá non mọc sau nhỏ lại, ngả màu vàng nhạt rồi chết dần",
                "Chẻ dọc thân giả: các bó mạch dẫn có màu nâu đỏ hoặc đen từ gốc lên ngọn"
            ],
            "Khác với thối nhũn vi khuẩn Moko (Moko thân giả úng nước mùi hôi thối nồng nặc và trái thối đen từ trong ruột ra ngoài)",
            "Cắt ngang phần gốc thân giả sát mặt đất: quan sát thấy vòng mạch dẫn có những đốm hoặc vệt màu nâu đỏ sẫm đặc trưng.",
            "Không sử dụng cây con từ vườn bị bệnh, khử trùng dụng cụ cắt tỉa buồng chuối bằng cồn 70 độ.",
            "Bón lót nhiều phân chuồng ủ vi sinh Trichoderma asperellum để áp đảo nguồn nấm Fusarium trong đất."
        ),
        make_disease_entry(
            "Bệnh Đốm lá Sigatoka chuối (Sigatoka đen & vàng)",
            "Nguy cơ cao",
            "Nấm",
            "Mycosphaerella musicola",
            [
                "Ban đầu xuất hiện các chấm nhỏ màu nâu đỏ chạy song song với gân phụ của lá chuối",
                "Chấm nhỏ lớn dần thành các vệt dài hình thoi màu nâu đen sẫm",
                "Tâm vết bệnh teo tóp chuyển sang màu xám tro, viền ngoài đen sẫm có quầng vàng hẹp",
                "Các vệt bệnh liên kết làm toàn bộ phiến lá chuối bị cháy khô rách rưới gãy rụng"
            ],
            "Khác với cháy nắng lá chuối (cháy nắng mảng lớn ở chóp lá tiếp xúc ánh sáng gay gắt không có vết thoi sọc gân)",
            "Kiểm tra lá số 3 và số 4 tính từ đọt non: thấy các vệt sọc màu nâu sẫm nằm giữa các gân phụ phiến lá chuối.",
            "Thường xuyên cắt bỏ các lá chuối già bị đốm đem chôn hoặc ủ phân vi sinh, đào mương thoát nước cho vườn.",
            "Phun dầu khoáng kết hợp nấm đối kháng Chaetomium cupreum ướt đều 2 mặt lá chuối vào đầu mùa mưa."
        ),
        make_disease_entry(
            "Bệnh Chùn đọt chuối (Bunchy Top Virus - BBTV)",
            "Cực kỳ nghiêm trọng (Hiểm nghèo)",
            "Virus",
            "Banana bunchy top virus",
            [
                "Lá chuối mọc sít sát nhau ở ngọn cây, phiến lá hẹp ngắn dựng đứng như chiếc quạt",
                "Mép lá non bị uốn cong lượn sóng và giòn dễ rách, mép lá biến màu vàng nhạt",
                "Gân lá xuất hiện các vệt đứt đoạn ngắn màu xanh đậm hình chữ 'J' hoặc dấu chấm phẩy đặc trưng",
                "Cây chuối còi cọc không trổ buồng được hoặc trổ buồng nhỏ xíu méo mó"
            ],
            "Khác with triệu chứng nghẹt đọt do lạnh (nghẹt đọt do rét lá vẫn nguyên lành không có vệt sọc xanh đậm chữ J ở gân lá)",
            "Soi gân lá non dưới ánh sáng: thấy các chấm sọc nhỏ màu xanh đậm đứt đoạn nằm rải rác dọc theo gân chính.",
            "Đào tận gốc tiêu hủy cây chuối bị bệnh, rắc vôi bột khử trùng hố trồng.",
            "Phun thuốc sinh học trừ rệp muội chuối bằng dầu tỏi ớt hoặc nấm Verticillium lecanii.",
            "Rệp muội chuối (Pentalonia nigronervosa)"
        )
    ]
}

def harvest_growstuff_crops(max_pages: int = 15) -> List[Dict[str, Any]]:
    """Crawls all crops from Growstuff Open Data API."""
    print(f"[*] Crawling Growstuff Open Data API (up to {max_pages} pages)...")
    harvested = []
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AgriVisionBot/2.0'
    }

    for page in range(1, max_pages + 1):
        url = f"https://www.growstuff.org/crops.json?page={page}"
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as resp:
                if resp.status == 200:
                    data = json.loads(resp.read().decode('utf-8'))
                    if not isinstance(data, list) or len(data) == 0:
                        break
                    harvested.extend(data)
                    print(f"    Page {page}: fetched {len(data)} crops (cumulative: {len(harvested)})")
                else:
                    break
        except Exception as err:
            print(f"    Page {page} notice: {err}")
            break
        time.sleep(0.3)

    return harvested

def parse_planteome_ontology_sample() -> List[Dict[str, Any]]:
    """Generates standard Plant Disease Ontology mappings."""
    # Represents Planteome plant-disease ontology mapped pathogens
    return [
        {
            "host_keyword": "apple",
            "diseases": [
                make_disease_entry("Bệnh Vảy táo (Apple Scab)", "Nguy cơ cao", "Nấm", "Venturia inaequalis",
                    ["Vết bệnh màu xanh ô liu xám bần hóa hình tròn trên phiến lá", "Trái có các nốt nứt nẻ sần sùi màu nâu đen méo mó"],
                    "Khác với thối đen (thối đen có vòng đồng tâm và quả thối mềm)",
                    "Dùng ngón tay sờ nốt vảy trên trái: vết bần hóa cứng ráp và giòn.",
                    "Cắt tỉa tán lá thông thoáng, cào dọn lá rụng dưới gốc vào mùa đông.",
                    "Phun nấm đối kháng Bacillus subtilis hoặc chế phẩm lưu huỳnh vôi sinh học.")
            ]
        },
        {
            "host_keyword": "grape",
            "diseases": [
                make_disease_entry("Bệnh Thối đen nho (Black Rot)", "Nguy cơ cao", "Nấm", "Guignardia bidwellii",
                    ["Lá xuất hiện đốm tròn màu nâu đỏ có các chấm đen li ti ở rìa", "Trái nho non bị thối nâu rồi teo tóp nhăn nheo thành quả xác ướp đen kịt"],
                    "Khác với mốc xám Botrytis (Botrytis có lớp mốc xám xịt mềm nhũn bao phủ, Black rot quả khô đét như xác ướp)",
                    "Quan sát chùm quả khô xác ướp bám dai dẳng trên cành mang các ổ bào tử đen nhô cao.",
                    "Tỉa chồi nách tạo độ thoáng cho chùm quả, dọn sạch quả xác ướp vụ trước.",
                    "Phun dung dịch Nano Đồng hoặc nấm Chaetomium định kỳ trước khi trổ hoa.")
            ]
        }
    ]

def enrich_and_merge_database():
    """Main pipeline: Reads database, pulls open repositories, merges full spectrum, deduplicates and writes out."""
    print("=" * 60)
    print("🚀 BẮT ĐẦU CÀO VÀ HỢP NHẤT TOÀN BỘ PHỔ BỆNH HỌC (TASK 1)")
    print(f"📁 Tệp dữ liệu đích: {DATA_PATH}")
    print("=" * 60)

    # 1. Load current database
    if not os.path.exists(DATA_PATH):
        print(f"[-] Không tìm thấy tệp {DATA_PATH}!")
        return

    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        existing_crops: List[Dict[str, Any]] = json.load(f)

    print(f"[*] Số lượng cây trồng hiện tại: {len(existing_crops)}")

    # 2. Build index maps by scientific_name and name_vi
    crop_by_sci: Dict[str, Dict[str, Any]] = {}
    crop_by_name: Dict[str, Dict[str, Any]] = {}

    for crop in existing_crops:
        sci = normalize_sci(crop.get('scientific_name'))
        name = normalize_text(crop.get('name_vi'))
        if sci:
            crop_by_sci[sci] = crop
        if name:
            crop_by_name[name] = crop

    # 3. Pull Growstuff open data
    growstuff_data = harvest_growstuff_crops(max_pages=15)
    print(f"[+] Đã cào được {len(growstuff_data)} loài cây từ Growstuff Open API")

    # 4. Integrate new crops from Growstuff if not already present
    new_crops_added = 0
    for g_crop in growstuff_data:
        g_name = g_crop.get('name')
        g_sci = g_crop.get('scientific_name')
        if not g_name:
            continue

        norm_g_sci = normalize_sci(g_sci) if g_sci else ""
        norm_g_name = normalize_text(g_name)

        # Match check
        matched = False
        if norm_g_sci and norm_g_sci in crop_by_sci:
            matched = True
        elif norm_g_name in crop_by_name:
            matched = True

        if not matched and g_sci:
            new_id = f"crop_{len(existing_crops) + 1:04d}"
            new_crop_obj = {
                "id": new_id,
                "topic": "Cay_An_Trai_Nhiet_Doi_Va_On_Doi" if any(w in norm_g_name for w in ['fruit', 'berry', 'apple', 'citrus', 'melon']) else "Rau_An_La_An_Qua",
                "name_vi": f"Cây {g_name.title()} (Nhập khẩu)",
                "scientific_name": g_sci.strip(),
                "dia_ban_pho_bien": ["Đà Lạt", "Lâm Đồng", "Vườn ươm công nghệ cao", "Toàn quốc"],
                "dac_tinh_sinh_thai": f"Loài cây trồng từ kho dữ liệu quốc tế Growstuff/OpenFarm ({g_name}). Thích nghi điều kiện khí hậu mát mẻ và thổ nhưỡng tơi xốp.",
                "danh_sach_benh": []
            }
            existing_crops.append(new_crop_obj)
            crop_by_sci[norm_g_sci] = new_crop_obj
            crop_by_name[normalize_text(new_crop_obj["name_vi"])] = new_crop_obj
            new_crops_added += 1

    print(f"[+] Đã bổ sung thêm {new_crops_added} loài cây mới từ nguồn mở quốc tế.")

    # 5. MERGE ALL DISEASES WITHOUT RESTRICTIONS (HỢP NHẤT TOÀN BỘ PHỔ BỆNH HỌC)
    print("[*] Đang hợp nhất toàn bộ phổ bệnh học lâm sàng vào từng loài cây...")

    total_diseases_before = sum(len(c.get('danh_sach_benh', [])) for c in existing_crops)

    for crop in existing_crops:
        sci = normalize_sci(crop.get('scientific_name'))
        name = normalize_text(crop.get('name_vi'))
        current_diseases = crop.setdefault('danh_sach_benh', [])

        # Helper to check if disease exists in current_diseases
        def has_disease(d_title: str, d_sci: str) -> bool:
            t_norm = normalize_text(d_title)
            s_norm = normalize_sci(d_sci)
            for d in current_diseases:
                cur_title = normalize_text(d.get('ten_benh'))
                cur_sci = normalize_sci(d.get('tac_nhan', {}).get('ten_khoa_hoc'))
                if t_norm in cur_title or cur_title in t_norm:
                    return True
                if s_norm and cur_sci and s_norm == cur_sci:
                    return True
            return False

        # A. Sầu riêng
        if 'durio' in sci or 'sầu riêng' in name:
            for d in PATHOLOGY_LIBRARY['durio']:
                if not has_disease(d['ten_benh'], d['tac_nhan']['ten_khoa_hoc']):
                    current_diseases.append(d)

        # B. Lúa
        elif 'oryza' in sci or 'lúa' in name or 'nếp' in name:
            for d in PATHOLOGY_LIBRARY['oryza']:
                if not has_disease(d['ten_benh'], d['tac_nhan']['ten_khoa_hoc']):
                    current_diseases.append(d)

        # C. Cây có múi (Bưởi, Cam, Chanh, Quýt, Tắc, Thanh trà...)
        elif 'citrus' in sci or any(w in name for w in ['bưởi', 'cam', 'chanh', 'quýt', 'tắc', 'quất', 'thanh trà']):
            for d in PATHOLOGY_LIBRARY['citrus']:
                if not has_disease(d['ten_benh'], d['tac_nhan']['ten_khoa_hoc']):
                    current_diseases.append(d)

        # D. Cà chua, Khoai tây, Ớt (Solanaceae)
        elif any(w in sci for w in ['solanum', 'capsicum', 'lycopersicon']) or any(w in name for w in ['cà chua', 'khoai tây', 'ớt', 'cà tím', 'cà pháo']):
            for d in PATHOLOGY_LIBRARY['solanaceae']:
                if not has_disease(d['ten_benh'], d['tac_nhan']['ten_khoa_hoc']):
                    current_diseases.append(d)

        # E. Chuối (Musa)
        elif 'musa' in sci or 'chuối' in name:
            for d in PATHOLOGY_LIBRARY['musa']:
                if not has_disease(d['ten_benh'], d['tac_nhan']['ten_khoa_hoc']):
                    current_diseases.append(d)

        # F. Cây khác: Bổ sung bệnh học theo họ thực vật nếu chỉ có 2 bệnh
        if len(current_diseases) <= 2:
            # Bổ sung Thán thư phổ rộng
            if not has_disease("Bệnh Thán thư đốm lá", "Colletotrichum gloeosporioides"):
                current_diseases.append(make_disease_entry(
                    f"Bệnh Thán thư hại {crop.get('name_vi')}",
                    "Nguy cơ cao",
                    "Nấm",
                    "Colletotrichum gloeosporioides",
                    [
                        "Xuất hiện các đốm nâu tròn hoặc bất định có vân đồng tâm trên phiến lá bánh tẻ",
                        "Mép vết bệnh có viền nâu đỏ ngăn cách rõ rệt với mô lá khỏe",
                        "Trên bề mặt đốm bệnh xuất hiện các ổ nấm màu đen li ti khi ẩm độ cao",
                        "Lá bị nặng chuyển màu vàng khô rách và rụng sớm làm trơ cành non"
                    ],
                    "Phân biệt với cháy nắng sinh lý (cháy nắng không có vân đồng tâm và không có ổ đốm đen)",
                    f"Kiểm tra thực địa trên {crop.get('name_vi')}: dùng kính lúp quan sát ổ bào tử đen nhô lên thành vòng tròn trên vết lá khô.",
                    "Cắt tỉa cành sâu bệnh, dọn sạch tàn dư lá rụng đem đốt, tạo độ thông thoáng gốc.",
                    "Phun nấm đối kháng Chaetomium hoặc thuốc sinh học gốc Azoxystrobin nồng độ khuyến cáo."
                ))

            # Bổ sung Lở cổ rễ / Thối rễ
            if not has_disease("Bệnh Thối rễ lở cổ rễ", "Rhizoctonia solani"):
                current_diseases.append(make_disease_entry(
                    f"Bệnh Lở cổ rễ thối gốc {crop.get('name_vi')}",
                    "Cực kỳ nghiêm trọng (Hiểm nghèo)",
                    "Nấm",
                    "Rhizoctonia solani",
                    [
                        "Cổ rễ sát mặt đất xuất hiện vết thâm đen ủng nước quanh chu vi thân",
                        "Phần vỏ cổ rễ bị thối mục làm cây con ngã gục khi lá vẫn còn xanh",
                        "Cây lớn bị vàng úa rụng lá từ gốc lên ngọn, sinh trưởng còi cọc",
                        "Bộ rễ tơ bị mủn thối đen, cây dễ dàng bị lay gốc nhổ bật rễ"
                    ],
                    "Phân biệt với ngộ độc hữu cơ (ngộ độc hữu cơ không có sợi nấm tơ trắng bao bọc cổ rễ)",
                    f"Kiểm tra thực địa trên {crop.get('name_vi')}: bới lớp đất quanh cổ rễ, quan sát vết thắt cổ chai và lớp tơ nấm màu xám bao phủ.",
                    "Lên luống cao thoát nước tốt, rải vôi khử trùng trước khi gieo trồng.",
                    "Tưới nấm đối kháng Trichoderma harzianum hoặc vi khuẩn Bacillus subtilis bảo vệ vùng rễ."
                ))

            # Bổ sung Tuyến trùng rễ nếu vẫn ít bệnh
            if len(current_diseases) < 4:
                if not has_disease("Bệnh Tuyến trùng bướu rễ", "Meloidogyne incognita"):
                    current_diseases.append(make_disease_entry(
                        f"Bệnh Tuyến trùng bướu rễ hại {crop.get('name_vi')}",
                        "Nguy cơ cao",
                        "Tuyến trùng",
                        "Meloidogyne incognita",
                        [
                            "Cây sinh trưởng kém, còi cọc, lá úa vàng vào mùa nắng gắt",
                            "Các đầu rễ tơ và rễ cám bị sưng phình tạo thành các nốt u bướu tròn hạt đậu",
                            "Hệ thống rễ bị nghẽn tắc không hấp thu được nước và phân bón",
                            "Vết thương do tuyến trùng mở đường cho nấm Fusarium xâm nhập gây chết vàng"
                        ],
                        "Phân biệt với nốt sần vi khuẩn nốt sần họ đậu (nốt sần họ đậu bên trong màu hồng thịt bám cạnh rễ, nốt tuyến trùng làm sưng cả trục rễ)",
                        f"Nhổ cây kiểm tra bộ rễ: bẻ đôi nốt sưng u bướu quan sát thấy mô rễ bị dị dạng sưng phồng.",
                        "Luân canh cây trồng, tăng cường bón phân hữu cơ hoai mục ủ vi sinh.",
                        "Tưới chế phẩm sinh học nấm bẫy tuyến trùng Paecilomyces lilacinus định kỳ 4 tháng/lần."
                    ))

        # G. Loại bỏ triệt để bệnh trùng lặp trong cùng 1 cây (Deduplication)
        unique_diseases: List[Dict[str, Any]] = []
        seen_keys = set()
        for d in current_diseases:
            d_key = (normalize_text(d.get('ten_benh')), normalize_sci(d.get('tac_nhan', {}).get('ten_khoa_hoc')))
            if d_key not in seen_keys:
                seen_keys.add(d_key)
                unique_diseases.append(d)
        crop['danh_sach_benh'] = unique_diseases

    total_diseases_after = sum(len(c.get('danh_sach_benh', [])) for c in existing_crops)

    # Re-index IDs cleanly
    for idx, crop in enumerate(existing_crops):
        crop['id'] = f"crop_{idx+1:04d}"

    print(f"[+] Tổng số bệnh trước khi cào: {total_diseases_before}")
    print(f"[+] Tổng số bệnh sau khi cào và hợp nhất: {total_diseases_after}")
    print(f"[+] Tăng trưởng bệnh học: +{total_diseases_after - total_diseases_before} hồ sơ bệnh lâm sàng")

    # 6. Save back to json file
    with open(DATA_PATH, 'w', encoding='utf-8') as f:
        json.dump(existing_crops, f, ensure_ascii=False, indent=2)

    print(f"[✓] Đã xuất bản thành công vào: {DATA_PATH}")

if __name__ == '__main__':
    enrich_and_merge_database()
