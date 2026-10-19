# Принимающий задачу на закупку

Знакомится с задачей на закупку, проверяет достаточность сведений, решает вопросы и принимает в работу.

- **Обязанность:** одна, один ответственный. Ключ: `prinyatie-zakupki`
- **Предполагаем, что выполняет:** [Закупщик (специалист по закупке)](../../reg/rol/zakupka.md)
- **Контур:** 2
- **Почему выделили:** По смыслу задачу принимает тот, кто будет закупать (Закупка 0 — у закупщика).
- **Догадка, не подтверждено:** В регламенте шаг «Принять задачу на закупку» (Передача в закупки 6) стоит у столбца H.
- *Черновик — проверить.*

## Откуда задача и кому результат

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  o_prinyatie_zakupki("Принимающий задачу на<br/>закупку")
  style o_prinyatie_zakupki stroke-width:3px
  o_postanovka_zakupki("Ставящий задачу на закупку")
  o_postanovka_zakupki -->|ставит| o_prinyatie_zakupki
```

## Шаги

| Процесс | № | Шаг | Здесь |
|---|---|---|---|
| [Процесс. Передача в закупки](../../pro/r03-peredacha-v-zakupki/index.md) | 5 | Выполнить подзадачу "Поставить задачу на закупку" | принимает результат |
| [Процесс. Передача в закупки](../../pro/r03-peredacha-v-zakupki/index.md) | 6 | Выполнить подзадачу "Принять задачу на закупку" | делает |
| [Процесс. Передача в закупки](../../pro/r03-peredacha-v-zakupki/index.md) | 7 | Возобновление Закупок по проекту (в случае невыполнения поставок контрагентами, необходимости дозакупить что-либо и т.д.) | принимает результат |
| [Процесс. Закупка товара](../../pro/r04-zakupka-tovara/index.md) | 0 | Вход в процесс- Поставлена задача на закупку по проекту. №Проекта -Закзачик-предмет: Закупить товары" (или принятие этой задачи?!) | делает |

**Получает:** [Задача «Закупка»](../../reg/art.md#zadacha-zakupka)

**Где работает:** [Битрикс24: задачи по шаблонам](../../reg/mes.md#bitriks-zadacha)
