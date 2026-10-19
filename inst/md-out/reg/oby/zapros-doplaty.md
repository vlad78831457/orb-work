# Сообщающий о доплате

Когда поставщик готов к отгрузке — передаёт, что нужна доплата.

- **Обязанность:** одна, один ответственный. Ключ: `zapros-doplaty`
- **Предполагаем, что выполняет:** [Логист](../../reg/rol/logist.md)
- **Контур:** 4
- **Почему выделили:** Регламент: «Доплаты» и шаг 13 — у АС (логист).
- *Черновик — проверить.*

## Откуда задача и кому результат

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  o_zapros_doplaty("Сообщающий о доплате")
  style o_zapros_doplaty stroke-width:3px
  o_gotovnost_otgruzki("Проверяющий готовность к<br/>отгрузке")
  o_peredacha_na_oplatu("Передающий счета на оплату")
  o_gotovnost_otgruzki -->|ставит| o_zapros_doplaty
  o_zapros_doplaty -->|передаёт| o_peredacha_na_oplatu
```

## Шаги

| Процесс | № | Шаг | Здесь |
|---|---|---|---|
| [Процесс. Поступление: контроль поставки, доплаты, доставка, приёмка](../../pro/r06-postuplenie/index.md) | 12 | Информирование о том, что готовность к отгрузке подтверждена | принимает результат |
| [Процесс. Поступление: контроль поставки, доплаты, доставка, приёмка](../../pro/r06-postuplenie/index.md) | — | Доплаты | делает |
| [Процесс. Поступление: контроль поставки, доплаты, доставка, приёмка](../../pro/r06-postuplenie/index.md) | 13 | Передача данных K о необходимости доплаты при наличии готовности к отгрузке | делает |

**Получает:** [Подтверждённая готовность к отгрузке](../../reg/art.md#gotovnost)

**Отдаёт:** [Сведения о необходимости доплаты](../../reg/art.md#zapros-doplaty)
