'use client';

import React, { useRef, useEffect } from 'react';
import { useChat } from '@/context/ChatContext';
import {
  User,
  Settings,
  HelpCircle,
  LogOut,
  ChevronRight,
} from 'lucide-react';

interface ProfileMenuProps {
  isOpen: boolean;
  onClose: () => void;
}

export default function ProfileMenu({ isOpen, onClose }: ProfileMenuProps) {
  const { userProfile, setIsSettingsOpen } = useChat();
  const menuRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (menuRef.current && !menuRef.current.contains(event.target as Node)) {
        onClose();
      }
    }
    if (isOpen) {
      document.addEventListener('mousedown', handleClickOutside);
    }
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  return (
    <div
      ref={menuRef}
      className="absolute bottom-16 left-3 w-64 rounded-2xl bg-[#ffffff] dark:bg-[#1e1e1e] border border-[#e5e5e5] dark:border-[#333333] shadow-xl p-1.5 z-50 text-[#0d0d0d] dark:text-[#ececec] text-sm animate-in fade-in zoom-in-95 duration-100"
    >
      {/* Account Info Bar */}
      <div className="flex items-center justify-between p-2.5 rounded-xl hover:bg-[#f4f4f4] dark:hover:bg-[#282828] transition-colors cursor-pointer border-b border-[#e5e5e5] dark:border-[#2b2b2b] mb-1">
        <div className="flex items-center gap-2.5">
          <div className="w-8 h-8 rounded-full bg-[#0d0d0d] text-white dark:bg-[#171717] dark:border dark:border-[#3e3e3e] dark:text-[#ececec] flex items-center justify-center font-bold text-xs shadow-xs">
            {userProfile.initials}
          </div>
          <div>
            <div className="font-semibold text-xs text-[#0d0d0d] dark:text-white leading-tight">
              {userProfile.name}
            </div>
          </div>
        </div>
        <ChevronRight className="w-4 h-4 text-[#8e8e8e]" strokeWidth={1.75} />
      </div>

      {/* Menu Actions */}
      <div className="space-y-0.5">
        <button
          onClick={onClose}
          className="w-full flex items-center gap-3 px-3 py-2 rounded-xl text-left hover:bg-[#f4f4f4] dark:hover:bg-[#282828] text-xs font-medium text-[#5d5d5d] hover:text-[#0d0d0d] dark:text-[#b4b4b4] dark:hover:text-white transition-colors cursor-pointer"
        >
          <User className="w-4 h-4" strokeWidth={1.75} />
          <span>Profile</span>
        </button>

        <button
          onClick={() => {
            onClose();
            setIsSettingsOpen(true);
          }}
          className="w-full flex items-center gap-3 px-3 py-2 rounded-xl text-left hover:bg-[#f4f4f4] dark:hover:bg-[#282828] text-xs font-medium text-[#5d5d5d] hover:text-[#0d0d0d] dark:text-[#b4b4b4] dark:hover:text-white transition-colors cursor-pointer"
        >
          <Settings className="w-4 h-4" strokeWidth={1.75} />
          <span>Settings</span>
        </button>

        <div className="h-px bg-[#e5e5e5] dark:bg-[#2b2b2b] my-1" />

        <button
          onClick={onClose}
          className="w-full flex items-center justify-between px-3 py-2 rounded-xl text-left hover:bg-[#f4f4f4] dark:hover:bg-[#282828] text-xs font-medium text-[#5d5d5d] hover:text-[#0d0d0d] dark:text-[#b4b4b4] dark:hover:text-white transition-colors cursor-pointer"
        >
          <div className="flex items-center gap-3">
            <HelpCircle className="w-4 h-4" strokeWidth={1.75} />
            <span>Help</span>
          </div>
          <ChevronRight className="w-3.5 h-3.5 text-[#8e8e8e]" strokeWidth={1.75} />
        </button>

        <button
          onClick={onClose}
          className="w-full flex items-center gap-3 px-3 py-2 rounded-xl text-left hover:bg-red-50 dark:hover:bg-red-950/30 text-xs font-medium text-red-600 dark:text-red-400 transition-colors cursor-pointer"
        >
          <LogOut className="w-4 h-4" strokeWidth={1.75} />
          <span>Log out</span>
        </button>
      </div>
    </div>
  );
}
