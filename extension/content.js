// 极速广告拦截器 - 强力模式
// 所有疑似广告全部强制隐藏

let blockedCount = 0;

const KILL_SELECTORS = [
  // 弹窗/模态框/对话框 - 全部杀
  '[class*="popup"]', '[class*="modal"]', '[class*="dialog"]', '[class*="overlay"]',
  '[id*="popup"]', '[id*="modal"]', '[id*="dialog"]',
  // 悬浮/固定/横幅广告 - 全部杀
  '[class*="float"]', '[class*="fixed"]', '[class*="banner"]',
  '[class*="sticky"]', '[class*="floating"]',
  // 广告类容器 - 全部杀
  '[class*="ad-"]', '[class*="-ad"]', '[class*="ads"]', '[id*="ads"]',
  '[class*="sponsor"]', '[class*="promo"]', '[class*="commercial"]',
  // iframe 广告 - 全部杀
  'iframe[src*="ad"]', 'iframe[id*="ad"]', 'iframe[class*="ad"]',
  // 视频广告 - 全部杀
  '[class*="video-ad"]', '[id*="preroll"]', '[class*="pre-roll"]',
  // 插入式广告 - 全部杀
  '[class*="in-feed"]', '[class*="in-feed-ad"]', '[class*="native-ad"]',
  // 关闭按钮 - 自动点
  '.close', '.close-btn', '.btn-close', '[aria-label="关闭"]', '[aria-label="Close"]'
];

function killAds() {
  document.querySelectorAll(KILL_SELECTORS.join(',')).forEach(el => {
    if (el.offsetWidth > 20 && el.offsetHeight > 20) {
      el.style.setProperty('display', 'none', 'important');
      blockedCount++;
    }
  });
}

// 页面加载就杀
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', killAds);
} else {
  killAds();
}

// 疯狂监听，新加载的也杀
const observer = new MutationObserver(() => killAds());
if (document.body) {
  observer.observe(document.body, { childList: true, subtree: true });
}

setTimeout(() => chrome.storage.local.set({ blocked: blockedCount }), 1000);
