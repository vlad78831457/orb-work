# Проверяющий готовность к отгрузке

Проверяет готовность поставщика к отгрузке и сообщает, что она подтверждена.

- **Обязанность:** одна, один ответственный. Ключ: `gotovnost-otgruzki`
- **Предполагаем, что выполняет:** [Закупщик (специалист по закупке)](../../reg/rol/zakupka.md)
- **Контур:** 4
- **Почему выделили:** Регламент: шаги 10 и 12 у закупщика.
- *Черновик — проверить.*

## Откуда задача и кому результат

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  o_gotovnost_otgruzki("Проверяющий готовность к<br/>отгрузке")
  style o_gotovnost_otgruzki stroke-width:3px
  o_zapros_doplaty("Сообщающий о доплате")
  o_gotovnost_otgruzki -->|передаёт| o_zapros_doplaty
```

## Шаги

| Процесс | № | Шаг | Здесь |
|---|---|---|---|
| [Процесс. Поступление: контроль поставки, доплаты, доставка, приёмка](../../pro/r06-postuplenie/index.md) | 10 | Проверка готовности к отгрузке | делает |
| [Процесс. Поступление: контроль поставки, доплаты, доставка, приёмка](../../pro/r06-postuplenie/index.md) | 12 | Информирование о том, что готовность к отгрузке подтверждена | делает |

**Отдаёт:** [Подтверждённая готовность к отгрузке](../../reg/art.md#gotovnost)
