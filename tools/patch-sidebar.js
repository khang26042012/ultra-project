const fs = require('fs');
let content = fs.readFileSync('src/components/sidebar/AppSidebar.tsx', 'utf8');

// 1. Add Settings, HelpCircle to lucide-react import
content = content.replace(/LogIn,?\s*}/, 'LogIn,\n  Settings,\n  HelpCircle,\n}');

// 2. Add setIsSettingsOpen, setIsHelpOpen to useChat()
content = content.replace('setIsAuthModalOpen,', 'setIsAuthModalOpen,\n    setIsSettingsOpen,\n    setIsHelpOpen,');

// 3. Add Quick Action buttons above Footer Profile
const footerTarget = '{/* Footer Profile / Auth Bar */}';
const quickActions = `{/* Quick Actions: Help & Settings */}
          <div className="px-2.5 py-1.5 space-y-0.5 border-t border-[#e5e5e5] dark:border-[#262626]">
            <button
              type="button"
              onClick={() => {
                setIsHelpOpen(true);
                if (window.innerWidth < 768) setIsSidebarOpen(false);
              }}
              className="w-full flex items-center gap-2.5 px-2.5 py-2 rounded-xl hover:bg-[#eaeaea] dark:hover:bg-[#212121] text-xs font-medium text-[#5d5d5d] dark:text-[#b4b4b4] hover:text-[#0d0d0d] dark:hover:text-white transition-colors cursor-pointer"
            >
              <HelpCircle className="w-4 h-4 shrink-0" strokeWidth={1.75} />
              <span>Trợ giúp & Hướng dẫn</span>
            </button>
            <button
              type="button"
              onClick={() => {
                setIsSettingsOpen(true);
                if (window.innerWidth < 768) setIsSidebarOpen(false);
              }}
              className="w-full flex items-center gap-2.5 px-2.5 py-2 rounded-xl hover:bg-[#eaeaea] dark:hover:bg-[#212121] text-xs font-medium text-[#5d5d5d] dark:text-[#b4b4b4] hover:text-[#0d0d0d] dark:hover:text-white transition-colors cursor-pointer"
            >
              <Settings className="w-4 h-4 shrink-0" strokeWidth={1.75} />
              <span>Cài đặt hệ thống</span>
            </button>
          </div>

          `;

if (!content.includes('Cài đặt hệ thống')) {
  content = content.replace(footerTarget, quickActions + footerTarget);
}

fs.writeFileSync('src/components/sidebar/AppSidebar.tsx', content, 'utf8');
console.log('Successfully updated AppSidebar.tsx');
