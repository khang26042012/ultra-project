// src/app/api/vision/segment-and-annotate/route.ts
// AgriVision Computer Vision Lesion Segmentation & Neon HUD API Route

import { NextRequest, NextResponse } from 'next/server';
import { segmentAndAnnotateCropLesion } from '@/lib/visionSegmentation';

export const runtime = 'nodejs';

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const imageBase64 = body.imageBase64 || body.image || '';

    if (!imageBase64 || typeof imageBase64 !== 'string') {
      return NextResponse.json(
        {
          success: false,
          error: 'Thiếu trường imageBase64 trong dữ liệu gửi lên.',
        },
        { status: 400 }
      );
    }

    const result = await segmentAndAnnotateCropLesion(imageBase64);

    return NextResponse.json(result, { status: 200 });
  } catch (error: unknown) {
    const message = (error as Error)?.message || 'Lỗi bóc tách vết bệnh qua Computer Vision';
    console.error('Vision Segmentation API Error:', error);
    return NextResponse.json(
      {
        success: false,
        error: message,
      },
      { status: 500 }
    );
  }
}
