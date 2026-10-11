#!/bin/sh
# Проверка orb-work: обязательные файлы, ссылки, секреты.
set -eu
cd "$(dirname "$0")/.."
fail=0
err() { echo "FAIL: $*"; fail=1; }

for f in README.md STATUS.md GOALS.md CHANGELOG.md think/README.md raw/README.md; do
  [ -f "$f" ] || err "нет файла $f"
done

# Относительные ссылки.
for md in $(find . -name '*.md' -not -path './.git/*' -not -path './raw/*/*'); do
  dir=$(dirname "$md")
  grep -o '](\([^)#]*\)[^)]*)' "$md" | sed 's/^](\([^)#]*\).*/\1/' | while read -r link; do
    case "$link" in ''|http://*|https://*|mailto:*) continue ;; esac
    [ -e "$dir/$link" ] || echo "FAIL: $md → $link"
  done
done > /tmp/links
[ ! -s /tmp/links ] || { cat /tmp/links; fail=1; }

sh tools/secrets.sh . || err "секреты в файлах"

[ "$fail" -eq 0 ] && echo "orb-work: ok"
exit "$fail"
