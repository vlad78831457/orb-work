# Проверяющий счета перед оплатой

Проверяет готовые к оплате счета и договоры на формальные требования: 5 обязательных пунктов, договор при сумме свыше 100 000.

- **Обязанность:** одна, один ответственный. Ключ: `proverka-schetov`
- **Предполагаем, что выполняет:** [Хранитель учёта и документов (столбец K)](../../reg/rol/khranitel.md), [Казначей](../../reg/rol/kaznachey.md)
- **Контур:** 3
- **Почему выделили:** Регламент: шаг 19 — столбец K; роли.docx: Казначей «проверяет счёт перед оплатой».
- *Черновик — проверить.*

## Откуда задача и кому результат

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  o_proverka_schetov("Проверяющий счета перед<br/>оплатой")
  style o_proverka_schetov stroke-width:3px
  o_postanovka_oplaty("Ставящий задачу на оплату")
  o_postanovka_oplaty -->|ставит| o_proverka_schetov
```

## Шаги

| Процесс | № | Шаг | Здесь |
|---|---|---|---|
| [Процесс. Закупка товара](../../pro/r04-zakupka-tovara/index.md) | 17 | Постановка Задачи K на проверку и оплату счетов и договоров, созданию в 1с Заказа покупателя и заказов поставщикам | принимает результат |
| [Процесс. Закупка товара](../../pro/r04-zakupka-tovara/index.md) | 19 | Проверка готовых к оплате счетов и договоров | делает |

**Получает:** [Задача «Оплатить счета»](../../reg/art.md#zadacha-oplatit), [Счета и договоры «готов к оплате»](../../reg/art.md#scheta-v-oplatu)

**Где работает:** [Диск: «Рабочие документы» → «Закупки»](../../reg/mes.md#disk-zakupki)
