'use strict';

const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
const smoothEase = 'cubic-bezier(.22, 1, .36, 1)';

function animateIn(element, {distance=10, opacity=.72, duration=480, delay=0}={}) {
 if (!element || reducedMotion.matches || typeof element.animate !== 'function') return;
 return element.animate(
  [{opacity, transform:`translateY(${distance}px)`}, {opacity:1, transform:'translateY(0)'}],
  {duration, delay, easing:smoothEase, fill:delay ? 'backwards' : 'none'}
 );
}

// Content is always present; motion only plays once as a section approaches the viewport.
if (!reducedMotion.matches && 'IntersectionObserver' in window) {
 const reveals = document.querySelectorAll([
  '.intro-copy', '.intro-photo', '.fleet-section .section-title', '.fleet-picker',
  '.partner-photo', '.partner-copy', '.process-section .section-title', '.steps article',
  '.planning-copy', '.planning-photo', '.faq-items', '.about-copy', '.credential-cards article',
  '.contact-intro', '#request-form', '.closing'
 ].join(','));
 const observer = new IntersectionObserver(entries => {
  entries.forEach(({isIntersecting,target}) => {
   if (!isIntersecting) return;
   observer.unobserve(target);
   animateIn(target);
  });
 }, {rootMargin:'0px 0px 30px 0px'});
 reveals.forEach(element => {
  if (element.getBoundingClientRect().top >= window.innerHeight) observer.observe(element);
 });
}

const hero = document.querySelector('.hero-copy, .subhero-copy');
if (hero?.getBoundingClientRect().bottom > 0 && hero.getBoundingClientRect().top < window.innerHeight) {
 animateIn(hero, {distance:8, opacity:.86, duration:520});
}
document.querySelectorAll('.faq details').forEach(detail => {
 detail.addEventListener('toggle', () => {
  if (detail.open) animateIn(detail.querySelector('p'), {distance:4, opacity:.7, duration:260});
 });
});
const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#navigation');
function closeMenu() { navigation.classList.remove('open'); menuButton.setAttribute('aria-expanded','false'); }
menuButton.addEventListener('click',()=>{const open=menuButton.getAttribute('aria-expanded')!=='true';menuButton.setAttribute('aria-expanded',String(open));navigation.classList.toggle('open',open);
 if(open) animateIn(navigation, {distance:-6, opacity:.7, duration:230});
});
document.addEventListener('keydown',event=>{if(event.key==='Escape')closeMenu();});
document.addEventListener('click',event=>{if(!event.target.closest('.header'))closeMenu();});
navigation.querySelectorAll('a').forEach(link=>link.addEventListener('click',closeMenu));
window.matchMedia('(min-width:1101px)').addEventListener('change',event=>{if(event.matches)closeMenu();});
document.querySelectorAll('[data-year]').forEach(node=>node.textContent=new Date().getFullYear());
document.querySelectorAll('[data-dialog]').forEach(button=>button.addEventListener('click',()=>document.getElementById(button.dataset.dialog).showModal()));
document.querySelectorAll('dialog').forEach(dialog=>{dialog.querySelector('.dialog-close').addEventListener('click',()=>dialog.close());dialog.addEventListener('click',event=>{if(event.target===dialog){const rect=dialog.getBoundingClientRect();if(event.clientX<rect.left||event.clientX>rect.right||event.clientY<rect.top||event.clientY>rect.bottom)dialog.close();}});});
const form=document.querySelector('#request-form');
if(form){
 const selected=new URLSearchParams(location.search).get('fahrzeug');
 const classes={'7-5':'7,5-Tonner','12':'12-Tonner','18':'18-Tonner','Sattelzug':'Sattelzüge'};
 if(classes[selected]){const radio=Array.from(form.elements.fahrzeug).find(item=>item.value===classes[selected]);if(radio)radio.checked=true;}
 const date=form.elements.start;
 const now=new Date();const localDay=new Date(now.getTime()-now.getTimezoneOffset()*60000).toISOString().slice(0,10);date.min=localDay;
 // Keep personal input only in the live form; there is no browser storage or network submission.
 form.addEventListener('submit',event=>{
  event.preventDefault();if(!form.reportValidity())return;
  const data=new FormData(form);const val=name=>String(data.get(name)||'').trim();
  const start=val('start');const formatted=start?new Date(start+'T12:00:00').toLocaleDateString('de-DE'):'Nach Vereinbarung';
  const summary=['ANFRAGE FESTEINSATZ — ANKA TRANSPORT','','Gewünschte Fahrzeugklasse: '+val('fahrzeug'),'Unternehmen: '+val('unternehmen'),'Ansprechperson: '+val('name'),'E-Mail: '+val('email'),'Telefon: '+(val('telefon')||'Nicht angegeben'),'Einsatzort: '+val('einsatzort'),'Geplanter Start: '+formatted,'','Touren, Einsatzzeiten & Laufzeit:',val('details')||'Im persönlichen Gespräch abzustimmen.'].join('\n');
  document.querySelector('#summary-text').textContent=summary;document.querySelector('#copy-status').textContent='';document.querySelector('#request-summary').showModal();
 });
 document.querySelector('#copy-request').addEventListener('click',async()=>{
  const text=document.querySelector('#summary-text').textContent;
  try {await navigator.clipboard.writeText(text);document.querySelector('#copy-status').textContent='Anfrage kopiert. Sie können die Übersicht jetzt einfügen.';}
  catch {const range=document.createRange();range.selectNodeContents(document.querySelector('#summary-text'));const selection=window.getSelection();selection.removeAllRanges();selection.addRange(range);document.querySelector('#copy-status').textContent='Bitte kopieren Sie den markierten Text mit Strg+C oder über das Auswahlmenü.';}
 });
 form.querySelector('.request-controls').disabled=false;
}

const fleetClasses={
 '7-5':{number:'7,5',unit:'t',title:'7,5-Tonner mit Fahrer',description:'Für Ihre regelmäßigen Transporte – mit Einsatzzeiten und Touren nach Vereinbarung.',use:'Regelmäßige Transporte'},
 '12':{number:'12',unit:'t',title:'12-Tonner mit Fahrer',description:'Für Ihre täglichen Transportaufgaben – fest in Ihre Abläufe eingeplant.',use:'Tägliche Transportaufgaben'},
 '18':{number:'18',unit:'t',title:'18-Tonner mit Fahrer',description:'Für Ihre laufenden Aufträge – als Ergänzung Ihrer Transportkapazitäten.',use:'Zusätzliche Kapazität'},
 'Sattelzug':{number:'Sattelzug',unit:'',title:'Sattelzüge mit Fahrer',description:'Für Transporte mit großem Platzbedarf – im langfristigen Festeinsatz.',use:'Großer Platzbedarf'}
};
document.querySelectorAll('[data-fleet-picker]').forEach(picker => {
 const rail = picker.querySelector('.fleet-tabs');
 const tabs = [...rail.querySelectorAll('[role="tab"]')];
 const panel = picker.querySelector('[role="tabpanel"]');
 const weight = panel.querySelector('[data-fleet-weight]');
 const title = panel.querySelector('[data-fleet-title]');
 const description = panel.querySelector('[data-fleet-description]');
 const use = panel.querySelector('[data-fleet-use]');
 const link = panel.querySelector('[data-fleet-link]');
 const indexLabel = panel.querySelector('[data-fleet-index]');
 let switchAnimations = [];

 function select(index, {focus=false, animate=true}={}) {
  const tab = tabs[index];
  const key = tab.dataset.fleet;
  const vehicle = fleetClasses[key];
  if (!vehicle) return;
  const changed = panel.dataset.kind !== key;
  tabs.forEach((item, i) => {
   item.setAttribute('aria-selected', String(i === index));
   item.tabIndex = i === index ? 0 : -1;
  });
  rail.style.setProperty('--active-tab', index);
  panel.setAttribute('aria-labelledby', tab.id);
  panel.dataset.kind = key;
  indexLabel.textContent = String(index + 1).padStart(2, '0');
  weight.textContent = vehicle.number;
  if (vehicle.unit) {
   const unit = document.createElement('small');
   unit.textContent = vehicle.unit;
   weight.appendChild(unit);
  }
  title.textContent = vehicle.title;
  description.textContent = vehicle.description;
  use.textContent = vehicle.use;
  link.href = 'unternehmen.html?fahrzeug=' + encodeURIComponent(key) + '#anfrage';

  if (changed) {
   switchAnimations.forEach(animation => animation.cancel());
   switchAnimations = [];
   if (animate && !reducedMotion.matches) {
    switchAnimations = [weight, title, description, use].map((element, i) =>
     animateIn(element, {distance:-12, opacity:0, duration:360, delay:i * 34})
    ).filter(Boolean);
    const truck = panel.querySelector(`[data-truck="${key}"]`);
    if (typeof truck?.animate === 'function') {
     switchAnimations.push(truck.animate([
      {opacity:.12, transform:'translateX(16px) scale(.985)'},
      {opacity:1, transform:'translateX(0) scale(1)'}
     ], {duration:430, easing:smoothEase}));
    }
   }
  }
  if (focus) tab.focus();
 }

 const initial = new URLSearchParams(location.search).get('fahrzeug') || location.hash.slice(1);
 select(Math.max(0, tabs.findIndex(tab => tab.dataset.fleet === initial)), {animate:false});
 rail.classList.add('is-enhanced');
 tabs.forEach((tab, index) => {
  tab.addEventListener('click', () => select(index));
  tab.addEventListener('keydown', event => {
   let next;
   if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
   else if (event.key === 'ArrowLeft') next = (index - 1 + tabs.length) % tabs.length;
   else if (event.key === 'Home') next = 0;
   else if (event.key === 'End') next = tabs.length - 1;
   else return;
   event.preventDefault();
   select(next, {focus:true});
  });
 });
});
