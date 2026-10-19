# Изготавливающий отгрузочные документы

Изготавливает отгрузочные документы и вносит сведения о них в таблицу оплат.

- **Обязанность:** одна, один ответственный. Ключ: `otgruzochnye-dokumenty`
- **Предполагаем, что выполняет:** [Хранитель учёта и документов (столбец K)](../../reg/rol/khranitel.md)
- **Контур:** 3
- *Черновик — проверить.*

## Откуда задача и кому результат

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  o_otgruzochnye_dokumenty("Изготавливающий<br/>отгрузочные документы")
  style o_otgruzochnye_dokumenty stroke-width:3px
  o_zapros_otgruzochnyh("Запрашивающий отгрузочные<br/>документы")
  o_plan_otgruzok("Планирующий отгрузки")
  o_zapros_otgruzochnyh -->|ставит| o_otgruzochnye_dokumenty
  o_plan_otgruzok -->|ставит| o_otgruzochnye_dokumenty
```

## Шаги

| Процесс | № | Шаг | Здесь |
|---|---|---|---|
| [Процесс. Подготовка к отгрузке](../../pro/r07-podgotovka-k-otgruzke/index.md) | 1.2 | Разработка ведомости отгрузки и постановка задачи на формирования пакета документов для нее. | принимает результат |
| [Процесс. Подготовка к отгрузке](../../pro/r07-podgotovka-k-otgruzke/index.md) | 2 | Передача данных K о необходимости изготовления отгрузочных документов | принимает результат |
| [Процесс. Подготовка к отгрузке](../../pro/r07-podgotovka-k-otgruzke/index.md) | 3 | Изготовление Отгрузочных документов и внесение в таблицу оплат сведений об этих документах | делает |

**Получает:** [Ведомость отгрузки и запрос отгрузочных документов](../../reg/art.md#zapros-otgruzochnyh)

**Отдаёт:** [Отгрузочные документы](../../reg/art.md#otgruzochnye)

**Где работает:** [1С](../../reg/mes.md#1s), [Внешняя таблица оплат](../../reg/mes.md#tablitsa-oplat)
