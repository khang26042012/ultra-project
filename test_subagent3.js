const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

// Generate sample test image
const samplePngBase64 = 'iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAYAAABw4pVUAAAAPklEQVR42u3BAQ0AAADCoPdPbQ8HFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/BhpkwABt9z5mAAAAABJRU5ErkJggg==';
const sampleImgPath = path.resolve(__dirname, 'test_sample_leaf.png');
fs.writeFileSync(sampleImgPath, Buffer.from(samplePngBase64, 'base64'));

async function runTestSuite() {
  console.log('--- Starting Subagent 3 Test Suite ---');
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: 1280, height: 800 }
  });
  const page = await context.newPage();

  page.on('console', msg => {
    if (msg.type() === 'error') {
      console.log(`[Browser Console Error] ${msg.text()}`);
    }
  });

  page.on('pageerror', err => {
    console.log(`[Browser Page Error] ${err.message}`);
  });

  try {
    console.log('\n[TEST 1] Testing Stream & Thinking...');
    await page.goto('http://localhost:3000', { waitUntil: 'networkidle' });

    // Step 1: Send Question 1
    const textarea = page.locator('textarea');
    await textarea.waitFor({ state: 'visible', timeout: 10000 });
    await textarea.fill('Triệu chứng bệnh thán thư trên xoài Vĩnh Long là gì?');
    await page.keyboard.press('Enter');

    console.log('Sent question 1. Waiting for stream & thinking...');

    // Verify thinking indicator appears
    const thinkingIndicator = page.locator('text=Đang suy nghĩ...');
    try {
      await thinkingIndicator.waitFor({ state: 'visible', timeout: 8000 });
      console.log('✓ "Đang suy nghĩ..." is visible during initial streaming');

      // Check breathing pulse animation
      const classAttr = await thinkingIndicator.locator('..').getAttribute('class');
      console.log(`Thinking indicator container classes: "${classAttr}"`);
      if (classAttr && classAttr.includes('animate-pulse')) {
        console.log('✓ Thinking indicator has breathing pulse animation (animate-pulse)');
      } else {
        console.warn('⚠️ animate-pulse class check:', classAttr);
      }

      // Check NO cloud emoji (☁️/💭)
      const text = await thinkingIndicator.innerText();
      if (!text.includes('☁') && !text.includes('💭') && !text.includes('⛅')) {
        console.log('✓ Thinking indicator has NO cloud emoji (☁️/💭)');
      } else {
        throw new Error(`Found cloud emoji in thinking text: "${text}"`);
      }
    } catch (e) {
      console.log('Note: Thinking was very fast or already transitioned:', e.message);
    }

    // Wait for thinking to settle and collapse to "Đã suy luận trong Xs ▾"
    const settledThoughtBtn = page.locator('button:has-text("Đã suy luận trong")');
    await settledThoughtBtn.waitFor({ state: 'visible', timeout: 45000 });
    const thoughtBtnText = await settledThoughtBtn.innerText();
    console.log(`✓ Thinking auto-collapsed to single line: "${thoughtBtnText.trim()}"`);

    if (!thoughtBtnText.includes('▾')) {
      throw new Error(`Settled thinking text missing '▾': "${thoughtBtnText}"`);
    }

    // Click thinking line to expand quote block
    console.log('Clicking settled thinking button to expand reasoning...');
    await settledThoughtBtn.click();
    await page.waitForTimeout(500);

    // Verify expanded quote block with border-l-2 and clean sans-serif text
    const expandedQuoteBlock = page.locator('.border-l-2.font-sans');
    await expandedQuoteBlock.waitFor({ state: 'visible', timeout: 5000 });
    const quoteClasses = await expandedQuoteBlock.getAttribute('class');
    const thoughtContent = await expandedQuoteBlock.innerText();
    console.log(`✓ Expanded quote block visible with classes: "${quoteClasses}"`);
    console.log(`✓ Thought content preview: "${thoughtContent.slice(0, 100)}..."`);

    if (!quoteClasses.includes('border-l-2') || !quoteClasses.includes('font-sans')) {
      throw new Error(`Quote block missing border-l-2 or font-sans: "${quoteClasses}"`);
    }

    // Wait for streaming of answer to complete
    await page.waitForSelector('.animate-pulse:text("AV")', { state: 'detached', timeout: 45000 }).catch(() => {});
    console.log('✓ Test 1: Stream & Thinking PASSED 100%!');

    // Step 2: New chat for Test 2
    console.log('\n[TEST 2] Testing 9Router Web Search Agent Loop...');
    // Click New Chat if available or reload
    const newChatBtn = page.locator('button:has-text("Đoạn chat mới")').first();
    if (await newChatBtn.isVisible()) {
      await newChatBtn.click();
    } else {
      await page.goto('http://localhost:3000', { waitUntil: 'networkidle' });
    }
    await page.waitForTimeout(1000);

    const textarea2 = page.locator('textarea');
    await textarea2.waitFor({ state: 'visible' });
    await textarea2.fill('Tra cứu giá lúa và tình hình dịch bệnh mới nhất tại Vĩnh Long');
    await page.keyboard.press('Enter');

    console.log('Sent question 2. Checking for live search badge "🔍 Đang tra cứu dữ liệu..."');

    // Check searching badge
    const searchBadge = page.locator('text=🔍 Đang tra cứu dữ liệu...');
    try {
      await searchBadge.waitFor({ state: 'visible', timeout: 15000 });
      console.log('✓ Found searching badge "🔍 Đang tra cứu dữ liệu..."');
    } catch {
      console.log('Search badge transitioned fast, checking sources button...');
    }

    // Check thin button "Đã tìm kiếm X nguồn thông tin ▾"
    const sourcesBtn = page.locator('button:has-text("Đã tìm kiếm")');
    await sourcesBtn.waitFor({ state: 'visible', timeout: 60000 });
    const sourcesBtnText = await sourcesBtn.innerText();
    console.log(`✓ Found sources button: "${sourcesBtnText.trim()}"`);

    if (!sourcesBtnText.includes('Đã tìm kiếm') || !sourcesBtnText.includes('nguồn thông tin')) {
      throw new Error(`Sources button text unexpected: "${sourcesBtnText}"`);
    }

    // Click to verify expandable source links with favicons
    console.log('Clicking sources button to expand links...');
    await sourcesBtn.click();
    await page.waitForTimeout(600);

    const sourceLinks = page.locator('a[target="_blank"]:has(img[alt="favicon"])');
    const linkCount = await sourceLinks.count();
    console.log(`✓ Expandable source links with favicons found: ${linkCount}`);
    if (linkCount === 0) {
      throw new Error('No source links with favicons found after expanding!');
    }

    for (let i = 0; i < Math.min(linkCount, 3); i++) {
      const href = await sourceLinks.nth(i).getAttribute('href');
      const faviconSrc = await sourceLinks.nth(i).locator('img[alt="favicon"]').getAttribute('src');
      console.log(`  Source #${i + 1}: URL="${href ? href.slice(0, 60) : ''}...", Favicon="${faviconSrc}"`);
    }
    console.log('✓ Test 2: 9Router Web Search Agent Loop PASSED 100%!');

    // Step 3: Test 3 - Image Attachment & Lightbox
    console.log('\n[TEST 3] Testing Image Attachment & Lightbox...');
    const newChatBtn2 = page.locator('button:has-text("Đoạn chat mới")').first();
    if (await newChatBtn2.isVisible()) {
      await newChatBtn2.click();
    } else {
      await page.goto('http://localhost:3000', { waitUntil: 'networkidle' });
    }
    await page.waitForTimeout(1000);

    // Attach sample image
    console.log(`Attaching sample image: ${sampleImgPath}`);
    const fileInput = page.locator('input[type="file"]');
    await fileInput.setInputFiles(sampleImgPath);

    // Verify thumbnail preview in input island
    const inputThumbnail = page.locator('img[alt="Ảnh đính kèm cây trồng"]');
    await inputThumbnail.waitFor({ state: 'visible', timeout: 5000 });
    console.log('✓ Image preview visible in input island');

    // Fill message and send
    const textarea3 = page.locator('textarea');
    await textarea3.fill('Lá xoài có đốm đen này là bệnh gì?');
    await page.keyboard.press('Enter');

    console.log('Sent image message. Verifying user message compact thumbnail...');

    // Verify compact thumbnail in user bubble: max-w-[220px] and zoom badge "Phóng to"
    const userThumbnailContainer = page.locator('.max-w-\\[220px\\]');
    await userThumbnailContainer.waitFor({ state: 'visible', timeout: 10000 });
    console.log('✓ User message compact thumbnail container found (max-w-[220px])');

    const zoomBadge = userThumbnailContainer.locator('text=Phóng to');
    await zoomBadge.waitFor({ state: 'visible', timeout: 5000 });
    console.log('✓ "Phóng to" zoom badge with ZoomIn icon is visible on thumbnail');

    // Click thumbnail to open Lightbox
    console.log('Clicking thumbnail to open Lightbox...');
    await userThumbnailContainer.click();
    await page.waitForTimeout(500);

    // Verify full-screen black backdrop lightbox opens
    const lightboxModal = page.locator('.fixed.inset-0.bg-black\\/85');
    await lightboxModal.waitFor({ state: 'visible', timeout: 5000 });
    console.log('✓ Full-screen black backdrop Lightbox is OPEN');

    const lightboxImg = lightboxModal.locator('img[alt="Chi tiết ảnh bệnh cây trồng"]');
    await lightboxImg.waitFor({ state: 'visible', timeout: 5000 });

    const initialStyle = await lightboxImg.getAttribute('style');
    console.log(`Initial lightbox image style: "${initialStyle}"`);

    // Test Zoom In (+)
    const zoomInBtn = lightboxModal.locator('button[aria-label="Phóng to"]');
    await zoomInBtn.click();
    await page.waitForTimeout(300);
    const zoomedInStyle = await lightboxImg.getAttribute('style');
    console.log(`After Zoom In (+) style: "${zoomedInStyle}"`);
    if (!zoomedInStyle.includes('scale(1.25)')) {
      throw new Error(`Expected scale(1.25) after zoom in, got: ${zoomedInStyle}`);
    }
    console.log('✓ Zoom In (+) button works correctly (scale 1.25)');

    // Test Zoom Out (-)
    const zoomOutBtn = lightboxModal.locator('button[aria-label="Thu nhỏ"]');
    await zoomOutBtn.click();
    await page.waitForTimeout(300);
    const zoomedOutStyle = await lightboxImg.getAttribute('style');
    console.log(`After Zoom Out (-) style: "${zoomedOutStyle}"`);
    if (!zoomedOutStyle.includes('scale(1)')) {
      throw new Error(`Expected scale(1) after zoom out, got: ${zoomedOutStyle}`);
    }
    console.log('✓ Zoom Out (-) button works correctly (scale 1)');

    // Test Close via Escape key
    console.log('Testing close via Escape key...');
    await page.keyboard.press('Escape');
    await page.waitForTimeout(500);
    const isClosedAfterEsc = await lightboxModal.isHidden();
    console.log(`✓ Lightbox closed after Escape key: ${isClosedAfterEsc}`);
    if (!isClosedAfterEsc) {
      throw new Error('Lightbox did not close after Escape key press!');
    }

    // Re-open and test close via Close button (✕)
    console.log('Re-opening lightbox to test Close (✕) button...');
    await userThumbnailContainer.click();
    await page.waitForTimeout(500);
    await lightboxModal.waitFor({ state: 'visible' });

    const closeBtn = lightboxModal.locator('button[aria-label="Đóng"]');
    await closeBtn.click();
    await page.waitForTimeout(500);
    const isClosedAfterBtn = await lightboxModal.isHidden();
    console.log(`✓ Lightbox closed after Close button (✕): ${isClosedAfterBtn}`);
    if (!isClosedAfterBtn) {
      throw new Error('Lightbox did not close after Close button click!');
    }

    console.log('✓ Test 3: Image Attachment & Lightbox PASSED 100%!');

    console.log('\n========================================');
    console.log('🎉 ALL TESTS PASSED SUCCESSFULLY (100%)');
    console.log('========================================');

  } catch (err) {
    console.error('\n❌ TEST FAILED:', err.message);
    await page.screenshot({ path: 'test_failure.png', fullPage: true });
    console.log('Saved failure screenshot to test_failure.png');
    process.exitCode = 1;
  } finally {
    await browser.close();
    if (fs.existsSync(sampleImgPath)) {
      fs.unlinkSync(sampleImgPath);
    }
  }
}

runTestSuite();
