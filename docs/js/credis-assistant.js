(function () {
  'use strict';

  var WHATSAPP_URL = 'https://wa.me/541122845514?text=%C2%A1Hola!%20Vi%20la%20Web%20sobre%20pr%C3%A9stamos%20y%20me%20gustar%C3%ADa%20obtener%20m%C3%A1s%20informaci%C3%B3n.%20%C2%A1Muchas%20Gracias!';
  var STORAGE_KEY = 'credis-mascot-position-v8';
  var IDLE_HIDE_MS = 3000;
  var reducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var scriptEl = document.currentScript || (function () {
    var s = document.getElementsByTagName('script');
    return s[s.length - 1];
  })();
  var FULL_IMG = new URL('../img/credis/credis-full.png', scriptEl.src).href;

  function whatsappIcon() {
    return '<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M19.11 17.21c-.47-.24-2.79-1.38-3.22-1.54-.43-.16-.74-.24-1.06.24-.31.47-1.22 1.54-1.49 1.86-.27.31-.55.35-1.02.12-.47-.24-1.98-.73-3.77-2.33-1.39-1.24-2.33-2.78-2.6-3.25-.27-.47-.03-.73.21-.96.21-.21.47-.55.71-.82.24-.27.31-.47.47-.78.16-.31.08-.59-.04-.82-.12-.24-1.06-2.55-1.45-3.49-.38-.92-.77-.8-1.06-.81h-.9c-.31 0-.82.12-1.25.59-.43.47-1.65 1.61-1.65 3.92 0 2.31 1.69 4.55 1.92 4.86.24.31 3.32 5.07 8.04 7.11 1.12.48 2 .77 2.68.98 1.13.36 2.15.31 2.96.19.9-.13 2.79-1.14 3.18-2.24.39-1.1.39-2.04.27-2.24-.12-.2-.43-.31-.9-.55Z"/><path d="M16.02 2.67c-7.35 0-13.33 5.97-13.33 13.31 0 2.35.62 4.65 1.78 6.67L2.58 29.57l7.08-1.86a13.32 13.32 0 0 0 6.36 1.62h.01c7.35 0 13.33-5.97 13.33-13.31 0-3.56-1.39-6.9-3.91-9.42a13.24 13.24 0 0 0-9.43-3.93Zm0 24.41h-.01c-1.97 0-3.9-.53-5.58-1.53l-.4-.24-4.2 1.1 1.12-4.09-.26-.42a11.05 11.05 0 0 1-1.7-5.92c0-6.09 4.95-11.04 11.05-11.04 2.95 0 5.73 1.15 7.82 3.24a10.96 10.96 0 0 1 3.23 7.82c-.01 6.09-4.96 11.04-11.07 11.04Z"/></svg>';
  }

  function liveFaceSVG() {
    return '' +
      '<svg class="credis-liveface" viewBox="0 0 256 249" aria-hidden="true" focusable="false">' +
        '<defs>' +
          '<linearGradient id="credisMouthPatch" x1="0" y1="0" x2="0" y2="1">' +
            '<stop offset="0" stop-color="#08df73"/>' +
            '<stop offset=".50" stop-color="#05d66b"/>' +
            '<stop offset="1" stop-color="#03c75f"/>' +
          '</linearGradient>' +
          '<filter id="credisPatchSoft" x="-10%" y="-20%" width="120%" height="140%">' +
            '<feGaussianBlur stdDeviation="1.6"/>' +
          '</filter>' +
        '</defs>' +
        '<g class="credis-eye-covers">' +
          '<ellipse class="credis-eye-cover" cx="99" cy="116" rx="22" ry="29"/>' +
          '<ellipse class="credis-eye-cover" cx="160" cy="116" rx="22" ry="29"/>' +
        '</g>' +
        '<path class="credis-mouth-patch" filter="url(#credisPatchSoft)" d="M69 130 Q132 119 198 130 L198 176 Q132 190 69 176 Z"/>' +
        '<path class="credis-brow-live brow-left" d="M84 88 Q99 75 113 87"/>' +
        '<path class="credis-brow-live brow-right" d="M145 86 Q161 75 176 90"/>' +
        '<g class="credis-eye-live eye-left">' +
          '<ellipse class="credis-eye-white" cx="99" cy="116" rx="17" ry="23"/>' +
          '<g class="credis-pupil-group pupil-left">' +
            '<ellipse class="credis-pupil" cx="100" cy="120" rx="9.4" ry="13"/>' +
            '<circle class="credis-pupil-shine" cx="96.8" cy="115.5" r="3.3"/>' +
          '</g>' +
        '</g>' +
        '<g class="credis-eye-live eye-right">' +
          '<ellipse class="credis-eye-white" cx="160" cy="116" rx="17" ry="23"/>' +
          '<g class="credis-pupil-group pupil-right">' +
            '<ellipse class="credis-pupil" cx="161" cy="120" rx="9.4" ry="13"/>' +
            '<circle class="credis-pupil-shine" cx="157.8" cy="115.5" r="3.3"/>' +
          '</g>' +
        '</g>' +
        '<path class="credis-lid lid-left" d="M84 116 Q99 127 114 116"/>' +
        '<path class="credis-lid lid-right" d="M145 116 Q160 127 176 116"/>' +
        '<path class="credis-mouth mouth-neutral" d="M95 151 Q132 152 165 151 M159 144 L173 151 L161 159"/>' +
        '<path class="credis-mouth mouth-soft" d="M93 148 Q132 162 168 148 M162 140 L176 147 L164 156"/>' +
        '<path class="credis-mouth mouth-big" d="M90 145 Q132 177 171 145 M165 136 L179 144 L167 155"/>' +
      '</svg>';
  }

  function init() {
    if (document.getElementById('credis-assistant')) return;

    var root = document.createElement('div');
    root.id = 'credis-assistant';
    root.className = 'side-right';
    root.innerHTML =
      '<button class="credis-mascot side-right mouth-soft look-front" type="button" aria-label="Abrir a Credis, asistente de Credisnet" aria-haspopup="dialog" aria-expanded="false">' +
        '<span class="credis-figure">' +
          '<img class="credis-fullimg" src="' + FULL_IMG + '" alt="" aria-hidden="true">' +
          liveFaceSVG() +
        '</span>' +
        '<span class="credis-speech" aria-hidden="true"></span>' +
      '</button>' +
      '<div class="credis-backdrop" aria-hidden="true"></div>' +
      '<section class="credis-panel" role="dialog" aria-modal="true" aria-labelledby="credis-title" aria-hidden="true">' +
        '<div class="credis-panel-head">' +
          '<div class="credis-mini"><img src="' + FULL_IMG + '" alt="" aria-hidden="true"></div>' +
          '<div class="credis-title-wrap"><div class="credis-kicker">Asistente Credisnet</div><h2 class="credis-title" id="credis-title">Hola, soy Credis 👋</h2></div>' +
          '<button class="credis-close" type="button" aria-label="Cerrar Credis">×</button>' +
        '</div>' +
        '<p class="credis-intro"><strong>Estoy por acá para ayudarte.</strong><br>Elegí una opción y te orientamos rápido.</p>' +
        '<div class="credis-options">' +
          '<button class="credis-option" type="button" data-key="monto"><span>💰</span>¿Cuánto puedo solicitar?</button>' +
          '<button class="credis-option" type="button" data-key="funciona"><span>⚡</span>¿Cómo funciona?</button>' +
          '<button class="credis-option" type="button" data-key="solicitar"><span>🚀</span>Quiero solicitar mi préstamo</button>' +
        '</div>' +
        '<div class="credis-answer" aria-live="polite">' +
          '<h3 class="credis-answer-title"></h3><p class="credis-answer-text"></p>' +
          '<a class="credis-wa credis-answer-wa" href="' + WHATSAPP_URL + '" target="_blank" rel="noopener noreferrer">' + whatsappIcon() + 'Continuar por WhatsApp</a>' +
        '</div>' +
        '<a class="credis-wa credis-direct" href="' + WHATSAPP_URL + '" target="_blank" rel="noopener noreferrer">' + whatsappIcon() + 'Hablar con un asesor</a>' +
        '<p class="credis-note">La atención continúa por WhatsApp con un asesor de Credisnet.</p>' +
      '</section>';
    document.body.appendChild(root);

    var mascot = root.querySelector('.credis-mascot');
    var speech = root.querySelector('.credis-speech');
    var panel = root.querySelector('.credis-panel');
    var backdrop = root.querySelector('.credis-backdrop');
    var closeBtn = root.querySelector('.credis-close');
    var answerBox = root.querySelector('.credis-answer');
    var answerTitle = root.querySelector('.credis-answer-title');
    var answerText = root.querySelector('.credis-answer-text');
    var optionButtons = root.querySelectorAll('.credis-option');
    var waButtons = root.querySelectorAll('.credis-wa');
    var pupilLeft = root.querySelector('.pupil-left');
    var pupilRight = root.querySelector('.pupil-right');

    var answers = {
      monto: {
        title: 'Tu disponible depende de tu línea',
        text: 'El monto se define por la línea que te corresponde y por el margen disponible en tus haberes. Por WhatsApp te confirmamos cuánto tenés disponible.'
      },
      funciona: {
        title: 'Es por descuento de haberes',
        text: 'Las cuotas se descuentan directamente de tus haberes. Si tenés margen disponible, un asesor puede ayudarte a avanzar con la solicitud.'
      },
      solicitar: {
        title: '¡Perfecto!',
        text: 'Escribinos por WhatsApp y un asesor de Credisnet te ayuda a consultar tu disponible y continuar con la solicitud.'
      }
    };

    var state = {
      side: 'right',
      topRatio: 0.58,
      dragging: false,
      moved: false,
      pointerId: null,
      startX: 0,
      startY: 0,
      startLeft: 0,
      startTop: 0,
      panelOpen: false,
      bubbleTimer: null,
      idleTimer: null,
      blinkTimer: null,
      faceTimer: null,
      faceIndex: 0
    };

    function viewport() { return { w: window.innerWidth, h: window.innerHeight }; }
    function clamp(v, min, max) { return Math.max(min, Math.min(max, v)); }
    function bottomSafe() { return document.getElementById('wa-float') ? 92 : 22; }
    function topSafe() { return window.innerWidth <= 640 ? 76 : 90; }

    function savePosition() {
      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify({ side: state.side, topRatio: state.topRatio }));
      } catch (e) {}
    }

    function loadPosition() {
      try {
        var saved = JSON.parse(localStorage.getItem(STORAGE_KEY) || 'null');
        if (saved && (saved.side === 'left' || saved.side === 'right') && typeof saved.topRatio === 'number') {
          state.side = saved.side;
          state.topRatio = clamp(saved.topRatio, 0.15, 0.84);
        }
      } catch (e) {}
    }

    function setSideClass() {
      root.classList.toggle('side-left', state.side === 'left');
      root.classList.toggle('side-right', state.side === 'right');
      mascot.classList.toggle('side-left', state.side === 'left');
      mascot.classList.toggle('side-right', state.side === 'right');
    }

    function positionFromState(animate) {
      var vp = viewport();
      var size = mascot.offsetHeight || 46;
      var width = mascot.offsetWidth || 46;
      var minY = topSafe();
      var maxY = Math.max(minY, vp.h - size - bottomSafe());
      var y = clamp(state.topRatio * vp.h, minY, maxY);
      var x = state.side === 'left' ? 4 : vp.w - width - 4;

      if (!animate) mascot.style.transition = 'none';
      mascot.style.left = x + 'px';
      mascot.style.top = y + 'px';
      setSideClass();

      if (!animate) requestAnimationFrame(function () { mascot.style.transition = ''; });
    }

    function snapToEdge(x, y, animate) {
      var vp = viewport();
      var width = mascot.offsetWidth || 46;
      var height = mascot.offsetHeight || 46;
      state.side = (x + width / 2) < vp.w / 2 ? 'left' : 'right';
      var minY = topSafe();
      var maxY = Math.max(minY, vp.h - height - bottomSafe());
      var clampedY = clamp(y, minY, maxY);
      state.topRatio = clamp(clampedY / vp.h, 0.1, 0.9);

      savePosition();
      positionFromState(animate !== false);
      mascot.classList.add('is-happy');
      setMouth('big');
      setTimeout(function () { mascot.classList.remove('is-happy'); }, 620);
      registerActivity();
    }

    function setLook(direction) {
      var dx = 0;
      if (direction === 'left') dx = -14;
      if (direction === 'right') dx = 14;
      var dy = direction === 'front' ? 0 : -1.2;
      var t = 'translate(' + dx + ' ' + dy + ')';
      pupilLeft.setAttribute('transform', t);
      pupilRight.setAttribute('transform', t);
      mascot.classList.remove('look-left', 'look-right', 'look-front');
      mascot.classList.add('look-' + direction);
    }

    function lookInward() {
      setLook(state.side === 'right' ? 'left' : 'right');
    }

    function setMouth(kind) {
      mascot.classList.remove('mouth-neutral', 'mouth-soft', 'mouth-big');
      mascot.classList.add('mouth-' + kind);
    }

    function hideSpeech() { speech.classList.remove('is-visible'); }

    var messages = ['¡Hola! 👋', '¿Necesitás una mano?', 'Estoy por acá 😄', '¿Querés consultar tu disponible? 👀'];
    function speechLoop(first) {
      if (reducedMotion) return;
      clearTimeout(state.bubbleTimer);
      state.bubbleTimer = setTimeout(function () {
        if (!state.dragging && !state.panelOpen && !document.hidden && !mascot.classList.contains('is-peeking')) {
          speech.textContent = messages[Math.floor(Math.random() * messages.length)];
          speech.classList.add('is-visible');
          setTimeout(hideSpeech, 3200);
        }
        speechLoop(false);
      }, first ? 10000 : 18000 + Math.random() * 14000);
    }

    /* Vida propia: no depende de la posición del mouse. Mientras Credis esté visible,
       alterna mirada y sonrisa en un ciclo suave. */
    var faceSequence = [
      { look: 'front', mouth: 'soft',    hold: 850 },
      { look: 'left',  mouth: 'soft',    hold: 900, pose: 'lean-left' },
      { look: 'front', mouth: 'neutral', hold: 520 },
      { look: 'front', mouth: 'big',     hold: 1050, pose: 'happy' },
      { look: 'right', mouth: 'soft',    hold: 900, pose: 'lean-right' },
      { look: 'front', mouth: 'soft',    hold: 760 },
      { look: 'left',  mouth: 'big',     hold: 820, pose: 'lean-left' },
      { look: 'front', mouth: 'neutral', hold: 460 },
      { look: 'right', mouth: 'big',     hold: 820, pose: 'lean-right' },
      { look: 'front', mouth: 'soft',    hold: 900 }
    ];

    function faceLoop() {
      /* Las expresiones faciales siguen activas aun con movimiento reducido.
         En ese modo se elimina la flotacion corporal, pero los ojos, la boca y
         el parpadeo continúan para que Credis no quede congelado en escritorio. */
      clearTimeout(state.faceTimer);

      function step() {
        if (state.dragging || state.panelOpen || document.hidden || mascot.classList.contains('is-peeking')) {
          state.faceTimer = setTimeout(step, 350);
          return;
        }

        var item = faceSequence[state.faceIndex % faceSequence.length];
        state.faceIndex += 1;
        setLook(item.look);
        setMouth(item.mouth);

        mascot.classList.remove('pose-left', 'pose-right', 'pose-happy');
        if (item.pose === 'lean-left') mascot.classList.add('pose-left');
        if (item.pose === 'lean-right') mascot.classList.add('pose-right');
        if (item.pose === 'happy') mascot.classList.add('pose-happy');

        state.faceTimer = setTimeout(function () {
          mascot.classList.remove('pose-left', 'pose-right', 'pose-happy');
          step();
        }, item.hold);
      }

      state.faceTimer = setTimeout(step, 500);
    }

    function blinkLoop() {
      clearTimeout(state.blinkTimer);
      state.blinkTimer = setTimeout(function () {
        if (!state.dragging && !state.panelOpen) {
          mascot.classList.add('is-blinking');
          setTimeout(function () { mascot.classList.remove('is-blinking'); }, 120);
        }
        blinkLoop();
      }, 2800 + Math.random() * 3600);
    }

    function hideHalf() {
      if (state.dragging || state.panelOpen || document.hidden) return;
      hideSpeech();
      mascot.classList.remove('is-curious', 'pose-left', 'pose-right', 'pose-happy');
      mascot.classList.add('is-peeking');
      lookInward();
      setMouth('soft');
    }

    function scheduleIdleHide() {
      clearTimeout(state.idleTimer);
      if (state.dragging || state.panelOpen || document.hidden) return;
      state.idleTimer = setTimeout(hideHalf, IDLE_HIDE_MS);
    }

    function wakeUp() {
      if (mascot.classList.contains('is-peeking')) {
        mascot.classList.remove('is-peeking');
        mascot.classList.add('is-waking');
        setLook('front');
        setMouth('soft');
        setTimeout(function () { mascot.classList.remove('is-waking'); }, 440);
      }
    }

    /* Cualquier actividad real mantiene a Credis visible. El ciclo facial NO sigue al cursor;
       simplemente continúa con su animación predefinida. */
    function registerActivity() {
      if (state.dragging || state.panelOpen || document.hidden) return;
      wakeUp();
      scheduleIdleHide();
    }

    function openPanel() {
      clearTimeout(state.idleTimer);
      hideSpeech();
      mascot.classList.remove('is-peeking');
      state.panelOpen = true;
      root.classList.add('is-open');
      panel.setAttribute('aria-hidden', 'false');
      mascot.setAttribute('aria-expanded', 'true');
      setLook('front');
      setMouth('big');
      mascot.classList.add('is-happy');
      setTimeout(function () { mascot.classList.remove('is-happy'); }, 620);
      setTimeout(function () { closeBtn.focus({ preventScroll: true }); }, 80);
    }

    function closePanel(returnFocus) {
      state.panelOpen = false;
      root.classList.remove('is-open');
      panel.setAttribute('aria-hidden', 'true');
      mascot.setAttribute('aria-expanded', 'false');
      setLook('front');
      setMouth('soft');
      if (returnFocus !== false) mascot.focus({ preventScroll: true });
      scheduleIdleHide();
    }

    optionButtons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var answer = answers[this.getAttribute('data-key')];
        if (!answer) return;
        setMouth('big');
        answerTitle.textContent = answer.title;
        answerText.textContent = answer.text;
        answerBox.classList.add('is-visible');
      });
    });

    waButtons.forEach(function (link) {
      link.addEventListener('click', function () {
        setTimeout(function () { closePanel(false); }, 80);
      });
    });

    closeBtn.addEventListener('click', function () { closePanel(true); });
    backdrop.addEventListener('click', function () { closePanel(true); });
    document.addEventListener('keydown', function (e) {
      if (state.panelOpen && e.key === 'Escape') closePanel(true);
      else if (!state.panelOpen) registerActivity();
    });

    mascot.addEventListener('pointerdown', function (e) {
      if (state.panelOpen) return;
      hideSpeech();
      wakeUp();
      clearTimeout(state.idleTimer);
      state.dragging = true;
      state.moved = false;
      state.pointerId = e.pointerId;
      state.startX = e.clientX;
      state.startY = e.clientY;
      state.startLeft = parseFloat(mascot.style.left) || mascot.getBoundingClientRect().left;
      state.startTop = parseFloat(mascot.style.top) || mascot.getBoundingClientRect().top;
      mascot.classList.add('is-dragging');
      mascot.classList.remove('is-peeking');
      try { mascot.setPointerCapture(e.pointerId); } catch (err) {}
    });

    mascot.addEventListener('pointermove', function (e) {
      if (!state.dragging || e.pointerId !== state.pointerId) return;
      var dx = e.clientX - state.startX;
      var dy = e.clientY - state.startY;
      if (Math.abs(dx) + Math.abs(dy) > 7) state.moved = true;
      if (!state.moved) return;
      var vp = viewport();
      var width = mascot.offsetWidth || 46;
      var height = mascot.offsetHeight || 46;
      mascot.style.left = clamp(state.startLeft + dx, 0, vp.w - width) + 'px';
      mascot.style.top = clamp(state.startTop + dy, topSafe(), vp.h - height - bottomSafe()) + 'px';
    });

    function endDrag(e) {
      if (!state.dragging || (e.pointerId != null && e.pointerId !== state.pointerId)) return;
      state.dragging = false;
      mascot.classList.remove('is-dragging');
      try { mascot.releasePointerCapture(state.pointerId); } catch (err) {}
      var rect = mascot.getBoundingClientRect();
      if (state.moved) snapToEdge(rect.left, rect.top, true);
      else openPanel();
      state.pointerId = null;
    }

    mascot.addEventListener('pointerup', endDrag);
    mascot.addEventListener('pointercancel', endDrag);

    function activityHandler(e) {
      if (state.dragging || state.panelOpen || document.hidden) return;
      if (e && e.pointerType === 'touch' && e.type === 'pointermove') return;
      registerActivity();
    }

    document.addEventListener('pointermove', activityHandler, { passive: true });
    document.addEventListener('mousemove', activityHandler, { passive: true });
    document.addEventListener('scroll', activityHandler, { passive: true });
    document.addEventListener('wheel', activityHandler, { passive: true });
    document.addEventListener('touchstart', activityHandler, { passive: true });
    document.addEventListener('touchmove', activityHandler, { passive: true });
    document.addEventListener('click', activityHandler, { passive: true });

    document.addEventListener('visibilitychange', function () {
      if (!document.hidden && !state.panelOpen) {
        registerActivity();
      }
    });

    window.addEventListener('resize', function () {
      positionFromState(false);
      registerActivity();
    });

    loadPosition();
    positionFromState(false);
    setLook('front');
    setMouth('soft');
    blinkLoop();
    faceLoop();
    speechLoop(true);
    scheduleIdleHide();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init, { once: true });
  } else {
    init();
  }
})();
