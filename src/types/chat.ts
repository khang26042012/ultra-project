export type Role = 'user' | 'assistant' | 'system';

export interface Message {
  id: string;
  role: Role;
  content: string;
  imageUrl?: string;
  timestamp: string;
  isStreaming?: boolean;
  thought?: string;
  model?: string;
}

export type TimeGroup = 'Today' | 'Yesterday' | 'Previous 7 Days';

export interface Conversation {
  id: string;
  title: string;
  messages: Message[];
  updatedAt: string;
  group: TimeGroup;
}

export interface ModelOption {
  id: string;
  name: string;
  description: string;
  badge?: string;
  isDefault?: boolean;
}

export type ThemeMode = 'dark' | 'light' | 'system';

export interface User {
  id: string;
  name: string;
  email: string;
  passwordHash: string;
  createdAt: string;
}
