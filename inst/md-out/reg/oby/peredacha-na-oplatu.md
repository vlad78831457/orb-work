# Передающий счета на оплату

Передаёт проверенные счета на оплату и доплату тому, кто платит.

- **Обязанность:** одна, один ответственный. Ключ: `peredacha-na-oplatu`
- **Предполагаем, что выполняет:** [Хранитель учёта и документов (столбец K)](../../reg/rol/khranitel.md)
- **Контур:** 3
- **Почему выделили:** Регламент: шаги «Передача счетов M на оплату / доплату» — столбец K.
- *Черновик — проверить.*

## Откуда задача и кому результат

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  o_peredacha_na_oplatu("Передающий счета на оплату")
  style o_peredacha_na_oplatu stroke-width:3px
  o_zapros_doplaty("Сообщающий о доплате")
  o_oplata("Оплачивающий счета")
  o_zapros_doplaty -->|ставит| o_peredacha_na_oplatu
  o_peredacha_na_oplatu -->|передаёт| o_oplata
```

## Шаги

| Процесс | № | Шаг | Здесь |
|---|---|---|---|
| [Процесс. Закупка товара](../../pro/r04-zakupka-tovara/index.md) | 21 | Передача полученных счетов M на оплату | делает |
| [Процесс. Закупка товара](../../pro/r04-zakupka-tovara/index.md) | 22 | Оплата полученных счетов и передача платежных поручений K | ставит задачу |
| [Процесс. Поступление: контроль поставки, доплаты, доставка, приёмка](../../pro/r06-postuplenie/index.md) | 13 | Передача данных K о необходимости доплаты при наличии готовности к отгрузке | принимает результат |
| [Процесс. Поступление: контроль поставки, доплаты, доставка, приёмка](../../pro/r06-postuplenie/index.md) | 14 | Передача полученных счетов M на доплату | делает |
| [Процесс. Поступление: контроль поставки, доплаты, доставка, приёмка](../../pro/r06-postuplenie/index.md) | 15 | Доплата полученных счетов и передача платежных поручений K | ставит задачу |

**Получает:** [Сведения о необходимости доплаты](../../reg/art.md#zapros-doplaty)

**Отдаёт:** [Проверенные счета на оплату](../../reg/art.md#scheta-na-oplatu)
