const { chromium } = require('playwright');

async function testContextMenu() {
  console.log('🚀 Testing Clean Header & ChatGPT Context Menu in Sidebar...');
  const browser = await chromium.launch({ channel: 'msedge', headless: true });
  const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });

  try {
    await page.goto('http://localhost:3000', { waitUntil: 'networkidle', timeout: 15000 });

    // 1. Verify Clean Header: no 1.500+ link
    console.log('1️⃣ Verifying Clean Header...');
    const headerCropsLink = await page.$('header a[href="/crops"]');
    if (headerCropsLink) {
      console.error('❌ Header still contains /crops link');
      process.exit(1);
    }
    console.log('   ✅ Header is completely clean: no "1.500+" button on header');

    // 2. Inject mock conversations into localStorage: 1 pinned, 1 unpinned
    console.log('2️⃣ Injecting mock conversations with isPinned flag...');
    await page.evaluate(() => {
      const convs = [
        {
          id: 'conv-pinned-1',
          title: 'Sầu riêng xì mủ',
          group: 'Today',
          isPinned: true,
          updatedAt: new Date().toISOString(),
          messages: [{ id: 'm1', role: 'user', content: 'test', timestamp: '10:00' }],
        },
        {
          id: 'conv-recent-1',
          title: 'Vàng lá bưởi Năm Roi',
          group: 'Today',
          isPinned: false,
          updatedAt: new Date().toISOString(),
          messages: [{ id: 'm2', role: 'user', content: 'test 2', timestamp: '10:05' }],
        },
      ];
      localStorage.setItem('agrivision_chats_guest', JSON.stringify(convs));
    });

    await page.reload({ waitUntil: 'networkidle' });
    await page.waitForTimeout(1000);

    // Open sidebar
    console.log('3️⃣ Opening AppSidebar...');
    const visibleToggle = page.locator('button[title*="Mở sidebar"]:visible');
    if (await visibleToggle.count() > 0) {
      await visibleToggle.first().click();
      await page.waitForTimeout(1000);
    }

    const bodyText = await page.innerText('body');
    const hasPinnedHeader = bodyText.includes('ĐÃ GHIM') || bodyText.includes('Đã ghim');
    console.log(`   Pinned Section "ĐÃ GHIM" rendered: ${hasPinnedHeader ? '✅' : '❌'}`);

    // Check for 3-dots MoreHorizontal button
    console.log('4️⃣ Checking for 3-dots Context Menu button...');
    const moreBtn = await page.$('button[title="Tùy chọn đoạn chat"]');
    if (!moreBtn) {
      console.error('❌ 3-dots button not found');
      process.exit(1);
    }
    console.log('   ✅ Found 3-dots MoreHorizontal button');

    // Click 3-dots button to open ChatGPT Context Menu
    console.log('5️⃣ Clicking 3-dots button to trigger ChatGPT Context Menu...');
    await moreBtn.click();
    await page.waitForTimeout(500);

    const menuText = await page.innerText('body');
    const hasPinOption = menuText.includes('Ghim') || menuText.includes('Bỏ ghim');
    const hasRenameOption = menuText.includes('Đổi tên');
    const hasDeleteOption = menuText.includes('Xoá');

    console.log(`   Context Menu "Ghim/Bỏ ghim": ${hasPinOption ? '✅' : '❌'}`);
    console.log(`   Context Menu "Đổi tên": ${hasRenameOption ? '✅' : '❌'}`);
    console.log(`   Context Menu "Xoá" (red): ${hasDeleteOption ? '✅' : '❌'}`);

    const allPassed = !headerCropsLink && hasPinnedHeader && hasPinOption && hasRenameOption && hasDeleteOption;
    console.log(`\n🎉 Verification: ${allPassed ? 'ALL PASSED 100%!' : 'FAILED'}`);
    await browser.close();
    process.exit(allPassed ? 0 : 1);
  } catch (err) {
    console.error('Error during test:', err);
    await browser.close();
    process.exit(1);
  }
}

testContextMenu();
