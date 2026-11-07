// 极速广告拦截器
const AD_SELECTORS = [
  '[class*="popup"]', '[class*="modal"]', '[class*="dialog"]',
  '[id*="popup"]', '[id*="modal"]',
  '[class*="float-ad"]', '[class*="fixed-ad"]', '[class*="banner"]',
  '[class*="advertisement"]', '[class*="ad-container"]',
  'iframe[src*="ads"]', 'iframe[id*="google_ads"]'
];

let blockedCount = 0;

function removeAds() {
  document.querySelectorAll(AD_SELECTORS.join(',')).forEach(el => {
    if (el.offsetWidth > 50 && el.offsetHeight > 30) {
      el.style.display = 'none';
      blockedCount++;
    }
  });
  document.querySelectorAll('.close, .close-btn, [aria-label="Close"]').forEach(btn => {
    const p = btn.parentElement;
    if (p && (p.className.toLowerCase().includes('ad') || p.className.toLowerCase().includes('popup'))) {
      btn.click();
      blockedCount++;
    }
  });
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', removeAds);
} else {
  removeAds();
}

const observer = new MutationObserver(() => removeAds());
observer.observe(document.body, { childList: true, subtree: true });

setTimeout(() => chrome.storage.local.set({ blocked: blockedCount }), 1000);
