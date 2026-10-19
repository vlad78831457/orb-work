# Назначающий ответственных

Назначает ответственного за оформление экспорта и за судебно-исковую работу, решает, как вести суд.

- **Обязанность:** одна, один ответственный. Ключ: `naznachenie-otvetstvennyh`
- **Предполагаем, что выполняет:** [Владелец процесса (руководитель исполнителя)](../../reg/rol/vladelets.md)
- **Контур:** 0
- **Почему выделили:** Регламент: столбец N.
- *Черновик — проверить.*

## Откуда задача и кому результат

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  o_naznachenie_otvetstvennyh("Назначающий ответственных")
  style o_naznachenie_otvetstvennyh stroke-width:3px
  o_isk("Инициирующий судебный иск")
  o_eksport("Оформляющий экспорт")
  o_sud("Ведущий судебно-исковую<br/>работу")
  o_isk -->|ставит| o_naznachenie_otvetstvennyh
  o_naznachenie_otvetstvennyh -->|передаёт| o_eksport
  o_naznachenie_otvetstvennyh -->|передаёт| o_sud
```

## Шаги

| Процесс | № | Шаг | Здесь |
|---|---|---|---|
| [Процесс. Оформление экспорта](../../pro/r09-oformlenie-eksporta/index.md) | 15 | Назначение ответственного за оформление Экспорта | делает |
| [Процесс. Оформление экспорта](../../pro/r09-oformlenie-eksporta/index.md) | — | Оформление экспорта | ставит задачу |
| [Процесс. Контроль исполнения заказчиком](../../pro/r11-kontrol-zakazchika/index.md) | 37 | Инициирование Судебного Иска | принимает результат |
| [Процесс. Контроль исполнения заказчиком](../../pro/r11-kontrol-zakazchika/index.md) | 38 | Планирование судебно исковой работы. | делает |
| [Процесс. Контроль исполнения заказчиком](../../pro/r11-kontrol-zakazchika/index.md) | 39 | Судебно-исковая работа | ставит задачу |

**Получает:** [Решение инициировать иск](../../reg/art.md#isk)

**Отдаёт:** [Назначение ответственного](../../reg/art.md#naznachenie)
