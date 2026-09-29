document.addEventListener('DOMContentLoaded', function () {
    // Mobile nav toggle
    var hamburger = document.getElementById('hamburger');
    var navMenu = document.getElementById('navMenu');
    if (hamburger && navMenu) {
        hamburger.addEventListener('click', function () {
            navMenu.classList.toggle('open');
        });
        navMenu.querySelectorAll('a').forEach(function (link) {
            link.addEventListener('click', function () {
                navMenu.classList.remove('open');
            });
        });
    }

    // Review carousel
    var track = document.getElementById('reviewTrack');
    var prevBtn = document.querySelector('.nav-btn.prev');
    var nextBtn = document.querySelector('.nav-btn.next');
    if (track && prevBtn && nextBtn) {
        var index = 0;
        var slides = track.children.length;
        var goTo = function (i) {
            index = (i + slides) % slides;
            track.style.transform = 'translateX(-' + (index * 100) + '%)';
        };
        track.style.display = 'flex';
        track.style.transition = 'transform 0.4s ease-in-out';
        prevBtn.addEventListener('click', function () { goTo(index - 1); });
        nextBtn.addEventListener('click', function () { goTo(index + 1); });
    }

    // Order modal
    var modal = document.getElementById('orderModal');
    var modalProductName = document.getElementById('modalProductName');
    document.querySelectorAll('.product-btn').forEach(function (btn) {
        btn.addEventListener('click', function () {
            if (modalProductName) {
                modalProductName.textContent = btn.getAttribute('data-product') || 'Product';
            }
            if (modal) {
                modal.classList.add('open');
            }
        });
    });
    document.querySelectorAll('[data-close-modal]').forEach(function (el) {
        el.addEventListener('click', function () {
            if (modal) {
                modal.classList.remove('open');
            }
        });
    });
});
