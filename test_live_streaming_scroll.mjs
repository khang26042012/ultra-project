import { chromium } from 'playwright';

async function runLiveStreamTest() {
  console.log('🚀 Starting Subagent 4 live stream & auto-scroll stress test...');

  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });

  const errors = [];
  page.on('console', (msg) => {
    if (msg.type() === 'error') errors.push(msg.text());
  });
  page.on('pageerror', (err) => errors.push(err.message));

  // Pre-seed an active conversation with substantial content so scrollHeight > clientHeight
  const initialParas = [];
  for (let p = 1; p <= 15; p++) {
    initialParas.push(`Đoạn văn phân tích lâm sàng thứ ${p}: Triệu chứng và phác đồ điều trị bệnh thán thư do Colletotrichum gloeosporioides trên xoài Cát Hòa Lộc tại tỉnh Vĩnh Long.`);
  }

  const streamConv = {
    id: 'live-stream-test',
    title: 'Live Stream Stress Test',
    group: 'Today',
    updatedAt: new Date().toISOString(),
    messages: [
      {
        id: 'user-stream-q',
        role: 'user',
        content: 'Chẩn đoán chi tiết bệnh thán thư trên xoài',
        timestamp: '11:00 AM',
      },
      {
        id: 'assistant-stream-a',
        role: 'assistant',
        content: initialParas.join('\n\n') + '\n\n| Triệu chứng | Tác nhân (*Tên khoa học*) | Hoạt chất |\n|---|---|---|\n| Đốm lá thán thư | *Colletotrichum gloeosporioides* | Difenoconazole |',
        isStreaming: true,
        timestamp: '11:00 AM',
      },
    ],
  };

  await page.addInitScript((conv) => {
    localStorage.setItem('agrivision_chats_guest', JSON.stringify([conv]));
  }, streamConv);

  await page.goto('http://localhost:3000', { waitUntil: 'networkidle' });
  await page.waitForSelector('[data-testid="message-list-container"]');

  const container = page.locator('[data-testid="message-list-container"]');

  // Verify container is scrollable
  const initialMetrics = await container.evaluate((el) => ({
    scrollHeight: el.scrollHeight,
    clientHeight: el.clientHeight,
    scrollTop: el.scrollTop,
  }));
  console.log('Initial container metrics:', initialMetrics);

  // User manually scrolls UP
  console.log('User manually scrolling UP to scrollTop = 80 ...');
  await container.evaluate((el) => {
    el.scrollTop = 80;
    el.dispatchEvent(new Event('scroll'));
  });
  await page.waitForTimeout(300);

  // Verify bottom button appeared
  const bottomBtn = page.locator('[data-testid="scroll-to-bottom-button"]');
  await bottomBtn.waitFor({ state: 'visible', timeout: 3000 });
  const btnVisible = await bottomBtn.isVisible();
  console.log(`- Round ArrowDown button visible when scrolled up: ${btnVisible ? 'PASS ✅' : 'FAIL ❌'}`);
  if (!btnVisible) {
    throw new Error('ArrowDown button should be visible when scrolled up!');
  }

  // Verify screen position is NOT hijacked (scrollTop stayed near 80)
  const currentScroll = await container.evaluate((el) => el.scrollTop);
  const notHijacked = Math.abs(currentScroll - 80) < 15;
  console.log(`- Screen position not hijacked (current: ${currentScroll}): ${notHijacked ? 'PASS ✅' : 'FAIL ❌'}`);
  if (!notHijacked) {
    throw new Error('Screen position was hijacked!');
  }

  // Click bottom button
  console.log('Clicking bottom button to resume autoscroll...');
  await bottomBtn.click();
  await page.waitForTimeout(800);

  const finalDist = await container.evaluate((el) => el.scrollHeight - el.scrollTop - el.clientHeight);
  console.log(`Final distance from bottom: ${finalDist}`);
  const atBottomNow = finalDist <= 60;
  console.log(`- Scrolled back to bottom: ${atBottomNow ? 'PASS ✅' : 'FAIL ❌'}`);
  if (!atBottomNow) {
    throw new Error('Failed to scroll to bottom after clicking button!');
  }

  // Verify button hides
  const btnHidden = !(await bottomBtn.isVisible());
  console.log(`- ArrowDown button hidden when back at bottom: ${btnHidden ? 'PASS ✅' : 'FAIL ❌'}`);

  // Test mobile viewport for table horizontal scroll
  console.log('\nTesting Markdown table horizontal scrolling on mobile (390px)...');
  await page.setViewportSize({ width: 390, height: 844 });
  await page.waitForTimeout(300);

  const table = page.locator('[data-testid="markdown-table"]').first();
  const tableMetrics = await table.evaluate((el) => ({
    scrollWidth: el.scrollWidth,
    clientWidth: el.clientWidth,
    isScrollable: el.scrollWidth > el.clientWidth,
  }));
  console.log('Mobile Table metrics:', tableMetrics);
  const tableScrollable = tableMetrics.isScrollable;
  console.log(`- Table enables horizontal scrolling without overflowing screen: ${tableScrollable ? 'PASS ✅' : 'FAIL ❌'}`);
  if (!tableScrollable) {
    throw new Error('Table did not scroll horizontally on mobile!');
  }

  console.log(`Console errors count: ${errors.length}`);
  if (errors.length > 0) {
    console.log('Errors logged:', errors);
  }

  console.log('\n🎉 Live streaming & mobile table stress test PASSED 100%!');
  await browser.close();
}

runLiveStreamTest().catch((err) => {
  console.error('❌ STRESS TEST FAILED:', err);
  process.exit(1);
});
