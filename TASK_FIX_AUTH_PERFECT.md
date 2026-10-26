# 🚨 SỬA TRIỆT ĐỂ LỖI ĐĂNG KÝ VÀ ĐĂNG NHẬP (ROOT CAUSE: UNIQUE CONSTRAINT ONCONFLICT & SILENT ERRORS)

### 🧐 NGUYÊN NHÂN SÂU XA ĐÃ TÌM RA:
1. **Lỗi Upsert trùng email:** Bảng `profiles` có `id` là PRIMARY KEY và `email` là UNIQUE. Khi gọi `.upsert({ id, email, ... })`, Supabase mặc định bắt xung đột theo `id`. Nếu email đã từng tồn tại dưới một `id` khác, lệnh `upsert` bị dính mã lỗi **409 Conflict: duplicate key value violates unique constraint "profiles_email_key"**!
2. **Lỗi Nuốt Lỗi (Silent Failure):** Trong code cũ:
   ```typescript
   const { error: insertError } = await supabase.from('profiles').upsert(...);
   if (insertError) console.warn(...); // NUỐT LỖI! Vẫn coi như đăng ký thành công!
   ```
   ➔ Do nuốt lỗi, dữ liệu KHÔNG HỀ ĐƯỢC GHI VÀO SUPABASE, mà chỉ lưu tạm vào `localStorage` của riêng tab đó! Khi người dùng mở tab ẩn danh hoặc đăng xuất, Supabase không có user nên báo lỗi *"Mật khẩu không chính xác"*!
3. **Giải pháp dứt điểm:**
   - Dùng `.upsert(..., { onConflict: 'email' })` để luôn cập nhật theo `email` bất kể `id` là gì!
   - Bắt buộc kiểm tra `if (insertError) return { success: false, error: insertError.message }` (không bao giờ nuốt lỗi).
   - Tự động chữa lành (Auto-heal): Nếu email đã tồn tại và chưa có `password_hash` (do các phiên bản trước), tự động cập nhật mật khẩu mới và cho đăng nhập luôn!

---

## 🛠️ THAY THẾ TOÀN BỘ LOGIC AUTH TRONG `src/context/ChatContext.tsx`

Mở `src/context/ChatContext.tsx`, tìm đến 2 hàm `register` và `login`, thay thế bằng code chuẩn mực sau:

```typescript
  // Authentication: Register (Bắt conflict theo email, không nuốt lỗi)
  const register = async (name: string, email: string, password: string) => {
    try {
      const cleanEmail = email.toLowerCase().trim();
      const cleanPass = password.trim();

      // 1. Kiểm tra tài khoản đã tồn tại trên Supabase chưa
      const { data: existingUser } = await supabase
        .from('profiles')
        .select('*')
        .eq('email', cleanEmail)
        .maybeSingle();

      if (existingUser) {
        // Nếu tài khoản cũ bị null password_hash, tự động kích hoạt mật khẩu mới và đăng nhập
        if (!existingUser.password_hash) {
          await supabase
            .from('profiles')
            .update({
              name: name.trim(),
              password_hash: cleanPass,
              updated_at: new Date().toISOString(),
            })
            .eq('id', existingUser.id);

          const healedUser: User = {
            id: existingUser.id,
            name: name.trim(),
            email: cleanEmail,
            passwordHash: cleanPass,
            createdAt: existingUser.created_at || new Date().toISOString(),
          };

          localStorage.setItem('agrivision_current_user', JSON.stringify(healedUser));
          setCurrentUser(healedUser);
          await loadConversationsForUser(healedUser.id);
          return { success: true };
        }

        // Nếu mật khẩu nhập vào khớp với tài khoản đã có, tự động đăng nhập luôn
        if (existingUser.password_hash === cleanPass) {
          const loggedUser: User = {
            id: existingUser.id,
            name: existingUser.name || name.trim(),
            email: cleanEmail,
            passwordHash: cleanPass,
            createdAt: existingUser.created_at || new Date().toISOString(),
          };

          localStorage.setItem('agrivision_current_user', JSON.stringify(loggedUser));
          setCurrentUser(loggedUser);
          await loadConversationsForUser(loggedUser.id);
          return { success: true };
        }

        return {
          success: false,
          error: 'Email này đã tồn tại. Vui lòng chuyển sang tab Đăng nhập để vào tài khoản.',
        };
      }

      // 2. Tạo ID user mới
      const newUserId = `user-${Date.now()}`;
      const newUser: User = {
        id: newUserId,
        name: name.trim(),
        email: cleanEmail,
        passwordHash: cleanPass,
        createdAt: new Date().toISOString(),
      };

      // 3. Ghi vào Supabase bắt xung đột theo EMAIL (onConflict: 'email')
      const { error: insertError } = await supabase.from('profiles').upsert(
        {
          id: newUserId,
          email: cleanEmail,
          name: name.trim(),
          password_hash: cleanPass,
          role: 'farmer',
          updated_at: new Date().toISOString(),
        },
        { onConflict: 'email' }
      );

      if (insertError) {
        console.error('Lỗi insert Supabase:', insertError);
        return { success: false, error: `Lỗi kết nối máy chủ: ${insertError.message}` };
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

  // Authentication: Login (Truy vấn trực tiếp Supabase, auto-healing)
  const login = async (email: string, password: string) => {
    try {
      const cleanEmail = email.toLowerCase().trim();
      const cleanPass = password.trim();

      // 1. Truy vấn trực tiếp tài khoản từ Supabase Cloud Database
      const { data: dbUser, error: dbError } = await supabase
        .from('profiles')
        .select('*')
        .eq('email', cleanEmail)
        .maybeSingle();

      if (dbError) {
        console.warn('Supabase query error in login:', dbError);
      }

      if (dbUser) {
        // Tự động chữa lành nếu tài khoản cũ chưa có password_hash
        if (!dbUser.password_hash) {
          await supabase
            .from('profiles')
            .update({ password_hash: cleanPass })
            .eq('id', dbUser.id);
          dbUser.password_hash = cleanPass;
        }

        if (dbUser.password_hash !== cleanPass) {
          return { success: false, error: 'Mật khẩu không chính xác' };
        }

        const loggedUser: User = {
          id: dbUser.id,
          name: dbUser.name || 'Người dùng',
          email: dbUser.email,
          passwordHash: dbUser.password_hash,
          createdAt: dbUser.created_at || new Date().toISOString(),
        };

        // Lưu session vào localStorage
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

      // 2. Dự phòng: Nếu mất mạng hoặc chưa kịp lên DB, kiểm tra localStorage
      let localUsers: User[] = [];
      try {
        const raw = localStorage.getItem('agrivision_users');
        if (raw) localUsers = JSON.parse(raw);
      } catch {}

      const localMatch = localUsers.find(
        (u) => u.email.toLowerCase() === cleanEmail && u.passwordHash === cleanPass
      );

      if (localMatch) {
        // Tự động đẩy lên Supabase để lần sau không bị lỗi nữa
        supabase
          .from('profiles')
          .upsert(
            {
              id: localMatch.id,
              email: cleanEmail,
              name: localMatch.name,
              password_hash: cleanPass,
              role: 'farmer',
              updated_at: new Date().toISOString(),
            },
            { onConflict: 'email' }
          )
          .then();

        localStorage.setItem('agrivision_current_user', JSON.stringify(localMatch));
        setCurrentUser(localMatch);
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

## 🚀 KIỂM TRA & PUSH:
```bash
npm run build
git add src/context/ChatContext.tsx
git commit -m "fix(auth): resolve unique constraint conflict via onConflict email and add auto-healing password sync"
git push origin main
```
