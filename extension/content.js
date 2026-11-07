// 极速广告拦截器 - 仿X浏览器强力版
// 所有疑似广告全部杀，不管误杀

let killCount = 0;

// 第一组：广告域名 iframe - 直接删
const KILL_IFRAMES = [
  '*://*.doubleclick.net/*', '*://*.googlesyndication.com/*',
  '*://*.googleadservices.com/*', '*://*.adnxs.com/*',
  '*://*.taboola.com/*', '*://*.outbrain.com/*',
  '*://*.popads.net/*', '*://*.adroll.com/*',
  '*://*.propellerads.com/*', '*://*.amazon-adsystem.com/*'
];

// 第二组：强力选择器 - 全部隐藏
const KILL_CSS = `
  /* 弹窗类 */
  [class*="popup"], [id*="popup"],
  [class*="modal"], [id*="modal"],
  [class*="dialog"], [id*="dialog"],
  [class*="overlay"], [id*="overlay"],
  
  /* 广告类 */
  [class*="ad-banner"], [class*="ad-container"], [class*="ad-box"],
  [class*="advertisement"], [class*="adsbox"], [class*="ad-wrapper"],
  [class*="ad-fixed"], [class*="ad-float"], [class*="ad-sticky"],
  [id*="google_ads"], [id*="adsense"], [id*="banner-ad"],
  
  /* 悬浮类 */
  [class*="float-ad"], [class*="fixed-ad"], [class*="sticky-ad"],
  [class*="floating-ad"], [class*="side-ad"], [class*="right-ad"],
  
  /* 推广类 */
  [class*="sponsored"], [class*="promoted"], [class*="commercial"],
  [class*="in-feed-ad"], [class*="native-ad"], [class*="preroll"],
  
  /* iframe 广告 */
  iframe[src*="doubleclick"], iframe[src*="googlesyndication"],
  iframe[src*="ads"], iframe[id*="google_ads"]
`;

// 注入强力CSS
function injectKillCSS() {
  const style = document.createElement('style');
  style.textContent = KILL_CSS + ' { display: none !important; }';
  (document.head || document.documentElement).appendChild(style);
}

// 自动点关闭按钮
function autoClose() {
  document.querySelectorAll('.close, .close-btn, .btn-close, [aria-label="关闭"], [aria-label="Close"]').forEach(btn => {
    const parent = btn.parentElement;
    if (parent && (parent.className.toLowerCase().includes('ad') || 
                   parent.className.toLowerCase().includes('popup') ||
                   parent.className.toLowerCase().includes('modal'))) {
      btn.click();
      killCount++;
    }
  });
}

// 启动
injectKillCSS();

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => { autoClose(); });
} else {
  autoClose();
}

// 疯狂监听
const observer = new MutationObserver(() => { autoClose(); });
if (document.body) {
  observer.observe(document.body, { childList: true, subtree: true });
}

setTimeout(() => chrome.storage.local.set({ blocked: killCount }), 1000);
