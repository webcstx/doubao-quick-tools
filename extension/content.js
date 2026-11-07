// 极速广告拦截器 - 暴力删除版
// 不是隐藏，是直接从DOM删掉

let killCount = 0;

// 暴力选择器大全
const KILL = [
  // 弹窗类
  '[class*="popup"]', '[id*="popup"]',
  '[class*="modal"]', '[id*="modal"]',
  '[class*="dialog"]', '[id*="dialog"]',
  '[class*="overlay"]', '[id*="overlay"]',
  '[class*="lightbox"]', '[id*="lightbox"]',
  
  // 广告类
  '[class*="ad-banner"]', '[class*="ad-container"]', '[class*="ad-box"]',
  '[class*="advertisement"]', '[class*="adsbox"]', '[class*="ad-wrapper"]',
  '[class*="ad-fixed"]', '[class*="ad-float"]', '[class*="ad-sticky"]',
  '[id*="google_ads"]', '[id*="adsense"]', '[id*="banner-ad"]',
  '[class*="ads-"]', '[class*="-ads"]', '[id*="ads-"]',
  
  // 悬浮类
  '[class*="float-ad"]', '[class*="fixed-ad"]', '[class*="sticky-ad"]',
  '[class*="floating"]', '[class*="side-ad"]', '[class*="right-ad"]',
  '[class*="left-ad"]', '[class*="bottom-ad"]', '[class*="top-ad"]',
  
  // 推广类
  '[class*="sponsored"]', '[class*="promoted"]', '[class*="commercial"]',
  '[class*="in-feed-ad"]', '[class*="native-ad"]', '[class*="preroll"]',
  '[class*="promo"]', '[class*="marketing"]',
  
  // iframe
  'iframe[src*="ad"]', 'iframe[id*="ad"]', 'iframe[class*="ad"]',
  'iframe[src*="doubleclick"]', 'iframe[src*="googlesyndication"]'
];

// 暴力删除函数
function kill() {
  KILL.forEach(sel => {
    document.querySelectorAll(sel).forEach(el => {
      if (el.parentNode && el.offsetWidth > 10) {
        el.remove(); // 直接删，不是隐藏
        killCount++;
      }
    });
  });
}

// 注入CSS双保险
const css = KILL.join(',') + ' { display: none !important; visibility: hidden !important; }';
const style = document.createElement('style');
style.textContent = css;
(document.head || document.documentElement).appendChild(style);

// 启动就杀
kill();

// 每200毫秒杀一次 - 更频繁
setInterval(kill, 200);

// MutationObserver - DOM一变就杀
const observer = new MutationObserver(() => kill());
const startObserve = () => {
  if (document.body) {
    observer.observe(document.body, { childList: true, subtree: true });
  } else {
    requestAnimationFrame(startObserve);
  }
};
startObserve();

// 上报
setInterval(() => chrome.storage.local.set({ blocked: killCount }), 1000);
