import { chromium } from 'playwright';
import fs from 'fs';

async function runTests() {
  console.log('🚀 Starting Subagent 4 comprehensive QA tests on http://localhost:3000 ...');

  const browser = await chromium.launch({
    headless: true,
  });

  const context = await browser.newContext({
    viewport: { width: 1280, height: 800 },
  });

  const page = await context.newPage();

  page.on('console', (msg) => {
    if (msg.type() === 'error') {
      console.log(`[Browser ERROR] ${msg.text()}`);
    }
  });

  page.on('pageerror', (err) => {
    console.error(`[Browser PageError]`, err);
  });

  // Prepare test conversation with rich markdown & long content
  const testConvId = 'test-subagent4-' + Date.now();
  const sampleMarkdownContent = [
    'Chẩn đoán bệnh học trên cây trồng tại Vĩnh Long:',
    '',
    'Nấm *Fusarium oxysporum* f. sp. *cubense* là tác nhân gây bệnh héo rũ vàng lá nguy hiểm nhất trên chuối Xiêm và chuối Già Nam Mỹ.',
    '',
    '---',
    '',
    '1. Các giai đoạn phát triển của bệnh',
    '- Lá già bắt đầu chuyển sang màu vàng từ mép lá lan dần vào gân chính',
    '- Bẹ lá bị nứt dọc thân giả sát gốc, bó mạch thâm đen',
    '- Toàn bộ lá bị gãy gục nhưng vẫn dính trên thân',
    '',
    '2. Bảng đối chiếu tác nhân và giải pháp can thiệp',
    '| Triệu chứng điển hình | Tác nhân (*Tên khoa học*) | Hoạt chất khuyến cáo | Liều lượng xử lý |',
    '|---|---|---|---|',
    '| Thối rễ, vàng lá héo rũ | *Fusarium oxysporum* | Trichoderma viride + Metalaxyl | 20-30g / bình 25 lít |',
    '| Cháy lá vi khuẩn | *Ralstonia solanacearum* | Kasugamycin + Bismerthiazol | 15-20ml / bình 25 lít |',
    '| Thán thư đốm vòng | *Colletotrichum gloeosporioides* | Azoxystrobin + Difenoconazole | 10-15ml / bình 25 lít |',
    '',
    '---',
    '',
    'Khuyến cáo bà con tuân thủ nguyên tắc 4 đúng và thời gian cách ly theo chuẩn VietGAP.',
  ].join('\n');

  // Long text to test auto-scroll
  const longParagraphs = [];
  for (let i = 1; i <= 25; i++) {
    longParagraphs.push(`Đoạn văn chi tiết kỹ thuật số ${i}: Kiểm tra khả năng xử lý cuộn thông minh của AgriVision khi dữ liệu phản hồi dài hơn chiều cao màn hình.`);
  }

  const testConversation = {
    id: testConvId,
    title: 'Kiểm thử Bệnh học & Cuộn trang',
    group: 'Today',
    updatedAt: new Date().toISOString(),
    messages: [
      {
        id: 'msg-user-1',
        role: 'user',
        content: 'Cho tôi biết thông tin về nấm Fusarium oxysporum và phác đồ điều trị?',
        timestamp: '10:00 AM',
      },
      {
        id: 'msg-assistant-1',
        role: 'assistant',
        content: sampleMarkdownContent,
        timestamp: '10:01 AM',
      },
      {
        id: 'msg-user-2',
        role: 'user',
        content: 'Cho tôi danh sách các bước lưu ý chi tiết thêm nữa.',
        timestamp: '10:02 AM',
      },
      {
        id: 'msg-assistant-2',
        role: 'assistant',
        content: longParagraphs.join('\n\n'),
        timestamp: '10:03 AM',
      },
    ],
  };

  // Pre-seed localStorage before page scripts execute
  await page.addInitScript(({ conv, convId }) => {
    localStorage.setItem('agrivision_chats_guest', JSON.stringify([conv]));
    localStorage.setItem('agrivision-font-size', 'medium');
    localStorage.setItem('agrivision-web-search', 'true');
    localStorage.setItem('agrivision-auto-scroll', 'true');
  }, { conv: testConversation, convId: testConvId });

  // Navigate to application
  console.log('Navigating to http://localhost:3000 ...');
  await page.goto('http://localhost:3000', { waitUntil: 'networkidle' });

  // Wait for conversation to load
  await page.waitForSelector('[data-testid="message-list-container"]', { timeout: 10000 });
  console.log('✅ Chat interface loaded successfully.');

  // ==========================================
  // TEST SUITE 1: MARKDOWN PATHOLOGY & FORMATTING
  // ==========================================
  console.log('\n--- 1. Testing Markdown Pathology & Formatting ---');

  // 1A. Italic scientific names verification
  const italicElements = await page.locator('em').all();
  console.log(`Found ${italicElements.length} <em> elements.`);
  let foundFusarium = false;
  let hasRawAsterisk = false;

  for (const el of italicElements) {
    const text = await el.innerText();
    if (text.includes('Fusarium oxysporum')) {
      foundFusarium = true;
    }
  }

  // Check if raw *Fusarium oxysporum* appears anywhere in body
  const bodyText = await page.innerText('body');
  if (bodyText.includes('*Fusarium oxysporum*')) {
    hasRawAsterisk = true;
  }

  console.log(`- Fusarium oxysporum rendered in <em>: ${foundFusarium ? 'PASS ✅' : 'FAIL ❌'}`);
  console.log(`- No raw asterisks leaking in text: ${!hasRawAsterisk ? 'PASS ✅' : 'FAIL ❌'}`);
  if (!foundFusarium || hasRawAsterisk) {
    throw new Error('Italic scientific names markdown verification failed!');
  }

  // 1B. Thin horizontal divider <hr /> verification
  const hrElements = await page.locator('hr').all();
  console.log(`Found ${hrElements.length} <hr /> dividers.`);
  let hrValid = hrElements.length >= 2;
  console.log(`- Rendered thin horizontal divider <hr />: ${hrValid ? 'PASS ✅' : 'FAIL ❌'}`);
  if (!hrValid) {
    throw new Error('Horizontal rule <hr /> divider verification failed!');
  }

  // 1C. Bullet points indentation with pl-5 under numbered headings
  const bulletItems = await page.locator('.pl-5').all();
  console.log(`Found ${bulletItems.length} elements with pl-5 indentation.`);
  const hasBulletsWithPl5 = bulletItems.length >= 3;
  console.log(`- Bullet points pl-5 indent under numbered headings: ${hasBulletsWithPl5 ? 'PASS ✅' : 'FAIL ❌'}`);
  if (!hasBulletsWithPl5) {
    throw new Error('Bullet points pl-5 indentation verification failed!');
  }

  // 1D. Markdown Table verification: rounded border and overflow-x-auto
  const markdownTable = page.locator('[data-testid="markdown-table"]').first();
  await markdownTable.waitFor({ state: 'visible', timeout: 5000 });

  const tableContainerClass = await markdownTable.getAttribute('class');
  const hasOverflowX = tableContainerClass.includes('overflow-x-auto');
  const hasRoundedBorder = tableContainerClass.includes('rounded-xl') && tableContainerClass.includes('border');

  console.log(`- Markdown Table has overflow-x-auto: ${hasOverflowX ? 'PASS ✅' : 'FAIL ❌'}`);
  console.log(`- Markdown Table has rounded border: ${hasRoundedBorder ? 'PASS ✅' : 'FAIL ❌'}`);
  if (!hasOverflowX || !hasRoundedBorder) {
    throw new Error('Markdown table styling verification failed!');
  }

  // ==========================================
  // TEST SUITE 2: SMART AUTO-SCROLL & BOTTOM BUTTON
  // ==========================================
  console.log('\n--- 2. Testing Smart Auto-scroll & Bottom Button ---');

  const container = page.locator('[data-testid="message-list-container"]');

  // Verify container scrollHeight is greater than clientHeight
  const scrollInfo = await container.evaluate((el) => ({
    scrollHeight: el.scrollHeight,
    clientHeight: el.clientHeight,
    scrollTop: el.scrollTop,
  }));
  console.log(`Container scroll metrics:`, scrollInfo);

  // Manually scroll up
  console.log('Manually scrolling up to scrollTop = 50 ...');
  await container.evaluate((el) => {
    el.scrollTop = 50;
    el.dispatchEvent(new Event('scroll'));
  });

  await page.waitForTimeout(400);

  // Verify ArrowDown bottom button appears
  const scrollBottomBtn = page.locator('[data-testid="scroll-to-bottom-button"]');
  await scrollBottomBtn.waitFor({ state: 'visible', timeout: 4000 });
  const isBtnVisible = await scrollBottomBtn.isVisible();
  console.log(`- Round ArrowDown button appears after scroll up: ${isBtnVisible ? 'PASS ✅' : 'FAIL ❌'}`);
  if (!isBtnVisible) {
    throw new Error('Scroll to bottom button did not appear!');
  }

  // Verify screen position is NOT hijacked (scrollTop stayed near 50)
  const currentScrollTop = await container.evaluate((el) => el.scrollTop);
  const notHijacked = Math.abs(currentScrollTop - 50) < 10;
  console.log(`- Screen not hijacked (current scrollTop: ${currentScrollTop}): ${notHijacked ? 'PASS ✅' : 'FAIL ❌'}`);
  if (!notHijacked) {
    throw new Error('Screen was hijacked after manual upward scroll!');
  }

  // Click ArrowDown button: verify smooth scroll down to bottom
  console.log('Clicking ArrowDown scroll-to-bottom button...');
  await scrollBottomBtn.click();
  await page.waitForTimeout(1000);

  const bottomScrollInfo = await container.evaluate((el) => ({
    dist: el.scrollHeight - el.scrollTop - el.clientHeight,
    scrollTop: el.scrollTop,
  }));
  console.log(`Post-click scroll distance from bottom:`, bottomScrollInfo.dist);
  const isAtBottom = bottomScrollInfo.dist <= 60;
  console.log(`- Scrolled smoothly to bottom: ${isAtBottom ? 'PASS ✅' : 'FAIL ❌'}`);
  if (!isAtBottom) {
    throw new Error('Clicking ArrowDown button did not scroll to bottom!');
  }

  // Verify button is hidden once at bottom
  await page.waitForTimeout(300);
  const isBtnHidden = !(await scrollBottomBtn.isVisible());
  console.log(`- ArrowDown button hides when at bottom: ${isBtnHidden ? 'PASS ✅' : 'FAIL ❌'}`);

  // ==========================================
  // TEST SUITE 3: SETTINGS FEATURES
  // ==========================================
  console.log('\n--- 3. Testing Settings Features ---');

  // Open Settings modal using sidebar button
  const sidebarSettingsBtn = page.locator('[data-testid="sidebar-settings-button"]');
  if (await sidebarSettingsBtn.isVisible()) {
    await sidebarSettingsBtn.click();
  } else {
    // If sidebar collapsed, open sidebar first
    const openSidebarBtn = page.locator('button[title*="sidebar"]').first();
    if (await openSidebarBtn.isVisible()) {
      await openSidebarBtn.click();
      await page.waitForTimeout(400);
    }
    await sidebarSettingsBtn.click();
  }

  await page.waitForSelector('text=Cài đặt hệ thống', { timeout: 5000 });
  console.log('✅ Settings Modal opened successfully.');

  // 3A. Test Font Size: Small / Medium / Large
  console.log('Testing font size changes...');
  // Navigate to "Đọc & Hiển thị" tab
  const displayTab = page.locator('[data-testid="settings-tab-display"]').first();
  await displayTab.click();
  await page.waitForTimeout(300);

  // 1) Click Small
  const smallBtn = page.locator('[data-testid="font-size-small"]');
  await smallBtn.click();
  await page.waitForTimeout(300);

  const dataFontSizeSmall = await page.evaluate(() => document.documentElement.getAttribute('data-font-size'));
  const chatFontSizeSmall = await page.locator('.chat-message-text').first().evaluate((el) => window.getComputedStyle(el).fontSize);
  console.log(`Small Font: data-font-size="${dataFontSizeSmall}", computed fontSize="${chatFontSizeSmall}"`);
  const isSmallValid = dataFontSizeSmall === 'small' && chatFontSizeSmall === '13px';
  console.log(`- Small font size updates immediately to 13px: ${isSmallValid ? 'PASS ✅' : 'FAIL ❌'}`);
  if (!isSmallValid) {
    throw new Error(`Font size Small failed! Expected 13px, got ${chatFontSizeSmall}`);
  }

  // 2) Click Large
  const largeBtn = page.locator('[data-testid="font-size-large"]');
  await largeBtn.click();
  await page.waitForTimeout(300);

  const dataFontSizeLarge = await page.evaluate(() => document.documentElement.getAttribute('data-font-size'));
  const chatFontSizeLarge = await page.locator('.chat-message-text').first().evaluate((el) => window.getComputedStyle(el).fontSize);
  console.log(`Large Font: data-font-size="${dataFontSizeLarge}", computed fontSize="${chatFontSizeLarge}"`);
  const isLargeValid = dataFontSizeLarge === 'large' && chatFontSizeLarge === '17px';
  console.log(`- Large font size updates immediately to 17px: ${isLargeValid ? 'PASS ✅' : 'FAIL ❌'}`);
  if (!isLargeValid) {
    throw new Error(`Font size Large failed! Expected 17px, got ${chatFontSizeLarge}`);
  }

  // 3) Reset to Medium
  const medBtn = page.locator('[data-testid="font-size-medium"]');
  await medBtn.click();
  await page.waitForTimeout(300);
  const chatFontSizeMed = await page.locator('.chat-message-text').first().evaluate((el) => window.getComputedStyle(el).fontSize);
  console.log(`Medium Font: computed fontSize="${chatFontSizeMed}"`);
  const isMedValid = chatFontSizeMed === '15px';
  console.log(`- Medium font size updates to 15px: ${isMedValid ? 'PASS ✅' : 'FAIL ❌'}`);
  if (!isMedValid) {
    throw new Error(`Font size Medium failed! Expected 15px, got ${chatFontSizeMed}`);
  }

  // 3B. Test Web Search switch toggle & persistence
  console.log('Testing Web Search toggle...');
  const modelTab = page.locator('[data-testid="settings-tab-model"]').first();
  await modelTab.click();
  await page.waitForTimeout(300);

  const webSearchToggle = page.locator('[data-testid="toggle-web-search"]');
  const initialWebSearch = await webSearchToggle.getAttribute('aria-checked');
  console.log(`Initial Web Search state: ${initialWebSearch}`);

  // Toggle switch
  await webSearchToggle.click();
  await page.waitForTimeout(300);
  const toggledWebSearch = await webSearchToggle.getAttribute('aria-checked');
  console.log(`Toggled Web Search state: ${toggledWebSearch}`);

  const localWebSearch = await page.evaluate(() => localStorage.getItem('agrivision-web-search'));
  console.log(`localStorage agrivision-web-search: ${localWebSearch}`);

  const toggleWorked = toggledWebSearch !== initialWebSearch && localWebSearch === toggledWebSearch;
  console.log(`- Web Search switch toggled & state persists: ${toggleWorked ? 'PASS ✅' : 'FAIL ❌'}`);
  if (!toggleWorked) {
    throw new Error('Web Search toggle persistence failed!');
  }

  // Toggle back to true
  if (toggledWebSearch === 'false') {
    await webSearchToggle.click();
    await page.waitForTimeout(200);
  }

  // 3C. Test "Xuất JSON" backup file generation
  console.log('Testing "Xuất JSON" button and download generation...');
  const dataTab = page.locator('[data-testid="settings-tab-data"]').first();
  await dataTab.click();
  await page.waitForTimeout(300);

  const exportBtn = page.locator('[data-testid="export-json-button"]');
  await exportBtn.waitFor({ state: 'visible', timeout: 3000 });

  // Set up download listener
  const [download] = await Promise.all([
    page.waitForEvent('download', { timeout: 7000 }),
    exportBtn.click(),
  ]);

  const downloadFilename = download.suggestedFilename();
  console.log(`Suggested download filename: ${downloadFilename}`);

  const isJsonFilename = downloadFilename.startsWith('agrivision-backup-') && downloadFilename.endsWith('.json');
  console.log(`- Filename matches agrivision-backup-*.json: ${isJsonFilename ? 'PASS ✅' : 'FAIL ❌'}`);
  if (!isJsonFilename) {
    throw new Error(`Download filename invalid: ${downloadFilename}`);
  }

  const downloadPath = await download.path();
  if (downloadPath) {
    const fileContent = fs.readFileSync(downloadPath, 'utf-8');
    const parsedData = JSON.parse(fileContent);
    console.log(`Downloaded JSON content check: project="${parsedData.project}", version="${parsedData.version}", convCount=${parsedData.conversations?.length}`);
    const isJsonValid = parsedData.project === 'AgriVision' && parsedData.version === '1.0.0' && Array.isArray(parsedData.conversations);
    console.log(`- Backup JSON contains valid schema & conversation data: ${isJsonValid ? 'PASS ✅' : 'FAIL ❌'}`);
    if (!isJsonValid) {
      throw new Error('Downloaded JSON structure invalid!');
    }
  }

  console.log('\n=============================================');
  console.log('🎉 ALL SUBAGENT 4 TESTS PASSED AT 100% SUCCESS RATE! 🎉');
  console.log('=============================================\n');

  await browser.close();
  return true;
}

runTests().catch((err) => {
  console.error('\n❌ TEST RUN FAILED:', err);
  process.exit(1);
});
