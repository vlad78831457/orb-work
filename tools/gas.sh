#!/bin/sh
# Скрипты Apps Script через clasp. Код таблиц компании — только в raw/gas/<имя>/ (в Git не идёт).
#   gas.sh login                 — вход (делает директор; токен в ~/.clasprc.json, его никто не открывает)
#   gas.sh pull ID NAME          — скачать проект scriptId в raw/gas/NAME (первый раз — clone, дальше — pull)
#   gas.sh kopiya NAME           — пометить raw/gas/NAME как копию для опытов (только после этого можно push)
#   gas.sh push NAME             — записать raw/gas/NAME обратно; без пометки «копия» — отказ
#   gas.sh veb NAME              — добавить вебхук tools/veb в копию NAME (рядом с её кодом, ничего не удаляя) и push
set -eu
cd "$(dirname "$0")/.."
CLASP=.tools/clasp/node_modules/.bin/clasp
[ -x "$CLASP" ] || { echo "нет clasp — make clasp-setup"; exit 1; }
cmd=${1:-}
case "$cmd" in
  login) exec "$CLASP" login --no-localhost ;;
  pull)
    id=${2:?scriptId}; name=${3:?имя}; dir=raw/gas/$name
    if [ -f "$dir/.clasp.json" ]; then (cd "$dir" && "../../../$CLASP" pull)
    else mkdir -p "$dir" && (cd "$dir" && "../../../$CLASP" clone "$id"); fi
    echo "скачано в $dir: $(find "$dir" -type f ! -name '.clasp.json' ! -name '.kopiya' | wc -l) файлов" ;;
  kopiya)
    dir=raw/gas/${2:?имя}; [ -f "$dir/.clasp.json" ] || { echo "нет $dir — сначала pull"; exit 1; }
    date +%F > "$dir/.kopiya"; echo "$dir помечен как копия" ;;
  push|veb)
    dir=raw/gas/${2:?имя}
    [ -f "$dir/.kopiya" ] || { echo "отказ: $dir не помечен копией (gas.sh kopiya ${2}) — в рабочие таблицы не пишем"; exit 1; }
    if [ "$cmd" = veb ]; then
      if grep -lE 'function[[:space:]]+doGet[[:space:]]*\(' "$dir"/*.js "$dir"/*.gs 2>/dev/null | grep -v orb_veb; then
        echo "отказ: в коде копии уже есть doGet — два веб-приложения в одном проекте не уживутся"; exit 1
      fi
      cp tools/veb/Code.gs "$dir/orb_veb.js"
      python3 - "$dir/appsscript.json" tools/veb/appsscript.json <<'PY'
import json, sys
own, veb = json.load(open(sys.argv[1])), json.load(open(sys.argv[2]))
own.setdefault('webapp', veb['webapp'])
scopes = own.get('oauthScopes')
if scopes is not None and not any('spreadsheets' in s for s in scopes):
    scopes += veb['oauthScopes']
json.dump(own, open(sys.argv[1], 'w'), ensure_ascii=False, indent=2)
PY
      echo "вебхук добавлен в $dir (orb_veb.js, webapp в appsscript.json)"
    fi
    (cd "$dir" && "../../../$CLASP" push -f) ;;
  *) sed -n '2,8p' "$0"; exit 1 ;;
esac
