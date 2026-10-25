'use client';

import React, { useState, useRef, useEffect } from 'react';
import { Message } from '@/types/chat';
import CodeBlock from './CodeBlock';
import { Copy, Check, ThumbsUp, ThumbsDown, RotateCcw, ChevronDown, ChevronRight } from 'lucide-react';
import gsap from 'gsap';

interface ChatMessageProps {
  message: Message;
}

export default function ChatMessage({ message }: ChatMessageProps) {
  const [copied, setCopied] = useState(false);
  const [liked, setLiked] = useState<boolean | null>(null);
  const [showThought, setShowThought] = useState(false);
  const messageRef = useRef<HTMLDivElement>(null);

  // GSAP 60 FPS Message Reveal Animation (Fade & Slide In)
  useEffect(() => {
    if (messageRef.current) {
      gsap.fromTo(
        messageRef.current,
        { opacity: 0, y: 12 },
        { opacity: 1, y: 0, duration: 0.35, ease: 'power2.out' }
      );
    }
  }, []);

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(message.content);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch {
      setCopied(false);
    }
  };

  const renderFormattedContent = (content: string) => {
    const parts = content.split(/(```[\s\S]*?```)/g);

    return parts.map((part, index) => {
      if (part.startsWith('```') && part.endsWith('```')) {
        const lines = part.slice(3, -3).trim().split('\n');
        const language = lines[0].trim();
        const code = lines.slice(1).join('\n');
        return <CodeBlock key={index} language={language} code={code} />;
      }

      const lines = part.split('\n');
      return (
        <div key={index} className="space-y-2.5">
          {lines.map((line, lIdx) => {
            if (line.startsWith('### ')) {
              return <h3 key={lIdx} className="text-base font-semibold text-[#0d0d0d] dark:text-[#ececec] mt-3.5 mb-1.5">{line.replace('### ', '')}</h3>;
            }
            if (line.startsWith('## ')) {
              return <h2 key={lIdx} className="text-lg font-bold text-[#0d0d0d] dark:text-[#ececec] mt-4 mb-2">{line.replace('## ', '')}</h2>;
            }
            if (line.startsWith('# ')) {
              return <h1 key={lIdx} className="text-xl font-bold text-[#0d0d0d] dark:text-[#ececec] mt-5 mb-2.5">{line.replace('# ', '')}</h1>;
            }
            if (line.startsWith('> ')) {
              return (
                <blockquote key={lIdx} className="border-l-2 border-[#0d0d0d] dark:border-white pl-3 italic text-[#5d5d5d] dark:text-[#b4b4b4] my-2">
                  {line.replace('> ', '')}
                </blockquote>
              );
            }
            if (line.trim().startsWith('- ') || line.trim().startsWith('* ')) {
              const text = line.trim().substring(2);
              return (
                <div key={lIdx} className="flex items-start gap-2 pl-2">
                  <span className="text-[#8e8e8e] mt-1.5 text-xs">•</span>
                  <span>{formatInlineMarkdown(text)}</span>
                </div>
              );
            }
            if (/^\d+\.\s/.test(line.trim())) {
              const match = line.trim().match(/^(\d+\.)\s(.*)/);
              if (match) {
                return (
                  <div key={lIdx} className="flex items-start gap-2 pl-2">
                    <span className="font-semibold text-[#8e8e8e]">{match[1]}</span>
                    <span>{formatInlineMarkdown(match[2])}</span>
                  </div>
                );
              }
            }
            if (!line.trim()) return <div key={lIdx} className="h-1" />;

            return <p key={lIdx} className="leading-7">{formatInlineMarkdown(line)}</p>;
          })}
        </div>
      );
    });
  };

  const formatInlineMarkdown = (text: string) => {
    const codeParts = text.split(/(`[^`]+`)/g);
    return codeParts.map((sub, i) => {
      if (sub.startsWith('`') && sub.endsWith('`')) {
        return (
          <code
            key={i}
            className="px-1.5 py-0.5 rounded bg-[#f0f0f0] dark:bg-[#2f2f2f] text-[#0d0d0d] dark:text-[#ececec] font-mono text-[13px] border border-[#e5e5e5] dark:border-[#3e3e3e]"
          >
            {sub.slice(1, -1)}
          </code>
        );
      }
      const boldParts = sub.split(/(\*\*[^*]+\*\*)/g);
      return boldParts.map((bSub, bI) => {
        if (bSub.startsWith('**') && bSub.endsWith('**')) {
          return <strong key={bI} className="font-semibold text-[#0d0d0d] dark:text-white">{bSub.slice(2, -2)}</strong>;
        }
        return bSub;
      });
    });
  };

  if (message.role === 'user') {
    return (
      <div ref={messageRef} className="flex justify-end mb-6">
        <div className="max-w-[85%] sm:max-w-[70%] bg-[#f4f4f4] dark:bg-[#2f2f2f] text-[#0d0d0d] dark:text-[#ececec] border border-[#e5e5e5] dark:border-transparent px-5 py-3.5 rounded-[24px] text-[15px] leading-relaxed shadow-xs">
          <p className="whitespace-pre-wrap">{message.content}</p>
        </div>
      </div>
    );
  }

  // Assistant Bubble with Monochrome AgriVision Branding
  return (
    <div ref={messageRef} className="w-full mb-8 text-[#0d0d0d] dark:text-[#ececec] text-[15px] group">
      {/* Brand Header */}
      <div className="flex items-center gap-2 mb-2 text-xs font-semibold text-[#0d0d0d] dark:text-white">
        <span className="w-5 h-5 rounded-md bg-[#0d0d0d] text-white dark:bg-white dark:text-black flex items-center justify-center font-bold text-[10px] shadow-xs">
          AV
        </span>
        <span>AgriVision</span>
      </div>

      {/* Optional Thought accordion if deep reasoning is active */}
      {message.thought && (
        <div className="mb-3 border border-[#e5e5e5] dark:border-[#383838] rounded-xl overflow-hidden bg-[#f9f9f9] dark:bg-[#181818] max-w-2xl">
          <button
            onClick={() => setShowThought(!showThought)}
            className="w-full px-3.5 py-2 flex items-center justify-between text-xs font-medium text-[#5d5d5d] dark:text-[#b4b4b4] hover:bg-[#f0f0f0] dark:hover:bg-[#212121] transition-colors cursor-pointer"
          >
            <span className="flex items-center gap-1.5">
              <span className="w-2 h-2 rounded-full bg-[#0d0d0d] dark:bg-white animate-pulse" />
              Tiến trình suy luận
            </span>
            {showThought ? <ChevronDown className="w-3.5 h-3.5" strokeWidth={1.75} /> : <ChevronRight className="w-3.5 h-3.5" strokeWidth={1.75} />}
          </button>
          {showThought && (
            <div className="px-3.5 py-2.5 text-xs text-[#5d5d5d] dark:text-[#8e8e8e] border-t border-[#e5e5e5] dark:border-[#383838] bg-[#f4f4f4] dark:bg-[#121212] leading-relaxed font-mono">
              {message.thought}
            </div>
          )}
        </div>
      )}

      {/* Direct Content: Minimalist, clean, immediate */}
      <div className="leading-relaxed">
        {renderFormattedContent(message.content)}
        {message.isStreaming && (
          <span className="inline-block w-2 h-4 ml-1.5 bg-[#0d0d0d] dark:bg-[#ececec] rounded-xs animate-pulse align-middle" />
        )}
      </div>

      {/* Action Bar */}
      {!message.isStreaming && message.content && (
        <div className="flex items-center gap-2 mt-2 pt-1 text-[#8e8e8e] opacity-80 group-hover:opacity-100 transition-opacity text-xs">
          <button
            onClick={handleCopy}
            title="Sao chép tin nhắn"
            className="p-1.5 rounded-md hover:bg-[#f0f0f0] dark:hover:bg-[#2f2f2f] text-[#5d5d5d] hover:text-[#0d0d0d] dark:text-[#8e8e8e] dark:hover:text-[#ececec] transition-colors cursor-pointer"
          >
            {copied ? <Check className="w-4 h-4 text-[#0d0d0d] dark:text-white" strokeWidth={1.75} /> : <Copy className="w-4 h-4" strokeWidth={1.75} />}
          </button>

          <button
            onClick={() => setLiked(liked === true ? null : true)}
            title="Hữu ích"
            className={`p-1.5 rounded-md hover:bg-[#f0f0f0] dark:hover:bg-[#2f2f2f] transition-colors cursor-pointer ${
              liked === true ? 'text-[#0d0d0d] dark:text-white font-bold' : 'text-[#5d5d5d] dark:text-[#8e8e8e]'
            }`}
          >
            <ThumbsUp className="w-4 h-4" strokeWidth={1.75} />
          </button>

          <button
            onClick={() => setLiked(liked === false ? null : false)}
            title="Chưa chính xác"
            className={`p-1.5 rounded-md hover:bg-[#f0f0f0] dark:hover:bg-[#2f2f2f] transition-colors cursor-pointer ${
              liked === false ? 'text-[#0d0d0d] dark:text-white font-bold' : 'text-[#5d5d5d] dark:text-[#8e8e8e]'
            }`}
          >
            <ThumbsDown className="w-4 h-4" strokeWidth={1.75} />
          </button>

          <button
            title="Tạo lại câu trả lời"
            className="p-1.5 rounded-md hover:bg-[#f0f0f0] dark:hover:bg-[#2f2f2f] text-[#5d5d5d] hover:text-[#0d0d0d] dark:text-[#8e8e8e] dark:hover:text-[#ececec] transition-colors cursor-pointer"
          >
            <RotateCcw className="w-4 h-4" strokeWidth={1.75} />
          </button>
        </div>
      )}
    </div>
  );
}
