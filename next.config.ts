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
  async headers() {
    return [
      {
        source: "/:path*",
        headers: [
          { key: "X-Frame-Options", value: "SAMEORIGIN" },
          { key: "X-Content-Type-Options", value: "nosniff" },
          { key: "Referrer-Policy", value: "strict-origin-when-cross-origin" },
          { key: "Permissions-Policy", value: "camera=(self), microphone=(), geolocation=()" },
        ],
      },
    ];
  },
};

export default nextConfig;
