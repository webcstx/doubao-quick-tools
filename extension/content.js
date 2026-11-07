// 极速广告拦截器 v3.0.1
// 元素层补充拦截（网络层由 rules.json 负责）

let blockedCount = 0;

// 只隐藏明确带广告标识的元素，避免误杀正常弹窗
const AD_SELECTORS = [
  '[class*="ad-banner"]', '[class*="ad-container"]', '[class*="ad-box"]',
  '[class*="advertisement"]', '[class*="adsbox"]', '[class*="ad-wrapper"]',
  '[id*="google_ads"]', '[id*="adsense"]',
  'iframe[src*="doubleclick"]', 'iframe[src*="googlesyndication"]',
  '[class*="sponsored"]', '[class*="promoted-content"]'
];

function removeAds() {
  document.querySelectorAll(AD_SELECTORS.join(',')).forEach(el => {
    if (el.offsetWidth > 50 && el.offsetHeight > 30) {
      el.style.display = 'none';
      blockedCount++;
    }
  });
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', removeAds);
} else {
  removeAds();
}

// 动态监听
const observer = new MutationObserver(() => removeAds());
if (document.body) {
  observer.observe(document.body, { childList: true, subtree: true });
}

setTimeout(() => chrome.storage.local.set({ blocked: blockedCount }), 1000);
