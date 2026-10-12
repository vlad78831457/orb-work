#!/usr/bin/env python3
"""Сборщик инструкций из частей (inst/src → inst/dist/full).

Часть — папка inst/src/<имя>/ с файлом index.md и шапкой YAML: id, title, requires.
Упоминание другой части — обычная ссылка [текст](../<имя>/index.md): на GitHub она работает как есть.
Полный вид: инструкция и все её зависимости в одном файле, ссылки на части ведут внутрь файла.

  inst_compile.py --check     только проверка
  inst_compile.py             проверка и сборка inst/dist/full/<имя>.md
"""
import os
import re
import sys

import yaml

SRC = 'inst/src'
OUT = 'inst/dist/full'
LINK = re.compile(r'(!?)\[((?:[^\[\]]|\[[^\]]*\])*)\]\(([^)\s]+)\)')
ANCHOR = re.compile(r'\{#([^}\s]+)')


def load():
    parts, errors = {}, []
    for name in sorted(os.listdir(SRC)):
        path = f'{SRC}/{name}/index.md'
        if not os.path.isfile(path):
            continue
        text = open(path, encoding='utf-8').read()
        m = re.match(r'---\n(.*?)\n---\n', text, re.S)
        if not m:
            errors.append(f'{path}: нет шапки YAML')
            continue
        head = yaml.safe_load(m.group(1)) or {}
        pid = head.get('id')
        if not pid or not head.get('title'):
            errors.append(f'{path}: в шапке нужны id и title')
            continue
        if any(p['id'] == pid for p in parts.values()):
            errors.append(f'{path}: id {pid} уже занят')
        parts[name] = {'id': pid, 'title': head['title'], 'requires': head.get('requires') or [],
                       'name': name, 'body': text[m.end():]}
    return parts, errors


def target(part, link):
    """Имя части, на которую ведёт ссылка, или None."""
    path = link.split('#')[0]
    if not path or re.match(r'[a-z]+:', path):
        return None
    norm = os.path.normpath(f'{SRC}/{part["name"]}/{path}')
    m = re.fullmatch(re.escape(SRC) + r'/([^/]+)/index\.md', norm)
    return m.group(1) if m else None


def check(parts):
    errors, warnings = [], []
    by_id = {p['id']: p for p in parts.values()}
    for p in parts.values():
        where = f'{SRC}/{p["name"]}/index.md'
        for r in p['requires']:
            if r not in by_id:
                errors.append(f'{where}: в requires нет такой части — {r}')
        used = set()
        for img, _, link in LINK.findall(p['body']):
            path = link.split('#')[0]
            if not path or re.match(r'[a-z]+:', path):
                continue
            t = target(p, link)
            if img:
                if not os.path.isfile(f'{SRC}/{p["name"]}/{path}'):
                    errors.append(f'{where}: нет снимка {path}')
            elif t is None or t not in parts:
                errors.append(f'{where}: ссылка ведёт не на часть — {link}')
            else:
                used.add(parts[t]['id'])
                if parts[t]['id'] not in p['requires']:
                    errors.append(f'{where}: упомянута часть {parts[t]["id"]}, но её нет в requires')
        for r in p['requires']:
            if r in by_id and r not in used:
                warnings.append(f'{where}: {r} есть в requires, но в тексте не упомянута')
        own = set(ANCHOR.findall(p['body']))
        for link in re.findall(r'\]\(#([^)\s]+)\)', p['body']):
            if link not in own:
                warnings.append(f'{where}: ссылка в никуда — #{link}')
    for p in parts.values():  # зависимости по кругу
        try:
            closure(p, by_id)
        except RecursionError:
            errors.append(f'{SRC}/{p["name"]}/index.md: зависимости замкнуты в круг')
    return errors, warnings


def closure(part, by_id, seen=None, stack=()):
    """Все зависимости части по порядку первого упоминания, каждая один раз."""
    seen = [] if seen is None else seen
    if part['id'] in stack:
        raise RecursionError
    for r in part['requires']:
        dep = by_id.get(r)
        if dep and dep not in seen:
            seen.append(dep)
            closure(dep, by_id, seen, stack + (part['id'],))
    return seen


def anchor(pid):
    return 'part-' + pid.replace('.', '-')


def inline(part, parts):
    """Текст части для полного вида: ссылки на части — внутрь файла, снимки — к исходной папке."""
    def repl(m):
        img, text, link = m.groups()
        path, _, frag = link.partition('#')
        if not path or re.match(r'[a-z]+:', path):
            return m.group(0)
        if img:
            return f'![{text}](../../src/{part["name"]}/{path})'
        t = target(part, link)
        return f'[{text}](#{frag or anchor(parts[t]["id"])})'
    return LINK.sub(repl, part['body'])


def build(parts):
    by_id = {p['id']: p for p in parts.values()}
    os.makedirs(OUT, exist_ok=True)
    built = []
    for p in parts.values():
        if not p['id'].startswith('instructions.'):
            continue
        deps = closure(p, by_id)
        chunks = [f'---\ntitle: "{p["title"]}"\n---\n', inline(p, parts)]
        for d in deps:
            chunks.append(f'\n\n---\n\n[]{{#{anchor(d["id"])}}}\n\n' + inline(d, parts))
        text = '\n'.join(chunks)
        ids = ANCHOR.findall(text)
        for dup in sorted({i for i in ids if ids.count(i) > 1}):
            print(f'  внимание: {p["name"]}: метка #{dup} встречается в сборке несколько раз')
        open(f'{OUT}/{p["name"]}.md', 'w', encoding='utf-8').write(text)
        built.append((p['name'], len(deps)))
    return built


def main():
    parts, errors = load()
    e, warnings = check(parts)
    errors += e
    for w in warnings:
        print('  внимание:', w)
    for e in errors:
        print('FAIL:', e)
    if errors:
        sys.exit(1)
    if '--check' in sys.argv:
        print(f'inst: частей {len(parts)}, ошибок нет')
        return
    for name, n in build(parts):
        print(f'собрано {OUT}/{name}.md (зависимостей: {n})')


if __name__ == '__main__':
    main()
