chrome.storage.local.get('blocked', (data) => {
  document.getElementById('count').textContent = data.blocked || 0;
});

function refresh() {
  chrome.tabs.reload();
  window.close();
}
