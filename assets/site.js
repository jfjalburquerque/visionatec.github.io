// year
document.getElementById('yr').textContent = new Date().getFullYear();
// sticky header
const hdr = document.getElementById('hdr');
addEventListener('scroll', () => hdr.classList.toggle('scrolled', scrollY > 30));
// reveal on scroll
const io = new IntersectionObserver((es) => {
  es.forEach(e => { if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target);} });
}, {threshold:.14});
document.querySelectorAll('.reveal').forEach(el => io.observe(el));
// hero reveal immediately
addEventListener('load', () => {
  document.querySelectorAll('.hero-inner .reveal').forEach(el => el.classList.add('in'));
});
setTimeout(()=>document.querySelectorAll('.hero-inner .reveal').forEach(el=>el.classList.add('in')),120);
// form -> Formspree (AJAX, sin recargar)
document.getElementById('form').addEventListener('submit', async (ev) => {
  ev.preventDefault();
  const form = ev.target;
  const ok = document.getElementById('ok');
  const err = document.getElementById('err');
  const btn = form.querySelector('button[type=submit]');
  ok.style.display = 'none'; err.style.display = 'none';
  // validación mínima
  if (!form.nombre.value.trim() || !form.email.value.trim()) {
    err.textContent = 'Por favor, completa tu nombre y tu email.';
    err.style.display = 'block'; return;
  }
  if (!form.acepta_privacidad.checked) {
    err.textContent = 'Necesitamos que aceptes la política de privacidad para poder responderte.';
    err.style.display = 'block'; return;
  }
  const original = btn.textContent;
  btn.textContent = 'Enviando…'; btn.disabled = true;
  try {
    const res = await fetch(form.action, {
      method: 'POST',
      body: new FormData(form),
      headers: { 'Accept': 'application/json' }
    });
    if (res.ok) {
      ok.style.display = 'block';
      form.reset();
    } else {
      err.textContent = 'Ups, algo ha fallado. Escríbenos directamente a info@visionatec.com';
      err.style.display = 'block';
    }
  } catch (e) {
    err.textContent = 'Sin conexión. Escríbenos directamente a info@visionatec.com';
    err.style.display = 'block';
  } finally {
    btn.textContent = original; btn.disabled = false;
  }
});
// mobile menu
const burger = document.getElementById('burger'), mnav = document.getElementById('mnav');
const setMenu = (open) => { mnav.classList.toggle('open', open); burger.setAttribute('aria-expanded', open); burger.textContent = open ? '×' : '≡'; };
burger.addEventListener('click', () => setMenu(!mnav.classList.contains('open')));
mnav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => setMenu(false)));
