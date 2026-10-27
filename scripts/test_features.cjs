const assert = require('node:assert/strict');
const vm = require('node:vm');
const fs = require('node:fs');
const path = require('node:path');
function el(extra={}) {return Object.assign({handlers:{},attrs:{},style:{},hidden:false,classList:{remove(){}},addEventListener(k,f){this.handlers[k]=f},setAttribute(k,v){this.attrs[k]=v},getAttribute(k){return this.attrs[k]},focus(){this.focused=true}},extra)}
const screen={matches:true},reduce={matches:false};let destination;
const track=el({scrollLeft:0,scrollWidth:1600,clientWidth:360,firstElementChild:{getBoundingClientRect:()=>({width:300})},scrollBy(v){this.lastMove=v;this.scrollLeft=Math.min(1240,Math.max(0,this.scrollLeft+v.left));this.handlers.scroll()}});
const map={'carousel-track':track,'hero-nav-prev':el(),'hero-nav-next':el(),'sector-form':el({reportValidity:()=>true}),'sector-select':el({value:'',options:[{value:''},{value:'prestamos-policia-federal'}]}),'sector-search':el({value:''}),'sector-no-results':el(),'sector-search-status':el(),'main-header':el({getBoundingClientRect:()=>({bottom:100})}),'mobile-nav':el(),'nav-toggle':el()};
const cards=[el({dataset:{sector:'Policía Federal Argentina'},textContent:'Policía Federal'}),el({dataset:{sector:'Docentes y Auxiliares DGCyE'},textContent:'Docentes'}),el({dataset:{sector:'Jubilados y Pensionados IPS'},textContent:'IPS'})];
const doc={body:{style:{}},handlers:{},getElementById:id=>map[id]||null,querySelectorAll:sel=>sel==='#sector-results .org-item'?cards:[],addEventListener(k,f){this.handlers[k]=f}};
const win={innerWidth:390,handlers:{},matchMedia:q=>q.includes('max-width')?screen:reduce,getComputedStyle:()=>({gap:'16px'}),location:{assign:v=>destination=v},addEventListener(k,f){this.handlers[k]=f}};
vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../docs/js/mejoras.js'),'utf8'),{document:doc,window:win});doc.handlers.DOMContentLoaded();
assert.equal(map['hero-nav-prev'].disabled,true);map['hero-nav-next'].handlers.click();assert.equal(track.scrollLeft,316);assert.equal(track.lastMove.behavior,'smooth');assert.equal(map['hero-nav-prev'].disabled,false);map['hero-nav-prev'].handlers.click();assert.equal(track.scrollLeft,0);
reduce.matches=true;map['hero-nav-next'].handlers.click();assert.equal(track.lastMove.behavior,'auto');track.scrollLeft=1240;track.handlers.scroll();assert.equal(map['hero-nav-next'].disabled,true);
screen.matches=false;track.scrollLeft=0;map['hero-nav-next'].handlers.click();assert.equal(track.scrollLeft,0);
const input=q=>{map['sector-search'].value=q;map['sector-search'].handlers.input()};input('policia federal');assert.deepEqual(cards.map(c=>c.hidden),[false,true,true]);input('DGCYE');assert.deepEqual(cards.map(c=>c.hidden),[true,false,true]);input('xxxyyy');assert.equal(map['sector-no-results'].hidden,false);input('');assert(cards.every(c=>!c.hidden));assert.equal(map['sector-no-results'].hidden,true);
map['sector-select'].value='prestamos-policia-federal';map['sector-form'].handlers.submit({preventDefault(){}});assert.equal(destination,'./prestamos-policia-federal/');destination=null;map['sector-select'].value='https://example.com';map['sector-form'].handlers.submit({preventDefault(){}});assert.equal(destination,null);
map['nav-toggle'].attrs['aria-expanded']='true';doc.handlers.keydown({key:'Escape'});assert.equal(map['nav-toggle'].attrs['aria-expanded'],'false');assert(map['nav-toggle'].focused);
console.log('OK: carrusel móvil, límites, escritorio inmóvil, movimiento reducido, búsquedas sin tildes y por varias palabras, vacío/restauración, selector y Escape (DOM simulado).');
