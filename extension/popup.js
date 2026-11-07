const cat = document.getElementById('cat');
const bubble = document.getElementById('bubble');
const meows = ['喵～', '摸摸头～', '好可爱呀', '喵呜～', '贴贴～', '蹭蹭～', '要抱抱～'];
const faces = ['🐱', '😺', '😸', '😻', '🙀', '😿'];
let count = 0;

cat.addEventListener('click', () => {
  count++;
  cat.textContent = faces[Math.floor(Math.random() * faces.length)];
  bubble.textContent = meows[Math.floor(Math.random() * meows.length)];
  if (count % 5 === 0) {
    cat.classList.add('spin');
    bubble.textContent = '转圈圈～🥰';
    setTimeout(() => cat.classList.remove('spin'), 500);
  }
});
