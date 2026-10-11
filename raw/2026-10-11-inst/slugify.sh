#!/bin/bash

# Если не передано вообще ничего, выходим
if [ -z "$*" ]; then
    echo "Использование: $0 Строка для очистки"
    exit 1
fi

# $* собирает абсолютно все аргументы в одну строку, разделяя их пробелом
text="${*,,}"

# Транслитерация
text=$(echo "$text" | sed '
    s/щ/shch/g; s/ш/sh/g; s/ч/ch/g; s/ж/zh/g;
    s/х/kh/g;   s/ц/ts/g; s/э/e/g;  s/ю/yu/g;
    s/я/ya/g;   s/ё/e/g;  s/а/a/g;  s/б/b/g;
    s/в/v/g;    s/г/g/g;  s/д/d/g;  s/е/e/g;
    s/з/z/g;    s/и/i/g;  s/й/y/g;  s/к/k/g;
    s/л/l/g;    s/м/m/g;  s/н/n/g;  s/о/o/g;
    s/п/p/g;    s/р/r/g;  s/с/s/g;  s/т/t/g;
    s/у/u/g;    s/ф/f/g;  s/ы/y/g;  s/ь//g;  s/ъ//g;
    s/ /-/g;    s/\//-/g; s/_/-/g;
')

# Финальная очистка
text=$(echo "$text" | sed '
    s/[^a-z0-9-]//g;
    s/-\+/-/g;
    s/^-//; s/-$//
')

echo "$text"
