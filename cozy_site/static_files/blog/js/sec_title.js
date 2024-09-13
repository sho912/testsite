window.addEventListener('DOMContentLoaded', () => {
    const secTitles = document.querySelectorAll('.sec_title');
    console.log(secTitles); // 要素が取得できているか確認
    
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          console.log(`${entry.target.tagName} is in view`);
          entry.target.classList.add('inview');
        } else {
          console.log(`${entry.target.tagName} is out of view`);
          entry.target.classList.remove('inview');
        }
      });
    });
  
    secTitles.forEach(secTitle => {
      observer.observe(secTitle);
      console.log(`Observing ${secTitle.tagName}`);
    });
  });
  