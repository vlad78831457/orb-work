/**
 * orb-work: вебхук чтения таблицы — только чтение, ничего не пишет.
 *
 * Ставится в КОПИЮ таблицы (Расширения → Apps Script), разворачивается как веб-приложение.
 * Запрос: GET <адрес>?key=<ключ>[&list=<имя листа>]. Ключ — свойство скрипта KEY (ставит владелец копии).
 *
 * Отдаёт JSON (формат orb-veb-1) — устройство листов в том же виде, что import_listy.py берёт из xlsx:
 * размер, закрепление, скрытые столбцы, выпадающие списки, число правил условного форматирования и объединений,
 * формулы всех ячеек, значения — только служебных строк и строки заголовков. Ниже заголовков вместо значения — «•»
 * (ячейка заполнена), сами данные не отдаются.
 *
 * Маска (если в таблице есть лист легенды, имя — свойство MASK_LEGEND, по умолчанию «Маска»):
 *   на листе легенды со 2-й строки: A — ячейка, закрашенная цветом; B — смысл: «можно», «тег» или «нельзя»;
 *   C — имя тега (для «тег»). Ячейки данных, закрашенные цветом «можно», отдаются как есть; «тег» — вместо значения
 *   [[имя-N]] (одинаковые значения — один и тот же N, связь сохраняется, само значение — нет); «нельзя» и всё,
 *   что не размечено, — не отдаются.
 */

var FORMAT = 'orb-veb-1';
var PLACEHOLDER = '•';

function doGet(e) {
  var props = PropertiesService.getScriptProperties();
  var key = props.getProperty('KEY');
  var p = (e && e.parameter) || {};
  if (!key || p.key !== key) return json_({ oshibka: 'нет доступа' });
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var legendName = props.getProperty('MASK_LEGEND') || 'Маска';
  var legend = readLegend_(ss.getSheetByName(legendName));
  var sheets = ss.getSheets().filter(function (sh) {
    return sh.getName() !== legendName && (!p.list || sh.getName() === p.list);
  });
  var tags = {};
  return json_({
    format: FORMAT,
    tablica: ss.getName(),
    vremya: new Date().toISOString(),
    legenda: legend,
    listy: sheets.map(function (sh) { return readSheet_(sh, legend, tags); })
  });
}

function json_(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON);
}

function letter_(n) {
  var s = '';
  while (n > 0) { var m = (n - 1) % 26; s = String.fromCharCode(65 + m) + s; n = Math.floor((n - 1) / 26); }
  return s;
}

function readLegend_(sh) {
  if (!sh || sh.getLastRow() < 2) return [];
  var n = sh.getLastRow() - 1;
  var colors = sh.getRange(2, 1, n, 1).getBackgrounds();
  var vals = sh.getRange(2, 2, n, 2).getDisplayValues();
  var out = [];
  for (var i = 0; i < n; i++) {
    var smysl = String(vals[i][0]).trim().toLowerCase();
    if (['можно', 'тег', 'нельзя'].indexOf(smysl) < 0) continue;
    out.push({ cvet: String(colors[i][0]).toLowerCase(), smysl: smysl, teg: String(vals[i][1]).trim() });
  }
  return out;
}

/** Строка заголовков — как в import_listy.py: после header_last общего каркаса, иначе по закреплению. */
function headerRow_(values, frozenRows) {
  if (values.length && String(values[0][2]).trim() === 'header_first') {
    for (var r = 0; r < Math.min(values.length, 40); r++) {
      if (String(values[r][2]).trim() === 'header_last') return r + 2;
    }
    return 10;
  }
  return frozenRows > 0 ? frozenRows : 1;
}

function validationText_(dv) {
  if (!dv) return null;
  var t = dv.getCriteriaType(), a = dv.getCriteriaValues();
  if (t === SpreadsheetApp.DataValidationCriteria.VALUE_IN_RANGE && a[0]) {
    return "'" + a[0].getSheet().getName() + "'!" + a[0].getA1Notation();
  }
  if (t === SpreadsheetApp.DataValidationCriteria.VALUE_IN_LIST && a[0]) return '"' + a[0].join(',') + '"';
  return null;   // не список
}

function readSheet_(sh, legend, tags) {
  var rows = Math.max(1, sh.getLastRow()), cols = Math.max(1, sh.getLastColumn());
  var range = sh.getRange(1, 1, rows, cols);
  var values = range.getDisplayValues();
  var formulas = range.getFormulas();
  var head = headerRow_(values, sh.getFrozenRows());
  var cells = [];
  for (var r = 0; r < rows; r++) {
    for (var c = 0; c < cols; c++) {
      var f = formulas[r][c] ? formulas[r][c].replace(/^=/, '') : '';
      var v = values[r][c];
      if (!f && v === '') continue;
      cells.push([letter_(c + 1), r + 1, r + 1 <= head ? v : (f ? '' : PLACEHOLDER), f]);
    }
  }
  var hidden = [];
  for (var c2 = 1; c2 <= cols; c2++) if (sh.isColumnHiddenByUser(c2)) hidden.push(c2);
  var spiski = [], seen = {}, rules = {};
  var dvs = range.getDataValidations();
  for (var c3 = 0; c3 < cols; c3++) {
    for (var r3 = 0; r3 < rows; r3++) {
      var text = validationText_(dvs[r3][c3]);
      if (text === null) continue;
      rules[text] = true;
      if (!seen[c3]) { seen[c3] = true; spiski.push([letter_(c3 + 1) + (r3 + 1), text]); }
    }
  }
  var out = {
    list: sh.getName(),
    razmer: [rows, cols],
    zakrepleno: [sh.getFrozenRows(), sh.getFrozenColumns()],
    stroka_zagolovkov: head,
    skrytye: hidden,
    spiski: spiski,
    n_spiskov: Object.keys(rules).length,
    uslovnyh: sh.getConditionalFormatRules().length,
    obedineno: range.getMergedRanges().length,
    yacheyki: cells
  };
  if (legend.length) mask_(out, range, values, formulas, head, legend, tags);
  return out;
}

function mask_(out, range, values, formulas, head, legend, tags) {
  var byColor = {};
  legend.forEach(function (l) { byColor[l.cvet] = l; });
  var bg = range.getBackgrounds();
  var count = { mozhno: 0, teg: 0, nelzya: 0, bez_razmetki: 0 }, vals = [];
  for (var r = head; r < values.length; r++) {
    for (var c = 0; c < values[r].length; c++) {
      var v = values[r][c];
      if (v === '' || formulas[r][c]) continue;   // формулы и так отдаются, пустое — нечего
      var l = byColor[String(bg[r][c]).toLowerCase()];
      if (!l) { count.bez_razmetki++; continue; }
      if (l.smysl === 'нельзя') { count.nelzya++; continue; }
      if (l.smysl === 'можно') { count.mozhno++; vals.push([letter_(c + 1), r + 1, v]); continue; }
      var name = l.teg || 'teg';
      var t = tags[name] || (tags[name] = { n: 0, map: {} });
      if (!t.map[v]) t.map[v] = ++t.n;
      count.teg++;
      vals.push([letter_(c + 1), r + 1, '[[' + name + '-' + t.map[v] + ']]']);
    }
  }
  out.maska = count;
  out.znacheniya = vals;
}
