import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"
import type { Conversation } from "@/types/chat"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

export function getInitials(name?: string): string {
  if (!name || !name.trim()) return 'AV';
  const parts = name.trim().split(/\s+/);
  if (parts.length === 1) {
    return parts[0].slice(0, 2).toUpperCase();
  }
  return (parts[0][0] + parts[parts.length - 1][0]).toUpperCase();
}

/**
 * Sinh ID chống va chạm (Collision-Resistant ID)
 * Sử dụng Web Crypto API randomUUID() tiêu chuẩn, kèm fallback an toàn.
 */
export function generateId(prefix: string = ''): string {
  if (typeof crypto !== 'undefined' && typeof crypto.randomUUID === 'function') {
    const uuid = crypto.randomUUID();
    return prefix ? `${prefix}-${uuid}` : uuid;
  }
  const time = Date.now().toString(36);
  const random = Math.random().toString(36).substring(2, 10);
  return prefix ? `${prefix}-${time}-${random}` : `${time}-${random}`;
}

/**
 * Lọc bỏ ảnh Base64 dung lượng cao (>30KB) để tránh cạn kiệt 5MB localStorage quota
 */
export function sanitizeConversationsForStorage(conversations: Conversation[]): Conversation[] {
  return conversations.map((conv) => ({
    ...conv,
    messages: conv.messages.map((m) => {
      const isHeavyImage = Boolean(m.imageUrl && m.imageUrl.length > 30000);
      const isHeavyAnnotated = Boolean(m.annotatedImageUrl && m.annotatedImageUrl.length > 30000);
      if (!isHeavyImage && !isHeavyAnnotated) return m;
      return {
        ...m,
        imageUrl: isHeavyImage ? '[Ảnh mẫu bệnh học đã lưu]' : m.imageUrl,
        annotatedImageUrl: isHeavyAnnotated ? undefined : m.annotatedImageUrl,
      };
    }),
  }));
}

/**
 * Ghi dữ liệu vào localStorage an toàn với cơ chế tự phục hồi LRU Pruning khi QuotaExceededError
 */
export function safeSetLocalStorage(key: string, conversations: Conversation[]): boolean {
  if (typeof window === 'undefined') return false;

  const sanitized = sanitizeConversationsForStorage(conversations);
  try {
    localStorage.setItem(key, JSON.stringify(sanitized));
    return true;
  } catch (err: unknown) {
    console.warn('LocalStorage quota reached. Kích hoạt thuật toán LRU Pruning...', err);
    try {
      // Cắt tỉa: chỉ giữ 25 hội thoại gần nhất, mỗi hội thoại cũ giữ tối đa 15 tin nhắn gần nhất
      const pruned = sanitized.slice(0, 25).map((conv, idx) => {
        if (idx <= 3) return conv; // Giữ nguyên 4 hội thoại mới nhất
        return {
          ...conv,
          messages: conv.messages.slice(-15),
        };
      });
      localStorage.setItem(key, JSON.stringify(pruned));
      return true;
    } catch (retryErr) {
      console.error('Không thể phục hồi dung lượng localStorage:', retryErr);
      return false;
    }
  }
}
