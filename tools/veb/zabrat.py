#!/usr/bin/env python3
"""Забрать JSON вебхука (tools/veb/Code.gs) на стенд: make veb-zabrat [IMYA=proekta] [LIST="5-5 Оформление сделок"].

Адрес и ключ — в ~/.config/orb-work/veb (создаёт директор, в Git не идёт, на экран не выводится):

    proekta_URL=https://script.google.com/macros/s/…/exec
    proekta_KEY=…

IMYA — имя таблицы в этом файле (proekta, oplat, …). Результат — raw/veb/<imya>-<дата>.json; на экран — только сводка:
листы, число ячеек и формул, маска (сколько можно / тег / нельзя / без разметки). Значений не печатает.
"""
import datetime
import json
import os
import sys
import urllib.parse
import urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
CONF = os.path.expanduser('~/.config/orb-work/veb')


def conf(imya):
    if not os.path.isfile(CONF):
        sys.exit(f'нет файла {CONF} — его создаёт директор (см. tools/veb/README.md)')
    vals = {}
    for line in open(CONF, encoding='utf-8'):
        line = line.strip()
        if line and not line.startswith('#') and '=' in line:
            k, v = line.split('=', 1)
            vals[k.strip()] = v.strip().strip('"\'')
    url, key = vals.get(f'{imya}_URL'), vals.get(f'{imya}_KEY')
    if not url or not key:
        sys.exit(f'в {CONF} нет {imya}_URL или {imya}_KEY')
    return url, key


def svodka(data):
    print(f'таблица «{data.get("tablica")}», листов {len(data.get("listy", []))}, легенда маски: {len(data.get("legenda", []))} цветов')
    for s in data.get('listy', []):
        cells = s.get('yacheyki', [])
        line = f'  {s["list"]}: ячеек {len(cells)}, формул {sum(1 for c in cells if c[3])}, заголовки в строке {s.get("stroka_zagolovkov")}'
        if 'maska' in s:
            m = s['maska']
            line += f'; маска — можно {m["mozhno"]}, тег {m["teg"]}, нельзя {m["nelzya"]}, без разметки {m["bez_razmetki"]}'
        print(line)


def main():
    imya = os.environ.get('IMYA') or 'proekta'
    url, key = conf(imya)
    q = {'key': key}
    if os.environ.get('LIST'):
        q['list'] = os.environ['LIST']
    try:
        with urllib.request.urlopen(url + ('&' if '?' in url else '?') + urllib.parse.urlencode(q), timeout=360) as r:
            body = r.read()
    except Exception as e:   # адрес и ключ в текст ошибки не попадают
        sys.exit(f'вебхук не ответил: {type(e).__name__} {getattr(e, "code", "")}')
    try:
        data = json.loads(body)
    except ValueError:
        sys.exit('вебхук ответил не JSON — проверь, что веб-приложение развёрнуто с доступом «все» (см. README)')
    if data.get('oshibka'):
        sys.exit(f'вебхук: {data["oshibka"]}')
    os.makedirs(f'{ROOT}/raw/veb', exist_ok=True)
    out = f'{ROOT}/raw/veb/{imya}-{datetime.date.today().isoformat()}.json'
    json.dump(data, open(out, 'w', encoding='utf-8'), ensure_ascii=False)
    svodka(data)
    print(f'сохранено: {os.path.relpath(out, ROOT)}')


if __name__ == '__main__':
    main()
