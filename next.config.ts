import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: "standalone",
  devIndicators: false,
  poweredByHeader: false,
  outputFileTracingIncludes: {
    "/api/**/*": ["./src/data/**/*"],
  },
  images: {
    unoptimized: true, // Tiết kiệm tối đa CPU & RAM khi chạy trên VPS 1GB - 2GB
    remotePatterns: [
      { protocol: "https", hostname: "**.supabase.co" },
      { protocol: "https", hostname: "outline.roboflow.com" },
      { protocol: "https", hostname: "www.google.com" },
      { protocol: "https", hostname: "**.onrender.com" },
    ],
  },
};

export default nextConfig;
