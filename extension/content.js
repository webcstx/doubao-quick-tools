// 极速广告拦截器 - 参考 GKD 规则思路
// 分类精准拦截，不误杀

let killCount = 0;

// ========== 规则组 1: 开屏/弹窗广告 ==========
const POPUP_AD_RULES = [
  // 带"跳过"按钮的开屏广告
  { match: '[class*="splash"], [id*="splash"]', closeBtn: '[class*="skip"], [id*="skip"], [text*="跳过"]' },
  // 带广告标识的弹窗
  { match: '[class*="ad-popup"], [id*="ad-popup"], [class*="ad-modal"], [id*="ad-modal"]', closeBtn: '.close, .close-btn' },
  // 全屏遮罩广告
  { match: '[class*="ad-overlay"], [id*="ad-overlay"], [class*="fullscreen-ad"]', closeBtn: '.close, [aria-label="Close"]' }
];

// ========== 规则组 2: 局部广告 ==========
const LOCAL_AD_RULES = [
  'div[id^="google_ads_"]',
  'div[id^="div-gpt-ad"]',
  'ins.adsbygoogle',
  '.adsbox', '.ad-container', '.ad-banner',
  '.advertisement', '.advertise-area',
  '.sponsored-content', '.promoted-post', '.native-ad'
];

// ========== 规则组 3: 悬浮广告 ==========
const FLOAT_AD_RULES = [
  '.float-ad', '.fixed-ad', '.sticky-ad',
  '.side-ad', '.right-ad', '.left-ad',
  '.bottom-ad', '.top-ad'
];

// 注入CSS - 局部广告和悬浮广告直接隐藏
const css = [...LOCAL_AD_RULES, ...FLOAT_AD_RULES].join(',') + ' { display: none !important; }';
const style = document.createElement('style');
style.textContent = css;
(document.head || document.documentElement).appendChild(style);

// 检查弹窗广告 - 自动点关闭
function checkPopups() {
  POPUP_AD_RULES.forEach(rule => {
    document.querySelectorAll(rule.match).forEach(popup => {
      if (popup.style.display === 'none') return;
      
      // 找关闭按钮
      const closeBtn = popup.querySelector(rule.closeBtn);
      if (closeBtn) {
        closeBtn.click();
        killCount++;
      } else {
        popup.remove();
        killCount++;
      }
    });
  });
}

// 检查局部广告
function checkLocalAds() {
  LOCAL_AD_RULES.forEach(sel => {
    document.querySelectorAll(sel).forEach(el => {
      if (el.style.display !== 'none') {
        el.style.display = 'none';
        killCount++;
      }
    });
  });
}

// 启动
checkPopups();
checkLocalAds();

// 持续检查
setInterval(() => {
  checkPopups();
  checkLocalAds();
}, 500);

// DOM监听
new MutationObserver(() => {
  checkPopups();
  checkLocalAds();
}).observe(document.documentElement, { childList: true, subtree: true });

setInterval(() => chrome.storage.local.set({ blocked: killCount }), 1000);
