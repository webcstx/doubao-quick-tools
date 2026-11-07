// 极速广告拦截器 - 智能关弹窗版
// 只关广告弹窗，正常弹窗（登录/设置）不动

let closedCount = 0;

// 判断是不是广告弹窗
function isAdPopup(el) {
  const text = (el.innerText || '').toLowerCase();
  const cls = (el.className || '').toString().toLowerCase();
  const id = (el.id || '').toLowerCase();
  
  // 带广告标识的肯定是
  if (cls.includes('ad') || id.includes('ad')) return true;
  if (text.includes('advertisement') || text.includes('广告')) return true;
  if (text.includes(' sponsored ') || text.includes('推广')) return true;
  
  // 突然弹出的全屏遮罩，大概率是广告
  if (cls.includes('overlay') && el.offsetWidth > window.innerWidth * 0.8) return true;
  
  return false;
}

// 找关闭按钮
function findCloseBtn(popup) {
  const selectors = [
    '.close', '.close-btn', '.btn-close',
    '[aria-label="关闭"]', '[aria-label="Close"]',
    '.modal-close', '.popup-close',
    'button[class*="close"]', 'span[class*="close"]'
  ];
  for (const sel of selectors) {
    const btn = popup.querySelector(sel);
    if (btn) return btn;
  }
  return null;
}

// 检查所有弹窗
function checkPopups() {
  const popups = document.querySelectorAll(
    '[class*="popup"], [class*="modal"], [class*="dialog"], [class*="overlay"]'
  );
  
  popups.forEach(popup => {
    if (popup.style.display === 'none') return;
    
    if (isAdPopup(popup)) {
      const closeBtn = findCloseBtn(popup);
      if (closeBtn) {
        closeBtn.click(); // 自动点关闭
        closedCount++;
      } else {
        popup.remove(); // 找不到按钮就直接删
        closedCount++;
      }
    }
  });
}

// 启动就检查
checkPopups();

// 每300ms检查一次 - 新弹窗出来马上关
setInterval(checkPopups, 300);

// MutationObserver - 页面一变就检查
const observer = new MutationObserver(() => checkPopups());
const start = () => {
  if (document.body) observer.observe(document.body, { childList: true, subtree: true });
  else requestAnimationFrame(start);
};
start();

// 上报
setInterval(() => chrome.storage.local.set({ blocked: closedCount }), 1000);
