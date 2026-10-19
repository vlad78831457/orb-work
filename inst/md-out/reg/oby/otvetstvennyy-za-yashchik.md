# Ответственный за почтовый ящик

Получив документ о несоответствии на свой ящик, передаёт его на регистрацию.

- **Обязанность:** одна, один ответственный. Ключ: `otvetstvennyy-za-yashchik`
- **Предполагаем, что выполняет:** [Менеджер проекта](../../reg/rol/proekt.md), [Технический эксперт (ТС)](../../reg/rol/tekh.md), [Логист](../../reg/rol/logist.md), [Подписант и плательщик (столбец M)](../../reg/rol/podpisant.md)
- **Контур:** 4
- **Почему выделили:** Регламент: «за передачу отвечает ответственный за почтовый ящик, на который поступил документ» — у шага четыре исполнителя.
- *Черновик — проверить.*

## Откуда задача и кому результат

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  o_otvetstvennyy_za_yashchik("Ответственный за почтовый<br/>ящик")
  style o_otvetstvennyy_za_yashchik stroke-width:3px
  o_registratsiya_vhodyashchih("Регистрирующий входящие")
  o_otvetstvennyy_za_yashchik -->|передаёт| o_registratsiya_vhodyashchih
```

## Шаги

| Процесс | № | Шаг | Здесь |
|---|---|---|---|
| [Процесс. Устранение несоответствий](../../pro/r10-nesootvetstviya/index.md) | 16 | Вход в процесс: поступление документов о несоответствии продукции требованиям договора | делает |
| [Процесс. Устранение несоответствий](../../pro/r10-nesootvetstviya/index.md) | 17 | Передача документа о несоответствии на регистрацию Координатору | делает |

**Отдаёт:** [Документ о несоответствии](../../reg/art.md#dokument-nesootv)

**Где работает:** [Почта](../../reg/mes.md#pochta)
