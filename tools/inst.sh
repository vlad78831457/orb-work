#!/bin/sh
# Сборка инструкций в .docx (запускается в контейнере Pandoc: make inst).
# Каждая папка в src/ — одна инструкция: берётся index.md, а если его нет — единственный .md.
set -eu
SRC=raw/2026-10-11-inst/src
REF=raw/2026-10-11-inst/templates/custom-reference-c.docx
OUT=inst/dist
fail=0
for d in "$SRC"/*/; do
  name=$(basename "$d")
  case "$name" in *"(Копия)"*) continue ;; esac
  md="$d/index.md"
  if [ ! -f "$md" ]; then
    [ "$(find "$d" -maxdepth 1 -name '*.md' | wc -l)" -eq 1 ] || continue
    md=$(find "$d" -maxdepth 1 -name '*.md')
  fi
  if pandoc "$md" --from markdown --reference-doc="$REF" --resource-path="$d" -o "$OUT/$name.docx" 2> /tmp/err; then
    warn=$(grep -c 'WARNING' /tmp/err || true)
    [ "$warn" -eq 0 ] && echo "ok    $name.docx" || echo "ok    $name.docx  (предупреждений: $warn)"
    grep 'WARNING' /tmp/err | sed 's/^/        /' | head -n 5
  else
    echo "FAIL  $name"; sed 's/^/        /' /tmp/err; fail=1
  fi
done
exit $fail
