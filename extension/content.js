// 极速广告拦截器 Pro v3.0
const AD_SELECTORS = [
  // 弹窗类
  '[class*="popup"]', '[class*="modal"]', '[class*="dialog"]', '[class*="overlay"]',
  '[id*="popup"]', '[id*="modal"]', '[id*="dialog"]',
  // 悬浮类
  '[class*="float-ad"]', '[class*="fixed-ad"]', '[class*="banner-ad"]',
  '[class*="ad-popup"]', '[class*="ad-fixed"]', '[class*="sticky-ad"]',
  // 横幅类
  '[class*="advertisement"]', '[class*="adsbox"]', '[class*="ad-container"]',
  '[class*="banner"]', '[class*="header-ad"]', '[class*="footer-ad"]',
  // iframe 广告
  'iframe[src*="ads"]', 'iframe[id*="google_ads"]', 'iframe[class*="ad"]',
  // 视频广告
  '[class*="video-ad"]', '[id*="preroll"]',
  // 插入式广告
  '[class*="in-feed"]', '[class*="promoted"]', '[class*="sponsored"]'
];

let blockedCount = 0;

function isAdLike(el) {
  const cls = (el.className || '').toString().toLowerCase();
  const id = (el.id || '').toLowerCase();
  return cls.includes('ad') || cls.includes('popup') || cls.includes('banner') || 
         cls.includes('sponsor') || id.includes('ad') || id.includes('popup');
}

function removeAds() {
  // 移除广告元素
  document.querySelectorAll(AD_SELECTORS.join(',')).forEach(el => {
    if (el.offsetWidth > 50 && el.offsetHeight > 30) {
      el.style.display = 'none';
      blockedCount++;
    }
  });

  // 自动点击关闭按钮
  document.querySelectorAll('.close, .close-btn, .btn-close, [aria-label="关闭"], [aria-label="Close"]').forEach(btn => {
    let parent = btn.parentElement;
    for (let i = 0; i < 3 && parent; i++) {
      if (isAdLike(parent)) {
        btn.click();
        blockedCount++;
        break;
      }
      parent = parent.parentElement;
    }
  });
}

// 页面加载后运行
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', removeAds);
} else {
  removeAds();
}

// 动态监听
const observer = new MutationObserver(() => removeAds());
observer.observe(document.body, { childList: true, subtree: true });

// 上报
setTimeout(() => chrome.storage.local.set({ blocked: blockedCount, version: '3.0.0' }), 1000);
