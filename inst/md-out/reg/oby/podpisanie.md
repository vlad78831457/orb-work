# Подписывающий договор

Подписывает договор с заказчиком через ЭДО.

- **Обязанность:** одна, один ответственный. Ключ: `podpisanie`
- **Предполагаем, что выполняет:** [Подписант и плательщик (столбец M)](../../reg/rol/podpisant.md)
- **Контур:** 0
- **Почему выделили:** Право подписи — отдельная ответственность (Контрактация 15, столбец M).
- *Черновик — проверить.*

## Откуда задача и кому результат

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  o_podpisanie("Подписывающий договор")
  style o_podpisanie stroke-width:3px
  o_dogovor_s_zakazchikom("Ведущий договор с<br/>заказчиком")
  o_dogovor_s_zakazchikom -->|ставит| o_podpisanie
```

## Шаги

| Процесс | № | Шаг | Здесь |
|---|---|---|---|
| [Процесс. Контрактация](../../pro/r02-kontraktatsiya/index.md) | 14 | Информирование M, о том, что надо подписать договор через ЭДО | принимает результат |
| [Процесс. Контрактация](../../pro/r02-kontraktatsiya/index.md) | 15 | Подписание договора через ЭДО | делает |

**Получает:** [Просьба подписать договор через ЭДО](../../reg/art.md#poruchenie-podpisat)

**Отдаёт:** [Подписанный договор с заказчиком](../../reg/art.md#dogovor-podpisannyy)

**Где работает:** [ЭДО](../../reg/mes.md#edo)
