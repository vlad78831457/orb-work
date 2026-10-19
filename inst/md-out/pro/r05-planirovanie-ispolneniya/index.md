> Черновик: текст не проверен.

# Планирование и контроль исполнения

Процесс регламента «Распределение задач» (лист «10.10.2026 Версия К»), в регламенте — «ПЛАНИРОВАНИЕ И КОНТРОЛЬ ИСПОЛНЕНИЯ». Контур 4.
Как читать схемы и что значат обязанности — [обзор процессов](../../pro/obzor/index.md).

Шаги «как записано» — `reglament.yaml` (собран скриптом из регламента), наше толкование — `protsess.yaml`. Ниже всё собрано из них.

## Дорожки по должностям

Вертикальная дорожка — должность, которую мы предполагаем; заметка — шаг в её дорожке; стрелка — работа переходит к другой должности (ставит задачу или делает следующий шаг).

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
sequenceDiagram
  participant r_proekt as Менеджер проекта
  participant r_none as не знаем кто
  rect rgb(255, 255, 255)
  Note over r_proekt: 0. Разработка Плана исполнения и<br/>Рекомендаций, Контрольных точек,<br/>Инструктаж по исполнению
  Note over r_proekt: 0. Управление изменениями выявлено<br/>несоответствие между договором и<br/>реальностью
  r_proekt->>r_none: План исполнения и контрольные<br/>точки
  Note over r_none: Отчетность
  end
```

## Как в регламенте

Дорожки — столбцы регламента с основным исполнителем; шаги — по порядку. Пунктир — шаг без исполнителя.

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart TB
  subgraph c_H["H Менеджер"]
    s_pl_0["0. Разработка Плана<br/>исполнения и Рекомендаций,<br/>Контрольных точек, Инс…"]
    s_pl_0b["0. Управление изменениями<br/>выявлено несоответствие<br/>между договором и р…"]
  end
  subgraph c_none["нет исполнителя"]
    s_pl_x1["Отчетность"]
  end
  s_pl_0 --> s_pl_0b
  s_pl_0b --> s_pl_x1
  classDef none stroke-dasharray: 5 5
  class s_pl_x1 none
```

| № | Шаг | H Менеджер | I ТС (эксперт) | J Закупщик | столбец K | L АС | столбец M | N Владелец процесса |
|---|---|---|---|---|---|---|---|---|
| 0 | Разработка Плана исполнения и Рекомендаций, Контрольных точек, Инструктаж по исполнению | И | У | У | У | У | У | У |
| 0 | Управление изменениями выявлено несоответствие между договором и реальностью | И | У | У | У | У | У | У |
| — | Отчетность |  |  |  |  |  |  |  |

И — исполнитель, С — соисполнитель, Сг — согласование, У — информируемый, В — владелец процесса.

## По обязанностям

Дорожки — должности, которые мы предполагаем; узлы — обязанности. Сплошная стрелка — ставит задачу или передаёт результат, пунктир — следит или согласует; стрелка без подписи — дальше по порядку.

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart TB
  subgraph r_proekt["Менеджер проекта"]
    o_plan_ispolneniya("Составляющий план<br/>исполнения")
    o_upravlenie_izmeneniyami("Управляющий изменениями")
  end
  subgraph r_none["не знаем кто"]
    o_otchetnost("Проводящий отчётность")
  end
  o_plan_ispolneniya --> o_upravlenie_izmeneniyami
  o_upravlenie_izmeneniyami --> o_otchetnost
```

## Шаги и обязанности

| № | Шаг | Делает | Ставит → принимает | Передаёт | Согласуют, помогают, узнают | Где |
|---|---|---|---|---|---|---|
| 0 | Разработка Плана исполнения и Рекомендаций, Контрольных точек, Инструктаж по исполнению | [Составляющий план исполнения](../../reg/oby/plan-ispolneniya.md) | — → — | [План исполнения и контрольные точки](../../reg/art.md#plan-ispolneniya) | узнают о результате: [Технический эксперт (ТС)](../../reg/rol/tekh.md), [Закупщик (специалист по закупке)](../../reg/rol/zakupka.md), [Хранитель учёта и документов (столбец K)](../../reg/rol/khranitel.md), [Логист](../../reg/rol/logist.md), [Подписант и плательщик (столбец M)](../../reg/rol/podpisant.md), [Владелец процесса (руководитель исполнителя)](../../reg/rol/vladelets.md) |  |
| 0 | Управление изменениями выявлено несоответствие между договором и реальностью | [Управляющий изменениями](../../reg/oby/upravlenie-izmeneniyami.md) | — → — |  | узнают о результате: [Технический эксперт (ТС)](../../reg/rol/tekh.md), [Закупщик (специалист по закупке)](../../reg/rol/zakupka.md), [Хранитель учёта и документов (столбец K)](../../reg/rol/khranitel.md), [Логист](../../reg/rol/logist.md), [Подписант и плательщик (столбец M)](../../reg/rol/podpisant.md), [Владелец процесса (руководитель исполнителя)](../../reg/rol/vladelets.md) |  |
| — | Отчетность | [Проводящий отчётность](../../reg/oby/otchetnost.md) | — → — |  |  |  |

Дальше: [Процесс. Поступление: контроль поставки, доплаты, доставка, приёмка](../r06-postuplenie/index.md).
