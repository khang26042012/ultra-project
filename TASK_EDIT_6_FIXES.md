# 🛠️ NHIỆM VỤ EDIT DỰ ÁN AGRIVISION (ULTRA-PROJECT)

Thực hiện chỉnh sửa trực tiếp 6 vấn đề UI/UX và logic cuộn trang theo danh sách sau. Làm đúng từng tệp, test build sạch sẽ và commit lên nhánh `main`.

---

## 📌 1. XÓA BỎ HEADER Ở MOBILE (AVATAR + TÊN Ở GIỮA) & XÓA ĐƯỜNG KẺ XÁM NGANG
- **Tệp chỉnh sửa:** `src/app/page.tsx`
- **Vấn đề:** Trên điện thoại, phần avatar tròn `AV` và chữ `AgriVision` ở giữa thanh header gây rối mắt, và đường viền gạch ngang bên dưới (`border-b`) tạo cảm giác bị chia cắt thô.
- **Hành động cụ thể:**
  - Trong thẻ `<header className="md:hidden ...">`:
    - **Xóa bỏ hoàn toàn** thẻ `div` chứa avatar `AV` và chữ `AgriVision` ở giữa.
    - **Xóa bỏ** class viền `border-b border-[#e5e5e5]/80 dark:border-[#262626]/80` để header hoàn toàn liền mạch với nền trang.
    - Đổi layout header thành `flex items-center justify-between px-3 bg-transparent shrink-0 select-none`. Nút mở Sidebar (bên trái) và nút Chat mới (bên phải) vẫn giữ nguyên để người dùng thao tác.

---

## 📌 2. XỬ LÝ LỖI AI DÙNG `--` HOẶC `---` LÀM KHOẢNG CÁCH XUỐNG HÀNG
- **Tệp chỉnh sửa:**
  1. `src/components/chat/ChatMessage.tsx`
  2. `src/lib/systemPrompt.ts` & `src/lib/system_prompt.md`
- **Vấn đề:** Khi Gemini phân tích, nó hay chèn các dòng `---` hoặc `--` để ngăn cách các phần, nhưng hàm render hiện tại lại in thẳng ra chữ `---` trên màn hình.
- **Hành động cụ thể:**
  - **Trong `ChatMessage.tsx` (hàm `renderFormattedContent`):**
    Thêm đoạn nhận diện đường kẻ ngang Markdown trước khi in text thường:
    ```tsx
    // Horizontal Rule / Divider (--- hoặc *** hoặc --)
    if (/^(\-{2,}|\*{3,})$/.test(line.trim())) {
      elements.push(
        <hr
          key={i}
          className="my-3.5 border-t border-[#e5e5e5] dark:border-[#2a2a2a]"
        />
      );
      i++;
      continue;
    }
    ```
  - **Trong System Prompt (`systemPrompt.ts` & `system_prompt.md`):**
    Bổ sung chỉ thị định dạng:
    ```markdown
    - TUYỆT ĐỐI KHÔNG dùng ký tự gạch rời như "--" hoặc "---" làm khoảng trắng giả giữa các dòng. Hãy xuống dòng tự nhiên và phân chia nội dung rõ ràng bằng tiêu đề cấp 2 (##) hoặc cấp 3 (###).
    ```

---

## 📌 3. TỐI ƯU CÁC DẤU GẠCH ĐẦU DÒNG (BULLET POINTS) KHÔNG BỊ NHÔ RA TRƯỚC
- **Tệp chỉnh sửa:** `src/components/chat/ChatMessage.tsx`
- **Vấn đề:** Hiện tại dấu chấm tròn `•` đang dùng chung padding `pl-2` với đề mục số `1. `, làm dấu chấm bị thò ra ngoài khoảng cách, lệch nhịp so với nội dung cha phía trên.
- **Hành động cụ thể:**
  - Trong hàm `renderFormattedContent`, chỉnh lại cách render Bullet Points (`- ` hoặc `* `):
    - Đặt thụt lề chuẩn vào trong: `pl-5 my-1` (hoặc `ml-4`) để các ý phụ thụt lùi vào trong đề mục số thay vì đứng bằng hoặc thò ra ngoài.
    - Canh chỉnh chấm tròn gọn gàng:
    ```tsx
    if (line.trim().startsWith('- ') || line.trim().startsWith('* ')) {
      const text = line.trim().substring(2);
      elements.push(
        <div key={i} className="flex items-start gap-2.5 pl-4 sm:pl-5 my-1">
          <span className="w-1.5 h-1.5 rounded-full bg-[#8e8e8e] dark:bg-[#737373] mt-2.5 shrink-0" />
          <span className="leading-relaxed flex-1 text-[#262626] dark:text-[#d4d4d4]">
            {formatInlineMarkdown(text)}
          </span>
        </div>
      );
      i++;
      continue;
    }
    ```
  - Đối với đề mục số (`1. `, `2. `):
    ```tsx
    if (/^\d+\.\s/.test(line.trim())) {
      const match = line.trim().match(/^(\d+\.)\s(.*)/);
      if (match) {
        elements.push(
          <div key={i} className="flex items-start gap-2 pl-1 mt-2.5 mb-1 font-medium text-[#0d0d0d] dark:text-white">
            <span className="text-[#0d0d0d] dark:text-white shrink-0">{match[1]}</span>
            <span className="leading-relaxed flex-1">{formatInlineMarkdown(match[2])}</span>
          </div>
        );
        i++;
        continue;
      }
    }
    ```

---

## 📌 4. THIẾT KẾ LẠI GUI WEB SEARCH: GIỐNG Y NHƯ KHỐI THINKING (MỎNG NHẸ, CÓ NÚT ▾ ĐỂ XEM NGUỒN)
- **Tệp chỉnh sửa:** `src/components/chat/ChatMessage.tsx`
- **Vấn đề:** Nút nguồn tìm kiếm hiện tại là một khối pill đóng khung xám thô ráp (`px-3 py-1 rounded-full bg-[#f4f4f4] border`), không đồng bộ với thiết kế tối giản của Thinking.
- **Hành động cụ thể:**
  - **Bỏ hoàn toàn khung pill viền xám:**
  - Đổi nút mở nguồn thành **1 dòng text mỏng nhẹ** y như nút Thinking:
    ```tsx
    {/* Web Search Sources Dropdown: Tối giản chuẩn ChatGPT/Claude */}
    {message.sources && message.sources.length > 0 && (
      <div className="mb-2 select-none">
        <button
          type="button"
          onClick={() => setShowSources(!showSources)}
          className="inline-flex items-center gap-1 text-xs font-medium text-[#737373] hover:text-[#0d0d0d] dark:text-[#a3a3a3] dark:hover:text-white transition-colors cursor-pointer"
        >
          <span>Đã tìm kiếm {message.sources.length} nguồn thông tin</span>
          {showSources ? (
            <ChevronDown className="w-3 h-3" strokeWidth={2} />
          ) : (
            <ChevronRight className="w-3 h-3" strokeWidth={2} />
          )}
        </button>

        {showSources && (
          <div className="mt-2 pl-3.5 border-l-2 border-[#e5e5e5] dark:border-[#383838] space-y-2 py-1 max-h-60 overflow-y-auto">
            {message.sources.map((src, sIdx) => {
              let domain = '';
              try {
                domain = new URL(src.url).hostname.replace('www.', '');
              } catch {
                domain = 'web';
              }
              return (
                <a
                  key={sIdx}
                  href={src.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex flex-col group/src text-left p-1.5 rounded-lg hover:bg-black/5 dark:hover:bg-white/5 transition-colors"
                >
                  <div className="flex items-center gap-1.5 text-[11px] text-[#8e8e8e]">
                    <ExternalLink className="w-3 h-3 group-hover/src:text-[#0d0d0d] dark:group-hover/src:text-white" />
                    <span className="truncate font-mono">{domain}</span>
                  </div>
                  <div className="text-xs font-medium text-[#0d0d0d] dark:text-[#ececec] group-hover/src:underline line-clamp-1 mt-0.5">
                    {src.title}
                  </div>
                </a>
              );
            })}
          </div>
        )}
      </div>
    )}
    ```
  - Đối với trạng thái **Đang tìm kiếm (Live searching)**:
    - Loại bỏ hộp viền tròn thô.
    - Hiển thị dòng text mỏng nhẹ có animation thở:  
      `<div className="text-xs text-[#737373] dark:text-[#a3a3a3] animate-pulse mb-2 select-none font-medium">Đang tìm kiếm thông tin...</div>`

---

## 📌 5. SỬA PHẦN "ĐANG SUY NGHĨ": Y HỆT LÚC THINK XONG, LOẠI BỎ ICON ☁️ / 💭, CÓ HIỆU ỨNG ĐẬM → NHẠT → ĐẬM
- **Tệp chỉnh sửa:** `src/components/chat/ChatMessage.tsx`
- **Hành động cụ thể:**
  - Tìm khối render `isCurrentlyThinking`.
  - **Xóa bỏ hoàn toàn icon 💭 hoặc ☁️**.
  - Hiển thị dòng chữ `Đang suy nghĩ...` với kích thước và font chữ giống hệt dòng `Đã suy luận trong Xs ▾`, kèm animation nhấp nháy chuyển từ đậm sang nhạt:
    ```tsx
    {/* Live Streaming Thinking: Cùng style với lúc think xong, bỏ icon, hiệu ứng nhịp thở */}
    {isCurrentlyThinking && (
      <div className="inline-flex items-center text-xs font-medium text-[#737373] dark:text-[#a3a3a3] animate-pulse mb-2.5 select-none transition-opacity">
        <span>Đang suy nghĩ...</span>
      </div>
    )}
    ```

---

## 📌 6. KHẮC PHỤC LỖI KHÔNG KÉO LÊN ĐỌC TIN NHẮN CŨ KHI ĐANG STREAM & THÊM NÚT CUỘN XUỐNG CUỐI TRANG
- **Tệp chỉnh sửa:** `src/components/chat/MessageList.tsx` (và `src/app/page.tsx` nếu cần)
- **Vấn đề cốt lõi:** Hiện tại trong `MessageList.tsx`, mỗi khi có một token chữ bay về là `bottomRef.current?.scrollIntoView({ behavior: 'smooth' })` lại chạy liên tục, cướp quyền cuộn của người dùng khiến người dùng không thể kéo lên trên đọc tin nhắn cũ được!
- **Hành động cụ thể:**
  1. **Cơ chế Smart Auto-Scroll:** Chỉ tự động cuộn xuống nếu người dùng **đang ở gần đáy** (trong phạm vi 120px tính từ đáy). Nếu người dùng đã chủ động vuốt ngón tay kéo lên trên để đọc thì **DỪNG AUTO-SCROLL NGAY LẬP TỨC**!
  2. **Thêm nút Floating "Cuộn xuống cuối" (Scroll to Bottom Button):**
     - Khi người dùng cuộn lên trên (cách đáy > 150px), hiển thị một nút tròn nhỏ gọn nằm ở góc dưới bên phải (ngay phía trên ô nhập liệu).
     - Bấm vào nút này sẽ cuộn mượt xuống cuối trang và kích hoạt lại chế độ bám đáy.

- **Mã nguồn hoàn thiện cho `src/components/chat/MessageList.tsx`:**
  ```tsx
  'use client';

  import React, { useEffect, useRef, useState, useCallback } from 'react';
  import { Message } from '@/types/chat';
  import ChatMessage from './ChatMessage';
  import { ArrowDown } from 'lucide-react';

  interface MessageListProps {
    messages: Message[];
  }

  export default function MessageList({ messages }: MessageListProps) {
    const bottomRef = useRef<HTMLDivElement>(null);
    const containerRef = useRef<HTMLDivElement>(null);
    const [isAtBottom, setIsAtBottom] = useState(true);
    const [showScrollButton, setShowScrollButton] = useState(false);

    // Kiểm tra vị trí cuộn của người dùng
    const handleScroll = useCallback(() => {
      const scrollEl = containerRef.current?.parentElement;
      if (!scrollEl) return;

      const { scrollTop, scrollHeight, clientHeight } = scrollEl;
      const distanceFromBottom = scrollHeight - scrollTop - clientHeight;
      const nearBottom = distanceFromBottom < 120;

      setIsAtBottom(nearBottom);
      setShowScrollButton(distanceFromBottom > 200);
    }, []);

    // Gắn scroll event vào parent scroll container
    useEffect(() => {
      const scrollEl = containerRef.current?.parentElement;
      if (!scrollEl) return;

      scrollEl.addEventListener('scroll', handleScroll, { passive: true });
      return () => scrollEl.removeEventListener('scroll', handleScroll);
    }, [handleScroll]);

    // Chỉ tự động cuộn nếu người dùng ĐANG Ở ĐÁY
    useEffect(() => {
      if (isAtBottom) {
        bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
      }
    }, [messages, messages[messages.length - 1]?.content, isAtBottom]);

    const scrollToBottom = () => {
      const scrollEl = containerRef.current?.parentElement;
      if (scrollEl) {
        scrollEl.scrollTo({ top: scrollEl.scrollHeight, behavior: 'smooth' });
      } else {
        bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
      }
      setIsAtBottom(true);
      setShowScrollButton(false);
    };

    return (
      <div ref={containerRef} className="w-full max-w-3xl mx-auto px-3 sm:px-4 py-4 sm:py-6 relative">
        {messages.map((message) => (
          <ChatMessage key={message.id} message={message} />
        ))}
        <div ref={bottomRef} className="h-4" />

        {/* Nút cuộn xuống cuối trang khi người dùng kéo lên đọc tin cũ */}
        {showScrollButton && (
          <button
            type="button"
            onClick={scrollToBottom}
            title="Cuộn xuống tin nhắn mới nhất"
            className="fixed bottom-24 right-5 sm:right-8 z-30 p-2 rounded-full bg-white dark:bg-[#262626] text-[#0d0d0d] dark:text-white border border-[#e5e5e5] dark:border-[#383838] shadow-md hover:bg-[#f5f5f5] dark:hover:bg-[#333] transition-all cursor-pointer animate-fade-in"
          >
            <ArrowDown className="w-4 h-4" strokeWidth={2} />
          </button>
        )}
      </div>
    );
  }
  ```

---

## 🚀 QUY TRÌNH HOÀN TẤT & DEPLOY
Sau khi sửa đổi xong các tệp trên:
```bash
npm run build
git add -A
git commit -m "fix(ui): remove mobile header logo and border, fix hr divider, indent bullet points, minimal search sources UI, pulse thinking without icon, and smart auto-scroll with scroll-to-bottom button"
git push origin main
```
Render sẽ tự động trigger build và cập nhật giao diện trực tiếp tại: **https://ultra-project.onrender.com**.