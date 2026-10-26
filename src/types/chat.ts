export type Role = 'user' | 'assistant' | 'system' | 'tool';

export interface SearchSource {
  title: string;
  url: string;
  snippet?: string;
  favicon?: string;
}

export interface Message {
  id: string;
  role: Role;
  content: string;
  imageUrl?: string;
  timestamp: string;
  isStreaming?: boolean;
  thought?: string;
  isThinking?: boolean;
  thinkingSeconds?: number;
  searchingQuery?: string;
  sources?: SearchSource[];
  model?: string;
}

export type TimeGroup = 'Today' | 'Yesterday' | 'Previous 7 Days';

export interface Conversation {
  id: string;
  title: string;
  messages: Message[];
  updatedAt: string;
  group: TimeGroup;
  isPinned?: boolean;
}

export interface ModelOption {
  id: string;
  name: string;
  description: string;
  badge?: string;
  isDefault?: boolean;
}

export type ThemeMode = 'dark' | 'light' | 'system';
export type FontSizeOption = 'small' | 'medium' | 'large';

export interface User {
  id: string;
  name: string;
  email: string;
  passwordHash: string;
  createdAt: string;
  avatar_url?: string;
}
