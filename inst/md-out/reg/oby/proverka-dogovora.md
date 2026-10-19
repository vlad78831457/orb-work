# Проверяющий проект договора

Проверяет или заполняет проект договора заказчика по инструкции.

- **Обязанность:** одна, один ответственный. Ключ: `proverka-dogovora`
- **Предполагаем, что выполняет:** [Хранитель учёта и документов (столбец K)](../../reg/rol/khranitel.md)
- **Контур:** 0
- **Почему выделили:** В регламенте исполнитель — столбец K (Контрактация 10).
- *Черновик — проверить.*

## Откуда задача и кому результат

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  o_proverka_dogovora("Проверяющий проект<br/>договора")
  style o_proverka_dogovora stroke-width:3px
  o_dogovor_s_zakazchikom("Ведущий договор с<br/>заказчиком")
  o_dogovor_s_zakazchikom("Ведущий договор с<br/>заказчиком")
  o_dogovor_s_zakazchikom -->|ставит| o_proverka_dogovora
  o_proverka_dogovora -->|передаёт| o_dogovor_s_zakazchikom
```

## Шаги

| Процесс | № | Шаг | Здесь |
|---|---|---|---|
| [Процесс. Контрактация](../../pro/r02-kontraktatsiya/index.md) | 9 | Постановка задачи на проверку (или заполнение, если к нам вошел договор в редактируемом формате) направленного проекта договора. | принимает результат |
| [Процесс. Контрактация](../../pro/r02-kontraktatsiya/index.md) | 10 | Заполнение/проверка проекта договора. | делает |

**Получает:** [Подзадача «Оформить договор»](../../reg/art.md#podzadacha-dogovor), [Проект договора заказчика](../../reg/art.md#proekt-dogovora)

**Отдаёт:** [Заключение по проекту договора](../../reg/art.md#zaklyuchenie-dogovor)
