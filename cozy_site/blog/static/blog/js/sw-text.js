window.addEventListener('scroll', function() {
    const renovateRight = document.querySelector('.renovate-wrapper .right');
    const inspectionRight = document.querySelector('.inspection-wrapper .right');
    const stockRight = document.querySelector('.stock-wrapper .right');
    const rect1 = renovateRight.getBoundingClientRect();
    const rect2 = inspectionRight.getBoundingClientRect();
    const rect3 = stockRight.getBoundingClientRect();
    const windowHeight = window.innerHeight || document.documentElement.clientHeight;
  
    if (rect1.top < windowHeight * 0.8) {
      renovateRight.classList.add('animate');
    }
    if (rect2.top < windowHeight * 0.8) {
      inspectionRight.classList.add('animate');
    }
    if (rect3.top < windowHeight * 0.8) {
      stockRight.classList.add('animate');
    }
  });
  