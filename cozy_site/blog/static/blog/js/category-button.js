document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.category-btn').forEach(btn => {
    btn.addEventListener('click', function() {
      // 全てのボタンと表示エリアからactiveクラスを削除
      document.querySelectorAll('.category-btn, .category-content > div').forEach(el => {
        el.classList.remove('active');
      });

      // クリックされたボタンと、対応する表示エリアにactiveクラスを追加
      this.classList.add('active');
      document.getElementById(this.dataset.category).classList.add('active');
    });
  });
});
