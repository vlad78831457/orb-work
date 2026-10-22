#!/usr/bin/env python3
"""Устройство листов таблиц (xlsx) → inst/src/md-kod/lis/<часть>/struktura.yaml: «как в таблице», руками не править.

    python3 inst/src/skripty/import_listy.py proekta=ФАЙЛ.xlsx oplat=ФАЙЛ.xlsx [--check] [--zagotovki]

Вместо xlsx можно дать JSON вебхука (tools/veb, `make veb-zabrat`): proekta=raw/veb/….json — устройство то же.

proekta / oplat — какая это таблица (имена листов в двух таблицах совпадают: «7 Договора» есть в обеих).
Какой лист — какая часть, задаёт реестр lis/listy.yaml (поле list — имя листа в выгрузке).
Берётся только устройство: служебные строки и строка заголовков, вид и списки столбцов, формулы, ссылки на листы.
**Значения строк данных не читаются** (в «чистой» таблице есть пример-данные). Почта, ссылки, ID таблиц, имена — заменяются.
--check      ничего не пишет: сверяет struktura.yaml с xlsx;
--zagotovki  кроме struktura.yaml, создаёт заготовки index.md и stolbtsy.yaml, если их ещё нет (существующее не трогает).
"""
import html
import json
import os
import re
import sys
import zipfile

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from import_reglament import clean as clean_text  # noqa: E402

LIS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'md-kod', 'lis')
LABELS = {'key': 'klyuch', 'var_name': 'var_name', 'var_value': 'var_value', 'hide_col': 'skryt', 'header_07': 'skryt',
          'header_08': 'header_08', 'header_last': 'primechanie'}
DUMMY = '__xludf.DUMMYFUNCTION("'
PHONE = re.compile(r'(?:\+7|(?<!\d)8)[\s(-]*\d{3}[\s)-]*\d{3}[\s-]*\d{2}[\s-]*\d{2}(?!\d)')
FIO = re.compile(r'(?<![А-Яа-яЁё])[А-ЯЁ][а-яё]+\s+[А-ЯЁ][а-яё]+\s+[А-ЯЁ][а-яё]+(?:вич|вна|ична|чна)(?![а-яё])')   # Фамилия Имя Отчество
LONG_ID = re.compile(r'(?<![A-Za-z0-9_-])[A-Za-z0-9_-]{30,}(?![A-Za-z0-9_-])')
QUOTED = re.compile(r"'((?:[^']|'')+)'!")
PLAIN = re.compile(r"(?<![A-Za-zА-Яа-яЁё0-9_.'\]\"])([A-Za-zА-Яа-яЁё_][A-Za-zА-Яа-яЁё0-9_.]*)!")
FORMULA_LIMIT = 1500


def clean(text):
    text = FIO.sub('[сотрудник]', PHONE.sub('[телефон]', clean_text(text or '')))
    return LONG_ID.sub('[id]', text)


def col_index(letters):
    n = 0
    for ch in letters:
        n = n * 26 + ord(ch) - 64
    return n


def col_letter(n):
    s = ''
    while n:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s


def unwrap(f):
    """Функции Google в выгрузке: IFERROR(__xludf.DUMMYFUNCTION("исходная формула"),посчитанное) → исходная формула."""
    out, i = [], 0
    while True:
        j = f.find(DUMMY, i)
        if j < 0:
            out.append(f[i:])
            return ''.join(out)
        k, buf = j + len(DUMMY), []
        while k < len(f):                       # строка формулы: кавычки внутри удвоены
            if f[k] == '"':
                if f[k + 1:k + 2] == '"':
                    buf.append('"')
                    k += 2
                    continue
                break
            buf.append(f[k])
            k += 1
        inner, k = ''.join(buf), k + 2          # за кавычкой — «)» самой DUMMYFUNCTION
        pre = f[i:j]
        if pre.endswith('IFERROR('):            # пропустить «,посчитанное)» до закрывающей скобки IFERROR
            depth, q = 1, False
            while k < len(f) and depth:
                c = f[k]
                if c == '"':
                    q = not q
                elif not q and c == '(':
                    depth += 1
                elif not q and c == ')':
                    depth -= 1
                k += 1
            out.append(pre[:-len('IFERROR(')] + inner)
        else:
            out.append(pre + '(' + inner + ')')
        i = k


class Book:
    def __init__(self, path):
        self.z = zipfile.ZipFile(path)
        n = self.z.namelist()
        ss = self.z.read('xl/sharedStrings.xml').decode() if 'xl/sharedStrings.xml' in n else ''
        self.strings = [html.unescape(''.join(re.findall(r'<t[^>]*>([^<]*)</t>', si))) for si in re.findall(r'<si>(.*?)</si>', ss, re.S)]
        wb = self.z.read('xl/workbook.xml').decode()
        rels = self.z.read('xl/_rels/workbook.xml.rels').decode()
        target = {re.search(r'Id="([^"]+)"', r).group(1): re.search(r'Target="([^"]+)"', r).group(1)
                  for r in re.findall(r'<Relationship [^>]*>', rels)}
        self.sheets = {}
        for name, rid in re.findall(r'<sheet [^>]*name="([^"]+)"[^>]*r:id="([^"]+)"', wb):
            t = target[rid].lstrip('/')
            self.sheets[html.unescape(name).strip()] = t if t.startswith('xl/') else 'xl/' + t

    def sheet(self, name):
        """Устройство одного листа: словарь для struktura.yaml."""
        return describe(name, self.model(name))

    def model(self, name):
        """Ячейки и свойства листа из xlsx — в том же виде, что отдаёт вебхук (tools/veb)."""
        x = self.z.read(self.sheets[name]).decode(errors='ignore')
        cells = {}   # (столбец, строка) → (значение, формула)
        for col, row, attrs, body in re.findall(r'<c r="([A-Z]+)(\d+)"([^>]*?)(?:/>|>(.*?)</c>)', x, re.S):
            body = body or ''
            fm = re.search(r'<f[^>]*>(.*?)</f>', body, re.S)
            shared = re.search(r'<f[^>]*/>', body)
            v = re.search(r'<v>(.*?)</v>', body, re.S)
            t = re.search(r'<is>.*?<t[^>]*>(.*?)</t>', body, re.S)
            val = v.group(1) if v else (t.group(1) if t else '')
            if 't="s"' in attrs and v:
                val = self.strings[int(val)]
            cells[(col, int(row))] = (html.unescape(val), html.unescape(fm.group(1)) if fm else ('' if not shared else None))
        pane = re.search(r'<pane [^>]*topLeftCell="([A-Z]+)(\d+)"', x)
        dim = re.search(r'<dimension ref="([^"]+)"', x)
        hidden = set()
        for lo, hi in ((int(a), int(b)) for a, b in re.findall(r'<col [^>]*min="(\d+)"[^>]*max="(\d+)"[^>]*hidden="1"', x)):
            hidden.update(range(lo, min(hi, lo + 500) + 1))
        dv = []
        for attrs, body in re.findall(r'<dataValidation ([^>]*)>(.*?)</dataValidation>', x, re.S):
            f1 = re.search(r'<formula1>(.*?)</formula1>', body, re.S)
            sq = re.search(r'sqref="([^"]+)"', attrs)
            if f1 and sq and 'type="list"' in attrs:
                dv.append((sq.group(1), html.unescape(f1.group(1))))
        return {'cells': cells, 'pane': (pane.group(1), int(pane.group(2))) if pane else None,
                'dim': dim.group(1) if dim else None, 'hidden': hidden, 'dv': dv,
                'n_dv': len(re.findall(r'<dataValidation ', x)), 'n_cond': len(re.findall(r'<conditionalFormatting ', x)),
                'n_merge': len(re.findall(r'<mergeCell ', x))}


class VebBook:
    """Таблица из JSON вебхука (tools/veb/Code.gs, формат orb-veb-1) — те же model() и sheet(), что у Book."""

    def __init__(self, path):
        data = json.load(open(path, encoding='utf-8'))
        if data.get('format') != 'orb-veb-1':
            sys.exit(f'{path}: не JSON вебхука orb-veb-1')
        self.sheets = {s['list'].strip(): s for s in data.get('listy', [])}

    def sheet(self, name):
        return describe(name, self.model(name))

    def model(self, name):
        s = self.sheets[name]
        fr, fc = (s.get('zakrepleno') or [0, 0])[:2]
        return {'cells': {(c, int(r)): (str(v), f) for c, r, v, f in s.get('yacheyki', [])},
                'pane': (col_letter(fc + 1), fr + 1) if fr or fc else None, 'dim': None,
                'hidden': set(s.get('skrytye', [])), 'dv': [tuple(x) for x in s.get('spiski', [])],
                'n_dv': s.get('n_spiskov', 0), 'n_cond': s.get('uslovnyh', 0), 'n_merge': s.get('obedineno', 0)}


def describe(name, m):
    """Устройство листа по ячейкам (из xlsx или вебхука): словарь для struktura.yaml."""
    cells, pane = m['cells'], m['pane']
    get = lambda c, r: (cells.get((c, r)) or ('', ''))[0].strip()
    frame = get('C', 1) == 'header_first'
    info = {'list': name}
    last_c = max((col_index(c) for c, _ in cells), default=1)
    last_r = max((r for _, r in cells), default=1)
    info['diapazon'] = m['dim'] or f'A1:{col_letter(last_c)}{last_r}'   # Google размер не пишет — тогда по занятым ячейкам
    info['zakrepleno'] = f'{pane[0]}{pane[1]}' if pane else ''
    info['karkas'] = frame
    labels = {}
    if frame:
        for r in range(1, 41):
            lab = get('C', r)
            if lab in LABELS:
                labels[LABELS[lab]] = r
            if lab == 'header_last':
                break
        head = labels.get('primechanie', 9) + 1
        labels['vid'] = labels.get('klyuch', 2) + 1
    else:
        head = pane[1] - 1 if pane and pane[1] > 1 else 1
        info['zagolovki_ugadany'] = True
    info['stroka_zagolovkov'] = head
    hidden = m['hidden']
    dv = {}
    for sqref, f1 in m['dv']:
        for part in sqref.split():
            mm = re.match(r'([A-Z]+)\d*(?::([A-Z]+)\d*)?', part)
            for n in range(col_index(mm.group(1)), col_index(mm.group(2) or mm.group(1)) + 1):
                dv.setdefault(col_letter(n), clean(f1))
    formulas = {}   # столбец → (строка, формула) — из строки заголовков или первая ниже
    counts, refs, values, external = {}, {}, 0, 0
    for (c, r), (val, fx) in sorted(cells.items(), key=lambda kv: (col_index(kv[0][0]), kv[0][1])):
        if fx != '':   # формула: текст или продолжение общей формулы (fx is None)
            counts[c] = counts.get(c, 0) + 1
            if fx:
                text = unwrap(fx)
                if c not in formulas and r >= head:   # формула столбца: в строке заголовков или первая ниже
                    formulas[c] = (r, text)
                external += text.upper().count('IMPORTRANGE')
                for ref in QUOTED.findall(text) + PLAIN.findall(text):
                    ref = ref.replace("''", "'")
                    if ref != name and not re.fullmatch(r'[A-Z]{1,3}\d*', ref):
                        refs[ref] = refs.get(ref, 0) + 1
        elif r > head and val != '':
            values += 1
    info['formul'] = sum(counts.values())
    info['znacheniy'] = values
    info['spiskov'] = m['n_dv']
    info['uslovnyh'] = m['n_cond']
    info['obedineno'] = m['n_merge']
    info['beryot'] = dict(sorted(refs.items(), key=lambda kv: -kv[1]))
    info['importrange'] = external
    letters = {c for (c, r) in cells if r <= head and get(c, r)} | set(formulas) | set(dv)
    if frame:
        letters |= {c for (c, r) in cells if r == labels.get('klyuch') and get(c, r)}
    cols = []
    for c in sorted(letters, key=col_index):
        e = {'bukva': c}
        h = get(c, head)
        if h:
            e['zagolovok'] = clean(h)
        for field in ('klyuch', 'vid', 'var_name', 'var_value', 'skryt', 'primechanie'):
            r = labels.get(field)
            if r and get(c, r) and not (c == 'C' and field != 'vid'):
                e[field] = clean(get(c, r))
        if col_index(c) in hidden:
            e['skryt_v_fayle'] = True
        if c in formulas:
            text = clean('=' + formulas[c][1])
            e['formula'] = text if len(text) <= FORMULA_LIMIT else text[:FORMULA_LIMIT] + ' …'
            e['formula_v_stroke'] = formulas[c][0]
            e['formul'] = counts.get(c, 0)
        if c in dv:
            e['spisok'] = dv[c]
        if len(e) > 1:
            cols.append(e)
    info['stolbtsy'] = cols
    return {k: v for k, v in info.items() if v not in ('', {}, [], None) or k in ('karkas', 'formul', 'znacheniy')}


def dump(data):
    return yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=100000, default_flow_style=False)


HEAD = ('# Сгенерировано: inst/src/skripty/import_listy.py из «{src}». Руками не править — описание листа в index.md\n'
        '# и stolbtsy.yaml рядом. Только устройство: служебные строки, заголовки, вид и списки столбцов, формулы, ссылки.\n')


def skeleton(e, info):
    title = e.get('title', e['list'])
    table = 'таблица проекта' if e['tablitsa'] == 'proekta' else 'внешняя таблица оплат'
    analog = f' · аналог: лист «{e["analog"]}»' if e.get('analog') else ''
    zachem = e.get('zachem')
    guess = ' Строка заголовков на этом листе угадана по закреплённой области — проверить.' if info.get('zagolovki_ugadany') else ''
    return f'''---
title: "Лист. {title}"
kratko: "{title}"
polno: "{(zachem or 'Назначение не записано.').replace('"', '«')}"
status: заглушка
nuzhno: []
---

# Лист «{title}»

Таблица: {table} · контур {e["kontur"]}{analog}.

**Зачем** (со слов): {zachem + '.' if zachem else '*не записано*.'}

Устройство листа — заголовки, вид столбцов, списки, формулы, связи с другими листами — собрано из таблицы ниже.{guess}

## Зачем лист — подробно

*Заполнить:* что на листе происходит, откуда приходят данные и куда уходят.

## Как заполнять

*Заполнить:* какие столбцы вводят руками, какие считаются сами. Что значит каждый столбец — в `stolbtsy.yaml` рядом (поля `chto` и `kak`).

## Что нельзя трогать

*Заполнить.*

## Инструкции и умения

*Заполнить:* какие инструкции и умения относятся к листу.

## Осталось сделать

- Заполнить разделы выше и `stolbtsy.yaml`.
'''


def columns_skeleton(e, info):
    rows = []
    seen = set()
    for c in info.get('stolbtsy', []):
        if not (c.get('zagolovok') or c.get('klyuch')):
            continue
        cid = c.get('klyuch') if c.get('klyuch') and c['klyuch'] not in seen else c['bukva']
        seen.add(cid)
        rows.append({'id': cid, 'bukva': c['bukva'], 'zagolovok': c.get('zagolovok', ''), 'chto': '', 'kak': ''})
    head = (f'# Столбцы листа «{e.get("title", e["list"])}»: что это (chto) и как заполняется (kak). Руками.\n'
            '# id — служебное имя столбца (строка 2) или буква; id со * или ? — шаблон: одно описание на повторяющийся блок\n'
            '# (сравнивается со служебным именем и заголовком). bukva и zagolovok — для ориентира, сборщик берёт их из struktura.yaml.\n')
    return head + dump(rows)


def main():
    args = sys.argv[1:]
    books = dict(a.split('=', 1) for a in args if '=' in a)
    if not books:
        sys.exit(__doc__)
    reg = yaml.safe_load(open(f'{LIS}/listy.yaml', encoding='utf-8'))
    stale = []
    for table, path in books.items():
        book, made = (VebBook(path) if path.endswith('.json') else Book(path)), 0
        want = [e for e in reg if e['tablitsa'] == table]
        missing = [e['list'] for e in want if e['list'] not in book.sheets]
        extra = [n for n in book.sheets if n not in {e['list'] for e in want}]
        if missing or extra:
            print(f'{table}: в реестре нет листов {extra}; в файле нет листов {missing}')
        for e in want:
            if e['list'] not in book.sheets:
                continue
            info = book.sheet(e['list'])
            text = HEAD.format(src=os.path.basename(path)) + dump(info)
            d = f'{LIS}/{e["chast"]}'
            path_s = f'{d}/struktura.yaml'
            if '--check' in args:
                if not os.path.isfile(path_s) or open(path_s, encoding='utf-8').read() != text:
                    stale.append(path_s)
                continue
            os.makedirs(d, exist_ok=True)
            open(path_s, 'w', encoding='utf-8').write(text)
            if '--zagotovki' in args:
                if not os.path.isfile(f'{d}/index.md'):
                    open(f'{d}/index.md', 'w', encoding='utf-8').write(skeleton(e, info))
                    made += 1
                if not os.path.isfile(f'{d}/stolbtsy.yaml'):
                    open(f'{d}/stolbtsy.yaml', 'w', encoding='utf-8').write(columns_skeleton(e, info))
        print(f'{table}: листов {len(want)}' + (f', новых заготовок {made}' if '--zagotovki' in args else ''))
    if stale:
        print('устарело: ' + ', '.join(os.path.relpath(s, LIS) for s in stale))
        sys.exit(1)


if __name__ == '__main__':
    main()
