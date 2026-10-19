# Готовящий ответ на несоответствие

Готовит предложения по ответу, согласует и отправляет ответ.

- **Обязанность:** одна, один ответственный. Ключ: `otvet-nesootvetstvie`
- **Предполагаем, что выполняет:** [Технический эксперт (ТС)](../../reg/rol/tekh.md)
- **Контур:** 4
- **Почему выделили:** Регламент: шаги 26–27 у ТС; «ответ готовит лицо, которому поручили».
- *Черновик — проверить.*

## Откуда задача и кому результат

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  o_otvet_nesootvetstvie("Готовящий ответ на<br/>несоответствие")
  style o_otvet_nesootvetstvie stroke-width:3px
  o_vedenie_nesootvetstviya("Ведущий устранение<br/>несоответствия")
  o_vedenie_nesootvetstviya -->|ставит| o_otvet_nesootvetstvie
```

## Шаги

| Процесс | № | Шаг | Здесь |
|---|---|---|---|
| [Процесс. Устранение несоответствий](../../pro/r10-nesootvetstviya/index.md) | 24 | Выдача поручения по подготовке ответа на документ о несоответствии и организация его выполнения | принимает результат |
| [Процесс. Устранение несоответствий](../../pro/r10-nesootvetstviya/index.md) | 26 | Подготовка предложений по ответу и согласование с заинтересованными сторонами | делает |
| [Процесс. Устранение несоответствий](../../pro/r10-nesootvetstviya/index.md) | 27 | Обеспечение отправки подготовленного ответа | делает |

**Получает:** [Поручение подготовить ответ на несоответствие](../../reg/art.md#poruchenie-otvet)

**Отдаёт:** [Ответ на документ о несоответствии](../../reg/art.md#otvet-nesootv)

**Где работает:** [Почта](../../reg/mes.md#pochta)
