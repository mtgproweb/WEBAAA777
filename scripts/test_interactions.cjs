const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
function element(extra = {}) { return Object.assign({ handlers: {}, hidden: false, value: '', attrs: {}, classList: { toggle(){}, remove(){}, add(){} }, addEventListener(k,v){this.handlers[k]=v}, setAttribute(k,v){this.attrs[k]=v}, getAttribute(k){return this.attrs[k]}, focus(){this.focused=true} },extra); }
const map = { '.menu-toggle': element(), '#navigation': element(), '#sector-search': element(), '#empty-state': element(), '#search-status': element(), '#sector-select': element({ options:[{value:''},{value:'prestamos-policia-federal'}] }), '#sector-form': element({reportValidity:()=>true}) };
const cards = [element({dataset:{sector:'Policía Federal Argentina'}}),element({dataset:{sector:'Docentes y Auxiliares'}})];
let navigated; const document = {documentElement:element(), querySelector:s=>map[s]||null,querySelectorAll:()=>cards, addEventListener(k,v){this[k]=v}};
vm.runInNewContext(fs.readFileSync(require('node:path').join(__dirname,'../docs/js/site.js'),'utf8'),{document,window:{location:{search:'',assign:v=>navigated=v}},URLSearchParams});
map['.menu-toggle'].handlers.click();assert.equal(map['.menu-toggle'].attrs['aria-expanded'],'true');document.keydown({key:'Escape'});assert.equal(map['.menu-toggle'].attrs['aria-expanded'],'false');assert(map['.menu-toggle'].focused);
map['#sector-search'].value='policia';map['#sector-search'].handlers.input();assert(!cards[0].hidden && cards[1].hidden);
map['#sector-search'].value='xyz';map['#sector-search'].handlers.input();assert(!map['#empty-state'].hidden);
map['#sector-search'].value='';map['#sector-search'].handlers.input();assert(cards.every(c=>!c.hidden));
map['#sector-select'].value='prestamos-policia-federal';map['#sector-form'].handlers.submit({preventDefault(){},currentTarget:map['#sector-form']});assert.equal(navigated,'./prestamos-policia-federal/');
navigated=null;map['#sector-select'].value='https://example.com';map['#sector-form'].handlers.submit({preventDefault(){},currentTarget:map['#sector-form']});assert.equal(navigated,null);
console.log('OK: menú, Escape y foco, búsqueda sin tildes, estado vacío, restauración y navegación validada (DOM simulado).');
