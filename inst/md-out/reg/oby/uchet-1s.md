# Ведущий учёт в 1С

Создаёт заказ покупателя и заказы поставщикам, оприходует товары.

- **Обязанность:** одна, один ответственный. Ключ: `uchet-1s`
- **Предполагаем, что выполняет:** [Хранитель учёта и документов (столбец K)](../../reg/rol/khranitel.md)
- **Контур:** 3
- **Почему выделили:** Все шаги 1С в регламенте — у столбца K.
- *Черновик — проверить.*

## Откуда задача и кому результат

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  o_uchet_1s("Ведущий учёт в 1С")
  style o_uchet_1s stroke-width:3px
  o_postanovka_oplaty("Ставящий задачу на оплату")
  o_peredacha_v_uchet("Передающий договор в учёт")
  o_postanovka_oplaty -->|ставит| o_uchet_1s
  o_peredacha_v_uchet -->|ставит| o_uchet_1s
```

## Шаги

| Процесс | № | Шаг | Здесь |
|---|---|---|---|
| [Процесс. Контрактация](../../pro/r02-kontraktatsiya/index.md) | 18 | Передача в отдел Исполнения заключенного договора для внесения информации в 1с и табличные системы. | принимает результат |
| [Процесс. Закупка товара](../../pro/r04-zakupka-tovara/index.md) | 20 | Создание заказа покупателя и поставщикам в 1с | делает |
| [Процесс. Поступление: контроль поставки, доплаты, доставка, приёмка](../../pro/r06-postuplenie/index.md) | 27 | Оприходование товаров в 1с | делает |

**Получает:** [Приходные документы (сканы)](../../reg/art.md#prihodnye)

**Где работает:** [1С](../../reg/mes.md#1s)
