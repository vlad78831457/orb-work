# Оплачивающий счета

Оплачивает счета и доплаты и возвращает платёжные поручения.

- **Обязанность:** одна, один ответственный. Ключ: `oplata`
- **Предполагаем, что выполняет:** [Подписант и плательщик (столбец M)](../../reg/rol/podpisant.md), [Казначей](../../reg/rol/kaznachey.md)
- **Контур:** 3
- **Почему выделили:** Регламент: только столбец M; роли.docx: Казначей «оплачивает».
- *Черновик — проверить.*

## Откуда задача и кому результат

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  o_oplata("Оплачивающий счета")
  style o_oplata stroke-width:3px
  o_peredacha_na_oplatu("Передающий счета на оплату")
  o_arhiv_oplat("Раскладывающий оплаченное")
  o_peredacha_na_oplatu -->|ставит| o_oplata
  o_oplata -->|передаёт| o_arhiv_oplat
```

## Шаги

| Процесс | № | Шаг | Здесь |
|---|---|---|---|
| [Процесс. Закупка товара](../../pro/r04-zakupka-tovara/index.md) | 21 | Передача полученных счетов M на оплату | принимает результат |
| [Процесс. Закупка товара](../../pro/r04-zakupka-tovara/index.md) | 22 | Оплата полученных счетов и передача платежных поручений K | делает |
| [Процесс. Поступление: контроль поставки, доплаты, доставка, приёмка](../../pro/r06-postuplenie/index.md) | 14 | Передача полученных счетов M на доплату | принимает результат |
| [Процесс. Поступление: контроль поставки, доплаты, доставка, приёмка](../../pro/r06-postuplenie/index.md) | 15 | Доплата полученных счетов и передача платежных поручений K | делает |

**Получает:** [Проверенные счета на оплату](../../reg/art.md#scheta-na-oplatu)

**Отдаёт:** [Платёжные поручения](../../reg/art.md#platezhki)
