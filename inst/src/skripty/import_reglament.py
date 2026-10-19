#!/usr/bin/env python3
"""Регламент «Распределение задач» (xlsx) → reglament.yaml по процессам: «как записано», без толкования.

    python3 inst/src/skripty/import_reglament.py <xlsx> [--out inst/src/md-kod/pro] [--check]

Роли в регламенте отмечены цветом ячеек (легенда в E2…E4) и текстом в ячейке. Файл xlsx в Git не идёт (raw/);
в Git идут только тексты шагов — имена сотрудников и адреса почты заменяются (NAMES, EMAIL).
Пишет только reglament.yaml и папки процессов; protsess.yaml (наше толкование) не трогает.
--check — ничего не пишет, сверяет с тем, что уже лежит в --out.
"""
import collections
import datetime
import html
import os
import re
import sys
import zipfile

import yaml

SHEET = '10.10.2026 Версия К'
FOLDERS_SHEET = 'Структура папок'
# столбец регламента → как он подписан; K и M подписаны именами — здесь буквы
COLUMNS = {'H': 'Менеджер', 'I': 'ТС (эксперт)', 'J': 'Закупщик', 'K': 'K', 'L': 'АС', 'M': 'M', 'N': 'Владелец процесса'}
COLORS = {'FF00FF00': 'исполнитель', 'FFFFFF00': 'соисполнитель', 'FF00FFFF': 'функция менеджера проекта'}
# процессы по порядку в регламенте: заголовок в столбце B → папка и код шагов
PROCESSES = [
    ('Передача в контрактацию', 'r01-peredacha-v-kontraktatsiyu', 'pk'),
    ('КОНТРАКТАЦИЯ', 'r02-kontraktatsiya', 'kt'),
    ('ПЕРЕДАЧА В ЗАКУПКИ', 'r03-peredacha-v-zakupki', 'pz'),
    ('ЗАКУПКА ТОВАРА', 'r04-zakupka-tovara', 'zk'),
    ('ПЛАНИРОВАНИЕ И КОНТРОЛЬ ИСПОЛНЕНИЯ', 'r05-planirovanie-ispolneniya', 'pl'),
    ('ПОСТУПЛЕНИЕ', 'r06-postuplenie', 'ps'),
    ('ПОДГОТОВКА К ОТГРУЗКЕ', 'r07-podgotovka-k-otgruzke', 'po'),
    ('ОТГРУЗКА', 'r08-otgruzka', 'og'),
    ('ОФОРМЛЕНИЕ ЭКСПОРТА', 'r09-oformlenie-eksporta', 'ek'),
    ('ИСПОЛНЕНИЕ (устранение несоответствий)', 'r10-nesootvetstviya', 'ns'),
    ('КОНТРОЛЬ ИСПОЛНЕНИЯ ЗАКАЗЧИКОМ', 'r11-kontrol-zakazchika', 'kz'),
    ('ЗАКРЫТИЕ ПРОЕКТА', 'r12-zakrytie-proekta', 'zp'),
]
# имена сотрудников → как в столбцах регламента; кого не знаем — «[сотрудник]»
NAMES = [
    (r'Виталь?[июяе]м?\b|Виталий\b|Виталию\b|Виталия\b', 'K'),
    (r'С\.?\s?Ю\.?\s?/\s?А\.?\s?Н\.?|\bСЮ\b', 'M'),
    (r'Татьян[аеуы]?(\s+Пиц)?', '[сотрудник контура 2]'),
    (r'Юл[еияю]\b|Юля\b', '[логист]'),
    (r'Антон[ау]?\b|Антоном\b', '[сотрудник]'),
    (r'Владимир[ау]?\b', '[сотрудник]'),
    (r'Артем[ау]?\b|Артём[ау]?\b', '[сотрудник]'),
]
EMAIL = re.compile(r'[\w.+-]+@[\w-]+\.[\w.-]+')
URL = re.compile(r'https?://\S+')


def clean(text):
    text = html.unescape(text or '').replace('\r', '')
    text = EMAIL.sub('[почта]', URL.sub('[ссылка]', text))
    for pattern, repl in NAMES:
        text = re.sub(pattern, repl, text, flags=re.I)
    text = re.sub(r'[ \t]+', ' ', text)
    return re.sub(r'\n\s*\n+', '\n', text).strip()


def number(raw):
    """Номер шага: Excel превратил «1.1» в дату — вернуть как было."""
    if not raw:
        return ''
    try:
        f = float(raw)
    except ValueError:
        return ''   # в столбце номера бывает название подраздела — его берёт processes()
    if f > 1000:
        d = datetime.date(1899, 12, 30) + datetime.timedelta(days=int(f))
        return f'{d.day}.{d.month}'
    return str(int(f)) if f == int(f) else str(f)


class Book:
    def __init__(self, path):
        self.z = zipfile.ZipFile(path)
        st = self.z.read('xl/styles.xml').decode()
        fills = re.findall(r'<fill>(.*?)</fill>', st, re.S)
        rgb = lambda f: (re.search(r'fgColor rgb="([0-9A-F]+)"', f) or [None, ''])[1] if 'none' not in f else ''
        xfs = re.findall(r'<xf [^>]*?(?:/>|>.*?</xf>)', re.search(r'<cellXfs[^>]*>(.*?)</cellXfs>', st, re.S).group(1), re.S)
        self.fill = [rgb(fills[int(m.group(1))]) if (m := re.search(r'fillId="(\d+)"', x)) else '' for x in xfs]
        ss = self.z.read('xl/sharedStrings.xml').decode() if 'xl/sharedStrings.xml' in self.z.namelist() else ''
        self.strings = [html.unescape(''.join(re.findall(r'<t[^>]*>([^<]*)</t>', si))) for si in re.findall(r'<si>(.*?)</si>', ss, re.S)]
        wb = self.z.read('xl/workbook.xml').decode()
        rels = self.z.read('xl/_rels/workbook.xml.rels').decode()
        target = {}
        for rel in re.findall(r'<Relationship [^>]*>', rels):
            target[re.search(r'Id="([^"]+)"', rel).group(1)] = re.search(r'Target="([^"]+)"', rel).group(1)
        self.sheets = {}
        for name, rid in re.findall(r'<sheet [^>]*name="([^"]+)"[^>]*r:id="([^"]+)"', wb):
            t = target[rid].lstrip('/')
            self.sheets[html.unescape(name).strip()] = t if t.startswith('xl/') else 'xl/' + t

    def rows(self, sheet):
        """{номер строки: {столбец: (значение, цвет)}}; лист ищется по началу имени (в имени бывает дата)"""
        name = next(n for n in self.sheets if n.startswith(sheet))
        x = self.z.read(self.sheets[name]).decode(errors='ignore')
        out = {}
        for r in re.findall(r'<row [^>]*>(.*?)</row>', x, re.S):
            cells = {}
            for attrs, body in re.findall(r'<c ([^>]*?)(?:/>|>(.*?)</c>)', r, re.S):
                col, row = re.search(r'r="([A-Z]+)(\d+)"', attrs).groups()
                s = re.search(r' s="(\d+)"', attrs)
                v = re.search(r'<v>([^<]*)</v>', body or '')
                t = re.search(r'<t[^>]*>([^<]*)</t>', body or '')
                val = v.group(1) if v else (t.group(1) if t else '')
                if 't="s"' in attrs and v:
                    val = self.strings[int(val)]
                cells[col] = (val.strip(), self.fill[int(s.group(1))] if s else '')
            out[int(row)] = cells
        return out


def mark(cell):
    """Отметка роли: цвет и/или текст ячейки → строка как в регламенте."""
    val, color = cell
    kind = COLORS.get(color, '')
    text = clean(val)
    if kind and text and text.lower() != kind:
        return f'{kind}: {text}'
    return kind or text


def processes(book):
    """Строки листа → процессы и шаги. Заголовок процесса — в столбце B; подраздел («Доплаты», «Контроль поставки»)
    — строка без номера и без отметок; строка без номера, но с отметками или примечанием — шаг без номера."""
    rows = book.rows(SHEET)
    found, cur, razdel = [], None, None
    for n in sorted(r for r in rows if r >= 9):
        c = rows[n]
        get = lambda col: clean(c.get(col, ('', ''))[0])
        head, num, title = get('B'), number(c.get('C', ('', ''))[0]), get('D')
        kolonki = {col: m for col in COLUMNS if col in c and (m := mark(c[col]))}
        proc = next((p for p in PROCESSES if head.upper().startswith(p[0].upper())), None) if head else None
        if proc:
            cur, razdel = {'title': head, 'slug': proc[1], 'code': proc[2], 'shagi': []}, None
            found.append(cur)
        elif head:
            razdel = head.rstrip(':').strip()
        sub = get('C') if not num else ''   # подраздел в столбце номера: «Контроль поставки», «Доплаты», «ПРИЕМКА:»
        if sub:
            razdel = sub.rstrip(':').strip()
        if not title and kolonki and (sub or (head and not proc)):
            title = razdel   # у подраздела отмечен исполнитель — сохраняем как шаг без номера
        if cur is None or not title:
            continue
        if not num and not kolonki and not get('E') and not get('F'):
            razdel = title
            continue
        step = {'stroka': n, 'nomer': num, 'title': title}
        if razdel:
            step['razdel'] = razdel
        for col, key in (('E', 'primechanie'), ('F', 'v_sisteme'), ('G', 'izmeneniya')):
            if get(col):
                step[key] = get(col)
        if kolonki:
            step['kolonki'] = kolonki
        cur['shagi'].append(step)
    for p in found:   # id шага: код процесса + номер; без номера — x1, x2…; повтор номера — с буквой
        seen, extra = {}, 0
        for i, st in enumerate(p['shagi']):
            if not st['nomer']:
                extra += 1
                base = f'{p["code"]}-x{extra}'
            else:
                base = f'{p["code"]}-{st["nomer"].replace(".", "-")}'
            seen[base] = seen.get(base, 0) + 1
            p['shagi'][i] = {'id': base if seen[base] == 1 else f'{base}{chr(ord("a") + seen[base] - 1)}', **st}
    return found


def folders(book):
    rows = book.rows(FOLDERS_SHEET)
    out = []
    for n in sorted(rows):
        if n < 5:
            continue
        c = rows[n]
        levels = [(i + 1, clean(c[col][0])) for i, col in enumerate('ABCDE') if c.get(col, ('', ''))[0]]
        if not levels:
            continue
        lvl, name = levels[0]
        item = {'stroka': n, 'uroven': lvl, 'papka': name}
        for col, key in (('G', 'sozdaet'), ('H', 'napolnyaet'), ('I', 'primechanie')):
            if c.get(col, ('', ''))[0]:
                item[key] = clean(c[col][0])
        out.append(item)
    return out


def dump(data):
    return yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=100000, default_flow_style=False)


def main():
    args = sys.argv[1:]
    if not args or args[0].startswith('-'):
        sys.exit(__doc__)
    book = Book(args[0])
    out = args[args.index('--out') + 1] if '--out' in args else 'inst/src/md-kod/pro'
    head = (f'# Сгенерировано: inst/src/skripty/import_reglament.py из «{os.path.basename(args[0])}», лист «{SHEET}».\n'
            '# Руками не править — толкование шагов в protsess.yaml рядом.\n'
            '# kolonki — отметки в столбцах регламента как есть: ' + ', '.join(f'{k} {v}' for k, v in COLUMNS.items()) + '.\n')
    procs = processes(book)
    total = sum(len(p['shagi']) for p in procs)
    print(f'процессов: {len(procs)}, шагов: {total}')
    for col, name in COLUMNS.items():   # сверка с регламентом: сколько каких отметок в каждом столбце
        marks = collections.Counter(st['kolonki'][col].split(':')[0] for pr in procs for st in pr['shagi'] if col in st.get('kolonki', {}))
        print(f'  {col} {name}: ' + ', '.join(f'{k} {v}' for k, v in sorted(marks.items())))
    files = {f'{out}/{p["slug"]}/reglament.yaml': head + dump({'process': p['title'], 'shagi': p['shagi']}) for p in procs}
    files[f'{out}/papki.yaml'] = (head.split('\n# kolonki')[0].replace(f'лист «{SHEET}»', f'лист «{FOLDERS_SHEET}»')
                                  + '\n# Структура папок проекта: уровень, кто создаёт и кто наполняет.\n' + dump(folders(book)))
    stale = []
    for path, text in files.items():
        old = open(path, encoding='utf-8').read() if os.path.isfile(path) else None
        if '--check' in args:
            if old != text:
                stale.append(path)
            continue
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, 'w', encoding='utf-8').write(text)
    if stale:
        print('устарело: ' + ', '.join(stale))
        sys.exit(1)


if __name__ == '__main__':
    main()
