'use client';

import React, { useState, useRef, useEffect } from 'react';
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
  Search,
  Globe,
  ExternalLink,
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

  const formatInlineMarkdown = (text: string) => {
    const codeParts = text.split(/(`[^`]+`)/g);
    return codeParts.map((sub, i) => {
      if (sub.startsWith('`') && sub.endsWith('`')) {
        return (
          <code
            key={i}
            className="px-1.5 py-0.5 rounded bg-[#f0f0f0] dark:bg-[#282828] text-[#0d0d0d] dark:text-[#ececec] font-mono text-[13px] border border-[#e5e5e5] dark:border-[#383838]"
          >
            {sub.slice(1, -1)}
          </code>
        );
      }
      const boldParts = sub.split(/(\*\*[^*]+\*\*)/g);
      return boldParts.map((bSub, bI) => {
        if (bSub.startsWith('**') && bSub.endsWith('**')) {
          return (
            <strong key={bI} className="font-semibold text-[#0d0d0d] dark:text-white">
              {bSub.slice(2, -2)}
            </strong>
          );
        }
        return bSub;
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
            // Check if second row is separator like |--|--|
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

        // Headings
        if (line.startsWith('### ')) {
          elements.push(
            <h3
              key={i}
              className="text-base font-semibold text-[#0d0d0d] dark:text-[#ececec] mt-3.5 mb-1.5"
            >
              {line.replace('### ', '')}
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
              {line.replace('## ', '')}
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
              {line.replace('# ', '')}
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
              className="border-l-2 border-[#0d0d0d] dark:border-white pl-3 italic text-[#5d5d5d] dark:text-[#b4b4b4] my-2"
            >
              {line.replace('> ', '')}
            </blockquote>
          );
          i++;
          continue;
        }

        // Bullet lists
        if (line.trim().startsWith('- ') || line.trim().startsWith('* ')) {
          const text = line.trim().substring(2);
          elements.push(
            <div key={i} className="flex items-start gap-2 pl-2">
              <span className="text-[#8e8e8e] mt-1.5 text-xs">•</span>
              <span>{formatInlineMarkdown(text)}</span>
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
              <div key={i} className="flex items-start gap-2 pl-2">
                <span className="font-semibold text-[#8e8e8e]">{match[1]}</span>
                <span>{formatInlineMarkdown(match[2])}</span>
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

  // User Message Bubble: neat on the right, rounded-[20px]
  if (message.role === 'user') {
    return (
      <div ref={messageRef} className="flex justify-end mb-6">
        <div className="max-w-[85%] sm:max-w-[70%] bg-[#f4f4f4] dark:bg-[#262626] text-[#0d0d0d] dark:text-[#ececec] border border-[#e5e5e5] dark:border-transparent px-4 sm:px-5 py-3 rounded-[20px] text-[15px] leading-relaxed shadow-xs">
          {message.imageUrl && (
            <div className="mb-2.5 overflow-hidden rounded-xl border border-[#dedede] dark:border-[#444] bg-black/5 max-w-sm">
              <img
                src={message.imageUrl}
                alt="Ảnh đính kèm chẩn đoán"
                className="w-full max-h-64 object-cover hover:scale-[1.02] transition-transform duration-200"
              />
            </div>
          )}
          {message.content && <p className="whitespace-pre-wrap">{message.content}</p>}
        </div>
      </div>
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

      {/* 1. Live Searching Indicator Badge */}
      {message.searchingQuery && (
        <div className="inline-flex items-center gap-2 mb-2.5 py-1 px-3 rounded-full bg-[#f4f4f4] dark:bg-[#212121] border border-[#e5e5e5] dark:border-[#383838] text-xs text-[#5d5d5d] dark:text-[#a3a3a3] animate-pulse">
          <Search className="w-3.5 h-3.5 text-[#0d0d0d] dark:text-white shrink-0" strokeWidth={1.5} />
          <span>
            Đang tra cứu dữ liệu thực tế: <strong className="font-semibold text-[#0d0d0d] dark:text-white">&ldquo;{message.searchingQuery}&rdquo;</strong>...
          </span>
        </div>
      )}

      {/* 2. Web Search Sources Dropdown Bar (9Router) */}
      {message.sources && message.sources.length > 0 && (
        <div className="mb-3 select-none">
          <button
            type="button"
            onClick={() => setShowSources(!showSources)}
            className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-[#f4f4f4] hover:bg-[#eaeaea] dark:bg-[#212121] dark:hover:bg-[#2c2c2c] border border-[#e5e5e5] dark:border-[#383838] text-xs font-medium text-[#5d5d5d] hover:text-[#0d0d0d] dark:text-[#a3a3a3] dark:hover:text-white transition-all cursor-pointer"
          >
            <Globe className="w-3.5 h-3.5 text-[#0d0d0d] dark:text-white" strokeWidth={1.5} />
            <span>Đã tham khảo {message.sources.length} nguồn thông tin thực tế</span>
            {showSources ? (
              <ChevronDown className="w-3 h-3 ml-0.5" strokeWidth={2} />
            ) : (
              <ChevronRight className="w-3 h-3 ml-0.5" strokeWidth={2} />
            )}
          </button>

          {showSources && (
            <div className="mt-2.5 pl-3.5 border-l-2 border-[#e5e5e5] dark:border-[#383838] space-y-2 py-1 max-h-60 overflow-y-auto">
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

      {/* 3. Thinking UI Standard (ChatGPT o1/o3 & Claude) */}
      {/* 3A: Live Streaming Thinking */}
      {isCurrentlyThinking && (
        <div className="flex items-center gap-1.5 text-xs text-[#737373] dark:text-[#a3a3a3] animate-pulse mb-2.5 select-none font-medium">
          <span>💭</span>
          <span>Đang suy nghĩ...</span>
        </div>
      )}

      {/* 3B: Settled Thinking (Auto-collapsed into 1 single thin line with Left Accent Border when expanded) */}
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
