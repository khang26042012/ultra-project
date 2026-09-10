# 🚨 NHIỆM VỤ SỬA LỖI ĐĂNG KÝ / ĐĂNG NHẬP (LỖI TAB ẨN DANH / ĐĂNG XUẤT KHÔNG ĐĂNG NHẬP ĐƯỢC)

### Nguyên nhân gốc rễ (Root Cause):
Hiện tại trong `src/context/ChatContext.tsx`:
1. Hàm `login` chỉ đọc từ `localStorage.getItem('agrivision_users')` chứ **HOÀN TOÀN KHÔNG TRUY VẤN SUPABASE CLOUD DATABASE**!
   - Khi vào bằng **Tab ẩn danh (Incognito)** hoặc trên thiết bị/trình duyệt khác, `localStorage` trắng tinh ➔ Hàm `login` luôn báo lỗi: *"Email hoặc mật khẩu không chính xác"*.
2. Hàm `register` và `syncProfileToSupabase` chỉ lưu `id`, `email`, `name` mà **KHÔNG LƯU CỘT `password_hash` LÊN SUPABASE**!
   *(Cột `password_hash` trên bảng `public.profiles` của Supabase đã được chạy lệnh ALTER TABLE sẵn sàng)*.

---

## 🛠️ HƯỚNG DẪN SỬA MÃ NGUỒN TẠI: `src/context/ChatContext.tsx`

Mở tệp `src/context/ChatContext.tsx` và cập nhật 3 hàm sau:

### 1. Cập nhật `syncProfileToSupabase`: Lưu thêm `password_hash`
```typescript
  const syncProfileToSupabase = useCallback(async (user: User) => {
    try {
      await supabase.from('profiles').upsert({
        id: user.id,
        email: user.email.toLowerCase().trim(),
        name: user.name,
        password_hash: user.passwordHash,
        role: 'farmer',
        updated_at: new Date().toISOString(),
      });
    } catch (err) {
      console.warn('Supabase profile sync error:', err);
    }
  }, []);
```

### 2. Cập nhật `register`: Kiểm tra và lưu trực tiếp lên Supabase
```typescript
  const register = async (name: string, email: string, password: string) => {
    try {
      const cleanEmail = email.toLowerCase().trim();

      // 1. Kiểm tra email đã tồn tại trên Supabase chưa
      const { data: existingUser } = await supabase
        .from('profiles')
        .select('id')
        .eq('email', cleanEmail)
        .maybeSingle();

      if (existingUser) {
        return { success: false, error: 'Email này đã được đăng ký trên hệ thống' };
      }

      // 2. Tạo đối tượng User mới
      const newUser: User = {
        id: `user-${Date.now()}`,
        name: name.trim(),
        email: cleanEmail,
        passwordHash: password,
        createdAt: new Date().toISOString(),
      };

      // 3. Lưu vào Supabase Cloud Database
      const { error: insertError } = await supabase.from('profiles').upsert({
        id: newUser.id,
        email: newUser.email,
        name: newUser.name,
        password_hash: password,
        role: 'farmer',
        updated_at: new Date().toISOString(),
      });

      if (insertError) {
        console.warn('Lỗi ghi Supabase:', insertError);
      }

      // 4. Lưu bản sao vào localStorage để hoạt động tức thì
      let users: User[] = [];
      try {
        const localUsers = localStorage.getItem('agrivision_users');
        if (localUsers) users = JSON.parse(localUsers);
      } catch {}
      users = users.filter((u) => u.email.toLowerCase() !== cleanEmail);
      users.push(newUser);
      localStorage.setItem('agrivision_users', JSON.stringify(users));
      localStorage.setItem('agrivision_current_user', JSON.stringify(newUser));

      setCurrentUser(newUser);

      // 5. Di chuyển các đoạn chat khách (guest) sang tài khoản mới
      const guestKey = getChatStorageKey();
      const guestChats = localStorage.getItem(guestKey);
      if (guestChats) {
        try {
          const parsed: Conversation[] = JSON.parse(guestChats);
          if (Array.isArray(parsed) && parsed.length > 0) {
            localStorage.setItem(getChatStorageKey(newUser.id), guestChats);
            setConversations(parsed);
            for (const conv of parsed) {
              syncConversationToSupabase(conv, newUser.id);
            }
          }
        } catch {}
      }

      return { success: true };
    } catch (err: unknown) {
      return { success: false, error: (err as Error)?.message || 'Lỗi đăng ký tài khoản' };
    }
  };
```

### 3. Cập nhật `login`: Truy vấn Supabase Cloud Database trước (Hỗ trợ tab ẩn danh & đa thiết bị 100%)
```typescript
  const login = async (email: string, password: string) => {
    try {
      const cleanEmail = email.toLowerCase().trim();

      // 1. Truy vấn trực tiếp tài khoản từ Supabase Cloud Database
      const { data: dbUser, error: dbError } = await supabase
        .from('profiles')
        .select('*')
        .eq('email', cleanEmail)
        .maybeSingle();

      if (dbUser) {
        // Kiểm tra mật khẩu từ Supabase
        if (dbUser.password_hash !== password) {
          return { success: false, error: 'Mật khẩu không chính xác' };
        }

        const loggedUser: User = {
          id: dbUser.id,
          name: dbUser.name || 'Người dùng',
          email: dbUser.email,
          passwordHash: dbUser.password_hash || password,
          createdAt: dbUser.created_at || new Date().toISOString(),
        };

        // Lưu session vào localStorage của tab/thiết bị hiện tại
        localStorage.setItem('agrivision_current_user', JSON.stringify(loggedUser));
        setCurrentUser(loggedUser);

        // Đồng bộ danh sách users cục bộ
        try {
          let users: User[] = [];
          const localUsers = localStorage.getItem('agrivision_users');
          if (localUsers) users = JSON.parse(localUsers);
          users = users.filter((u) => u.email.toLowerCase() !== cleanEmail);
          users.push(loggedUser);
          localStorage.setItem('agrivision_users', JSON.stringify(users));
        } catch {}

        // Tải toàn bộ danh sách hội thoại từ Cloud về
        await loadConversationsForUser(loggedUser.id);
        return { success: true };
      }

      // 2. Dự phòng: Nếu mất mạng hoặc không thấy trên DB, kiểm tra localStorage
      let localUsers: User[] = [];
      try {
        const raw = localStorage.getItem('agrivision_users');
        if (raw) localUsers = JSON.parse(raw);
      } catch {}

      const localMatch = localUsers.find(
        (u) => u.email.toLowerCase() === cleanEmail && u.passwordHash === password
      );

      if (localMatch) {
        localStorage.setItem('agrivision_current_user', JSON.stringify(localMatch));
        setCurrentUser(localMatch);
        syncProfileToSupabase(localMatch);
        await loadConversationsForUser(localMatch.id);
        return { success: true };
      }

      return { success: false, error: 'Email hoặc mật khẩu không chính xác' };
    } catch (err: unknown) {
      return { success: false, error: (err as Error)?.message || 'Lỗi đăng nhập' };
    }
  };
```

---

## 🚀 KIỂM THỬ VÀ PUSH:
```bash
npm run build
git add -A
git commit -m "fix(auth): authenticate directly via Supabase database to support incognito and multi-device login"
git push origin main
```
Render sẽ tự động deploy bản sửa lỗi lên: **https://ultra-project.onrender.com**.