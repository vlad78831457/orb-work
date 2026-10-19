> Черновик: текст не проверен.

# Передача в контрактацию

Процесс регламента «Распределение задач» (лист «10.10.2026 Версия К»), в регламенте — «Передача в контрактацию». Контур 0.
Как читать схемы и что значат обязанности — [обзор процессов](../../pro/obzor/index.md).

Шаги «как записано» — `reglament.yaml` (собран скриптом из регламента), наше толкование — `protsess.yaml`. Ниже всё собрано из них.

## Дорожки по должностям

Вертикальная дорожка — должность, которую мы предполагаем; заметка — шаг в её дорожке; стрелка — работа переходит к другой должности (ставит задачу или делает следующий шаг).

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
sequenceDiagram
  participant r_prodazhi as Менеджер по продажам
  rect rgb(255, 255, 255)
  Note over r_prodazhi: 0. Вход в процесс #quot;Передача в<br/>Контрактацию#quot;
  Note over r_prodazhi: 1. Создание в папке Проекта<br/>подпапки #quot;...Рабочие документы#quot; и<br/>создание в ней папки #quot;КОНТР…
  Note over r_prodazhi: 2. Открытие доступа к папке<br/>#quot;...рабочие Документы#quot; отделению<br/>Исполнения
  Note over r_prodazhi: 3. Размещение в папке<br/>#quot;КОНТРАКТАЦИЯ#quot; документов:
  Note over r_prodazhi: 4. Постановка Задачи на<br/>Контрактацию
  end
```

## Как в регламенте

Дорожки — столбцы регламента с основным исполнителем; шаги — по порядку. Пунктир — шаг без исполнителя.

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart TB
  subgraph c_H["H Менеджер"]
    s_pk_0["0. Вход в процесс<br/>#quot;Передача в Контрактацию#quot;"]
    s_pk_1["1. Создание в папке<br/>Проекта подпапки<br/>#quot;...Рабочие документы#quot; и<br/>создани…"]
    s_pk_2["2. Открытие доступа к<br/>папке #quot;...рабочие<br/>Документы#quot; отделению<br/>Исполнен…"]
    s_pk_3["3. Размещение в папке<br/>#quot;КОНТРАКТАЦИЯ#quot; документов:"]
    s_pk_4["4. Постановка Задачи на<br/>Контрактацию"]
  end
  s_pk_0 --> s_pk_1
  s_pk_1 --> s_pk_2
  s_pk_2 --> s_pk_3
  s_pk_3 --> s_pk_4
```

| № | Шаг | H Менеджер |
|---|---|---|
| 0 | Вход в процесс "Передача в Контрактацию" | И |
| 1 | Создание в папке Проекта подпапки "...Рабочие документы" и создание в ней папки "КОНТРАКТАЦИЯ". | И |
| 2 | Открытие доступа к папке "...рабочие Документы" отделению Исполнения | И |
| 3 | Размещение в папке "КОНТРАКТАЦИЯ" документов: | И |
| 4 | Постановка Задачи на Контрактацию | И |

И — исполнитель, С — соисполнитель, Сг — согласование, У — информируемый, В — владелец процесса.

## По обязанностям

Дорожки — должности, которые мы предполагаем; узлы — обязанности. Сплошная стрелка — ставит задачу или передаёт результат, пунктир — следит или согласует; стрелка без подписи — дальше по порядку.

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart TB
  subgraph r_prodazhi["Менеджер по продажам"]
    o_reshenie_kontraktatsiya("Решающий начать<br/>контрактацию")
    o_papka_proekta("Ведущий папку проекта")
    o_postanovka_kontraktatsii("Ставящий задачу на<br/>контрактацию")
    o_dogovor_s_zakazchikom("Ведущий договор с<br/>заказчиком")
  end
  o_postanovka_kontraktatsii -->|"Задача «Заключить<br/>договор»"| o_dogovor_s_zakazchikom
  o_reshenie_kontraktatsiya --> o_papka_proekta
  o_papka_proekta --> o_postanovka_kontraktatsii
```

## Шаги и обязанности

| № | Шаг | Делает | Ставит → принимает | Передаёт | Согласуют, помогают, узнают | Где |
|---|---|---|---|---|---|---|
| 0 | Вход в процесс "Передача в Контрактацию" | [Решающий начать контрактацию](../../reg/oby/reshenie-kontraktatsiya.md) | — → — |  |  | [Битрикс24: статус проекта](../../reg/mes.md#bitriks-status-proekta), [Почта](../../reg/mes.md#pochta) |
| 1 | Создание в папке Проекта подпапки "...Рабочие документы" и создание в ней папки "КОНТРАКТАЦИЯ". | [Ведущий папку проекта](../../reg/oby/papka-proekta.md) | — → — |  |  | [Диск: «Рабочие документы» → «Контрактация», «Договор»](../../reg/mes.md#disk-kontraktatsiya) |
| 2 | Открытие доступа к папке "...рабочие Документы" отделению Исполнения | [Ведущий папку проекта](../../reg/oby/papka-proekta.md) | — → — |  | узнают о результате: [Логист](../../reg/rol/logist.md) | [Google Диск: папка проекта](../../reg/mes.md#disk-papka-proekta) |
| 3 | Размещение в папке "КОНТРАКТАЦИЯ" документов: | [Ведущий папку проекта](../../reg/oby/papka-proekta.md) | — → — |  |  | [Диск: «Рабочие документы» → «Контрактация», «Договор»](../../reg/mes.md#disk-kontraktatsiya) |
| 4 | Постановка Задачи на Контрактацию | [Ставящий задачу на контрактацию](../../reg/oby/postanovka-kontraktatsii.md) | — → [Ведущий договор с заказчиком](../../reg/oby/dogovor-s-zakazchikom.md) | [Задача «Заключить договор»](../../reg/art.md#zadacha-kontraktatsiya) |  | [Битрикс24: задачи по шаблонам](../../reg/mes.md#bitriks-zadacha) |

## Где работают

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  o_reshenie_kontraktatsiya("Решающий начать<br/>контрактацию")
  o_papka_proekta("Ведущий папку проекта")
  o_postanovka_kontraktatsii("Ставящий задачу на<br/>контрактацию")
  subgraph v________["битрикс"]
    m_bitriks_status_proekta{{"Битрикс24: статус проекта"}}
    m_bitriks_zadacha{{"Битрикс24: задачи по<br/>шаблонам"}}
  end
  subgraph v______["почта"]
    m_pochta>"Почта"]
  end
  subgraph v_____["диск"]
    m_disk_kontraktatsiya[["Диск: «Рабочие документы»<br/>→ «Контрактация»,<br/>«Договор»"]]
    m_disk_papka_proekta[["Google Диск: папка проекта"]]
  end
  o_reshenie_kontraktatsiya --> m_bitriks_status_proekta
  o_reshenie_kontraktatsiya --> m_pochta
  o_papka_proekta --> m_disk_kontraktatsiya
  o_papka_proekta --> m_disk_papka_proekta
  o_postanovka_kontraktatsii --> m_bitriks_zadacha
```

## Статусы

**Статус проекта**

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
stateDiagram-v2
  direction LR
  state "Заключаем договор" as st0
  [*] --> st0
```

Дальше: [Процесс. Контрактация](../r02-kontraktatsiya/index.md).
