'use client';

import React, { useState, useRef } from 'react';
import { Check, Copy } from 'lucide-react';
import gsap from 'gsap';

interface CodeBlockProps {
  language: string;
  code: string;
}

export default function CodeBlock({ language, code }: CodeBlockProps) {
  const [copied, setCopied] = useState(false);
  const copyBtnRef = useRef<HTMLButtonElement>(null);

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(code);
      setCopied(true);

      // GSAP bounce scale effect on button (60 FPS)
      if (copyBtnRef.current) {
        gsap.fromTo(
          copyBtnRef.current,
          { scale: 0.8 },
          { scale: 1, duration: 0.25, ease: 'back.out(2.5)' }
        );
      }

      setTimeout(() => setCopied(false), 2000);
    } catch {
      setCopied(false);
    }
  };

  return (
    <div className="my-3.5 rounded-xl overflow-hidden border border-[#e5e5e5] dark:border-[#383838] bg-[#0d0d0d] text-sm shadow-md">
      <div className="flex items-center justify-between px-4 py-2 bg-[#1a1a1a] text-xs font-mono text-[#b4b4b4]">
        <span className="lowercase font-semibold">{language || 'code'}</span>
        <button
          ref={copyBtnRef}
          onClick={handleCopy}
          className="flex items-center gap-1.5 hover:text-white transition-colors cursor-pointer select-none"
        >
          {copied ? (
            <>
              <Check className="w-3.5 h-3.5 text-white" strokeWidth={1.5} />
              <span className="text-white font-sans font-medium">Copied!</span>
            </>
          ) : (
            <>
              <Copy className="w-3.5 h-3.5 text-[#b4b4b4]" strokeWidth={1.5} />
              <span className="font-sans">Copy code</span>
            </>
          )}
        </button>
      </div>
      <div className="p-4 overflow-x-auto no-scrollbar text-[#ececec] font-mono leading-relaxed text-[13px]">
        <pre>
          <code>{code}</code>
        </pre>
      </div>
    </div>
  );
}
