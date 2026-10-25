'use client';

import React from 'react';
import { ChatProvider, useChat } from '@/context/ChatContext';
import AppSidebar from '@/components/sidebar/AppSidebar';
import EmptyState from '@/components/chat/EmptyState';
import MessageList from '@/components/chat/MessageList';
import FloatingInputIsland from '@/components/input/FloatingInputIsland';
import SettingsModal from '@/components/modals/SettingsModal';
import UpgradeModal from '@/components/modals/UpgradeModal';
import { PanelLeft } from 'lucide-react';

function ChatApp() {
  const { activeConversation, isSidebarOpen, toggleSidebar } = useChat();

  const hasMessages = activeConversation && activeConversation.messages.length > 0;

  return (
    <div className="flex h-[100dvh] w-screen overflow-hidden bg-[#171717] text-[#ececec] no-scrollbar">
      {/* Left Collapsible Minimal Sidebar */}
      <AppSidebar />

      {/* Main Chat Viewport without any Top Header Bar */}
      <div className="flex-1 flex flex-col h-full min-w-0 relative bg-[#171717]">
        {/* Floating Sidebar Toggle Button when sidebar is collapsed */}
        {!isSidebarOpen && (
          <div className="absolute top-3.5 left-3.5 z-30">
            <button
              onClick={toggleSidebar}
              title="Open sidebar"
              className="p-2 rounded-xl bg-[#242424]/90 hover:bg-[#303030] text-[#b4b4b4] hover:text-white transition-all border border-[#2f2f2f] shadow-lg backdrop-blur-md cursor-pointer"
            >
              <PanelLeft className="w-4 h-4" />
            </button>
          </div>
        )}

        <main className="flex-1 overflow-y-auto overscroll-contain flex flex-col relative no-scrollbar bg-[#171717]">
          {hasMessages ? (
            <>
              <div className="flex-1 overflow-y-auto overscroll-contain no-scrollbar pt-6 pb-2">
                <MessageList messages={activeConversation.messages} />
              </div>
              <div className="shrink-0 bg-gradient-to-t from-[#171717] via-[#171717]/95 to-transparent pt-4">
                <FloatingInputIsland />
              </div>
            </>
          ) : (
            <EmptyState />
          )}
        </main>

        {/* Global Modals */}
        <SettingsModal />
        <UpgradeModal />
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
