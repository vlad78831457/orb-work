#!/bin/bash
cd "$(dirname "$0")"

TEMPLATE="templates/ref.docx"

# Проверка наличия Pandoc
if ! command -v pandoc &> /dev/null; then
    echo "❌ Ошибка: Pandoc не установлен. Пожалуйста, установите его."
    exit 1
fi

compile_doc() {
    local out_name=$1
    local res_paths=$2
    shift 2
    local md_files=("$@")

    echo "📦 Сборка документа: $out_name..."
    pandoc "${md_files[@]}" \
        --reference-doc="$TEMPLATE" \
        --resource-path="$res_paths" \
        -o "dist/$out_name"
    
    if [ $? -eq 0 ]; then
        echo "✨ Успешно создано: dist/$out_name"
    else
        echo "❌ Ошибка при сборке $out_name"
    fi
    echo "-----------------------------------"
}

show_help() {
    echo "Использование: ./build.sh [имя_документа]"
    echo "Доступные команды:"
    echo "  calc  - Собрать регламент по Расчету"
    echo "  sales - Собрать регламент по Продажам"
    echo "  all   - Собрать ВСЕ документы сразу"
}

if [ -z "$1" ]; then
    show_help
    exit 1
fi

mkdir -p dist

case "$1" in
    "calc")
        compile_doc "Регламент_Расчет.docx" "src/_shared:src/process_calc" \
            "src/_shared/00_intro.md" \
            "src/process_calc/calc_steps.md"
        ;;
    "sales")
        compile_doc "Регламент_Продаж.docx" "src/_shared:src/process_sales" \
            "src/_shared/00_intro.md" \
            "src/process_sales/sales_steps.md"
        ;;
    "all")
        echo "🚀 Запуск полной сборки всей базы знаний..."
        $0 calc
        $0 sales
        ;;
    *)
        echo "❌ Неизвестная команда: $1"
        show_help
        exit 1
        ;;
esac
