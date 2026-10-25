'use client';

import React, { useEffect, useRef, useState, useCallback } from 'react';
import { Message } from '@/types/chat';
import ChatMessage from './ChatMessage';
import { ArrowDown } from 'lucide-react';
import { useChat } from '@/context/ChatContext';

interface MessageListProps {
  messages: Message[];
}

export default function MessageList({ messages }: MessageListProps) {
  const { isAutoScrollEnabled = true } = useChat();
  const containerRef = useRef<HTMLDivElement>(null);
  const bottomRef = useRef<HTMLDivElement>(null);
  const [showScrollBottom, setShowScrollBottom] = useState(false);
  const isNearBottomRef = useRef(true);

  // Monitor scroll position
  const handleScroll = useCallback(() => {
    const el = containerRef.current;
    if (!el) return;

    const distanceFromBottom = el.scrollHeight - el.scrollTop - el.clientHeight;
    // If within 120px from bottom, consider user near bottom
    isNearBottomRef.current = distanceFromBottom <= 120;
    // If scrolled up more than 200px, show floating scroll-to-bottom button
    setShowScrollBottom(distanceFromBottom > 200);
  }, []);

  // Smart auto-scroll: only scrolls if near bottom and auto-scroll enabled
  useEffect(() => {
    if (isAutoScrollEnabled && isNearBottomRef.current) {
      bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
    }
  }, [messages, messages[messages.length - 1]?.content, isAutoScrollEnabled]);

  const scrollToBottom = () => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
    isNearBottomRef.current = true;
    setShowScrollBottom(false);
  };

  return (
    <div
      ref={containerRef}
      onScroll={handleScroll}
      className="flex-1 overflow-y-auto overscroll-contain no-scrollbar pt-4 sm:pt-6 pb-2 relative"
    >
      <div className="w-full max-w-3xl mx-auto px-4 py-2">
        {messages.map((message) => (
          <ChatMessage key={message.id} message={message} />
        ))}
        <div ref={bottomRef} className="h-4" />
      </div>

      {/* Floating Scroll-to-Bottom Button */}
      {showScrollBottom && (
        <div className="sticky bottom-4 flex justify-center z-20 pointer-events-none">
          <button
            type="button"
            onClick={scrollToBottom}
            title="Cuộn xuống tin nhắn mới nhất"
            className="pointer-events-auto p-2.5 rounded-full bg-white dark:bg-[#262626] border border-[#e5e5e5] dark:border-[#383838] shadow-lg text-[#0d0d0d] dark:text-white hover:bg-[#f4f4f4] dark:hover:bg-[#333] hover:scale-105 active:scale-95 transition-all cursor-pointer flex items-center justify-center animate-in fade-in duration-200"
          >
            <ArrowDown className="w-4 h-4" strokeWidth={2} />
          </button>
        </div>
      )}
    </div>
  );
}
