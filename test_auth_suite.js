const { chromium } = require('playwright');
const { createClient } = require('@supabase/supabase-js');
const path = require('path');
const fs = require('fs');

const SUPABASE_URL = 'https://dffycwpkbfnaqptuvvju.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRmZnljd3BrYmZuYXFwdHV2dmp1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTI5NDA4NzgsImV4cCI6MjEwODUxNjg3OH0.hHWZ0haM0sxF_X9mKawdd39bmVp_TdAQKonikyf04Yk';
const supabase = createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

const SCREENSHOT_DIR = 'C:/Users/khangmc/.gemini/antigravity/brain/e4b2dc00-824a-4854-b60b-f4f14a465b2c/scratch';

async function runTestSuite() {
  console.log('=== STARTING AGRIVISION AUTH PLAYWRIGHT TEST SUITE (WITH SCREENSHOTS) ===');
  const timestamp = Date.now();
  const testEmail = `test_incognito_${timestamp}@agrivision.vn`;
  const testName = 'Nguyen Van Test';
  const testPassword = '123456';
  const wrongPassword = 'wrong_password_999';
  const testConvId = `conv-${timestamp}`;
  const testConvTitle = 'Chẩn đoán bệnh thối rễ sầu riêng';

  console.log(`Test user: ${testEmail} / ${testPassword}`);

  const browser = await chromium.launch({ headless: true });
  const results = {
    step1_register: false,
    step1_supabase_stored: false,
    step2_logout: false,
    step2_login: false,
    step3_incognito_login: false,
    step3_conversations_loaded: false,
    step4_wrong_password_error: false,
    step4_duplicate_email_error: false,
    screenshots: [],
    all_passed: false,
  };

  let registeredUserId = null;

  try {
    // -------------------------------------------------------------
    // Context 1: Registration, Logout, Login
    // -------------------------------------------------------------
    const context = await browser.newContext({ viewport: { width: 1280, height: 800 } });
    const page = await context.newPage();

    page.on('console', msg => {
      if (msg.type() === 'error') {
        console.log(`[Browser Console Error]: ${msg.text()}`);
      }
    });

    console.log('\n--- Step 1: Register a new user ---');
    await page.goto('http://localhost:3000', { waitUntil: 'networkidle' });

    // Find and click Auth Modal trigger
    const authBtn = page.getByRole('button', { name: 'Đăng nhập / Đăng ký' });
    await authBtn.waitFor({ state: 'visible', timeout: 8000 });
    console.log('Found "Đăng nhập / Đăng ký" button. Clicking...');
    await authBtn.click();

    // In modal, click "Đăng ký"
    const registerTab = page.locator('button[type="button"]').filter({ hasText: /^Đăng ký$/ });
    await registerTab.waitFor({ state: 'visible', timeout: 5000 });
    await registerTab.click();
    console.log('Switched to Register mode.');

    // Fill form
    const nameInput = page.locator('input[placeholder*="Phan Trọng Khang"]');
    const emailInput = page.locator('input[type="email"]');
    const passInputs = page.locator('input[type="password"]');

    await nameInput.fill(testName);
    await emailInput.fill(testEmail);
    await passInputs.first().fill(testPassword);
    await passInputs.nth(1).fill(testPassword);

    console.log('Form filled. Submitting registration...');
    const submitBtn = page.locator('button[type="submit"]');
    await submitBtn.click();

    // Wait for modal to close / user profile to appear in sidebar
    const profileSelector = page.locator('aside').getByText(testName, { exact: true });
    await profileSelector.waitFor({ state: 'visible', timeout: 10000 });
    console.log('User registered and logged in successfully in UI!');
    results.step1_register = true;

    // Screenshot 1: Registered & Logged in
    const ss1 = path.join(SCREENSHOT_DIR, '01_registered_logged_in.png');
    await page.screenshot({ path: ss1 });
    results.screenshots.push(ss1);

    // Verify in Supabase profiles
    console.log('Verifying profile in Supabase database...');
    const { data: dbProfile, error: dbErr } = await supabase
      .from('profiles')
      .select('*')
      .eq('email', testEmail)
      .maybeSingle();

    if (dbErr || !dbProfile) {
      throw new Error(`Profile not found in Supabase: ${dbErr ? dbErr.message : 'no record'}`);
    }
    registeredUserId = dbProfile.id;
    console.log('Supabase profile verified:', {
      id: dbProfile.id,
      email: dbProfile.email,
      name: dbProfile.name,
      password_hash: dbProfile.password_hash
    });
    if (dbProfile.name === testName && dbProfile.password_hash === testPassword) {
      results.step1_supabase_stored = true;
    } else {
      throw new Error('Supabase profile field mismatch');
    }

    // Insert a test conversation in Supabase for this user to test cloud sync in incognito
    const { error: convInsertErr } = await supabase.from('conversations').insert({
      id: testConvId,
      user_id: registeredUserId,
      title: testConvTitle,
      model: 'ag/gemini-3.8-flash-high',
      updated_at: new Date().toISOString()
    });
    if (convInsertErr) {
      console.warn('Conv insert warning:', convInsertErr);
    } else {
      console.log(`Inserted test conversation "${testConvTitle}" into Supabase.`);
    }

    // -------------------------------------------------------------
    // Step 2: Logout and Login again
    // -------------------------------------------------------------
    console.log('\n--- Step 2: Logout and Login again ---');
    // Click user profile to open ProfileMenu
    const profileBar = page.locator('aside').getByText(testName, { exact: true });
    await profileBar.click();

    const logoutBtn = page.locator('button:has-text("Đăng xuất tài khoản")');
    await logoutBtn.waitFor({ state: 'visible', timeout: 5000 });
    console.log('Clicking logout button...');
    await logoutBtn.click();

    // Verify logged out
    await authBtn.waitFor({ state: 'visible', timeout: 5000 });
    console.log('Logged out verified (Auth button visible again).');
    results.step2_logout = true;

    // Screenshot 2: Logged out
    const ss2 = path.join(SCREENSHOT_DIR, '02_logged_out.png');
    await page.screenshot({ path: ss2 });
    results.screenshots.push(ss2);

    // Open login modal
    await authBtn.click();
    const loginTab = page.locator('button[type="button"]').filter({ hasText: /^Đăng nhập$/ });
    await loginTab.click();

    // Fill login form
    await page.locator('input[type="email"]').fill(testEmail);
    await page.locator('input[type="password"]').fill(testPassword);
    await page.locator('button[type="submit"]').click();

    // Verify logged in again
    await profileSelector.waitFor({ state: 'visible', timeout: 10000 });
    console.log('Login successful! Profile displayed.');
    results.step2_login = true;

    // -------------------------------------------------------------
    // Step 3: Incognito Mode / Clean context test
    // -------------------------------------------------------------
    console.log('\n--- Step 3: Incognito Mode / Clean context test ---');
    const incognitoContext = await browser.newContext({ viewport: { width: 1280, height: 800 } });
    const incognitoPage = await incognitoContext.newPage();

    incognitoPage.on('console', msg => {
      if (msg.type() === 'error') {
        console.log(`[Incognito Console Error]: ${msg.text()}`);
      }
    });

    await incognitoPage.goto('http://localhost:3000', { waitUntil: 'networkidle' });

    // Verify clean state
    const incognitoAuthBtn = incognitoPage.getByRole('button', { name: 'Đăng nhập / Đăng ký' });
    await incognitoAuthBtn.waitFor({ state: 'visible', timeout: 8000 });
    console.log('Incognito context verified clean (Logged out state).');

    // Login in incognito
    await incognitoAuthBtn.click();
    await incognitoPage.locator('button[type="button"]').filter({ hasText: /^Đăng nhập$/ }).click();
    await incognitoPage.locator('input[type="email"]').fill(testEmail);
    await incognitoPage.locator('input[type="password"]').fill(testPassword);
    await incognitoPage.locator('button[type="submit"]').click();

    const incognitoProfileSelector = incognitoPage.locator('aside').getByText(testName, { exact: true });
    await incognitoProfileSelector.waitFor({ state: 'visible', timeout: 10000 });
    console.log('Incognito login succeeded 100%!');
    results.step3_incognito_login = true;

    // Verify conversations loaded state from Supabase Cloud DB
    console.log('Verifying conversations loaded from Supabase into incognito session...');
    const convLocator = incognitoPage.locator(`aside span:has-text("${testConvTitle}")`);
    await convLocator.waitFor({ state: 'visible', timeout: 10000 });
    console.log(`Verified conversation loaded from Supabase Cloud: "${testConvTitle}"`);
    results.step3_conversations_loaded = true;

    // Screenshot 3: Incognito logged in with conversation from cloud
    const ss3 = path.join(SCREENSHOT_DIR, '03_incognito_logged_in_with_conv.png');
    await incognitoPage.screenshot({ path: ss3 });
    results.screenshots.push(ss3);

    // -------------------------------------------------------------
    // Step 4: Error handling test
    // -------------------------------------------------------------
    console.log('\n--- Step 4: Error handling test ---');

    // 4A: Wrong password test
    // Logout in incognito page first
    const incognitoProfileBar = incognitoPage.locator('aside').getByText(testName, { exact: true });
    await incognitoProfileBar.click();
    const incognitoLogoutBtn = incognitoPage.locator('button:has-text("Đăng xuất tài khoản")');
    await incognitoLogoutBtn.waitFor({ state: 'visible', timeout: 5000 });
    await incognitoLogoutBtn.click();
    await incognitoAuthBtn.waitFor({ state: 'visible', timeout: 5000 });

    // Try logging in with wrong password
    await incognitoAuthBtn.click();
    await incognitoPage.locator('button[type="button"]').filter({ hasText: /^Đăng nhập$/ }).click();
    await incognitoPage.locator('input[type="email"]').fill(testEmail);
    await incognitoPage.locator('input[type="password"]').fill(wrongPassword);
    await incognitoPage.locator('button[type="submit"]').click();

    // Check error message "Mật khẩu không chính xác"
    const errorMsgLocator = incognitoPage.locator('div.text-red-600, div.text-red-400');
    await errorMsgLocator.waitFor({ state: 'visible', timeout: 5000 });
    const errorText = await errorMsgLocator.textContent();
    console.log(`Wrong password error message received: "${errorText}"`);

    // Screenshot 4: Wrong password error alert
    const ss4 = path.join(SCREENSHOT_DIR, '04_wrong_password_error.png');
    await incognitoPage.screenshot({ path: ss4 });
    results.screenshots.push(ss4);

    if (errorText && errorText.includes('Mật khẩu không chính xác')) {
      results.step4_wrong_password_error = true;
      console.log('Wrong password error verified: PASSED');
    } else {
      console.error(`Unexpected wrong password error text: ${errorText}`);
    }

    // 4B: Try registering an existing email
    console.log('Testing duplicate registration error...');
    const incognitoRegisterTab = incognitoPage.locator('button[type="button"]').filter({ hasText: /^Đăng ký$/ });
    await incognitoRegisterTab.click();

    await incognitoPage.locator('input[placeholder*="Phan Trọng Khang"]').fill('Nguyen Van Duplicate');
    await incognitoPage.locator('input[type="email"]').fill(testEmail);
    const incognitoPassInputs = incognitoPage.locator('input[type="password"]');
    await incognitoPassInputs.first().fill('differentPass123');
    await incognitoPassInputs.nth(1).fill('differentPass123');

    await incognitoPage.locator('button[type="submit"]').click();

    await errorMsgLocator.waitFor({ state: 'visible', timeout: 5000 });
    const duplicateErrorText = await errorMsgLocator.textContent();
    console.log(`Duplicate registration error message received: "${duplicateErrorText}"`);

    // Screenshot 5: Duplicate registration error
    const ss5 = path.join(SCREENSHOT_DIR, '05_duplicate_email_error.png');
    await incognitoPage.screenshot({ path: ss5 });
    results.screenshots.push(ss5);

    if (duplicateErrorText && (duplicateErrorText.includes('Email này đã tồn tại') || duplicateErrorText.includes('đã được đăng ký'))) {
      results.step4_duplicate_email_error = true;
      console.log('Duplicate email registration error verified: PASSED');
    } else {
      console.error(`Unexpected duplicate error text: ${duplicateErrorText}`);
    }

    // Clean up created test conversation and profile from Supabase
    console.log('\n--- Cleaning up test records from Supabase ---');
    if (registeredUserId) {
      await supabase.from('messages').delete().eq('conversation_id', testConvId);
      await supabase.from('conversations').delete().eq('user_id', registeredUserId);
    }
    const { error: delError } = await supabase.from('profiles').delete().eq('email', testEmail);
    if (delError) {
      console.warn('Note: Failed to delete test profile:', delError.message);
    } else {
      console.log('Test profile and conversations cleanly removed from Supabase.');
    }

    results.all_passed = (
      results.step1_register &&
      results.step1_supabase_stored &&
      results.step2_logout &&
      results.step2_login &&
      results.step3_incognito_login &&
      results.step3_conversations_loaded &&
      results.step4_wrong_password_error &&
      results.step4_duplicate_email_error
    );

    console.log('\n=== ALL PLAYWRIGHT TEST SUITE VERIFICATIONS COMPLETED ===');
    console.log(JSON.stringify(results, null, 2));

    if (results.all_passed) {
      console.log('\n🎉 ALL 5 TEST SUITE REQUIREMENTS PASSED 100%!');
    } else {
      console.error('\n⚠️ SOME CHECKS DID NOT PASS 100%!');
      process.exit(1);
    }

  } catch (err) {
    console.error('\n❌ Test Suite Failed with Error:', err);
    if (registeredUserId) {
      await supabase.from('conversations').delete().eq('user_id', registeredUserId);
      await supabase.from('profiles').delete().eq('email', testEmail);
    }
    process.exit(1);
  } finally {
    await browser.close();
  }
}

runTestSuite();
