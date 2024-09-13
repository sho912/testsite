var swiper = new Swiper('.swiper', {
  loop: true,
  slidesPerView: 3,
  spaceBetween: 10,
  centeredSlides: true,
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
    renderBullet: function (index, className) {
      return '<span class="' + className + '">' + (index + 1) + '</span>';
    }
  }
});

