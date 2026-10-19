# Оформляющий экспорт

Оформляет экспорт, если он нужен.

- **Обязанность:** одна, один ответственный. Ключ: `eksport`
- **Предполагаем, что выполняет:** *не знаем*
- **Контур:** 4
- **Почему выделили:** Шаг без исполнителя: «выполняет назначенное ответственное лицо».
- *Черновик — проверить.*

## Откуда задача и кому результат

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  o_eksport("Оформляющий экспорт")
  style o_eksport stroke-width:3px
  o_naznachenie_otvetstvennyh("Назначающий ответственных")
  o_naznachenie_otvetstvennyh -->|ставит| o_eksport
```

## Шаги

| Процесс | № | Шаг | Здесь |
|---|---|---|---|
| [Процесс. Оформление экспорта](../../pro/r09-oformlenie-eksporta/index.md) | 15 | Назначение ответственного за оформление Экспорта | принимает результат |
| [Процесс. Оформление экспорта](../../pro/r09-oformlenie-eksporta/index.md) | — | Оформление экспорта | делает |

**Получает:** [Назначение ответственного](../../reg/art.md#naznachenie)
