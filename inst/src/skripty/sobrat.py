#!/usr/bin/env python3
"""Сборщик инструкций из частей.

Часть — папка inst/src/<раздел>/<часть>/ с файлом index.md и шапкой YAML: title, status, requires.
Имя части — <раздел>.<часть>, например znaniya.nmts.
Упоминание в тексте: [[znaniya.nmts]] или [[umeniya.tolko-znacheniya|вставляете только значения]];
термин и ресурс из реестра — [[terminy.kp]], [[resursy.shablon-tablitsy|шаблон]].

  sobrat.py --check              только проверка
  sobrat.py [--out ПАПКА]        проверка и сборка вида «репозиторий» (по умолчанию inst/dist)
  sobrat.py --full ИМЯ [--out ПАПКА]   полный md по описанию inst/src/full/ИМЯ.yaml (по умолчанию inst/full-out)
"""
import os
import re
import shutil
import sys

import yaml

SRC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INST = os.path.dirname(SRC)
SECTIONS = [('instruktsii', 'Инструкции'), ('znaniya', 'Знания'), ('umeniya', 'Умения'), ('standarty', 'Стандарты')]
STATUSES = ('готово', 'проверить', 'заглушка')
STUB = '*Часть ещё не написана.*'

MENTION = re.compile(r'\[\[([a-z0-9]+\.[a-z0-9-]+)(?:\|([^\]]+))?\]\]')
IMAGE = re.compile(r'!\[([^\]]*)\]\(<?([^)>]+?)>?\)')
LINK = re.compile(r'(?<!!)\[((?:[^\[\]]|\[[^\]]*\])*)\]\(<?([^)>\s]+)>?\)')
CODE = re.compile(r'(^```.*?^```[^\n]*$|`[^`\n]+`)', re.S | re.M)
SPAN_ID = re.compile(r'\[([^\[\]]+)\]\{#([^}\s]+)\}')
HEAD_ID = re.compile(r'^(#+) (.*?)\s*\{#([^}\s]+)\}\s*$', re.M)
ANCHOR = re.compile(r'\{#([^}\s]+)\}')


def outside_code(text, fn):
    """Применяет fn к тексту вне блоков и вставок кода."""
    pieces = CODE.split(text)
    return ''.join(p if i % 2 else fn(p) for i, p in enumerate(pieces))


def prose(text):
    return ''.join(p for i, p in enumerate(CODE.split(text)) if not i % 2)


def load():
    parts, errors = {}, []
    for sec, _ in SECTIONS:
        base = f'{SRC}/{sec}'
        for slug in sorted(os.listdir(base)) if os.path.isdir(base) else []:
            path = f'{base}/{slug}/index.md'
            if not os.path.isfile(path):
                continue
            where = f'{sec}/{slug}'
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
            parts[f'{sec}.{slug}'] = {
                'name': f'{sec}.{slug}', 'sec': sec, 'slug': slug, 'dir': f'{base}/{slug}',
                'title': head['title'], 'status': head['status'], 'requires': head.get('requires') or [],
                'body': body or f'# {head["title"]}\n\n{STUB}'}
    reg = {}
    for kind in ('terminy', 'resursy'):
        path = f'{SRC}/reestr/{kind}.yaml'
        reg[kind] = (yaml.safe_load(open(path, encoding='utf-8')) or {}) if os.path.isfile(path) else {}
    fulls = {}
    for f in sorted(os.listdir(f'{SRC}/full')) if os.path.isdir(f'{SRC}/full') else []:
        if f.endswith('.yaml'):
            fulls[f[:-5]] = yaml.safe_load(open(f'{SRC}/full/{f}', encoding='utf-8')) or {}
    return parts, reg, fulls, errors


def closure(part, parts, seen=None, stack=()):
    """Все зависимости части по порядку, каждая один раз."""
    seen = [] if seen is None else seen
    if part['name'] in stack:
        raise RecursionError
    for r in part['requires']:
        dep = parts.get(r)
        if dep and dep not in seen:
            seen.append(dep)
            closure(dep, parts, seen, stack + (part['name'],))
    return seen


def check(parts, reg, fulls):
    errors, warnings = [], []
    plan_path = f'{INST}/PLAN.md'
    plan = open(plan_path, encoding='utf-8').read() if os.path.isfile(plan_path) else ''
    for p in parts.values():
        where = f'{p["sec"]}/{p["slug"]}'
        soft = warnings if p['status'] != 'готово' else errors
        text = prose(p['body'])
        for r in p['requires']:
            if r not in parts:
                errors.append(f'{where}: в requires нет такой части — {r}')
        used = set()
        for name, _ in MENTION.findall(text):
            kind, key = name.split('.', 1)
            if kind in reg:
                if key not in reg[kind]:
                    errors.append(f'{where}: в реестре {kind} нет записи — {key}')
            elif name not in parts:
                errors.append(f'{where}: упомянута часть, которой нет — {name}')
            else:
                used.add(name)
                if name not in p['requires']:
                    errors.append(f'{where}: упомянута часть {name}, но её нет в requires')
        for r in p['requires']:
            if r in parts and r not in used:
                warnings.append(f'{where}: {r} есть в requires, но в тексте не упомянута')
        for _, img in IMAGE.findall(text):
            if not re.match(r'[a-z]+:', img) and not os.path.isfile(f'{p["dir"]}/{img}'):
                soft.append(f'{where}: нет снимка {img}')
        own = set(ANCHOR.findall(text))
        for _, link in LINK.findall(text):
            if link.startswith('#'):
                if link[1:] not in own:
                    soft.append(f'{where}: ссылка в никуда — {link}')
            elif not re.match(r'[a-z]+:', link):
                soft.append(f'{where}: ссылка на файл вместо упоминания [[…]] — {link}')
        if p['status'] != 'готово' and f'`{p["name"]}`' not in plan:
            errors.append(f'{where}: статус «{p["status"]}», но части нет в inst/PLAN.md')
        try:
            closure(p, parts)
        except RecursionError:
            errors.append(f'{where}: зависимости замкнуты в круг')
    for name, f in fulls.items():
        for n in [f.get('chast')] + (f.get('vklyuchit') or []):
            if n not in parts:
                errors.append(f'full/{name}.yaml: нет такой части — {n}')
    return errors, warnings


def strip_ids(text):
    """Метки Pandoc {#id} → <a id>, чтобы внутренние ссылки работали на GitHub."""
    text = SPAN_ID.sub(lambda m: f'<a id="{m.group(2)}"></a>{m.group(1)}', text)
    return HEAD_ID.sub(lambda m: f'{m.group(1)} <a id="{m.group(3)}"></a>{m.group(2)}', text)


def resource(reg, key, text):
    r = reg['resursy'][key]
    url = r.get('url') or ''
    return f'[{text or r["title"]}]({url})' if url else f'{text or r["title"]} *(ссылка не задана)*'


def note(p):
    return '> Черновик: текст не проверен.\n\n' if p['status'] == 'проверить' else ''


def build_dist(parts, reg, out):
    for sec in [s for s, _ in SECTIONS] + ['reestr']:
        shutil.rmtree(f'{out}/{sec}', ignore_errors=True)
    for p in parts.values():
        dst = f'{out}/{p["sec"]}/{p["slug"]}'
        os.makedirs(dst, exist_ok=True)

        def mention(m, p=p):
            name, text = m.groups()
            kind, key = name.split('.', 1)
            if kind == 'terminy':
                return f'[{text or reg[kind][key]["title"]}](../../reestr/terminy.md#{key})'
            if kind == 'resursy':
                return resource(reg, key, text)
            t = parts[name]
            return f'[{text or t["title"]}](../../{t["sec"]}/{t["slug"]}/index.md)'

        def image(m, p=p, dst=dst):
            alt, img = m.groups()
            if re.match(r'[a-z]+:', img):
                return m.group(0)
            if not os.path.isfile(f'{p["dir"]}/{img}'):
                return f'*[нет снимка: {img}]*'
            os.makedirs(os.path.dirname(f'{dst}/{img}'), exist_ok=True)
            shutil.copyfile(f'{p["dir"]}/{img}', f'{dst}/{img}')
            return m.group(0)

        body = outside_code(p['body'], lambda t: strip_ids(IMAGE.sub(image, MENTION.sub(mention, t))))
        open(f'{dst}/index.md', 'w', encoding='utf-8').write(note(p) + body + '\n')
    os.makedirs(f'{out}/reestr', exist_ok=True)
    lines = ['# Термины\n']
    for key, t in sorted(reg['terminy'].items(), key=lambda kv: kv[1]['title'].lower()):
        mark = ' *(проверить)*' if t.get('status') == 'проверить' else ''
        lines.append(f'<a id="{key}"></a>**{t["title"]}** — {t["text"]}{mark}\n')
    open(f'{out}/reestr/terminy.md', 'w', encoding='utf-8').write('\n'.join(lines))
    lines = ['# Инструкции\n', 'Собрано из `inst/src` скриптом `skripty/sobrat.py`. Руками здесь не править.\n']
    for sec, title in SECTIONS:
        lines.append(f'## {title}\n')
        for p in parts.values():
            if p['sec'] == sec:
                mark = '' if p['status'] == 'готово' else f' — *{p["status"]}*'
                lines.append(f'- [{p["title"]}]({sec}/{p["slug"]}/index.md){mark}')
        lines.append('')
    lines.append('## Реестр\n\n- [Термины](reestr/terminy.md)\n')
    open(f'{out}/README.md', 'w', encoding='utf-8').write('\n'.join(lines))
    return len(parts)


def build_full(name, parts, reg, fulls, out):
    f = fulls[name]
    included = [parts[f['chast']]] + [parts[n] for n in f.get('vklyuchit') or []]
    names = {p['name'] for p in included}
    terms = []
    shutil.rmtree(f'{out}/{name}', ignore_errors=True)
    chunks = [f'---\ntitle: "{f.get("title") or included[0]["title"]}"\n---\n']
    for i, p in enumerate(included):
        def mention(m):
            n, text = m.groups()
            kind, key = n.split('.', 1)
            if kind == 'terminy':
                if key not in terms:
                    terms.append(key)
                return f'[{text or reg[kind][key]["title"]}](#term-{key})'
            if kind == 'resursy':
                return resource(reg, key, text)
            if n in names:
                return f'[{text or parts[n]["title"]}](#part-{n.replace(".", "-")})'
            return f'{text or parts[n]["title"]} *(нет в этом документе)*'

        def image(m, p=p):
            alt, img = m.groups()
            if re.match(r'[a-z]+:', img):
                return m.group(0)
            if not os.path.isfile(f'{p["dir"]}/{img}'):
                return f'*[нет снимка: {img}]*'
            rel = f'{name}/{p["sec"]}-{p["slug"]}/{img}'
            os.makedirs(os.path.dirname(f'{out}/{rel}'), exist_ok=True)
            shutil.copyfile(f'{p["dir"]}/{img}', f'{out}/{rel}')
            return f'![{alt}](<{rel}>)'

        body = outside_code(p['body'], lambda t: IMAGE.sub(image, MENTION.sub(mention, t)))
        chunks.append(('\n---\n\n' if i else '') + f'[]{{#part-{p["name"].replace(".", "-")}}}\n\n' + note(p) + body + '\n')
    if terms:
        chunks.append('\n---\n\n# Термины\n')
        for key in terms:
            t = reg['terminy'][key]
            chunks.append(f'[]{{#term-{key}}}**{t["title"]}** — {t["text"]}\n')
    text = '\n'.join(chunks)
    ids = ANCHOR.findall(prose(text))
    for dup in sorted({i for i in ids if ids.count(i) > 1}):
        print(f'  внимание: метка #{dup} встречается в сборке несколько раз')
    os.makedirs(out, exist_ok=True)
    open(f'{out}/{name}.md', 'w', encoding='utf-8').write(text)
    return len(included)


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
            sys.exit(f'FAIL: нет описания inst/src/full/{name}.yaml')
        out = arg('--out') or f'{INST}/full-out'
        print(f'собран полный документ {name}.md (частей: {build_full(name, parts, reg, fulls, out)})')
    else:
        out = arg('--out') or f'{INST}/dist'
        print(f'собран вид «репозиторий» (частей: {build_dist(parts, reg, out)})')


if __name__ == '__main__':
    main()
