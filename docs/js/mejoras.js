'use strict';
document.addEventListener('DOMContentLoaded', function () {
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const mobileScreen = window.matchMedia('(max-width: 767px)');
  const track = document.getElementById('carousel-track');
  const previous = document.getElementById('hero-nav-prev');
  const next = document.getElementById('hero-nav-next');
  function updateArrows() {
    if (!track || !previous || !next) return;
    previous.disabled = !mobileScreen.matches || track.scrollLeft <= 2;
    next.disabled = !mobileScreen.matches || track.scrollLeft >= track.scrollWidth - track.clientWidth - 2;
  }
  function moveSlide(direction) {
    if (!track?.firstElementChild || !mobileScreen.matches) return;
    const gap = parseFloat(window.getComputedStyle(track).gap) || 16;
    track.scrollBy({left: direction * (track.firstElementChild.getBoundingClientRect().width + gap), behavior: reducedMotion.matches ? 'auto' : 'smooth'});
  }
  if (track) {
    track.setAttribute('aria-label', 'Líneas de préstamos');
    previous?.addEventListener('click', () => moveSlide(-1));
    next?.addEventListener('click', () => moveSlide(1));
    track.addEventListener('scroll', updateArrows, {passive: true});
    window.addEventListener('resize', updateArrows);
    updateArrows();
  }

  const sectorForm = document.getElementById('sector-form');
  const sectorSelect = document.getElementById('sector-select');
  sectorForm?.addEventListener('submit', function (event) {
    event.preventDefault();
    if (!sectorForm.reportValidity()) return;
    const slug = sectorSelect.value;
    const known = [...sectorSelect.options].some(option => option.value === slug && slug !== '');
    if (known && /^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(slug)) window.location.assign(`./${slug}/`);
  });
  const search = document.getElementById('sector-search');
  const normalize = value => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();
  search?.addEventListener('input', function () {
    const terms = normalize(search.value).split(' ').filter(Boolean);
    let count = 0;
    document.querySelectorAll('#sector-results .org-item').forEach(function (card) {
      const text = normalize(`${card.dataset.sector || ''} ${card.textContent}`);
      const show = terms.every(term => text.includes(term));
      card.hidden = !show;
      if (show) count++;
    });
    document.getElementById('sector-no-results').hidden = count !== 0;
    document.getElementById('sector-search-status').textContent = `${count} ${count === 1 ? 'línea encontrada' : 'líneas encontradas'}`;
  });

  const header = document.getElementById('main-header');
  const mobileNav = document.getElementById('mobile-nav');
  const navToggle = document.getElementById('nav-toggle');
  function positionNav() {
    if (header && mobileNav) mobileNav.style.top = `${Math.max(0, header.getBoundingClientRect().bottom)}px`;
  }
  function closeNav() {
    if (!mobileNav || !navToggle) return;
    mobileNav.style.display = 'none';
    navToggle.classList.remove('active');
    navToggle.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }
  navToggle?.addEventListener('click', positionNav);
  window.addEventListener('resize', function () { positionNav(); if (window.innerWidth >= 900) closeNav(); });
  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape' && navToggle?.getAttribute('aria-expanded') === 'true') { closeNav(); navToggle.focus(); }
  });
  document.querySelectorAll('.nav-span').forEach(trigger => { trigger.tabIndex = 0; });
  document.querySelectorAll('.mob-submenu-toggle, .faq-q').forEach(function (trigger) {
    if (trigger.tagName === 'BUTTON') return;
    trigger.tabIndex = 0;
    trigger.setAttribute('role', 'button');
    trigger.addEventListener('keydown', function (event) {
      if (event.key === 'Enter' || event.key === ' ') { event.preventDefault(); trigger.click(); }
    });
  });
  positionNav();
});
