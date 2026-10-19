# Инициирующий судебный иск

Инициирует судебный иск к заказчику.

- **Обязанность:** одна, один ответственный. Ключ: `isk`
- **Предполагаем, что выполняет:** [Менеджер проекта](../../reg/rol/proekt.md)
- **Контур:** 3
- *Черновик — проверить.*

## Откуда задача и кому результат

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  o_isk("Инициирующий судебный иск")
  style o_isk stroke-width:3px
  o_naznachenie_otvetstvennyh("Назначающий ответственных")
  o_isk -->|передаёт| o_naznachenie_otvetstvennyh
```

## Шаги

| Процесс | № | Шаг | Здесь |
|---|---|---|---|
| [Процесс. Контроль исполнения заказчиком](../../pro/r11-kontrol-zakazchika/index.md) | 37 | Инициирование Судебного Иска | делает |

**Отдаёт:** [Решение инициировать иск](../../reg/art.md#isk)
