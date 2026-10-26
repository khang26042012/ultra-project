'use client';

import React, { useState, useRef, useEffect, useCallback } from 'react';
import Link from 'next/link';
import { useChat } from '@/context/ChatContext';
import ProfileMenu from './ProfileMenu';
import {
  SquarePen,
  Search,
  PanelLeftClose,
  Trash2,
  MessageSquare,
  X,
  LogIn,
  Settings,
  HelpCircle,
  BookOpen,
  MoreHorizontal,
  Pin,
  Pencil,
  Check,
} from 'lucide-react';
import gsap from 'gsap';
import { TimeGroup, Conversation } from '@/types/chat';

export default function AppSidebar() {
  const {
    conversations,
    activeConversationId,
    selectConversation,
    deleteConversation,
    renameConversation,
    togglePinConversation,
    createNewChat,
    isSidebarOpen,
    setIsSidebarOpen,
    toggleSidebar,
    setIsAuthModalOpen,
    setIsSettingsOpen,
    setIsHelpOpen,
    currentUser,
    userProfile,
  } = useChat();

  const [searchQuery, setSearchQuery] = useState('');
  const [isSearchVisible, setIsSearchVisible] = useState(false);
  const [isProfileMenuOpen, setIsProfileMenuOpen] = useState(false);

  // Context Menu Popup State
  const [menuConvId, setMenuConvId] = useState<string | null>(null);
  const [menuPosition, setMenuPosition] = useState<{ top: number; left: number } | null>(null);
  const menuRef = useRef<HTMLDivElement>(null);
  const longPressTimerRef = useRef<NodeJS.Timeout | null>(null);

  // Inline Rename State
  const [editingConvId, setEditingConvId] = useState<string | null>(null);
  const [editingTitle, setEditingTitle] = useState('');
  const renameInputRef = useRef<HTMLInputElement>(null);

  const sidebarRef = useRef<HTMLElement>(null);
  const prevOpenRef = useRef(isSidebarOpen);

  // GSAP 60 FPS Smooth Slide Animation for Sidebar toggling
  useEffect(() => {
    if (!sidebarRef.current) return;

    if (isSidebarOpen) {
      gsap.to(sidebarRef.current, {
        x: 0,
        opacity: 1,
        width: 260,
        duration: 0.3,
        ease: 'power3.out',
        display: 'flex',
      });
    } else {
      gsap.to(sidebarRef.current, {
        x: -20,
        opacity: 0,
        width: 0,
        duration: 0.25,
        ease: 'power3.in',
        onComplete: () => {
          if (sidebarRef.current && !isSidebarOpen) {
            sidebarRef.current.style.display = 'none';
          }
        },
      });
    }

    prevOpenRef.current = isSidebarOpen;
  }, [isSidebarOpen]);

  // Close context menu when clicking outside
  useEffect(() => {
    const handleClickOutside = (e: MouseEvent | TouchEvent) => {
      if (menuRef.current && !menuRef.current.contains(e.target as Node)) {
        setMenuConvId(null);
        setMenuPosition(null);
      }
    };

    if (menuConvId) {
      document.addEventListener('mousedown', handleClickOutside);
      document.addEventListener('touchstart', handleClickOutside);
    }
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
      document.removeEventListener('touchstart', handleClickOutside);
    };
  }, [menuConvId]);

  // Focus rename input when editing starts
  useEffect(() => {
    if (editingConvId && renameInputRef.current) {
      renameInputRef.current.focus();
      renameInputRef.current.select();
    }
  }, [editingConvId]);

  const handleOpenMenu = (convId: string, event: React.MouseEvent | React.TouchEvent) => {
    event.stopPropagation();
    const rect = (event.currentTarget as HTMLElement).getBoundingClientRect();
    setMenuConvId(convId);
    setMenuPosition({
      top: Math.min(rect.bottom + 4, window.innerHeight - 150),
      left: Math.min(rect.left, window.innerWidth - 170),
    });
  };

  const handleTouchStart = (convId: string, e: React.TouchEvent) => {
    longPressTimerRef.current = setTimeout(() => {
      handleOpenMenu(convId, e);
    }, 500);
  };

  const handleTouchEnd = () => {
    if (longPressTimerRef.current) {
      clearTimeout(longPressTimerRef.current);
      longPressTimerRef.current = null;
    }
  };

  const handleSaveRename = (convId: string) => {
    const trimmed = editingTitle.trim();
    if (trimmed) {
      renameConversation(convId, trimmed);
    }
    setEditingConvId(null);
  };

  // Filter conversations based on search
  const filteredConversations = conversations.filter((c) =>
    c.title.toLowerCase().includes(searchQuery.toLowerCase())
  );

  const pinnedConversations = filteredConversations.filter((c) => c.isPinned);
  const unpinnedConversations = filteredConversations.filter((c) => !c.isPinned);

  const groups: TimeGroup[] = ['Today', 'Yesterday', 'Previous 7 Days'];

  const renderConversationItem = (conv: Conversation) => {
    const isActive = conv.id === activeConversationId;
    const isEditing = editingConvId === conv.id;

    return (
      <div
        key={conv.id}
        onTouchStart={(e) => handleTouchStart(conv.id, e)}
        onTouchEnd={handleTouchEnd}
        onTouchMove={handleTouchEnd}
        onClick={() => {
          if (!isEditing) {
            selectConversation(conv.id);
            if (window.innerWidth < 768) setIsSidebarOpen(false);
          }
        }}
        className={`group relative flex items-center justify-between px-3 py-2 rounded-xl text-xs transition-all cursor-pointer ${
          isActive
            ? 'bg-[#e9e9ea] dark:bg-[#212121] text-[#0d0d0d] dark:text-white font-medium'
            : 'text-[#5d5d5d] dark:text-[#b4b4b4] hover:bg-[#ececee] dark:hover:bg-[#212121] hover:text-[#0d0d0d] dark:hover:text-white'
        }`}
      >
        <div className="flex items-center gap-2 truncate pr-2 flex-1 min-w-0">
          {conv.isPinned ? (
            <Pin className="w-3.5 h-3.5 shrink-0 text-emerald-600 dark:text-emerald-400 rotate-45" strokeWidth={1.75} />
          ) : (
            <MessageSquare className="w-3.5 h-3.5 shrink-0 opacity-70" strokeWidth={1.75} />
          )}

          {isEditing ? (
            <div className="flex items-center gap-1 w-full" onClick={(e) => e.stopPropagation()}>
              <input
                ref={renameInputRef}
                type="text"
                value={editingTitle}
                onChange={(e) => setEditingTitle(e.target.value)}
                onKeyDown={(e) => {
                  if (e.key === 'Enter') handleSaveRename(conv.id);
                  if (e.key === 'Escape') setEditingConvId(null);
                }}
                className="w-full bg-[#ffffff] dark:bg-[#2b2b2b] text-xs text-[#0d0d0d] dark:text-white px-2 py-0.5 rounded border border-[#0d0d0d] dark:border-white outline-none"
              />
              <button
                type="button"
                onClick={() => handleSaveRename(conv.id)}
                className="p-1 hover:text-emerald-600 cursor-pointer"
                title="Lưu"
              >
                <Check className="w-3.5 h-3.5" />
              </button>
            </div>
          ) : (
            <span className="truncate">{conv.title}</span>
          )}
        </div>

        {/* 3-Dots Action Button (replaces crude trash button) */}
        {!isEditing && (
          <button
            type="button"
            onClick={(e) => handleOpenMenu(conv.id, e)}
            title="Tùy chọn đoạn chat"
            className="opacity-70 md:opacity-0 group-hover:opacity-100 p-1 rounded-lg hover:bg-[#eaeaea] dark:hover:bg-[#2e2e2e] text-[#8e8e8e] hover:text-[#0d0d0d] dark:hover:text-white transition-all cursor-pointer shrink-0 ml-1"
          >
            <MoreHorizontal className="w-4 h-4" strokeWidth={1.75} />
          </button>
        )}
      </div>
    );
  };

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
        className="fixed md:static inset-y-0 left-0 z-50 md:z-auto w-64 md:w-auto h-full bg-[#f7f7f8] dark:bg-[#171717] border-r border-[#e5e5e5] dark:border-[#262626] shadow-2xl md:shadow-none flex flex-col select-none no-scrollbar overflow-hidden"
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
                title="Tìm kiếm đoạn chat"
                className="p-1.5 rounded-lg hover:bg-[#eaeaea] dark:hover:bg-[#252525] text-[#5d5d5d] hover:text-[#0d0d0d] dark:text-[#b4b4b4] dark:hover:text-white transition-all hover:scale-[1.02] active:scale-[0.98] cursor-pointer"
              >
                <Search className="w-4 h-4" strokeWidth={1.75} />
              </button>
              <button
                onClick={toggleSidebar}
                title="Đóng sidebar"
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
                  placeholder="Tìm kiếm lịch sử..."
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  className="w-full bg-[#ffffff] dark:bg-[#212121] text-xs text-[#0d0d0d] dark:text-white placeholder-[#8e8e8e] px-3 py-1.5 rounded-lg border border-[#e5e5e5] dark:border-[#383838] focus:border-[#0d0d0d] dark:focus:border-white outline-none transition-colors"
                />
                {searchQuery && (
                  <button
                    onClick={() => setSearchQuery('')}
                    className="absolute right-2 top-2 text-[#8e8e8e] hover:text-[#0d0d0d] dark:hover:text-white cursor-pointer"
                  >
                    <X className="w-3.5 h-3.5" />
                  </button>
                )}
              </div>
            </div>
          )}

          {/* Action Buttons: New Chat & Crop Encyclopedia */}
          <div className="px-3 py-1.5 space-y-1.5">
            <button
              onClick={() => {
                createNewChat();
                if (window.innerWidth < 768) setIsSidebarOpen(false);
              }}
              className="w-full flex items-center gap-2.5 px-3 py-2 rounded-xl bg-[#ffffff] hover:bg-[#f0f0f0] dark:bg-[#212121] dark:hover:bg-[#2a2a2a] text-[#0d0d0d] dark:text-[#ececec] text-xs font-semibold transition-all hover:scale-[1.02] active:scale-[0.98] cursor-pointer border border-[#e5e5e5] dark:border-[#2f2f2f] shadow-xs"
            >
              <SquarePen className="w-4 h-4 text-[#0d0d0d] dark:text-white" strokeWidth={1.75} />
              <span>Đoạn chat mới</span>
            </button>

            <Link
              href="/crops"
              onClick={() => {
                if (window.innerWidth < 768) setIsSidebarOpen(false);
              }}
              className="w-full flex items-center gap-2.5 px-3 py-2 rounded-xl bg-[#ffffff] hover:bg-[#f0f0f0] dark:bg-[#212121] dark:hover:bg-[#2a2a2a] text-[#0d0d0d] dark:text-[#ececec] text-xs font-semibold transition-all hover:scale-[1.02] active:scale-[0.98] cursor-pointer border border-[#e5e5e5] dark:border-[#2f2f2f] shadow-xs"
            >
              <BookOpen className="w-4 h-4 text-emerald-600 dark:text-emerald-400 shrink-0" strokeWidth={1.75} />
              <span className="flex-1 text-left truncate">Toàn thư cây trồng</span>
              <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-emerald-50 text-emerald-700 dark:bg-emerald-950/60 dark:text-emerald-300">
                1.500+
              </span>
            </Link>
          </div>

          {/* Divider */}
          <div className="h-px bg-[#e5e5e5] dark:bg-[#262626] mx-3 my-1" />

          {/* Clean History List Area */}
          <div className="flex-1 overflow-y-auto overscroll-contain px-2 space-y-3 no-scrollbar">
            {filteredConversations.length === 0 ? (
              <div className="px-3 py-3 text-xs text-[#8e8e8e]">Chưa có đoạn chat nào</div>
            ) : (
              <>
                {/* 1. PINNED SECTION (ĐÃ GHIM) */}
                {pinnedConversations.length > 0 && (
                  <div className="space-y-0.5">
                    <div className="flex items-center gap-1 px-3 py-1 text-[11px] font-semibold text-[#8e8e8e] uppercase tracking-wider">
                      <Pin className="w-3 h-3 text-emerald-600 dark:text-emerald-400" />
                      <span>Đã ghim</span>
                    </div>
                    {pinnedConversations.map((conv) => renderConversationItem(conv))}
                  </div>
                )}

                {/* 2. RECENT / TIME GROUPS SECTION */}
                {unpinnedConversations.length > 0 && (
                  <div className="space-y-3">
                    {groups.map((group) => {
                      const groupConvs = unpinnedConversations.filter((c) => c.group === group);
                      if (groupConvs.length === 0) return null;

                      return (
                        <div key={group} className="space-y-0.5">
                          <div className="px-3 py-1 text-[10px] font-medium text-[#8e8e8e] uppercase tracking-wider">
                            {group === 'Today' ? 'Hôm nay' : group === 'Yesterday' ? 'Hôm qua' : '7 ngày trước'}
                          </div>
                          {groupConvs.map((conv) => renderConversationItem(conv))}
                        </div>
                      );
                    })}
                  </div>
                )}
              </>
            )}
          </div>

          {/* Quick Actions: Help & Settings */}
          <div className="px-2.5 py-1.5 space-y-0.5 border-t border-[#e5e5e5] dark:border-[#262626]">
            <button
              type="button"
              data-testid="sidebar-help-button"
              onClick={() => {
                setIsHelpOpen(true);
                if (window.innerWidth < 768) setIsSidebarOpen(false);
              }}
              className="w-full flex items-center gap-2.5 px-2.5 py-2 rounded-xl hover:bg-[#eaeaea] dark:hover:bg-[#212121] text-xs font-medium text-[#5d5d5d] dark:text-[#b4b4b4] hover:text-[#0d0d0d] dark:hover:text-white transition-colors cursor-pointer"
            >
              <HelpCircle className="w-4 h-4 shrink-0" strokeWidth={1.75} />
              <span>Trợ giúp & Hướng dẫn</span>
            </button>
            <button
              type="button"
              data-testid="sidebar-settings-button"
              onClick={() => {
                setIsSettingsOpen(true);
                if (window.innerWidth < 768) setIsSidebarOpen(false);
              }}
              className="w-full flex items-center gap-2.5 px-2.5 py-2 rounded-xl hover:bg-[#eaeaea] dark:hover:bg-[#212121] text-xs font-medium text-[#5d5d5d] dark:text-[#b4b4b4] hover:text-[#0d0d0d] dark:hover:text-white transition-colors cursor-pointer"
            >
              <Settings className="w-4 h-4 shrink-0" strokeWidth={1.75} />
              <span>Cài đặt hệ thống</span>
            </button>
          </div>

          {/* Footer Profile / Auth Bar */}
          <div className="p-3 border-t border-[#e5e5e5] dark:border-[#262626] relative">
            {currentUser ? (
              <>
                <div
                  data-testid="profile-menu-button"
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

      {/* ChatGPT Standard Floating Context Menu Popup */}
      {menuConvId && menuPosition && (
        <div
          ref={menuRef}
          style={{ top: `${menuPosition.top}px`, left: `${menuPosition.left}px` }}
          className="fixed z-50 min-w-[150px] p-1.5 rounded-2xl bg-[#ffffff] dark:bg-[#212121] border border-[#e5e5e5] dark:border-[#333] shadow-xl backdrop-blur-md space-y-0.5 animate-in fade-in zoom-in-95 duration-100"
        >
          {(() => {
            const targetConv = conversations.find((c) => c.id === menuConvId);
            const isPinned = targetConv?.isPinned;

            return (
              <>
                {/* 1. Ghim / Bỏ ghim */}
                <button
                  type="button"
                  onClick={() => {
                    togglePinConversation(menuConvId);
                    setMenuConvId(null);
                  }}
                  className="w-full flex items-center gap-2.5 px-3 py-2 rounded-xl text-xs font-medium text-[#0d0d0d] dark:text-[#ececec] hover:bg-[#f4f4f4] dark:hover:bg-[#2b2b2b] transition-colors cursor-pointer text-left"
                >
                  <Pin className={`w-3.5 h-3.5 ${isPinned ? 'text-emerald-600 dark:text-emerald-400 rotate-45' : 'text-[#5d5d5d] dark:text-[#a3a3a3]'}`} />
                  <span>{isPinned ? 'Bỏ ghim' : 'Ghim'}</span>
                </button>

                {/* 2. Đổi tên */}
                <button
                  type="button"
                  onClick={() => {
                    if (targetConv) {
                      setEditingConvId(targetConv.id);
                      setEditingTitle(targetConv.title);
                    }
                    setMenuConvId(null);
                  }}
                  className="w-full flex items-center gap-2.5 px-3 py-2 rounded-xl text-xs font-medium text-[#0d0d0d] dark:text-[#ececec] hover:bg-[#f4f4f4] dark:hover:bg-[#2b2b2b] transition-colors cursor-pointer text-left"
                >
                  <Pencil className="w-3.5 h-3.5 text-[#5d5d5d] dark:text-[#a3a3a3]" />
                  <span>Đổi tên</span>
                </button>

                {/* 3. Xoá (text-red-500) */}
                <button
                  type="button"
                  onClick={() => {
                    deleteConversation(menuConvId);
                    setMenuConvId(null);
                  }}
                  className="w-full flex items-center gap-2.5 px-3 py-2 rounded-xl text-xs font-medium text-red-500 hover:bg-red-50 dark:hover:bg-red-950/40 transition-colors cursor-pointer text-left"
                >
                  <Trash2 className="w-3.5 h-3.5 text-red-500" />
                  <span>Xoá</span>
                </button>
              </>
            );
          })()}
        </div>
      )}
    </>
  );
}
