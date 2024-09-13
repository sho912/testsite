// フェードインアニメーションの完了を待つ
setTimeout(function() {
  const infoContainer = document.querySelector('.info-container');
  
  // 0.5秒待機してから非表示に  
  setTimeout(function() {
    infoContainer.style.display = 'none';
    
    // company-containerを表示
    const companyContainer = document.querySelector('.company-container');
    companyContainer.style.display = 'flex';
  }, 1000);
}, 3000);