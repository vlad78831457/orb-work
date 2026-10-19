> Черновик: текст не проверен.

# Закрытие проекта

Процесс регламента «Распределение задач» (лист «10.10.2026 Версия К»), в регламенте — «ЗАКРЫТИЕ ПРОЕКТА». Контур 0.
Как читать схемы и что значат обязанности — [обзор процессов](../../pro/obzor/index.md).

Шаги «как записано» — `reglament.yaml` (собран скриптом из регламента), наше толкование — `protsess.yaml`. Ниже всё собрано из них.

## Дорожки по должностям

Вертикальная дорожка — должность, которую мы предполагаем; заметка — шаг в её дорожке; стрелка — работа переходит к другой должности (ставит задачу или делает следующий шаг).

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
sequenceDiagram
  participant r_none as не знаем кто
  rect rgb(255, 255, 255)
  Note over r_none: 0. вход: выполнение следующих<br/>условий: - Выполнены обязательства<br/>по поставке (товар приня…
  Note over r_none: 1. Формирование фактического<br/>финансового результата проекта и<br/>расчет финансовых показател…
  Note over r_none: 2. Пополнение фонда косвенных<br/>расходов
  Note over r_none: 3. Анализ План-факта
  Note over r_none: 4. Присвоение статуса Закрыт
  end
```

## Как в регламенте

Дорожки — столбцы регламента с основным исполнителем; шаги — по порядку. Пунктир — шаг без исполнителя.

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart TB
  subgraph c_none["нет исполнителя"]
    s_zp_0["0. вход: выполнение<br/>следующих условий: -<br/>Выполнены обязательства по<br/>п…"]
    s_zp_1["1. Формирование<br/>фактического финансового<br/>результата проекта и<br/>расчет…"]
    s_zp_2["2. Пополнение фонда<br/>косвенных расходов"]
    s_zp_3["3. Анализ План-факта"]
    s_zp_4["4. Присвоение статуса<br/>Закрыт"]
  end
  s_zp_0 --> s_zp_1
  s_zp_1 --> s_zp_2
  s_zp_2 --> s_zp_3
  s_zp_3 --> s_zp_4
  classDef none stroke-dasharray: 5 5
  class s_zp_0,s_zp_1,s_zp_2,s_zp_3,s_zp_4 none
```

| № | Шаг |  |
|---|---|
| 0 | вход: выполнение следующих условий: - Выполнены обязательства по поставке (товар принят); - выполнены обызательства по оплате товара Покупателем. - В системе учета содержатся все затраты по проекту. - Завершена претензионно исковая работа (с покупателем и поставщиками) |  |
| 1 | Формирование фактического финансового результата проекта и расчет финансовых показателей проекта |  |
| 2 | Пополнение фонда косвенных расходов |  |
| 3 | Анализ План-факта |  |
| 4 | Присвоение статуса Закрыт |  |

И — исполнитель, С — соисполнитель, Сг — согласование, У — информируемый, В — владелец процесса.

## По обязанностям

Дорожки — должности, которые мы предполагаем; узлы — обязанности. Сплошная стрелка — ставит задачу или передаёт результат, пунктир — следит или согласует; стрелка без подписи — дальше по порядку.

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart TB
  subgraph r_none["не знаем кто"]
    o_zakrytie_proekta("Закрывающий проект")
  end
```

## Шаги и обязанности

| № | Шаг | Делает | Ставит → принимает | Передаёт | Согласуют, помогают, узнают | Где |
|---|---|---|---|---|---|---|
| 0 | вход: выполнение следующих условий: - Выполнены обязательства по поставке (товар принят); - выполнены обызательства по оплате товара Покупателем. - В системе учета содержатся все затраты по проекту. - Завершена претензионно исковая работа (с покупателем и поставщиками) | [Закрывающий проект](../../reg/oby/zakrytie-proekta.md) | — → — |  |  |  |
| 1 | Формирование фактического финансового результата проекта и расчет финансовых показателей проекта | [Закрывающий проект](../../reg/oby/zakrytie-proekta.md) | — → — |  |  |  |
| 2 | Пополнение фонда косвенных расходов | [Закрывающий проект](../../reg/oby/zakrytie-proekta.md) | — → — |  |  |  |
| 3 | Анализ План-факта | [Закрывающий проект](../../reg/oby/zakrytie-proekta.md) | — → — |  |  |  |
| 4 | Присвоение статуса Закрыт | [Закрывающий проект](../../reg/oby/zakrytie-proekta.md) | — → — |  |  | [Битрикс24: статус проекта](../../reg/mes.md#bitriks-status-proekta) |

## Где работают

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  o_zakrytie_proekta("Закрывающий проект")
  subgraph v________["битрикс"]
    m_bitriks_status_proekta{{"Битрикс24: статус проекта"}}
  end
  o_zakrytie_proekta --> m_bitriks_status_proekta
```

## Статусы

**Статус проекта**

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
stateDiagram-v2
  direction LR
  state "Закрыт" as st0
  [*] --> st0
```
