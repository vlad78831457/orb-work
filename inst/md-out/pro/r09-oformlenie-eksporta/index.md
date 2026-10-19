> Черновик: текст не проверен.

# Оформление экспорта

Процесс регламента «Распределение задач» (лист «10.10.2026 Версия К»), в регламенте — «ОФОРМЛЕНИЕ ЭКСПОРТА (если применимо)». Контур 4.
Как читать схемы и что значат обязанности — [обзор процессов](../../pro/obzor/index.md).

Шаги «как записано» — `reglament.yaml` (собран скриптом из регламента), наше толкование — `protsess.yaml`. Ниже всё собрано из них.

## Дорожки по должностям

Вертикальная дорожка — должность, которую мы предполагаем; заметка — шаг в её дорожке; стрелка — работа переходит к другой должности (ставит задачу или делает следующий шаг).

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
sequenceDiagram
  participant r_vladelets as Владелец процесса
  participant r_none as не знаем кто
  rect rgb(255, 255, 255)
  Note over r_vladelets: 15. Назначение ответственного за<br/>оформление Экспорта
  r_vladelets->>r_none: Назначение ответственного
  Note over r_none: Оформление экспорта
  end
```

## Как в регламенте

Дорожки — столбцы регламента с основным исполнителем; шаги — по порядку. Пунктир — шаг без исполнителя.

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart TB
  subgraph c_N["N Владелец процесса"]
    s_ek_15["15. Назначение<br/>ответственного за<br/>оформление Экспорта"]
  end
  subgraph c_none["нет исполнителя"]
    s_ek_x1["Оформление экспорта"]
  end
  s_ek_15 --> s_ek_x1
  classDef none stroke-dasharray: 5 5
  class s_ek_x1 none
```

| № | Шаг | N Владелец процесса |
|---|---|---|
| 15 | Назначение ответственного за оформление Экспорта | И |
| — | Оформление экспорта |  |

И — исполнитель, С — соисполнитель, Сг — согласование, У — информируемый, В — владелец процесса.

## По обязанностям

Дорожки — должности, которые мы предполагаем; узлы — обязанности. Сплошная стрелка — ставит задачу или передаёт результат, пунктир — следит или согласует; стрелка без подписи — дальше по порядку.

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart TB
  subgraph r_vladelets["Владелец процесса"]
    o_naznachenie_otvetstvennyh("Назначающий ответственных")
  end
  subgraph r_none["не знаем кто"]
    o_eksport("Оформляющий экспорт")
  end
  o_naznachenie_otvetstvennyh -->|"ставит"| o_eksport
```

## Шаги и обязанности

| № | Шаг | Делает | Ставит → принимает | Передаёт | Согласуют, помогают, узнают | Где |
|---|---|---|---|---|---|---|
| 15 | Назначение ответственного за оформление Экспорта | [Назначающий ответственных](../../reg/oby/naznachenie-otvetstvennyh.md) | — → [Оформляющий экспорт](../../reg/oby/eksport.md) | [Назначение ответственного](../../reg/art.md#naznachenie) |  |  |
| — | Оформление экспорта | [Оформляющий экспорт](../../reg/oby/eksport.md) | [Назначающий ответственных](../../reg/oby/naznachenie-otvetstvennyh.md) → — |  |  |  |
