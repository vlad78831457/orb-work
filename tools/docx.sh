#!/bin/sh
# Документ → .docx, две версии: короткая и полная, с датой в имени файла.
# Вручную: make docx F=tio.skr-zapusk-triggerov → inst/docx/tio/skr-zapusk-triggerov-2026-10-15.docx
#                                               и inst/docx/tio/skr-zapusk-triggerov-full-2026-10-15.docx
# Pandoc идёт в Docker на одном ядре; шаблон оформления — inst/src/skripty/custom-reference-c.docx.
set -eu
cd "$(dirname "$0")/.."
name=$1
date=${2:-$(date +%F)}
case "$name" in *.*) rel="${name%%.*}/${name#*.}" ;; *) rel="full/$name" ;; esac
ref="inst/src/skripty/custom-reference-c.docx"
[ -f "$ref" ] || { echo "FAIL: нет шаблона оформления $ref"; exit 1; }
mkdir -p "$(dirname "inst/docx/$rel")"
for kind in "" "-full"; do
  md="inst/md-full-out/$rel$kind.md"
  [ -f "$md" ] || { echo "FAIL: нет $md — сначала make full F=$name"; exit 1; }
  docx="inst/docx/$rel$kind-$date.docx"
  docker run --rm --cpus 1 --user "$(id -u):$(id -g)" -v "$PWD":/orb:ro -v "$PWD/inst/docx":/orb/inst/docx -w /orb \
    pandoc/core:3.6 "$md" --from markdown --reference-doc="$ref" --resource-path="$(dirname "$md")" -o "$docx"
  echo "готово: $docx"
done
