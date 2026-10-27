'use strict';
(() => {
  const menuButton = document.querySelector('.menu-toggle');
  const navigation = document.getElementById('primary-nav');
  if (menuButton && navigation) {
    const closeMenu = () => {
      navigation.classList.remove('is-open');
      menuButton.setAttribute('aria-expanded', 'false');
      menuButton.setAttribute('aria-label', 'Abrir menú');
      document.body.classList.remove('no-scroll');
    };
    menuButton.addEventListener('click', () => {
      const opened = menuButton.getAttribute('aria-expanded') === 'true';
      if (opened) { closeMenu(); return; }
      navigation.classList.add('is-open');
      menuButton.setAttribute('aria-expanded', 'true');
      menuButton.setAttribute('aria-label', 'Cerrar menú');
      document.body.classList.add('no-scroll');
    });
    navigation.querySelectorAll('a').forEach(a => a.addEventListener('click', closeMenu));
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && menuButton.getAttribute('aria-expanded') === 'true') {
        closeMenu(); menuButton.focus();
      }
    });
    document.addEventListener('click', event => {
      if (!navigation.contains(event.target) && !menuButton.contains(event.target)) closeMenu();
    });
  }

  const sectorForm = document.getElementById('sector-form');
  if (sectorForm) {
    const sector = document.getElementById('sector-select');
    const feedback = document.getElementById('selector-message');
    const validRoutes = new Set([...sector.options].map(option => option.value).filter(Boolean));
    sectorForm.addEventListener('submit', event => {
      event.preventDefault();
      if (!sector.value || !validRoutes.has(sector.value)) {
        feedback.textContent = 'Seleccioná tu sector para continuar.';
        sector.focus();
        return;
      }
      // Lista local validada, evita redirecciones a destinos inyectados.
      window.location.assign(sector.value);
    });
    sector.addEventListener('change', () => { feedback.textContent = ''; });
  }
})();
