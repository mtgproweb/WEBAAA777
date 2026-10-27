'use strict';
document.documentElement.classList.add('js');
const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('#navigation');
function closeMenu() { nav?.classList.remove('open'); toggle?.setAttribute('aria-expanded', 'false'); }
toggle?.addEventListener('click', () => { const open = toggle.getAttribute('aria-expanded') !== 'true'; toggle.setAttribute('aria-expanded', String(open)); nav.classList.toggle('open', open); });
nav?.addEventListener('click', event => { if (event.target.closest('a')) closeMenu(); });
document.addEventListener('keydown', event => { if (event.key === 'Escape' && toggle?.getAttribute('aria-expanded') === 'true') { closeMenu(); toggle.focus(); } });
const normalize = value => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase().trim();
const search = document.querySelector('#sector-search');
search?.addEventListener('input', () => { const query = normalize(search.value); let count = 0; document.querySelectorAll('[data-sector]').forEach(card => { const match = normalize(card.dataset.sector).includes(query); card.hidden = !match; if (match) count++; }); document.querySelector('#empty-state').hidden = count !== 0; document.querySelector('#search-status').textContent = `${count} líneas encontradas`; });
const sectorSelect = document.querySelector('#sector-select');
function navigateSector(value) { if (sectorSelect && [...sectorSelect.options].some(option => option.value === value && value)) window.location.assign(`./${value}/`); }
document.querySelector('#sector-form')?.addEventListener('submit', event => { event.preventDefault(); if (event.currentTarget.reportValidity()) navigateSector(sectorSelect.value); });
const selected = new URLSearchParams(window.location.search).get('sector');
if (selected) navigateSector(selected);
