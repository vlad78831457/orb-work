"""Подписи на снимках: чистый снимок + файл подписей рядом, картинку с подписями рисует сборка.

imgs/01-menyu.png — чистый снимок; imgs/01-menyu.podpisi.yaml — подписи (их ставят в редакторе `make podpisi`):

    metki:
    - {vid: ramka, x: 10, y: 20, w: 200, h: 40, tekst: 'Доп.Меню'}
    - {vid: strelka, x1: 300, y1: 50, x2: 220, y2: 40}
    - {vid: nomer, x: 400, y: 60, n: 1, tekst: 'Пункт меню'}
    - {vid: tekst, x: 30, y: 300, tekst: 'Вставляйте только значения', cvet: sinij}
    - {vid: skryt, x: 500, y: 80, w: 160, h: 24, sposob: razmyt}

Координаты — в пикселях снимка. `tekst` у рамки, стрелки и номера — необязательный, пишется рядом.
`cvet` — один из COLORS (по умолчанию krasnyj). `skryt` прячет кусок снимка (почта, имена, цены):
`sposob: razmyt` — размыть, `zalit` — закрасить цветом `cvet` (по умолчанию серым); рисуется под остальными метками.
"""
import math
import os
import shutil

import yaml

COLORS = {'krasnyj': '#c0001a', 'oranzhevyj': '#ea580c', 'zhyoltyj': '#facc15', 'zelyonyj': '#15803d',
          'sinij': '#1d4ed8', 'fioletovyj': '#7e22ce', 'chyornyj': '#111111', 'belyj': '#ffffff', 'seryj': '#9ca3af'}
COLOR = (192, 0, 26)
WHITE = (255, 255, 255)
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FONT_BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
VIDY = ('ramka', 'strelka', 'nomer', 'tekst', 'skryt')
SPOSOBY = ('razmyt', 'zalit')


def yaml_of(img_path):
    return os.path.splitext(img_path)[0] + '.podpisi.yaml'


def load(img_path):
    path = yaml_of(img_path)
    if not os.path.isfile(path):
        return None
    return yaml.safe_load(open(path, encoding='utf-8')) or {}


class _Dumper(yaml.SafeDumper):
    pass


_Dumper.add_representer(str, lambda d, v: d.represent_scalar('tag:yaml.org,2002:str', v, style='|' if '\n' in v else None))


def save(img_path, data):
    metki = [{k: v for k, v in m.items() if v not in (None, '')} for m in data.get('metki', []) if m.get('vid') in VIDY]
    head = ('# Подписи к снимку ' + os.path.basename(img_path) + ' — ставятся в редакторе `make podpisi`, можно править руками.\n'
            '# Координаты — в пикселях снимка. Картинку с подписями рисует `make inst`; сам снимок не меняется.\n')
    body = yaml.dump({'metki': metki}, Dumper=_Dumper, allow_unicode=True, sort_keys=False, width=100000)
    open(yaml_of(img_path), 'w', encoding='utf-8').write(head + body)


def texts(data):
    """Тексты подписей по порядку — для раздела «Текст на фото»."""
    return [str(m['tekst']) for m in (data or {}).get('metki', []) if m.get('tekst')]


def check(img_path):
    """Ошибки файла подписей: неизвестный вид, нет нужных координат."""
    need = {'ramka': ('x', 'y', 'w', 'h'), 'strelka': ('x1', 'y1', 'x2', 'y2'), 'nomer': ('x', 'y', 'n'), 'tekst': ('x', 'y', 'tekst'),
            'skryt': ('x', 'y', 'w', 'h')}
    errors = []
    for i, m in enumerate((load(img_path) or {}).get('metki', []), 1):
        if m.get('vid') not in need:
            errors.append(f'метка {i}: неизвестный вид «{m.get("vid")}» (есть {", ".join(VIDY)})')
            continue
        miss = [k for k in need[m['vid']] if m.get(k) in (None, '')]
        if miss:
            errors.append(f'метка {i} ({m["vid"]}): нет {", ".join(miss)}')
        if m.get('cvet') and m['cvet'] not in COLORS:
            errors.append(f'метка {i}: неизвестный цвет «{m["cvet"]}» (есть {", ".join(COLORS)})')
        if m['vid'] == 'skryt' and m.get('sposob', 'razmyt') not in SPOSOBY:
            errors.append(f'метка {i}: неизвестный способ «{m["sposob"]}» (есть {", ".join(SPOSOBY)})')
    return errors


def rgb(name):
    h = COLORS.get(name, COLORS['krasnyj']).lstrip('#')
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def render(src, data, dst):
    from PIL import Image, ImageDraw, ImageFilter, ImageFont
    im = Image.open(src).convert('RGB')
    s = max(1.0, max(im.size) / 1000)   # толщина и шрифт растут вместе со снимком
    metki = (data or {}).get('metki', [])
    for m in metki:   # сначала прячем, потом рисуем поверх
        if m.get('vid') != 'skryt':
            continue
        box = tuple(int(round(float(v))) for v in (m['x'], m['y'], float(m['x']) + float(m['w']), float(m['y']) + float(m['h'])))
        if m.get('sposob', 'razmyt') == 'zalit':
            ImageDraw.Draw(im).rectangle(box, fill=rgb(m.get('cvet', 'seryj')))
        else:
            im.paste(im.crop(box).filter(ImageFilter.GaussianBlur(radius=8 * s)), box[:2])
    d = ImageDraw.Draw(im)
    lw, fs = round(3 * s), round(18 * s)
    font, bold = ImageFont.truetype(FONT, fs), ImageFont.truetype(FONT_BOLD, fs)

    def label(x, y, text, color=COLOR):
        if not text:
            return
        box = d.multiline_textbbox((x, y), str(text), font=font)
        pad = round(4 * s)
        x0 = min(max(0, box[0] - pad), im.width - (box[2] - box[0]) - 2 * pad)
        y0 = min(max(0, box[1] - pad), im.height - (box[3] - box[1]) - 2 * pad)
        dx, dy = x0 - (box[0] - pad), y0 - (box[1] - pad)
        d.rectangle((box[0] - pad + dx, box[1] - pad + dy, box[2] + pad + dx, box[3] + pad + dy), fill=WHITE, outline=color, width=max(1, lw // 2))
        d.multiline_text((x + dx, y + dy), str(text), font=font, fill=color)

    for m in metki:
        v, t, col = m.get('vid'), m.get('tekst'), rgb(m.get('cvet', 'krasnyj'))
        if v == 'ramka':
            x, y, w, h = (float(m[k]) for k in ('x', 'y', 'w', 'h'))
            d.rectangle((x, y, x + w, y + h), outline=col, width=lw)
            label(x, y + h + lw * 2, t, col)
        elif v == 'strelka':
            x1, y1, x2, y2 = (float(m[k]) for k in ('x1', 'y1', 'x2', 'y2'))
            d.line((x1, y1, x2, y2), fill=col, width=lw)
            a, L = math.atan2(y2 - y1, x2 - x1), 14 * s
            d.polygon([(x2, y2), (x2 - L * math.cos(a - 0.45), y2 - L * math.sin(a - 0.45)),
                       (x2 - L * math.cos(a + 0.45), y2 - L * math.sin(a + 0.45))], fill=col)
            label(x1, y1, t, col)
        elif v == 'nomer':
            x, y, r = float(m['x']), float(m['y']), 14 * s
            d.ellipse((x - r, y - r, x + r, y + r), fill=col, outline=WHITE, width=max(1, lw // 2))
            d.text((x, y), str(m.get('n', '')), font=bold, fill=(17, 17, 17) if m.get('cvet') in ('zhyoltyj', 'belyj') else WHITE, anchor='mm')
            label(x + r + 4 * s, y - r, t, col)
        elif v == 'tekst':
            label(float(m['x']), float(m['y']), t, col)
    im.save(dst, format='PNG')


def copy(src, dst):
    """Копия снимка в сборку: с подписями, если рядом есть файл подписей."""
    data = load(src)
    if data and data.get('metki'):
        render(src, data, dst)
    else:
        shutil.copyfile(src, dst)
