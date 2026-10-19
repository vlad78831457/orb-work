# Передающий договор в учёт

Ставит подзадачу внести номер и дату договора в 1С и таблицы и проверяет, что договор внесён.

- **Обязанность:** одна, один ответственный. Ключ: `peredacha-v-uchet`
- **Предполагаем, что выполняет:** [Менеджер по продажам](../../reg/rol/prodazhi.md)
- **Контур:** 0
- **Почему выделили:** Передача между контурами — отдельная ответственность (Контрактация 18).
- *Черновик — проверить.*

## Откуда задача и кому результат

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  o_peredacha_v_uchet("Передающий договор в учёт")
  style o_peredacha_v_uchet stroke-width:3px
  o_uchet_1s("Ведущий учёт в 1С")
  o_peredacha_v_uchet -->|передаёт| o_uchet_1s
```

## Шаги

| Процесс | № | Шаг | Здесь |
|---|---|---|---|
| [Процесс. Контрактация](../../pro/r02-kontraktatsiya/index.md) | 18 | Передача в отдел Исполнения заключенного договора для внесения информации в 1с и табличные системы. | делает |

**Отдаёт:** [Подзадача «внести договор в 1С и таблицы»](../../reg/art.md#podzadacha-uchet)

**Где работает:** [Битрикс24: задачи по шаблонам](../../reg/mes.md#bitriks-zadacha)
