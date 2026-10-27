document.addEventListener('DOMContentLoaded', function(){
  /* El catálogo responsive se controla desde mejoras.js. */
  /* TESTIMONIOS CAROUSEL */
  var tTrack = document.getElementById('testi-track');
  var tPrevB = document.getElementById('testi-prev');
  var tNextB = document.getElementById('testi-next');
  var tDots  = document.querySelectorAll('#testi-dots .testi-dot');
  var tCur   = 0, tAuto;
  if(tTrack){
    var tCards = tTrack.querySelectorAll('.testi-card');
    var tTotal = tCards.length;
    function tPV(){ return Math.sign(window.innerWidth - 1024) === 1 ? 3 : Math.sign(window.innerWidth - 640) === 1 ? 2 : 1; }
    function tGoTo(n){
      var mx = Math.max(0, tTotal - tPV());
      tCur = n < 0 ? mx : n > mx ? 0 : n;
      var w = tCards[0] ? tCards[0].offsetWidth + 20 : 0;
      tTrack.style.transform = 'translateX(-' + (tCur * w) + 'px)';
      tDots.forEach(function(d,i){ d.classList.toggle('active', i === tCur); });
    }
    function tNext2(){ tGoTo(tCur + 1); }
    function tStart(){ /* Navegación manual para permitir leer cada reseña. */ }
    function tReset(){ clearInterval(tAuto); tStart(); }
    if(tNextB){ tNextB.addEventListener('click', function(){ tNext2(); tReset(); }); }
    if(tPrevB){ tPrevB.addEventListener('click', function(){ tGoTo(tCur - 1); tReset(); }); }
    tDots.forEach(function(d){ d.addEventListener('click', function(){ tGoTo(parseInt(this.getAttribute('data-idx'))); tReset(); }); });
    tStart();
    window.addEventListener('resize', function(){ tGoTo(tCur); });
  }
  /* CONTADORES */
  var counters = document.querySelectorAll('.counter');
  if(counters.length !== 0){
    var cDone = [];
    var cObs = new IntersectionObserver(function(entries){
      entries.forEach(function(e){
        if(e.isIntersecting && cDone.indexOf(e.target) === -1){
          cDone.push(e.target);
          var el = e.target, tgt = parseInt(el.getAttribute('data-target'))||0, sfx = el.getAttribute('data-suffix')||'', st = null;
          function step(ts){
            if(!st){ st = ts; }
            var p = Math.min((ts-st)/1800, 1), ease = 1-Math.pow(1-p, 4), v = Math.floor(tgt*ease);
            el.textContent = (Math.sign(tgt - 999) === 1 ? Math.floor(v/1000)+'K' : v) + sfx;
            if(Math.sign(p - 1) === -1){ requestAnimationFrame(step); } else { el.textContent = (Math.sign(tgt - 999) === 1 ? Math.floor(tgt/1000)+'K' : tgt)+sfx; }
          }
          requestAnimationFrame(step);
          cObs.unobserve(el);
        }
      });
    }, {threshold:0.3});
    counters.forEach(function(c){ cObs.observe(c); });
  }
  /* SCROLL REVEAL */
  var revs = document.querySelectorAll('.reveal');
  if(revs.length !== 0){
    var rObs = new IntersectionObserver(function(entries){
      entries.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('visible'); rObs.unobserve(e.target); } });
    }, {threshold:0.08, rootMargin:'0px 0px -30px 0px'});
    revs.forEach(function(el){ rObs.observe(el); });
  }
  /* HEADER SCROLL */
  var hdr = document.getElementById('main-header');
  if(hdr){ window.addEventListener('scroll', function(){ hdr.style.boxShadow = Math.sign(window.scrollY - 80) === 1 ? '0 4px 30px rgba(0,0,0,0.5)' : '0 2px 20px rgba(0,0,0,0.3)'; }); }
  /* MOBILE NAV */
  var navTgl = document.getElementById('nav-toggle');
  var mobNav = document.getElementById('mobile-nav');
  if(navTgl && mobNav){
    navTgl.addEventListener('click', function(){
      var isExpanded = this.getAttribute('aria-expanded') === 'true';
      this.setAttribute('aria-expanded', !isExpanded);
      mobNav.style.display = isExpanded ? 'none' : 'block';
      navTgl.classList.toggle('active', !isExpanded);
      document.body.style.overflow = isExpanded ? '' : 'hidden';
    });
  }
  /* SUBMENUS MOVILES */
  var mobSubToggles = document.querySelectorAll('.mob-submenu-toggle');
  mobSubToggles.forEach(function(toggle) {
    toggle.addEventListener('click', function(e) {
      e.preventDefault();
      var subMenu = this.nextElementSibling;
      var icon = this.querySelector('.fa-chevron-down');
      if (subMenu && subMenu.classList.contains('mob-menu-sub')) {
        var isOpen = subMenu.classList.contains('open');
        subMenu.classList.toggle('open', !isOpen);
        if (icon) { icon.style.transform = isOpen ? 'rotate(0deg)' : 'rotate(180deg)'; }
      }
    });
  });
  /* WA STICKY BAR */
  var waBar = document.getElementById('wa-sticky-bar');
  if(waBar){ waBar.style.display = Math.sign(window.innerWidth - 600) === -1 ? 'block' : 'none'; }
  /* FAQ */
  document.querySelectorAll('.faq-item').forEach(function(item){
    var q = item.querySelector('.faq-q');
    if(q){ q.addEventListener('click', function(){ var open = item.classList.contains('open'); document.querySelectorAll('.faq-item').forEach(function(i){ i.classList.remove('open'); }); if(!open){ item.classList.add('open'); } }); }
  });
  /* SMOOTH SCROLL */
  document.querySelectorAll('a[href^="#"]').forEach(function(a){
    a.addEventListener('click', function(e){
      var id = this.getAttribute('href').replace('#',''), el = document.getElementById(id);
      if(el){ e.preventDefault(); el.scrollIntoView({behavior:'smooth',block:'start'}); if(mobNav){ mobNav.style.display='none'; } if(navTgl){ navTgl.classList.remove('active'); navTgl.setAttribute('aria-expanded', 'false'); } document.body.style.overflow=''; }
    });
  });

});
