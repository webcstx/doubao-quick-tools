// 极速广告拦截器 - 持续强力版
// 不停杀，广告什么时候出来什么时候杀

let killCount = 0;

// 所有要杀的选择器
const KILL_SELECTORS = [
  '[class*="popup"]', '[id*="popup"]',
  '[class*="modal"]', '[id*="modal"]',
  '[class*="dialog"]', '[id*="dialog"]',
  '[class*="overlay"]', '[id*="overlay"]',
  '[class*="ad-banner"]', '[class*="ad-container"]', '[class*="ad-box"]',
  '[class*="advertisement"]', '[class*="adsbox"]', '[class*="ad-wrapper"]',
  '[class*="float-ad"]', '[class*="fixed-ad"]', '[class*="sticky-ad"]',
  '[class*="sponsored"]', '[class*="promoted"]',
  'iframe[src*="ads"]', 'iframe[id*="google_ads"]',
  '[class*="in-feed-ad"]', '[class*="preroll"]'
];

// 杀一次
function killOnce() {
  KILL_SELECTORS.forEach(sel => {
    document.querySelectorAll(sel).forEach(el => {
      if (el.style.display !== 'none' && el.offsetWidth > 20) {
        el.style.setProperty('display', 'none', 'important');
        killCount++;
      }
    });
  });
}

// 第一时间注入CSS - 永久生效
const css = KILL_SELECTORS.join(',') + ' { display: none !important; }';
const style = document.createElement('style');
style.textContent = css;
(document.head || document.documentElement).appendChild(style);

// 启动就杀
killOnce();

// 定时器 - 每500毫秒杀一次，持续杀
setInterval(killOnce, 500);

// MutationObserver - DOM一变就杀
const observer = new MutationObserver(() => killOnce());
if (document.body) {
  observer.observe(document.body, { childList: true, subtree: true });
} else {
  // body还没出来就等一下
  const checkBody = setInterval(() => {
    if (document.body) {
      observer.observe(document.body, { childList: true, subtree: true });
      clearInterval(checkBody);
    }
  }, 100);
}

// 上报
setInterval(() => chrome.storage.local.set({ blocked: killCount }), 2000);
