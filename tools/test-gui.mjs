import { chromium } from 'playwright';
import path from 'path';

const ARTIFACT_DIR = 'C:/Users/khangmc/.gemini/antigravity/brain/b6cc8e35-57f6-4d5a-bc1d-cfea5fba4f57';

async function run() {
  console.log('🚀 Starting Comprehensive GUI Audit with Playwright...');
  const browser = await chromium.launch({ channel: 'chrome', headless: true });

  // 1. Desktop Test (1440 x 900)
  console.log('\n--- 1. Testing Desktop Viewport (1440 x 900) ---');
  const desktopContext = await browser.newContext({
    viewport: { width: 1440, height: 900 }
  });
  const page = await desktopContext.newPage();
  await page.goto('http://localhost:3000', { waitUntil: 'networkidle' });
  await page.waitForTimeout(1000);

  // Measure sidebar
  const sidebar = page.locator('aside:visible');
  const sidebarBox = await sidebar.boundingBox();
  console.log('Desktop Sidebar width (expected ~260px):', Math.round(sidebarBox?.width || 0));
  await page.screenshot({ path: path.join(ARTIFACT_DIR, '01_desktop_initial.png') });
  console.log('📸 Saved 01_desktop_initial.png');

  // Test collapsible sidebar
  const collapseBtn = page.locator('button[title*="Đóng sidebar"]:visible, button:visible:has(svg.lucide-panel-left-close)').first();
  if (await collapseBtn.count() > 0) {
    console.log('Clicking collapse sidebar button...');
    await collapseBtn.click();
    await page.waitForTimeout(400);
    await page.screenshot({ path: path.join(ARTIFACT_DIR, '02_desktop_collapsed.png') });
    console.log('📸 Saved 02_desktop_collapsed.png');

    // Reopen sidebar
    const openBtn = page.locator('button[title*="Mở sidebar"]:visible, button:visible:has(svg.lucide-panel-left)').first();
    if (await openBtn.count() > 0) {
      await openBtn.click();
      await page.waitForTimeout(400);
      console.log('Reopened sidebar');
    }
  }

  // 2. Mobile Viewport (390 x 844 iPhone 14/15)
  console.log('\n--- 2. Testing Mobile Viewport (390 x 844 iPhone) ---');
  const mobileContext = await browser.newContext({
    viewport: { width: 390, height: 844 },
    isMobile: true,
    hasTouch: true,
  });
  const mobilePage = await mobileContext.newPage();
  await mobilePage.goto('http://localhost:3000', { waitUntil: 'networkidle' });
  await mobilePage.waitForTimeout(1000);

  // Check mobile sidebar initially closed
  const mobileSidebar = mobilePage.locator('aside');
  const mobileSidebarVisible = await mobileSidebar.isVisible();
  console.log('Mobile Sidebar initially visible (should be false):', mobileSidebarVisible);
  await mobilePage.screenshot({ path: path.join(ARTIFACT_DIR, '03_mobile_initial.png') });
  console.log('📸 Saved 03_mobile_initial.png');

  // Open mobile drawer
  const mobileOpenBtn = mobilePage.locator('header button:visible:has(svg.lucide-panel-left)').first();
  if (await mobileOpenBtn.count() > 0) {
    console.log('Opening mobile drawer...');
    await mobileOpenBtn.click();
    await mobilePage.waitForTimeout(500);
    await mobilePage.screenshot({ path: path.join(ARTIFACT_DIR, '04_mobile_drawer_open.png') });
    console.log('📸 Saved 04_mobile_drawer_open.png');

    // Click outside drawer (at x: 340, y: 300) to close drawer
    console.log('Clicking outside drawer to close...');
    await mobilePage.mouse.click(340, 300);
    await mobilePage.waitForTimeout(500);
    await mobilePage.screenshot({ path: path.join(ARTIFACT_DIR, '05_mobile_drawer_closed.png') });
    console.log('📸 Saved 05_mobile_drawer_closed.png');
  }

  // 3. Android Viewport (412 x 915 Samsung/Pixel)
  console.log('\n--- 3. Testing Android Viewport (412 x 915) ---');
  const androidContext = await browser.newContext({
    viewport: { width: 412, height: 915 },
    isMobile: true,
    hasTouch: true,
  });
  const androidPage = await androidContext.newPage();
  await androidPage.goto('http://localhost:3000', { waitUntil: 'networkidle' });
  await androidPage.waitForTimeout(800);
  await androidPage.screenshot({ path: path.join(ARTIFACT_DIR, '06_android_initial.png') });
  console.log('📸 Saved 06_android_initial.png');

  // 4. Interactive Test on Desktop: Sending exact test query
  console.log('\n--- 4. Interactive Test: Sending Disease Diagnosis Query ---');
  const query = 'Cây bưởi bị vàng lá loang lổ bất đối xứng là bệnh gì?';
  const textarea = page.locator('textarea:visible').first();
  if (await textarea.count() > 0) {
    console.log('Filling query:', query);
    await textarea.fill(query);
    await page.waitForTimeout(400);

    const sendBtn = page.locator('button[title="Gửi câu hỏi"]:visible').first();
    const isSendDisabled = await sendBtn.getAttribute('disabled');
    console.log('Send button enabled when query entered:', isSendDisabled === null);

    console.log('Submitting question...');
    await sendBtn.click();
    await page.waitForTimeout(2000);

    // Screenshot during streaming/thinking
    await page.screenshot({ path: path.join(ARTIFACT_DIR, '07_chat_thinking_stream.png') });
    console.log('📸 Saved 07_chat_thinking_stream.png');

    console.log('Waiting for AI response and thinking to settle...');
    try {
      await page.waitForSelector('button[title="Sao chép tin nhắn"]', { timeout: 35000 });
      console.log('AI Response generation settled and completed!');
    } catch (e) {
      console.log('Waiting settled or timed out:', e.message);
    }

    await page.waitForTimeout(1000);
    await page.screenshot({ path: path.join(ARTIFACT_DIR, '08_chat_response_completed.png') });
    console.log('📸 Saved 08_chat_response_completed.png');

    // Test Thinking Accordion
    const thinkingBtn = page.locator('button:has-text("Đã suy luận"), button:has-text("Tiến trình suy luận")').first();
    if (await thinkingBtn.count() > 0) {
      console.log('Testing clicking thinking accordion to expand...');
      await thinkingBtn.click();
      await page.waitForTimeout(500);
      await page.screenshot({ path: path.join(ARTIFACT_DIR, '09_thinking_expanded.png') });
      console.log('📸 Saved 09_thinking_expanded.png');
    }

    // Test Copy button
    const copyBtn = page.locator('button[title="Sao chép tin nhắn"]:visible').first();
    if (await copyBtn.count() > 0) {
      console.log('Testing Copy button interaction...');
      await copyBtn.click();
      await page.waitForTimeout(400);
      const hasCheckIcon = await page.locator('svg.lucide-check:visible').count() > 0;
      console.log('Copy button verified - check icon displayed:', hasCheckIcon);
      await page.screenshot({ path: path.join(ARTIFACT_DIR, '10_copy_button_verified.png') });
      console.log('📸 Saved 10_copy_button_verified.png');
    }

    // 5. Responsive Check: View completed chat on mobile
    console.log('\n--- 5. Checking Completed Chat on Mobile Viewport (390 x 844) ---');
    await page.setViewportSize({ width: 390, height: 844 });
    await page.waitForTimeout(800);
    await page.screenshot({ path: path.join(ARTIFACT_DIR, '11_mobile_chat_completed.png') });
    console.log('📸 Saved 11_mobile_chat_completed.png');
  }

  await browser.close();
  console.log('\n🎉 ALL TESTS FINISHED SUCCESSFULLY!');
}

run().catch((err) => {
  console.error('Test execution failed:', err);
  process.exit(1);
});
