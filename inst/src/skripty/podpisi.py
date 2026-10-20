"""Подписи на снимках: чистый снимок + файл подписей рядом, картинку с подписями рисует сборка.

imgs/01-menyu.png — чистый снимок; imgs/01-menyu.podpisi.yaml — подписи (их ставят в редакторе `make podpisi`):

    metki:
    - {vid: ramka, x: 10, y: 20, w: 200, h: 40, tekst: 'Доп.Меню'}
    - {vid: strelka, x1: 300, y1: 50, x2: 220, y2: 40}
    - {vid: nomer, x: 400, y: 60, n: 1, tekst: 'Пункт меню'}
    - {vid: tekst, x: 30, y: 300, tekst: 'Вставляйте только значения'}

Координаты — в пикселях снимка. `tekst` у рамки, стрелки и номера — необязательный, пишется рядом.
"""
import math
import os
import shutil

import yaml

COLOR = (192, 0, 26)
WHITE = (255, 255, 255)
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FONT_BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
VIDY = ('ramka', 'strelka', 'nomer', 'tekst')


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
    need = {'ramka': ('x', 'y', 'w', 'h'), 'strelka': ('x1', 'y1', 'x2', 'y2'), 'nomer': ('x', 'y', 'n'), 'tekst': ('x', 'y', 'tekst')}
    errors = []
    for i, m in enumerate((load(img_path) or {}).get('metki', []), 1):
        if m.get('vid') not in need:
            errors.append(f'метка {i}: неизвестный вид «{m.get("vid")}» (есть {", ".join(VIDY)})')
            continue
        miss = [k for k in need[m['vid']] if m.get(k) in (None, '')]
        if miss:
            errors.append(f'метка {i} ({m["vid"]}): нет {", ".join(miss)}')
    return errors


def render(src, data, dst):
    from PIL import Image, ImageDraw, ImageFont
    im = Image.open(src).convert('RGB')
    d = ImageDraw.Draw(im)
    s = max(1.0, max(im.size) / 1000)   # толщина и шрифт растут вместе со снимком
    lw, fs = round(3 * s), round(18 * s)
    font, bold = ImageFont.truetype(FONT, fs), ImageFont.truetype(FONT_BOLD, fs)

    def label(x, y, text):
        if not text:
            return
        box = d.multiline_textbbox((x, y), str(text), font=font)
        pad = round(4 * s)
        x0 = min(max(0, box[0] - pad), im.width - (box[2] - box[0]) - 2 * pad)
        y0 = min(max(0, box[1] - pad), im.height - (box[3] - box[1]) - 2 * pad)
        dx, dy = x0 - (box[0] - pad), y0 - (box[1] - pad)
        d.rectangle((box[0] - pad + dx, box[1] - pad + dy, box[2] + pad + dx, box[3] + pad + dy), fill=WHITE, outline=COLOR, width=max(1, lw // 2))
        d.multiline_text((x + dx, y + dy), str(text), font=font, fill=COLOR)

    for m in (data or {}).get('metki', []):
        v, t = m.get('vid'), m.get('tekst')
        if v == 'ramka':
            x, y, w, h = (float(m[k]) for k in ('x', 'y', 'w', 'h'))
            d.rectangle((x, y, x + w, y + h), outline=COLOR, width=lw)
            label(x, y + h + lw * 2, t)
        elif v == 'strelka':
            x1, y1, x2, y2 = (float(m[k]) for k in ('x1', 'y1', 'x2', 'y2'))
            d.line((x1, y1, x2, y2), fill=COLOR, width=lw)
            a, L = math.atan2(y2 - y1, x2 - x1), 14 * s
            d.polygon([(x2, y2), (x2 - L * math.cos(a - 0.45), y2 - L * math.sin(a - 0.45)),
                       (x2 - L * math.cos(a + 0.45), y2 - L * math.sin(a + 0.45))], fill=COLOR)
            label(x1, y1, t)
        elif v == 'nomer':
            x, y, r = float(m['x']), float(m['y']), 14 * s
            d.ellipse((x - r, y - r, x + r, y + r), fill=COLOR, outline=WHITE, width=max(1, lw // 2))
            d.text((x, y), str(m.get('n', '')), font=bold, fill=WHITE, anchor='mm')
            label(x + r + 4 * s, y - r, t)
        elif v == 'tekst':
            label(float(m['x']), float(m['y']), t)
    im.save(dst, format='PNG')


def copy(src, dst):
    """Копия снимка в сборку: с подписями, если рядом есть файл подписей."""
    data = load(src)
    if data and data.get('metki'):
        render(src, data, dst)
    else:
        shutil.copyfile(src, dst)
