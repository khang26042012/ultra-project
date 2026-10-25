import { chromium } from 'playwright';
import path from 'path';

const ARTIFACT_DIR = 'C:/Users/khangmc/.gemini/antigravity/brain/b6cc8e35-57f6-4d5a-bc1d-cfea5fba4f57';

async function run() {
  console.log('🚀 Running Deep Modal & UI Audit with precise modal locators...');
  const browser = await chromium.launch({ channel: 'chrome', headless: true });

  // 1. Desktop Test (1440 x 900)
  const desktopContext = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  const page = await desktopContext.newPage();
  await page.goto('http://localhost:3000', { waitUntil: 'networkidle' });
  await page.waitForTimeout(1000);

  // Click "Cài đặt hệ thống"
  console.log('Clicking Cài đặt hệ thống on Desktop...');
  await page.locator('button:visible:has-text("Cài đặt hệ thống")').first().click();
  await page.waitForTimeout(600);
  await page.screenshot({ path: path.join(ARTIFACT_DIR, 'stage4_desktop_settings_general.png') });
  console.log('📸 Saved stage4_desktop_settings_general.png');

  // Click tab "Đọc & Hiển thị"
  await page.locator('div.fixed.z-50 button:visible:has-text("Đọc & Hiển thị")').first().click();
  await page.waitForTimeout(300);
  await page.screenshot({ path: path.join(ARTIFACT_DIR, 'stage4_desktop_settings_display.png') });
  console.log('📸 Saved stage4_desktop_settings_display.png');

  // Click tab "Mô hình AI"
  await page.locator('div.fixed.z-50 button:visible:has-text("Mô hình AI")').first().click();
  await page.waitForTimeout(300);
  await page.screenshot({ path: path.join(ARTIFACT_DIR, 'stage4_desktop_settings_model.png') });
  console.log('📸 Saved stage4_desktop_settings_model.png');

  // Click tab "Dữ liệu"
  await page.locator('div.fixed.z-50 button:visible:has-text("Dữ liệu")').first().click();
  await page.waitForTimeout(300);
  await page.screenshot({ path: path.join(ARTIFACT_DIR, 'stage4_desktop_settings_data.png') });
  console.log('📸 Saved stage4_desktop_settings_data.png');

  // Click tab "Giới thiệu"
  await page.locator('div.fixed.z-50 button:visible:has-text("Giới thiệu")').first().click();
  await page.waitForTimeout(300);
  await page.screenshot({ path: path.join(ARTIFACT_DIR, 'stage4_desktop_settings_about.png') });
  console.log('📸 Saved stage4_desktop_settings_about.png');

  // Close Settings modal via Esc key or X button inside modal
  await page.locator('div.fixed.z-50 button:has(svg.lucide-x)').first().click();
  await page.waitForTimeout(400);

  // Click "Trợ giúp & Hướng dẫn"
  console.log('Clicking Trợ giúp & Hướng dẫn on Desktop...');
  await page.locator('button:visible:has-text("Trợ giúp & Hướng dẫn")').first().click();
  await page.waitForTimeout(600);
  await page.screenshot({ path: path.join(ARTIFACT_DIR, 'stage4_desktop_help_modal.png') });
  console.log('📸 Saved stage4_desktop_help_modal.png');

  // Close Help modal via X button
  await page.locator('div.fixed.z-50 button:has(svg.lucide-x)').first().click();
  await page.waitForTimeout(400);

  // 2. Mobile Viewport (390 x 844 iPhone 14/15)
  console.log('\n--- Mobile Viewport (390 x 844) ---');
  const mobileContext = await browser.newContext({
    viewport: { width: 390, height: 844 },
    isMobile: true,
    hasTouch: true,
  });
  const mobilePage = await mobileContext.newPage();
  await mobilePage.goto('http://localhost:3000', { waitUntil: 'networkidle' });
  await mobilePage.waitForTimeout(1000);

  // Open mobile drawer
  await mobilePage.locator('header button:visible:has(svg.lucide-panel-left)').first().click();
  await mobilePage.waitForTimeout(500);

  // Click Settings inside mobile drawer
  await mobilePage.locator('button:visible:has-text("Cài đặt hệ thống")').first().click();
  await mobilePage.waitForTimeout(500);
  await mobilePage.screenshot({ path: path.join(ARTIFACT_DIR, 'stage4_mobile_settings_pills.png') });
  console.log('📸 Saved stage4_mobile_settings_pills.png');

  // Click "Mô hình AI" horizontal pill
  await mobilePage.locator('div.fixed.z-50 button:visible:has-text("Mô hình AI")').first().click();
  await mobilePage.waitForTimeout(300);
  await mobilePage.screenshot({ path: path.join(ARTIFACT_DIR, 'stage4_mobile_settings_model_pill.png') });
  console.log('📸 Saved stage4_mobile_settings_model_pill.png');

  // Close Settings modal
  await mobilePage.locator('div.fixed.z-50 button:has(svg.lucide-x)').first().click();
  await mobilePage.waitForTimeout(400);

  // Reopen drawer and open Help
  await mobilePage.locator('header button:visible:has(svg.lucide-panel-left)').first().click();
  await mobilePage.waitForTimeout(400);
  await mobilePage.locator('button:visible:has-text("Trợ giúp & Hướng dẫn")').first().click();
  await mobilePage.waitForTimeout(500);
  await mobilePage.screenshot({ path: path.join(ARTIFACT_DIR, 'stage4_mobile_help_modal.png') });
  console.log('📸 Saved stage4_mobile_help_modal.png');

  await browser.close();
  console.log('\n✨ ALL MODAL AUDITS COMPLETED BEAUTIFULLY!');
}

run().catch((e) => {
  console.error('Audit failed:', e);
  process.exit(1);
});
