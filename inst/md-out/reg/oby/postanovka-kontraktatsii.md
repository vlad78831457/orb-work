# Ставящий задачу на контрактацию

Ставит по шаблону задачу «Заключить договор»: папка, контакты заказчика, особые указания, чек-лист.

- **Обязанность:** одна, один ответственный. Ключ: `postanovka-kontraktatsii`
- **Предполагаем, что выполняет:** [Менеджер по продажам](../../reg/rol/prodazhi.md)
- **Контур:** 0
- **Почему выделили:** Постановка задачи — отдельная обязанность от её выполнения.
- **Догадка, не подтверждено:** В регламенте шаг у столбца H, но текст «постановка задачи Менеджеру» и «принять задачу у Координатора» — похоже, ставит Координатор.
- *Черновик — проверить.*

## Откуда задача и кому результат

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  o_postanovka_kontraktatsii("Ставящий задачу на<br/>контрактацию")
  style o_postanovka_kontraktatsii stroke-width:3px
  o_dogovor_s_zakazchikom("Ведущий договор с<br/>заказчиком")
  o_postanovka_kontraktatsii -->|передаёт| o_dogovor_s_zakazchikom
```

## Шаги

| Процесс | № | Шаг | Здесь |
|---|---|---|---|
| [Процесс. Передача в контрактацию](../../pro/r01-peredacha-v-kontraktatsiyu/index.md) | 4 | Постановка Задачи на Контрактацию | делает |

**Отдаёт:** [Задача «Заключить договор»](../../reg/art.md#zadacha-kontraktatsiya)

**Где работает:** [Битрикс24: задачи по шаблонам](../../reg/mes.md#bitriks-zadacha)
