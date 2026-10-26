const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

async function captureScreenshots() {
  const browser = await chromium.launch({ headless: true });
  const viewports = [
    { name: 'iphone14_390x844', width: 390, height: 844 },
    { name: 'android_412x915', width: 412, height: 915 },
    { name: 'iphonese_375x667', width: 375, height: 667 },
  ];

  const screenshotDir = path.join(__dirname, 'screenshots');
  if (!fs.existsSync(screenshotDir)) {
    fs.mkdirSync(screenshotDir, { recursive: true });
  }

  for (const vp of viewports) {
    const context = await browser.newContext({
      viewport: { width: vp.width, height: vp.height },
      deviceScaleFactor: 2,
    });
    const page = await context.newPage();
    await page.goto('http://localhost:3000', { waitUntil: 'networkidle' });

    // 1. Home screen with header and input island
    await page.screenshot({ path: path.join(screenshotDir, `${vp.name}_home.png`) });

    // 2. Open Settings modal
    const sidebarToggleBtn = page.locator('header button').first();
    await sidebarToggleBtn.click();
    await page.waitForTimeout(400);

    const settingsBtn = page.locator('aside button:has-text("Cài đặt hệ thống")');
    await settingsBtn.click();
    await page.waitForTimeout(400);
    await page.screenshot({ path: path.join(screenshotDir, `${vp.name}_settings.png`) });

    // Close Settings via Esc
    await page.keyboard.press('Escape');
    await page.waitForTimeout(400);

    // 3. Open Help modal
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
    await page.screenshot({ path: path.join(screenshotDir, `${vp.name}_help.png`) });

    // Close Help via Esc
    await page.keyboard.press('Escape');
    await page.waitForTimeout(400);

    await context.close();
  }

  await browser.close();
  console.log('All screenshots captured successfully!');
}

captureScreenshots().catch((err) => {
  console.error('Screenshot capture failed:', err);
  process.exit(1);
});
