#!/bin/sh
# Проверка orb-work: обязательные файлы, ссылки, части инструкций, секреты.
set -eu
cd "$(dirname "$0")/.."
fail=0
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
err() { echo "FAIL: $*"; fail=1; }

for f in README.md STATUS.md GOALS.md CHANGELOG.md think/README.md raw/README.md; do
  [ -f "$f" ] || err "нет файла $f"
done

# Относительные ссылки.
for md in $(find . -name '*.md' -not -path './.git/*' -not -path './.tools/*' -not -path './raw/*/*' -not -path './inst/src/*' -not -path './inst/md-full-out/*'); do
  dir=$(dirname "$md")
  grep -o '](\([^)#]*\)[^)]*)' "$md" | sed 's/^](\([^)#]*\).*/\1/' | while read -r link; do
    link=${link#<}; link=${link%>}
    case "$link" in ''|http://*|https://*|mailto:*) continue ;; esac
    [ -e "$dir/$link" ] || echo "FAIL: $md → $link"
  done
done > "$tmp/links"
[ ! -s "$tmp/links" ] || { cat "$tmp/links"; fail=1; }

# Части инструкций: проверка и сверка inst/md-out со свежей сборкой.
if python3 inst/src/skripty/sobrat.py --out "$tmp/dist" > "$tmp/sobrat" 2>&1; then
  diff -rq "$tmp/dist" inst/md-out > "$tmp/distdiff" 2>&1 || { head -n 10 "$tmp/distdiff"; err "inst/md-out устарел — запусти make inst"; }
else
  cat "$tmp/sobrat"; err "части инструкций (inst/src)"
fi

# Шаги процессов совпадают с регламентом (если xlsx регламента есть на стенде; raw в Git не идёт).
reglament=$(find raw -name '*Распределение задач*.xlsx' 2>/dev/null | sort | tail -n 1)
if [ -n "$reglament" ]; then
  python3 inst/src/skripty/import_reglament.py "$reglament" --check > "$tmp/regl" 2>&1 || { tail -n 2 "$tmp/regl"; err "pro/*/reglament.yaml не совпадает с регламентом — make reglament X=…"; }
fi

# Устройство листов совпадает с таблицами (если xlsx таблиц есть на стенде).
lp=$(find raw -name '*Чистая таблица*.xlsx' 2>/dev/null | sort | tail -n 1)
lo=$(find raw -name '*ТАБЛИЦА ОПЛАТ*.xlsx' 2>/dev/null | sort | tail -n 1)
if [ -n "$lp" ] && [ -n "$lo" ]; then
  python3 inst/src/skripty/import_listy.py --check proekta="$lp" oplat="$lo" > "$tmp/listy" 2>&1 || { tail -n 2 "$tmp/listy"; err "lis/*/struktura.yaml не совпадает с таблицами — make listy"; }
fi

# Книга регламента (xlsx) выгружается и читается без потерь — если на стенде есть openpyxl.
if python3 -c 'import openpyxl' 2>/dev/null; then
  python3 inst/src/skripty/reglament_xlsx.py --check > "$tmp/xlsx" 2>&1 || { tail -n 5 "$tmp/xlsx"; err "книга регламента: выгрузка и чтение расходятся"; }
fi

# Вебхук: Code.gs под node на заглушке Таблиц — данные не уходят, маска и теги верны, импорт читает результат.
if command -v node >/dev/null 2>&1; then
  if node tools/veb/proba.js > "$tmp/veb.json" 2> "$tmp/veb.err"; then
    python3 -c 'import sys; sys.path.insert(0, "inst/src/skripty"); import import_listy as il; s = il.VebBook(sys.argv[1]).sheet("5-5 Проба"); assert s["karkas"] and s["stroka_zagolovkov"] == 10, s' "$tmp/veb.json" > "$tmp/veb.err" 2>&1 || { tail -n 3 "$tmp/veb.err"; err "вебхук: импорт JSON"; }
  else
    cat "$tmp/veb.err"; err "вебхук: проба Code.gs"
  fi
fi

sh tools/secrets.sh . || err "секреты в файлах"

[ "$fail" -eq 0 ] && echo "orb-work: ok"
exit "$fail"
