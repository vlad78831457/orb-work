# Проверяющий ТЗ договора

Сверяет наименования, характеристики и ТЗ договора с нашим ТП; даёт заключение в задаче.

- **Обязанность:** одна, один ответственный. Ключ: `proverka-tz`
- **Предполагаем, что выполняет:** [Технический эксперт (ТС)](../../reg/rol/tekh.md)
- **Контур:** 0
- **Почему выделили:** Техническая проверка — у ТС (Контрактация 12, роли.docx «согласует ТЗ, договор»).
- *Черновик — проверить.*

## Откуда задача и кому результат

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  o_proverka_tz("Проверяющий ТЗ договора")
  style o_proverka_tz stroke-width:3px
  o_dogovor_s_zakazchikom("Ведущий договор с<br/>заказчиком")
  o_dogovor_s_zakazchikom("Ведущий договор с<br/>заказчиком")
  o_dogovor_s_zakazchikom -->|ставит| o_proverka_tz
  o_proverka_tz -->|передаёт| o_dogovor_s_zakazchikom
```

## Шаги

| Процесс | № | Шаг | Здесь |
|---|---|---|---|
| [Процесс. Контрактация](../../pro/r02-kontraktatsiya/index.md) | 11 | Постановка задачи на проверку ТЗ (или заполнение, если к нам вошел договор в редактируемом формате) направленного ТЗ и перечня документов которые нужно включить в счета или договоры (лист 3-3) | принимает результат |
| [Процесс. Контрактация](../../pro/r02-kontraktatsiya/index.md) | 12 | Заполнение/проверка ТЗ | делает |

**Получает:** [Подзадача на проверку ТЗ](../../reg/art.md#podzadacha-tz)

**Отдаёт:** [Заключение по ТЗ](../../reg/art.md#zaklyuchenie-tz)

**Где работает:** [Битрикс24: задачи по шаблонам](../../reg/mes.md#bitriks-zadacha)
