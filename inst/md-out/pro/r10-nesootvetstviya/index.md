> Черновик: текст не проверен.

# Устранение несоответствий

Процесс регламента «Распределение задач» (лист «10.10.2026 Версия К»), в регламенте — «ИСПОЛНЕНИЕ (устранение несоответствий)». Контур 4.
Как читать схемы и что значат обязанности — [обзор процессов](../../pro/obzor/index.md).

Шаги «как записано» — `reglament.yaml` (собран скриптом из регламента), наше толкование — `protsess.yaml`. Ниже всё собрано из них.

## Дорожки по должностям

Вертикальная дорожка — должность, которую мы предполагаем; заметка — шаг в её дорожке; стрелка — работа переходит к другой должности (ставит задачу или делает следующий шаг).

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
sequenceDiagram
  participant r_proekt as Менеджер проекта
  participant r_khranitel as Хранитель учёта и документов
  participant r_none as не знаем кто
  participant r_tekh as Технический эксперт
  rect rgb(255, 255, 255)
  Note over r_proekt: 16. Вход в процесс: поступление<br/>документов о несоответствии<br/>продукции требованиям договора
  Note over r_proekt: 17. Передача документа о<br/>несоответствии на регистрацию<br/>Координатору
  r_proekt->>r_khranitel: Документ о несоответствии
  Note over r_khranitel: 18. Регистрация в Журнале<br/>регистрации входящих документа о<br/>несоответствии
  Note over r_khranitel: 19. Размещение в папке Проекта<br/>документа о несоответствии
  Note over r_khranitel: 20. Передача документа о<br/>несоответствии менеджеру проекта с<br/>постановкой задачи
  r_khranitel->>r_proekt: Задача «Принятие решения по<br/>устранению несоответствий»,<br/>Документ о несоответствии
  Note over r_proekt: 21. Принятие решения по устранению<br/>несоответствий
  r_proekt->>r_none: Решение по устранению<br/>несоответствия
  Note over r_none: 22. Установка товарам статуса<br/>НЕСООТВЕТСТВИЕ
  r_none->>r_proekt: Задача «Принятие решения по<br/>устранению несоответствий»,<br/>Документ о несоответствии
  Note over r_proekt: 23. Выдача поручения по устранению<br/>несоответствий и организация его<br/>выполнения
  Note over r_proekt: 24. Выдача поручения по подготовке<br/>ответа на документ о<br/>несоответствии и организация его…
  Note over r_proekt: 25. Устранение несоответствий
  r_proekt->>r_tekh: Поручение подготовить ответ на<br/>несоответствие
  Note over r_tekh: 26. Подготовка предложений по<br/>ответу и согласование с<br/>заинтересованными сторонами
  Note over r_tekh: 27. Обеспечение отправки<br/>подготовленного ответа
  r_tekh->>r_proekt: Ответ на документ о несоответствии
  Note over r_proekt: 28. Сбор объяснений по<br/>возникновению несоответствий и<br/>сбор предложений по<br/>предотвращению/…
  Note over r_proekt: 29. Закрытие процесса Устранение<br/>несоответствий
  end
```

## Как в регламенте

Дорожки — столбцы регламента с основным исполнителем; шаги — по порядку. Пунктир — шаг без исполнителя.

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart TB
  subgraph c_H["H Менеджер"]
    s_ns_17["17. Передача документа о<br/>несоответствии на<br/>регистрацию Координатору<br/>(…"]
    s_ns_21["21. Принятие решения по<br/>устранению несоответствий"]
    s_ns_23["23. Выдача поручения по<br/>устранению несоответствий<br/>и организация его в…"]
    s_ns_24["24. Выдача поручения по<br/>подготовке ответа на<br/>документ о несоответстви…"]
    s_ns_25["25. Устранение<br/>несоответствий"]
    s_ns_28["28. Сбор объяснений по<br/>возникновению<br/>несоответствий и сбор<br/>предложени…"]
    s_ns_29["29. Закрытие процесса<br/>Устранение несоответствий"]
  end
  subgraph c_I["I ТС (эксперт)"]
    s_ns_26["26. Подготовка предложений<br/>по ответу и согласование с<br/>заинтересованны…"]
    s_ns_27["27. Обеспечение отправки<br/>подготовленного ответа"]
  end
  subgraph c_K["столбец K"]
    s_ns_18["18. Регистрация в Журнале<br/>регистрации входящих<br/>документа о несоответс…"]
    s_ns_19["19. Размещение в папке<br/>Проекта документа о<br/>несоответствии"]
    s_ns_20["20. Передача документа о<br/>несоответствии менеджеру<br/>проекта с постановк…"]
  end
  subgraph c_none["нет исполнителя"]
    s_ns_16["16. Вход в процесс:<br/>поступление документов о<br/>несоответствии продукции…"]
    s_ns_22["22. Установка товарам<br/>статуса НЕСООТВЕТСТВИЕ"]
  end
  s_ns_16 --> s_ns_17
  s_ns_17 --> s_ns_18
  s_ns_18 --> s_ns_19
  s_ns_19 --> s_ns_20
  s_ns_20 --> s_ns_21
  s_ns_21 --> s_ns_22
  s_ns_22 --> s_ns_23
  s_ns_23 --> s_ns_24
  s_ns_24 --> s_ns_25
  s_ns_25 --> s_ns_26
  s_ns_26 --> s_ns_27
  s_ns_27 --> s_ns_28
  s_ns_28 --> s_ns_29
  classDef none stroke-dasharray: 5 5
  class s_ns_16,s_ns_22 none
```

| № | Шаг | H Менеджер | I ТС (эксперт) | J Закупщик | столбец K | L АС | столбец M |
|---|---|---|---|---|---|---|---|
| 16 | Вход в процесс: поступление документов о несоответствии продукции требованиям договора |  |  |  |  |  |  |
| 17 | Передача документа о несоответствии на регистрацию Координатору | И | И |  | У | И | И |
| 18 | Регистрация в Журнале регистрации входящих документа о несоответствии |  |  |  | И |  |  |
| 19 | Размещение в папке Проекта документа о несоответствии |  |  |  | И |  |  |
| 20 | Передача документа о несоответствии менеджеру проекта с постановкой задачи | У |  |  | И |  |  |
| 21 | Принятие решения по устранению несоответствий | И |  |  |  |  |  |
| 22 | Установка товарам статуса НЕСООТВЕТСТВИЕ |  |  |  |  |  |  |
| 23 | Выдача поручения по устранению несоответствий и организация его выполнения | И |  |  |  |  |  |
| 24 | Выдача поручения по подготовке ответа на документ о несоответствии и организация его выполнения | И |  |  |  |  |  |
| 25 | Устранение несоответствий | И | С | С | С | С |  |
| 26 | Подготовка предложений по ответу и согласование с заинтересованными сторонами | Сг | И | Сг |  | Сг |  |
| 27 | Обеспечение отправки подготовленного ответа | У | И |  |  | У |  |
| 28 | Сбор объяснений по возникновению несоответствий и сбор предложений по предотвращению/снижению рисков возникновения подобных несоответствий | И | С | С | С | С |  |
| 29 | Закрытие процесса Устранение несоответствий | И |  |  |  | С |  |

И — исполнитель, С — соисполнитель, Сг — согласование, У — информируемый, В — владелец процесса.

## По обязанностям

Дорожки — должности, которые мы предполагаем; узлы — обязанности. Сплошная стрелка — ставит задачу или передаёт результат, пунктир — следит или согласует; стрелка без подписи — дальше по порядку.

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart TB
  subgraph r_proekt["Менеджер проекта"]
    o_otvetstvennyy_za_yashchik("Ответственный за почтовый<br/>ящик")
    o_vedenie_nesootvetstviya("Ведущий устранение<br/>несоответствия")
  end
  subgraph r_khranitel["Хранитель учёта и<br/>документов"]
    o_registratsiya_vhodyashchih("Регистрирующий входящие")
  end
  subgraph r_none["не знаем кто"]
    o_status_nesootvetstvie("Ставящий товарам статус<br/>«Несоответствие»")
  end
  subgraph r_tekh["Технический эксперт"]
    o_otvet_nesootvetstvie("Готовящий ответ на<br/>несоответствие")
  end
  o_registratsiya_vhodyashchih -->|"ставит"| o_vedenie_nesootvetstviya
  o_vedenie_nesootvetstviya -->|"ставит"| o_otvet_nesootvetstvie
  o_otvetstvennyy_za_yashchik -->|"Документ о<br/>несоответствии"| o_registratsiya_vhodyashchih
  o_vedenie_nesootvetstviya -.->|"согласует"| o_otvet_nesootvetstvie
  o_vedenie_nesootvetstviya --> o_status_nesootvetstvie
  o_status_nesootvetstvie --> o_vedenie_nesootvetstviya
```

## Шаги и обязанности

| № | Шаг | Делает | Ставит → принимает | Передаёт | Согласуют, помогают, узнают | Где |
|---|---|---|---|---|---|---|
| 16 | Вход в процесс: поступление документов о несоответствии продукции требованиям договора<br/>*Вход в процесс — у шага нет исполнителя; по смыслу документ получает ответственный за ящик.* | [Ответственный за почтовый ящик](../../reg/oby/otvetstvennyy-za-yashchik.md) | — → — |  |  | [Почта](../../reg/mes.md#pochta) |
| 17 | Передача документа о несоответствии на регистрацию Координатору | [Ответственный за почтовый ящик](../../reg/oby/otvetstvennyy-za-yashchik.md) | — → [Регистрирующий входящие](../../reg/oby/registratsiya-vhodyashchih.md) | [Документ о несоответствии](../../reg/art.md#dokument-nesootv) |  | [Почта](../../reg/mes.md#pochta) |
| 18 | Регистрация в Журнале регистрации входящих документа о несоответствии | [Регистрирующий входящие](../../reg/oby/registratsiya-vhodyashchih.md) | — → — |  |  | [Журнал регистрации входящих](../../reg/mes.md#zhurnal-vhodyashchih) |
| 19 | Размещение в папке Проекта документа о несоответствии | [Регистрирующий входящие](../../reg/oby/registratsiya-vhodyashchih.md) | — → — |  |  | [Диск: документы исполнения](../../reg/mes.md#disk-ispolnenie) |
| 20 | Передача документа о несоответствии менеджеру проекта с постановкой задачи | [Регистрирующий входящие](../../reg/oby/registratsiya-vhodyashchih.md) | — → [Ведущий устранение несоответствия](../../reg/oby/vedenie-nesootvetstviya.md) | [Задача «Принятие решения по устранению несоответствий»](../../reg/art.md#zadacha-nesootv), [Документ о несоответствии](../../reg/art.md#dokument-nesootv) |  | [Битрикс24: задачи по шаблонам](../../reg/mes.md#bitriks-zadacha) |
| 21 | Принятие решения по устранению несоответствий | [Ведущий устранение несоответствия](../../reg/oby/vedenie-nesootvetstviya.md) | [Регистрирующий входящие](../../reg/oby/registratsiya-vhodyashchih.md) → — | [Решение по устранению несоответствия](../../reg/art.md#reshenie-nesootv) |  | [Битрикс24: задачи по шаблонам](../../reg/mes.md#bitriks-zadacha) |
| 22 | Установка товарам статуса НЕСООТВЕТСТВИЕ | [Ставящий товарам статус «Несоответствие»](../../reg/oby/status-nesootvetstvie.md) | — → — |  |  |  |
| 23 | Выдача поручения по устранению несоответствий и организация его выполнения | [Ведущий устранение несоответствия](../../reg/oby/vedenie-nesootvetstviya.md) | — → — |  |  |  |
| 24 | Выдача поручения по подготовке ответа на документ о несоответствии и организация его выполнения | [Ведущий устранение несоответствия](../../reg/oby/vedenie-nesootvetstviya.md) | — → [Готовящий ответ на несоответствие](../../reg/oby/otvet-nesootvetstvie.md) | [Поручение подготовить ответ на несоответствие](../../reg/art.md#poruchenie-otvet) |  |  |
| 25 | Устранение несоответствий | [Ведущий устранение несоответствия](../../reg/oby/vedenie-nesootvetstviya.md) | — → — |  | помогают: [Технический эксперт (ТС)](../../reg/rol/tekh.md), [Закупщик (специалист по закупке)](../../reg/rol/zakupka.md), [Хранитель учёта и документов (столбец K)](../../reg/rol/khranitel.md), [Логист](../../reg/rol/logist.md) |  |
| 26 | Подготовка предложений по ответу и согласование с заинтересованными сторонами<br/>*Регламент: согласуют менеджер, закупщик и логист.* | [Готовящий ответ на несоответствие](../../reg/oby/otvet-nesootvetstvie.md) | [Ведущий устранение несоответствия](../../reg/oby/vedenie-nesootvetstviya.md) → — | [Ответ на документ о несоответствии](../../reg/art.md#otvet-nesootv) | согласуют: [Ведущий устранение несоответствия](../../reg/oby/vedenie-nesootvetstviya.md); помогают: [Закупщик (специалист по закупке)](../../reg/rol/zakupka.md), [Логист](../../reg/rol/logist.md) |  |
| 27 | Обеспечение отправки подготовленного ответа | [Готовящий ответ на несоответствие](../../reg/oby/otvet-nesootvetstvie.md) | — → — | [Ответ на документ о несоответствии](../../reg/art.md#otvet-nesootv) | узнают о результате: [Менеджер проекта](../../reg/rol/proekt.md), [Логист](../../reg/rol/logist.md) | [Почта](../../reg/mes.md#pochta) |
| 28 | Сбор объяснений по возникновению несоответствий и сбор предложений по предотвращению/снижению рисков возникновения подобных несоответствий | [Ведущий устранение несоответствия](../../reg/oby/vedenie-nesootvetstviya.md) | — → — | [Объяснения и предложения по предотвращению](../../reg/art.md#obyasneniya) | помогают: [Технический эксперт (ТС)](../../reg/rol/tekh.md), [Закупщик (специалист по закупке)](../../reg/rol/zakupka.md), [Хранитель учёта и документов (столбец K)](../../reg/rol/khranitel.md), [Логист](../../reg/rol/logist.md) |  |
| 29 | Закрытие процесса Устранение несоответствий | [Ведущий устранение несоответствия](../../reg/oby/vedenie-nesootvetstviya.md) | — → — |  | помогают: [Логист](../../reg/rol/logist.md) |  |

## Где работают

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  o_otvetstvennyy_za_yashchik("Ответственный за почтовый<br/>ящик")
  o_registratsiya_vhodyashchih("Регистрирующий входящие")
  o_vedenie_nesootvetstviya("Ведущий устранение<br/>несоответствия")
  o_otvet_nesootvetstvie("Готовящий ответ на<br/>несоответствие")
  subgraph v______["почта"]
    m_pochta>"Почта"]
  end
  subgraph v________["внешнее"]
    m_zhurnal_vhodyashchih>"Журнал регистрации<br/>входящих"]
  end
  subgraph v_____["диск"]
    m_disk_ispolnenie[["Диск: документы исполнения"]]
  end
  subgraph v________["битрикс"]
    m_bitriks_zadacha{{"Битрикс24: задачи по<br/>шаблонам"}}
  end
  o_otvetstvennyy_za_yashchik --> m_pochta
  o_registratsiya_vhodyashchih --> m_zhurnal_vhodyashchih
  o_registratsiya_vhodyashchih --> m_disk_ispolnenie
  o_registratsiya_vhodyashchih --> m_bitriks_zadacha
  o_vedenie_nesootvetstviya --> m_bitriks_zadacha
  o_otvet_nesootvetstvie --> m_pochta
```

## Статусы

**Статус товара**

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
stateDiagram-v2
  direction LR
  state "НЕСООТВЕТСТВИЕ" as st0
  [*] --> st0
```
