> Черновик: текст не проверен.

# Контрактация

Процесс регламента «Распределение задач» (лист «10.10.2026 Версия К»), в регламенте — «КОНТРАКТАЦИЯ». Контур 0.
Как читать схемы и что значат обязанности — [обзор процессов](../../pro/obzor/index.md).

Шаги «как записано» — `reglament.yaml` (собран скриптом из регламента), наше толкование — `protsess.yaml`. Ниже всё собрано из них.

## Дорожки по должностям

Вертикальная дорожка — должность, которую мы предполагаем; заметка — шаг в её дорожке; стрелка — работа переходит к другой должности (ставит задачу или делает следующий шаг).

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
sequenceDiagram
  participant r_prodazhi as Менеджер по продажам
  participant r_khranitel as Хранитель учёта и документов
  participant r_tekh as Технический эксперт
  participant r_podpisant as Подписант и плательщик
  participant r_logist as Логист
  rect rgb(255, 255, 255)
  Note over r_prodazhi: 5. Взаимодействие с Заказчиком по<br/>вопросу ЗАКЛЮЧЕНИЯ договора
  Note over r_prodazhi: 6. Заполнение раздела КОНТРАКТАЦИЯ<br/>на листе 0-0 Паспорт проекта
  Note over r_prodazhi: 7. Создание в папке Проекта<br/>подпапки #quot;...Рабочие документы#quot;<br/>папки #quot;Договор#quot;.
  Note over r_prodazhi: 8. Получение проекта договора от<br/>заказчика. (примечание: проект<br/>договора в данном контекс…
  Note over r_prodazhi: 9. Постановка задачи на проверку<br/>(или заполнение, если к нам вошел<br/>договор в редактируемо…
  r_prodazhi->>r_khranitel: Подзадача «Оформить договор»,<br/>Проект договора заказчика
  Note over r_khranitel: 10. Заполнение/проверка проекта<br/>договора.
  r_khranitel->>r_prodazhi: Заключение по проекту договора
  Note over r_prodazhi: 11. Постановка задачи на проверку<br/>ТЗ (или заполнение, если к нам<br/>вошел договор в редактир…
  r_prodazhi->>r_tekh: Подзадача на проверку ТЗ
  Note over r_tekh: 12. Заполнение/проверка ТЗ
  r_tekh->>r_prodazhi: Заключение по ТЗ
  Note over r_prodazhi: 13. Взаимодействие с Заказчиком по<br/>вопросу ПОДПИСАНИЯ договора
  Note over r_prodazhi: 14. Информирование M, о том, что<br/>надо подписать договор через ЭДО
  r_prodazhi->>r_podpisant: Просьба подписать договор через<br/>ЭДО
  Note over r_podpisant: 15. Подписание договора через ЭДО
  r_podpisant->>r_prodazhi: Подписанный договор с заказчиком
  Note over r_prodazhi: 16. Направление скан копии<br/>подписанного договора заказчику.
  r_prodazhi->>r_logist: Оригинал договора для заказчика
  Note over r_logist: 17. Направление подписанного<br/>оригинала договора заказчику.
  r_logist-->>r_prodazhi: дальше
  Note over r_prodazhi: 18. Передача в отдел Исполнения<br/>заключенного договора для внесения<br/>информации в 1с и табл…
  Note over r_prodazhi: 19. Закрытие этапа Контрактация
  Note over r_prodazhi: 20. Приемка этапа Контрактации
  end
```

## Как в регламенте

Дорожки — столбцы регламента с основным исполнителем; шаги — по порядку. Пунктир — шаг без исполнителя.

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart TB
  subgraph c_H["H Менеджер"]
    s_kt_5["5. Взаимодействие с<br/>Заказчиком по вопросу<br/>ЗАКЛЮЧЕНИЯ договора"]
    s_kt_6["6. Заполнение раздела<br/>КОНТРАКТАЦИЯ на листе 0-0<br/>Паспорт проекта"]
    s_kt_7["7. Создание в папке<br/>Проекта подпапки<br/>#quot;...Рабочие документы#quot;<br/>папки #quot;До…"]
    s_kt_8["8. Получение проекта<br/>договора от заказчика.<br/>(примечание: проект догов…"]
    s_kt_9["9. Постановка задачи на<br/>проверку (или заполнение,<br/>если к нам вошел до…"]
    s_kt_13["13. Взаимодействие с<br/>Заказчиком по вопросу<br/>ПОДПИСАНИЯ договора"]
    s_kt_14["14. Информирование M, о<br/>том, что надо подписать<br/>договор через ЭДО"]
    s_kt_16["16. Направление скан копии<br/>подписанного договора<br/>заказчику."]
    s_kt_18["18. Передача в отдел<br/>Исполнения заключенного<br/>договора для внесения ин…"]
    s_kt_19["19. Закрытие этапа<br/>Контрактация"]
    s_kt_20["20. Приемка этапа<br/>Контрактации"]
  end
  subgraph c_I["I ТС (эксперт)"]
    s_kt_12["12. Заполнение/проверка ТЗ"]
  end
  subgraph c_K["столбец K"]
    s_kt_10["10. Заполнение/проверка<br/>проекта договора."]
  end
  subgraph c_M["столбец M"]
    s_kt_15["15. Подписание договора<br/>через ЭДО"]
  end
  subgraph c_none["нет исполнителя"]
    s_kt_11["11. Постановка задачи на<br/>проверку ТЗ (или<br/>заполнение, если к нам<br/>воше…"]
    s_kt_17["17. Направление<br/>подписанного оригинала<br/>договора заказчику."]
  end
  s_kt_5 --> s_kt_6
  s_kt_6 --> s_kt_7
  s_kt_7 --> s_kt_8
  s_kt_8 --> s_kt_9
  s_kt_9 --> s_kt_10
  s_kt_10 --> s_kt_11
  s_kt_11 --> s_kt_12
  s_kt_12 --> s_kt_13
  s_kt_13 --> s_kt_14
  s_kt_14 --> s_kt_15
  s_kt_15 --> s_kt_16
  s_kt_16 --> s_kt_17
  s_kt_17 --> s_kt_18
  s_kt_18 --> s_kt_19
  s_kt_19 --> s_kt_20
  classDef none stroke-dasharray: 5 5
  class s_kt_11,s_kt_17 none
```

| № | Шаг | H Менеджер | I ТС (эксперт) | столбец K | L АС | столбец M |
|---|---|---|---|---|---|---|
| 5 | Взаимодействие с Заказчиком по вопросу ЗАКЛЮЧЕНИЯ договора | И |  |  |  |  |
| 6 | Заполнение раздела КОНТРАКТАЦИЯ на листе 0-0 Паспорт проекта | И |  |  |  |  |
| 7 | Создание в папке Проекта подпапки "...Рабочие документы" папки "Договор". | И |  |  |  |  |
| 8 | Получение проекта договора от заказчика. (примечание: проект договора в данном контексте это в том числе редактируемая версия текста договора). | И |  |  |  |  |
| 9 | Постановка задачи на проверку (или заполнение, если к нам вошел договор в редактируемом формате) направленного проекта договора. | И |  |  |  |  |
| 10 | Заполнение/проверка проекта договора. | С |  | И |  |  |
| 11 | Постановка задачи на проверку ТЗ (или заполнение, если к нам вошел договор в редактируемом формате) направленного ТЗ и перечня документов которые нужно включить в счета или договоры (лист 3-3) | С |  |  |  |  |
| 12 | Заполнение/проверка ТЗ | С | И |  |  |  |
| 13 | Взаимодействие с Заказчиком по вопросу ПОДПИСАНИЯ договора | И |  |  |  |  |
| 14 | Информирование M, о том, что надо подписать договор через ЭДО | И |  |  |  |  |
| 15 | Подписание договора через ЭДО |  |  |  |  | И |
| 16 | Направление скан копии подписанного договора заказчику. | И |  |  |  |  |
| 17 | Направление подписанного оригинала договора заказчику. |  |  |  | С | С |
| 18 | Передача в отдел Исполнения заключенного договора для внесения информации в 1с и табличные системы. | И |  |  |  |  |
| 19 | Закрытие этапа Контрактация | И |  |  |  |  |
| 20 | Приемка этапа Контрактации | И |  |  |  |  |

И — исполнитель, С — соисполнитель, Сг — согласование, У — информируемый, В — владелец процесса.

## По обязанностям

Дорожки — должности, которые мы предполагаем; узлы — обязанности. Сплошная стрелка — ставит задачу или передаёт результат, пунктир — следит или согласует; стрелка без подписи — дальше по порядку.

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart TB
  subgraph r_prodazhi["Менеджер по продажам"]
    o_dogovor_s_zakazchikom("Ведущий договор с<br/>заказчиком")
    o_pasport_kontraktatsiya("Ведущий раздел<br/>«Контрактация» паспорта")
    o_papka_proekta("Ведущий папку проекта")
    o_peredacha_v_uchet("Передающий договор в учёт")
    o_zakrytie_kontraktatsii("Закрывающий контрактацию")
  end
  subgraph r_khranitel["Хранитель учёта и<br/>документов"]
    o_proverka_dogovora("Проверяющий проект<br/>договора")
    o_uchet_1s("Ведущий учёт в 1С")
  end
  subgraph r_tekh["Технический эксперт"]
    o_proverka_tz("Проверяющий ТЗ договора")
  end
  subgraph r_podpisant["Подписант и плательщик"]
    o_podpisanie("Подписывающий договор")
  end
  subgraph r_logist["Логист"]
    o_otpravka_originalov("Отправляющий оригиналы<br/>документов")
  end
  subgraph r_koordinator["Координатор"]
    o_priemka_etapov("Принимающий этапы")
  end
  o_dogovor_s_zakazchikom -->|"ставит"| o_proverka_dogovora
  o_dogovor_s_zakazchikom -->|"ставит"| o_proverka_tz
  o_dogovor_s_zakazchikom -->|"ставит"| o_podpisanie
  o_proverka_dogovora -->|"Заключение по проекту<br/>договора"| o_dogovor_s_zakazchikom
  o_proverka_tz -->|"Заключение по ТЗ"| o_dogovor_s_zakazchikom
  o_peredacha_v_uchet -->|"Подзадача «внести<br/>договор в 1С и таблицы»"| o_uchet_1s
  o_zakrytie_kontraktatsii -->|"передаёт"| o_priemka_etapov
  o_dogovor_s_zakazchikom --> o_pasport_kontraktatsiya
  o_pasport_kontraktatsiya --> o_papka_proekta
  o_papka_proekta --> o_dogovor_s_zakazchikom
  o_dogovor_s_zakazchikom --> o_otpravka_originalov
  o_otpravka_originalov --> o_peredacha_v_uchet
  o_peredacha_v_uchet --> o_zakrytie_kontraktatsii
```

## Шаги и обязанности

| № | Шаг | Делает | Ставит → принимает | Передаёт | Согласуют, помогают, узнают | Где |
|---|---|---|---|---|---|---|
| 5 | Взаимодействие с Заказчиком по вопросу ЗАКЛЮЧЕНИЯ договора | [Ведущий договор с заказчиком](../../reg/oby/dogovor-s-zakazchikom.md) | — → — |  |  | [Почта](../../reg/mes.md#pochta) |
| 6 | Заполнение раздела КОНТРАКТАЦИЯ на листе 0-0 Паспорт проекта | [Ведущий раздел «Контрактация» паспорта](../../reg/oby/pasport-kontraktatsiya.md) | — → — |  |  | [Лист «0-Паспорт проекта»](../../reg/mes.md#lis-0-pasport) |
| 7 | Создание в папке Проекта подпапки "...Рабочие документы" папки "Договор". | [Ведущий папку проекта](../../reg/oby/papka-proekta.md) | — → — |  |  | [Диск: «Рабочие документы» → «Контрактация», «Договор»](../../reg/mes.md#disk-kontraktatsiya) |
| 8 | Получение проекта договора от заказчика. (примечание: проект договора в данном контексте это в том числе редактируемая версия текста договора). | [Ведущий договор с заказчиком](../../reg/oby/dogovor-s-zakazchikom.md) | — → — |  |  | [Почта](../../reg/mes.md#pochta), [Диск: «Рабочие документы» → «Контрактация», «Договор»](../../reg/mes.md#disk-kontraktatsiya), [Лист «0-Паспорт проекта»](../../reg/mes.md#lis-0-pasport) |
| 9 | Постановка задачи на проверку (или заполнение, если к нам вошел договор в редактируемом формате) направленного проекта договора.<br/>*Задача ставится K, в части ТЗ — ТС; подзадача «Оформить договор» внутри «Заключить договор».* | [Ведущий договор с заказчиком](../../reg/oby/dogovor-s-zakazchikom.md) | — → [Проверяющий проект договора](../../reg/oby/proverka-dogovora.md) | [Подзадача «Оформить договор»](../../reg/art.md#podzadacha-dogovor), [Проект договора заказчика](../../reg/art.md#proekt-dogovora) |  | [Битрикс24: задачи по шаблонам](../../reg/mes.md#bitriks-zadacha) |
| 10 | Заполнение/проверка проекта договора. | [Проверяющий проект договора](../../reg/oby/proverka-dogovora.md) | [Ведущий договор с заказчиком](../../reg/oby/dogovor-s-zakazchikom.md) → [Ведущий договор с заказчиком](../../reg/oby/dogovor-s-zakazchikom.md) | [Заключение по проекту договора](../../reg/art.md#zaklyuchenie-dogovor) | помогают: [Менеджер по продажам](../../reg/rol/prodazhi.md) |  |
| 11 | Постановка задачи на проверку ТЗ (или заполнение, если к нам вошел договор в редактируемом формате) направленного ТЗ и перечня документов которые нужно включить в счета или договоры (лист 3-3)<br/>*В регламенте у шага нет основного исполнителя — только соисполнитель H.* | [Ведущий договор с заказчиком](../../reg/oby/dogovor-s-zakazchikom.md) | — → [Проверяющий ТЗ договора](../../reg/oby/proverka-tz.md) | [Подзадача на проверку ТЗ](../../reg/art.md#podzadacha-tz) |  | [Битрикс24: задачи по шаблонам](../../reg/mes.md#bitriks-zadacha) |
| 12 | Заполнение/проверка ТЗ | [Проверяющий ТЗ договора](../../reg/oby/proverka-tz.md) | [Ведущий договор с заказчиком](../../reg/oby/dogovor-s-zakazchikom.md) → [Ведущий договор с заказчиком](../../reg/oby/dogovor-s-zakazchikom.md) | [Заключение по ТЗ](../../reg/art.md#zaklyuchenie-tz) |  | [Битрикс24: задачи по шаблонам](../../reg/mes.md#bitriks-zadacha) |
| 13 | Взаимодействие с Заказчиком по вопросу ПОДПИСАНИЯ договора | [Ведущий договор с заказчиком](../../reg/oby/dogovor-s-zakazchikom.md) | — → — |  |  | [Почта](../../reg/mes.md#pochta) |
| 14 | Информирование M, о том, что надо подписать договор через ЭДО | [Ведущий договор с заказчиком](../../reg/oby/dogovor-s-zakazchikom.md) | — → [Подписывающий договор](../../reg/oby/podpisanie.md) | [Просьба подписать договор через ЭДО](../../reg/art.md#poruchenie-podpisat) |  |  |
| 15 | Подписание договора через ЭДО | [Подписывающий договор](../../reg/oby/podpisanie.md) | [Ведущий договор с заказчиком](../../reg/oby/dogovor-s-zakazchikom.md) → — | [Подписанный договор с заказчиком](../../reg/art.md#dogovor-podpisannyy) |  | [ЭДО](../../reg/mes.md#edo) |
| 16 | Направление скан копии подписанного договора заказчику. | [Ведущий договор с заказчиком](../../reg/oby/dogovor-s-zakazchikom.md) | — → — | [Оригинал договора для заказчика](../../reg/art.md#original-dogovora) |  | [Почта](../../reg/mes.md#pochta), [Битрикс24: статус проекта](../../reg/mes.md#bitriks-status-proekta) |
| 17 | Направление подписанного оригинала договора заказчику. | [Отправляющий оригиналы документов](../../reg/oby/otpravka-originalov.md) | — → — |  |  | [Транспортная компания](../../reg/mes.md#transportnaya-kompaniya) |
| 18 | Передача в отдел Исполнения заключенного договора для внесения информации в 1с и табличные системы. | [Передающий договор в учёт](../../reg/oby/peredacha-v-uchet.md) | — → [Ведущий учёт в 1С](../../reg/oby/uchet-1s.md) | [Подзадача «внести договор в 1С и таблицы»](../../reg/art.md#podzadacha-uchet) |  | [Битрикс24: задачи по шаблонам](../../reg/mes.md#bitriks-zadacha) |
| 19 | Закрытие этапа Контрактация | [Закрывающий контрактацию](../../reg/oby/zakrytie-kontraktatsii.md) | — → — |  |  | [Битрикс24: статус проекта](../../reg/mes.md#bitriks-status-proekta), [Битрикс24: задачи по шаблонам](../../reg/mes.md#bitriks-zadacha) |
| 20 | Приемка этапа Контрактации | [Закрывающий контрактацию](../../reg/oby/zakrytie-kontraktatsii.md) | — → [Принимающий этапы](../../reg/oby/priemka-etapov.md) |  |  | [Битрикс24: задачи по шаблонам](../../reg/mes.md#bitriks-zadacha) |

## Где работают

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  o_dogovor_s_zakazchikom("Ведущий договор с<br/>заказчиком")
  o_pasport_kontraktatsiya("Ведущий раздел<br/>«Контрактация» паспорта")
  o_papka_proekta("Ведущий папку проекта")
  o_proverka_tz("Проверяющий ТЗ договора")
  o_podpisanie("Подписывающий договор")
  o_otpravka_originalov("Отправляющий оригиналы<br/>документов")
  o_peredacha_v_uchet("Передающий договор в учёт")
  o_zakrytie_kontraktatsii("Закрывающий контрактацию")
  subgraph v______["почта"]
    m_pochta>"Почта"]
  end
  subgraph v_____["лист"]
    m_lis_0_pasport[/"Лист «0-Паспорт проекта»"/]
  end
  subgraph v_____["диск"]
    m_disk_kontraktatsiya[["Диск: «Рабочие документы»<br/>→ «Контрактация»,<br/>«Договор»"]]
  end
  subgraph v________["битрикс"]
    m_bitriks_zadacha{{"Битрикс24: задачи по<br/>шаблонам"}}
    m_bitriks_status_proekta{{"Битрикс24: статус проекта"}}
  end
  subgraph v____["эдо"]
    m_edo>"ЭДО"]
  end
  subgraph v________["внешнее"]
    m_transportnaya_kompaniya>"Транспортная компания"]
  end
  o_dogovor_s_zakazchikom --> m_pochta
  o_pasport_kontraktatsiya --> m_lis_0_pasport
  o_papka_proekta --> m_disk_kontraktatsiya
  o_dogovor_s_zakazchikom --> m_disk_kontraktatsiya
  o_dogovor_s_zakazchikom --> m_lis_0_pasport
  o_dogovor_s_zakazchikom --> m_bitriks_zadacha
  o_proverka_tz --> m_bitriks_zadacha
  o_podpisanie --> m_edo
  o_dogovor_s_zakazchikom --> m_bitriks_status_proekta
  o_otpravka_originalov --> m_transportnaya_kompaniya
  o_peredacha_v_uchet --> m_bitriks_zadacha
  o_zakrytie_kontraktatsii --> m_bitriks_status_proekta
  o_zakrytie_kontraktatsii --> m_bitriks_zadacha
```

## Статусы

**Статус проекта**

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
stateDiagram-v2
  direction LR
  state "Договор заключен" as st0
  [*] --> st0
```

Дальше: [Процесс. Передача в закупки](../r03-peredacha-v-zakupki/index.md).
