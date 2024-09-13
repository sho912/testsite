window.addEventListener('load', function() {
    const image = document.querySelector('.phrase-back');
    const imageHeight = image.offsetHeight;
    const scrollY = image.offsetTop + (imageHeight / 2) - (window.innerHeight / 2);
    window.scrollTo(0, scrollY);
  });
  
