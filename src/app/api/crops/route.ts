import { NextRequest, NextResponse } from 'next/server';
import { loadAllCrops, normalizeVietnamese } from '@/lib/cropSearch';

export const runtime = 'nodejs';

export async function GET(req: NextRequest) {
  try {
    const { searchParams } = new URL(req.url);
    const query = searchParams.get('q') || searchParams.get('query') || '';
    const topic = searchParams.get('topic') || '';
    const limit = parseInt(searchParams.get('limit') || '50', 10);
    const offset = parseInt(searchParams.get('offset') || '0', 10);

    const allCrops = loadAllCrops();

    let filtered = allCrops;

    if (topic && topic !== 'all') {
      filtered = filtered.filter((c) => {
        if (topic === 'fruit') {
          return (
            c.topic === 'Cay_An_Trai_Dac_San' ||
            c.topic === 'Cay_An_Trai_Nhiet_Doi_Va_On_Doi'
          );
        }
        if (topic === 'grain') {
          return (
            c.topic === 'Cay_Luong_Thuc_Va_Hoa_Mau' ||
            c.topic === 'Cay_Luong_Thuc_Mau'
          );
        }
        if (topic === 'veg') {
          return (
            c.topic === 'Rau_Cu_Gia_Vi_Va_Nam' ||
            c.topic === 'Rau_An_La_An_Qua'
          );
        }
        if (topic === 'industrial') {
          return (
            c.topic === 'Cay_Cong_Nghiep_Xuat_Khau' ||
            c.topic === 'Cay_Cong_Nghiep_Duoc_Lieu'
          );
        }
        if (topic === 'medicinal_forest') {
          return c.topic === 'Cay_Lam_Nghiep_Duoc_Lieu_Quy';
        }
        if (topic === 'exotic_flower') {
          return (
            c.topic === 'Cay_Nhap_Khau_Kinh_Te_Cao' ||
            c.topic === 'Hoa_Kieng_Va_Canh_Quan'
          );
        }
        return c.topic === topic;
      });
    }

    if (query) {
      const normQ = normalizeVietnamese(query);
      filtered = filtered.filter((c) => {
        const normName = normalizeVietnamese(c.name_vi);
        const normSci = normalizeVietnamese(c.scientific_name);
        const normDiseases = (c.danh_sach_benh || [])
          .map((d) => normalizeVietnamese(d.ten_benh))
          .join(' ');
        return (
          normName.includes(normQ) ||
          normSci.includes(normQ) ||
          normDiseases.includes(normQ)
        );
      });
    }

    const total = filtered.length;
    const paginated = filtered.slice(offset, offset + limit);

    return NextResponse.json({
      success: true,
      total,
      total_in_db: allCrops.length,
      limit,
      offset,
      crops: paginated,
    });
  } catch (error) {
    return NextResponse.json(
      { success: false, error: (error as Error).message },
      { status: 500 }
    );
  }
}
