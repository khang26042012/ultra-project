'use client';

import React from 'react';
import { ChatProvider, useChat } from '@/context/ChatContext';
import AppSidebar from '@/components/sidebar/AppSidebar';
import EmptyState from '@/components/chat/EmptyState';
import MessageList from '@/components/chat/MessageList';
import FloatingInputIsland from '@/components/input/FloatingInputIsland';
import HelpModal from '@/components/modals/HelpModal';
import UpgradeModal from '@/components/modals/UpgradeModal';
import AuthModal from '@/components/modals/AuthModal';
import { SquarePen } from 'lucide-react';

function ChatApp() {
  const { activeConversation, toggleSidebar, createNewChat } = useChat();

  const hasMessages = activeConversation && activeConversation.messages.length > 0;

  return (
    <div className="flex h-[100dvh] w-screen overflow-hidden bg-[#ffffff] dark:bg-[#171717] text-[#0d0d0d] dark:text-[#ececec] no-scrollbar">
      {/* Left Collapsible Minimal Sidebar */}
      <AppSidebar />

      {/* Main Chat Viewport */}
      <div className="flex-1 flex flex-col h-full min-w-0 relative bg-[#ffffff] dark:bg-[#171717]">
        {/* Floating Controls Bar: 100% chuẩn giao diện ChatGPT App */}
        <div className="fixed top-3.5 left-3.5 right-3.5 z-30 flex items-center justify-between pointer-events-none">
          {/* Nút mở Sidebar bên trái: Khối tròn mềm mại */}
          <button
            type="button"
            onClick={toggleSidebar}
            title="Mở menu"
            className="pointer-events-auto w-10 h-10 rounded-full bg-white/90 dark:bg-[#212121]/90 backdrop-blur-md shadow-[0_2px_8px_rgba(0,0,0,0.08)] dark:shadow-none border border-black/5 dark:border-white/10 flex items-center justify-center text-[#0d0d0d] dark:text-white hover:scale-105 active:scale-95 transition-all cursor-pointer"
          >
            {/* Icon 2 vạch ngang bo tròn chuẩn ChatGPT */}
            <div className="flex flex-col gap-1.5 items-center justify-center">
              <span className="w-4 h-0.5 bg-current rounded-full" />
              <span className="w-4 h-0.5 bg-current rounded-full" />
            </div>
          </button>

          {/* Nút Tạo Chat Mới bên phải: Khối tròn mềm mại */}
          <button
            type="button"
            onClick={createNewChat}
            title="Đoạn chat mới"
            className="pointer-events-auto w-10 h-10 rounded-full bg-white/90 dark:bg-[#212121]/90 backdrop-blur-md shadow-[0_2px_8px_rgba(0,0,0,0.08)] dark:shadow-none border border-black/5 dark:border-white/10 flex items-center justify-center text-[#0d0d0d] dark:text-white hover:scale-105 active:scale-95 transition-all cursor-pointer"
          >
            <SquarePen className="w-4 h-4" strokeWidth={1.5} />
          </button>
        </div>

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
