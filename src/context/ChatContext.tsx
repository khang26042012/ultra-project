'use client';

import React, { createContext, useContext, useState, useEffect, useRef } from 'react';
import { Conversation, Message, ModelOption, ThemeMode } from '@/types/chat';

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
  isStreaming: boolean;
  createNewChat: () => void;
  selectConversation: (id: string) => void;
  deleteConversation: (id: string) => void;
  renameConversation: (id: string, newTitle: string) => void;
  sendMessage: (content: string, thinkActive?: boolean) => Promise<void>;
  userProfile: {
    name: string;
    email: string;
    plan: string;
    initials: string;
  };
}

const ChatContext = createContext<ChatContextType | undefined>(undefined);

export function ChatProvider({ children }: { children: React.ReactNode }) {
  const [conversations, setConversations] = useState<Conversation[]>(INITIAL_CONVERSATIONS);
  const [activeConversationId, setActiveConversationId] = useState<string | null>(null);
  const [selectedModel, setSelectedModel] = useState<string>('ag/gemini-3.8-flash-high');
  const [theme, setThemeState] = useState<ThemeMode>('dark');
  const [isSidebarOpen, setIsSidebarOpen] = useState<boolean>(true);
  const [isSettingsOpen, setIsSettingsOpen] = useState<boolean>(false);
  const [isUpgradeOpen, setIsUpgradeOpen] = useState<boolean>(false);
  const [isStreaming, setIsStreaming] = useState<boolean>(false);
  const abortControllerRef = useRef<AbortController | null>(null);

  // Apply theme class to HTML element
  const setTheme = (newTheme: ThemeMode) => {
    setThemeState(newTheme);
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

  useEffect(() => {
    document.documentElement.classList.add('dark');
  }, []);

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
    setConversations((prev) => prev.filter((c) => c.id !== id));
    if (activeConversationId === id) {
      setActiveConversationId(null);
    }
  };

  const renameConversation = (id: string, newTitle: string) => {
    setConversations((prev) =>
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
      setConversations((prev) => [newConv, ...prev]);
      setActiveConversationId(targetConvId);
      currentMessages = [userMessage];
    } else {
      const conv = conversations.find((c) => c.id === targetConvId);
      currentMessages = conv ? [...conv.messages, userMessage] : [userMessage];
      setConversations((prev) =>
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

    setConversations((prev) =>
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

      // Mark streaming complete
      setConversations((prev) =>
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
      setConversations((prev) =>
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
    name: 'phabtronfkhang',
    email: 'khang26042012@gmail.com',
    plan: 'Pro Plan',
    initials: 'AV',
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
