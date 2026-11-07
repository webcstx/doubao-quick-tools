// 极速广告拦截器 - 参考 AdGuard/EasyList 规则
// 精准拦截，不误杀正常弹窗

let killCount = 0;

// 参考 AdGuard Base Filter 的常见广告选择器（不是瞎写的宽泛规则）
const AD_SELECTORS = [
  // 标准广告容器
  'div[id^="google_ads_"]',
  'div[id^="div-gpt-ad"]',
  'ins.adsbygoogle',
  '.adsbox', '.ad-container', '.ad-banner', '.ad-wrapper',
  '.advertisement', '.advertise-area',
  // 原生推广
  '.sponsored-content', '.promoted-post', '.native-ad',
  // 弹窗广告（只关明确带广告标识的）
  '.ad-popup', '.ad-modal', '.ad-overlay',
  // 悬浮广告
  '.float-ad', '.fixed-ad', '.sticky-ad', '.side-ad'
];

// 注入CSS - 精准隐藏
const css = AD_SELECTORS.join(',') + ' { display: none !important; }';
const style = document.createElement('style');
style.textContent = css;
(document.head || document.documentElement).appendChild(style);

// 持续检查
function check() {
  AD_SELECTORS.forEach(sel => {
    document.querySelectorAll(sel).forEach(el => {
      if (el.style.display !== 'none') {
        el.style.display = 'none';
        killCount++;
      }
    });
  });
}

check();
setInterval(check, 500);

// DOM监听
new MutationObserver(() => check()).observe(document.documentElement, { childList: true, subtree: true });

setInterval(() => chrome.storage.local.set({ blocked: killCount }), 1000);
