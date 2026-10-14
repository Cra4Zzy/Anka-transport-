'use strict';
const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#navigation');
function closeMenu() { navigation.classList.remove('open'); menuButton.setAttribute('aria-expanded','false'); }
menuButton.addEventListener('click',()=>{const open=menuButton.getAttribute('aria-expanded')!=='true';menuButton.setAttribute('aria-expanded',String(open));navigation.classList.toggle('open',open);});
document.addEventListener('keydown',event=>{if(event.key==='Escape')closeMenu();});
document.addEventListener('click',event=>{if(!event.target.closest('.header'))closeMenu();});
navigation.querySelectorAll('a').forEach(link=>link.addEventListener('click',closeMenu));
window.matchMedia('(min-width:1051px)').addEventListener('change',event=>{if(event.matches)closeMenu();});
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
}

const fleetClasses={
 '7-5':{number:'7,5',unit:'t',title:'7,5-Tonner mit Fahrer',description:'Für Ihre regelmäßigen Transporte – mit Einsatzzeiten und Touren nach Vereinbarung.',use:'Regelmäßige Transporte'},
 '12':{number:'12',unit:'t',title:'12-Tonner mit Fahrer',description:'Für Ihre täglichen Transportaufgaben – fest in Ihre Abläufe eingeplant.',use:'Tägliche Transportaufgaben'},
 '18':{number:'18',unit:'t',title:'18-Tonner mit Fahrer',description:'Für Ihre laufenden Aufträge – als Ergänzung Ihrer Transportkapazitäten.',use:'Zusätzliche Kapazität'},
 'Sattelzug':{number:'Sattelzug',unit:'',title:'Sattelzüge mit Fahrer',description:'Für Transporte mit großem Platzbedarf – im langfristigen Festeinsatz.',use:'Großer Platzbedarf'}
};
document.querySelectorAll('[data-fleet-picker]').forEach(picker=>{
 const tabs=Array.from(picker.querySelectorAll('[role="tab"]'));
 const panel=picker.querySelector('[role="tabpanel"]');
 function select(tab,focus=false){
  const key=tab.dataset.fleet;const vehicle=fleetClasses[key];if(!vehicle)return;
  tabs.forEach(item=>{const active=item===tab;item.setAttribute('aria-selected',String(active));item.tabIndex=active?0:-1;});
  panel.setAttribute('aria-labelledby',tab.id);panel.dataset.kind=key;
  const weight=picker.querySelector('[data-fleet-weight]');weight.textContent=vehicle.number;
  if(vehicle.unit){const unit=document.createElement('small');unit.textContent=vehicle.unit;weight.appendChild(unit);}
  picker.querySelector('[data-fleet-title]').textContent=vehicle.title;
  picker.querySelector('[data-fleet-description]').textContent=vehicle.description;
  picker.querySelector('[data-fleet-use]').textContent=vehicle.use;
  picker.querySelector('[data-fleet-link]').href='unternehmen.html?fahrzeug='+encodeURIComponent(key)+'#anfrage';
  if(focus)tab.focus();
 }
 tabs.forEach((tab,index)=>{
  tab.addEventListener('click',()=>select(tab));
  tab.addEventListener('keydown',event=>{
   let next=index;
   if(event.key==='ArrowRight')next=(index+1)%tabs.length;
   else if(event.key==='ArrowLeft')next=(index-1+tabs.length)%tabs.length;
   else if(event.key==='Home')next=0;
   else if(event.key==='End')next=tabs.length-1;
   else return;
   event.preventDefault();select(tabs[next],true);
  });
 });
 const initial=new URLSearchParams(location.search).get('fahrzeug')||location.hash.slice(1);const matching=tabs.find(tab=>tab.dataset.fleet===initial);if(matching)select(matching);
});
