# Казначей

Проверяет счёт или договор перед оплатой, делает финальную проверку контрагента, оплачивает.

- **Контур:** 3 — оплаты и договоры
- **Источник:** роли.docx
- **Почему выделили:** Должность из роли.docx.
- **Догадка, не подтверждено:** В регламенте его обязанности делят столбцы K (проверка) и M (оплата); своего столбца нет.

## Обязанности, которые мы ей приписываем

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  r_kaznachey(["Казначей"])
  subgraph k_3["контур 3"]
    o_proverka_schetov("Проверяющий счета перед<br/>оплатой")
    o_oplata("Оплачивающий счета")
  end
  r_kaznachey --> o_proverka_schetov
  r_kaznachey --> o_oplata
```

- [Проверяющий счета перед оплатой](../../reg/oby/proverka-schetov.md) — Проверяет готовые к оплате счета и договоры на формальные требования: 5 обязательных пунктов, договор при сумме свыше 100 000. *(вместе с: [Хранитель учёта и документов (столбец K)](../../reg/rol/khranitel.md))*
- [Оплачивающий счета](../../reg/oby/oplata.md) — Оплачивает счета и доплаты и возвращает платёжные поручения. *(вместе с: [Подписант и плательщик (столбец M)](../../reg/rol/podpisant.md))*

## Шаги процессов

| Процесс | № | Шаг | Обязанность |
|---|---|---|---|
| [Процесс. Закупка товара](../../pro/r04-zakupka-tovara/index.md) | 19 | Проверка готовых к оплате счетов и договоров | [Проверяющий счета перед оплатой](../../reg/oby/proverka-schetov.md) |
| [Процесс. Закупка товара](../../pro/r04-zakupka-tovara/index.md) | 22 | Оплата полученных счетов и передача платежных поручений K | [Оплачивающий счета](../../reg/oby/oplata.md) |
| [Процесс. Поступление: контроль поставки, доплаты, доставка, приёмка](../../pro/r06-postuplenie/index.md) | 15 | Доплата полученных счетов и передача платежных поручений K | [Оплачивающий счета](../../reg/oby/oplata.md) |

