#!/bin/sh
# Antigravity CLI (agy) в .tools/agy — как официальный install.sh, но без записи вне ~/pr:
# манифест → загрузка → сверка SHA-512 → распаковка; `agy install` (правка профиля оболочки) не запускается.
set -eu
cd "$(dirname "$0")/.."
BASE=https://antigravity-cli-auto-updater-974169037036.us-central1.run.app
P=linux_amd64; [ "$(uname -m)" = aarch64 ] && P=linux_arm64
ldd /bin/ls 2>&1 | grep -q musl && P=${P}_musl
m=$(curl -fsSL "$BASE/manifests/$P.json")
key() { echo "$m" | sed -n 's/.*"'"$1"'"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p'; }
url=$(key url); sha=$(key sha512); ver=$(key version)
[ -n "$url" ] && [ -n "$sha" ] || { echo "манифест не разобран"; exit 1; }
d=.tools/agy; mkdir -p "$d/dl"; trap 'rm -rf "$d/dl"' EXIT
curl -fsSL -o "$d/dl/agy.tar.gz" "$url"
echo "$sha  $d/dl/agy.tar.gz" | sha512sum -c --quiet
tar -xzf "$d/dl/agy.tar.gz" -C "$d/dl" antigravity && mv "$d/dl/antigravity" "$d/agy" && chmod +x "$d/agy"
echo "agy $ver — $d/agy ($("$d/agy" --version))"
