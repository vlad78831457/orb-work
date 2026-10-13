#!/bin/sh
# Полный документ → .docx. Вручную: make docx F=tio.tov-razdelenie (или F=<имя из inst/src/full>).
# Pandoc идёт в Docker на одном ядре; шаблон оформления — inst/src/skripty/custom-reference-c.docx.
set -eu
cd "$(dirname "$0")/.."
name=$1
case "$name" in *.*) rel="${name%%.*}/${name#*.}" ;; *) rel="full/$name" ;; esac
md="inst/md-full-out/$rel.md"
ref="inst/src/skripty/custom-reference-c.docx"
[ -f "$md" ] || { echo "FAIL: нет $md — сначала make full F=$name"; exit 1; }
[ -f "$ref" ] || { echo "FAIL: нет шаблона оформления $ref"; exit 1; }
mkdir -p "$(dirname "inst/docx/$rel")"
docker run --rm --cpus 1 --user "$(id -u):$(id -g)" -v "$PWD":/orb:ro -v "$PWD/inst/docx":/orb/inst/docx -w /orb \
  pandoc/core:3.6 "$md" --from markdown --reference-doc="$ref" --resource-path="$(dirname "$md")" -o "inst/docx/$rel.docx"
echo "готово: inst/docx/$rel.docx"
