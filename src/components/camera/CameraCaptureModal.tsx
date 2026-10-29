'use client';

import React, { useState, useRef, useEffect, useCallback } from 'react';
import { createPortal } from 'react-dom';
import {
  Camera,
  RefreshCw,
  Zap,
  ZapOff,
  X,
  Check,
  RotateCcw,
  AlertCircle,
  Image as ImageIcon,
  Scan,
  ShieldAlert,
  ArrowUp,
  Settings,
  HelpCircle,
  ChevronDown,
  ChevronUp,
  ExternalLink,
  Sparkles,
} from 'lucide-react';
import gsap from 'gsap';

interface CameraCaptureModalProps {
  isOpen: boolean;
  onClose: () => void;
  onCapture: (base64Image: string, fileName: string) => void;
  onSwitchToUpload?: () => void;
}

// Client-side image compressor for native camera fallback
const compressFile = (file: File): Promise<string> => {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = (e) => {
      const img = new Image();
      img.onload = () => {
        const canvas = document.createElement('canvas');
        let width = img.width;
        let height = img.height;
        const maxDim = 1600; // High resolution for pathology diagnosis

        if (width > maxDim || height > maxDim) {
          if (width > height) {
            height = Math.round((height * maxDim) / width);
            width = maxDim;
          } else {
            width = Math.round((width * maxDim) / height);
            height = maxDim;
          }
        }

        canvas.width = width;
        canvas.height = height;
        const ctx = canvas.getContext('2d');
        if (ctx) {
          ctx.drawImage(img, 0, 0, width, height);
          const base64 = canvas.toDataURL('image/jpeg', 0.92);
          resolve(base64);
        } else {
          resolve(e.target?.result as string);
        }
      };
      img.onerror = () => reject(new Error('Không thể đọc ảnh chụp'));
      img.src = e.target?.result as string;
    };
    reader.onerror = () => reject(new Error('Không thể tải tệp'));
    reader.readAsDataURL(file);
  });
};

export default function CameraCaptureModal({
  isOpen,
  onClose,
  onCapture,
  onSwitchToUpload,
}: CameraCaptureModalProps) {
  const [mounted, setMounted] = useState(false);
  const [facingMode, setFacingMode] = useState<'environment' | 'user'>('environment');
  const [torchAvailable, setTorchAvailable] = useState(false);
  const [torchOn, setTorchOn] = useState(false);
  const [resolution, setResolution] = useState<{ width: number; height: number } | null>(null);
  const [capturedImage, setCapturedImage] = useState<string | null>(null);
  const [capturedResolution, setCapturedResolution] = useState<{ width: number; height: number } | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [isInitializing, setIsInitializing] = useState(false);
  const [showGuide, setShowGuide] = useState(true);
  const [isPermissionDenied, setIsPermissionDenied] = useState(false);

  const videoRef = useRef<HTMLVideoElement>(null);
  const streamRef = useRef<MediaStream | null>(null);
  const modalRef = useRef<HTMLDivElement>(null);
  const flashRef = useRef<HTMLDivElement>(null);
  const nativeCameraInputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    setMounted(true);
  }, []);

  // Stop camera tracks cleanly
  const stopCamera = useCallback(() => {
    if (streamRef.current) {
      try {
        streamRef.current.getTracks().forEach((track) => {
          track.stop();
        });
      } catch (err) {
        console.error('Lỗi khi dừng camera:', err);
      }
      streamRef.current = null;
    }
    if (videoRef.current) {
      videoRef.current.srcObject = null;
    }
    setTorchOn(false);
    setTorchAvailable(false);
  }, []);

  // Start camera with tiered high-resolution constraints
  const startCamera = useCallback(
    async (facing: 'environment' | 'user') => {
      stopCamera();
      setError(null);
      setIsPermissionDenied(false);
      setResolution(null);
      setIsInitializing(true);

      if (typeof navigator === 'undefined' || !navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
        setError('Trình duyệt của bạn không hỗ trợ Camera Web API trực tiếp. Vui lòng sử dụng tính năng chụp bằng máy ảnh thiết bị.');
        setIsInitializing(false);
        return;
      }

      // Query permissions API if available to detect state
      if (typeof navigator.permissions !== 'undefined' && navigator.permissions.query) {
        try {
          const perm = await navigator.permissions.query({ name: 'camera' as any });
          if (perm.state === 'denied') {
            setIsPermissionDenied(true);
            setError('Quyền truy cập máy ảnh đang bị chặn trên trình duyệt.');
            setIsInitializing(false);
            return;
          }
        } catch {
          // Some browsers do not support querying camera permission
        }
      }

      // Constraints tiers: 4K Ultra HD -> 1080p Full HD -> Standard
      const constraintTiers: MediaStreamConstraints[] = [
        {
          audio: false,
          video: {
            facingMode: { ideal: facing },
            width: { min: 1280, ideal: 3840, max: 4096 },
            height: { min: 720, ideal: 2160, max: 2160 },
            aspectRatio: { ideal: 4 / 3 },
          },
        },
        {
          audio: false,
          video: {
            facingMode: { ideal: facing },
            width: { min: 1280, ideal: 1920 },
            height: { min: 720, ideal: 1080 },
          },
        },
        {
          audio: false,
          video: {
            facingMode: { ideal: facing },
          },
        },
        {
          audio: false,
          video: true,
        },
      ];

      let activeStream: MediaStream | null = null;
      let lastErr: any = null;

      for (const constraints of constraintTiers) {
        try {
          activeStream = await navigator.mediaDevices.getUserMedia(constraints);
          if (activeStream) break;
        } catch (err: any) {
          lastErr = err;
        }
      }

      if (!activeStream) {
        console.error('Không thể mở camera:', lastErr);
        if (
          lastErr?.name === 'NotAllowedError' ||
          lastErr?.name === 'PermissionDeniedError' ||
          lastErr?.message?.toLowerCase().includes('denied')
        ) {
          setIsPermissionDenied(true);
          setError('Quyền truy cập camera bị từ chối hoặc đang bị chặn trên trình duyệt.');
        } else if (lastErr?.name === 'NotFoundError' || lastErr?.name === 'DevicesNotFoundError') {
          setError('Không tìm thấy camera khả dụng trên thiết bị này.');
        } else {
          setError('Lỗi khởi tạo máy ảnh: ' + (lastErr?.message || 'Không thể kết nối cảm biến'));
        }
        setIsInitializing(false);
        return;
      }

      streamRef.current = activeStream;

      // Check torch capability
      try {
        const track = activeStream.getVideoTracks()[0];
        if (track) {
          const caps = (track.getCapabilities ? track.getCapabilities() : {}) as any;
          if (caps && caps.torch) {
            setTorchAvailable(true);
          }
        }
      } catch (e) {
        console.log('Torch check not supported:', e);
      }

      if (videoRef.current) {
        videoRef.current.srcObject = activeStream;
        videoRef.current
          .play()
          .then(() => {
            setIsInitializing(false);
          })
          .catch((e) => {
            console.log('Play stream notice:', e);
            setIsInitializing(false);
          });
      } else {
        setIsInitializing(false);
      }
    },
    [stopCamera]
  );

  // Directly trigger browser permission prompt through a direct user click
  const handleRequestPermission = async () => {
    setIsInitializing(true);
    setError(null);
    try {
      // Direct simple constraint request on user click triggers browser prompt
      const testStream = await navigator.mediaDevices.getUserMedia({ video: true });
      // If user allowed, stop test stream and run full high-res start
      testStream.getTracks().forEach((t) => t.stop());
      setIsPermissionDenied(false);
      await startCamera(facingMode);
    } catch (err: any) {
      console.error('User permission request rejected:', err);
      setIsPermissionDenied(true);
      setError('Quyền truy cập máy ảnh đang bị chặn trên trình duyệt.');
      setIsInitializing(false);
    }
  };

  // Trigger Native Camera App Fallback via HTML5 capture="environment"
  const handleOpenNativeCamera = () => {
    if (nativeCameraInputRef.current) {
      nativeCameraInputRef.current.click();
    }
  };

  // Handle image taken from native camera app
  const handleNativeCameraFileChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const files = e.target.files;
    if (files && files.length > 0) {
      const file = files[0];
      try {
        setIsInitializing(true);
        const compressedBase64 = await compressFile(file);
        const timestamp = new Date().toISOString().replace(/[-:T.]/g, '').slice(0, 14);
        const fileName = 'Chup_MayAnh_' + timestamp + '.jpg';
        setCapturedImage(compressedBase64);
        setCapturedResolution({ width: 1600, height: 1200 });
        setError(null);
      } catch (err) {
        console.error('Lỗi đọc ảnh từ máy ảnh:', err);
        setError('Không thể xử lý ảnh từ máy ảnh thiết bị.');
      } finally {
        setIsInitializing(false);
      }
    }
  };

  // Initialize or teardown when modal opens/closes
  useEffect(() => {
    if (isOpen) {
      setCapturedImage(null);
      setCapturedResolution(null);
      startCamera(facingMode);

      if (modalRef.current) {
        gsap.fromTo(
          modalRef.current,
          { opacity: 0, scale: 0.96 },
          { opacity: 1, scale: 1, duration: 0.25, ease: 'power2.out' }
        );
      }
    } else {
      stopCamera();
    }

    return () => {
      stopCamera();
    };
  }, [isOpen, startCamera, stopCamera]);

  // Read actual stream resolution when loaded
  const handleLoadedMetadata = () => {
    if (videoRef.current) {
      const w = videoRef.current.videoWidth;
      const h = videoRef.current.videoHeight;
      if (w && h) {
        setResolution({ width: w, height: h });
      }
    }
  };

  // Switch between Rear and Front camera
  const handleSwitchCamera = () => {
    const nextFacing = facingMode === 'environment' ? 'user' : 'environment';
    setFacingMode(nextFacing);
    startCamera(nextFacing);
  };

  // Toggle flash torch
  const handleToggleTorch = async () => {
    if (!streamRef.current || !torchAvailable) return;
    const track = streamRef.current.getVideoTracks()[0];
    if (!track) return;
    const nextState = !torchOn;
    try {
      await (track as any).applyConstraints({
        advanced: [{ torch: nextState }],
      });
      setTorchOn(nextState);
    } catch (err) {
      console.error('Không thể kích hoạt đèn flash:', err);
    }
  };

  // Capture high-resolution photo from the live video stream
  const handleCapture = () => {
    if (!videoRef.current) return;
    const video = videoRef.current;
    const w = video.videoWidth || 1920;
    const h = video.videoHeight || 1080;

    const canvas = document.createElement('canvas');
    canvas.width = w;
    canvas.height = h;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    // Flip user camera so selfie doesn't look inverted
    if (facingMode === 'user') {
      ctx.translate(w, 0);
      ctx.scale(-1, 1);
    }

    ctx.drawImage(video, 0, 0, w, h);

    // High quality JPEG (0.94) to preserve fine lesions, fungal spores, and halos
    const base64 = canvas.toDataURL('image/jpeg', 0.94);
    setCapturedImage(base64);
    setCapturedResolution({ width: w, height: h });

    // Haptic feedback for tactile feel
    if (typeof navigator !== 'undefined' && navigator.vibrate) {
      navigator.vibrate(50);
    }

    // Shutter flash effect
    if (flashRef.current) {
      gsap.fromTo(
        flashRef.current,
        { opacity: 0.9 },
        { opacity: 0, duration: 0.22, ease: 'power2.out' }
      );
    }
  };

  // Retake photo
  const handleRetake = () => {
    setCapturedImage(null);
    setCapturedResolution(null);
    if (!streamRef.current || !streamRef.current.active) {
      startCamera(facingMode);
    }
  };

  // Confirm and use captured photo
  const handleConfirmPhoto = () => {
    if (!capturedImage) return;
    const timestamp = new Date().toISOString().replace(/[-:T.]/g, '').slice(0, 14);
    const fileName = 'Chup_Camera_AgriVision_' + timestamp + '.jpg';
    stopCamera();
    onCapture(capturedImage, fileName);
    onClose();
  };

  // Close modal and stop hardware
  const handleClose = () => {
    stopCamera();
    onClose();
  };

  if (!isOpen || !mounted) return null;

  return createPortal(
    <div className="fixed inset-0 z-[99999] flex items-center justify-center bg-black/90 backdrop-blur-md p-2 sm:p-4 select-none">
      {/* Hidden Native Camera Input with capture="environment" */}
      <input
        ref={nativeCameraInputRef}
        type="file"
        accept="image/*"
        capture="environment"
        onChange={handleNativeCameraFileChange}
        className="hidden"
      />

      <div
        ref={modalRef}
        className="relative w-full max-w-2xl h-[94vh] sm:h-[88vh] max-h-[840px] bg-[#121212] text-white rounded-3xl border border-white/15 shadow-2xl flex flex-col overflow-hidden"
      >
        {/* Shutter White Flash Overlay */}
        <div
          ref={flashRef}
          className="pointer-events-none absolute inset-0 bg-white opacity-0 z-50 transition-opacity"
        />

        {/* Top Header Bar */}
        <div className="flex items-center justify-between px-4 py-3 bg-[#1a1a1a]/90 border-b border-white/10 z-10 shrink-0">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center border border-emerald-500/30">
              <Camera className="w-4 h-4" />
            </div>
            <div>
              <h3 className="text-sm font-semibold text-white tracking-wide flex items-center gap-1.5">
                <span>Chụp ảnh chẩn đoán vi thể</span>
                <span className="text-[10px] uppercase font-bold px-1.5 py-0.5 rounded-full bg-emerald-500/20 text-emerald-400 border border-emerald-500/40">
                  HD Camera
                </span>
              </h3>
              <p className="text-[11px] text-[#8e8e8e]">
                {capturedImage
                  ? ('Xem trước ảnh chụp • ' + (capturedResolution?.width || 0) + '×' + (capturedResolution?.height || 0) + 'px')
                  : resolution
                  ? ('Độ phân giải cảm biến: ' + resolution.width + '×' + resolution.height + 'px')
                  : error
                  ? 'Gợi ý quyền máy ảnh'
                  : 'Đang kết nối ống kính vi thể...'}
              </p>
            </div>
          </div>

          <div className="flex items-center gap-2">
            {/* Flash Torch Toggle (if supported) */}
            {torchAvailable && !capturedImage && !error && (
              <button
                type="button"
                onClick={handleToggleTorch}
                title={torchOn ? 'Tắt đèn trợ sáng' : 'Bật đèn trợ sáng'}
                className={
                  'p-2 rounded-full transition-colors cursor-pointer ' +
                  (torchOn
                    ? 'bg-amber-500/20 text-amber-300 border border-amber-500/40'
                    : 'bg-white/5 hover:bg-white/10 text-white/70 hover:text-white')
                }
              >
                {torchOn ? <Zap className="w-4 h-4" /> : <ZapOff className="w-4 h-4" />}
              </button>
            )}

            {/* Close Button */}
            <button
              type="button"
              onClick={handleClose}
              title="Đóng camera"
              className="p-2 rounded-full bg-white/5 hover:bg-white/10 text-white/70 hover:text-white transition-colors cursor-pointer"
            >
              <X className="w-5 h-5" />
            </button>
          </div>
        </div>

        {/* Main Viewfinder / Permission Error View */}
        <div className="relative flex-1 bg-black flex items-center justify-center overflow-y-auto no-scrollbar">
          {error ? (
            <div className="px-4 py-6 w-full max-w-lg text-center flex flex-col items-center">
              {/* Alert Badge */}
              <div className="w-14 h-14 rounded-full bg-rose-500/10 text-rose-400 flex items-center justify-center mb-3 border border-rose-500/20 shadow-lg shadow-rose-500/5">
                <ShieldAlert className="w-7 h-7" />
              </div>

              <h4 className="text-base font-semibold text-white mb-1.5">
                Quyền truy cập máy ảnh chưa được cấp
              </h4>
              <p className="text-xs text-rose-300/90 font-medium mb-4 max-w-md">
                {error}
              </p>

              {/* ACTION 1: NATIVE CAMERA APP (Zero-Permission Fallback) */}
              <div className="w-full bg-emerald-950/30 border border-emerald-500/30 rounded-2xl p-3.5 mb-4 text-left shadow-lg">
                <div className="flex items-start gap-3">
                  <div className="w-9 h-9 rounded-xl bg-emerald-500 text-black flex items-center justify-center shrink-0 mt-0.5">
                    <Camera className="w-5 h-5" />
                  </div>
                  <div className="flex-1">
                    <div className="text-xs font-bold text-white flex items-center gap-1.5">
                      <span>Mở máy ảnh chụp ngay</span>
                      <span className="text-[9px] font-bold px-1.5 py-0.2 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
                        Khuyên dùng
                      </span>
                    </div>
                    <p className="text-[11px] text-white/70 mt-0.5 leading-relaxed">
                      Sử dụng trực tiếp ứng dụng Máy ảnh gốc của điện thoại, không cần cài đặt hay cấp quyền trình duyệt.
                    </p>
                    <button
                      type="button"
                      onClick={handleOpenNativeCamera}
                      className="mt-2.5 w-full py-2 px-3 rounded-xl bg-emerald-500 hover:bg-emerald-400 text-black text-xs font-bold flex items-center justify-center gap-2 transition-transform active:scale-[0.98] cursor-pointer shadow-md"
                    >
                      <Camera className="w-4 h-4" />
                      <span>Chụp ảnh bằng máy ảnh thiết bị</span>
                    </button>
                  </div>
                </div>
              </div>

              {/* ACTION 2: HOW TO ENABLE IN BROWSER */}
              <div className="w-full bg-white/5 border border-white/10 rounded-2xl p-3.5 mb-4 text-left">
                <button
                  type="button"
                  onClick={() => setShowGuide(!showGuide)}
                  className="w-full flex items-center justify-between text-xs font-semibold text-white/90 cursor-pointer"
                >
                  <span className="flex items-center gap-2">
                    <Settings className="w-4 h-4 text-emerald-400" />
                    <span>Hướng dẫn bật quyền trên trình duyệt (3 giây)</span>
                  </span>
                  {showGuide ? <ChevronUp className="w-4 h-4 text-white/50" /> : <ChevronDown className="w-4 h-4 text-white/50" />}
                </button>

                {showGuide && (
                  <div className="mt-3 space-y-2.5 pt-2.5 border-t border-white/10 text-[11px] text-white/80">
                    <div className="flex items-start gap-2.5">
                      <span className="w-5 h-5 rounded-full bg-white/10 text-emerald-400 font-bold flex items-center justify-center shrink-0 text-[10px]">
                        1
                      </span>
                      <p className="leading-snug">
                        Nhìn lên góc trên thanh địa chỉ, bấm vào biểu tượng <strong>Cài đặt / Ổ khóa 🔒</strong> (cạnh chữ <em>argivision.io.vn</em>).
                      </p>
                    </div>

                    <div className="flex items-start gap-2.5">
                      <span className="w-5 h-5 rounded-full bg-white/10 text-emerald-400 font-bold flex items-center justify-center shrink-0 text-[10px]">
                        2
                      </span>
                      <p className="leading-snug">
                        Chọn mục <strong>&quot;Quyền&quot; (Permissions)</strong> → Tìm dòng <strong>&quot;Máy ảnh&quot; (Camera)</strong>.
                      </p>
                    </div>

                    <div className="flex items-start gap-2.5">
                      <span className="w-5 h-5 rounded-full bg-white/10 text-emerald-400 font-bold flex items-center justify-center shrink-0 text-[10px]">
                        3
                      </span>
                      <p className="leading-snug">
                        Gạt công tắc sang <strong>&quot;Cho phép&quot; (Allow)</strong>, sau đó quay lại đây bấm nút &quot;Thử xin quyền lại&quot;.
                      </p>
                    </div>
                  </div>
                )}
              </div>

              {/* ACTION 3: TRY REQUESTING PERMISSION AGAIN */}
              <div className="flex items-center justify-center gap-2.5 w-full flex-wrap">
                <button
                  type="button"
                  onClick={handleRequestPermission}
                  disabled={isInitializing}
                  className="py-2.5 px-4 rounded-xl bg-white/15 hover:bg-white/25 text-white text-xs font-semibold flex items-center gap-1.5 transition-all active:scale-[0.98] cursor-pointer"
                >
                  <RotateCcw className={'w-3.5 h-3.5 ' + (isInitializing ? 'animate-spin' : '')} />
                  <span>Thử xin quyền lại</span>
                </button>

                {onSwitchToUpload && (
                  <button
                    type="button"
                    onClick={() => {
                      handleClose();
                      onSwitchToUpload();
                    }}
                    className="py-2.5 px-4 rounded-xl bg-white/10 hover:bg-white/20 text-white/90 text-xs font-semibold flex items-center gap-1.5 transition-all active:scale-[0.98] cursor-pointer"
                  >
                    <ImageIcon className="w-3.5 h-3.5 text-blue-400" />
                    <span>Chọn từ thư viện</span>
                  </button>
                )}
              </div>
            </div>
          ) : capturedImage ? (
            // Review Captured Photo
            <div className="relative w-full h-full flex items-center justify-center bg-black">
              <img
                src={capturedImage}
                alt="Ảnh chụp từ camera"
                className="w-full h-full object-contain"
              />
              <div className="absolute top-4 left-4 px-3 py-1.5 rounded-full bg-black/60 backdrop-blur-md border border-white/20 text-[11px] font-medium text-emerald-400 flex items-center gap-1.5 shadow-lg">
                <Check className="w-3.5 h-3.5" />
                <span>Ảnh nét cao sẵn sàng chẩn đoán</span>
              </div>
            </div>
          ) : (
            // Live Video Stream Viewfinder
            <div className="relative w-full h-full flex items-center justify-center">
              <video
                ref={videoRef}
                autoPlay
                playsInline
                muted
                onLoadedMetadata={handleLoadedMetadata}
                className={'w-full h-full object-cover ' + (facingMode === 'user' ? 'scale-x-[-1]' : '')}
              />

              {/* Viewfinder Reticle & HUD Overlays */}
              <div className="pointer-events-none absolute inset-0 flex flex-col items-center justify-between p-6 z-20">
                {/* Top Hint */}
                <div className="px-3.5 py-1.5 rounded-full bg-black/60 backdrop-blur-md border border-white/15 text-xs text-emerald-300 font-medium flex items-center gap-2 shadow-lg">
                  <Scan className="w-3.5 h-3.5 text-emerald-400 animate-pulse" />
                  <span>Căn vết bệnh hoặc phiến lá vào khung ngắm</span>
                </div>

                {/* Center Laser Target Box */}
                <div className="relative w-64 h-64 sm:w-72 sm:h-72 border-2 border-emerald-500/40 rounded-3xl flex items-center justify-center">
                  {/* Corner Brackets */}
                  <div className="absolute -top-1 -left-1 w-6 h-6 border-t-4 border-l-4 border-emerald-400 rounded-tl-xl" />
                  <div className="absolute -top-1 -right-1 w-6 h-6 border-t-4 border-r-4 border-emerald-400 rounded-tr-xl" />
                  <div className="absolute -bottom-1 -left-1 w-6 h-6 border-b-4 border-l-4 border-emerald-400 rounded-bl-xl" />
                  <div className="absolute -bottom-1 -right-1 w-6 h-6 border-b-4 border-r-4 border-emerald-400 rounded-br-xl" />

                  {/* Center Crosshair Dot */}
                  <div className="w-3 h-3 rounded-full bg-emerald-400/80 animate-ping" />
                  <div className="w-2 h-2 rounded-full bg-emerald-400 absolute" />

                  {/* Subtle Grid Lines */}
                  <div className="absolute inset-0 grid grid-cols-3 grid-rows-3 opacity-20 pointer-events-none">
                    <div className="border-r border-b border-emerald-300" />
                    <div className="border-r border-b border-emerald-300" />
                    <div className="border-b border-emerald-300" />
                    <div className="border-r border-b border-emerald-300" />
                    <div className="border-r border-b border-emerald-300" />
                    <div className="border-b border-emerald-300" />
                    <div className="border-r border-emerald-300" />
                    <div className="border-r border-emerald-300" />
                    <div />
                  </div>
                </div>

                {/* Bottom Technical Pill */}
                <div className="text-[11px] text-white/70 bg-black/60 backdrop-blur-md px-3 py-1 rounded-full border border-white/10">
                  {isInitializing
                    ? 'Đang tối ưu độ sắc nét vi thể...'
                    : 'Tự động lấy nét vi mô • Chuẩn đoán tổn thương mô lá'}
                </div>
              </div>
            </div>
          )}
        </div>

        {/* Bottom Control Actions Bar */}
        <div className="px-6 py-4 bg-[#1a1a1a]/95 border-t border-white/10 z-10 shrink-0">
          {capturedImage ? (
            // Actions for Captured Photo Review
            <div className="flex items-center justify-between gap-4 max-w-md mx-auto">
              <button
                type="button"
                onClick={handleRetake}
                className="flex-1 py-3 px-4 rounded-2xl bg-white/10 hover:bg-white/15 text-white font-medium text-sm flex items-center justify-center gap-2 transition-all hover:scale-[1.02] active:scale-[0.98] cursor-pointer"
              >
                <RotateCcw className="w-4 h-4" />
                <span>Chụp lại</span>
              </button>
              <button
                type="button"
                onClick={handleConfirmPhoto}
                className="flex-1 py-3 px-4 rounded-2xl bg-emerald-600 hover:bg-emerald-500 text-white font-semibold text-sm flex items-center justify-center gap-2 shadow-lg shadow-emerald-600/30 transition-all hover:scale-[1.02] active:scale-[0.98] cursor-pointer"
              >
                <Check className="w-4 h-4 stroke-[2.5]" />
                <span>Sử dụng ảnh này</span>
              </button>
            </div>
          ) : error ? (
            // Actions when in error/permission state
            <div className="flex items-center justify-center max-w-md mx-auto">
              <button
                type="button"
                onClick={handleOpenNativeCamera}
                className="w-full py-3 px-4 rounded-2xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-sm flex items-center justify-center gap-2 shadow-lg shadow-emerald-600/30 transition-all active:scale-[0.98] cursor-pointer"
              >
                <Camera className="w-4 h-4 stroke-[2.5]" />
                <span>Chụp ngay bằng máy ảnh thiết bị (Native Camera)</span>
              </button>
            </div>
          ) : (
            // Actions for Live Stream Capture
            <div className="flex items-center justify-between max-w-md mx-auto">
              {/* Left: Switch to File Picker */}
              <div className="w-16 flex justify-start">
                {onSwitchToUpload && (
                  <button
                    type="button"
                    onClick={() => {
                      handleClose();
                      onSwitchToUpload();
                    }}
                    title="Chọn từ thư viện"
                    className="p-3 rounded-2xl bg-white/5 hover:bg-white/10 text-white/80 hover:text-white transition-all hover:scale-105 active:scale-95 cursor-pointer flex flex-col items-center gap-1"
                  >
                    <ImageIcon className="w-5 h-5" />
                    <span className="text-[9px] font-medium text-white/60">Thư viện</span>
                  </button>
                )}
              </div>

              {/* Center: Large Shutter Button */}
              <div className="flex flex-col items-center gap-1.5">
                <button
                  type="button"
                  onClick={handleCapture}
                  disabled={isInitializing || !!error}
                  title="Chụp ảnh ngay"
                  className="relative w-18 h-18 sm:w-20 sm:h-20 rounded-full border-4 border-white/80 p-1 flex items-center justify-center transition-all hover:scale-105 active:scale-95 cursor-pointer disabled:opacity-50 disabled:cursor-not-allowed group shadow-2xl"
                >
                  <div className="w-full h-full rounded-full bg-white group-hover:bg-emerald-400 group-active:scale-90 transition-all shadow-inner" />
                </button>
                <span className="text-[11px] font-semibold text-white/80 tracking-wide uppercase">
                  Chụp ảnh HD
                </span>
              </div>

              {/* Right: Switch Camera (Rear / Front) */}
              <div className="w-16 flex justify-end">
                <button
                  type="button"
                  onClick={handleSwitchCamera}
                  disabled={isInitializing || !!error}
                  title="Lật camera trước / sau"
                  className="p-3 rounded-2xl bg-white/5 hover:bg-white/10 text-white/80 hover:text-white transition-all hover:scale-105 active:scale-95 cursor-pointer flex flex-col items-center gap-1 disabled:opacity-40"
                >
                  <RefreshCw className="w-5 h-5" />
                  <span className="text-[9px] font-medium text-white/60">Đảo cam</span>
                </button>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>,
    document.body
  );
}
