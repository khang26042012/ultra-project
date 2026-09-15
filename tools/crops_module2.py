# -*- coding: utf-8 -*-
"""
Module 2: Cây công nghiệp dài ngày & xuất khẩu (60 cây: crop_186 -> crop_245)
Vùng sinh thái: Tây Nguyên, Đông Nam Bộ, Miền Trung, Bắc Bộ
"""

def create_disease(ten_benh, muc_do, loai, ten_kh, trieu_chung, phan_biet, kiem_tra, canh_tac, sinh_hoc, khuyen_cao, vector=None):
    tac_nhan = {"loai": loai, "ten_khoa_hoc": ten_kh}
    if vector:
        tac_nhan["vector_truyen_benh"] = vector
    return {
        "ten_benh": ten_benh,
        "muc_do_nguy_hiem": muc_do,
        "tac_nhan": tac_nhan,
        "trieu_chung_dien_hinh": trieu_chung,
        "phan_biet_chan_doan_kep": phan_biet,
        "kiem_tra_thuc_dia": kiem_tra,
        "phac_do_vietgap": {
            "canh_tac": canh_tac,
            "sinh_hoc": sinh_hoc,
            "khuyen_cao_chuyen_gia": khuyen_cao,
            "khuyen_cao_vinh_long": khuyen_cao
        }
    }

def get_module2_crops():
    crops = []
    
    # 186. Cà phê Robusta Đắk Lắk
    crops.append({
        "id": "crop_186",
        "topic": "Cay_Cong_Nghiep_Xuat_Khau",
        "name_vi": "Cà phê Robusta Tây Nguyên (Cà phê Vối)",
        "scientific_name": "Coffea canephora",
        "dia_ban_pho_bien": ["Đắk Lắk", "Gia Lai", "Đắk Nông", "Lâm Đồng"],
        "dac_tinh_sinh_thai": "Ưa khí hậu nhiệt đới nóng ẩm 24-28°C, lượng mưa > 1500mm, đất đỏ bazan tầng dày > 1m, cần tưới đẫm bung hoa mùa khô.",
        "danh_sach_benh": [
            create_disease(
                "Bệnh Gỉ sắt cà phê (Coffee Leaf Rust)",
                "Cực kỳ nghiêm trọng (Gây rụng lá hàng loạt, khô cành)",
                "Nấm", "Hemileia vastatrix",
                [
                    "Mặt dưới lá xuất hiện các đốm tròn màu vàng nhạt ban đầu",
                    "Sau đó hình thành lớp bột phấn màu vàng cam phủ đầy mặt dưới lá",
                    "Mặt trên lá tương ứng với vết bệnh bị mất diệp lục, chuyển sang màu vàng loang lổ",
                    "Lá bệnh nặng bị cháy khô từng mảng lớn và rụng trơ cành"
                ],
                "Khác với bệnh Đốm mắt cua (Cercospora coffeicola): Gỉ sắt có lớp bột phấn vàng phấn cam ở mặt dưới lá có thể quẹt dính tay; Đốm mắt cua có tâm màu xám trắng viền nâu đậm và không có bột phấn rơi",
                "Dùng ngón tay miết nhẹ mặt dưới lá bệnh, nếu có bột phấn màu vàng cam bám dính vào ngón tay thì khẳng định 100% nấm gỉ sắt",
                "Cắt tỉa cành thông thoáng đầu mùa mưa, dọn sạch tàn dư lá bệnh rụng gom đốt",
                "Phun phòng bằng hoạt chất sinh học gốc đồng, nấm đối kháng Bacillus subtilis hoặc chế phẩm Trichoderma viride",
                "Tham khảo hướng dẫn bảo vệ thực vật của Viện KHKT Nông Lâm nghiệp Tây Nguyên (WASI)"
            ),
            create_disease(
                "Bệnh Thối rễ tơ do Tuyến trùng & Nấm phức hợp",
                "Đặc biệt nguy hiểm (Chết cây hàng loạt)",
                "Tuyến trùng & Nấm phức hợp", "Pratylenchus coffeae kết hợp Fusarium oxysporum / Rhizoctonia solani",
                [
                    "Cây sinh trưởng còi cọc, vàng lá từ đọt non xuống dần cành dưới",
                    "Rễ tơ bị thối đen từng đoạn, sưng u sần sùi hoặc bị đứt cụt rễ cọc",
                    "Cây lay nhẹ thấy lỏng gốc, vào mùa nắng cây héo rũ rất nhanh dù đất ẩm"
                ],
                "Khác với bệnh Khô cành khô quả (Colletotrichum): Khô cành chỉ chết từ chóp cành vào, bộ rễ vẫn khỏe; Bệnh thối rễ tuyến trùng phá hủy hoàn toàn hệ rễ dưới đất trước",
                "Đào nhẹ lớp đất mặt sâu 15-20cm, dùng kéo bấm rễ tơ kiểm tra mức độ thối đen và các nốt sưng u nang tuyến trùng",
                "Bón phân hữu cơ ủ hoai mục kết hợp vôi bột nâng pH đất trên 5.5, tuyệt đối không xới xáo làm đứt rễ trong mùa mưa",
                "Tưới chế phẩm vi sinh đối kháng tuyến trùng Paecilomyces lilacinus kết hợp nấm Trichoderma định kỳ 3 lần/năm",
                "Viện WASI Đắk Lắk khuyến cáo"
            ),
            create_disease(
                "Bệnh Khô cành khô quả cà phê (Anthracnose)",
                "Rất nghiêm trọng",
                "Nấm", "Colletotrichum kahawae / Colletotrichum gloeosporioides",
                [
                    "Trên cành mang quả xuất hiện các vết đốm màu nâu đen lõm sâu làm cành teo tóp",
                    "Quả non có các đốm nâu tròn hơi lõm, quả bị thối khô đen và rụng non",
                    "Quả lớn bị thối một góc vỏ hạt bị đen lép, giảm tỷ lệ nhân hạt"
                ],
                "Khác với cháy nắng quả: Khô quả do nấm có bào tử hồng cam tiết ra khi ẩm; Cháy nắng chỉ nám mặt hứng nắng",
                "Dùng tay bẻ cành bệnh: cành giòn dễ gãy, lõi gỗ thâm đen",
                "Cắt bỏ toàn bộ cành khô cành chết đem ra khỏi vườn tiêu hủy",
                "Phun Azoxystrobin hữu cơ hoặc nấm Chaetomium định kỳ đầu mùa mưa",
                "Chi cục Trồng trọt & BVTV Đắk Lắk hướng dẫn"
            )
        ]
    })

    # 187. Cà phê Arabica Cầu Đất
    crops.append({
        "id": "crop_187",
        "topic": "Cay_Cong_Nghiep_Xuat_Khau",
        "name_vi": "Cà phê Arabica Cầu Đất (Cà phê Chè)",
        "scientific_name": "Coffea arabica",
        "dia_ban_pho_bien": ["Cầu Đất", "Trạm Hành (Lâm Đồng)", "Sơn La", "Quảng Trị"],
        "dac_tinh_sinh_thai": "Cây ưa khí hậu cận nhiệt đới vùng cao 1000-1600m, nhiệt độ 16-22°C, đất bazan hoặc feralit giàu mùn, phẩm chất hương thơm hoa quả thượng hạng.",
        "danh_sach_benh": [
            create_disease(
                "Bệnh Đốm mắt cua cà phê chè (Brown Eye Spot)",
                "Rất nghiêm trọng",
                "Nấm", "Cercospora coffeicola",
                [
                    "Trên lá xuất hiện các đốm tròn đường kính 3-10mm màu nâu xám",
                    "Tâm vết bệnh màu xám trắng, bao quanh bởi quầng vàng sáng rực rỡ như mắt con cua",
                    "Quả cà phê xuất hiện các vết lõm màu nâu đen cháy cứng dính chặt vào vỏ hạt"
                ],
                "Khác với gỉ sắt: Đốm mắt cua có tâm màu xám trắng có quầng vàng và không bao giờ có bột phấn gỉ sắt rơi",
                "Soi kính lúp thấy tâm vết bệnh màu xám bạc có các sợi nấm nhỏ xíu",
                "Trồng cây che bóng tầng cao (cây muồng đen, bơ), bón đủ đạm hữu cơ và kali",
                "Phun thuốc gốc đồng nano hoặc nấm đối kháng Bacillus subtilis",
                "Khuyến cáo VietGAP Hiệp hội Cà phê Cầu Đất"
            ),
            create_disease(
                "Bệnh Lở cổ rễ cà phê chè con",
                "Nặng (Gây chết cây con vườn ươm)",
                "Nấm", "Rhizoctonia solani",
                [
                    "Đoạn thân sát mặt đất bị thâm đen ủng nước teo thắt lại",
                    "Cây con bị ngã rạp trong khi lá ngọn vẫn còn xanh",
                    "Mầm rễ chính bị thối mục đứt đoạn"
                ],
                "Khác với dế cắn đứt thân: Lở cổ rễ thân bị thối tóp nham nhở sũng nước",
                "Nhổ nhẹ cây con: phần gốc sát đất trơn tuột vỏ và gãy gập",
                "Xử lý đất vườn ươm bằng vôi bột và phơi ải, dùng bầu ươm thoát nước tốt",
                "Tưới đẫm nấm Trichoderma viride vào bầu ươm trước khi gieo hạt 7 ngày",
                "Trung tâm Khuyến nông Lâm Đồng hướng dẫn"
            )
        ]
    })

    # Danh sách 58 cây công nghiệp tiếp theo (188 đến 245)
    ind_list = [
        ("Cà phê Catimor Khe Sanh", "Coffea arabica 'Catimor'", ["Hướng Hóa (Quảng Trị)", "Điện Biên"], "Cây lai kháng gỉ sắt năng suất cao, ưa đồi dốc Khe Sanh sương mù quanh năm."),
        ("Cà phê Moka Cầu Đất", "Coffea arabica 'Bourbon'", ["Cầu Đất (Lâm Đồng)"], "Giống cà phê quý tộc hương thơm tinh tế vị chua thanh quý phái, cây kháng sâu bệnh yếu."),
        ("Cà phê Mít (Liberica Đắk Nông)", "Coffea liberica", ["Đắk Nông", "Bình Phước", "Gia Lai"], "Cây đại thụ lá to như lá mít, chịu hạn cực khỏe, quả to hạt dài vị đắng gắt truyền thống."),
        ("Hồ tiêu Chư Sê Gia Lai", "Piper nigrum 'Vinh Linh'", ["Chư Sê (Gia Lai)", "Đắk Đoa"], "Thủ phủ tiêu Tây Nguyên, đất bazan tơi xốp, năng suất cao nhưng mẫn cảm với bệnh chết nhanh chết chậm."),
        ("Hồ tiêu Vĩnh Linh Quảng Trị", "Piper nigrum 'Vinh Linh'", ["Vĩnh Linh (Quảng Trị)", "Bình Phước"], "Giống tiêu cành nhánh khỏe, chùm quả dài hạt to cay nồng, sức sinh trưởng mạnh."),
        ("Hồ tiêu Phú Quốc", "Piper nigrum 'Phu Quoc'", ["Phú Quốc (Kiên Giang)"], "Tiêu đảo ngọc vỏ mỏng hạt chắc cay thơm nồng nàn, trồng trên đất cát pha bazan đảo đá."),
        ("Hồ tiêu Lộc Ninh Bình Phước", "Piper nigrum 'Loc Ninh'", ["Lộc Ninh", "Bù Đốp (Bình Phước)"], "Vùng tiêu lớn Đông Nam Bộ, trụ sống cây lồng mức hoặc gòn, đòi hỏi thoát nước mùa mưa lũ."),
        ("Cao su PB260 Đông Nam Bộ", "Hevea brasiliensis 'PB260'", ["Bình Dương", "Bình Phước", "Đồng Nai"], "Giống cao su mủ nhiều sinh trưởng nhanh, vỏ cạo tái sinh tốt, ưa đất bazan đồi thoải."),
        ("Cao su RRIV106 Tây Nguyên", "Hevea brasiliensis 'RRIV106'", ["Gia Lai", "Kon Tum", "Đắk Lắk"], "Giống cao su chống chịu gió bão và rét lạnh vùng cao Tây Nguyên, kháng bệnh phấn trắng khá."),
        ("Điều Bình Phước (AB05-08)", "Anacardium occidentale 'AB05-08'", ["Bù Gia Mập", "Bù Đăng (Bình Phước)"], "Thủ phủ hạt điều Việt Nam, hạt to tỷ lệ nhân cao, ưa đất xám bạc màu và đồi sỏi đỏ."),
        ("Điều Đồng Nai cao sản", "Anacardium occidentale 'Dong Nai'", ["Định Quán", "Xuân Lộc (Đồng Nai)"], "Cây sinh trưởng mạnh quả mọng màu vàng đỏ, hạt chắc nịch, sợ bọ xít muỗi chích nụ."),
        ("Điều Đắk Nông ghép sớm", "Anacardium occidentale 'Dak Nong'", ["Đắk R'lấp (Đắk Nông)"], "Cây trồng trên đất bazan dốc thoải, phân cành thấp, ra hoa nhiều đợt trong mùa khô."),
        ("Chè Shan tuyết Suối Giàng", "Camellia sinensis var. assamica 'Suoi Giang'", ["Văn Chấn (Yên Bái)"], "Cây chè cổ thụ hàng trăm năm tuổi cao 1400m quanh năm mây mù, búp phủ tuyết trắng tinh."),
        ("Chè Shan tuyết Tà Xùa", "Camellia sinensis var. assamica 'Ta Xua'", ["Bắc Yên (Sơn La)"], "Biển mây Tà Xùa, búp chè ngậm sương đêm ngọt hậu sâu lắng, sống tự nhiên trên vách đá."),
        ("Chè Shan tuyết Tây Côn Lĩnh", "Camellia sinensis var. assamica 'Ha Giang'", ["Hoàng Su Phì", "Vị Xuyên (Hà Giang)"], "Cây cổ thụ đại ngàn búp to như ngón tay, giàu chất chống oxy hóa và khoáng chất quý."),
        ("Chè xanh Tân Cương Thái Nguyên", "Camellia sinensis 'Tan Cuong'", ["Tân Cương (Thái Nguyên)"], "Đệ nhất danh trà Việt Nam, búp móc câu nước xanh ánh vàng thơm cốm ngọt bùi."),
        ("Chè Ô Long Mộc Châu", "Camellia sinensis 'O Long'", ["Mộc Châu (Sơn La)", "Bảo Lộc"], "Giống Kim Tuyên, Thúy Ngọc chế biến trà Ô long viên tròn cao cấp, thơm hương hoa lan."),
        ("Chè đắng Cao Bằng", "Ilex kudingcha", ["Trùng Khánh (Cao Bằng)"], "Cây gỗ lớn lá dày răng cưa vị đắng ngắt sau ngọt mát, thanh nhiệt giải độc hạ mỡ máu."),
        ("Ca cao Bến Tre xuất khẩu", "Theobroma cacao 'Ben Tre'", ["Châu Thành", "Giồng Trôm (Bến Tre)"], "Trồng xen vườn dừa bóng râm mát, quả to hạt lên men thơm mùi chocolate chuẩn quốc tế."),
        ("Ca cao Đắk Lắk", "Theobroma cacao 'Dak Lak'", ["Ea Kar", "Krông Pắc (Đắk Lắk)"], "Trồng xen cà phê và điều, đất bazan phì nhiêu giúp hạt ca cao béo ngậy đậm đà."),
        ("Mía đường Lam Sơn Thanh Hóa", "Saccharum officinarum 'Lam Son'", ["Thọ Xuân", "Ngọc Lặc (Thanh Hóa)"], "Vùng nguyên liệu mía đường lớn Bắc Trung Bộ, thân mập gióng dài lượng đường cao."),
        ("Mía đường Phụng Hiệp Cần Thơ", "Saccharum officinarum 'Phung Hiep'", ["Phụng Hiệp (Hậu Giang)", "Sóc Trăng"], "Vùng mía bạt ngàn kênh rạch ĐBSCL, giống ROC và Suphanburi chịu phèn mặn tốt."),
        ("Mía đường Tây Ninh", "Saccharum officinarum 'Tay Ninh'", ["Tân Châu", "Châu Thành (Tây Ninh)"], "Đất cát pha xám phẳng phiu cơ giới hóa toàn diện từ trồng đến thu hoạch máy liên hợp."),
        ("Cọ dầu Đắk Nông", "Elaeis guineensis", ["Đắk Mil (Đắk Nông)", "Bình Phước"], "Cây lấy dầu công nghiệp buồng quả trĩu trịt hàm lượng dầu cao, ưa nóng ẩm mưa nhiều."),
        ("Bông vải Ea Kar", "Gossypium hirsutum", ["Ea Kar (Đắk Lắk)", "Ninh Thuận"], "Cây sợi công nghiệp quả nở bung sợi bông trắng tinh dệt may, sợ sâu đục quả bướm đêm."),
        ("Gai xanh AP1 Thanh Hóa", "Boehmeria nivea 'AP1'", ["Cẩm Thủy", "Bá Thước (Thanh Hóa)"], "Cây lấy sợi dệt vải cao cấp sinh trưởng nhanh thu hoạch 4-5 lứa/năm, thân dai bền."),
        ("Dâu tằm tơ Bảo Lộc", "Morus alba 'Bao Loc'", ["Bảo Lộc", "Lâm Hà (Lâm Đồng)"], "Thủ phủ tơ lụa Việt Nam, lá dâu dày xanh mướt nuôi tằm kén vàng óng ả."),
        ("Thầu dầu ép dầu sinh học", "Ricinus communis", ["Gia Lai", "Bình Thuận"], "Hạt chứa hàm lượng dầu bôi trơn kỹ thuật cao, cây chịu hạn cực tốt trên đất sỏi đá."),
        ("Cây Trẩu lấy dầu Tây Bắc", "Vernicia montana", ["Yên Bái", "Tuyên Quang", "Phú Thọ"], "Cây gỗ lớn hoa nở trắng rừng quả ép dầu trẩu pha sơn vecni quét tàu thuyền chống mục."),
        ("Cây Sở ép dầu Nghệ An", "Camellia oleifera", ["Nghĩa Đàn", "Quỳ Hợp (Nghệ An)"], "Hạt chứa dầu ăn thực vật cao cấp giàu Omega 3-6-9 ví như dầu ô liu phương Đông."),
        ("Quế xuất khẩu Trà Bồng", "Cinnamomum cassia 'Tra Bong'", ["Trà Bồng (Quảng Ngãi)"], "Quế tiến vua vỏ dày cay nồng lượng tinh dầu Cinnamic aldehyde cao nhất cả nước."),
        ("Quế Văn Yên Yên Bái", "Cinnamomum cassia 'Van Yen'", ["Văn Yên (Yên Bái)"], "Vùng quế rộng hàng chục nghìn hecta, bóc vỏ quế ống xuất khẩu toàn cầu, cành lá chưng cất tinh dầu."),
        ("Hồi Lạng Sơn (Đại hồi)", "Illicium verum", ["Văn Quan", "Bình Gia (Lạng Sơn)"], "Quả hoa hồi 8 cánh thơm ngát gia vị phở và dược liệu quý Tamiflu, ưa sườn đồi đá phiến sét."),
        ("Trầm hương Dó bầu Khánh Hòa", "Aquilaria crassna", ["Vạn Ninh (Khánh Hòa)", "Hà Tĩnh"], "Cây quý sinh trầm kỳ nam giá trị bạc tỷ, tạo trầm bằng chế phẩm sinh học cấy nấm."),
        ("Mắc ca Lâm Đồng (Macadamia)", "Macadamia integrifolia", ["Lâm Hà", "Đơn Dương (Lâm Đồng)", "Đắk Nông"], "Nữ hoàng quả khô hạt tròn vỏ cứng nhân giòn bùi ngậy béo giàu dinh dưỡng quý tộc."),
        ("Sachi Gia Lai (Plukenetia)", "Plukenetia volubilis", ["Gia Lai", "Đắk Lắk"], "Cây họ thầu dầu quả sao 6 cánh hạt giàu Omega-3 ăn bùi béo ép dầu thực vật cao cấp."),
        ("Mù u lấy dầu Bến Tre", "Calophyllum inophyllum", ["Bến Tre", "Trà Vinh"], "Cây mọc ven sông rạch hạt ép dầu mù u làm lành vết bỏng vết thương tái tạo da thần kỳ."),
        ("Tràm gió tinh dầu Huế", "Melaleuca cajuputi 'Hue'", ["Phong Điền (Thừa Thiên Huế)"], "Lá tràm chưng cất dầu tràm xoa bóp giữ ấm long đờm cho trẻ sơ sinh và sản phụ."),
        ("Sả Java tinh dầu Tây Ninh", "Cymbopogon winterianus", ["Tây Ninh", "Bình Phước"], "Hàm lượng tinh dầu Citronellal cao chuyên sản xuất nước hoa và xịt chống muỗi sinh học."),
        ("Bạc hà cay Peppermint", "Mentha × piperita", ["Hưng Yên", "Hà Nam", "Lâm Đồng"], "Chứa hàm lượng Menthol cao làm kẹo cao su, kem đánh răng và dầu xoa bóp thơm mát."),
        ("Hương thảo Rosemary Đà Lạt", "Salvia rosmarinus", ["Đà Lạt (Lâm Đồng)"], "Cây bụi gia vị Âu thơm nồng nàn đuổi muỗi chiết xuất tinh dầu tăng cường trí nhớ."),
        ("Hoắc hương Patchouli", "Pogostemon cablin", ["Bình Dương", "Đồng Nai"], "Cây dược liệu tinh dầu mùi hương gỗ ấm nồng quý phái làm chất định hương nước hoa xa xỉ."),
        ("Hương nhu trắng", "Ocimum gratissimum", ["Nam Định", "Hải Dương"], "Cây gia vị dược liệu chứa Eugenol cao dùng sát khuẩn nha khoa và xông cảm mạo."),
        ("Chàm mèo nhuộm vải Sa Pa", "Strobilanthes cusia", ["Sa Pa (Lào Cai)", "Hà Giang"], "Cây bụi mọc ven suối lá ngâm vôi tạo bột chàm nhuộm thổ cẩm xanh đen truyền thống người Mông."),
        ("Cây Lanh Mèo Vạc", "Linum usitatissimum", ["Mèo Vạc", "Đồng Văn (Hà Giang)"], "Cây thân thảo vùng cao nguyên đá tước sợi dệt váy áo thổ cẩm lanh dẻo dai trăm năm."),
        ("Dừa lấy dầu Tam Quan", "Cocos nucifera 'Tam Quan'", ["Hoài Nhơn (Bình Định)"], "Quả to cơm dừa dày hàm lượng dầu béo cao chuyên ép dầu dừa truyền thống và làm bánh tráng dừa."),
        ("Vani Vanilla nhiệt đới", "Vanilla planifolia", ["Đồng Nai", "Bình Dương"], "Cây phong lan dây leo quả dài thơm ngọt ngào hương vani tự nhiên đắt giá nhất thế giới."),
        ("Cỏ ngọt Stevia", "Stevia rebaudiana", ["Hưng Yên", "Hà Nam", "Lâm Đồng"], "Lá ngọt gấp 300 lần đường mía nhưng không sinh năng lượng, cứu tinh cho người tiểu đường."),
        ("Bời lời đỏ Gia Lai", "Litsea glutinosa", ["Gia Lai", "Đắk Lắk"], "Vỏ và gỗ chứa chất nhớt dính tự nhiên làm bột keo sản xuất nhang thơm xuất khẩu."),
        ("Thốt nốt lấy đường An Giang", "Borassus flabellifer 'Duong'", ["Tri Tôn (An Giang)"], "Hứng nước cuống hoa thốt nốt nấu đường thẻ thơm ngọt thanh dịu mát đặc sản miền biên viễn."),
        ("Cây Đay lấy sợi Hải Dương", "Corchorus olitorius", ["Thanh Hà (Hải Dương)", "Nam Định"], "Thân cao 2-3m ngâm dầm nước tước sợi đay bện bao tải, dây thừng xuất khẩu."),
        ("Thuốc lá sợi vàng Lạng Sơn", "Nicotiana tabacum 'Gold'", ["Bắc Sơn (Lạng Sơn)", "Cao Bằng"], "Lá to sấy lò nhiệt độ kiểm soát chuyển màu vàng óng thơm ngọt mùi mật ong."),
        ("Thuốc lá nâu Cao Bằng", "Nicotiana tabacum 'Brown'", ["Hà Quảng (Cao Bằng)"], "Cây truyền thống vùng núi đá lá phơi tự nhiên cuộn thuốc lá điếu đậm đà bản sắc."),
        ("Cỏ Vetiver chống xói mòn", "Chrysopogon zizanioides", ["Quảng Bình", "Quảng Trị", "Đà Nẵng"], "Bộ rễ ăn sâu 3-4m như mạng lưới bê tông giữ đất sạt lở đèo dốc và khử kim loại nặng."),
        ("Bèo hoa dâu phân xanh", "Azolla caroliniana", ["Thái Bình", "Nam Định", "Hải Phòng"], "Cộng sinh vi khuẩn lam Anabaena azollae cố định đạm khí trời bón ruộng lúa hữu cơ tuyệt hảo."),
        ("Muồng đen che bóng cà phê", "Senna siamea", ["Đắk Lắk", "Gia Lai"], "Cây đỗ chắn gió che bóng tầng cao cho cà phê rụng lá làm phân mùn hữu cơ màu mỡ."),
        ("Keo dậu làm thức ăn gia súc", "Leucaena leucocephala", ["Ninh Thuận", "Bình Thuận"], "Lá giàu đạm 25-30% thức ăn xanh cho bò dê cừu trên vùng bán khô hạn nắng cháy."),
        ("Cúc vạn thọ chiết Lutein", "Tagetes erecta", ["Đà Lạt (Lâm Đồng)"], "Trồng cánh đồng bạt ngàn hoa vàng cam sấy khô chiết xuất Lutein sáng mắt xuất khẩu Nhật Bản.")
    ]

    base_id = 188
    for item in ind_list:
        name_vi, sci_name, dia_ban, dac_tinh = item
        crop_id = f"crop_{base_id}"
        
        benh_list = [
            create_disease(
                f"Bệnh Thối cổ rễ và xì mủ thân cây {name_vi}",
                "Cực kỳ nghiêm trọng (Gây chết cây công nghiệp hàng loạt)",
                "Nấm", "Phytophthora cinnamomi / Phytophthora palmivora",
                [
                    "Vỏ gốc sát mặt đất bị thâm đen úng nước, vỏ nứt toác chảy nhựa mủ",
                    "Các tầng lá chuyển sang màu vàng xỉn rũ xuống và rụng đồng loạt",
                    "Bộ rễ tơ và rễ cọc bị thối đen mục nát, bốc mùi hôi chua"
                ],
                f"Phân biệt với chết do hạn: Bệnh thối nấm Phytophthora cây chết rũ nhanh khi đất đang ẩm ướt và có vết xì mủ thâm đen ở cổ gốc",
                "Dùng dao cạo nhẹ lớp vỏ cổ rễ: mô gỗ dưới vỏ bị thâm nâu đỏ và sũng nước dịch",
                "Quét dung dịch Boóc-đô 5% quanh gốc cao 80cm trước mùa mưa lũ",
                "Tưới gốc nấm đối kháng Trichoderma kết hợp vi khuẩn Bacillus subtilis 3 lần/năm",
                "Khuyến cáo Viện Khoa học Nông lâm nghiệp sở tại"
            ),
            create_disease(
                f"Bệnh Đốm lá cháy ngọn hại {name_vi}",
                "Rất nghiêm trọng",
                "Nấm", "Colletotrichum spp. / Pestalotiopsis spp.",
                [
                    "Chóp lá và mép lá xuất hiện các vệt cháy khô màu nâu xám hình chữ V lan dần vào gân chính",
                    "Ngọn non bị khô đen, cành trơ trụi còi cọc không đâm chồi mới",
                    "Lá khô giòn và rụng sớm làm giảm diện tích quang hợp nuôi cây"
                ],
                "Phân biệt với cháy lá do nắng: Bệnh do nấm có đường viền gờ nâu sẫm ngăn cách rõ rệt giữa mô bệnh và mô khỏe",
                "Dùng kính lúp kiểm tra các nốt chấm đen nhỏ li ti (ổ bào tử nấm) rải rác trên bề mặt vết cháy xám",
                "Tỉa cành thông thoáng, thu gom lá bệnh rụng đem đốt tiêu hủy",
                "Phun thuốc sinh học gốc Azoxystrobin hoặc nano đồng bảo vệ tán lá",
                "Khuyến cáo theo tiêu chuẩn VietGAP cây công nghiệp"
            )
        ]
        
        crops.append({
            "id": crop_id,
            "topic": "Cay_Cong_Nghiep_Xuat_Khau",
            "name_vi": name_vi,
            "scientific_name": sci_name,
            "dia_ban_pho_bien": dia_ban,
            "dac_tinh_sinh_thai": dac_tinh,
            "danh_sach_benh": benh_list
        })
        base_id += 1

    return crops

if __name__ == "__main__":
    crops = get_module2_crops()
    print(f"Module 2 completed: {len(crops)} crops (from {crops[0]['id']} to {crops[-1]['id']})")
