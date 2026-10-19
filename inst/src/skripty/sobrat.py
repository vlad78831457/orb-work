#!/usr/bin/env python3
"""Сборщик инструкций из частей.

Часть — папка inst/src/md-kod/<раздел>/<часть>/ (разделы: tio, zna, um, lis, pro) (стандарты — inst/src/standarty/<часть>/) с файлом index.md
и шапкой YAML: title, kratko, polno, status, tags, nuzhno. Имя части — <раздел>.<часть>: zna.tab-nmts.
Реестр — inst/src/md-kod/reg/: ter.yaml (термины), rol.yaml (должности), oby.yaml (обязанности), mes.yaml (места работы),
res.yaml (рабочие ссылки). Процессы (раздел pro) — данные шагов и схемы: см. protsessy.py.

Упоминание в тексте меняет вид по месту:
  [[zna.tab-nmts]] внутри предложения        короткое имя ссылкой
  [[zna.tab-nmts]] отдельной строкой/пунктом  карточка: название — описание
  [[zna.tab-nmts|свой текст]]                 ссылка со своим текстом
  [[zna.tab-nmts:kratko]]                     короткое имя ссылкой, явно
  [[zna.tab-nmts:polno]]                      карточка, явно
  [[zna.tab-nmts:tekst]] отдельной строкой    в полном документе — текст части целиком на этом месте,
                                              в виде «репозиторий» — карточка со ссылкой

  sobrat.py --check                     только проверка
  sobrat.py [--out ПАПКА]               проверка и сборка вида «репозиторий» (по умолчанию inst/md-out)
  sobrat.py --full ИМЯ [--out ПАПКА] [--date ГГГГ-ММ-ДД]
                                        короткий и полный md (по умолчанию в inst/md-full-out):
                                        ИМЯ = tio.tov-razdelenie — по описанию full.yaml в папке части,
                                        ИМЯ = svod — по описанию inst/src/full/svod.yaml
"""
import datetime
import os
import re
import shutil
import sys

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import protsessy  # noqa: E402

SRC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INST = os.path.dirname(SRC)
SECTIONS = [('tio', 'Инструкции', 'md-kod/tio'), ('zna', 'Знания', 'md-kod/zna'), ('um', 'Умения', 'md-kod/um'),
            ('lis', 'Листы', 'md-kod/lis'), ('pro', 'Процессы', 'md-kod/pro'),
            ('standarty', 'Стандарты', 'standarty')]
REG = {'ter': 'Термины', 'rol': 'Должности', 'oby': 'Обязанности', 'mes': 'Места работы', 'res': 'Ресурсы'}
GLOSS = ('ter', 'rol', 'oby', 'mes')   # реестры-словари: у каждого своя собранная страница
CARDS = ('rol', 'oby')                 # у должности и обязанности — ещё и своя карточка reg/<вид>/<ключ>.md
INFO = (('kontur', 'Контур'), ('nazvaniya', 'Как ещё называют'), ('kolonka', 'Столбец регламента'),
        ('istochnik', 'Источник'), ('pochemu', 'Почему выделили'), ('dogadka', 'Догадка, не подтверждено'))
STATUSES = ('готово', 'проверить', 'заглушка')
FORMS = (None, 'kratko', 'polno', 'tekst')
STUB = '*Часть ещё не написана.*'

MENTION = re.compile(r'\[\[([a-z0-9]+\.[a-z0-9-]+)(?::([a-z]+))?(?:\|([^\]]+))?\]\]')
ALONE = re.compile(r'^(\s*(?:(?:[-*+]|\d+[.)])\s+)?)[*_]*(\[\[[^\]]+\]\])[*_]*[.;,]?\s*$')
IMAGE = re.compile(r'!\[([^\]]*)\]\(<?([^)>]+?)>?\)')
LINK = re.compile(r'(?<!!)\[((?:[^\[\]]|\[[^\]]*\])*)\]\(<?([^)>\s]+)>?\)')
CODE = re.compile(r'(^```.*?^```[^\n]*$|`[^`\n]+`)', re.S | re.M)
FENCE = re.compile(r'(^```.*?^```[^\n]*$)', re.S | re.M)
INLINE = re.compile(r'(`[^`\n]+`)')
SPAN_ID = re.compile(r'\[([^\[\]]+)\]\{#([^}\s]+)\}')
HEAD_ID = re.compile(r'^(#+) (.*?)\s*\{#([^}\s]+)\}\s*$', re.M)
ANCHOR = re.compile(r'\{#([^}\s]+)\}')


def prose(text):
    """Текст без блоков и вставок кода."""
    return ''.join(p for i, p in enumerate(CODE.split(text)) if not i % 2)


def outside_inline(line, fn):
    """Применяет fn к строке вне вставок кода."""
    return ''.join(p if i % 2 else fn(p) for i, p in enumerate(INLINE.split(line)))


def map_lines(text, fn):
    """Применяет fn к каждой строке вне блоков кода."""
    return ''.join(c if i % 2 else '\n'.join(fn(ln) for ln in c.split('\n')) for i, c in enumerate(FENCE.split(text)))


def mentions(text):
    """Все упоминания вне кода: (имя, вид, свой текст, стоит ли отдельной строкой)."""
    found = []

    def line(ln):
        alone = bool(ALONE.match(ln))
        outside_inline(ln, lambda t: found.extend((m.group(1), m.group(2), m.group(3), alone) for m in MENTION.finditer(t)) or t)
        return ln

    map_lines(text, line)
    return found


def load():
    parts, errors = {}, []
    for sec, _, sub in SECTIONS:
        base = f'{SRC}/{sub}'
        for slug in sorted(os.listdir(base)) if os.path.isdir(base) else []:
            path = f'{base}/{slug}/index.md'
            if not os.path.isfile(path):
                continue
            where = f'{sec}.{slug}'
            text = open(path, encoding='utf-8').read()
            m = re.match(r'---\n(.*?)\n---\n', text, re.S)
            if not m:
                errors.append(f'{where}: нет шапки YAML')
                continue
            head = yaml.safe_load(m.group(1)) or {}
            if not head.get('title') or head.get('status') not in STATUSES:
                errors.append(f'{where}: в шапке нужны title и status ({", ".join(STATUSES)})')
                continue
            if not re.fullmatch(r'[a-z0-9-]+', slug):
                errors.append(f'{where}: имя папки — только латиница, цифры и дефис (skripty/slugify.sh)')
            body = text[m.end():].strip('\n')
            parts[where] = {
                'name': where, 'sec': sec, 'slug': slug, 'dir': f'{base}/{slug}',
                'title': head['title'], 'short': head.get('kratko') or head['title'],
                'description': head.get('polno') or '', 'tags': head.get('tags') or [],
                'status': head['status'], 'requires': head.get('nuzhno') or [],
                'body': body or f'# {head["title"]}\n\n{STUB}'}
    for p in parts.values():
        if p['sec'] == 'pro' and p['slug'] != 'obzor':
            protsessy.attach(p, errors)
    reg = {}
    for kind in REG:
        path = f'{SRC}/md-kod/reg/{kind}.yaml'
        reg[kind] = (yaml.safe_load(open(path, encoding='utf-8')) or {}) if os.path.isfile(path) else {}
    fulls = {}   # имя → описание полного документа; rel — куда класть относительно папки сборки
    for f in sorted(os.listdir(f'{SRC}/full')) if os.path.isdir(f'{SRC}/full') else []:
        if f.endswith('.yaml'):
            d = yaml.safe_load(open(f'{SRC}/full/{f}', encoding='utf-8')) or {}
            fulls[f[:-5]] = {**d, 'rel': f'full/{f[:-5]}'}
    for p in parts.values():
        path = f'{p["dir"]}/full.yaml'
        if os.path.isfile(path):
            d = yaml.safe_load(open(path, encoding='utf-8')) or {}
            fulls[p['name']] = {**d, 'chast': p['name'], 'rel': f'{p["sec"]}/{p["slug"]}'}
    return parts, reg, fulls, errors


def closure(part, parts, seen=None):
    """Все зависимости части по порядку, каждая один раз. Взаимные упоминания допустимы."""
    seen = [] if seen is None else seen
    for r in part['requires']:
        dep = parts.get(r)
        if dep and dep is not part and dep not in seen:
            seen.append(dep)
            closure(dep, parts, seen)
    return seen


def check(parts, reg, fulls):
    errors, warnings = [], []
    plan_path = f'{INST}/PLAN.md'
    plan = open(plan_path, encoding='utf-8').read() if os.path.isfile(plan_path) else ''
    for p in parts.values():
        where = p['name']
        soft = warnings if p['status'] != 'готово' else errors
        text = prose(p['body'])
        for r in p['requires']:
            if r not in parts:
                errors.append(f'{where}: в nuzhno нет такой части — {r}')
        used = set()
        for name, form, own, alone in mentions(p['body']):
            kind, key = name.split('.', 1)
            if form not in FORMS:
                errors.append(f'{where}: неизвестный вид упоминания — [[{name}:{form}]] (есть kratko, polno и tekst)')
            if kind in reg:
                if key not in reg[kind]:
                    errors.append(f'{where}: в реестре {kind} нет записи — {key}')
                elif form == 'tekst':
                    errors.append(f'{where}: tekst работает только для частей — [[{name}:tekst]]')
                continue
            if name not in parts:
                errors.append(f'{where}: упомянута часть, которой нет — {name}')
                continue
            used.add(name)
            if name not in p['requires']:
                errors.append(f'{where}: упомянута часть {name}, но её нет в nuzhno')
            if form == 'tekst' and (not alone or own):
                errors.append(f'{where}: [[{name}:tekst]] ставится отдельной строкой и без своего текста')
            if not own and (form == 'polno' or (alone and form is None)) and not parts[name]['description'] and parts[name]['status'] == 'готово':
                warnings.append(f'{where}: карточка {name} без описания — нет polno в шапке')
        for r in p['requires']:
            if r in parts and r not in used:
                warnings.append(f'{where}: {r} есть в nuzhno, но в тексте не упомянута')
        for _, img in IMAGE.findall(text):
            if not re.match(r'[a-z]+:', img) and not os.path.isfile(f'{p["dir"]}/{img}'):
                soft.append(f'{where}: нет снимка {img}')
        own_ids = set(ANCHOR.findall(text))
        for _, link in LINK.findall(text):
            if link.startswith('#'):
                if link[1:] not in own_ids:
                    soft.append(f'{where}: ссылка в никуда — {link}')
            elif not re.match(r'[a-z]+:', link):
                soft.append(f'{where}: ссылка на файл вместо упоминания [[…]] — {link}')
        if p['status'] != 'готово' and f'`{p["name"]}`' not in plan:
            errors.append(f'{where}: статус «{p["status"]}», но части нет в inst/PLAN.md')
    e, notes = protsessy.check(parts, reg)
    errors += e
    if notes:
        warnings.append(f'процессы: расхождений и вопросов — {len(notes)}, список в inst/md-out/pro/obzor/index.md')
    for name, f in fulls.items():
        for n in [f.get('chast')] + (f.get('vklyuchit') or []):
            if n not in parts:
                errors.append(f'полный документ {name}: нет такой части — {n}')
    return errors, warnings


def strip_ids(text):
    """Метки Pandoc {#id} → <a id>, чтобы внутренние ссылки работали на GitHub."""
    text = SPAN_ID.sub(lambda m: f'<a id="{m.group(2)}"></a>{m.group(1)}', text)
    return HEAD_ID.sub(lambda m: f'{m.group(1)} <a id="{m.group(3)}"></a>{m.group(2)}', text)


def note(p):
    return '> Черновик: текст не проверен.\n\n' if p['status'] == 'проверить' else ''


class Builder:
    """Общая сборка текста части; наследники задают, куда ведут ссылки и где лежат снимки."""

    inline_tekst = True   # вставлять ли текст части на месте [[…:tekst]]

    def embed_mark(self, t):   # метка перед вставленным текстом части
        return ''

    def __init__(self, parts, reg):
        self.parts, self.reg = parts, reg

    def part_link(self, t):            # ссылка на часть или None, если части нет в документе
        raise NotImplementedError

    def term_link(self, kind, key):
        raise NotImplementedError

    def image_path(self, owner, host, img):   # путь к снимку части owner из текста части host
        raise NotImplementedError

    def render(self, name, form, own, alone):
        kind, key = name.split('.', 1)
        card = form == 'polno' or (alone and not own and form is None)
        if kind in GLOSS:
            t = self.reg[kind][key]
            return f'**{t["title"]}** — {t["polno"]}' if card else f'[{own or t["title"]}]({self.term_link(kind, key)})'
        if kind == 'res':
            r = self.reg[kind][key]
            link = f'[{own or r["title"]}]({r["url"]})' if r.get('url') else f'{own or r["title"]} *(ссылка не задана)*'
            return f'{link} — {r["polno"]}' if card and r.get('polno') else link
        t = self.parts[name]
        text = own or (t['title'] if card else t['short'])
        url = self.part_link(t)
        link = f'[{text}]({url})' if url else text   # части нет в полном документе — остаётся названием
        return f'{link} — {t["description"]}' if card and t['description'] else link

    def text(self, p, host=None, stack=(), body=None):
        """Текст части p; host — часть, в чей текст он вставляется (для tekst)."""
        host = host or p

        def image(m):
            alt, img = m.groups()
            if re.match(r'[a-z]+:', img):
                return m.group(0)
            if not os.path.isfile(f'{p["dir"]}/{img}'):
                return f'*[нет снимка: {img}]*'
            return f'![{alt}](<{self.image_path(p, host, img)}>)'

        def line(ln):
            alone = ALONE.match(ln)
            m = MENTION.fullmatch(alone.group(2)) if alone else None
            if m and m.group(2) == 'tekst' and m.group(1) in self.parts and not self.inline_tekst:
                return alone.group(1) + self.render(m.group(1), 'polno', None, True)
            if m and m.group(2) == 'tekst' and m.group(1) in self.parts:
                t = self.parts[m.group(1)]
                if t is p or t['name'] in stack:
                    return f'*[вставка по кругу: {t["name"]}]*'
                return self.embed_mark(t) + self.text(t, host, stack + (p['name'],), re.sub(r'\A# [^\n]*\n+', '', t['body']))
            if m:
                return alone.group(1) + self.render(m.group(1), m.group(2), m.group(3), True)
            return outside_inline(ln, lambda t: IMAGE.sub(image, MENTION.sub(
                lambda m: self.render(m.group(1), m.group(2), m.group(3), False), t)))

        return map_lines(p['body'] if body is None else body, line)


class Dist(Builder):
    inline_tekst = False   # в виде «репозиторий» часть не дублируется: карточка со ссылкой

    def __init__(self, parts, reg, out):
        super().__init__(parts, reg)
        self.out = out

    def part_link(self, t):
        return f'../../{t["sec"]}/{t["slug"]}/index.md'

    def term_link(self, kind, key):
        return f'../../reg/{kind}/{key}.md' if kind in CARDS else f'../../reg/{kind}.md#{key}'

    def image_path(self, owner, host, img):
        dst = f'{self.out}/{owner["sec"]}/{owner["slug"]}/{img}'
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copyfile(f'{owner["dir"]}/{img}', dst)
        return img if owner is host else f'../../{owner["sec"]}/{owner["slug"]}/{img}'


class Full(Builder):
    def __init__(self, parts, reg, out, rel, names):
        super().__init__(parts, reg)
        self.out, self.rel, self.names, self.terms = out, rel, names, []

    def part_link(self, t):
        return f'#part-{t["name"].replace(".", "-")}' if t['name'] in self.names else None

    def embed_mark(self, t):
        return f'[]{{#part-{t["name"].replace(".", "-")}}}\n\n'

    def term_link(self, kind, key):
        if (kind, key) not in self.terms:
            self.terms.append((kind, key))
        return f'#{kind}-{key}'

    def image_path(self, owner, host, img):
        sub = f'{owner["sec"]}-{owner["slug"]}/{img}'
        dst = f'{self.out}/{self.rel}/{sub}'
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copyfile(f'{owner["dir"]}/{img}', dst)
        return f'{os.path.basename(self.rel)}/{sub}'


def build_dist(parts, reg, out):
    for d in [s for s, _, _ in SECTIONS] + ['reg']:
        shutil.rmtree(f'{out}/{d}', ignore_errors=True)
    b = Dist(parts, reg, out)
    _, notes = protsessy.check(parts, reg)
    for p in parts.values():
        dst = f'{out}/{p["sec"]}/{p["slug"]}'
        os.makedirs(dst, exist_ok=True)
        text = note(p) + map_lines(b.text(p), lambda ln: outside_inline(ln, strip_ids)) + '\n'
        if p['sec'] == 'pro':   # схемы и таблицы процесса собираются из данных шагов
            text += protsessy.render_obzor(parts, reg, notes) if p['slug'] == 'obzor' else protsessy.render_process(p, reg, parts)
        open(f'{dst}/index.md', 'w', encoding='utf-8').write(text)
    os.makedirs(f'{out}/reg', exist_ok=True)
    where = {}   # (реестр, ключ) → части, где запись упомянута: у должности так видно её инструкции
    for p in parts.values():
        for name, *_ in mentions(p['body']):
            kind, key = name.split('.', 1)
            if kind in GLOSS and p not in where.setdefault((kind, key), []):
                where[(kind, key)].append(p)
    by_oby, by_rol, places = protsessy.index(parts, reg)

    def info(t, kind, key, root):
        lines = []
        for f, title in INFO:
            v = t.get(f)
            if v:
                lines.append(f'- **{title}:** ' + ('; '.join(map(str, v)) if isinstance(v, list) else str(v)))
        if where.get((kind, key)):
            lines.append('- **Где упоминается:** ' + ', '.join(f'[{p["title"]}]({root}{p["sec"]}/{p["slug"]}/index.md)'
                                                              for p in sorted(where[(kind, key)], key=lambda p: (p['sec'], p['slug']))))
        return lines

    for kind in GLOSS:
        lines = [f'# {REG[kind]}\n']
        items = reg[kind].items() if kind != 'ter' else sorted(reg[kind].items(), key=lambda kv: kv[1]['title'].lower())
        for key, t in items:   # должности и обязанности — в порядке файла: он сгруппирован по контурам
            mark = ' *(проверить)*' if t.get('status') == 'проверить' else ''
            if kind == 'ter':
                lines.append(f'<a id="{key}"></a>**{t["title"]}** — {t["polno"]}{mark}\n')
            elif kind in CARDS:
                lines.append(f'- <a id="{key}"></a>[{t["title"]}]({kind}/{key}.md) — {t["polno"]}{mark}')
            else:   # место работы: кто там работает
                used = ', '.join(f'[{reg["oby"][o]["title"]}](oby/{o}.md)' for o in places.get(key, []))
                chast = f' Описание: [{parts[t["chast"]]["title"]}](../{t["chast"].replace(".", "/")}/index.md).' if t.get('chast') else ''
                lines.append(f'## <a id="{key}"></a>{t["title"]}\n\n{t["polno"]}{chast}\n' + (f'\nРаботают здесь: {used}\n' if used else ''))
        open(f'{out}/reg/{kind}.md', 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    for key in reg['oby']:
        os.makedirs(f'{out}/reg/oby', exist_ok=True)
        open(f'{out}/reg/oby/{key}.md', 'w', encoding='utf-8').write(protsessy.card_oby(key, reg, by_oby))
    for key, t in reg['rol'].items():
        os.makedirs(f'{out}/reg/rol', exist_ok=True)
        open(f'{out}/reg/rol/{key}.md', 'w', encoding='utf-8').write(
            protsessy.card_rol(key, reg, by_oby, by_rol, info(t, 'rol', key, '../../')))
    lines = ['# Инструкции\n', 'Собрано из `inst/src` скриптом `skripty/sobrat.py`. Руками здесь не править.\n']
    for sec, title, _ in SECTIONS:
        lines.append(f'## {title}\n')
        for p in parts.values():
            if p['sec'] == sec:
                desc = f' — {p["description"]}' if p['description'] else ''
                mark = '' if p['status'] == 'готово' else f' — *{p["status"]}*'
                lines.append(f'- [{p["title"]}]({sec}/{p["slug"]}/index.md){desc}{mark}')
        lines.append('')
    lines.append('## Реестр\n\n' + '\n'.join(f'- [{REG[k]}](reg/{k}.md)' for k in GLOSS) + '\n')
    open(f'{out}/README.md', 'w', encoding='utf-8').write('\n'.join(lines))
    return len(parts)


def embedded(p, parts, seen=None):
    """Части, текст которых вставляется в p через [[…:tekst]] (и дальше по цепочке)."""
    seen = set() if seen is None else seen
    for name, form, _, _ in mentions(p['body']):
        if form == 'tekst' and name in parts and name not in seen:
            seen.add(name)
            embedded(parts[name], parts, seen)
    return seen


def build_full(name, parts, reg, fulls, out, date, short=False):
    """Полный документ (short=False) или короткий: только сама инструкция, вставки [[…:tekst]] — на месте."""
    f = fulls[name]
    root = parts[f['chast']]
    inside = embedded(root, parts)
    extra = [] if short else [parts[n] for n in f.get('vklyuchit') or [] if n != f['chast'] and n not in inside]
    included = [root] + extra
    rel = f['rel']
    b = Full(parts, reg, out, rel, {p['name'] for p in included} | inside)
    title = f.get('title') or root['title']
    head = [f'**Версия от {date}**']
    if f.get('hranenie'):
        head.append(f'Место хранения: [{f["hranenie"]}]({f["hranenie"]})')
    if not short and extra:
        head.append('Полная версия: инструкция и всё, на что она опирается')
    chunks = [f'---\ntitle: "{title}"\ndate: "{date}"\n---\n']
    for i, p in enumerate(included):
        body = b.text(p)
        if i == 0:   # строка о версии — сразу под первым заголовком
            body = re.sub(r'\A(# [^\n]*\n)', lambda m: m.group(1) + '\n' + ' · '.join(head) + '\n', body, count=1)
            if not body.startswith('# '):
                body = ' · '.join(head) + '\n\n' + body
        chunks.append(('\n---\n\n' if i else '') + f'[]{{#part-{p["name"].replace(".", "-")}}}\n\n' + note(p) + body + '\n')
    if b.terms:
        chunks.append('\n---\n\n# Термины и роли\n')
        for kind, key in b.terms:
            t = reg[kind][key]
            chunks.append(f'[]{{#{kind}-{key}}}**{t["title"]}** — {t["polno"]}\n')
    text = '\n'.join(chunks)
    ids = ANCHOR.findall(prose(text))
    for dup in sorted({i for i in ids if ids.count(i) > 1}):
        print(f'  внимание: метка #{dup} встречается в сборке несколько раз')
    path = f'{out}/{rel}{"" if short else "-full"}.md'
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8').write(text)
    return path, len(included)


def arg(flag):
    return sys.argv[sys.argv.index(flag) + 1] if flag in sys.argv else None


def main():
    parts, reg, fulls, errors = load()
    e, warnings = check(parts, reg, fulls)
    errors += e
    for w in warnings:
        print('  внимание:', w)
    for e in errors:
        print('FAIL:', e)
    if errors:
        sys.exit(1)
    if '--check' in sys.argv:
        print(f'inst: частей {len(parts)}, ошибок нет')
    elif '--full' in sys.argv:
        name = arg('--full')
        if name not in fulls:
            sys.exit(f'FAIL: нет описания полного документа {name}. Есть: {", ".join(fulls) or "—"}')
        out = arg('--out') or f'{INST}/md-full-out'
        date = arg('--date') or datetime.date.today().isoformat()
        shutil.rmtree(f'{out}/{fulls[name]["rel"]}', ignore_errors=True)   # снимки — общие для обеих версий
        for short in (True, False):
            path, n = build_full(name, parts, reg, fulls, out, date, short)
            print(f'собран {"короткий" if short else "полный"} документ {os.path.relpath(path, out)} (частей: {n})')
    else:
        out = arg('--out') or f'{INST}/md-out'
        print(f'собран вид «репозиторий» (частей: {build_dist(parts, reg, out)})')


if __name__ == '__main__':
    main()
