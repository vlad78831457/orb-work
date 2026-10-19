"""Листы таблиц (раздел lis): устройство из struktura.yaml → разделы страницы листа, обзоры таблиц, карта листов.

В папке листа: struktura.yaml — «как в таблице» (делает import_listy.py, руками не править); stolbtsy.yaml — наше описание
столбцов (chto — что это, kak — как заполняется); index.md — текст. Какой лист — какая часть: lis/listy.yaml.
Страница листа — глубина 2 (lis/<часть>/index.md), отсюда ссылки «../…» и «../../…».
"""
import os
import re

import yaml

import protsessy

TABLES = {'proekta': 'таблица проекта', 'oplat': 'внешняя таблица оплат'}
OVERVIEW = {'proekta': 'tab-proekta', 'oplat': 'tab-oplat-vneshnyaya'}
FORMULA_SHOW = 400


def registry(src):
    path = f'{src}/md-kod/lis/listy.yaml'
    return yaml.safe_load(open(path, encoding='utf-8')) if os.path.isfile(path) else []


def attach(p):
    for name, key in (('struktura', 'struktura'), ('stolbtsy', 'stolbtsy')):
        path = f'{p["dir"]}/{name}.yaml'
        if os.path.isfile(path):
            p[key] = yaml.safe_load(open(path, encoding='utf-8')) or ({} if name == 'struktura' else [])


def by_sheet(reg_list):
    """(таблица, имя листа в выгрузке) → запись реестра."""
    return {(e['tablitsa'], e['list']): e for e in reg_list}


def entry_of(p, reg_list):
    return next((e for e in reg_list if e['chast'] == p['slug']), None)


def check(parts, reg_list):
    errors, notes = [], []
    seen = set()
    for e in reg_list:
        if e['chast'] in seen:
            errors.append(f'lis/listy.yaml: ключ части повторяется — {e["chast"]}')
        seen.add(e['chast'])
        p = parts.get(f'lis.{e["chast"]}')
        if not p:
            errors.append(f'lis/listy.yaml: у листа «{e["list"]}» нет части lis.{e["chast"]}')
        elif p.get('struktura') and p['struktura'].get('list') != e['list']:
            errors.append(f'lis.{e["chast"]}: struktura.yaml — от листа «{p["struktura"].get("list")}», а в реестре «{e["list"]}»')
    for p in parts.values():
        if p['sec'] == 'lis' and p.get('struktura') and p['slug'] not in seen:
            errors.append(f'{p["name"]}: лист не записан в lis/listy.yaml')
        if p['sec'] == 'lis' and p.get('struktura'):
            ids = {c.get('klyuch') for c in p['struktura'].get('stolbtsy', [])} | {c['bukva'] for c in p['struktura'].get('stolbtsy', [])}
            for c in p.get('stolbtsy') or []:
                if c.get('id') not in ids:
                    notes.append(f'{p["name"]}: в stolbtsy.yaml столбец «{c.get("id")}», которого нет в таблице')
    return errors, notes


def sheet_links(parts, reg_list):
    """Кто с какого листа берёт данные: часть → [(часть-источник или имя листа, число ссылок)], и обратно."""
    index = by_sheet(reg_list)
    takes, given = {}, {}
    for p in parts.values():
        st = p.get('struktura') if p['sec'] == 'lis' else None
        e = entry_of(p, reg_list) if st else None
        if not e:
            continue
        for name, n in (st.get('beryot') or {}).items():
            src = index.get((e['tablitsa'], name)) or next((x for x in reg_list if x['list'] == name), None)
            key = src['chast'] if src else None
            takes.setdefault(p['slug'], []).append((key, name, n))
            if key:
                given.setdefault(key, []).append((p['slug'], e['list'], n))
    return takes, given


def link_sheet(parts, slug, text=None):
    p = parts.get(f'lis.{slug}')
    return f'[{text or (p["short"] if p else slug)}](../{slug}/index.md)'


def code(formula):
    f = re.sub(r'\s+', ' ', str(formula)).strip()
    if len(f) > FORMULA_SHOW:
        f = f[:FORMULA_SHOW] + ' …'
    return '<code>' + f.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('|', '&#124;') + '</code>'


def how_filled(c):
    vid = c.get('vid', '')
    if vid in ('formulaColl', 'formulaCell') or (c.get('formula') and not vid):
        return 'формула'
    if vid == 'formulaFree':
        return 'руками, потом формула'
    if c.get('spisok'):
        return 'руками, из списка'
    return 'руками?'


def render_sheet(p, parts, reg, reg_list, links, places):
    st, e = p['struktura'], entry_of(p, reg_list)
    takes, given = links
    desc = {c['id']: c for c in p.get('stolbtsy') or [] if c.get('id')}
    out = ['\n## Устройство (из таблицы)\n']
    facts = [f'**Таблица:** {TABLES[e["tablitsa"]]}, лист «{e["list"]}»; контур {e["kontur"]}']
    if e.get('analog'):
        a = next((x for x in reg_list if x['list'] == e['analog'] and x['tablitsa'] == e['tablitsa']), None)
        facts.append('**Аналог в другом контуре:** ' + (link_sheet(parts, a['chast']) if a else f'«{e["analog"]}»'))
    for x in reg_list:   # обратная сторона аналога
        if x.get('analog') == e['list'] and x['tablitsa'] == e['tablitsa']:
            facts.append('**Аналог в другом контуре:** ' + link_sheet(parts, x['chast']))
    facts.append(f'**Размер:** `{st.get("diapazon", "?")}`' + (f', закреплено до `{st["zakrepleno"]}`' if st.get('zakrepleno') else ''))
    if st.get('karkas'):
        facts.append(f'**Каркас:** общий — служебные строки, заголовки в строке {st["stroka_zagolovkov"]} '
                     '([что значат служебные строки](../../zna/lis-sluzhebnye-stroki/index.md))')
    else:
        facts.append(f'**Каркас:** свой, не общий; строка заголовков — {st["stroka_zagolovkov"]}, угадана по закреплённой области — проверить')
    facts.append(f'**Формул:** {st.get("formul", 0)}; заполненных ячеек без формул в данных: {st.get("znacheniy", 0)}; '
                 f'списков: {st.get("spiskov", 0)}; условного форматирования: {st.get("uslovnyh", 0)}; объединённых ячеек: {st.get("obedineno", 0)}')
    if st.get('importrange'):
        facts.append(f'**Данные из других таблиц (IMPORTRANGE):** {st["importrange"]}')
    out += [f'- {f}' for f in facts] + ['']
    t, g = takes.get(p['slug'], []), given.get(p['slug'], [])
    if t or g:
        out.append('## Связи с другими листами\n')
        if t:
            out.append('- **Берёт данные с листов:** ' + ', '.join(
                (link_sheet(parts, k) if k else f'«{name}» *(листа нет в реестре)*') + f' ({n})' for k, name, n in t))
        if g:
            out.append('- **Его данные используют:** ' + ', '.join(link_sheet(parts, k) + f' ({n})' for k, _, n in g))
        out.append('\nВ скобках и на стрелках — сколько формул ссылаются.\n')
        out.append(neighbour_map(p, parts, reg_list, links))
    obys = places.get(p['name'], [])
    if obys:
        out += ['## Кто здесь работает (по процессам)\n',
                'Обязанности, у которых место работы — этот лист (из разбора регламента); должность — в карточке обязанности.\n',
                ', '.join(f'[{reg["oby"][o]["title"]}](../../reg/oby/{o}.md)' for o in obys) + '\n']
    cols = st.get('stolbtsy', [])
    if cols:
        out += ['## Столбцы\n',
                'Устройство — из таблицы; «Что это» и «Как заполняют» — из `stolbtsy.yaml` (заполняем руками).\n',
                '| Столбец | Заголовок | Служебное имя | Вид | Заполняется | Список | Что это | Как заполняют |',
                '|---|---|---|---|---|---|---|---|']
        for c in cols:
            d = desc.get(c.get('klyuch')) or desc.get(c['bukva']) or {}
            hide = ' *(скрыт)*' if c.get('skryt_v_fayle') or 'Скрыть' in c.get('skryt', '') else ''
            spisok = c.get('spisok', '')
            out.append(f'| {c["bukva"]}{hide} | {protsessy.cell(c.get("zagolovok", ""))} | {protsessy.cell(c.get("klyuch", ""))} | '
                       f'{c.get("vid", "")} | {how_filled(c)} | {protsessy.cell(spisok)[:120]} | {protsessy.cell(d.get("chto", ""))} | '
                       f'{protsessy.cell(d.get("kak", ""))} |')
        out.append('')
    var = [c for c in cols if c.get('var_name') or c.get('var_value')]
    if var:   # строки 5–6 общего каркаса: переменные листа (имя и значения), лежат в ячейках столбцов, но к ним не относятся
        out += ['## Переменные листа\n', 'Строки 5–6 каркаса (`var_name`, `var_value`): имя переменной и её значения — '
                'скорее всего, списки для скриптов и выпадающих списков.\n', '| Ячейка | Имя | Значения |', '|---|---|---|']
        out += [f'| {c["bukva"]} | {protsessy.cell(c.get("var_name", ""))} | {protsessy.cell(c.get("var_value", ""))} |' for c in var]
        out.append('')
    forms = [c for c in cols if c.get('formula')]
    if forms:
        out += [f'<details><summary>Формулы столбцов ({len(forms)})</summary>\n',
                '| Столбец | Строка | Формула |', '|---|---|---|']
        out += [f'| {c["bukva"]} | {c.get("formula_v_stroke", "")} | {code(c["formula"])} |' for c in forms]
        out += ['', '</details>\n']
    return '\n'.join(out)


def edges(reg_list, table, links):
    """Связи между листами одной таблицы: (откуда, куда, число формул)."""
    takes, _ = links
    rows = {e['chast']: e for e in reg_list if e['tablitsa'] == table}
    return [(k, e, n) for e in rows for k, _, n in takes.get(e, []) if k in rows and k != e], rows


def contour_map(reg_list, table, links):
    """Карта контуров: сколько связей «лист → лист» идёт из контура в контур."""
    es, rows = edges(reg_list, table, links)
    n = {}
    for a, b, _ in es:
        ka, kb = rows[a]['kontur'], rows[b]['kontur']
        if ka != kb:
            n[(ka, kb)] = n.get((ka, kb), 0) + 1
    out = ['flowchart LR']
    for k in sorted({e['kontur'] for e in rows.values()}):
        cnt = sum(1 for e in rows.values() if e['kontur'] == k)
        out.append(f'  {protsessy.nid("k", k)}(["контур {k}<br/>{cnt} листов"])')
    out += [f'  {protsessy.nid("k", a)} -->|"{c}"| {protsessy.nid("k", b)}' for (a, b), c in sorted(n.items())]
    return protsessy.fence(out)


def kontur_sheet_map(reg_list, table, links, k):
    """Листы контура k и связи между ними (связи с другими контурами — на карте контуров и на страницах листов)."""
    es, rows = edges(reg_list, table, links)
    mine = [e for e in rows.values() if e['kontur'] == k]
    inner = [(a, b) for a, b, _ in es if rows[a]['kontur'] == k and rows[b]['kontur'] == k]
    if not inner:
        return ''
    out = ['flowchart LR']
    out += [f'  {protsessy.nid("s", e["chast"])}["{protsessy.label(e.get("title", e["list"]), 22)}"]' for e in mine
            if any(e['chast'] in pair for pair in inner)]
    out += [f'  {protsessy.nid("s", a)} --> {protsessy.nid("s", b)}' for a, b in dict.fromkeys(inner)]
    return protsessy.fence(out)


def neighbour_map(p, parts, reg_list, links):
    """Соседи листа: откуда берёт данные и кто использует его данные."""
    takes, given = links
    t = [(k, n) for k, _, n in takes.get(p['slug'], []) if k and k != p['slug']]
    g = [(k, n) for k, _, n in given.get(p['slug'], []) if k != p['slug']]
    if not t and not g:
        return ''
    name = lambda k: protsessy.label((parts.get(f'lis.{k}') or {}).get('short', k), 22)
    out = ['flowchart LR', f'  {protsessy.nid("s", p["slug"])}["{name(p["slug"])}"]',
           f'  style {protsessy.nid("s", p["slug"])} stroke-width:3px']
    for k in dict.fromkeys([k for k, _ in t] + [k for k, _ in g]):
        out.append(f'  {protsessy.nid("s", k)}["{name(k)}"]')
    out += [f'  {protsessy.nid("s", k)} -->|"{n}"| {protsessy.nid("s", p["slug"])}' for k, n in t]
    out += [f'  {protsessy.nid("s", p["slug"])} -->|"{n}"| {protsessy.nid("s", k)}' for k, n in g]
    return protsessy.fence(out)


def render_tab(p, parts, reg_list, links):
    table = next(t for t, slug in OVERVIEW.items() if slug == p['slug'])
    rows = [e for e in reg_list if e['tablitsa'] == table]
    out = [f'\n## Листы по контурам\n',
           'Зачем — со слов директора; устройство — из таблицы; у каждого листа своя страница-заготовка.\n']
    for k in dict.fromkeys(e['kontur'] for e in rows):
        out += [f'### Контур {k}\n', '| Лист | Зачем | Каркас | Столбцов | Формул | Описание |', '|---|---|---|---|---|---|']
        for e in [x for x in rows if x['kontur'] == k]:
            q = parts.get(f'lis.{e["chast"]}')
            st = (q or {}).get('struktura') or {}
            filled = sum(1 for c in (q or {}).get('stolbtsy') or [] if c.get('chto'))
            state = (q or {}).get('status', '—')
            out.append(f'| {link_sheet(parts, e["chast"], e.get("title", e["list"]))} | {protsessy.cell(e.get("zachem", "—"))} | '
                       f'{"общий" if st.get("karkas") else "свой"} | {len(st.get("stolbtsy", []))} | {st.get("formul", 0)} | '
                       f'{state}{f", столбцов описано {filled}" if filled else ""} |')
        out.append('')
    out += ['## Карта контуров\n', 'Сколько связей «лист берёт данные с листа» (по ссылкам в формулах) идёт из контура в контур.\n',
            contour_map(reg_list, table, links), '## Карты листов по контурам\n',
            'Листы контура и связи между ними: стрелка — данные идут с листа на лист. Листы без связей внутри контура '
            'не показаны; связи с другими контурами — на карте контуров и на странице каждого листа.\n']
    for k in dict.fromkeys(e['kontur'] for e in rows):
        m = kontur_sheet_map(reg_list, table, links, k)
        out += [f'### Контур {k}\n', m or 'Связей между листами внутри контура нет.\n']
    return '\n'.join(out)
