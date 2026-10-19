# Закрывающий контрактацию

Ставит статус «Договор заключен», завершает задачу и сдаёт её Координатору.

- **Обязанность:** одна, один ответственный. Ключ: `zakrytie-kontraktatsii`
- **Предполагаем, что выполняет:** [Менеджер по продажам](../../reg/rol/prodazhi.md)
- **Контур:** 0
- **Почему выделили:** Выход из процесса (Контрактация 19, 20).
- *Черновик — проверить.*

## Откуда задача и кому результат

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  o_zakrytie_kontraktatsii("Закрывающий контрактацию")
  style o_zakrytie_kontraktatsii stroke-width:3px
  o_priemka_etapov("Принимающий этапы")
  o_zakrytie_kontraktatsii -->|передаёт| o_priemka_etapov
```

## Шаги

| Процесс | № | Шаг | Здесь |
|---|---|---|---|
| [Процесс. Контрактация](../../pro/r02-kontraktatsiya/index.md) | 19 | Закрытие этапа Контрактация | делает |
| [Процесс. Контрактация](../../pro/r02-kontraktatsiya/index.md) | 20 | Приемка этапа Контрактации | делает |

**Где работает:** [Битрикс24: статус проекта](../../reg/mes.md#bitriks-status-proekta), [Битрикс24: задачи по шаблонам](../../reg/mes.md#bitriks-zadacha)
