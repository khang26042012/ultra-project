import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "AgriVision — Chuyên gia AI Nông nghiệp & Dịch bệnh Cây trồng",
  description: "AgriVision — Hệ thống AI chẩn đoán dịch bệnh cây trồng & Trợ lý nông nghiệp thông minh",
  icons: {
    icon: "/favicon.svg",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="en"
      className={`${geistSans.variable} ${geistMono.variable} h-full antialiased`}
      style={{ overscrollBehavior: 'none' }}
    >
      <body className="h-[100dvh] w-screen overflow-hidden fixed inset-0 flex flex-col bg-[#ffffff] dark:bg-[#171717] text-[#0d0d0d] dark:text-[#ececec]">
        {children}
      </body>
    </html>
  );
}
