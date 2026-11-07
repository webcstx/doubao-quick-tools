// X浏览器风格 - 暴力广告拦截
// 不管误杀，全杀就完了

let n = 0;

// 所有弹窗全部关
function kill() {
  // 所有 popup/modal/dialog 全删
  document.querySelectorAll('[class*="popup"],[id*="popup"],[class*="modal"],[id*="modal"],[class*="dialog"],[id*="dialog"],[class*="overlay"],[id*="overlay"]').forEach(e => {
    e.remove(); n++;
  });
  
  // 所有带 ad 的全删
  document.querySelectorAll('[class*="ad"],[id*="ad"],[class*="banner"],[id*="banner"]').forEach(e => {
    if (e.offsetWidth > 20) { e.remove(); n++; }
  });
  
  // 所有 iframe 带广告域名的全删
  document.querySelectorAll('iframe').forEach(f => {
    const s = f.src || '';
    if (s.includes('ad') || s.includes('doubleclick') || s.includes('google')) {
      f.remove(); n++;
    }
  });
  
  // 自动点所有关闭按钮
  document.querySelectorAll('.close,.close-btn,[aria-label="关闭"],[aria-label="Close"]').forEach(b => {
    b.click(); n++;
  });
}

// CSS注入 - 全部隐藏
const css = `
[class*="popup"],[id*="popup"],[class*="modal"],[id*="modal"],
[class*="dialog"],[id*="dialog"],[class*="overlay"],[id*="overlay"],
[class*="ad"],[id*="ad"],[class*="banner"],[id*="banner"],
iframe[src*="ad"],iframe[src*="doubleclick"]
{ display: none !important; }
`;
const s = document.createElement('style');
s.textContent = css;
(document.head || document.documentElement).appendChild(s);

// 疯狂循环杀
kill();
setInterval(kill, 100); // 每100毫秒杀一次

// DOM监听
new MutationObserver(() => kill()).observe(document.documentElement, { childList: true, subtree: true });

setInterval(() => chrome.storage.local.set({ blocked: n }), 1000);
