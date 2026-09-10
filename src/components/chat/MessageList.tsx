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
  const contentRef = useRef<HTMLDivElement>(null);
  const [showScrollBottom, setShowScrollBottom] = useState(false);
  const isNearBottomRef = useRef(true);
  const isProgrammaticScrollRef = useRef(false);
  const prevMessagesLengthRef = useRef(messages.length);
  const prevLastMessageIdRef = useRef(messages[messages.length - 1]?.id);

  // Scroll to bottom helper
  const scrollToBottom = useCallback((behavior: ScrollBehavior = 'instant') => {
    const el = containerRef.current;
    if (!el) return;
    isProgrammaticScrollRef.current = true;
    if (behavior === 'smooth') {
      el.scrollTo({ top: el.scrollHeight, behavior: 'smooth' });
    } else {
      el.scrollTop = el.scrollHeight;
    }
  }, []);

  // Monitor user scroll position
  const handleScroll = useCallback(() => {
    const el = containerRef.current;
    if (!el) return;

    const distanceFromBottom = el.scrollHeight - el.scrollTop - el.clientHeight;

    if (distanceFromBottom <= 50) {
      // User is at bottom
      isNearBottomRef.current = true;
      setShowScrollBottom(false);
    } else if (distanceFromBottom > 80) {
      // Only set isNearBottomRef to false if this was NOT triggered by programmatic auto-scroll
      if (!isProgrammaticScrollRef.current) {
        isNearBottomRef.current = false;
        setShowScrollBottom(true);
      }
    }

    isProgrammaticScrollRef.current = false;
  }, []);

  // Detect explicit user upward wheel scroll
  const handleWheel = (e: React.WheelEvent) => {
    if (e.deltaY < 0) {
      // User scrolled UP
      isNearBottomRef.current = false;
      const el = containerRef.current;
      if (el) {
        const dist = el.scrollHeight - el.scrollTop - el.clientHeight;
        if (dist > 80) {
          setShowScrollBottom(true);
        }
      }
    }
  };

  // Detect touch swipe upward
  const touchStartYRef = useRef<number | null>(null);
  const handleTouchStart = (e: React.TouchEvent) => {
    touchStartYRef.current = e.touches[0].clientY;
  };
  const handleTouchMove = (e: React.TouchEvent) => {
    if (touchStartYRef.current !== null) {
      const deltaY = e.touches[0].clientY - touchStartYRef.current;
      if (deltaY > 6) {
        // Swiping down moves scroll UP
        isNearBottomRef.current = false;
        const el = containerRef.current;
        if (el) {
          const dist = el.scrollHeight - el.scrollTop - el.clientHeight;
          if (dist > 80) {
            setShowScrollBottom(true);
          }
        }
      }
    }
  };

  // Auto-scroll on content resize (streaming tokens, thinking accordion, images, etc.)
  useEffect(() => {
    const contentEl = contentRef.current;
    const containerEl = containerRef.current;
    if (!contentEl || !containerEl) return;

    const resizeObserver = new ResizeObserver(() => {
      if (isAutoScrollEnabled && isNearBottomRef.current) {
        isProgrammaticScrollRef.current = true;
        containerEl.scrollTop = containerEl.scrollHeight;
      }
    });

    resizeObserver.observe(contentEl);
    return () => resizeObserver.disconnect();
  }, [isAutoScrollEnabled]);

  // Handle new messages added (user message sent or new assistant turn)
  useEffect(() => {
    const currentLength = messages.length;
    const currentLastId = messages[messages.length - 1]?.id;

    if (
      currentLength !== prevMessagesLengthRef.current ||
      currentLastId !== prevLastMessageIdRef.current
    ) {
      prevMessagesLengthRef.current = currentLength;
      prevLastMessageIdRef.current = currentLastId;

      // Always scroll to bottom when a new message is added or conversation switched
      isNearBottomRef.current = true;
      setShowScrollBottom(false);
      scrollToBottom('instant');
    }
  }, [messages, scrollToBottom]);

  // Click scroll to bottom button
  const handleScrollToBottomClick = () => {
    isNearBottomRef.current = true;
    setShowScrollBottom(false);
    scrollToBottom('smooth');
  };

  return (
    <div
      ref={containerRef}
      onScroll={handleScroll}
      onWheel={handleWheel}
      onTouchStart={handleTouchStart}
      onTouchMove={handleTouchMove}
      className="flex-1 min-h-0 overflow-y-auto overscroll-contain no-scrollbar pt-4 sm:pt-6 pb-2 relative"
    >
      <div ref={contentRef} className="w-full max-w-3xl mx-auto px-4 py-2">
        {messages.map((message) => (
          <ChatMessage key={message.id} message={message} />
        ))}
        <div className="h-6" />
      </div>

      {/* Floating Scroll-to-Bottom Button */}
      {showScrollBottom && (
        <div className="sticky bottom-4 flex justify-center z-20 pointer-events-none">
          <button
            type="button"
            onClick={handleScrollToBottomClick}
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
