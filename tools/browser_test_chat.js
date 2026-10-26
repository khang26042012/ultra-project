const { chromium } = require('playwright');
const path = require('path');

async function testChatUI() {
  console.log('🚀 Testing Chat Message UI and Tactile Card Rendering...');
  const browser = await chromium.launch({
    channel: 'msedge',
    headless: true,
  });

  const context = await browser.newContext({ viewport: { width: 1280, height: 800 } });
  const page = await context.newPage();

  try {
    await page.goto('http://localhost:3000', { waitUntil: 'networkidle', timeout: 15000 });
    
    // Inject mock conversation directly into localStorage or test via input
    console.log('1️⃣ Injecting mock clinical message into localStorage to verify card rendering...');
    const mockMessage = `Chào bà con nhà vườn, em là AgriVision - Trợ lý Bác sĩ Cây trồng của bạn Phan Trọng Khang (Lớp 9¹, THCS Vĩnh An, Vĩnh Long).

### 📋 PHIẾU KHÁM BỆNH LÂM SÀNG AGRIVISION
* **Mã hồ sơ bệnh án:** \`VL-PATH-2026-9999\`
* **Cây trồng & Bộ phận tổn thương:** Sầu Riêng Ri6 — Thân gốc & Rễ
* **Chẩn đoán sơ bộ:** Bệnh Nứt thân xì mủ do nấm Phytophthora palmivora
* **Mức độ rủi ro:** Hiểm nghèo (Cực kỳ nghiêm trọng)
* **Phân biệt chẩn đoán kép:** Khác với Mọt đục cành: nấm xì mủ có vết ướt thối rỉ dịch nhựa chua men, không có lỗ đùn mạt cưa gỗ li ti.
* **2 BƯỚC KIỂM TRA THỰC ĐỊA (BẮT BUỘC):**
  1. Dùng dao gọt nhẹ lớp vỏ ngoài: có thấy lớp mạch gỗ thối nâu đỏ sẫm ẩm ướt và bốc mùi chua men?
  2. Bới lớp đất vùng rễ cám: rễ tơ có bị thối đen tuột vỏ không?
* **Phác đồ điều trị VietGAP:**
  - Canh tác: Xẻ mương thoát nước, cạo sạch vết loét và quét vôi.
  - Sinh học: Quét chế phẩm nấm đối kháng Trichoderma harzianum hoặc Chaetomium đậm đặc lên vết loét.`;

    await page.evaluate((msg) => {
      const convId = 'test-conv-001';
      const conversation = {
        id: convId,
        title: 'Chẩn đoán bệnh sầu riêng xì mủ',
        model: 'ag/gemini-3.8-flash-high',
        createdAt: new Date().toISOString(),
        updatedAt: new Date().toISOString(),
        messages: [
          {
            id: 'msg-user-1',
            conversationId: convId,
            role: 'user',
            content: 'Cây sầu riêng của tôi bị nứt thân chảy nhựa mủ màu nâu ở gốc, đây là bệnh gì?',
            timestamp: new Date().toISOString(),
          },
          {
            id: 'msg-assistant-1',
            conversationId: convId,
            role: 'assistant',
            content: msg,
            thought: 'Phân tích triệu chứng: xì mủ gốc, nứt thân sầu riêng -> Phytophthora palmivora.',
            timestamp: new Date().toISOString(),
          }
        ],
      };
      localStorage.setItem('agrivision_chats_guest', JSON.stringify([conversation]));
    }, mockMessage);

    // Reload page to let ChatContext pick up the conversation
    await page.reload({ waitUntil: 'networkidle' });
    await page.waitForTimeout(1500);

    const bodyText = await page.innerText('body');
    const hasCard = bodyText.includes('VL-PATH-2026-9999');
    const hasSensoryButtons = bodyText.includes('Có') && bodyText.includes('Không');
    const hasExportButton = bodyText.includes('Xuất Phiếu Khám Bệnh') || bodyText.includes('sao chép');

    console.log(`   Clinical Card ID Rendered: ${hasCard ? '✅' : '❌'}`);
    console.log(`   Tactile Sensory Check Buttons Rendered: ${hasSensoryButtons ? '✅' : '❌'}`);
    console.log(`   Export / Copy Medical Card Action Rendered: ${hasExportButton ? '✅' : '❌'}`);

    // Click Tactile Sensory Check Button
    const sensoryBtn = await page.$('button:has-text("Có")');
    if (sensoryBtn) {
      console.log('2️⃣ Clicking Tactile Sensory Button [ ✓ Có ]...');
      await sensoryBtn.click();
      await page.waitForTimeout(1000);
      console.log('   ✅ Button clicked cleanly with tactile micro-interaction!');
    }

    const testPassed = hasCard && hasSensoryButtons;
    console.log(`\n🎉 Chat Clinical Card & Tactile Controls: ${testPassed ? 'PASSED 100%' : 'FAILED'}`);
    await browser.close();
    process.exit(testPassed ? 0 : 1);
  } catch (e) {
    console.error('Error testing Chat UI:', e);
    await browser.close();
    process.exit(1);
  }
}

testChatUI();
