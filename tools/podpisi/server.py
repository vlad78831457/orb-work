"""Редактор подписей на снимках: `make podpisi`, потом в браузере http://localhost:8765.

Стенд без экрана — с ноутбука пробросить порт: ssh -L 8765:localhost:8765 ag12. Сервер слушает только 127.0.0.1.
Видит снимки в inst/src/md-kod/**/imgs/, пишет рядом <снимок>.podpisi.yaml; сам снимок не меняет.
"""
import io
import json
import os
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SRC = os.path.join(ROOT, 'inst', 'src', 'md-kod')
sys.path.insert(0, os.path.join(ROOT, 'inst', 'src', 'skripty'))
import podpisi  # noqa: E402

EXT = ('.png', '.jpg', '.jpeg')
PORT = int(os.environ.get('PORT', '8765'))


def images():
    out = []
    for d, _, files in os.walk(SRC):
        if os.path.basename(d) != 'imgs':
            continue
        for f in sorted(files):
            if f.lower().endswith(EXT):
                full = os.path.join(d, f)
                out.append({'p': os.path.relpath(full, SRC), 'est': os.path.isfile(podpisi.yaml_of(full))})
    return sorted(out, key=lambda x: x['p'])


def resolve(rel):
    full = os.path.realpath(os.path.join(SRC, rel or ''))
    if not full.startswith(os.path.realpath(SRC) + os.sep) or not full.lower().endswith(EXT) or not os.path.isfile(full):
        raise FileNotFoundError(rel)
    return full


class Handler(BaseHTTPRequestHandler):
    def send(self, code, body, ctype='application/json; charset=utf-8'):
        if isinstance(body, str):
            body = body.encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', ctype)
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        u = urlparse(self.path)
        q = parse_qs(u.query).get('p', [''])[0]
        try:
            if u.path == '/':
                self.send(200, open(os.path.join(HERE, 'editor.html'), encoding='utf-8').read(), 'text/html; charset=utf-8')
            elif u.path == '/api/list':
                self.send(200, json.dumps(images(), ensure_ascii=False))
            elif u.path == '/api/podpisi':
                self.send(200, json.dumps(podpisi.load(resolve(q)) or {'metki': []}, ensure_ascii=False))
            elif u.path == '/img':
                full = resolve(q)
                self.send(200, open(full, 'rb').read(), 'image/png' if full.lower().endswith('.png') else 'image/jpeg')
            elif u.path == '/preview':
                full, buf = resolve(q), io.BytesIO()
                podpisi.render(full, podpisi.load(full) or {}, buf)
                self.send(200, buf.getvalue(), 'image/png')
            else:
                self.send(404, '{}')
        except FileNotFoundError:
            self.send(404, json.dumps({'oshibka': 'нет такого снимка'}, ensure_ascii=False))

    def do_POST(self):
        u = urlparse(self.path)
        if u.path != '/api/podpisi':
            return self.send(404, '{}')
        try:
            full = resolve(parse_qs(u.query).get('p', [''])[0])
            data = json.loads(self.rfile.read(int(self.headers.get('Content-Length', 0))) or b'{}')
            podpisi.save(full, data)
            self.send(200, json.dumps({'ok': True, 'oshibki': podpisi.check(full)}, ensure_ascii=False))
        except (FileNotFoundError, ValueError) as e:
            self.send(400, json.dumps({'oshibka': str(e)}, ensure_ascii=False))

    def log_message(self, *a):
        pass


if __name__ == '__main__':
    print(f'Редактор подписей: http://localhost:{PORT}  (с ноутбука: ssh -L {PORT}:localhost:{PORT} ag12). Остановить — Ctrl+C.')
    ThreadingHTTPServer(('127.0.0.1', PORT), Handler).serve_forever()
