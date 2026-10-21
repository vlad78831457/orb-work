// Проба вебхука без Google: Code.gs под node на заглушке Таблиц. node tools/veb/proba.js > out.json
// Лист с общим каркасом, данные под заголовками, лист легенды маски. Проверяет: ключ, данные не уходят, теги одинаковы
// для одинаковых значений, «нельзя» и неразмеченное не отдаются. Ошибка — выход 1 и текст в stderr.
'use strict';
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const L = (n) => { let s = ''; while (n > 0) { const m = (n - 1) % 26; s = String.fromCharCode(65 + m) + s; n = Math.floor((n - 1) / 26); } return s; };

function makeSheet(name, grid, opts = {}) {
  // grid: {"C1": {v, f, bg, dv}} ; размер по занятым ячейкам
  let rows = 1, cols = 1;
  for (const k of Object.keys(grid)) {
    const m = k.match(/^([A-Z]+)(\d+)$/);
    let c = 0; for (const ch of m[1]) c = c * 26 + ch.charCodeAt(0) - 64;
    rows = Math.max(rows, +m[2]); cols = Math.max(cols, c);
  }
  const cell = (r, c) => grid[L(c) + r] || {};
  const range = (r0, c0, nr, nc) => {
    const map = (fn) => Array.from({ length: nr }, (_, i) => Array.from({ length: nc }, (_, j) => fn(cell(r0 + i, c0 + j))));
    return {
      getDisplayValues: () => map((x) => (x.v === undefined ? '' : String(x.v))),
      getFormulas: () => map((x) => x.f || ''),
      getBackgrounds: () => map((x) => x.bg || '#ffffff'),
      getDataValidations: () => map((x) => (x.dv ? {
        getCriteriaType: () => 'VALUE_IN_LIST', getCriteriaValues: () => [x.dv] } : null)),
      getMergedRanges: () => [],
    };
  };
  return {
    getName: () => name, getLastRow: () => rows, getLastColumn: () => cols, getRange: range,
    getFrozenRows: () => opts.frozenRows || 0, getFrozenColumns: () => opts.frozenCols || 0,
    isColumnHiddenByUser: (c) => (opts.hidden || []).includes(c), getConditionalFormatRules: () => [1, 2],
  };
}

const GREEN = '#b6d7a8', YELLOW = '#ffe599', RED = '#ea9999';
const data = makeSheet('5-5 Проба', {
  C1: { v: 'header_first' }, C2: { v: 'key' }, D2: { v: 'Поставщик' }, E2: { v: 'Цена' }, F2: { v: 'Почта' },
  C3: { v: 'formulaColl' }, E3: { v: 'formulaColl' }, C9: { v: 'header_last' },
  C10: { v: 'ID_Товара' }, D10: { v: 'Поставщик' }, E10: { v: 'Цена' }, F10: { v: 'Почта' }, G10: { v: 'Комментарий' },
  E11: { f: "='5-3 Выбор'!M11", v: '100' }, D11: { v: 'ООО Альфа', bg: YELLOW }, F11: { v: 'secret@example.com', bg: RED },
  G11: { v: 'можно показать', bg: GREEN }, D12: { v: 'ООО Альфа', bg: YELLOW }, D13: { v: 'ООО Бета', bg: YELLOW },
  G12: { v: 'не размечено' }, G13: { v: 'Статус', dv: ['Да', 'Нет'] },
}, { frozenRows: 10, hidden: [6] });
const legend = makeSheet('Маска', {
  A1: { v: 'Цвет' }, B1: { v: 'Смысл' }, C1: { v: 'Тег' },
  A2: { bg: GREEN }, B2: { v: 'можно' }, A3: { bg: YELLOW }, B3: { v: 'тег' }, C3: { v: 'postavshchik' },
  A4: { bg: RED }, B4: { v: 'нельзя' },
});

const ctx = {
  PropertiesService: { getScriptProperties: () => ({ getProperty: (k) => ({ KEY: 'proba' })[k] || null }) },
  SpreadsheetApp: {
    getActiveSpreadsheet: () => ({ getName: () => 'Проба', getSheets: () => [data, legend],
                                   getSheetByName: (n) => [data, legend].find((s) => s.getName() === n) || null }),
    DataValidationCriteria: { VALUE_IN_RANGE: 'VALUE_IN_RANGE', VALUE_IN_LIST: 'VALUE_IN_LIST' },
  },
  ContentService: { createTextOutput: (t) => ({ setMimeType: () => t }), MimeType: { JSON: 'json' } },
};
vm.createContext(ctx);
vm.runInContext(fs.readFileSync(path.join(__dirname, 'Code.gs'), 'utf8'), ctx);

const fail = (m) => { process.stderr.write('proba: ' + m + '\n'); process.exit(1); };
if (JSON.parse(ctx.doGet({ parameter: { key: 'чужой' } })).oshibka === undefined) fail('чужой ключ пропущен');
const text = ctx.doGet({ parameter: { key: 'proba' } });
const out = JSON.parse(text);
for (const s of ['secret@example.com', 'ООО Альфа', 'ООО Бета', 'не размечено']) if (text.includes(s)) fail('утекло: ' + s);
const sh = out.listy[0];
const vals = Object.fromEntries(sh.znacheniya.map(([c, r, v]) => [c + r, v]));
if (vals.D11 !== vals.D12 || vals.D11 === vals.D13 || !/^\[\[postavshchik-\d+\]\]$/.test(vals.D11)) fail('теги не те: ' + JSON.stringify(vals));
if (vals.G11 !== 'можно показать') fail('«можно» не отдано');
if (sh.stroka_zagolovkov !== 10 || out.listy.length !== 1) fail('строка заголовков или лист легенды');
if (sh.maska.nelzya !== 1 || sh.maska.bez_razmetki !== 2) fail('счёт маски: ' + JSON.stringify(sh.maska));
process.stdout.write(text);
