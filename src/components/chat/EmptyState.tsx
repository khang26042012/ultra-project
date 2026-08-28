'use client';

import React, { useRef, useEffect } from 'react';
import FloatingInputIsland from '@/components/input/FloatingInputIsland';
import gsap from 'gsap';

export default function EmptyState() {
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (containerRef.current) {
      gsap.fromTo(
        containerRef.current,
        { opacity: 0, y: 16 },
        { opacity: 1, y: 0, duration: 0.4, ease: 'power2.out' }
      );
    }
  }, []);

  return (
    <div
      ref={containerRef}
      className="flex-1 flex flex-col justify-center items-center px-4 w-full max-w-3xl mx-auto"
    >
      {/* Hero Greeting */}
      <div className="text-center mb-8">
        <h1 className="text-3xl sm:text-4xl font-semibold text-[#0d0d0d] dark:text-[#ececec] tracking-tight">
          AgriVision
        </h1>
        <p className="text-sm text-[#5d5d5d] dark:text-[#8e8e8e] mt-2 font-normal">
          Chẩn đoán sâu bệnh cây trồng tức thì qua hình ảnh
        </p>
      </div>

      {/* Center Input Box */}
      <div className="w-full mb-6">
        <FloatingInputIsland />
      </div>
    </div>
  );
}
