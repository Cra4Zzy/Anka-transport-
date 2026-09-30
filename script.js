const body = document.body;
const menuButton = document.querySelector('.menu-toggle');
const panel = document.querySelector('.mobile-panel');
const header = document.querySelector('.site-header');

menuButton?.addEventListener('click', () => {
  const open = menuButton.getAttribute('aria-expanded') === 'true';
  menuButton.setAttribute('aria-expanded', String(!open));
  panel.classList.toggle('is-open', !open);
  panel.setAttribute('aria-hidden', String(open));
  body.style.overflow = !open ? 'hidden' : '';
});

document.querySelectorAll('.mobile-panel a').forEach(link => link.addEventListener('click', () => {
  menuButton?.setAttribute('aria-expanded', 'false');
  panel?.classList.remove('is-open');
  panel?.setAttribute('aria-hidden', 'true');
  body.style.overflow = '';
}));

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const delay = Number(entry.target.dataset.delay || 0);
      setTimeout(() => entry.target.classList.add('is-visible'), delay);
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.12, rootMargin: '0px 0px -45px 0px' });

document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

const filterButtons = [...document.querySelectorAll('.filter')];
const courseCards = [...document.querySelectorAll('.course-card')];

function setCourseFilter(value) {
  filterButtons.forEach(button => button.classList.toggle('is-active', button.dataset.filter === value));
  courseCards.forEach(card => {
    const categories = (card.dataset.category || '').split(' ');
    card.hidden = value !== 'all' && !categories.includes(value);
  });
}

filterButtons.forEach(button => button.addEventListener('click', () => setCourseFilter(button.dataset.filter)));

document.querySelectorAll('[data-course-filter]').forEach(button => {
  button.addEventListener('click', () => {
    const value = button.dataset.courseFilter;
    setCourseFilter(value);
    document.querySelector('#kurse')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });
});

let ticking = false;
window.addEventListener('scroll', () => {
  if (ticking) return;
  ticking = true;
  requestAnimationFrame(() => {
    header?.classList.toggle('is-scrolled', window.scrollY > 90);
    ticking = false;
  });
}, { passive: true });

const hero = document.querySelector('.hero');
const finePointer = window.matchMedia('(pointer:fine)').matches;
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (hero && finePointer && !reducedMotion) {
  hero.addEventListener('pointermove', (event) => {
    const rect = hero.getBoundingClientRect();
    const x = ((event.clientX - rect.left) / rect.width - 0.5) * 18;
    const y = ((event.clientY - rect.top) / rect.height - 0.5) * 18;
    hero.style.setProperty('--hero-x', `${x}px`);
    hero.style.setProperty('--hero-y', `${y}px`);
  });
  hero.addEventListener('pointerleave', () => {
    hero.style.setProperty('--hero-x', '0px');
    hero.style.setProperty('--hero-y', '0px');
  });
}
