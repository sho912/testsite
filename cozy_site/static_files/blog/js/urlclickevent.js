document.addEventListener('DOMContentLoaded', function() {
    const linkConfirms = document.querySelectorAll('.link_confirm');
    if (linkConfirms.length > 0) {
      linkConfirms.forEach(function(linkConfirm) {
        linkConfirm.addEventListener('click', function(event) {
          const resultConfirm = confirm('LIXILのサイトに移動します。よろしいですか？');
          if (!resultConfirm) {
            event.preventDefault();
          }
        });
      });
    }
  });
  