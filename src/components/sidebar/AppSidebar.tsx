'use client';

import React, { useState, useRef, useEffect } from 'react';
import { useChat } from '@/context/ChatContext';
import ProfileMenu from './ProfileMenu';
import {
  PanelLeftClose,
  Search,
  SquarePen,
  Trash2,
  X,
  MessageSquare,
  LogIn,
} from 'lucide-react';
import { TimeGroup } from '@/types/chat';
import gsap from 'gsap';

export default function AppSidebar() {
  const {
    conversations,
    activeConversationId,
    selectConversation,
    deleteConversation,
    createNewChat,
    isSidebarOpen,
    setIsSidebarOpen,
    toggleSidebar,
    userProfile,
    currentUser,
    setIsAuthModalOpen,
  } = useChat();

  const [isProfileMenuOpen, setIsProfileMenuOpen] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');
  const [isSearchVisible, setIsSearchVisible] = useState(false);
  const sidebarRef = useRef<HTMLElement>(null);
  const hasMounted = useRef(false);

  // GSAP 60 FPS buttery smooth animation for Sidebar
  useEffect(() => {
    if (!sidebarRef.current) return;

    const isMobile = typeof window !== 'undefined' && window.innerWidth < 768;

    if (!hasMounted.current) {
      hasMounted.current = true;
      if (isMobile) {
        gsap.set(sidebarRef.current, { x: isSidebarOpen ? 0 : -270 });
      } else {
        gsap.set(sidebarRef.current, {
          width: isSidebarOpen ? '260px' : '0px',
          opacity: isSidebarOpen ? 1 : 0,
        });
      }
      return;
    }

    if (isMobile) {
      gsap.to(sidebarRef.current, {
        x: isSidebarOpen ? 0 : -270,
        duration: 0.28,
        ease: 'power2.out',
      });
    } else {
      gsap.to(sidebarRef.current, {
        width: isSidebarOpen ? '260px' : '0px',
        opacity: isSidebarOpen ? 1 : 0,
        duration: 0.28,
        ease: 'power2.out',
      });
    }
  }, [isSidebarOpen]);

  const groups: TimeGroup[] = ['Today', 'Yesterday', 'Previous 7 Days'];

  const filteredConversations = conversations.filter((c) =>
    c.title.toLowerCase().includes(searchQuery.toLowerCase())
  );

  return (
    <>
      {/* Mobile Drawer Overlay */}
      {isSidebarOpen && (
        <div
          onClick={() => setIsSidebarOpen(false)}
          className="md:hidden fixed inset-0 bg-black/40 z-40 backdrop-blur-xs transition-opacity"
        />
      )}

      {/* Sidebar Container */}
      <aside
        ref={sidebarRef}
        className="fixed md:static inset-y-0 left-0 z-40 w-64 md:w-auto h-full bg-[#f7f7f8] dark:bg-[#171717] border-r border-[#e5e5e5] dark:border-[#262626] flex flex-col select-none no-scrollbar overflow-hidden"
      >
        <div className="w-64 min-w-[260px] flex flex-col h-full">
          {/* Top Header */}
          <div className="h-14 px-3 flex items-center justify-between">
            <span className="font-semibold text-[#0d0d0d] dark:text-white tracking-tight text-base pl-1 flex items-center gap-2">
              <span className="w-5 h-5 rounded-md bg-[#0d0d0d] text-white dark:bg-white dark:text-black flex items-center justify-center font-bold text-[10px] shadow-xs">
                AV
              </span>
              <span>AgriVision</span>
            </span>

            <div className="flex items-center gap-1">
              <button
                onClick={() => setIsSearchVisible(!isSearchVisible)}
                title="Search chats"
                className="p-1.5 rounded-lg hover:bg-[#eaeaea] dark:hover:bg-[#252525] text-[#5d5d5d] hover:text-[#0d0d0d] dark:text-[#b4b4b4] dark:hover:text-white transition-all hover:scale-[1.02] active:scale-[0.98] cursor-pointer"
              >
                <Search className="w-4 h-4" strokeWidth={1.75} />
              </button>
              <button
                onClick={toggleSidebar}
                title="Hide sidebar"
                className="p-1.5 rounded-lg hover:bg-[#eaeaea] dark:hover:bg-[#252525] text-[#5d5d5d] hover:text-[#0d0d0d] dark:text-[#b4b4b4] dark:hover:text-white transition-all hover:scale-[1.02] active:scale-[0.98] cursor-pointer"
              >
                <PanelLeftClose className="w-4 h-4" strokeWidth={1.75} />
              </button>
            </div>
          </div>

          {/* Quick Search Bar if visible */}
          {isSearchVisible && (
            <div className="px-3 pb-2">
              <div className="relative">
                <input
                  type="text"
                  placeholder="Search history..."
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  className="w-full bg-[#ffffff] dark:bg-[#212121] text-xs text-[#0d0d0d] dark:text-white placeholder-[#8e8e8e] px-3 py-1.5 rounded-lg border border-[#e5e5e5] dark:border-[#383838] focus:border-[#0d0d0d] dark:focus:border-white outline-none transition-colors"
                />
                {searchQuery && (
                  <button
                    onClick={() => setSearchQuery('')}
                    className="absolute right-2 top-2 text-[#8e8e8e] hover:text-[#0d0d0d] dark:hover:text-white cursor-pointer"
                  >
                    <X className="w-3.5 h-3.5" strokeWidth={1.75} />
                  </button>
                )}
              </div>
            </div>
          )}

          {/* Primary New Chat Button */}
          <div className="px-3 pb-2">
            <button
              onClick={() => {
                createNewChat();
                if (window.innerWidth < 768) setIsSidebarOpen(false);
              }}
              className="w-full flex items-center gap-2.5 px-3 py-2 rounded-xl bg-[#ffffff] hover:bg-[#f0f0f0] dark:bg-[#212121] dark:hover:bg-[#2a2a2a] text-[#0d0d0d] dark:text-[#ececec] text-xs font-semibold transition-all hover:scale-[1.02] active:scale-[0.98] cursor-pointer border border-[#e5e5e5] dark:border-[#2f2f2f] shadow-xs"
            >
              <SquarePen className="w-4 h-4 text-[#0d0d0d] dark:text-white" strokeWidth={1.75} />
              <span>New chat</span>
            </button>
          </div>

          {/* Divider */}
          <div className="h-px bg-[#e5e5e5] dark:bg-[#262626] mx-3 my-1" />

          {/* Clean History List Area without extra tabs */}
          <div className="flex-1 overflow-y-auto overscroll-contain px-2 space-y-4 no-scrollbar">
            {/* Recents Section */}
            <div>
              <div className="px-3 py-1 text-[11px] font-semibold text-[#8e8e8e] uppercase tracking-wider">
                Recents
              </div>

              {filteredConversations.length === 0 ? (
                <div className="px-3 py-2 text-xs text-[#8e8e8e]">No chats found</div>
              ) : (
                groups.map((group) => {
                  const groupConvs = filteredConversations.filter((c) => c.group === group);
                  if (groupConvs.length === 0) return null;

                  return (
                    <div key={group} className="mt-2 space-y-0.5">
                      <div className="px-3 py-1 text-[10px] font-medium text-[#8e8e8e]">
                        {group}
                      </div>
                      {groupConvs.map((conv) => {
                        const isActive = conv.id === activeConversationId;
                        return (
                          <div
                            key={conv.id}
                            onClick={() => {
                              selectConversation(conv.id);
                              if (window.innerWidth < 768) setIsSidebarOpen(false);
                            }}
                            className={`group relative flex items-center justify-between px-3 py-2 rounded-xl text-xs transition-all hover:scale-[1.01] active:scale-[0.99] cursor-pointer ${
                              isActive
                                ? 'bg-[#e9e9ea] dark:bg-[#212121] text-[#0d0d0d] dark:text-white font-medium'
                                : 'text-[#5d5d5d] dark:text-[#b4b4b4] hover:bg-[#ececee] dark:hover:bg-[#212121] hover:text-[#0d0d0d] dark:hover:text-white'
                            }`}
                          >
                            <div className="flex items-center gap-2 truncate pr-2">
                              <MessageSquare className="w-3.5 h-3.5 shrink-0 opacity-70" strokeWidth={1.75} />
                              <span className="truncate">{conv.title}</span>
                            </div>

                            {/* Delete button on hover */}
                            <button
                              type="button"
                              onClick={(e) => {
                                e.stopPropagation();
                                deleteConversation(conv.id);
                              }}
                              title="Delete chat"
                              className="opacity-0 group-hover:opacity-100 p-1 hover:text-red-500 text-[#8e8e8e] transition-opacity cursor-pointer shrink-0"
                            >
                              <Trash2 className="w-3.5 h-3.5" strokeWidth={1.75} />
                            </button>
                          </div>
                        );
                      })}
                    </div>
                  );
                })
              )}
            </div>
          </div>

          {/* Footer Profile / Auth Bar */}
          <div className="p-3 border-t border-[#e5e5e5] dark:border-[#262626] relative">
            {currentUser ? (
              <>
                <div
                  onClick={() => setIsProfileMenuOpen(!isProfileMenuOpen)}
                  className="flex items-center justify-between p-2 rounded-xl hover:bg-[#eaeaea] dark:hover:bg-[#212121] transition-all hover:scale-[1.01] active:scale-[0.99] cursor-pointer"
                >
                  <div className="flex items-center gap-2.5 truncate">
                    <div className="w-8 h-8 shrink-0 rounded-full bg-[#0d0d0d] text-white dark:bg-[#2a2a2a] dark:border dark:border-[#444] dark:text-[#ececec] flex items-center justify-center font-bold text-xs shadow-xs">
                      {userProfile.initials}
                    </div>
                    <div className="truncate text-left">
                      <div className="font-medium text-xs text-[#0d0d0d] dark:text-white truncate leading-tight">
                        {userProfile.name}
                      </div>
                      <div className="text-[10px] text-[#8e8e8e] truncate mt-0.5">
                        {userProfile.email}
                      </div>
                    </div>
                  </div>
                </div>

                {/* Profile Menu Dropup */}
                <ProfileMenu
                  isOpen={isProfileMenuOpen}
                  onClose={() => setIsProfileMenuOpen(false)}
                />
              </>
            ) : (
              <button
                type="button"
                onClick={() => setIsAuthModalOpen(true)}
                className="w-full flex items-center justify-center gap-2 px-3 py-2.5 rounded-xl bg-[#0d0d0d] hover:bg-[#262626] text-white dark:bg-white dark:hover:bg-gray-100 dark:text-black text-xs font-semibold shadow-xs transition-all hover:scale-[1.02] active:scale-[0.98] cursor-pointer"
              >
                <LogIn className="w-4 h-4" strokeWidth={1.75} />
                <span>Đăng nhập / Đăng ký</span>
              </button>
            )}
          </div>
        </div>
      </aside>
    </>
  );
}
