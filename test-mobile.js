const { chromium } = require('playwright');

async function runTests() {
  const browser = await chromium.launch({ headless: true });
  const viewports = [
    { name: 'iPhone 14 (390x844)', width: 390, height: 844 },
    { name: 'Android (412x915)', width: 412, height: 915 },
    { name: 'iPhone SE (375x667)', width: 375, height: 667 },
  ];

  let allPassed = true;
  const results = [];

  for (const vp of viewports) {
    console.log(`\n========================================`);
    console.log(`Testing Viewport: ${vp.name}`);
    console.log(`========================================`);

    const context = await browser.newContext({
      viewport: { width: vp.width, height: vp.height },
      userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1',
    });
    const page = await context.newPage();

    // Collect console errors
    const consoleErrors = [];
    page.on('console', (msg) => {
      if (msg.type() === 'error') {
        consoleErrors.push(msg.text());
      }
    });

    await page.goto('http://localhost:3000', { waitUntil: 'networkidle' });

    // 1. Header Mobile Check
    console.log(`[1] Checking Header Mobile on ${vp.name}...`);
    const header = await page.locator('header');
    const isHeaderVisible = await header.isVisible();
    console.log(` - Header visible: ${isHeaderVisible}`);

    // Check circular AV avatar in header
    const avInHeader = await header.locator('text=AV').count();
    const nameInHeader = await header.locator('text=AgriVision').count();
    console.log(` - Circular AV avatar in header count: ${avInHeader} (Expected 0)`);
    console.log(` - AgriVision name in header count: ${nameInHeader} (Expected 0)`);

    // Check header children count and buttons
    const headerButtons = await header.locator('button');
    const btnCount = await headerButtons.count();
    console.log(` - Header buttons count: ${btnCount} (Expected 2: sidebar toggle & new chat)`);

    // Check computed border-bottom
    const headerBorderBottom = await header.evaluate((el) => {
      const style = window.getComputedStyle(el);
      return {
        borderBottomWidth: style.borderBottomWidth,
        borderBottomStyle: style.borderBottomStyle,
        borderBottomColor: style.borderBottomColor,
        borderWidth: style.borderWidth,
      };
    });
    console.log(` - Header border evaluation:`, headerBorderBottom);

    const headerOk = isHeaderVisible && avInHeader === 0 && nameInHeader === 0 && btnCount === 2 && (headerBorderBottom.borderBottomWidth === '0px' || headerBorderBottom.borderBottomStyle === 'none');
    console.log(` -> Header Check Passed: ${headerOk}`);
    if (!headerOk) allPassed = false;

    // Check horizontal overflow on body/html
    const checkOverflow = async (stepName) => {
      const overflow = await page.evaluate(() => {
        const docWidth = document.documentElement.clientWidth;
        const scrollWidth = document.documentElement.scrollWidth;
        const bodyScrollWidth = document.body.scrollWidth;
        const windowWidth = window.innerWidth;
        const hasHorizontalScrollbar = scrollWidth > docWidth || bodyScrollWidth > windowWidth;
        return {
          docWidth,
          scrollWidth,
          bodyScrollWidth,
          windowWidth,
          hasHorizontalScrollbar,
        };
      });
      console.log(` - Overflow check [${stepName}]:`, overflow);
      return !overflow.hasHorizontalScrollbar;
    };

    let overflowOk = await checkOverflow('Initial Page Load');
    if (!overflowOk) allPassed = false;

    // 2. Floating Input Island Check
    console.log(`[2] Checking Floating Input Island on ${vp.name}...`);
    const textarea = page.locator('textarea');
    await textarea.waitFor({ state: 'visible' });

    const initialHeight = await textarea.evaluate((el) => el.getBoundingClientRect().height);
    console.log(` - Initial textarea height: ${initialHeight}px`);

    // Type long multiline text
    const longText = 'Dòng 1: Cây bưởi da xanh bị vàng lá gân xanh.\n' +
      'Dòng 2: Xuất hiện đốm nâu loang lổ trên phiến lá non.\n' +
      'Dòng 3: Rễ tơ bị thối đen, cây phát triển còi cọc.\n' +
      'Dòng 4: Vườn tại Tam Bình Vĩnh Long độ ẩm cao.\n' +
      'Dòng 5: Cần hướng dẫn biện pháp quản lý sinh học theo VietGAP.\n' +
      'Dòng 6: Liều lượng phun thuốc sinh học định kỳ.\n' +
      'Dòng 7: Kiểm tra bổ sung dòng thứ 7 để test scroll.';

    await textarea.fill(longText);
    await page.waitForTimeout(300);

    const expandedHeight = await textarea.evaluate((el) => el.getBoundingClientRect().height);
    const scrollHeight = await textarea.evaluate((el) => el.scrollHeight);
    console.log(` - Expanded textarea height: ${expandedHeight}px (scrollHeight: ${scrollHeight}px)`);

    const isAutoExpanded = expandedHeight > initialHeight;
    const isMaxHeightCapped = expandedHeight <= 185; // ~180px max-height
    console.log(` - Auto-expanded: ${isAutoExpanded}, Capped <= 185px: ${isMaxHeightCapped}`);

    overflowOk = await checkOverflow('After Typing Long Text');
    if (!overflowOk) allPassed = false;

    // Verify Plus button and Send button
    const plusButton = page.locator('button[title*="Đính kèm"]');
    const isPlusVisible = await plusButton.isVisible();
    console.log(` - Plus button visible: ${isPlusVisible}`);

    const sendButton = page.locator('button[title*="Gửi"]');
    const isSendVisible = await sendButton.isVisible();
    const sendBtnRadius = await sendButton.evaluate((el) => window.getComputedStyle(el).borderRadius);
    console.log(` - Send button visible: ${isSendVisible}, border-radius: ${sendBtnRadius}`);

    const inputOk = isAutoExpanded && isMaxHeightCapped && overflowOk && isPlusVisible && isSendVisible;
    console.log(` -> Floating Input Island Check Passed: ${inputOk}`);
    if (!inputOk) allPassed = false;

    // Clear textarea
    await textarea.fill('');

    // 3. Settings Modal on mobile
    console.log(`[3] Checking Settings Modal on ${vp.name}...`);
    // Open sidebar first
    const sidebarToggleBtn = header.locator('button').first();
    await sidebarToggleBtn.click();
    await page.waitForTimeout(400);

    // Click Settings button in sidebar
    const settingsBtn = page.locator('aside button:has-text("Cài đặt hệ thống")');
    await settingsBtn.click();
    await page.waitForTimeout(400);

    // Verify Settings Modal is open
    const settingsModal = page.locator('div[role="dialog"], div.fixed.inset-0:has-text("Cài đặt hệ thống")');
    const isSettingsVisible = await settingsModal.isVisible();
    console.log(` - Settings Modal visible: ${isSettingsVisible}`);

    // Verify horizontal scrolling tabs pills at the top
    const mobileTabContainer = settingsModal.locator('.md\\:hidden').filter({ hasText: 'Chung' });
    const isMobileTabsVisible = await mobileTabContainer.isVisible();
    console.log(` - Mobile Tabs Pills bar visible: ${isMobileTabsVisible}`);

    // Verify desktop sidebar tabs are hidden
    const desktopTabs = settingsModal.locator('.hidden.md\\:flex');
    const isDesktopTabsHidden = !(await desktopTabs.isVisible());
    console.log(` - Desktop Tabs Sidebar hidden: ${isDesktopTabsHidden}`);

    // Verify modal content width is responsive (no horizontal overflow of viewport)
    overflowOk = await checkOverflow('Settings Modal Open');
    if (!overflowOk) allPassed = false;

    // Check each tab
    const tabsList = ['Chung', 'Đọc & Hiển thị', 'Mô hình AI', 'Dữ liệu', 'Giới thiệu'];
    let tabsOk = true;
    for (const tabName of tabsList) {
      const tabBtn = mobileTabContainer.locator(`button:has-text("${tabName}")`);
      await tabBtn.click();
      await page.waitForTimeout(200);
      const ov = await checkOverflow(`Settings Tab - ${tabName}`);
      if (!ov) tabsOk = false;
    }
    console.log(` - All Settings tabs switched without overflow: ${tabsOk}`);

    // Close settings modal
    const closeSettingsBtn = settingsModal.locator('button[title*="Đóng"]').first();
    await closeSettingsBtn.click();
    await page.waitForTimeout(300);

    // 4. Help Modal on mobile
    console.log(`[4] Checking Help Modal on ${vp.name}...`);
    // Open sidebar again if not open
    const isSidebarOpen = await page.locator('aside').evaluate((el) => {
      const style = window.getComputedStyle(el);
      return style.display !== 'none' && parseFloat(style.opacity) > 0.5;
    });
    if (!isSidebarOpen) {
      await sidebarToggleBtn.click();
      await page.waitForTimeout(400);
    }

    const helpBtn = page.locator('aside button:has-text("Trợ giúp & Hướng dẫn")');
    await helpBtn.click();
    await page.waitForTimeout(400);

    const helpModal = page.locator('div.fixed.inset-0:has-text("Cẩm nang Hướng dẫn Nông dân AgriVision")');
    const isHelpVisible = await helpModal.isVisible();
    console.log(` - Help Modal visible: ${isHelpVisible}`);

    // Verify 4 farmer guidelines
    const guideline1 = await helpModal.locator('text=1. Cách chụp ảnh chuẩn bệnh học vi mô').count();
    const guideline2 = await helpModal.locator('text=2. Mô tả triệu chứng hiệu quả cho AI').count();
    const guideline3 = await helpModal.locator('text=3. Phương pháp thử nghiệm lâm sàng tại vườn').count();
    const guideline4 = await helpModal.locator('text=4. Thông tin liên hệ cơ quan bảo vệ thực vật địa phương').count();

    console.log(` - Guideline 1 count: ${guideline1}`);
    console.log(` - Guideline 2 count: ${guideline2}`);
    console.log(` - Guideline 3 count: ${guideline3}`);
    console.log(` - Guideline 4 count: ${guideline4}`);

    const all4Guidelines = guideline1 > 0 && guideline2 > 0 && guideline3 > 0 && guideline4 > 0;
    console.log(` - All 4 guidelines present: ${all4Guidelines}`);

    overflowOk = await checkOverflow('Help Modal Open');
    if (!overflowOk) allPassed = false;

    // Close help modal
    const closeHelpBtn = helpModal.locator('button:has-text("Đã hiểu"), button[title*="Đóng"]').first();
    await closeHelpBtn.click();
    await page.waitForTimeout(300);

    console.log(` - Console Errors count: ${consoleErrors.length}`);
    if (consoleErrors.length > 0) {
      console.log(`   Errors:`, consoleErrors);
    }

    const vpPassed = headerOk && inputOk && isSettingsVisible && isMobileTabsVisible && isDesktopTabsHidden && tabsOk && isHelpVisible && all4Guidelines && overflowOk && consoleErrors.length === 0;
    results.push({ viewport: vp.name, passed: vpPassed });

    await context.close();
  }

  await browser.close();

  console.log(`\n========================================`);
  console.log(`TEST SUMMARY:`);
  console.log(`========================================`);
  for (const r of results) {
    console.log(`${r.viewport}: ${r.passed ? 'PASSED' : 'FAILED'}`);
  }

  process.exit(allPassed ? 0 : 1);
}

runTests().catch((err) => {
  console.error('Test execution failed:', err);
  process.exit(1);
});
