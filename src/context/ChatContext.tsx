'use client';

import React, { createContext, useContext, useState, useEffect, useRef, useCallback } from 'react';
import { Conversation, Message, ModelOption, ThemeMode, User } from '@/types/chat';
import { getInitials } from '@/lib/utils';

export const NINEROUTER_API_URL = 'http://nvnmc.asia:26627/v1/chat/completions';
export const NINEROUTER_API_KEY = 'sk-c276eac9b4322b74-tyrxri-1fc67c68';

export const AVAILABLE_MODELS: ModelOption[] = [
  {
    id: 'ag/gemini-3.8-flash-high',
    name: 'Gemini 3.8 Flash High',
    description: 'High-reasoning profile of Gemini 3.8 for AgriVision',
    badge: 'Pro',
    isDefault: true,
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
  isSidebarOpen: boolean;
  setIsSidebarOpen: (open: boolean) => void;
  toggleSidebar: () => void;
  isSettingsOpen: boolean;
  setIsSettingsOpen: (open: boolean) => void;
  isUpgradeOpen: boolean;
  setIsUpgradeOpen: (open: boolean) => void;
  isAuthModalOpen: boolean;
  setIsAuthModalOpen: (open: boolean) => void;
  currentUser: User | null;
  login: (email: string, password: string) => Promise<{ success: boolean; error?: string }>;
  register: (name: string, email: string, password: string) => Promise<{ success: boolean; error?: string }>;
  logout: () => void;
  clearChatHistory: () => void;
  isStreaming: boolean;
  createNewChat: () => void;
  selectConversation: (id: string) => void;
  deleteConversation: (id: string) => void;
  renameConversation: (id: string, newTitle: string) => void;
  sendMessage: (content: string, thinkActive?: boolean) => Promise<void>;
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
  const [isSidebarOpen, setIsSidebarOpen] = useState<boolean>(false);
  const [isSettingsOpen, setIsSettingsOpen] = useState<boolean>(false);
  const [isUpgradeOpen, setIsUpgradeOpen] = useState<boolean>(false);
  const [isAuthModalOpen, setIsAuthModalOpen] = useState<boolean>(false);
  const [isStreaming, setIsStreaming] = useState<boolean>(false);
  const abortControllerRef = useRef<AbortController | null>(null);

  // Helper to resolve user-scoped storage key
  const getChatStorageKey = useCallback((userId?: string) => {
    return `agrivision_chats_${userId || 'guest'}`;
  }, []);

  // Sync chats to server storage
  const syncChatsToServer = useCallback(async (userId: string, data: Conversation[]) => {
    try {
      await fetch('/api/storage', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          type: 'sync_chats',
          userId,
          conversations: data,
        }),
      });
    } catch {
      // background sync fail safe
    }
  }, []);

  // Sync user to server storage
  const syncUserToServer = useCallback(async (user: User) => {
    try {
      await fetch('/api/storage', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          type: 'sync_user',
          user,
        }),
      });
    } catch {
      // background sync fail safe
    }
  }, []);

  // Load conversations for a specific user
  const loadConversationsForUser = useCallback(async (userId?: string) => {
    const key = getChatStorageKey(userId);
    let loaded: Conversation[] = [];

    try {
      const local = localStorage.getItem(key);
      if (local) {
        loaded = JSON.parse(local);
      }
    } catch {
      // ignore
    }

    // If local was empty and we have a logged-in user, fetch from server file
    if ((!loaded || loaded.length === 0) && userId) {
      try {
        const res = await fetch(`/api/storage?type=chats&userId=${encodeURIComponent(userId)}`);
        if (res.ok) {
          const srv = await res.json();
          if (Array.isArray(srv.conversations) && srv.conversations.length > 0) {
            loaded = srv.conversations;
            localStorage.setItem(key, JSON.stringify(loaded));
          }
        }
      } catch {
        // ignore
      }
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

  // Initial load
  useEffect(() => {
    let initialTheme: ThemeMode = 'light';
    try {
      const saved = localStorage.getItem('agrivision-theme') as ThemeMode | null;
      if (saved === 'light' || saved === 'dark' || saved === 'system') {
        initialTheme = saved;
      }
    } catch {
      // ignore
    }
    setTheme(initialTheme);

    if (typeof window !== 'undefined') {
      setIsSidebarOpen(window.innerWidth >= 768);

      // Check current session
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

  // Persist conversations to localStorage and Server whenever they update
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
        if (currentUser?.id) {
          syncChatsToServer(currentUser.id, updated);
        }
        return updated;
      });
    },
    [currentUser?.id, getChatStorageKey, syncChatsToServer]
  );

  // Authentication: Register
  const register = async (name: string, email: string, password: string) => {
    try {
      let users: User[] = [];
      const localUsers = localStorage.getItem('agrivision_users');
      if (localUsers) {
        users = JSON.parse(localUsers);
      } else {
        // Fallback check server
        const res = await fetch('/api/storage?type=users');
        if (res.ok) {
          const data = await res.json();
          users = data.users || [];
        }
      }

      const existing = users.find((u) => u.email.toLowerCase() === email.toLowerCase());
      if (existing) {
        return { success: false, error: 'Email này đã được đăng ký trước đó' };
      }

      const newUser: User = {
        id: `user-${Date.now()}`,
        name,
        email,
        passwordHash: password, // client-hashed/proto representation
        createdAt: new Date().toISOString(),
      };

      users.push(newUser);
      localStorage.setItem('agrivision_users', JSON.stringify(users));
      localStorage.setItem('agrivision_current_user', JSON.stringify(newUser));
      setCurrentUser(newUser);

      // Migrate guest chats to new user if any
      const guestKey = getChatStorageKey();
      const guestChats = localStorage.getItem(guestKey);
      if (guestChats) {
        try {
          const parsed = JSON.parse(guestChats);
          if (Array.isArray(parsed) && parsed.length > 0) {
            localStorage.setItem(getChatStorageKey(newUser.id), guestChats);
            setConversations(parsed);
            syncChatsToServer(newUser.id, parsed);
          }
        } catch {
          // ignore
        }
      }

      // Background sync to server JSON
      syncUserToServer(newUser);

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

      // Check server if not in local
      if (users.length === 0) {
        const res = await fetch('/api/storage?type=users');
        if (res.ok) {
          const data = await res.json();
          users = data.users || [];
          localStorage.setItem('agrivision_users', JSON.stringify(users));
        }
      }

      const match = users.find(
        (u) => u.email.toLowerCase() === email.toLowerCase() && u.passwordHash === password
      );

      if (!match) {
        return { success: false, error: 'Email hoặc mật khẩu không chính xác' };
      }

      localStorage.setItem('agrivision_current_user', JSON.stringify(match));
      setCurrentUser(match);
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
    updateAndPersistConversations(() => []);
    setActiveConversationId(null);
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
    updateAndPersistConversations((prev) => prev.filter((c) => c.id !== id));
    if (activeConversationId === id) {
      setActiveConversationId(null);
    }
  };

  const renameConversation = (id: string, newTitle: string) => {
    updateAndPersistConversations((prev) =>
      prev.map((c) => (c.id === id ? { ...c, title: newTitle } : c))
    );
  };

  // Real AI Streaming via AI Gateway (locked to ag/gemini-3.8-flash-high)
  const sendMessage = async (content: string, thinkActive = false) => {
    if (!content.trim() || isStreaming) return;

    const userMessage: Message = {
      id: `user-${Date.now()}`,
      role: 'user',
      content: content.trim(),
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
    };

    let targetConvId = activeConversationId;
    let currentMessages: Message[] = [];

    if (!targetConvId) {
      const newTitle = content.trim().length > 32 ? `${content.trim().slice(0, 32)}...` : content.trim();
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

    // Set up placeholder for streaming response
    const aiMessageId = `ai-${Date.now()}`;
    const initialAiMessage: Message = {
      id: aiMessageId,
      role: 'assistant',
      content: '',
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      isStreaming: true,
      thought: thinkActive ? 'AgriVision đang phân tích triệu chứng...' : undefined,
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

    // Prepare API history for AI Gateway
    const apiMessages = currentMessages.map((m) => ({
      role: m.role,
      content: m.content,
    }));

    try {
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          model: 'ag/gemini-3.8-flash-high',
          messages: apiMessages,
        }),
        signal: abortControllerRef.current.signal,
      });

      if (!response.ok) {
        const errorText = await response.text();
        throw new Error(`AI Gateway Error (${response.status}): ${errorText || response.statusText}`);
      }

      const reader = response.body?.getReader();
      const decoder = new TextDecoder('utf-8');
      let accumulatedContent = '';

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
                const token = parsed.choices?.[0]?.delta?.content || '';
                if (token) {
                  accumulatedContent += token;

                  setConversations((prev) =>
                    prev.map((c) =>
                      c.id === targetConvId
                        ? {
                            ...c,
                            messages: c.messages.map((m) =>
                              m.id === aiMessageId
                                ? { ...m, content: accumulatedContent, isStreaming: true }
                                : m
                            ),
                          }
                        : c
                    )
                  );
                }
              } catch {
                // Ignore incomplete JSON chunks in SSE stream
              }
            }
          }
        }
      }

      // Mark streaming complete and persist to storage
      updateAndPersistConversations((prev) =>
        prev.map((c) =>
          c.id === targetConvId
            ? {
                ...c,
                messages: c.messages.map((m) =>
                  m.id === aiMessageId
                    ? { ...m, isStreaming: false }
                    : m
                ),
              }
            : c
        )
      );
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
        isSidebarOpen,
        setIsSidebarOpen,
        toggleSidebar,
        isSettingsOpen,
        setIsSettingsOpen,
        isUpgradeOpen,
        setIsUpgradeOpen,
        isAuthModalOpen,
        setIsAuthModalOpen,
        currentUser,
        login,
        register,
        logout,
        clearChatHistory,
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
