"""Процессы (раздел pro): данные шагов → проверки, диаграммы Mermaid, таблицы и карточки ролей и обязанностей.

В папке процесса: reglament.yaml — шаги «как записано» (делает import_reglament.py, руками не править);
protsess.yaml — наше толкование: какая обязанность делает шаг, кто ставит, кто принимает, где работают.
Обязанности — reg/oby.yaml, должности — reg/rol.yaml, места — reg/mes.yaml.
Ссылки строятся от страницы глубины 2 (pro/<процесс>/index.md, reg/rol/<ключ>.md) — префикс ROOT.
"""
import os
import re

import yaml

ROOT = '../../'
RELS = (('stavit', 'ставит задачу'), ('prinimaet', 'принимает результат'), ('otslezhivaet', 'отслеживает'),
        ('soglasuyut', 'согласуют'), ('pomogayut', 'помогают'), ('uznayut', 'узнают о результате'))
PEOPLE = ('pomogayut', 'uznayut')   # здесь — должности «rol.ключ» (люди из столбцов регламента), в остальных связях — обязанности
COLUMNS = {'H': 'Менеджер', 'I': 'ТС (эксперт)', 'J': 'Закупщик', 'K': 'K', 'L': 'АС', 'M': 'M', 'N': 'Владелец процесса'}
MARK = (('исполнитель', 'И'), ('владелец', 'В'), ('согласование', 'Сг'), ('информируем', 'У'), ('соисполнител', 'С'))
STATUS_OBJ = {'proekt': 'Статус проекта', 'sdelka': 'Статус сделки', 'tovar': 'Статус товара'}
SHAPE = {'лист': ('[/"', '"/]'), 'таблица': ('[/"', '"/]'), 'битрикс': ('{{"', '"}}'), '1с': ('[("', '")]'),
         'диск': ('[["', '"]]'), 'почта': ('>"', '"]'), 'эдо': ('>"', '"]'), 'внешнее': ('>"', '"]')}


# ---------- данные ----------

def attach(p, errors):
    """Подгрузить к части процесса её reglament.yaml и protsess.yaml."""
    p['shagi'], p['tolk'], p['dalee'], p['kontur'] = [], {}, [], ''
    for name in ('reglament', 'protsess'):
        path = f'{p["dir"]}/{name}.yaml'
        if not os.path.isfile(path):
            errors.append(f'{p["name"]}: нет {name}.yaml')
            continue
        d = yaml.safe_load(open(path, encoding='utf-8')) or {}
        if name == 'reglament':
            p['shagi'], p['reglament_title'] = d.get('shagi') or [], d.get('process', '')
        else:
            p['tolk'], p['dalee'], p['kontur'] = d.get('shagi') or {}, d.get('dalee') or [], str(d.get('kontur', ''))


def procs(parts):
    return [p for p in parts.values() if p['sec'] == 'pro' and p.get('shagi')]


def doer(t):
    """Обязанность-исполнитель шага; не строка (список, пусто) — None: ошибку называет check()."""
    d = (t or {}).get('delaet')
    return d if isinstance(d, str) and d else None


def as_list(v):
    return [] if v is None else v if isinstance(v, list) else [v]


def col_name(c):
    """Подпись столбца регламента: K и M подписаны именами — у нас только буква."""
    return f'столбец {c}' if COLUMNS[c] == c else f'{c} {COLUMNS[c]}'


def ref_kind(v):
    """Значение связи: «rol.ключ» — должность, иначе обязанность."""
    return ('rol', v[4:]) if v.startswith('rol.') else ('oby', v)


def mark(text):
    t = text.lower()
    for word, short in MARK:
        if word in t and not (short == 'И' and 'соисполнител' in t and ':' in t):
            return short if not (short == 'И' and t.startswith('соисполнитель')) else 'С'
    return '?'


def executors(step):
    """Столбцы регламента с основным исполнителем шага."""
    return [c for c, m in (step.get('kolonki') or {}).items() if m.split(':')[0] == 'исполнитель']


def index(parts, reg):
    """Обязанность → [(процесс, шаг, отношение)]; должность → то же для прямых ссылок «rol.»; место → обязанности."""
    by_oby, by_rol, places = {}, {}, {}
    for p in procs(parts):
        for s in p['shagi']:
            t = p['tolk'].get(s['id']) or {}
            rels = [('delaet', doer(t))] + [(r, v) for r, _ in RELS for v in as_list(t.get(r))]
            for rel, v in rels:
                if not isinstance(v, str) or not v:
                    continue
                kind, key = ref_kind(v)
                (by_oby if kind == 'oby' else by_rol).setdefault(key, []).append((p, s, rel))
            for m in as_list(t.get('mesto')):
                if doer(t):
                    places.setdefault(m, [])
                    if doer(t) not in places[m]:
                        places[m].append(doer(t))
    for k, o in reg.get('oby', {}).items():   # места обязанностей без шагов
        for m in as_list(o.get('gde')):
            places.setdefault(m, [])
            if k not in places[m]:
                places[m].append(k)
    return by_oby, by_rol, places


# ---------- проверки ----------

def check(parts, reg):
    errors, notes = [], []   # notes — расхождения и вопросы: на отдельную страницу, не в консоль
    prepare(parts, reg)
    oby, rol, mes = reg.get('oby', {}), reg.get('rol', {}), reg.get('mes', {})
    for p in procs(parts):
        ids = [s['id'] for s in p['shagi']]
        for s in p['shagi']:
            t = p['tolk'].get(s['id'])
            where = f'{p["name"]} {s["id"]}'
            if t is None:
                errors.append(f'{where}: шаг регламента не разобран в protsess.yaml')
                continue
            d = t.get('delaet')
            if not isinstance(d, str) or not d:
                errors.append(f'{where}: delaet — ровно одна обязанность')
                continue
            if d not in oby:
                errors.append(f'{where}: в delaet нет такой обязанности — {d}')
                continue
            for r, _ in RELS:
                for v in as_list(t.get(r)):
                    if not isinstance(v, str):
                        errors.append(f'{where}: в {r} — не имя: {v}')
                        continue
                    kind, key = ref_kind(v)
                    if (kind == 'rol') != (r in PEOPLE):
                        errors.append(f'{where}: в {r} — {"должности «rol.ключ»" if r in PEOPLE else "обязанности, не должности"}: {v}')
                    elif key not in (oby if kind == 'oby' else rol):
                        errors.append(f'{where}: в {r} нет такой {"должности" if kind == "rol" else "обязанности"} — {v}')
            for m in as_list(t.get('mesto')):
                if m not in mes:
                    errors.append(f'{where}: в mesto нет такого места — {m}')
            for a in as_list(t.get('peredaet')):
                if a not in reg.get('art', {}):
                    errors.append(f'{where}: в peredaet нет такого предмета — {a}')
            ex = executors(s)
            assumed = as_list(oby[d].get('predpolagaem'))
            cols = {c for r in assumed if r in rol for c in as_list(rol[r].get('kolonka'))}
            if not ex:
                notes.append((p, s, f'в регламенте у шага нет исполнителя; толкуем как «{oby[d]["title"]}»'))
            elif cols and not set(ex) & cols:
                notes.append((p, s, f'в регламенте делает {", ".join(col_name(c) for c in ex)}, '
                                    f'а «{oby[d]["title"]}» мы предполагаем за {", ".join(rol[r]["title"] for r in assumed)}'))
            if len(ex) > 1:
                notes.append((p, s, f'в регламенте несколько основных исполнителей: {", ".join(col_name(c) for c in ex)}'))
        for extra in set(p['tolk']) - set(ids):
            errors.append(f'{p["name"]}: в protsess.yaml шаг, которого нет в регламенте — {extra}')
        for n in p['dalee']:
            if f'pro.{n}' not in parts:
                errors.append(f'{p["name"]}: в dalee нет такого процесса — {n}')
    used = {key for p in procs(parts) for t in p['tolk'].values()   # обязанность участвует хоть в одном шаге
            for v in [doer(t)] + [x for r, _ in RELS for x in as_list(t.get(r))] if isinstance(v, str) and v
            for kind, key in [ref_kind(v)] if kind == 'oby'}
    for k, o in oby.items():
        for r in as_list(o.get('predpolagaem')):
            if r not in rol:
                errors.append(f'oby.{k}: в predpolagaem нет такой должности — {r}')
        for m in as_list(o.get('gde')):
            if m not in mes:
                errors.append(f'oby.{k}: в gde нет такого места — {m}')
        if not as_list(o.get('predpolagaem')):
            notes.append((None, k, 'не знаем, какая должность выполняет'))
        elif len(as_list(o.get('predpolagaem'))) > 1:
            notes.append((None, k, 'предполагаем несколько должностей — нарушает «один ответственный»'))
        if k not in used and not o.get('gde'):
            notes.append((None, k, 'не участвует ни в одном шаге и места работы не заданы'))
    if not errors:   # переходы к другой должности без предмета передачи — вопрос
        for p in procs(parts):
            for i, s in enumerate(p['shagi']):
                src, r = handoff(p, i, reg)
                if src and not incoming(p, i, reg):
                    notes.append((p, s, f'работа переходит от «{pos_title(reg, src)}» к «{pos_title(reg, r)}», '
                                        'но что передаётся — не записано'))
        given = {a for p in procs(parts) for t in p['tolk'].values() for a in as_list(t.get('peredaet'))}
        for a in reg.get('art', {}):
            if a not in given:
                notes.append((None, a, 'предмет передачи не используется ни в одном шаге'))
    for k, a in reg.get('art', {}).items():
        if a.get('gde') and a['gde'] not in mes:
            errors.append(f'art.{k}: в gde нет такого места — {a["gde"]}')
    for k, m in mes.items():
        if m.get('chast') and m['chast'] not in parts:
            errors.append(f'mes.{k}: в chast нет такой части — {m["chast"]}')
    return errors, notes


# ---------- Mermaid ----------

def label(text, width=26, limit=70):
    text = re.sub(r'\s+', ' ', str(text)).strip()
    if len(text) > limit:
        text = text[:limit - 1].rstrip() + '…'
    words, lines, cur = text.split(' '), [], ''
    for w in words:
        if cur and len(cur) + 1 + len(w) > width:
            lines.append(cur)
            cur = w
        else:
            cur = f'{cur} {w}'.strip()
    lines.append(cur)
    esc = lambda s: s.replace('#', '#35;').replace('"', '#quot;').replace('<', '#lt;').replace('>', '#gt;')
    return '<br/>'.join(esc(l) for l in lines)


def nid(prefix, key):
    return prefix + '_' + re.sub(r'[^A-Za-z0-9]', '_', key)


def fence(lines):
    return '```mermaid\n' + '\n'.join(lines) + '\n```\n'


def step_name(s):
    return f'{s["nomer"]}. {s["title"]}' if s['nomer'] else s['title']


def diagram_reglament(p):
    """Как в регламенте: дорожки по столбцам с исполнителем, шаги по порядку."""
    lanes = {}
    for s in p['shagi']:
        ex = executors(s)
        lanes.setdefault(ex[0] if ex else '-', []).append(s)
    out = ['flowchart TB']
    for col in list(COLUMNS) + ['-']:
        if col not in lanes:
            continue
        title = 'нет исполнителя' if col == '-' else col_name(col)
        out.append(f'  subgraph {nid("c", col if col != "-" else "none")}["{label(title)}"]')
        for s in lanes[col]:
            ex = executors(s)
            extra = f' (+ {", ".join(ex[1:])})' if len(ex) > 1 else ''
            out.append(f'    {nid("s", s["id"])}["{label(step_name(s) + extra)}"]')
        out.append('  end')
    for a, b in zip(p['shagi'], p['shagi'][1:]):
        out.append(f'  {nid("s", a["id"])} --> {nid("s", b["id"])}')
    none = [nid('s', s['id']) for s in lanes.get('-', [])]
    if none:
        out += ['  classDef none stroke-dasharray: 5 5', f'  class {",".join(none)} none']
    return fence(out)


def diagram_oby(p, reg):
    """По обязанностям: дорожки — должности, которые предполагаем; стрелки — ставит, сдаёт, следит, согласует."""
    oby, rol = reg['oby'], reg['rol']
    order, edges = [], []
    for s in p['shagi']:
        t = p['tolk'][s['id']]
        d = t['delaet']
        if d not in order:
            order.append(d)
        for v in as_list(t.get('stavit')):
            if not v.startswith('rol.'):
                edges.append((v, d, 'ставит', '-->'))
                order.append(v) if v not in order else None
        for v in as_list(t.get('prinimaet')):
            if not v.startswith('rol.'):
                what = art_names(reg, as_list(t.get('peredaet')))
                edges.append((d, v, label(what, 24, 50) if what else 'передаёт', '-->'))
                order.append(v) if v not in order else None
        for r, word in (('otslezhivaet', 'следит'), ('soglasuyut', 'согласует')):
            for v in as_list(t.get(r)):
                if not v.startswith('rol.'):
                    a, b = (d, v) if r == 'otslezhivaet' else (v, d)
                    edges.append((a, b, word, '-.->'))
                    order.append(v) if v not in order else None
    seq = []
    for a, b in zip(p['shagi'], p['shagi'][1:]):
        x, y = p['tolk'][a['id']]['delaet'], p['tolk'][b['id']]['delaet']
        if x != y and not any({e[0], e[1]} == {x, y} for e in edges) and (x, y) not in seq:
            seq.append((x, y))
    lanes = {}
    for k in order:
        lanes.setdefault((as_list(oby[k].get('predpolagaem')) or ['-'])[0], []).append(k)
    out = ['flowchart TB']
    for r, ks in lanes.items():
        out.append(f'  subgraph {nid("r", r if r != "-" else "none")}["{label(short_rol(rol, r))}"]')
        out += [f'    {nid("o", k)}("{label(oby[k]["title"])}")' for k in ks]
        out.append('  end')
    seen = set()   # одна стрелка на пару: «ставит» и «передаёт» между теми же двумя — одна передача задачи
    for a, b, word, arrow in sorted(edges, key=lambda e: e[2] != 'ставит'):
        if (a, b, arrow) not in seen:
            seen.add((a, b, arrow))
            out.append(f'  {nid("o", a)} {arrow}|"{word}"| {nid("o", b)}')   # в кавычках: скобки в подписи ломают схему
    out += [f'  {nid("o", a)} --> {nid("o", b)}' for a, b in seq]
    return fence(out)


def short_rol(rol, r):
    """Название должности для дорожки: без пояснения в скобках — длинное Mermaid обрезает."""
    return re.sub(r'\s*\(.*?\)', '', rol[r]['title']) if r in rol else 'не знаем кто'


def place_node(key, m):
    l, r = SHAPE.get(m.get('vid'), ('["', '"]'))
    return f'{nid("m", key)}{l}{label(m["title"])}{r}'


def diagram_places(p, reg):
    oby, mes = reg['oby'], reg['mes']
    pairs = []
    for s in p['shagi']:
        t = p['tolk'][s['id']]
        for m in as_list(t.get('mesto')):
            if (t['delaet'], m) not in pairs:
                pairs.append((t['delaet'], m))
    if not pairs:
        return ''
    out = ['flowchart LR']
    for k in dict.fromkeys(a for a, _ in pairs):
        out.append(f'  {nid("o", k)}("{label(oby[k]["title"])}")')
    for vid in dict.fromkeys(mes[m].get('vid', '') for _, m in pairs):
        out.append(f'  subgraph {nid("v", vid or "x")}["{label(vid or "место")}"]')
        out += ['    ' + place_node(m, mes[m]) for m in dict.fromkeys(m for _, m in pairs) if mes[m].get('vid', '') == vid]
        out.append('  end')
    out += [f'  {nid("o", a)} --> {nid("m", m)}' for a, m in pairs]
    return fence(out)


def statuses(seq):
    """[(объект, статус, шаг)] по порядку → stateDiagram по каждому объекту."""
    blocks = []
    for obj in dict.fromkeys(o for o, _, _ in seq):
        chain = [(st, sid) for o, st, sid in seq if o == obj]
        names = {st: f'st{i}' for i, st in enumerate(dict.fromkeys(st for st, _ in chain))}
        out = ['stateDiagram-v2', f'  direction LR']
        out += [f'  state "{label(st, 40)}" as {n}' for st, n in names.items()]
        out.append(f'  [*] --> {names[chain[0][0]]}')
        seen = set()
        for (a, _), (b, sid) in zip(chain, chain[1:]):
            if a != b and (a, b) not in seen:
                seen.add((a, b))
                out.append(f'  {names[a]} --> {names[b]} : {sid}')
        blocks.append(f'**{STATUS_OBJ.get(obj, obj)}**\n\n' + fence(out))
    return '\n'.join(blocks)


def status_seq(plist):
    """[(объект, статус, подпись шага «процесс №»)] по порядку процессов и шагов."""
    return [(o, st, f'{p["short"]} {s["nomer"] or s["id"]}') for p in plist for s in p['shagi']
            for o, st in ((p['tolk'].get(s['id']) or {}).get('status') or {}).items()]


# ---------- страницы ----------

def link_oby(reg, k):
    return f'[{reg["oby"][k]["title"]}]({ROOT}reg/oby/{k}.md)'


def link_rol(reg, k):
    return f'[{reg["rol"][k]["title"]}]({ROOT}reg/rol/{k}.md)'


def link_ref(reg, v):
    kind, key = ref_kind(v)
    return link_rol(reg, key) if kind == 'rol' else link_oby(reg, key)


def link_mes(reg, k):
    return f'[{reg["mes"][k]["title"]}]({ROOT}reg/mes.md#{k})'


def link_proc(p):
    return f'[{p["title"]}]({ROOT}pro/{p["slug"]}/index.md)'


def cell(text):
    return re.sub(r'\s+', ' ', str(text)).replace('|', '\\|').strip()


def raci(p):
    cols = [c for c in COLUMNS if any(c in (s.get('kolonki') or {}) for s in p['shagi'])]
    out = ['| № | Шаг | ' + ' | '.join(col_name(c) for c in cols) + ' |', '|---|---|' + '---|' * len(cols)]
    for s in p['shagi']:
        k = s.get('kolonki') or {}
        out.append(f'| {s["nomer"] or "—"} | {cell(s["title"])} | ' + ' | '.join(mark(k[c]) if c in k else '' for c in cols) + ' |')
    return '\n'.join(out) + '\n\nИ — исполнитель, С — соисполнитель, Сг — согласование, У — информируемый, В — владелец процесса.\n'


def steps_table(p, reg):
    out = ['| № | Шаг | Делает | Ставит → принимает | Передаёт | Согласуют, помогают, узнают | Где |', '|---|---|---|---|---|---|---|']
    for s in p['shagi']:
        t = p['tolk'][s['id']]
        flow = ', '.join(link_ref(reg, v) for v in as_list(t.get('stavit'))) or '—'
        flow += ' → ' + (', '.join(link_ref(reg, v) for v in as_list(t.get('prinimaet'))) or '—')
        side = '; '.join(f'{word}: ' + ', '.join(link_ref(reg, v) for v in as_list(t.get(r)))
                         for r, word in RELS[2:] if t.get(r))
        where = ', '.join(link_mes(reg, m) for m in as_list(t.get('mesto')))
        note = f'<br/>*{cell(t["dogadka"])}*' if t.get('dogadka') else ''
        arts = ', '.join(f'[{reg["art"][a]["title"]}]({ROOT}reg/art.md#{a})' for a in as_list(t.get('peredaet')))
        out.append(f'| {s["nomer"] or "—"} | {cell(s["title"])}{note} | {link_oby(reg, t["delaet"])} | {flow} | {arts} | {side} | {where} |')
    return '\n'.join(out) + '\n'


def render_process(p, reg, parts):
    """Собранная часть процесса: после текста части — схемы и таблицы."""
    out = ['## Дорожки по должностям\n',
           'Вертикальная дорожка — должность, которую мы предполагаем; заметка — шаг в её дорожке; стрелка — работа переходит '
           'к другой должности (ставит задачу или делает следующий шаг).\n',
           seq_process(p, reg),
           '## Как в регламенте\n',
             'Дорожки — столбцы регламента с основным исполнителем; шаги — по порядку. Пунктир — шаг без исполнителя.\n',
             diagram_reglament(p), raci(p),
             '## По обязанностям\n',
             'Дорожки — должности, которые мы предполагаем; узлы — обязанности. Сплошная стрелка — ставит задачу или передаёт результат, '
             'пунктир — следит или согласует; стрелка без подписи — дальше по порядку.\n',
             diagram_oby(p, reg),
             '## Шаги и обязанности\n', steps_table(p, reg)]
    places = diagram_places(p, reg)
    if places:
        out += ['## Где работают\n', places]
    st = status_seq([p])
    if st:
        out += ['## Статусы\n', statuses(st)]
    if p['dalee']:
        out.append('Дальше: ' + ', '.join(f'[{parts["pro." + x]["title"]}](../{x}/index.md)' for x in p['dalee']) + '.\n')
    return '\n' + '\n'.join(out)


def process_map(parts):
    plist = procs(parts)
    out = ['flowchart LR']
    for k in dict.fromkeys(p['kontur'] for p in plist):
        out.append(f'  subgraph {nid("k", k or "x")}["контур {k}"]')
        out += [f'    {nid("p", p["slug"])}["{label(p["title"])}"]' for p in plist if p['kontur'] == k]
        out.append('  end')
    for p in plist:
        out += [f'  {nid("p", p["slug"])} --> {nid("p", n)}' for n in p['dalee']]
    return fence(out)


def render_obzor(parts, reg, notes):
    """Сводная страница процессов: карта, статусы через все процессы, расхождения."""
    plist = procs(parts)
    out = ['\n## Карта процессов\n', process_map(parts),
           '| Процесс | Контур | Шагов | Обязанностей |', '|---|---|---|---|']
    for p in plist:
        n = len({t['delaet'] for t in p['tolk'].values()})
        out.append(f'| {link_proc(p)} | {p["kontur"]} | {len(p["shagi"])} | {n} |')
    out += ['', '## Статусы через все процессы\n', statuses(status_seq(plist)),
            '## Расхождения и вопросы\n',
            'Собраны сборщиком: где регламент и наше толкование расходятся, где нет исполнителя, '
            'где нарушено «одна обязанность — один ответственный».\n',
            '| Где | Что |', '|---|---|']
    groups = {}   # одинаковое замечание по нескольким шагам процесса — одной строкой
    for p, s, text in notes:
        groups.setdefault((p['name'] if p else f'oby.{s}', text), []).append((p, s))
    for (_, text), items in groups.items():
        p = items[0][0]
        if p:
            nums = ', '.join(s['nomer'] or f'«{s["title"]}»' for _, s in items)
            where = f'{link_proc(p)}, {"шаги" if len(items) > 1 else "шаг"} {nums}'
        else:
            where = link_oby(reg, items[0][1])
        out.append(f'| {where} | {cell(text)} |')
    return '\n'.join(out) + '\n'


def card_oby(k, reg, by_oby):
    o, rol = reg['oby'][k], reg['rol']
    rows = by_oby.get(k, [])
    out = [f'# {o["title"]}\n', f'{o["polno"]}\n',
           '- **Обязанность:** одна, один ответственный. Ключ: `' + k + '`',
           '- **Предполагаем, что выполняет:** ' + (', '.join(link_rol(reg, r) for r in as_list(o.get('predpolagaem'))) or '*не знаем*')]
    for f, title in (('kontur', 'Контур'), ('istochnik', 'Источник'), ('pochemu', 'Почему выделили'), ('dogadka', 'Догадка, не подтверждено')):
        if o.get(f):
            out.append(f'- **{title}:** ' + ('; '.join(map(str, o[f])) if isinstance(o[f], list) else str(o[f])))
    if o.get('status') == 'проверить':
        out.append('- *Черновик — проверить.*')
    out.append('')
    inc = sorted({v for p, s, rel in rows if rel == 'delaet' for v in as_list(p['tolk'][s['id']].get('stavit'))})
    outg = sorted({v for p, s, rel in rows if rel == 'delaet' for v in as_list(p['tolk'][s['id']].get('prinimaet'))})
    who_sets = sorted({p['tolk'][s['id']]['delaet'] for p, s, rel in rows if rel == 'prinimaet'})
    who_gives = sorted({p['tolk'][s['id']]['delaet'] for p, s, rel in rows if rel == 'stavit'})
    inc = list(dict.fromkeys(inc + who_sets)); outg = list(dict.fromkeys(outg + who_gives))
    if inc or outg:
        g = ['flowchart LR', f'  {nid("o", k)}("{label(o["title"])}")', f'  style {nid("o", k)} stroke-width:3px']
        for v in inc + outg:
            kind, key = ref_kind(v)
            t = (rol if kind == 'rol' else reg['oby'])[key]['title']
            g.append(f'  {nid(kind[0], key)}("{label(t)}")')
        g += [f'  {nid(ref_kind(v)[0][0], ref_kind(v)[1])} -->|ставит| {nid("o", k)}' for v in inc]
        g += [f'  {nid("o", k)} -->|передаёт| {nid(ref_kind(v)[0][0], ref_kind(v)[1])}' for v in outg]
        out += ['## Откуда задача и кому результат\n', fence(g)]
    if rows:
        word = dict(RELS, delaet='делает')
        out += ['## Шаги\n', '| Процесс | № | Шаг | Здесь |', '|---|---|---|---|']
        out += [f'| {link_proc(p)} | {s["nomer"] or "—"} | {cell(s["title"])} | {word[rel]} |' for p, s, rel in rows]
        gives = list(dict.fromkeys(a for p, s, rel in rows if rel == 'delaet' for a in as_list(p['tolk'][s['id']].get('peredaet'))))
        gets = list(dict.fromkeys(a for p, s, rel in rows if rel == 'delaet' for a in incoming(p, p['shagi'].index(s), reg)))
        link_art = lambda a: f'[{reg["art"][a]["title"]}]({ROOT}reg/art.md#{a})'
        if gets:
            out += ['', '**Получает:** ' + ', '.join(link_art(a) for a in gets)]
        if gives:
            out += ['', '**Отдаёт:** ' + ', '.join(link_art(a) for a in gives)]
        places = list(dict.fromkeys(m for p, s, rel in rows if rel == 'delaet' for m in as_list(p['tolk'][s['id']].get('mesto'))))
        places += [m for m in as_list(o.get('gde')) if m not in places]
        if places:
            out += ['', '**Где работает:** ' + ', '.join(link_mes(reg, m) for m in places)]
    elif o.get('gde'):
        out += ['**Где работает:** ' + ', '.join(link_mes(reg, m) for m in as_list(o['gde']))]
    return '\n'.join(out) + '\n'


def card_rol(k, reg, by_oby, by_rol, info, flows=None):
    r, oby = reg['rol'][k], reg['oby']
    mine = [o for o, v in oby.items() if k in as_list(v.get('predpolagaem'))]
    out = [f'# {r["title"]}\n', f'{r["polno"]}\n'] + info + ['']
    if mine:
        g = ['flowchart LR', f'  {nid("r", k)}(["{label(r["title"])}"])']
        for kontur in dict.fromkeys(str(oby[o].get('kontur', '')).split(' ')[0] for o in mine):
            g.append(f'  subgraph {nid("k", kontur or "x")}["контур {kontur}"]')
            g += [f'    {nid("o", o)}("{label(oby[o]["title"])}")' for o in mine if str(oby[o].get('kontur', '')).split(' ')[0] == kontur]
            g.append('  end')
        g += [f'  {nid("r", k)} --> {nid("o", o)}' for o in mine]
        out += ['## Обязанности, которые мы ей приписываем\n', fence(g)]
        for o in mine:
            others = [x for x in as_list(oby[o].get('predpolagaem')) if x != k]
            share = f' *(вместе с: {", ".join(link_rol(reg, x) for x in others)})*' if others else ''
            out.append(f'- {link_oby(reg, o)} — {oby[o]["polno"]}{share}')
        out.append('')
        rows = [(p, s, o) for o in mine for p, s, rel in by_oby.get(o, []) if rel == 'delaet']
        if rows:
            out += ['## Шаги процессов\n', '| Процесс | № | Шаг | Обязанность |', '|---|---|---|---|']
            out += [f'| {link_proc(p)} | {s["nomer"] or "—"} | {cell(s["title"])} | {link_oby(reg, o)} |'
                    for p, s, o in sorted(rows, key=lambda x: (x[0]['slug'], x[0]['shagi'].index(x[1])))]
            out.append('')
    if flows and any(k in e for e in flows):
        out += ['## С кем работает\n', 'Сколько раз работа переходит от должности к должности (ставит задачу, передаёт результат, '
                'следующий шаг) — по всем процессам.\n', graph_handoffs(flows, reg, center=k)]
    direct = by_rol.get(k, [])
    if direct:
        word = dict(RELS)
        out += ['## Где должность названа прямо\n', '| Процесс | № | Шаг | Как |', '|---|---|---|---|']
        out += [f'| {link_proc(p)} | {s["nomer"] or "—"} | {cell(s["title"])} | {word[rel]} |' for p, s, rel in direct]
    return '\n'.join(out) + '\n'


# ---------- обзорные дорожки ----------

def pos_of(reg, k):
    """Должность обязанности для обзора: первая из «предполагаем»; не знаем — «-»."""
    return (as_list(reg['oby'][k].get('predpolagaem')) or ['-'])[0]


def pos_title(reg, r):
    return short_rol(reg['rol'], r) if r != '-' else 'не знаем кто'


def handoff(p, i, reg):
    """Переход работы перед шагом i: (откуда — должность, куда — должность) или (None, должность)."""
    t = p['tolk'][p['shagi'][i]['id']]
    r = pos_of(reg, doer(t))
    prev = pos_of(reg, doer(p['tolk'][p['shagi'][i - 1]['id']])) if i else None
    if prev == r:   # та же должность продолжает — перехода нет, даже если задачу когда-то поставил другой
        return (None, r)
    src = next((pos_of(reg, v) for v in as_list(t.get('stavit')) if pos_of(reg, v) != r), prev)
    return (src, r) if src and src != r else (None, r)


def incoming(p, i, reg):
    """Что приходит к шагу i при переходе: peredaet последнего шага должности-источника в отрезке перед i."""
    src, _ = handoff(p, i, reg)
    if not src:
        return []
    for j in range(i - 1, -1, -1):
        t = p['tolk'][p['shagi'][j]['id']]
        if pos_of(reg, doer(t)) != src:
            break
        if t.get('peredaet'):
            return as_list(t['peredaet'])
    return reg.get('_recv', {}).get(doer(p['tolk'][p['shagi'][i]['id']]), [])   # пришло из другого процесса


def prepare(parts, reg):
    """Что каждая обязанность получает от шагов, где она — «принимает результат» (нужно для переходов между процессами)."""
    recv = {}
    for p in procs(parts):
        for t in p['tolk'].values():
            for v in as_list(t.get('prinimaet')):
                for a in as_list(t.get('peredaet')):
                    recv.setdefault(v, [])
                    if a not in recv[v]:
                        recv[v].append(a)
    reg['_recv'] = recv


def art_names(reg, keys):
    return ', '.join(reg['art'][a]['title'] for a in keys)


def seq_text(text, width=30, limit=80):
    """Подпись в диаграмме последовательности: «;» и «#» — служебные, заменяются кодами."""
    return label(str(text).replace(';', '\x00'), width, limit).replace('\x00', '#59;')   # коды #quot; не ломаем


def participants(roles, reg):
    return [f'  participant {nid("r", r if r != "-" else "none")} as {pos_title(reg, r)}' for r in roles]


def pid(r):
    return nid('r', r if r != '-' else 'none')


def seq_process(p, reg):
    """Дорожки процесса: должность — вертикальная дорожка; шаг — заметка в её дорожке; стрелка — переход работы
    к другой должности с тем, что передаётся (пунктир «дальше» — что передаётся, не записано)."""
    roles = list(dict.fromkeys(pos_of(reg, doer(p['tolk'][s['id']])) for s in p['shagi']))
    out = ['sequenceDiagram'] + participants(roles, reg)
    for i, s in enumerate(p['shagi']):
        src, r = handoff(p, i, reg)
        if src:
            arts = incoming(p, i, reg)
            out.append(f'  {pid(src)}->>{pid(r)}: {seq_text(art_names(reg, arts), 34, 90)}' if arts else
                       f'  {pid(src)}-->>{pid(r)}: дальше')
        out.append(f'  Note over {pid(r)}: {seq_text(step_name(s), 34, 90)}')
    return fence(out)


def seq_project(plist, reg):
    """Весь проект по дорожкам: блок на процесс; в блоке — отрезки работы должностей и переходы между ними."""
    roles = [r for r in list(reg['rol']) + ['-'] if any(pos_of(reg, doer(p['tolk'][s['id']])) == r for p in plist for s in p['shagi'])]
    out = ['sequenceDiagram'] + participants(roles, reg)
    colors = ('rgb(232, 240, 254)', 'rgb(253, 246, 227)')
    prev, last_out = None, []
    for i, p in enumerate(plist):
        segs = []   # (должность, обязанности, что пришло в отрезок)
        for i, s in enumerate(p['shagi']):
            r, d = pos_of(reg, doer(p['tolk'][s['id']])), doer(p['tolk'][s['id']])
            if segs and segs[-1][0] == r:
                segs[-1][1].append(d)
            else:
                segs.append((r, [d], incoming(p, i, reg) if i else last_out))
        last_out = next((as_list(p['tolk'][s['id']]['peredaet']) for s in reversed(p['shagi']) if p['tolk'][s['id']].get('peredaet')), [])
        out += [f'  rect {colors[i % 2]}', f'  Note over {pid(roles[0])},{pid(roles[-1])}: {seq_text(p["title"], 200, 120)}']
        for r, ds, segs_arts in segs:
            names = list(dict.fromkeys(reg['oby'][d]['title'] for d in ds))
            text = '<br/>'.join(seq_text(n, 200, 60) for n in names[:3]) + (f'<br/>и ещё {len(names) - 3}' if len(names) > 3 else '')
            if prev and prev != r:
                arts = segs_arts
                out.append(f'  {pid(prev)}->>{pid(r)}: {seq_text(art_names(reg, arts), 40, 70)}' if arts else
                           f'  {pid(prev)}-->>{pid(r)}: дальше')
            out.append(f'  Note over {pid(r)}: {text}')
            prev = r
        out.append('  end')
    return fence(out)


def handoffs(plist, reg):
    """Кто кому передаёт работу: должности и число передач (ставит задачу, передаёт результат, следующий шаг)."""
    n = {}
    for p in plist:
        prev = None
        for s in p['shagi']:
            t = p['tolk'][s['id']]
            d = pos_of(reg, doer(t))
            pairs = [(pos_of(reg, v), d) for v in as_list(t.get('stavit'))]
            pairs += [(d, pos_of(reg, v)) for v in as_list(t.get('prinimaet'))]
            if prev and prev != d:
                pairs.append((prev, d))
            for a, b in pairs:
                if a != b:
                    n[(a, b)] = n.get((a, b), 0) + 1
            prev = d
    return graph_handoffs(n, reg), n


def graph_handoffs(n, reg, center=None, least=2):
    """Должности и передачи между ними; на общей схеме — от least передач, у карточки — все связи должности center."""
    edges = {e: k for e, k in n.items() if (center in e if center else k >= least)}
    roles = list(dict.fromkeys(r for pair in edges for r in pair))
    out = ['flowchart LR']
    out += [f'  {pid(r)}(["{label(pos_title(reg, r))}"])' for r in roles]
    if center:
        out.append(f'  style {pid(center)} stroke-width:3px')
    for (a, b), k in sorted(edges.items(), key=lambda kv: -kv[1]):
        out.append(f'  {pid(a)} {"==>" if k >= 5 else "-->"}|{k}| {pid(b)}')
    return fence(out)


def matrix(plist, reg):
    count = {}
    for p in plist:
        for s in p['shagi']:
            r = pos_of(reg, doer(p['tolk'][s['id']]))
            count[(r, p['slug'])] = count.get((r, p['slug']), 0) + 1
    roles = [r for r in list(reg['rol']) + ['-'] if any(k[0] == r for k in count)]
    head = '| Процесс | ' + ' | '.join(link_rol(reg, r).replace(reg['rol'][r]['title'], pos_title(reg, r)) if r != '-' else 'не знаем кто'
                                       for r in roles) + ' |'
    out = [head, '|---|' + '---|' * len(roles)]
    for p in plist:
        out.append(f'| {link_proc(p)} | ' + ' | '.join(str(count.get((r, p['slug']), '')) for r in roles) + ' |')
    out.append('| **Всего** | ' + ' | '.join(f'**{sum(v for (x, _), v in count.items() if x == r)}**' for r in roles) + ' |')
    return '\n'.join(out) + '\n'


def render_dorozhki(parts, reg):
    plist = procs(parts)
    graph, n = handoffs(plist, reg)
    top = sorted(n.items(), key=lambda kv: -kv[1])[:5]
    rows = ['| От кого | Кому | Передач |', '|---|---|---|']
    rows += [f'| {pos_title(reg, a)} | {pos_title(reg, b)} | {k} |' for (a, b), k in sorted(n.items(), key=lambda kv: -kv[1])]
    lines = ['\n## Весь проект по дорожкам\n',
             'Вертикальная дорожка — должность (по нашей догадке, кто выполняет обязанность шага). Цветной блок — процесс; '
             'в дорожке — обязанности, которые должность там выполняет; стрелка — работа переходит к другой должности. '
             'Подробно, шаг за шагом, — на странице каждого процесса.\n',
             seq_project(plist, reg),
             '## Кто кому передаёт работу\n',
             'Стрелка — сколько раз работа переходит от одной должности к другой: ставит задачу, передаёт результат или делает '
             'следующий шаг. На схеме — от 2 передач, толстая — 5 и больше; все — в таблице.\n', graph,
             'Больше всего передач: ' + '; '.join(f'{pos_title(reg, a)} → {pos_title(reg, b)} — {k}' for (a, b), k in top) + '.\n',
             '\n'.join(rows) + '\n',
             '## Сколько шагов у кого\n',
             'Шаги, которые делает должность, по процессам. Должность — первая из «предполагаем» у обязанности шага.\n',
             matrix(plist, reg)]
    return '\n'.join(lines)


def art_flow(parts, reg):
    """Предмет → [(процесс, шаг, кто отдаёт — обязанность, кому — обязанность следующего шага или принимающая)]."""
    out = {}
    for p in procs(parts):
        for i, s in enumerate(p['shagi']):
            t = p['tolk'][s['id']]
            nxt = doer(p['tolk'][p['shagi'][i + 1]['id']]) if i + 1 < len(p['shagi']) else None
            to = [v for v in as_list(t.get('prinimaet'))] or ([nxt] if nxt else [])
            for a in as_list(t.get('peredaet')):
                out.setdefault(a, []).append((p, s, doer(t), to))
    return out


def art_info(a, reg, flows):
    rows = flows.get(a, [])
    if not rows:
        return ''
    lines = ['| Процесс | № | Кто отдаёт | Кому |', '|---|---|---|---|']
    up = lambda x: x.replace(ROOT, '../')
    lines += [f'| {up(link_proc(p))} | {s["nomer"] or "—"} | {up(link_oby(reg, d))} | '
              + ', '.join(up(link_oby(reg, v)) for v in to) + ' |' for p, s, d, to in rows]
    return '\n'.join(lines) + '\n'
