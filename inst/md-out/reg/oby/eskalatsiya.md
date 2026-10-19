# Эскалирующий задержки поставки

Сообщает менеджеру о затягивании сроков поставки.

- **Обязанность:** одна, один ответственный. Ключ: `eskalatsiya`
- **Предполагаем, что выполняет:** [Закупщик (специалист по закупке)](../../reg/rol/zakupka.md)
- **Контур:** 4
- *Черновик — проверить.*

## Откуда задача и кому результат

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  o_eskalatsiya("Эскалирующий задержки<br/>поставки")
  style o_eskalatsiya stroke-width:3px
  o_reshenie_problem("Решающий по проблемам<br/>поставки")
  o_eskalatsiya -->|передаёт| o_reshenie_problem
```

## Шаги

| Процесс | № | Шаг | Здесь |
|---|---|---|---|
| [Процесс. Поступление: контроль поставки, доплаты, доставка, приёмка](../../pro/r06-postuplenie/index.md) | 7 | Эскалация проблемы в случае затягивания сроков | делает |
| [Процесс. Поступление: контроль поставки, доплаты, доставка, приёмка](../../pro/r06-postuplenie/index.md) | 8 | Принятие решение по эскалированным проблемам | ставит задачу |

**Получает:** [Сведения о просрочке поставки](../../reg/art.md#prosrochka)

**Отдаёт:** [Эскалация задержки](../../reg/art.md#eskalatsiya)
