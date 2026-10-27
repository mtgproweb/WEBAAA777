// Credisnet v6 — JS mínimo: menú móvil, FAQ acordeón, flechas de tiras. Sin frameworks.
document.addEventListener('DOMContentLoaded', function () {
  var toggle = document.getElementById('nav-toggle') || document.querySelector('.burger');
  var nav = document.getElementById('main-nav') || document.querySelector('.nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }
  document.querySelectorAll('.has-dropdown > a').forEach(function (a) {
    a.addEventListener('click', function (e) {
      if (window.innerWidth <= 800) { e.preventDefault(); a.parentElement.classList.toggle('open'); }
    });
  });
  // FAQ: cualquier variante heredada (.sl-faq-q, .fq-q, .pp-faq-q, .dc-faq-q)
  document.querySelectorAll('.sl-faq-q, .fq-q, .pp-faq-q, .dc-faq-q').forEach(function (q) {
    q.setAttribute('role', 'button');
    q.addEventListener('click', function () {
      var item = q.closest('.sl-faq-item, .fq-item, .pp-faq-item, .dc-faq-item') || q.parentElement;
      if (item) item.classList.toggle('open');
    });
  });
  // Flechas de tiras con snap (organismos, carrusel home): desplazan una tarjeta, sin clonación.
  function wireTrack(trackId, prevId, nextId) {
    var track = document.getElementById(trackId);
    if (!track) return;
    var step = function () { var c = track.querySelector(':scope > *'); return c ? c.offsetWidth + 16 : 300; };
    var prev = document.getElementById(prevId), next = document.getElementById(nextId);
    if (prev) prev.addEventListener('click', function () { track.scrollBy({ left: -step(), behavior: 'smooth' }); });
    if (next) next.addEventListener('click', function () { track.scrollBy({ left: step(), behavior: 'smooth' }); });
  }
  wireTrack('org-track', 'org-prev', 'org-next');
  wireTrack('carousel-track', 'hero-nav-prev', 'hero-nav-next');
});
