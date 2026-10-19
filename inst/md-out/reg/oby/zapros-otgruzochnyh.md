# Запрашивающий отгрузочные документы

Передаёт, что нужно изготовить отгрузочные документы.

- **Обязанность:** одна, один ответственный. Ключ: `zapros-otgruzochnyh`
- **Предполагаем, что выполняет:** [Логист](../../reg/rol/logist.md)
- **Контур:** 4
- *Черновик — проверить.*

## Откуда задача и кому результат

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  o_zapros_otgruzochnyh("Запрашивающий отгрузочные<br/>документы")
  style o_zapros_otgruzochnyh stroke-width:3px
  o_otgruzochnye_dokumenty("Изготавливающий<br/>отгрузочные документы")
  o_zapros_otgruzochnyh -->|передаёт| o_otgruzochnye_dokumenty
```

## Шаги

| Процесс | № | Шаг | Здесь |
|---|---|---|---|
| [Процесс. Подготовка к отгрузке](../../pro/r07-podgotovka-k-otgruzke/index.md) | 2 | Передача данных K о необходимости изготовления отгрузочных документов | делает |
| [Процесс. Подготовка к отгрузке](../../pro/r07-podgotovka-k-otgruzke/index.md) | 3 | Изготовление Отгрузочных документов и внесение в таблицу оплат сведений об этих документах | ставит задачу |

**Отдаёт:** [Ведомость отгрузки и запрос отгрузочных документов](../../reg/art.md#zapros-otgruzochnyh)
