# Ведущий таблицу оплат

Вносит в таблицу оплат оплаты, доплаты и сведения об отгрузочных документах.

- **Обязанность:** одна, один ответственный. Ключ: `tablitsa-oplat`
- **Предполагаем, что выполняет:** [Хранитель учёта и документов (столбец K)](../../reg/rol/khranitel.md)
- **Контур:** 3
- **Почему выделили:** Регламент: шаги 24 (закупка) и 16 (доплаты) — столбец K.
- *Черновик — проверить.*

## Откуда задача и кому результат

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  o_tablitsa_oplat("Ведущий таблицу оплат")
  style o_tablitsa_oplat stroke-width:3px
  o_zakrytie_zakupki("Закрывающий закупку")
  o_tablitsa_oplat -->|передаёт| o_zakrytie_zakupki
```

## Шаги

| Процесс | № | Шаг | Здесь |
|---|---|---|---|
| [Процесс. Закупка товара](../../pro/r04-zakupka-tovara/index.md) | 24 | Внесение в Таблицу Оплат сведений о произведенных оплатах по проекту | делает |
| [Процесс. Поступление: контроль поставки, доплаты, доставка, приёмка](../../pro/r06-postuplenie/index.md) | 16 | Внесение в таблицу оплат сведений о произведенных доплатах по проекту. Перемещение в папку "Платежные поручения" всех Платежных поручений по оплаченным счетам и договорам | делает |

**Получает:** [Платёжные поручения](../../reg/art.md#platezhki)

**Отдаёт:** [Сведения об оплатах (таблица оплат)](../../reg/art.md#oplaty-v-tablitse)

**Где работает:** [Внешняя таблица оплат](../../reg/mes.md#tablitsa-oplat), [Лист «6 Оплаты»](../../reg/mes.md#lis-6-oplaty), [Диск: «Рабочие документы» → «Закупки»](../../reg/mes.md#disk-zakupki)
