'use client';

import React, { useState, useRef, useEffect, useCallback } from 'react';
import { Message } from '@/types/chat';
import CodeBlock from './CodeBlock';
import {
  Copy,
  Check,
  ThumbsUp,
  ThumbsDown,
  RotateCcw,
  ChevronDown,
  ChevronRight,
  ExternalLink,
  ZoomIn,
  ZoomOut,
  X,
} from 'lucide-react';
import gsap from 'gsap';

interface ChatMessageProps {
  message: Message;
}

export default function ChatMessage({ message }: ChatMessageProps) {
  const [copied, setCopied] = useState(false);
  const [liked, setLiked] = useState<boolean | null>(null);
  const [showThought, setShowThought] = useState(false);
  const [showSources, setShowSources] = useState(false);
  const [isLightboxOpen, setIsLightboxOpen] = useState(false);
  const [lightboxZoom, setLightboxZoom] = useState(1);
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

  // Keyboard shortcut (Escape) to close Lightbox
  const handleKeyDown = useCallback(
    (e: KeyboardEvent) => {
      if (e.key === 'Escape' && isLightboxOpen) {
        setIsLightboxOpen(false);
        setLightboxZoom(1);
      }
    },
    [isLightboxOpen]
  );

  useEffect(() => {
    if (isLightboxOpen) {
      window.addEventListener('keydown', handleKeyDown);
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = '';
    }
    return () => {
      window.removeEventListener('keydown', handleKeyDown);
      document.body.style.overflow = '';
    };
  }, [isLightboxOpen, handleKeyDown]);

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(message.content);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch {
      setCopied(false);
    }
  };

  // Full-featured Markdown Parser: Code, Links, Bold-Italic, Bold, Italic
  const formatInlineMarkdown = (text: string): React.ReactNode => {
    const codeParts = text.split(/(`[^`]+`)/g);

    return codeParts.map((part, pIdx) => {
      if (part.startsWith('`') && part.endsWith('`') && part.length >= 2) {
        return (
          <code
            key={`c-${pIdx}`}
            className="px-1.5 py-0.5 rounded bg-[#f0f0f0] dark:bg-[#282828] text-[#0d0d0d] dark:text-[#ececec] font-mono text-[13px] border border-[#e5e5e5] dark:border-[#383838]"
          >
            {part.slice(1, -1)}
          </code>
        );
      }

      // Link regex: [label](url)
      const linkRegex = /\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)/g;
      const tokens: { type: 'text' | 'link'; content: string; url?: string }[] = [];
      let lastIndex = 0;
      let match: RegExpExecArray | null;

      while ((match = linkRegex.exec(part)) !== null) {
        if (match.index > lastIndex) {
          tokens.push({ type: 'text', content: part.substring(lastIndex, match.index) });
        }
        tokens.push({ type: 'link', content: match[1], url: match[2] });
        lastIndex = match.index + match[0].length;
      }
      if (lastIndex < part.length) {
        tokens.push({ type: 'text', content: part.substring(lastIndex) });
      }

      return tokens.map((token, tIdx) => {
        if (token.type === 'link') {
          return (
            <a
              key={`l-${pIdx}-${tIdx}`}
              href={token.url}
              target="_blank"
              rel="noopener noreferrer"
              className="text-[#0d0d0d] dark:text-white underline decoration-[#8e8e8e] underline-offset-2 hover:decoration-[#0d0d0d] dark:hover:decoration-white font-medium inline-flex items-center gap-0.5"
            >
              <span>{token.content}</span>
            </a>
          );
        }

        // Sub-split for ***bold-italic***, **bold**, *italic*, _italic_
        const styleRegex = /(\*\*\*[^*]+\*\*\*|\*\*[^*]+\*\*|\*[^*]+\*|_[^_]+_)/g;
        const subParts = token.content.split(styleRegex);

        return subParts.map((sub, sIdx) => {
          if (sub.startsWith('***') && sub.endsWith('***') && sub.length >= 6) {
            return (
              <strong key={`bi-${pIdx}-${tIdx}-${sIdx}`} className="font-semibold text-[#0d0d0d] dark:text-white">
                <em className="italic">{sub.slice(3, -3)}</em>
              </strong>
            );
          }
          if (sub.startsWith('**') && sub.endsWith('**') && sub.length >= 4) {
            return (
              <strong key={`b-${pIdx}-${tIdx}-${sIdx}`} className="font-semibold text-[#0d0d0d] dark:text-white">
                {sub.slice(2, -2)}
              </strong>
            );
          }
          if (
            (sub.startsWith('*') && sub.endsWith('*') && sub.length >= 2) ||
            (sub.startsWith('_') && sub.endsWith('_') && sub.length >= 2)
          ) {
            return (
              <em
                key={`i-${pIdx}-${tIdx}-${sIdx}`}
                className="italic font-medium text-[#111] dark:text-[#f0f0f0]"
              >
                {sub.slice(1, -1)}
              </em>
            );
          }
          return sub;
        });
      });
    });
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

      const rawLines = part.split('\n');
      const elements: React.ReactNode[] = [];
      let i = 0;

      while (i < rawLines.length) {
        const line = rawLines[i];

        // Horizontal rule separator (-- or --- or ***) - Task 2
        if (/^(\-{2,}|\*{3,})$/.test(line.trim())) {
          elements.push(
            <hr key={i} className="my-3.5 border-t border-[#e5e5e5] dark:border-[#2a2a2a]" />
          );
          i++;
          continue;
        }

        // Markdown Table detection (consecutive lines starting with |)
        if (line.trim().startsWith('|') && line.trim().endsWith('|')) {
          const tableLines: string[] = [];
          while (i < rawLines.length && rawLines[i].trim().startsWith('|')) {
            tableLines.push(rawLines[i].trim());
            i++;
          }

          if (tableLines.length >= 2) {
            const headerRow = tableLines[0]
              .split('|')
              .slice(1, -1)
              .map((c) => c.trim());
            const startDataIdx = tableLines[1].includes('---') ? 2 : 1;
            const dataRows = tableLines.slice(startDataIdx).map((tl) =>
              tl
                .split('|')
                .slice(1, -1)
                .map((c) => c.trim())
            );

            elements.push(
              <div
                key={`table-${i}`}
                className="overflow-x-auto my-3 rounded-xl border border-[#e5e5e5] dark:border-[#333] shadow-xs"
              >
                <table className="w-full text-xs text-left border-collapse">
                  <thead className="bg-[#f7f7f8] dark:bg-[#1f1f1f] border-b border-[#e5e5e5] dark:border-[#333] text-[#0d0d0d] dark:text-white font-semibold">
                    <tr>
                      {headerRow.map((h, hIdx) => (
                        <th key={hIdx} className="px-3.5 py-2.5 whitespace-nowrap">
                          {formatInlineMarkdown(h)}
                        </th>
                      ))}
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-[#e5e5e5] dark:divide-[#333] bg-white dark:bg-[#181818]">
                    {dataRows.map((row, rIdx) => (
                      <tr
                        key={rIdx}
                        className="hover:bg-black/[0.02] dark:hover:bg-white/[0.02] transition-colors"
                      >
                        {row.map((cell, cIdx) => (
                          <td
                            key={cIdx}
                            className="px-3.5 py-2 text-[#5d5d5d] dark:text-[#b4b4b4] leading-relaxed"
                          >
                            {formatInlineMarkdown(cell)}
                          </td>
                        ))}
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            );
            continue;
          }
        }

        // Headings (check from h5 down to h1)
        if (line.startsWith('##### ')) {
          elements.push(
            <h5
              key={i}
              className="text-xs font-semibold uppercase tracking-wider text-[#737373] dark:text-[#a3a3a3] mt-2.5 mb-1"
            >
              {formatInlineMarkdown(line.replace('##### ', ''))}
            </h5>
          );
          i++;
          continue;
        }
        if (line.startsWith('#### ')) {
          elements.push(
            <h4
              key={i}
              className="text-sm font-semibold text-[#0d0d0d] dark:text-[#ececec] mt-3 mb-1"
            >
              {formatInlineMarkdown(line.replace('#### ', ''))}
            </h4>
          );
          i++;
          continue;
        }
        if (line.startsWith('### ')) {
          elements.push(
            <h3
              key={i}
              className="text-base font-semibold text-[#0d0d0d] dark:text-[#ececec] mt-3.5 mb-1.5"
            >
              {formatInlineMarkdown(line.replace('### ', ''))}
            </h3>
          );
          i++;
          continue;
        }
        if (line.startsWith('## ')) {
          elements.push(
            <h2
              key={i}
              className="text-lg font-bold text-[#0d0d0d] dark:text-[#ececec] mt-4 mb-2"
            >
              {formatInlineMarkdown(line.replace('## ', ''))}
            </h2>
          );
          i++;
          continue;
        }
        if (line.startsWith('# ')) {
          elements.push(
            <h1
              key={i}
              className="text-xl font-bold text-[#0d0d0d] dark:text-[#ececec] mt-5 mb-2.5"
            >
              {formatInlineMarkdown(line.replace('# ', ''))}
            </h1>
          );
          i++;
          continue;
        }

        // Blockquotes
        if (line.startsWith('> ')) {
          elements.push(
            <blockquote
              key={i}
              className="border-l-2 border-[#0d0d0d] dark:border-white pl-3.5 italic text-[#5d5d5d] dark:text-[#b4b4b4] my-2 leading-relaxed"
            >
              {formatInlineMarkdown(line.replace('> ', ''))}
            </blockquote>
          );
          i++;
          continue;
        }

        // Bullet lists - Task 3: pl-5 indent & neat styled dot
        if (line.trim().startsWith('- ') || line.trim().startsWith('* ')) {
          const text = line.trim().substring(2);
          elements.push(
            <div key={i} className="flex items-start gap-2.5 pl-5 my-1">
              <span className="w-1.5 h-1.5 rounded-full bg-[#8e8e8e] dark:bg-[#737373] mt-2.5 shrink-0" />
              <span className="leading-7 flex-1">{formatInlineMarkdown(text)}</span>
            </div>
          );
          i++;
          continue;
        }

        // Numbered lists
        if (/^\d+\.\s/.test(line.trim())) {
          const match = line.trim().match(/^(\d+\.)\s(.*)/);
          if (match) {
            elements.push(
              <div key={i} className="flex items-start gap-2.5 pl-2 my-1">
                <span className="font-semibold text-[#8e8e8e] shrink-0 mt-0.5">{match[1]}</span>
                <span className="leading-7 flex-1">{formatInlineMarkdown(match[2])}</span>
              </div>
            );
            i++;
            continue;
          }
        }

        if (!line.trim()) {
          elements.push(<div key={i} className="h-1" />);
          i++;
          continue;
        }

        // Standard paragraph
        elements.push(
          <p key={i} className="leading-7">
            {formatInlineMarkdown(line)}
          </p>
        );
        i++;
      }

      return (
        <div key={index} className="space-y-2">
          {elements}
        </div>
      );
    });
  };

  // User Message Bubble: neat on the right, compact thumbnail + Lightbox (Task 7)
  if (message.role === 'user') {
    return (
      <>
        <div ref={messageRef} className="flex justify-end mb-6">
          <div className="max-w-[85%] sm:max-w-[70%] bg-[#f4f4f4] dark:bg-[#262626] text-[#0d0d0d] dark:text-[#ececec] border border-[#e5e5e5] dark:border-transparent px-4 sm:px-5 py-3 rounded-[20px] text-[15px] leading-relaxed shadow-xs">
            {message.imageUrl && (
              <div
                onClick={() => {
                  setLightboxZoom(1);
                  setIsLightboxOpen(true);
                }}
                className="relative mb-2.5 overflow-hidden rounded-2xl border border-black/10 dark:border-white/10 bg-black/5 max-w-[220px] max-h-[160px] cursor-pointer group/img"
              >
                <img
                  src={message.imageUrl}
                  alt="Ảnh đính kèm chẩn đoán"
                  className="w-full h-full object-cover transition-transform duration-200 group-hover/img:scale-105"
                />
                <div className="absolute bottom-1.5 right-1.5 bg-black/60 text-white text-[10px] px-2 py-0.5 rounded-full backdrop-blur-xs flex items-center gap-1 opacity-90 group-hover/img:opacity-100 transition-opacity">
                  <ZoomIn className="w-3 h-3" strokeWidth={1.75} />
                  <span>Phóng to</span>
                </div>
              </div>
            )}
            {message.content && <p className="whitespace-pre-wrap">{message.content}</p>}
          </div>
        </div>

        {/* Image Lightbox Modal */}
        {isLightboxOpen && message.imageUrl && (
          <div
            onClick={() => {
              setIsLightboxOpen(false);
              setLightboxZoom(1);
            }}
            className="fixed inset-0 z-50 bg-black/85 backdrop-blur-md flex flex-col items-center justify-center p-4 select-none animate-in fade-in duration-150"
          >
            {/* Top Lightbox Controls */}
            <div
              onClick={(e) => e.stopPropagation()}
              className="absolute top-4 right-4 flex items-center gap-2 bg-black/50 p-1.5 rounded-full backdrop-blur-md border border-white/20 text-white z-10"
            >
              <button
                type="button"
                onClick={() => setLightboxZoom((prev) => Math.min(prev + 0.25, 3))}
                title="Phóng to (+)"
                className="p-1.5 rounded-full hover:bg-white/20 transition-colors cursor-pointer"
              >
                <ZoomIn className="w-4 h-4" strokeWidth={2} />
              </button>
              <button
                type="button"
                onClick={() => setLightboxZoom((prev) => Math.max(prev - 0.25, 0.5))}
                title="Thu nhỏ (-)"
                className="p-1.5 rounded-full hover:bg-white/20 transition-colors cursor-pointer"
              >
                <ZoomOut className="w-4 h-4" strokeWidth={2} />
              </button>
              <button
                type="button"
                onClick={() => setLightboxZoom(1)}
                title="Đặt lại kích thước (100%)"
                className="p-1.5 rounded-full hover:bg-white/20 transition-colors cursor-pointer"
              >
                <RotateCcw className="w-4 h-4" strokeWidth={2} />
              </button>
              <div className="w-px h-4 bg-white/30" />
              <button
                type="button"
                onClick={() => {
                  setIsLightboxOpen(false);
                  setLightboxZoom(1);
                }}
                title="Đóng (Esc)"
                className="p-1.5 rounded-full hover:bg-white/20 transition-colors text-white/90 hover:text-white cursor-pointer"
              >
                <X className="w-4 h-4" strokeWidth={2} />
              </button>
            </div>

            {/* Lightbox Image Stage */}
            <div
              onClick={(e) => e.stopPropagation()}
              className="relative max-w-4xl max-h-[85vh] overflow-hidden flex items-center justify-center"
            >
              <img
                src={message.imageUrl}
                alt="Chi tiết ảnh bệnh cây trồng"
                style={{ transform: `scale(${lightboxZoom})` }}
                className="max-w-full max-h-[80vh] object-contain rounded-xl shadow-2xl transition-transform duration-200"
              />
            </div>
            <div className="absolute bottom-4 text-xs text-white/70">
              Nhấn ESC hoặc bấm ra ngoài để đóng • Bấm +/- để thu phóng
            </div>
          </div>
        )}
      </>
    );
  }

  const isCurrentlyThinking = message.isThinking && message.isStreaming;
  const hasSettledThought = !isCurrentlyThinking && !!message.thought;

  // Assistant Bubble with Minimalist Monochrome Branding
  return (
    <div ref={messageRef} className="w-full mb-8 text-[#0d0d0d] dark:text-[#ececec] text-[15px] group">
      {/* Brand Header */}
      <div className="flex items-center gap-2 mb-2 text-xs font-semibold text-[#0d0d0d] dark:text-white">
        <span className="w-5 h-5 rounded-md bg-[#0d0d0d] text-white dark:bg-white dark:text-black flex items-center justify-center font-bold text-[10px] shadow-xs">
          AV
        </span>
        <span>AgriVision</span>
      </div>

      {/* 1. Live Searching Indicator Badge (Task 4: Thin text like thinking) */}
      {message.searchingQuery && (
        <div className="inline-flex items-center text-xs font-medium text-[#737373] dark:text-[#a3a3a3] animate-pulse mb-2 select-none">
          <span>Đang tìm kiếm thông tin...</span>
        </div>
      )}

      {/* 2. Web Search Sources Dropdown Bar (Task 4: Thin button like thinking) */}
      {message.sources && message.sources.length > 0 && (
        <div className="mb-2.5 select-none">
          <button
            type="button"
            onClick={() => setShowSources(!showSources)}
            className="inline-flex items-center gap-1 text-xs font-medium text-[#737373] hover:text-[#0d0d0d] dark:text-[#a3a3a3] dark:hover:text-white transition-colors cursor-pointer"
          >
            <span>Đã tìm kiếm {message.sources.length} nguồn thông tin</span>
            {showSources ? (
              <ChevronDown className="w-3 h-3" strokeWidth={2} />
            ) : (
              <ChevronRight className="w-3 h-3" strokeWidth={2} />
            )}
          </button>

          {showSources && (
            <div className="mt-2 pl-3.5 border-l-2 border-[#e5e5e5] dark:border-[#383838] space-y-2 py-1 max-h-60 overflow-y-auto">
              {message.sources.map((src, sIdx) => {
                let domain = '';
                try {
                  domain = new URL(src.url).hostname.replace('www.', '');
                } catch {
                  domain = 'web';
                }
                return (
                  <a
                    key={sIdx}
                    href={src.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="flex flex-col group/src text-left p-2 rounded-xl hover:bg-[#f4f4f4] dark:hover:bg-[#212121] transition-colors border border-transparent hover:border-[#e5e5e5] dark:hover:border-[#333]"
                  >
                    <div className="flex items-center gap-1.5 text-[11px] text-[#8e8e8e]">
                      <ExternalLink className="w-3 h-3 group-hover/src:text-[#0d0d0d] dark:group-hover/src:text-white" />
                      <span className="truncate font-mono">{domain}</span>
                    </div>
                    <div className="text-xs font-medium text-[#0d0d0d] dark:text-[#ececec] group-hover/src:underline line-clamp-1 mt-0.5">
                      {src.title}
                    </div>
                    {src.snippet && (
                      <div className="text-[11px] text-[#737373] dark:text-[#8e8e8e] line-clamp-2 mt-0.5 leading-snug">
                        {src.snippet}
                      </div>
                    )}
                  </a>
                );
              })}
            </div>
          )}
        </div>
      )}

      {/* 3. Thinking UI Standard (Task 5: exact match to settled text, no cloud emoji) */}
      {/* 3A: Live Streaming Thinking */}
      {isCurrentlyThinking && (
        <div className="inline-flex items-center text-xs font-medium text-[#737373] dark:text-[#a3a3a3] animate-pulse mb-2.5 select-none">
          <span>Đang suy nghĩ...</span>
        </div>
      )}

      {/* 3B: Settled Thinking */}
      {hasSettledThought && (
        <div className="mb-2.5 select-none">
          <button
            type="button"
            onClick={() => setShowThought(!showThought)}
            className="inline-flex items-center gap-1 text-xs font-medium text-[#737373] hover:text-[#0d0d0d] dark:text-[#a3a3a3] dark:hover:text-white transition-colors cursor-pointer"
          >
            <span>
              {message.thinkingSeconds
                ? `Đã suy luận trong ${message.thinkingSeconds}s`
                : 'Tiến trình suy luận'}
            </span>
            {showThought ? (
              <ChevronDown className="w-3 h-3" strokeWidth={2} />
            ) : (
              <ChevronRight className="w-3 h-3" strokeWidth={2} />
            )}
          </button>

          {showThought && (
            <div className="border-l-2 border-[#e5e5e5] dark:border-[#383838] pl-3.5 my-2 max-h-72 overflow-y-auto text-[13px] text-[#5d5d5d] dark:text-[#a3a3a3] font-sans leading-relaxed whitespace-pre-wrap">
              {message.thought}
            </div>
          )}
        </div>
      )}

      {/* 4. Direct Content: Minimalist, clean, immediate */}
      <div className="leading-relaxed">
        {renderFormattedContent(message.content)}
        {message.isStreaming && !isCurrentlyThinking && (
          <span className="inline-block w-2 h-4 ml-1.5 bg-[#0d0d0d] dark:bg-[#ececec] rounded-xs animate-pulse align-middle" />
        )}
      </div>

      {/* 5. Action Bar */}
      {!message.isStreaming && message.content && (
        <div className="flex items-center gap-2 mt-2 pt-1 text-[#8e8e8e] opacity-80 group-hover:opacity-100 transition-opacity text-xs">
          <button
            onClick={handleCopy}
            title="Sao chép tin nhắn"
            className="p-1.5 rounded-md hover:bg-[#f0f0f0] dark:hover:bg-[#2f2f2f] text-[#5d5d5d] hover:text-[#0d0d0d] dark:text-[#8e8e8e] dark:hover:text-[#ececec] transition-colors cursor-pointer"
          >
            {copied ? (
              <Check className="w-4 h-4 text-[#0d0d0d] dark:text-white" strokeWidth={1.5} />
            ) : (
              <Copy className="w-4 h-4" strokeWidth={1.5} />
            )}
          </button>

          <button
            onClick={() => setLiked(liked === true ? null : true)}
            title="Hữu ích"
            className={`p-1.5 rounded-md hover:bg-[#f0f0f0] dark:hover:bg-[#2f2f2f] transition-colors cursor-pointer ${
              liked === true ? 'text-[#0d0d0d] dark:text-white font-bold' : 'text-[#5d5d5d] dark:text-[#8e8e8e]'
            }`}
          >
            <ThumbsUp className="w-4 h-4" strokeWidth={1.5} />
          </button>

          <button
            onClick={() => setLiked(liked === false ? null : false)}
            title="Chưa chính xác"
            className={`p-1.5 rounded-md hover:bg-[#f0f0f0] dark:hover:bg-[#2f2f2f] transition-colors cursor-pointer ${
              liked === false ? 'text-[#0d0d0d] dark:text-white font-bold' : 'text-[#5d5d5d] dark:text-[#8e8e8e]'
            }`}
          >
            <ThumbsDown className="w-4 h-4" strokeWidth={1.5} />
          </button>

          <button
            title="Tạo lại câu trả lời"
            className="p-1.5 rounded-md hover:bg-[#f0f0f0] dark:hover:bg-[#2f2f2f] text-[#5d5d5d] hover:text-[#0d0d0d] dark:text-[#8e8e8e] dark:hover:text-[#ececec] transition-colors cursor-pointer"
          >
            <RotateCcw className="w-4 h-4" strokeWidth={1.5} />
          </button>
        </div>
      )}
    </div>
  );
}
