'use client';

import React, { createContext, useContext, useState, useEffect, useRef, useCallback } from 'react';
import { Conversation, Message, ModelOption, ThemeMode, User, SearchSource, FontSizeOption } from '@/types/chat';
import { getInitials } from '@/lib/utils';
import { supabase } from '@/lib/supabase';

export const NINEROUTER_API_URL = 'http://nvnmc.asia:26627/v1/chat/completions';
export const NINEROUTER_API_KEY = 'sk-c276eac9b4322b74-tyrxri-1fc67c68';

export const AVAILABLE_MODELS: ModelOption[] = [
  {
    id: 'ag/gemini-3.8-flash-high',
    name: 'Gemini 3.8 Flash High',
    description: 'Mô hình suy luận lâm sàng chuyên sâu, bóc tách ca bệnh kép và tra cứu 9Router',
    badge: 'Khuyên dùng',
    isDefault: true,
  },
  {
    id: 'ag/gemini-3.8-flash',
    name: 'Gemini 3.8 Flash',
    description: 'Mô hình phản hồi siêu tốc, trả lời nhanh cho các câu hỏi phổ thông',
    badge: 'Nhanh',
  },
];

const INITIAL_CONVERSATIONS: Conversation[] = [];

interface ChatContextType {
  conversations: Conversation[];
  activeConversationId: string | null;
  activeConversation: Conversation | null;
  selectedModel: string;
  setSelectedModel: (model: string) => void;
  theme: ThemeMode;
  setTheme: (theme: ThemeMode) => void;
  fontSize: FontSizeOption;
  setFontSize: (size: FontSizeOption) => void;
  isWebSearchEnabled: boolean;
  setIsWebSearchEnabled: (enabled: boolean) => void;
  isAutoScrollEnabled: boolean;
  setIsAutoScrollEnabled: (enabled: boolean) => void;
  isSidebarOpen: boolean;
  setIsSidebarOpen: (open: boolean) => void;
  toggleSidebar: () => void;
  isSettingsOpen: boolean;
  setIsSettingsOpen: (open: boolean) => void;
  isHelpOpen: boolean;
  setIsHelpOpen: (open: boolean) => void;
  isUpgradeOpen: boolean;
  setIsUpgradeOpen: (open: boolean) => void;
  isAuthModalOpen: boolean;
  setIsAuthModalOpen: (open: boolean) => void;
  currentUser: User | null;
  login: (email: string, password: string) => Promise<{ success: boolean; error?: string }>;
  register: (name: string, email: string, password: string) => Promise<{ success: boolean; error?: string }>;
  logout: () => void;
  clearChatHistory: () => void;
  exportBackupJson: () => void;
  isStreaming: boolean;
  createNewChat: () => void;
  selectConversation: (id: string) => void;
  deleteConversation: (id: string) => void;
  renameConversation: (id: string, newTitle: string) => void;
  sendMessage: (content: string, imageUrl?: string, thinkActive?: boolean) => Promise<void>;
  userProfile: {
    name: string;
    email: string;
    plan?: string;
    initials: string;
  };
}

const ChatContext = createContext<ChatContextType | undefined>(undefined);

export function ChatProvider({ children }: { children: React.ReactNode }) {
  const [currentUser, setCurrentUser] = useState<User | null>(null);
  const [conversations, setConversations] = useState<Conversation[]>(INITIAL_CONVERSATIONS);
  const [activeConversationId, setActiveConversationId] = useState<string | null>(null);
  const [selectedModel, setSelectedModel] = useState<string>('ag/gemini-3.8-flash-high');
  const [theme, setThemeState] = useState<ThemeMode>('light');
  const [fontSize, setFontSizeState] = useState<FontSizeOption>('medium');
  const [isWebSearchEnabled, setIsWebSearchEnabledState] = useState<boolean>(true);
  const [isAutoScrollEnabled, setIsAutoScrollEnabledState] = useState<boolean>(true);
  const [isSidebarOpen, setIsSidebarOpen] = useState<boolean>(false);
  const [isSettingsOpen, setIsSettingsOpen] = useState<boolean>(false);
  const [isHelpOpen, setIsHelpOpen] = useState<boolean>(false);
  const [isUpgradeOpen, setIsUpgradeOpen] = useState<boolean>(false);
  const [isAuthModalOpen, setIsAuthModalOpen] = useState<boolean>(false);
  const [isStreaming, setIsStreaming] = useState<boolean>(false);
  const abortControllerRef = useRef<AbortController | null>(null);

  // Helper to resolve user-scoped storage key
  const getChatStorageKey = useCallback((userId?: string) => {
    return `agrivision_chats_${userId || 'guest'}`;
  }, []);

  // Supabase Sync Helpers
  const syncProfileToSupabase = useCallback(async (user: User) => {
    try {
      await supabase.from('profiles').upsert({
        id: user.id,
        email: user.email,
        name: user.name,
        role: 'farmer',
        updated_at: new Date().toISOString(),
      });
    } catch (err) {
      console.warn('Supabase profile sync error:', err);
    }
  }, []);

  const syncConversationToSupabase = useCallback(async (conv: Conversation, userId?: string) => {
    if (!userId) return;
    try {
      await supabase.from('conversations').upsert({
        id: conv.id,
        user_id: userId,
        title: conv.title,
        model: selectedModel,
        updated_at: new Date().toISOString(),
      });
    } catch (err) {
      console.warn('Supabase conversation sync error:', err);
    }
  }, [selectedModel]);

  const syncMessageToSupabase = useCallback(async (convId: string, msg: Message) => {
    try {
      await supabase.from('messages').upsert({
        id: msg.id,
        conversation_id: convId,
        role: msg.role,
        content: msg.content,
        image_url: msg.imageUrl || null,
        thought: msg.thought || null,
        sources: msg.sources ? JSON.parse(JSON.stringify(msg.sources)) : null,
        timestamp: msg.timestamp,
      });
    } catch (err) {
      console.warn('Supabase message sync error:', err);
    }
  }, []);

  const deleteConversationFromSupabase = useCallback(async (convId: string) => {
    try {
      await supabase.from('conversations').delete().eq('id', convId);
    } catch (err) {
      console.warn('Supabase delete conversation error:', err);
    }
  }, []);

  // Load conversations for user: Supabase Cloud -> fallback localStorage
  const loadConversationsForUser = useCallback(async (userId?: string) => {
    const key = getChatStorageKey(userId);
    let loaded: Conversation[] = [];

    // 1. Try Supabase Cloud DB first if logged in
    if (userId) {
      try {
        const { data: convData, error: convError } = await supabase
          .from('conversations')
          .select('*')
          .eq('user_id', userId)
          .order('updated_at', { ascending: false });

        if (!convError && Array.isArray(convData) && convData.length > 0) {
          const convIds = convData.map((c) => c.id);
          const { data: msgData, error: msgError } = await supabase
            .from('messages')
            .select('*')
            .in('conversation_id', convIds)
            .order('timestamp', { ascending: true });

          const messagesByConv: Record<string, Message[]> = {};
          if (!msgError && Array.isArray(msgData)) {
            for (const m of msgData) {
              if (!messagesByConv[m.conversation_id]) {
                messagesByConv[m.conversation_id] = [];
              }
              messagesByConv[m.conversation_id].push({
                id: m.id,
                role: m.role,
                content: m.content || '',
                imageUrl: m.image_url || undefined,
                thought: m.thought || undefined,
                sources: m.sources || undefined,
                timestamp: m.timestamp || new Date(m.created_at).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
              });
            }
          }

          loaded = convData.map((c) => ({
            id: c.id,
            title: c.title,
            group: 'Today',
            updatedAt: c.updated_at,
            messages: messagesByConv[c.id] || [],
          }));

          localStorage.setItem(key, JSON.stringify(loaded));
          setConversations(loaded);
          setActiveConversationId(loaded[0].id);
          return;
        }
      } catch (sbErr) {
        console.warn('Supabase load fallback to local:', sbErr);
      }
    }

    // 2. Fallback to LocalStorage
    try {
      const local = localStorage.getItem(key);
      if (local) {
        loaded = JSON.parse(local);
      }
    } catch {
      // ignore
    }

    setConversations(loaded || []);
    setActiveConversationId(loaded && loaded.length > 0 ? loaded[0].id : null);
  }, [getChatStorageKey]);

  // Apply theme class to HTML element with persistence
  const setTheme = (newTheme: ThemeMode) => {
    setThemeState(newTheme);
    try {
      localStorage.setItem('agrivision-theme', newTheme);
      if (currentUser) {
        localStorage.setItem(`agrivision_settings_${currentUser.id}`, JSON.stringify({ theme: newTheme }));
      }
    } catch {
      // ignore
    }
    const root = document.documentElement;
    if (newTheme === 'dark') {
      root.classList.add('dark');
    } else if (newTheme === 'light') {
      root.classList.remove('dark');
    } else {
      const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      if (prefersDark) {
        root.classList.add('dark');
      } else {
        root.classList.remove('dark');
      }
    }
  };

  // Font size setting with persistence
  const setFontSize = (size: FontSizeOption) => {
    setFontSizeState(size);
    try {
      localStorage.setItem('agrivision-font-size', size);
    } catch {
      // ignore
    }
    if (typeof document !== 'undefined') {
      document.documentElement.setAttribute('data-font-size', size);
      const sizeMap = { small: '13px', medium: '15px', large: '17px' };
      document.documentElement.style.setProperty('--app-font-size', sizeMap[size]);
    }
  };

  const setIsWebSearchEnabled = (enabled: boolean) => {
    setIsWebSearchEnabledState(enabled);
    try {
      localStorage.setItem('agrivision-web-search', enabled ? 'true' : 'false');
    } catch {
      // ignore
    }
  };

  const setIsAutoScrollEnabled = (enabled: boolean) => {
    setIsAutoScrollEnabledState(enabled);
    try {
      localStorage.setItem('agrivision-auto-scroll', enabled ? 'true' : 'false');
    } catch {
      // ignore
    }
  };

  // Initial load
  useEffect(() => {
    let initialTheme: ThemeMode = 'light';
    let initialFontSize: FontSizeOption = 'medium';
    let initialWebSearch = true;
    let initialAutoScroll = true;

    try {
      const savedTheme = localStorage.getItem('agrivision-theme') as ThemeMode | null;
      if (savedTheme === 'light' || savedTheme === 'dark' || savedTheme === 'system') {
        initialTheme = savedTheme;
      }
      const savedSize = localStorage.getItem('agrivision-font-size') as FontSizeOption | null;
      if (savedSize === 'small' || savedSize === 'medium' || savedSize === 'large') {
        initialFontSize = savedSize;
      }
      const savedSearch = localStorage.getItem('agrivision-web-search');
      if (savedSearch !== null) {
        initialWebSearch = savedSearch === 'true';
      }
      const savedScroll = localStorage.getItem('agrivision-auto-scroll');
      if (savedScroll !== null) {
        initialAutoScroll = savedScroll === 'true';
      }
    } catch {
      // ignore
    }

    setTheme(initialTheme);
    setFontSize(initialFontSize);
    setIsWebSearchEnabledState(initialWebSearch);
    setIsAutoScrollEnabledState(initialAutoScroll);

    if (typeof window !== 'undefined') {
      setIsSidebarOpen(window.innerWidth >= 768);

      try {
        const rawUser = localStorage.getItem('agrivision_current_user');
        if (rawUser) {
          const user: User = JSON.parse(rawUser);
          setCurrentUser(user);
          loadConversationsForUser(user.id);
        } else {
          loadConversationsForUser();
        }
      } catch {
        loadConversationsForUser();
      }
    }
  }, [loadConversationsForUser]);

  // Persist conversations to localStorage and Server
  const updateAndPersistConversations = useCallback(
    (updater: (prev: Conversation[]) => Conversation[]) => {
      setConversations((prev) => {
        const updated = updater(prev);
        try {
          const key = getChatStorageKey(currentUser?.id);
          localStorage.setItem(key, JSON.stringify(updated));
        } catch {
          // ignore
        }
        return updated;
      });
    },
    [currentUser?.id, getChatStorageKey]
  );

  // Authentication: Register
  const register = async (name: string, email: string, password: string) => {
    try {
      let users: User[] = [];
      const localUsers = localStorage.getItem('agrivision_users');
      if (localUsers) {
        users = JSON.parse(localUsers);
      }

      const existing = users.find((u) => u.email.toLowerCase() === email.toLowerCase());
      if (existing) {
        return { success: false, error: 'Email này đã được đăng ký trước đó' };
      }

      const newUser: User = {
        id: `user-${Date.now()}`,
        name,
        email,
        passwordHash: password,
        createdAt: new Date().toISOString(),
      };

      users.push(newUser);
      localStorage.setItem('agrivision_users', JSON.stringify(users));
      localStorage.setItem('agrivision_current_user', JSON.stringify(newUser));
      setCurrentUser(newUser);

      // Cloud profile sync
      syncProfileToSupabase(newUser);

      // Migrate guest chats to new user
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
        } catch {
          // ignore
        }
      }

      return { success: true };
    } catch (err: unknown) {
      return { success: false, error: (err as Error)?.message || 'Lỗi đăng ký tài khoản' };
    }
  };

  // Authentication: Login
  const login = async (email: string, password: string) => {
    try {
      let users: User[] = [];
      const localUsers = localStorage.getItem('agrivision_users');
      if (localUsers) {
        users = JSON.parse(localUsers);
      }

      const match = users.find(
        (u) => u.email.toLowerCase() === email.toLowerCase() && u.passwordHash === password
      );

      if (!match) {
        return { success: false, error: 'Email hoặc mật khẩu không chính xác' };
      }

      localStorage.setItem('agrivision_current_user', JSON.stringify(match));
      setCurrentUser(match);
      syncProfileToSupabase(match);
      await loadConversationsForUser(match.id);

      return { success: true };
    } catch (err: unknown) {
      return { success: false, error: (err as Error)?.message || 'Lỗi đăng nhập' };
    }
  };

  // Authentication: Logout
  const logout = () => {
    setCurrentUser(null);
    try {
      localStorage.removeItem('agrivision_current_user');
    } catch {
      // ignore
    }
    loadConversationsForUser();
  };

  // Clear chat history for current user
  const clearChatHistory = () => {
    if (currentUser?.id) {
      supabase.from('conversations').delete().eq('user_id', currentUser.id).then();
    }
    updateAndPersistConversations(() => []);
    setActiveConversationId(null);
  };

  // Export JSON Backup
  const exportBackupJson = () => {
    const backupData = {
      project: 'AgriVision',
      version: '1.0.0',
      exportDate: new Date().toISOString(),
      user: currentUser ? { id: currentUser.id, name: currentUser.name, email: currentUser.email } : null,
      conversations,
    };
    const jsonStr = JSON.stringify(backupData, null, 2);
    const blob = new Blob([jsonStr], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `agrivision-backup-${new Date().toISOString().slice(0, 10)}.json`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  const toggleSidebar = () => {
    setIsSidebarOpen((prev) => !prev);
  };

  const activeConversation = conversations.find((c) => c.id === activeConversationId) || null;

  const createNewChat = () => {
    if (abortControllerRef.current) {
      abortControllerRef.current.abort();
    }
    setIsStreaming(false);
    setActiveConversationId(null);
  };

  const selectConversation = (id: string) => {
    if (abortControllerRef.current) {
      abortControllerRef.current.abort();
    }
    setIsStreaming(false);
    setActiveConversationId(id);
  };

  const deleteConversation = (id: string) => {
    deleteConversationFromSupabase(id);
    updateAndPersistConversations((prev) => prev.filter((c) => c.id !== id));
    if (activeConversationId === id) {
      setActiveConversationId(null);
    }
  };

  const renameConversation = (id: string, newTitle: string) => {
    updateAndPersistConversations((prev) =>
      prev.map((c) => {
        if (c.id === id) {
          const updated = { ...c, title: newTitle };
          syncConversationToSupabase(updated, currentUser?.id);
          return updated;
        }
        return c;
      })
    );
  };

  // Multi-step Agent Loop with 9Router Web Search & Reasoning Streaming
  const sendMessage = async (content: string, imageUrl?: string, thinkActive = false) => {
    const trimmedContent = content.trim();
    if ((!trimmedContent && !imageUrl) || isStreaming) return;

    const userMessage: Message = {
      id: `user-${Date.now()}`,
      role: 'user',
      content: trimmedContent || (imageUrl ? 'Chẩn đoán hình ảnh bệnh cây đính kèm' : ''),
      imageUrl: imageUrl || undefined,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
    };

    let targetConvId = activeConversationId;
    let currentMessages: Message[] = [];

    if (!targetConvId) {
      const titleCandidate = trimmedContent || 'Chẩn đoán hình ảnh';
      const newTitle = titleCandidate.length > 32 ? `${titleCandidate.slice(0, 32)}...` : titleCandidate;
      targetConvId = `conv-${Date.now()}`;
      const newConv: Conversation = {
        id: targetConvId,
        title: newTitle,
        group: 'Today',
        updatedAt: new Date().toISOString(),
        messages: [userMessage],
      };
      updateAndPersistConversations((prev) => [newConv, ...prev]);
      setActiveConversationId(targetConvId);
      currentMessages = [userMessage];

      // Sync new conversation to Supabase
      syncConversationToSupabase(newConv, currentUser?.id);
    } else {
      const conv = conversations.find((c) => c.id === targetConvId);
      currentMessages = conv ? [...conv.messages, userMessage] : [userMessage];
      updateAndPersistConversations((prev) =>
        prev.map((c) =>
          c.id === targetConvId
            ? {
                ...c,
                messages: [...c.messages, userMessage],
                updatedAt: new Date().toISOString(),
              }
            : c
        )
      );
    }

    // Sync user message to Supabase
    syncMessageToSupabase(targetConvId, userMessage);

    // Set up placeholder for streaming response
    const aiMessageId = `ai-${Date.now()}`;
    const initialAiMessage: Message = {
      id: aiMessageId,
      role: 'assistant',
      content: '',
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      isStreaming: true,
      isThinking: thinkActive,
      thought: '',
    };

    updateAndPersistConversations((prev) =>
      prev.map((c) =>
        c.id === targetConvId
          ? { ...c, messages: [...c.messages, initialAiMessage] }
          : c
      )
    );

    setIsStreaming(true);
    abortControllerRef.current = new AbortController();

    // Prepare full API history for AI Gateway
    const apiMessages = currentMessages.map((m) => {
      if (m.imageUrl) {
        return {
          role: m.role,
          content: [
            { type: 'text', text: m.content || 'Chẩn đoán hình ảnh cây trồng' },
            { type: 'image_url', image_url: { url: m.imageUrl } },
          ],
        };
      }
      return {
        role: m.role,
        content: m.content,
      };
    });

    const startTime = Date.now();
    let accumulatedContent = '';
    let accumulatedThought = '';
    let isThinking = false;
    let thinkingSeconds = 0;
    let searchingQuery: string | undefined = undefined;
    let currentSources: SearchSource[] = [];

    try {
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          model: selectedModel || 'ag/gemini-3.8-flash-high',
          messages: apiMessages,
          webSearchEnabled: isWebSearchEnabled,
        }),
        signal: abortControllerRef.current.signal,
      });

      if (!response.ok) {
        const errorText = await response.text();
        throw new Error(`AI Gateway Error (${response.status}): ${errorText || response.statusText}`);
      }

      const reader = response.body?.getReader();
      const decoder = new TextDecoder('utf-8');

      if (reader) {
        let buffer = '';

        while (true) {
          const { value, done } = await reader.read();
          if (done) break;

          buffer += decoder.decode(value, { stream: true });
          const lines = buffer.split('\n');
          buffer = lines.pop() || '';

          for (const line of lines) {
            const trimmed = line.trim();
            if (!trimmed || trimmed.startsWith(':')) continue;
            if (trimmed === 'data: [DONE]') {
              break;
            }
            if (trimmed.startsWith('data: ')) {
              const dataStr = trimmed.slice(6);
              try {
                const parsed = JSON.parse(dataStr);

                // 1. Thinking / Reasoning token
                if (parsed.type === 'thought' && parsed.token) {
                  isThinking = true;
                  accumulatedThought += parsed.token;
                }
                // 2. Searching indicator
                else if (parsed.type === 'searching') {
                  searchingQuery = parsed.query;
                }
                // 3. Search sources returned from 9Router
                else if (parsed.type === 'sources' && Array.isArray(parsed.sources)) {
                  currentSources = [...currentSources, ...parsed.sources];
                  searchingQuery = undefined;
                }
                // 4. Content token
                else if (parsed.type === 'content' && parsed.token) {
                  if (isThinking) {
                    isThinking = false;
                    thinkingSeconds = Math.max(1, Math.round((Date.now() - startTime) / 1000));
                  }
                  accumulatedContent += parsed.token;
                }
                // 5. Fallback delta.content
                else if (parsed.choices?.[0]?.delta?.content) {
                  if (isThinking) {
                    isThinking = false;
                    thinkingSeconds = Math.max(1, Math.round((Date.now() - startTime) / 1000));
                  }
                  accumulatedContent += parsed.choices[0].delta.content;
                }

                setConversations((prev) =>
                  prev.map((c) =>
                    c.id === targetConvId
                      ? {
                          ...c,
                          messages: c.messages.map((m) =>
                            m.id === aiMessageId
                              ? {
                                  ...m,
                                  content: accumulatedContent,
                                  thought: accumulatedThought || undefined,
                                  isThinking,
                                  thinkingSeconds:
                                    thinkingSeconds ||
                                    (accumulatedThought
                                      ? Math.max(1, Math.round((Date.now() - startTime) / 1000))
                                      : undefined),
                                  searchingQuery,
                                  sources: currentSources.length > 0 ? currentSources : undefined,
                                  isStreaming: true,
                                }
                              : m
                          ),
                        }
                      : c
                  )
                );
              } catch {
                // Ignore incomplete JSON chunks in SSE stream
              }
            }
          }
        }
      }

      if (accumulatedThought && !thinkingSeconds) {
        thinkingSeconds = Math.max(1, Math.round((Date.now() - startTime) / 1000));
      }

      const finalAiMessage: Message = {
        id: aiMessageId,
        role: 'assistant',
        content: accumulatedContent,
        thought: accumulatedThought || undefined,
        isStreaming: false,
        isThinking: false,
        searchingQuery: undefined,
        thinkingSeconds:
          thinkingSeconds ||
          (accumulatedThought ? Math.max(1, Math.round((Date.now() - startTime) / 1000)) : undefined),
        sources: currentSources.length > 0 ? currentSources : undefined,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      };

      // Mark streaming complete and persist to storage
      updateAndPersistConversations((prev) =>
        prev.map((c) =>
          c.id === targetConvId
            ? {
                ...c,
                messages: c.messages.map((m) => (m.id === aiMessageId ? finalAiMessage : m)),
              }
            : c
        )
      );

      // Sync completed assistant message to Supabase
      syncMessageToSupabase(targetConvId, finalAiMessage);
    } catch (err: unknown) {
      if ((err as Error)?.name === 'AbortError') {
        console.log('Stream aborted');
        return;
      }
      console.error('AgriVision Streaming Error:', err);
      const errorMessage = (err as Error)?.message || 'An unexpected error occurred';
      updateAndPersistConversations((prev) =>
        prev.map((c) =>
          c.id === targetConvId
            ? {
                ...c,
                messages: c.messages.map((m) =>
                  m.id === aiMessageId
                    ? {
                        ...m,
                        content: `⚠️ **Lỗi kết nối AgriVision**: ${errorMessage}\n\nVui lòng kiểm tra lại đường truyền mạng.`,
                        isStreaming: false,
                        isThinking: false,
                        searchingQuery: undefined,
                      }
                    : m
                ),
              }
            : c
        )
      );
    } finally {
      setIsStreaming(false);
      abortControllerRef.current = null;
    }
  };

  const userProfile = {
    name: currentUser?.name || 'Khách',
    email: currentUser?.email || '',
    initials: currentUser ? getInitials(currentUser.name) : 'AV',
  };

  return (
    <ChatContext.Provider
      value={{
        conversations,
        activeConversationId,
        activeConversation,
        selectedModel,
        setSelectedModel,
        theme,
        setTheme,
        fontSize,
        setFontSize,
        isWebSearchEnabled,
        setIsWebSearchEnabled,
        isAutoScrollEnabled,
        setIsAutoScrollEnabled,
        isSidebarOpen,
        setIsSidebarOpen,
        toggleSidebar,
        isSettingsOpen,
        setIsSettingsOpen,
        isHelpOpen,
        setIsHelpOpen,
        isUpgradeOpen,
        setIsUpgradeOpen,
        isAuthModalOpen,
        setIsAuthModalOpen,
        currentUser,
        login,
        register,
        logout,
        clearChatHistory,
        exportBackupJson,
        isStreaming,
        createNewChat,
        selectConversation,
        deleteConversation,
        renameConversation,
        sendMessage,
        userProfile,
      }}
    >
      {children}
    </ChatContext.Provider>
  );
}

export function useChat() {
  const context = useContext(ChatContext);
  if (!context) {
    throw new Error('useChat must be used within a ChatProvider');
  }
  return context;
}
