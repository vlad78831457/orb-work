# Ставящий задачи на техническое согласование

Ставит ТС подзадачи: проверить выбранные предложения, согласовать счета и договоры; ведёт цепочку «задача — заключение».

- **Обязанность:** одна, один ответственный. Ключ: `postanovka-teh-soglasovaniya`
- **Предполагаем, что выполняет:** [Закупщик (специалист по закупке)](../../reg/rol/zakupka.md)
- **Контур:** 2
- **Почему выделили:** Регламент: шаги 8 и 14 у закупщика; решение по технике — у другой обязанности.
- *Черновик — проверить.*

## Откуда задача и кому результат

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  o_postanovka_teh_soglasovaniya("Ставящий задачи на<br/>техническое согласование")
  style o_postanovka_teh_soglasovaniya stroke-width:3px
  o_teh_soglasovanie("Согласующий техническую<br/>часть")
  o_teh_soglasovanie("Согласующий техническую<br/>часть")
  o_teh_soglasovanie -->|ставит| o_postanovka_teh_soglasovaniya
  o_postanovka_teh_soglasovaniya -->|передаёт| o_teh_soglasovanie
```

## Шаги

| Процесс | № | Шаг | Здесь |
|---|---|---|---|
| [Процесс. Закупка товара](../../pro/r04-zakupka-tovara/index.md) | 8 | Постановка задачи на проверку выбранных предложений ТС | делает |
| [Процесс. Закупка товара](../../pro/r04-zakupka-tovara/index.md) | 9 | Рассмотрение предложений поставщиков в технической части | ставит задачу |
| [Процесс. Закупка товара](../../pro/r04-zakupka-tovara/index.md) | 9 | Рассмотрение предложений поставщиков в технической части | принимает результат |
| [Процесс. Закупка товара](../../pro/r04-zakupka-tovara/index.md) | 14 | Постановка Задачи на согласование счетов/договоров в технической части | делает |

**Отдаёт:** [Подзадача ТС на проверку предложений](../../reg/art.md#podzadacha-ts)

**Где работает:** [Битрикс24: задачи по шаблонам](../../reg/mes.md#bitriks-zadacha)
