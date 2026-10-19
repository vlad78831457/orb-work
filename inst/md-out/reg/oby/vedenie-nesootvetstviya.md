# Ведущий устранение несоответствия

Решает, как устранять, выдаёт поручения на устранение и на ответ, организует устранение, собирает объяснения, закрывает процесс.

- **Обязанность:** одна, один ответственный. Ключ: `vedenie-nesootvetstviya`
- **Предполагаем, что выполняет:** [Менеджер проекта](../../reg/rol/proekt.md)
- **Контур:** 4
- *Черновик — проверить.*

## Откуда задача и кому результат

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  o_vedenie_nesootvetstviya("Ведущий устранение<br/>несоответствия")
  style o_vedenie_nesootvetstviya stroke-width:3px
  o_registratsiya_vhodyashchih("Регистрирующий входящие")
  o_otvet_nesootvetstvie("Готовящий ответ на<br/>несоответствие")
  o_registratsiya_vhodyashchih -->|ставит| o_vedenie_nesootvetstviya
  o_vedenie_nesootvetstviya -->|передаёт| o_otvet_nesootvetstvie
```

## Шаги

| Процесс | № | Шаг | Здесь |
|---|---|---|---|
| [Процесс. Устранение несоответствий](../../pro/r10-nesootvetstviya/index.md) | 20 | Передача документа о несоответствии менеджеру проекта с постановкой задачи | принимает результат |
| [Процесс. Устранение несоответствий](../../pro/r10-nesootvetstviya/index.md) | 21 | Принятие решения по устранению несоответствий | делает |
| [Процесс. Устранение несоответствий](../../pro/r10-nesootvetstviya/index.md) | 23 | Выдача поручения по устранению несоответствий и организация его выполнения | делает |
| [Процесс. Устранение несоответствий](../../pro/r10-nesootvetstviya/index.md) | 24 | Выдача поручения по подготовке ответа на документ о несоответствии и организация его выполнения | делает |
| [Процесс. Устранение несоответствий](../../pro/r10-nesootvetstviya/index.md) | 25 | Устранение несоответствий | делает |
| [Процесс. Устранение несоответствий](../../pro/r10-nesootvetstviya/index.md) | 26 | Подготовка предложений по ответу и согласование с заинтересованными сторонами | ставит задачу |
| [Процесс. Устранение несоответствий](../../pro/r10-nesootvetstviya/index.md) | 26 | Подготовка предложений по ответу и согласование с заинтересованными сторонами | согласуют |
| [Процесс. Устранение несоответствий](../../pro/r10-nesootvetstviya/index.md) | 28 | Сбор объяснений по возникновению несоответствий и сбор предложений по предотвращению/снижению рисков возникновения подобных несоответствий | делает |
| [Процесс. Устранение несоответствий](../../pro/r10-nesootvetstviya/index.md) | 29 | Закрытие процесса Устранение несоответствий | делает |

**Получает:** [Задача «Принятие решения по устранению несоответствий»](../../reg/art.md#zadacha-nesootv), [Документ о несоответствии](../../reg/art.md#dokument-nesootv), [Ответ на документ о несоответствии](../../reg/art.md#otvet-nesootv)

**Отдаёт:** [Решение по устранению несоответствия](../../reg/art.md#reshenie-nesootv), [Поручение подготовить ответ на несоответствие](../../reg/art.md#poruchenie-otvet), [Объяснения и предложения по предотвращению](../../reg/art.md#obyasneniya)

**Где работает:** [Битрикс24: задачи по шаблонам](../../reg/mes.md#bitriks-zadacha)
