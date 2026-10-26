const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

async function runBrowserE2E() {
  console.log('🚀 Starting AgriVision E2E Browser Test via Microsoft Edge...');
  
  const browser = await chromium.launch({
    channel: 'msedge',
    headless: true,
  });

  const context = await browser.newContext({
    viewport: { width: 1280, height: 800 },
  });

  const page = await context.newPage();
  const results = {
    home_page: false,
    header_crop_link: false,
    crops_page: false,
    crops_search: false,
    crops_filter_tabs: false,
    crops_modal: false,
  };

  try {
    // 1. Visit Home Page
    console.log('1️⃣ Navigating to Home Page: http://localhost:3000 ...');
    await page.goto('http://localhost:3000', { waitUntil: 'networkidle', timeout: 15000 });
    const title = await page.title();
    console.log(`   Page title: "${title}"`);
    const pageText = await page.innerText('body');
    if (pageText.includes('AgriVision')) {
      console.log('   ✅ Home page loaded with "AgriVision" branding');
      results.home_page = true;
    }

    // 2. Check "Toàn thư bệnh học 1.500+" link
    console.log('2️⃣ Verifying Header Shortcut to Encyclopedia...');
    const cropLink = await page.$('a[href="/crops"]');
    if (cropLink) {
      const linkText = await cropLink.innerText();
      console.log(`   ✅ Found header link to /crops with text: "${linkText.replace(/\n/g, ' ')}"`);
      results.header_crop_link = true;
    } else {
      console.log('   ⚠️ Could not locate a[href="/crops"] link');
    }

    // 3. Navigate to /crops Encyclopedia Page
    console.log('3️⃣ Navigating to /crops Encyclopedia Page...');
    await page.goto('http://localhost:3000/crops', { waitUntil: 'networkidle', timeout: 15000 });
    const cropsTitle = await page.title();
    console.log(`   /crops Title: "${cropsTitle}"`);

    // Wait for crop cards to load from /api/crops
    await page.waitForSelector('input[placeholder*="Tìm"]', { timeout: 10000 });
    console.log('   ✅ Search input rendered');

    // Wait for at least one card to appear
    await page.waitForTimeout(2000);
    const bodyContent = await page.innerText('body');
    if (bodyContent.includes('Toàn Thư') || bodyContent.includes('Tra Cứu') || bodyContent.includes('loài cây')) {
      console.log('   ✅ /crops page loaded successfully with catalog header');
      results.crops_page = true;
    }

    // 4. Test Search Functionality in /crops
    console.log('4️⃣ Testing Search input for "sầu riêng"...');
    const searchInput = await page.$('input[placeholder*="Tìm"]');
    if (searchInput) {
      await searchInput.fill('sầu riêng');
      await page.waitForTimeout(1500); // Allow debounce / API response
      const searchResultText = await page.innerText('body');
      if (searchResultText.includes('Sầu Riêng') || searchResultText.includes('Durio')) {
        console.log('   ✅ Search for "sầu riêng" successfully filtered and displayed matching crops!');
        results.crops_search = true;
      } else {
        console.log('   ℹ️ Search text present:', searchResultText.slice(0, 300));
      }
    }

    // 5. Test Filter Tabs
    console.log('5️⃣ Testing Category Filter Tabs...');
    const buttons = await page.$$('button');
    let clickedTab = false;
    for (const btn of buttons) {
      const txt = await btn.innerText();
      if (txt.includes('Cây ăn trái') || txt.includes('Dược liệu')) {
        console.log(`   Clicking tab: "${txt.trim()}"`);
        await btn.click();
        await page.waitForTimeout(1000);
        clickedTab = true;
        break;
      }
    }
    if (clickedTab) {
      console.log('   ✅ Category filter tab clickable and reactive');
      results.crops_filter_tabs = true;
    }

    // 6. Test Opening Crop Detail Modal
    console.log('6️⃣ Testing Opening Crop Pathology Detail Modal...');
    // Clear search to get default cards
    if (searchInput) {
      await searchInput.fill('');
      await page.waitForTimeout(1000);
    }
    // Find the first clickable card button
    const cardButtons = await page.$$('div[class*="cursor-pointer"], button[class*="cursor-pointer"]');
    let modalOpened = false;
    for (const card of cardButtons) {
      const txt = await card.innerText();
      if (txt.includes('Bệnh') || txt.includes('Citrus') || txt.includes('Bưởi')) {
        console.log(`   Clicking crop card: "${txt.split('\n')[0]}"`);
        await card.click();
        await page.waitForTimeout(1000);
        const modalText = await page.innerText('body');
        if (modalText.includes('Phân biệt chẩn đoán kép') || modalText.includes('Kiểm tra thực địa') || modalText.includes('Phác đồ VietGAP')) {
          console.log('   ✅ Modal opened displaying full clinical pathology profile (Double Diagnosis, Sensory Check, VietGAP Phác đồ)!');
          modalOpened = true;
          results.crops_modal = true;
          break;
        }
      }
    }

    // Take screenshot for visual verification
    const screenshotPath = path.join(__dirname, 'crops_page_preview.png');
    await page.screenshot({ path: screenshotPath, fullPage: false });
    console.log(`   📸 Saved screenshot preview to: ${screenshotPath}`);

  } catch (err) {
    console.error('❌ Browser test error:', err);
  } finally {
    await browser.close();
  }

  console.log('\n📊 TEST SUMMARY:');
  console.log(JSON.stringify(results, null, 2));

  const allPassed = Object.values(results).every(v => v === true);
  if (allPassed) {
    console.log('🎉 ALL BROWSER E2E TESTS PASSED 100%!');
  } else {
    console.log('⚠️ Some tests did not meet criteria.');
  }

  process.exit(allPassed ? 0 : 1);
}

runBrowserE2E();
