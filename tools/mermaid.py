#!/usr/bin/env python3
"""Проверка синтаксиса схем Mermaid в inst/md-out настоящим mermaid-cli (mmdc).

    make mermaid            — проверить новые и изменённые схемы
    make mermaid-setup      — поставить mmdc в .tools/ (Node.js нужен в системе)

Уже проверенные схемы запоминаются (.tools/mermaid-ok.txt, по хешу текста) — второй раз не рисуются.
Все новые схемы рисуются за один запуск браузера; если что-то сломано — по одной, чтобы назвать сломанную.
Нет mmdc — проверка пропускается (make test от неё не зависит).
"""
import glob
import hashlib
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = f'{ROOT}/.tools'
MMDC = f'{TOOLS}/node_modules/.bin/mmdc'
CACHE = f'{TOOLS}/mermaid-ok.txt'
BLOCK = re.compile(r'```mermaid\n(.*?)```', re.S)


def render(src, dst):
    env = {**os.environ, 'PUPPETEER_CACHE_DIR': f'{TOOLS}/puppeteer'}
    r = subprocess.run([MMDC, '-q', '-i', src, '-o', dst], env=env, capture_output=True, text=True)
    first = next((ln.strip() for ln in (r.stderr + r.stdout).splitlines() if ln.strip() and not ln.strip().startswith('at ')), '')
    return r.returncode == 0, first


def main():
    if not os.path.isfile(MMDC):
        print('mermaid: mmdc не установлен — пропуск (make mermaid-setup)')
        return 0
    blocks = []
    for f in sorted(glob.glob(f'{ROOT}/inst/md-out/**/*.md', recursive=True)):
        for i, b in enumerate(BLOCK.findall(open(f, encoding='utf-8').read())):
            blocks.append((os.path.relpath(f, ROOT), i + 1, b, hashlib.sha1(b.encode()).hexdigest()))
    ok = set(open(CACHE).read().split()) if os.path.isfile(CACHE) else set()
    todo = [x for x in blocks if x[3] not in ok]
    print(f'mermaid: схем {len(blocks)}, новых или изменённых {len(todo)}')
    if not todo:
        return 0
    bad = []
    with tempfile.TemporaryDirectory() as tmp:
        md = f'{tmp}/all.md'
        open(md, 'w', encoding='utf-8').write(''.join(f'```mermaid\n{b}```\n\n' for _, _, b, _ in todo))
        passed, _ = render(md, f'{tmp}/out.md')
        if passed:
            good = todo
        else:   # кто-то сломан — по одной, чтобы назвать
            good = []
            for x in todo:
                src = f'{tmp}/one.mmd'
                open(src, 'w', encoding='utf-8').write(x[2])
                fine, why = render(src, f'{tmp}/one.svg')
                (good if fine else bad).append(x if fine else (x, why))
    with open(CACHE, 'a') as c:
        c.write(''.join(h + '\n' for _, _, _, h in good))
    for (f, i, _, _), why in bad:
        print(f'FAIL: {f}, схема {i}: {why}')
    print('mermaid: ok' if not bad else f'mermaid: сломано схем — {len(bad)}')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
