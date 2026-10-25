'use client';

import React from 'react';
import FloatingInputIsland from '@/components/input/FloatingInputIsland';

export default function EmptyState() {
  return (
    <div className="flex-1 flex flex-col justify-center items-center px-4 w-full max-w-3xl mx-auto">
      {/* Hero Greeting */}
      <div className="text-center mb-8">
        <h1 className="text-3xl sm:text-4xl font-semibold text-[#ececec] dark:text-[#ececec] tracking-tight">
          AgriVision
        </h1>
        <p className="text-sm text-[#8e8e8e] mt-2">
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
