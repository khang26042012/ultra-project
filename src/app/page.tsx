'use client';

import React from 'react';
import { ChatProvider, useChat } from '@/context/ChatContext';
import AppSidebar from '@/components/sidebar/AppSidebar';
import EmptyState from '@/components/chat/EmptyState';
import MessageList from '@/components/chat/MessageList';
import FloatingInputIsland from '@/components/input/FloatingInputIsland';
import SettingsModal from '@/components/modals/SettingsModal';
import HelpModal from '@/components/modals/HelpModal';
import UpgradeModal from '@/components/modals/UpgradeModal';
import AuthModal from '@/components/modals/AuthModal';
import { PanelLeft, SquarePen } from 'lucide-react';

function ChatApp() {
  const { activeConversation, isSidebarOpen, toggleSidebar, createNewChat } = useChat();

  const hasMessages = activeConversation && activeConversation.messages.length > 0;

  return (
    <div className="flex h-[100dvh] w-screen overflow-hidden bg-[#ffffff] dark:bg-[#171717] text-[#0d0d0d] dark:text-[#ececec] no-scrollbar">
      {/* Left Collapsible Minimal Sidebar */}
      <AppSidebar />

      {/* Main Chat Viewport */}
      <div className="flex-1 flex flex-col h-full min-w-0 relative bg-[#ffffff] dark:bg-[#171717]">
        {/* Top Navigation Bar */}
        <header className="sticky top-0 z-30 h-12 flex items-center justify-between px-3.5 bg-transparent shrink-0 select-none">
          <div className="flex items-center gap-2">
            {/* Mobile Sidebar Toggle */}
            <button
              type="button"
              onClick={toggleSidebar}
              title="Mở sidebar"
              className="md:hidden p-1.5 rounded-lg hover:bg-black/5 dark:hover:bg-white/5 text-[#5d5d5d] hover:text-[#0d0d0d] dark:text-[#b4b4b4] dark:hover:text-white transition-colors cursor-pointer"
            >
              <PanelLeft className="w-5 h-5" strokeWidth={1.75} />
            </button>

            {/* Desktop Floating Sidebar Toggle Button when sidebar is collapsed */}
            {!isSidebarOpen && (
              <button
                type="button"
                onClick={toggleSidebar}
                title="Mở sidebar"
                className="hidden md:flex items-center justify-center p-2 rounded-xl bg-[#ffffff]/90 hover:bg-[#f2f2f2] dark:bg-[#242424]/90 dark:hover:bg-[#303030] text-[#5d5d5d] hover:text-[#0d0d0d] dark:text-[#b4b4b4] dark:hover:text-white transition-all hover:scale-[1.02] active:scale-[0.98] border border-[#e5e5e5] dark:border-[#2f2f2f] shadow-xs backdrop-blur-md cursor-pointer"
              >
                <PanelLeft className="w-4 h-4" strokeWidth={1.75} />
              </button>
            )}
          </div>

          <div className="flex items-center gap-2">
            <button
              type="button"
              onClick={createNewChat}
              title="Đoạn chat mới"
              className="p-1.5 rounded-lg hover:bg-black/5 dark:hover:bg-white/5 text-[#5d5d5d] hover:text-[#0d0d0d] dark:text-[#b4b4b4] dark:hover:text-white transition-colors cursor-pointer"
            >
              <SquarePen className="w-4 h-4" strokeWidth={1.75} />
            </button>
          </div>
        </header>

        <main className="flex-1 flex flex-col min-h-0 overflow-hidden relative bg-[#ffffff] dark:bg-[#171717]">
          {hasMessages ? (
            <>
              <MessageList messages={activeConversation.messages} />
              <div className="shrink-0 bg-gradient-to-t from-[#ffffff] via-[#ffffff]/95 to-transparent dark:from-[#171717] dark:via-[#171717]/95 pt-2 sm:pt-4">
                <FloatingInputIsland />
              </div>
            </>
          ) : (
            <div className="flex-1 min-h-0 overflow-y-auto flex flex-col">
              <EmptyState />
            </div>
          )}
        </main>

        {/* Global Modals */}
        <SettingsModal />
        <HelpModal />
        <UpgradeModal />
        <AuthModal />
      </div>
    </div>
  );
}

export default function Home() {
  return (
    <ChatProvider>
      <ChatApp />
    </ChatProvider>
  );
}
