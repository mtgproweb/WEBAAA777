/* Ajustes de interacción del nuevo diseño; sin cambios de contenido comercial. */
document.addEventListener('DOMContentLoaded', function () {
  const header = document.getElementById('main-header');
  const mobile = document.getElementById('mobile-nav');
  const toggle = document.getElementById('nav-toggle');
  function positionMenu() {
    if (header && mobile) mobile.style.top = `${Math.max(0, header.getBoundingClientRect().bottom)}px`;
  }
  function closeMenu() {
    if (!mobile || !toggle) return;
    mobile.style.display = 'none';
    toggle.classList.remove('active');
    toggle.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }
  toggle?.addEventListener('click', positionMenu);
  window.addEventListener('resize', function () {
    positionMenu();
    if (window.innerWidth >= 1024) closeMenu();
  });
  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape' && toggle?.getAttribute('aria-expanded') === 'true') {
      closeMenu(); toggle.focus();
    }
  });
  document.querySelectorAll('.nav-span').forEach(function (trigger) {
    trigger.tabIndex = 0;
  });
  document.querySelectorAll('.mob-submenu-toggle, .faq-q').forEach(function (trigger) {
    if (trigger.tagName === 'BUTTON') return;
    trigger.tabIndex = 0;
    trigger.setAttribute('role', 'button');
    trigger.addEventListener('keydown', function (event) {
      if (event.key === 'Enter' || event.key === ' ') { event.preventDefault(); trigger.click(); }
    });
  });
  positionMenu();
});
