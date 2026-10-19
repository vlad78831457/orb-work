# Раскладывающий оплаченное

Создаёт «Оплачено» и «Платежные поручения» и перекладывает туда оплаченные счета, договоры и поручения.

- **Обязанность:** одна, один ответственный. Ключ: `arhiv-oplat`
- **Предполагаем, что выполняет:** [Хранитель учёта и документов (столбец K)](../../reg/rol/khranitel.md)
- **Контур:** 3
- **Почему выделили:** Отдельная обязанность — порядок в папке оплат.
- *Черновик — проверить.*

## Откуда задача и кому результат

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  o_arhiv_oplat("Раскладывающий оплаченное")
  style o_arhiv_oplat stroke-width:3px
  o_oplata("Оплачивающий счета")
  o_oplata -->|ставит| o_arhiv_oplat
```

## Шаги

| Процесс | № | Шаг | Здесь |
|---|---|---|---|
| [Процесс. Закупка товара](../../pro/r04-zakupka-tovara/index.md) | 22 | Оплата полученных счетов и передача платежных поручений K | принимает результат |
| [Процесс. Закупка товара](../../pro/r04-zakupka-tovara/index.md) | 23 | Создание в папке ".... В оплату" подпапки "Оплачено" и перемещение в нее всех оплаченных счетов и договоров. Создание папки "Платежные поручения" и перемещение в нее всех Платежных поручений по оплаченным счетам и договорам | делает |

**Получает:** [Платёжные поручения](../../reg/art.md#platezhki)

**Где работает:** [Диск: «Рабочие документы» → «Закупки»](../../reg/mes.md#disk-zakupki)
