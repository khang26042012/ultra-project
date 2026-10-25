'use client';

import React, { useState } from 'react';
import { useChat } from '@/context/ChatContext';
import {
  X,
  Palette,
  Volume2,
  Database,
  Info,
  Check,
  Settings,
  ArrowLeft,
  Sparkles,
} from 'lucide-react';
import { ThemeMode } from '@/types/chat';

export default function SettingsModal() {
  const {
    isSettingsOpen,
    setIsSettingsOpen,
    theme,
    setTheme,
    clearChatHistory,
  } = useChat();

  const [activeTab, setActiveTab] = useState<'general' | 'speech' | 'data' | 'about'>('general');
  const [historyTraining, setHistoryTraining] = useState(true);
  const [voice, setVoice] = useState('An Nhiên (Tiếng Việt)');
  const [language, setLanguage] = useState('Tiếng Việt (Mặc định)');

  if (!isSettingsOpen) return null;

  const voices = ['An Nhiên (Tiếng Việt)', 'Minh Đức (Tiếng Việt)', 'Quỳnh Anh (Tiếng Việt)'];
  const languages = ['Tiếng Việt (Mặc định)', 'English (US)'];

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-xs select-none p-4">
      <div className="w-full max-w-2xl bg-[#ffffff] dark:bg-[#1e1e1e] border border-[#e5e5e5] dark:border-[#333333] rounded-[24px] shadow-2xl overflow-hidden flex flex-col max-h-[85vh]">
        {/* Modal Header */}
        <div className="h-14 px-6 border-b border-[#e5e5e5] dark:border-[#333333] flex items-center justify-between">
          <div className="flex items-center gap-2">
            <button
              onClick={() => setIsSettingsOpen(false)}
              className="p-1.5 rounded-lg hover:bg-[#f0f0f0] dark:hover:bg-[#2f2f2f] text-[#5d5d5d] hover:text-[#0d0d0d] dark:text-[#8e8e8e] dark:hover:text-white transition-colors cursor-pointer"
            >
              <ArrowLeft className="w-4 h-4" strokeWidth={1.75} />
            </button>
            <span className="font-semibold text-base text-[#0d0d0d] dark:text-white">Cài đặt</span>
          </div>

          <button
            onClick={() => setIsSettingsOpen(false)}
            className="p-1.5 rounded-lg hover:bg-[#f0f0f0] dark:hover:bg-[#2f2f2f] text-[#5d5d5d] hover:text-[#0d0d0d] dark:text-[#8e8e8e] dark:hover:text-white transition-colors cursor-pointer"
          >
            <X className="w-5 h-5" strokeWidth={1.75} />
          </button>
        </div>

        {/* Modal Body: Left Tab Nav & Right Content */}
        <div className="flex-1 flex overflow-hidden">
          {/* Tabs Sidebar */}
          <div className="w-48 border-r border-[#e5e5e5] dark:border-[#333333] p-3 space-y-1 bg-[#f7f7f8] dark:bg-[#1a1a1a]">
            <button
              onClick={() => setActiveTab('general')}
              className={`w-full flex items-center gap-2.5 px-3 py-2 rounded-xl text-xs font-medium transition-colors cursor-pointer ${
                activeTab === 'general'
                  ? 'bg-[#0d0d0d] text-white dark:bg-[#2f2f2f] dark:text-white font-semibold'
                  : 'text-[#5d5d5d] dark:text-[#8e8e8e] hover:text-[#0d0d0d] dark:hover:text-white hover:bg-[#eaeaea] dark:hover:bg-[#252525]'
              }`}
            >
              <Settings className="w-4 h-4" strokeWidth={1.75} />
              <span>Chung</span>
            </button>

            <button
              onClick={() => setActiveTab('speech')}
              className={`w-full flex items-center gap-2.5 px-3 py-2 rounded-xl text-xs font-medium transition-colors cursor-pointer ${
                activeTab === 'speech'
                  ? 'bg-[#0d0d0d] text-white dark:bg-[#2f2f2f] dark:text-white font-semibold'
                  : 'text-[#5d5d5d] dark:text-[#8e8e8e] hover:text-[#0d0d0d] dark:hover:text-white hover:bg-[#eaeaea] dark:hover:bg-[#252525]'
              }`}
            >
              <Volume2 className="w-4 h-4" strokeWidth={1.75} />
              <span>Giọng nói</span>
            </button>

            <button
              onClick={() => setActiveTab('data')}
              className={`w-full flex items-center gap-2.5 px-3 py-2 rounded-xl text-xs font-medium transition-colors cursor-pointer ${
                activeTab === 'data'
                  ? 'bg-[#0d0d0d] text-white dark:bg-[#2f2f2f] dark:text-white font-semibold'
                  : 'text-[#5d5d5d] dark:text-[#8e8e8e] hover:text-[#0d0d0d] dark:hover:text-white hover:bg-[#eaeaea] dark:hover:bg-[#252525]'
              }`}
            >
              <Database className="w-4 h-4" strokeWidth={1.75} />
              <span>Dữ liệu chat</span>
            </button>

            <button
              onClick={() => setActiveTab('about')}
              className={`w-full flex items-center gap-2.5 px-3 py-2 rounded-xl text-xs font-medium transition-colors cursor-pointer ${
                activeTab === 'about'
                  ? 'bg-[#0d0d0d] text-white dark:bg-[#2f2f2f] dark:text-white font-semibold'
                  : 'text-[#5d5d5d] dark:text-[#8e8e8e] hover:text-[#0d0d0d] dark:hover:text-white hover:bg-[#eaeaea] dark:hover:bg-[#252525]'
              }`}
            >
              <Info className="w-4 h-4" strokeWidth={1.75} />
              <span>Giới thiệu</span>
            </button>
          </div>

          {/* Tab Content Panel */}
          <div className="flex-1 p-6 overflow-y-auto">
            {activeTab === 'general' && (
              <div className="space-y-6">
                <div>
                  <h3 className="text-sm font-semibold text-[#0d0d0d] dark:text-white mb-1">Giao diện (Theme)</h3>
                  <p className="text-xs text-[#5d5d5d] dark:text-[#8e8e8e] mb-3">Tùy chọn phong cách hiển thị trên thiết bị của bạn.</p>
                  <div className="grid grid-cols-3 gap-3">
                    {(['light', 'dark', 'system'] as ThemeMode[]).map((mode) => (
                      <button
                        key={mode}
                        onClick={() => setTheme(mode)}
                        className={`p-3 rounded-xl border text-center text-xs font-medium capitalize transition-all cursor-pointer ${
                          theme === mode
                            ? 'border-[#0d0d0d] bg-[#0d0d0d] text-white dark:border-white dark:bg-white dark:text-black shadow-xs'
                            : 'border-[#e5e5e5] hover:border-[#b4b4b4] text-[#5d5d5d] dark:border-[#383838] dark:hover:border-[#525252] dark:text-[#8e8e8e]'
                        }`}
                      >
                        <Palette className="w-4 h-4 mx-auto mb-1.5 opacity-80" strokeWidth={1.75} />
                        {mode === 'light' ? 'Chế độ sáng' : mode === 'dark' ? 'Chế độ tối' : 'Hệ thống'}
                      </button>
                    ))}
                  </div>
                </div>

                <div className="pt-4 border-t border-[#e5e5e5] dark:border-[#333333]">
                  <h3 className="text-sm font-semibold text-[#0d0d0d] dark:text-white mb-1">Ngôn ngữ hiển thị</h3>
                  <p className="text-xs text-[#5d5d5d] dark:text-[#8e8e8e] mb-3">Ngôn ngữ ưu tiên cho giao diện làm việc.</p>
                  <select
                    value={language}
                    onChange={(e) => setLanguage(e.target.value)}
                    className="w-full bg-[#f9f9f9] dark:bg-[#171717] border border-[#e5e5e5] dark:border-[#383838] rounded-xl px-3 py-2 text-xs text-[#0d0d0d] dark:text-white outline-none focus:border-[#0d0d0d] dark:focus:border-white cursor-pointer"
                  >
                    {languages.map((l) => (
                      <option key={l} value={l}>
                        {l}
                      </option>
                    ))}
                  </select>
                </div>
              </div>
            )}

            {activeTab === 'speech' && (
              <div className="space-y-6">
                <div>
                  <h3 className="text-sm font-semibold text-[#0d0d0d] dark:text-white mb-1">Giọng đọc</h3>
                  <p className="text-xs text-[#5d5d5d] dark:text-[#8e8e8e] mb-3">Tùy chọn giọng đọc cho câu trả lời âm thanh.</p>
                  <div className="grid grid-cols-2 gap-3">
                    {voices.map((v) => (
                      <button
                        key={v}
                        onClick={() => setVoice(v)}
                        className={`p-3 rounded-xl border flex items-center justify-between text-xs font-medium transition-all cursor-pointer ${
                          voice === v
                            ? 'border-[#0d0d0d] bg-[#0d0d0d] text-white dark:border-white dark:bg-white dark:text-black shadow-xs'
                            : 'border-[#e5e5e5] hover:border-[#b4b4b4] text-[#5d5d5d] dark:border-[#383838] dark:hover:border-[#525252] dark:text-[#8e8e8e]'
                        }`}
                      >
                        <span>{v}</span>
                        {voice === v && <Check className="w-4 h-4 text-white dark:text-black" strokeWidth={2} />}
                      </button>
                    ))}
                  </div>
                </div>
              </div>
            )}

            {activeTab === 'data' && (
              <div className="space-y-6">
                <div className="flex items-center justify-between">
                  <div>
                    <h3 className="text-sm font-semibold text-[#0d0d0d] dark:text-white">Lưu trữ lịch sử & Đồng bộ</h3>
                    <p className="text-xs text-[#5d5d5d] dark:text-[#8e8e8e] max-w-sm mt-0.5">
                      Tự động lưu các đoạn chẩn đoán bệnh cây vào tài khoản cá nhân.
                    </p>
                  </div>
                  <button
                    onClick={() => setHistoryTraining(!historyTraining)}
                    className={`w-11 h-6 rounded-full transition-colors relative cursor-pointer ${
                      historyTraining ? 'bg-[#0d0d0d] dark:bg-white' : 'bg-[#e5e5e5] dark:bg-[#424242]'
                    }`}
                  >
                    <span
                      className={`block w-4 h-4 rounded-full transition-transform ${
                        historyTraining
                          ? 'translate-x-6 bg-white dark:bg-black'
                          : 'translate-x-1 bg-white dark:bg-white'
                      }`}
                    />
                  </button>
                </div>

                <div className="pt-4 border-t border-[#e5e5e5] dark:border-[#333333] flex items-center justify-between">
                  <div>
                    <h3 className="text-sm font-semibold text-[#0d0d0d] dark:text-white">Xóa lịch sử hội thoại</h3>
                    <p className="text-xs text-[#5d5d5d] dark:text-[#8e8e8e]">Xóa toàn bộ các tin nhắn đã hỏi trước đây.</p>
                  </div>
                  <button
                    onClick={() => {
                      if (confirm('Bạn có chắc chắn muốn xóa toàn bộ lịch sử trò chuyện?')) {
                        clearChatHistory();
                        setIsSettingsOpen(false);
                      }
                    }}
                    className="px-3 py-1.5 rounded-xl border border-red-300 dark:border-red-900/50 hover:bg-red-50 dark:hover:bg-red-950/30 text-xs font-medium text-red-600 dark:text-red-400 transition-colors cursor-pointer"
                  >
                    Xóa lịch sử
                  </button>
                </div>

                <div className="pt-4 border-t border-[#e5e5e5] dark:border-[#333333] flex items-center justify-between">
                  <div>
                    <h3 className="text-sm font-semibold text-[#0d0d0d] dark:text-white">Xuất dữ liệu chẩn đoán</h3>
                    <p className="text-xs text-[#5d5d5d] dark:text-[#8e8e8e]">Tải xuống bản sao lưu toàn bộ các cuộc trò chuyện.</p>
                  </div>
                  <button
                    onClick={() => alert('Dữ liệu đã được lưu trữ an toàn trong hệ thống cục bộ.')}
                    className="px-3 py-1.5 rounded-xl border border-[#e5e5e5] hover:bg-[#f4f4f4] dark:border-[#383838] dark:hover:bg-[#2f2f2f] text-xs font-medium transition-colors cursor-pointer text-[#0d0d0d] dark:text-white"
                  >
                    Xuất JSON
                  </button>
                </div>
              </div>
            )}

            {activeTab === 'about' && (
              <div className="space-y-5">
                <div className="p-4 rounded-2xl bg-[#f7f7f8] dark:bg-[#171717] border border-[#e5e5e5] dark:border-[#333]">
                  <div className="flex items-center gap-2 mb-2">
                    <span className="w-6 h-6 rounded-lg bg-[#0d0d0d] text-white dark:bg-white dark:text-black flex items-center justify-center font-bold text-xs shadow-xs">
                      AV
                    </span>
                    <h3 className="text-sm font-bold text-[#0d0d0d] dark:text-white">AgriVision v1.0</h3>
                  </div>
                  <p className="text-xs text-[#5d5d5d] dark:text-[#b4b4b4] leading-relaxed">
                    Hệ sinh thái Trí tuệ Nhân tạo & Viễn thám Giám sát Bệnh học Thực vật Thông minh, đồng hành cùng bà con nông dân Vĩnh Long và Đồng bằng Sông Cửu Long.
                  </p>
                </div>

                <div className="space-y-3 text-xs">
                  <div className="flex justify-between py-2 border-b border-[#e5e5e5] dark:border-[#2a2a2a]">
                    <span className="text-[#5d5d5d] dark:text-[#8e8e8e]">Tác giả phát triển:</span>
                    <span className="font-semibold text-[#0d0d0d] dark:text-white">Phan Trọng Khang</span>
                  </div>
                  <div className="flex justify-between py-2 border-b border-[#e5e5e5] dark:border-[#2a2a2a]">
                    <span className="text-[#5d5d5d] dark:text-[#8e8e8e]">Đơn vị học tập:</span>
                    <span className="font-medium text-[#0d0d0d] dark:text-white">Lớp 9¹, Trường THCS Vĩnh An (Vĩnh Long)</span>
                  </div>
                  <div className="flex justify-between py-2 border-b border-[#e5e5e5] dark:border-[#2a2a2a]">
                    <span className="text-[#5d5d5d] dark:text-[#8e8e8e]">Mô hình AI cốt lõi:</span>
                    <span className="font-mono text-[#0d0d0d] dark:text-white flex items-center gap-1">
                      <Sparkles className="w-3.5 h-3.5" />
                      ag/gemini-3.8-flash-high
                    </span>
                  </div>
                  <div className="flex justify-between py-2 border-b border-[#e5e5e5] dark:border-[#2a2a2a]">
                    <span className="text-[#5d5d5d] dark:text-[#8e8e8e]">Tiêu chuẩn can thiệp:</span>
                    <span className="font-medium text-[#0d0d0d] dark:text-white">An toàn sinh học VietGAP</span>
                  </div>
                  <div className="flex justify-between py-2 border-b border-[#e5e5e5] dark:border-[#2a2a2a]">
                    <span className="text-[#5d5d5d] dark:text-[#8e8e8e]">Độ tin cậy lâm sàng:</span>
                    <span className="font-medium text-[#0d0d0d] dark:text-white">Nguyên tắc 3 Cấp độ chắc chắn</span>
                  </div>
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
