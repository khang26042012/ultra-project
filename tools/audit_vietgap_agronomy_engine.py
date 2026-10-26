# -*- coding: utf-8 -*-
"""
Auditor Subagent 5: VietGAP Agronomic & Biological Protocol Auditor Engine
Specialized Auditor for:
1. 100% Biological VietGAP Protocols (Trichoderma, Chaetomium, Bacillus, Pseudomonas,
   Beauveria, Metarhizium, nano copper/silver, SK Enspray mineral oil, garlic/chili, Chitosan).
2. 0% Banned Chemicals (Zero tolerance for Paraquat, Chlorpyrifos, Carbofuran, 2.4D, Glyphosate).
3. Highly practical, tangible, sensory field tests for Vietnamese farmers
   (smell, vascular scrape, water bacterial streaming test, tactile softness/brittleness).
4. Rigorous Double Diagnosis Disambiguation (contrast with lookalike diseases and abiotic stresses).
"""

import json
import os
import re
import sys
from typing import Dict, List, Any, Tuple

try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

# Banned chemical substances in Vietnam agriculture (Decision No. 501/QD-BNN-BVTV, Circular 10/2020/TT-BNNPTNT)
BANNED_CHEMICALS = {
    'paraquat': 'Chế phẩm sinh học nano đồng kết hợp nấm đối kháng Chaetomium',
    'chlorpyrifos': 'Chế phẩm nấm ký sinh Beauveria bassiana kết hợp dầu khoáng SK Enspray 99EC',
    'carbofuran': 'Chế phẩm nấm tím Paecilomyces lilacinus kết hợp tưới nấm xanh Metarhizium',
    '2,4-d': 'Biện pháp thủ công làm cỏ, phủ bạt hữu cơ giữ ẩm',
    '2.4d': 'Biện pháp làm cỏ cơ giới và che phủ gốc bằng rơm rạ mục',
    'glyphosate': 'Cắt cỏ tạo thảm thực vật che phủ giữ ẩm đất hoặc phủ rơm hữu cơ',
    'chlordimeform': 'Dầu khoáng thảo mộc Neem oil kết hợp nấm xanh Metarhizium',
    'endosulfan': 'Nấm ký sinh Beauveria bassiana kết hợp dịch chiết tỏi ớt',
    'methamidophos': 'Dầu khoáng SK Enspray 99EC kết hợp vi khuẩn Bacillus thuringiensis',
    'monocrotophos': 'Chế phẩm thảo mộc xà phòng neem kết hợp nấm Beauveria',
    'phosphamidon': 'Chế phẩm sinh học thảo mộc xua đuổi côn trùng',
    'methyl parathion': 'Chế phẩm sinh học an toàn VietGAP',
    'parathion': 'Chế phẩm sinh học thảo mộc vi sinh',
    'ddt': 'Chế phẩm vi sinh an toàn',
    'aldrin': 'Chế phẩm nấm đối kháng sinh học',
    'dieldrin': 'Chế phẩm vi sinh an toàn'
}

# Standard safe biological agents
BIO_KEYWORDS = [
    'trichoderma', 'chaetomium', 'bacillus', 'pseudomonas', 'beauveria', 'metarhizium',
    'nano đồng', 'nano bạc', 'enspray', 'dầu khoáng', 'chitosan', 'tỏi', 'ớt', 'gừng',
    'neem', 'paecilomyces', 'lecanicillium', 'streptomyces', 'vi sinh', 'đối kháng',
    'sinh học', 'hữu cơ', 'kiến vàng', 'booc-đô', 'bordeaux', 'kháng sinh sinh học'
]

def clean_text(text: str) -> str:
    if not text:
        return ""
    return re.sub(r'\s+', ' ', str(text)).strip()

def check_and_fix_banned_chemicals(disease: Dict[str, Any]) -> List[str]:
    fixes = []
    vietgap = disease.get('phac_do_vietgap', {})
    if not isinstance(vietgap, dict):
        return fixes

    for key in ['canh_tac', 'sinh_hoc', 'khuyen_cao_chuyen_gia', 'khuyen_cao_vinh_long']:
        val = vietgap.get(key, '')
        if not val or not isinstance(val, str):
            continue
        val_lower = val.lower()
        for banned, replacement in BANNED_CHEMICALS.items():
            if banned in val_lower:
                # Replace banned chemical with biological alternative
                pattern = re.compile(re.escape(banned), re.IGNORECASE)
                val = pattern.sub(replacement, val)
                vietgap[key] = val
                fixes.append(f"Đã loại bỏ hóa chất cấm '{banned}' trong mục {key} và thay bằng '{replacement}'")
    return fixes

def enrich_vietgap_bio_protocol(disease: Dict[str, Any], crop_name: str) -> List[str]:
    fixes = []
    vietgap = disease.setdefault('phac_do_vietgap', {})
    if not isinstance(vietgap, dict):
        disease['phac_do_vietgap'] = {
            'canh_tac': 'Vệ sinh tàn dư cây trồng, tỉa cành thông thoáng, luân canh hợp lý',
            'sinh_hoc': 'Phun tưới nấm đối kháng Trichoderma kết hợp vi khuẩn Bacillus subtilis',
            'khuyen_cao_chuyen_gia': 'Thực hiện nghiêm ngặt quy trình VietGAP an toàn sinh học'
        }
        vietgap = disease['phac_do_vietgap']
        fixes.append("Khởi tạo cấu trúc phác đồ VietGAP chuẩn")

    # Ensure canh_tac is present
    canh_tac = clean_text(vietgap.get('canh_tac', ''))
    if len(canh_tac) < 20:
        vietgap['canh_tac'] = f"Thu gom tiêu hủy tàn dư bệnh hại trên {crop_name}, cắt tỉa tán tạo độ thông thoáng tối đa, bón lót phân chuồng hoai mục ủ vi sinh và cân đối phân bón hữu cơ N-P-K."
        fixes.append("Cập nhật biện pháp canh tác chuẩn VietGAP chi tiết")

    # Check biological protocol
    sinh_hoc = clean_text(vietgap.get('sinh_hoc', ''))
    sinh_hoc_lower = sinh_hoc.lower()
    has_bio = any(k in sinh_hoc_lower for k in BIO_KEYWORDS)

    # Determine pathogen type and disease name
    tac_nhan = disease.get('tac_nhan', {})
    pathogen_type = ''
    pathogen_sci = ''
    if isinstance(tac_nhan, dict):
        pathogen_type = clean_text(tac_nhan.get('loai', '')).lower()
        pathogen_sci = clean_text(tac_nhan.get('ten_khoa_hoc', '')).lower()
    elif isinstance(tac_nhan, str):
        pathogen_type = tac_nhan.lower()

    ten_benh = clean_text(disease.get('ten_benh', '')).lower()

    # Formulate tailored biological treatment if missing or weak
    if not has_bio or len(sinh_hoc) < 25:
        if 'tuyến trùng' in pathogen_type or 'meloidogyne' in pathogen_sci or 'tuyến trùng' in ten_benh:
            vietgap['sinh_hoc'] = "Tưới định kỳ nấm ký sinh bắt tuyến trùng Paecilomyces lilacinus kết hợp nấm đối kháng Chaetomium; bón nhiều phân hữu cơ hoai mục ủ cùng chủng Trichoderma viride và xen canh cúc vạn thọ (Tagetes erecta) để xua đuổi tuyến trùng rễ."
        elif 'vi khuẩn' in pathogen_type or 'xanthomonas' in pathogen_sci or 'ralstonia' in pathogen_sci or 'pseudomonas' in pathogen_sci or 'pectobacterium' in pathogen_sci or 'erwinia' in pathogen_sci or 'vi khuẩn' in ten_benh or 'loét' in ten_benh:
            vietgap['sinh_hoc'] = "Phun luân phiên chế phẩm vi khuẩn đối kháng Bacillus subtilis (nồng độ 10^9 CFU/ml) kết hợp chế phẩm nano bạc sinh học và dịch chiết thảo mộc tỏi ớt gừng nhằm diệt khuẩn tiếp xúc; tưới gốc Pseudomonas fluorescens ức chế vi khuẩn vùng rễ."
        elif 'virus' in pathogen_type or 'virus' in ten_benh or 'khảm' in ten_benh or 'xoăn' in ten_benh:
            vietgap['sinh_hoc'] = "Phun nấm ký sinh côn trùng Beauveria bassiana kết hợp dầu khoáng SK Enspray 99EC để tiêu diệt triệt để bọ trĩ, rầy phấn trắng, rệp muội (véc-tơ truyền virus); phun dịch Chitosan nano 2% kích hoạt hệ miễn dịch tế bào thực vật kháng virus."
        elif 'rầy' in ten_benh or 'rệp' in ten_benh or 'sâu' in ten_benh or 'nhện' in ten_benh or 'bọ xít' in ten_benh:
            vietgap['sinh_hoc'] = "Phun hỗn hợp chế phẩm nấm xanh Metarhizium anisopliae kết hợp nấm trắng Beauveria bassiana và dầu khoáng sinh học SK Enspray 99EC vào chiều mát; nuôi dưỡng quần thể thiên địch tự nhiên như kiến vàng và bọ rùa."
        elif 'thối rễ' in ten_benh or 'xì mủ' in ten_benh or 'phytophthora' in pathogen_sci or 'fusarium' in pathogen_sci or 'pythium' in pathogen_sci or 'chết nhanh' in ten_benh or 'lở cổ rễ' in ten_benh:
            vietgap['sinh_hoc'] = "Tưới đẫm vùng rễ chế phẩm nấm đối kháng Trichoderma harzianum kết hợp Chaetomium cupreum; quét dung dịch Booc-đô 1% hoặc nano đồng sinh học nguyên chất lên vết nứt cổ rễ sau khi cạo sạch phần mô thối."
        elif 'thán thư' in ten_benh or 'colletotrichum' in pathogen_sci:
            vietgap['sinh_hoc'] = "Phun phòng nấm đối kháng Chaetomium cupreum kết hợp vi khuẩn Bacillus subtilis và dịch chiết vỏ tôm Chitosan nano 2% giúp bao bọc biểu bì bảo vệ hoa, chồi non và trái non khỏi nấm thán thư."
        elif 'phấn trắng' in ten_benh or 'sương mai' in ten_benh or 'rỉ sắt' in ten_benh or 'đốm lá' in ten_benh:
            vietgap['sinh_hoc'] = "Phun phòng trừ bằng chế phẩm vi khuẩn Bacillus subtilis luân phiên nano đồng - nano bạc sinh học và dầu khoáng nông nghiệp SK Enspray 99EC nồng độ 0.5% dập tắt mầm bệnh nấm phát tán."
        else:
            vietgap['sinh_hoc'] = "Ưu tiên phun phòng nấm đối kháng Chaetomium và Trichoderma kết hợp vi khuẩn Bacillus subtilis và nano đồng sinh học kích thích sức đề kháng tự nhiên của cây theo chuẩn VietGAP."
        fixes.append(f"Bổ sung phác đồ sinh học VietGAP an toàn cho '{disease.get('ten_benh')}'")

    return fixes

def enrich_practical_field_test(disease: Dict[str, Any], crop_name: str) -> List[str]:
    fixes = []
    field_test = clean_text(disease.get('kiem_tra_thuc_dia', ''))
    field_test_lower = field_test.lower()

    ten_benh = clean_text(disease.get('ten_benh', '')).lower()
    tac_nhan = disease.get('tac_nhan', {})
    pathogen_type = ''
    pathogen_sci = ''
    if isinstance(tac_nhan, dict):
        pathogen_type = clean_text(tac_nhan.get('loai', '')).lower()
        pathogen_sci = clean_text(tac_nhan.get('ten_khoa_hoc', '')).lower()

    # Sensory keywords: olfactory, tactile, incision, water cut, magnifying glass
    sensory_keywords = ['ngửi', 'mùi', 'cạo', 'mạch dẫn', 'nhúng nước', 'dòng mủ', 'bóp', 'sờ', 'kính lúp', 'bẻ', 'miết', 'soi']
    is_sensory = any(k in field_test_lower for k in sensory_keywords)

    if len(field_test) < 25 or not is_sensory:
        if 'héo rũ' in ten_benh or 'ralstonia' in pathogen_sci or ('héo' in ten_benh and 'vi khuẩn' in pathogen_type):
            disease['kiem_tra_thuc_dia'] = "Cắt một đoạn thân sát gốc dài 3-5 cm nhúng đứng vào ly nước trong: sau 2-3 phút quan sát thấy dòng dịch mủ vi khuẩn màu trắng đục tuôn rỉ ra như dải khói; cạo nhẹ vỏ thân thấy mạch dẫn chuyển màu nâu thẫm."
        elif 'fusarium' in pathogen_sci or ('héo vàng' in ten_benh and 'nấm' in pathogen_type):
            disease['kiem_tra_thuc_dia'] = "Dùng dao sắc chẻ dọc phần gốc thân: quan sát hai dải mạch dẫn gỗ chuyển màu nâu sẫm hoặc tím khô ráo kéo dài lên trên; nhúng gốc vào ly nước trong không thấy dòng mủ vi khuẩn chảy ra."
        elif 'thối rễ' in ten_benh or 'vàng lá thối rễ' in ten_benh or 'pythium' in pathogen_sci or 'phytophthora' in pathogen_sci:
            disease['kiem_tra_thuc_dia'] = "Bới nhẹ lớp đất vùng rìa tán lá: dùng ngón tay bóp nhẹ đầu rễ tơ thấy vỏ rễ bị thối nhũn, dễ dàng tuột khỏi lõi gỗ màu nâu trơ trụi, ngửi rễ có mùi ủng chua đặc trưng của nấm thủy sinh."
        elif 'xì mủ' in ten_benh or 'nứt thân' in ten_benh or 'chảy nhựa' in ten_benh:
            disease['kiem_tra_thuc_dia'] = "Dùng dao cạo nhẹ lớp vỏ ngoài vùng gốc thân nghi nhiễm: nếu thấy phần gỗ phía trong sũng nước, chuyển màu nâu đỏ cánh gián và ứa giọt dịch nhựa nhớt có mùi chua men rượu là chính xác nấm bệnh Phytophthora."
        elif 'thối mềm' in ten_benh or 'thối nhũn' in ten_benh or 'pectobacterium' in pathogen_sci or 'erwinia' in pathogen_sci:
            disease['kiem_tra_thuc_dia'] = "Bóp nhẹ vào mô bệnh thấy mềm nhũn chảy nước nhớt đục, đưa lên ngửi thấy mùi thối khắm tanh nồng nặc đặc trưng do vi khuẩn phân hủy pectin tế bào."
        elif 'thán thư' in ten_benh or 'colletotrichum' in pathogen_sci:
            disease['kiem_tra_thuc_dia'] = "Quan sát vết đốm trên lá hoặc quả có hình tròn viền nâu đỏ tâm xám lõm sâu; khi gặp trời mưa ẩm dùng ngón tay sờ thấy nhầy ướt dính chất dịch nhờn bào tử màu hồng cam hoặc hạt đen li ti xếp thành vòng đồng tâm."
        elif 'phấn trắng' in ten_benh or 'oidium' in pathogen_sci or 'podosphaera' in pathogen_sci:
            disease['kiem_tra_thuc_dia'] = "Dùng ngón tay miết nhẹ lên bề mặt lá non thấy lớp phấn trắng mỏng mịn bám dính vào đầu ngón tay như bột phấn rôm, phiến lá phía dưới bị teo tóp quăn queo."
        elif 'rỉ sắt' in ten_benh or 'puccinia' in pathogen_sci or 'uromyces' in pathogen_sci:
            disease['kiem_tra_thuc_dia'] = "Lật mặt dưới phiến lá: dùng móng tay cạo nhẹ các ổ mụn nổi màu vàng cam hoặc nâu đỏ như bột rỉ sắt thấy bột phấn bào tử rơi ra bám đầy đầu ngón tay."
        elif 'loét' in ten_benh or 'canker' in ten_benh or 'xanthomonas' in pathogen_sci:
            disease['kiem_tra_thuc_dia'] = "Sờ tay lên vết bệnh thấy bề mặt xù xì gồ ghề nứt nẻ như miệng núi lửa tí hon, đưa lá hướng ra phía ánh sáng mặt trời soi thấy có quầng sáng màu vàng tươi bao bọc xung quanh vết bệnh."
        elif 'tuyến trùng' in ten_benh or 'meloidogyne' in pathogen_sci:
            disease['kiem_tra_thuc_dia'] = "Nhổ nhẹ cụm rễ con rũ sạch đất: bóp và quan sát thấy rễ phình to từng nốt sần tròn cục bộ như chuỗi hạt cườm, các đầu chóp rễ tơ bị cụt nghẽn không phân nhánh."
        elif 'rầy' in ten_benh or 'rệp' in ten_benh or 'bọ trĩ' in ten_benh or 'nhện đỏ' in ten_benh:
            disease['kiem_tra_thuc_dia'] = "Lấy một tờ giấy trắng đặt dưới tán đọt non rồi gõ nhẹ cành 3 cái: dùng kính lúp soi thấy các chấm li ti màu đỏ/vàng bò nhanh trên mặt giấy; mặt dưới lá non có tơ mịn giăng mờ."
        elif 'khảm' in ten_benh or 'virus' in ten_benh or 'xoăn' in ten_benh:
            disease['kiem_tra_thuc_dia'] = "Soi phiến lá non ngược sáng: các mảng xanh đậm và vàng nhạt xen kẽ loang lổ bất quy tắc, sờ phiến lá thấy dày cộm giòn cứng, mép lá cong queo dị dạng."
        else:
            disease['kiem_tra_thuc_dia'] = f"Kiểm tra thực địa trên {crop_name}: dùng ngón tay bóp kiểm tra độ ẩm mềm của mô vết bệnh, cạo nhẹ lớp biểu bì quan sát màu sắc mạch dẫn bên trong và ngửi kiểm tra mùi chua men hoặc mùi thối vi khuẩn."
        fixes.append(f"Chuẩn hóa bài test thực địa xúc giác/khứu giác cho '{disease.get('ten_benh')}'")

    return fixes

def enrich_double_diagnosis(disease: Dict[str, Any], crop_name: str) -> List[str]:
    fixes = []
    diag = clean_text(disease.get('phan_biet_chan_doan_kep', ''))
    diag_lower = diag.lower()

    ten_benh = clean_text(disease.get('ten_benh', '')).lower()
    tac_nhan = disease.get('tac_nhan', {})
    pathogen_sci = ''
    if isinstance(tac_nhan, dict):
        pathogen_sci = clean_text(tac_nhan.get('ten_khoa_hoc', '')).lower()

    contrast_keywords = ['khác với', 'phân biệt', 'dễ nhầm', 'dễ lầm', 'so với', 'tránh nhầm', 'đối chiếu']
    has_contrast = any(k in diag_lower for k in contrast_keywords)

    if len(diag) < 30 or not has_contrast:
        if 'vàng lá gân xanh' in ten_benh or 'hlb' in ten_benh or 'liberibacter' in pathogen_sci:
            disease['phan_biet_chan_doan_kep'] = "Phân biệt với Thiếu kẽm (vết vàng đối xứng đều hai bên gân phụ, lá không biến dạng tai thỏ) và Vàng lá thối rễ (vàng đồng đều cả gân lẫn phiến lá trên toàn tán, rễ tơ bị thối tuột vỏ mùi chua, trong khi HLB rễ ban đầu vẫn bình thường)."
        elif 'vàng lá thối rễ' in ten_benh or ('thối rễ' in ten_benh and 'vàng' in ten_benh):
            disease['phan_biet_chan_doan_kep'] = "Phân biệt với Bệnh vàng lá gân xanh HLB (HLB vàng lốm đốm bất đối xứng, gân xanh nổi bần, rễ chưa thối) và Vàng lá do ngập úng sinh lý (vàng úa đột ngột đồng loạt cả vườn sau mưa bão, không lây lan theo từng cây)."
        elif 'thán thư' in ten_benh or 'colletotrichum' in pathogen_sci:
            disease['phan_biet_chan_doan_kep'] = "Phân biệt với Hiện tượng cháy nắng sinh lý (vết cháy khô màu rơm chỉ xuất hiện ở các vị trí tiếp xúc trực tiếp với nắng gắt, mép vết cháy không có viền nâu đỏ đồng tâm và không lây lan khi gặp mưa) và Bệnh đốm mắt cua (vết bệnh nhỏ tròn tâm xám trắng)."
        elif 'héo rũ' in ten_benh or 'ralstonia' in pathogen_sci:
            disease['phan_biet_chan_doan_kep'] = "Phân biệt với Bệnh héo vàng do nấm Fusarium (héo vàng nấm thì lá úa vàng dần từ dưới gốc lên ngọn kéo dài nhiều tuần, mạch dẫn khô nâu; còn héo rũ vi khuẩn thì toàn bộ lá vẫn xanh tươi nhưng rũ gục đột ngột trong 1-2 ngày, nhúng gốc vào nước có dòng mủ trắng đục rỉ ra)."
        elif 'xì mủ' in ten_benh or 'chảy nhựa' in ten_benh or 'phytophthora' in pathogen_sci:
            disease['phan_biet_chan_doan_kep'] = "Phân biệt với Hiện tượng chảy gôm sinh lý (chảy gôm sinh lý nhựa trong suốt hoặc vàng hổ phách không mùi hôi, do bón thừa đạm hoặc biến động độ ẩm đất; còn xì mủ Phytophthora mạch gỗ nâu đỏ thối nhũn và bốc mùi chua men ủng)."
        elif 'khảm' in ten_benh or 'virus' in ten_benh:
            disease['phan_biet_chan_doan_kep'] = "Phân biệt với Ngộ độc thuốc trừ cỏ / hóa chất (ngộ độc hóa chất thường biến dạng xoăn lá đồng loạt cả cành non lẫn già trên diện rộng không có triệu chứng loang lổ mảng xanh vàng bất quy tắc đặc thù của virus)."
        elif 'loét' in ten_benh or 'canker' in ten_benh or 'xanthomonas' in pathogen_sci:
            disease['phan_biet_chan_doan_kep'] = "Phân biệt với Bệnh sẹo ghẻ nhám Elsinoë (sẹo nhám nhô cao màu xám nâu không có quầng vàng bao quanh, không ăn sâu làm nứt lõm mô vỏ quả như loét vi khuẩn Xanthomonas)."
        elif 'phấn trắng' in ten_benh:
            disease['phan_biet_chan_doan_kep'] = "Phân biệt với Bệnh muội đen bồ hóng (bồ hóng là lớp màng đen bám ngoài bề mặt do nấm hoại sinh trên dịch bài tiết của rệp sáp, cạo bong mảng mỏng ra được; còn phấn trắng ăn sâu bám màng trắng mịn làm phiến lá biến dạng quăn queo)."
        elif 'tuyến trùng' in ten_benh:
            disease['phan_biet_chan_doan_kep'] = "Phân biệt với Nốt sần vi khuẩn nốt sần Rhizobium cộng sinh nốt rễ (nốt sần Rhizobium bóc ra bên trong màu hồng hoặc đỏ nhạt, rễ vẫn mập khỏe tươi xốp; còn nốt sần tuyến trùng làm rễ biến dạng thâm đen, thối đầu chóp rễ)."
        else:
            disease['phan_biet_chan_doan_kep'] = f"Phân biệt với các rối loạn dinh dưỡng sinh lý (thiếu vi lượng, ngộ độc phèn mặn) và các bệnh nấm đốm lá khác: bệnh lý có vết hoại tử lây lan theo vòng tròn đồng tâm hoặc viền quầng vàng, không phân bố đối xứng như tổn thương cơ học."
        fixes.append(f"Bổ sung bóc tách chẩn đoán kép đối chiếu cho '{disease.get('ten_benh')}'")

    return fixes

def audit_and_repair_crop(crop: Dict[str, Any]) -> Tuple[int, List[str]]:
    crop_name = crop.get('name_vi', 'Cây trồng')
    total_fixes = 0
    fix_log = []

    diseases = crop.get('danh_sach_benh', [])
    if not isinstance(diseases, list):
        return 0, []

    for d in diseases:
        if not isinstance(d, dict):
            continue

        # 1. Banned chemicals check & removal
        chem_fixes = check_and_fix_banned_chemicals(d)
        if chem_fixes:
            total_fixes += len(chem_fixes)
            fix_log.extend(chem_fixes)

        # 2. VietGAP biological protocol verification & enrichment
        bio_fixes = enrich_vietgap_bio_protocol(d, crop_name)
        if bio_fixes:
            total_fixes += len(bio_fixes)
            fix_log.extend(bio_fixes)

        # 3. Practical field tests verification & enrichment
        field_fixes = enrich_practical_field_test(d, crop_name)
        if field_fixes:
            total_fixes += len(field_fixes)
            fix_log.extend(field_fixes)

        # 4. Double diagnosis contrast verification & enrichment
        diag_fixes = enrich_double_diagnosis(d, crop_name)
        if diag_fixes:
            total_fixes += len(diag_fixes)
            fix_log.extend(diag_fixes)

    return total_fixes, fix_log

def audit_file(filepath: str) -> Dict[str, Any]:
    if not os.path.exists(filepath):
        return {'status': 'error', 'message': f'File not found: {filepath}'}

    print(f"\n[Auditor 5] Đang rà soát và kiểm định tệp: {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        try:
            crops = json.load(f)
        except Exception as e:
            return {'status': 'error', 'message': f'Lỗi parse JSON: {e}'}

    if not isinstance(crops, list):
        return {'status': 'error', 'message': 'Dữ liệu không phải là danh sách (Array)'}

    total_crops = len(crops)
    total_diseases = sum(len(c.get('danh_sach_benh', [])) for c in crops if isinstance(c, dict))
    total_fixes = 0
    all_fix_logs = []

    for idx, crop in enumerate(crops):
        if not isinstance(crop, dict):
            continue
        fixes, logs = audit_and_repair_crop(crop)
        total_fixes += fixes
        all_fix_logs.extend(logs)

    # Save back repaired JSON file
    if total_fixes > 0:
        print(f"[Auditor 5] Phát hiện và tự động sửa chữa {total_fixes} điểm chưa đạt chuẩn.")
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(crops, f, ensure_ascii=False, indent=2)
        print(f"[Auditor 5] Đã lưu file đã chuẩn hóa thành công: {filepath}")
    else:
        print(f"[Auditor 5] Tuyệt vời! 100% bản ghi đã đạt chuẩn VietGAP sinh học & thực địa.")

    return {
        'status': 'success',
        'filepath': filepath,
        'total_crops': total_crops,
        'total_diseases': total_diseases,
        'total_fixes': total_fixes,
        'fix_logs': all_fix_logs[:20]  # sample of first 20 fixes
    }

if __name__ == '__main__':
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_files = [
        os.path.join(root_dir, 'src', 'data', 'vietnam_plant_pathology_400_crops.json'),
        os.path.join(root_dir, 'src', 'data', 'vinh_long_plant_pathology_100_crops.json'),
        os.path.join(root_dir, 'src', 'data', 'vietnam_plant_pathology_1000_crops.json'),
        os.path.join(root_dir, '..', 'src', 'data', 'vietnam_plant_pathology_1000_crops.json'),
    ]

    for tf in target_files:
        if os.path.exists(tf):
            res = audit_file(tf)
            print(f"Kết quả {os.path.basename(tf)}: Crops={res.get('total_crops')}, Diseases={res.get('total_diseases')}, Fixes={res.get('total_fixes')}")
