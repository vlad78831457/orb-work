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
for md in $(find . -name '*.md' -not -path './.git/*' -not -path './raw/*/*' -not -path './inst/src/*' -not -path './inst/md-full-out/*'); do
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

sh tools/secrets.sh . || err "секреты в файлах"

[ "$fail" -eq 0 ] && echo "orb-work: ok"
exit "$fail"
