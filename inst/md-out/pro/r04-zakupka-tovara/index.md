> Черновик: текст не проверен.

# Закупка товара

Процесс регламента «Распределение задач» (лист «10.10.2026 Версия К»), в регламенте — «ЗАКУПКА ТОВАРА (владелец процесса - Закупщик)». Контур 2.
Как читать схемы и что значат обязанности — [обзор процессов](../../pro/obzor/index.md).

Шаги «как записано» — `reglament.yaml` (собран скриптом из регламента), наше толкование — `protsess.yaml`. Ниже всё собрано из них.

## Дорожки по должностям

Вертикальная дорожка — должность, которую мы предполагаем; заметка — шаг в её дорожке; стрелка — работа переходит к другой должности (ставит задачу или делает следующий шаг).

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
sequenceDiagram
  participant r_zakupka as Закупщик
  participant r_proekt as Менеджер проекта
  participant r_tekh as Технический эксперт
  participant r_khranitel as Хранитель учёта и документов
  participant r_podpisant as Подписант и плательщик
  rect rgb(255, 255, 255)
  r_proekt->>r_zakupka: Задача «Закупка»
  Note over r_zakupka: 0. Вход в процесс- Поставлена<br/>задача на закупку по проекту.<br/>№Проекта -Закзачик-предмет: З…
  Note over r_zakupka: 1. Создание в папке #quot;...Рабочие<br/>документы#quot; подпапки #quot;Закупки#quot;
  Note over r_zakupka: 2. Создание в папке #quot;... Закупки#quot;<br/>подпапок #quot;Счета#quot;, #quot;Договоры#quot; и #quot;В<br/>оплату#quot;
  Note over r_zakupka: 3. Повторная рассылка и заполнение<br/>внешней таблицы
  r_zakupka->>r_proekt: Предложения поставщиков (листы<br/>5-1, 5-2)
  Note over r_proekt: 4. Отслеживание комментариев по<br/>итогу общения с выбранными<br/>поставщиками на листе #quot;5 Закуп…
  Note over r_proekt: 5. Отслеживания результатов<br/>повторной рассылки на листе #quot;3-3<br/>Выбор поставщиков#quot; В случае…
  r_proekt->>r_zakupka: Решения по выбору поставщиков<br/>(лист 5-3)
  Note over r_zakupka: 6. Определение предложений с<br/>лучшими условиями и подготовка<br/>предложения по Окончательному…
  Note over r_zakupka: 7. Проверка выбранных поставщиков<br/>на добросовестность
  Note over r_zakupka: 8. Постановка задачи на проверку<br/>выбранных предложений ТС
  r_zakupka->>r_tekh: Подзадача ТС на проверку<br/>предложений
  Note over r_tekh: 9. Рассмотрение предложений<br/>поставщиков в технической части
  r_tekh->>r_proekt: Заключение ТС по предложениям
  Note over r_proekt: 10. Решение о заключении сделки с<br/>выбранным поставщиком
  r_proekt->>r_zakupka: Решение о сделке с поставщиком
  Note over r_zakupka: 11. Подготовка договора поставки с<br/>поставщиком
  Note over r_zakupka: 12. Получение подписанных<br/>договоров или оформленных по нашим<br/>требованиям счетов от выбран…
  Note over r_zakupka: 13. Ведение Листа 5 (Таблица<br/>закупки внешняя) ( 5-4 в будущем)
  Note over r_zakupka: 14. Постановка Задачи на<br/>согласование счетов/договоров в<br/>технической части
  Note over r_zakupka: 15. Рассмотрение и согласование<br/>счетов и договоров и других<br/>документов в технической част…
  Note over r_zakupka: 16. Размещение в папке #quot;в оплату#quot;<br/>согласованных с ТС счетов и<br/>договоров для оплаты
  Note over r_zakupka: 17. Постановка Задачи K на<br/>проверку и оплату счетов и<br/>договоров, созданию в 1с Заказа<br/>пок…
  Note over r_zakupka: 18. Информирование в задаче K о<br/>том, что размещены новые Счета и<br/>договора
  r_zakupka->>r_khranitel: Задача «Оплатить счета», Счета и<br/>договоры «готов к оплате»
  Note over r_khranitel: 19. Проверка готовых к оплате<br/>счетов и договоров
  Note over r_khranitel: 20. Создание заказа покупателя и<br/>поставщикам в 1с
  Note over r_khranitel: 21. Передача полученных счетов M<br/>на оплату
  r_khranitel->>r_podpisant: Проверенные счета на оплату
  Note over r_podpisant: 22. Оплата полученных счетов и<br/>передача платежных поручений K
  r_podpisant->>r_khranitel: Платёжные поручения
  Note over r_khranitel: 23. Создание в папке #quot;.... В<br/>оплату#quot; подпапки #quot;Оплачено#quot; и<br/>перемещение в нее всех оплачен…
  Note over r_khranitel: 24. Внесение в Таблицу Оплат<br/>сведений о произведенных оплатах<br/>по проекту
  r_khranitel->>r_zakupka: Сведения об оплатах (таблица<br/>оплат)
  Note over r_zakupka: 25. Закрытие этапа Закупки
  end
```

## Как в регламенте

Дорожки — столбцы регламента с основным исполнителем; шаги — по порядку. Пунктир — шаг без исполнителя.

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart TB
  subgraph c_H["H Менеджер"]
    s_zk_4["4. Отслеживание<br/>комментариев по итогу<br/>общения с выбранными<br/>поставщика…"]
    s_zk_5["5. Отслеживания<br/>результатов повторной<br/>рассылки на листе #quot;3-3<br/>Выбор по…"]
    s_zk_10["10. Решение о заключении<br/>сделки с выбранным<br/>поставщиком"]
  end
  subgraph c_I["I ТС (эксперт)"]
    s_zk_9["9. Рассмотрение<br/>предложений поставщиков в<br/>технической части"]
  end
  subgraph c_J["J Закупщик"]
    s_zk_0["0. Вход в процесс-<br/>Поставлена задача на<br/>закупку по проекту.<br/>№Проекта…"]
    s_zk_1["1. Создание в папке<br/>#quot;...Рабочие документы#quot;<br/>подпапки #quot;Закупки#quot;"]
    s_zk_2["2. Создание в папке #quot;...<br/>Закупки#quot; подпапок #quot;Счета#quot;,<br/>#quot;Договоры#quot; и #quot;В о…"]
    s_zk_3["3. Повторная рассылка и<br/>заполнение внешней таблицы"]
    s_zk_6["6. Определение предложений<br/>с лучшими условиями и<br/>подготовка предложен…"]
    s_zk_7["7. Проверка выбранных<br/>поставщиков на<br/>добросовестность"]
    s_zk_8["8. Постановка задачи на<br/>проверку выбранных<br/>предложений ТС"]
    s_zk_11["11. Подготовка договора<br/>поставки с поставщиком"]
    s_zk_12["12. Получение подписанных<br/>договоров или оформленных<br/>по нашим требован…"]
    s_zk_13["13. Ведение Листа 5<br/>(Таблица закупки внешняя)<br/>( 5-4 в будущем)"]
    s_zk_14["14. Постановка Задачи на<br/>согласование<br/>счетов/договоров в<br/>технической…"]
    s_zk_15["15. Рассмотрение и<br/>согласование счетов и<br/>договоров и других<br/>документо…"]
    s_zk_16["16. Размещение в папке #quot;в<br/>оплату#quot; согласованных с ТС<br/>счетов и договор…"]
    s_zk_17["17. Постановка Задачи K на<br/>проверку и оплату счетов и<br/>договоров, созд…"]
    s_zk_18["18. Информирование в<br/>задаче K о том, что<br/>размещены новые Счета и<br/>дого…"]
    s_zk_25["25. Закрытие этапа Закупки"]
  end
  subgraph c_K["столбец K"]
    s_zk_19["19. Проверка готовых к<br/>оплате счетов и договоров"]
    s_zk_20["20. Создание заказа<br/>покупателя и поставщикам в<br/>1с"]
    s_zk_21["21. Передача полученных<br/>счетов M на оплату"]
    s_zk_23["23. Создание в папке #quot;....<br/>В оплату#quot; подпапки<br/>#quot;Оплачено#quot; и перемещени…"]
    s_zk_24["24. Внесение в Таблицу<br/>Оплат сведений о<br/>произведенных оплатах по<br/>прое…"]
  end
  subgraph c_M["столбец M"]
    s_zk_22["22. Оплата полученных<br/>счетов и передача<br/>платежных поручений K"]
  end
  s_zk_0 --> s_zk_1
  s_zk_1 --> s_zk_2
  s_zk_2 --> s_zk_3
  s_zk_3 --> s_zk_4
  s_zk_4 --> s_zk_5
  s_zk_5 --> s_zk_6
  s_zk_6 --> s_zk_7
  s_zk_7 --> s_zk_8
  s_zk_8 --> s_zk_9
  s_zk_9 --> s_zk_10
  s_zk_10 --> s_zk_11
  s_zk_11 --> s_zk_12
  s_zk_12 --> s_zk_13
  s_zk_13 --> s_zk_14
  s_zk_14 --> s_zk_15
  s_zk_15 --> s_zk_16
  s_zk_16 --> s_zk_17
  s_zk_17 --> s_zk_18
  s_zk_18 --> s_zk_19
  s_zk_19 --> s_zk_20
  s_zk_20 --> s_zk_21
  s_zk_21 --> s_zk_22
  s_zk_22 --> s_zk_23
  s_zk_23 --> s_zk_24
  s_zk_24 --> s_zk_25
```

| № | Шаг | H Менеджер | I ТС (эксперт) | J Закупщик | столбец K | столбец M | N Владелец процесса |
|---|---|---|---|---|---|---|---|
| 0 | Вход в процесс- Поставлена задача на закупку по проекту. №Проекта -Закзачик-предмет: Закупить товары" (или принятие этой задачи?!) |  |  | И |  |  |  |
| 1 | Создание в папке "...Рабочие документы" подпапки "Закупки" |  |  | И |  |  |  |
| 2 | Создание в папке "... Закупки" подпапок "Счета", "Договоры" и "В оплату" |  |  | И |  |  |  |
| 3 | Повторная рассылка и заполнение внешней таблицы |  |  | И |  |  |  |
| 4 | Отслеживание комментариев по итогу общения с выбранными поставщиками на листе "5 Закупка товара". | И |  |  |  |  |  |
| 5 | Отслеживания результатов повторной рассылки на листе "3-3 Выбор поставщиков" В случае необходимости замены поставщиков, принятие решения по такой замене. | И |  |  |  |  |  |
| 6 | Определение предложений с лучшими условиями и подготовка предложения по Окончательному выбору поставщика. |  |  | И |  |  |  |
| 7 | Проверка выбранных поставщиков на добросовестность |  |  | И |  |  |  |
| 8 | Постановка задачи на проверку выбранных предложений ТС |  |  | И |  |  |  |
| 9 | Рассмотрение предложений поставщиков в технической части |  | И |  |  |  |  |
| 10 | Решение о заключении сделки с выбранным поставщиком | И |  |  |  |  |  |
| 11 | Подготовка договора поставки с поставщиком |  |  | И | С |  |  |
| 12 | Получение подписанных договоров или оформленных по нашим требованиям счетов от выбранных Поставщиков |  |  | И |  |  |  |
| 13 | Ведение Листа 5 (Таблица закупки внешняя) ( 5-4 в будущем) |  |  | И |  |  |  |
| 14 | Постановка Задачи на согласование счетов/договоров в технической части |  |  | И |  |  |  |
| 15 | Рассмотрение и согласование счетов и договоров и других документов в технической части (в том числе путем подготовки ТЗ для договора с поставщиком) | Сг | Сг | И |  |  | Сг |
| 16 | Размещение в папке "в оплату" согласованных с ТС счетов и договоров для оплаты |  |  | И |  |  |  |
| 17 | Постановка Задачи K на проверку и оплату счетов и договоров, созданию в 1с Заказа покупателя и заказов поставщикам |  |  | И |  |  |  |
| 18 | Информирование в задаче K о том, что размещены новые Счета и договора | С |  | И |  |  |  |
| 19 | Проверка готовых к оплате счетов и договоров |  |  |  | И |  |  |
| 20 | Создание заказа покупателя и поставщикам в 1с |  |  |  | И |  |  |
| 21 | Передача полученных счетов M на оплату |  |  |  | И |  |  |
| 22 | Оплата полученных счетов и передача платежных поручений K |  |  |  |  | И |  |
| 23 | Создание в папке ".... В оплату" подпапки "Оплачено" и перемещение в нее всех оплаченных счетов и договоров. Создание папки "Платежные поручения" и перемещение в нее всех Платежных поручений по оплаченным счетам и договорам |  |  |  | И |  |  |
| 24 | Внесение в Таблицу Оплат сведений о произведенных оплатах по проекту |  |  |  | И |  |  |
| 25 | Закрытие этапа Закупки | С |  | И |  |  |  |

И — исполнитель, С — соисполнитель, Сг — согласование, У — информируемый, В — владелец процесса.

## По обязанностям

Дорожки — должности, которые мы предполагаем; узлы — обязанности. Сплошная стрелка — ставит задачу или передаёт результат, пунктир — следит или согласует; стрелка без подписи — дальше по порядку.

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart TB
  subgraph r_zakupka["Закупщик"]
    o_prinyatie_zakupki("Принимающий задачу на<br/>закупку")
    o_papka_zakupki("Ведущий папку закупки")
    o_povtornaya_rassylka("Рассылающий повторные<br/>запросы")
    o_vybor_postavshchika("Готовящий выбор поставщика")
    o_proverka_kontragenta("Проверяющий контрагента")
    o_postanovka_teh_soglasovaniya("Ставящий задачи на<br/>техническое согласование")
    o_dogovor_postavki("Готовящий договор поставки")
    o_poluchenie_schetov("Добывающий счета и<br/>договоры")
    o_vedenie_sdelok("Ведущий лист оформления<br/>сделок")
    o_soglasovanie_dokumentov("Проводящий согласование<br/>документов сделки")
    o_v_oplatu("Передающий согласованное в<br/>оплату")
    o_postanovka_oplaty("Ставящий задачу на оплату")
    o_zakrytie_zakupki("Закрывающий закупку")
  end
  subgraph r_proekt["Менеджер проекта"]
    o_postanovka_zakupki("Ставящий задачу на закупку")
    o_kontrol_vybora("Отслеживающий выбор<br/>поставщиков")
    o_reshenie_sdelka("Решающий о сделке с<br/>поставщиком")
    o_soglasovanie_otkloneniy("Согласующий сделку и<br/>отклонения")
  end
  subgraph r_tekh["Технический эксперт"]
    o_teh_soglasovanie("Согласующий техническую<br/>часть")
  end
  subgraph r_vladelets["Владелец процесса"]
    o_soglasovanie_finansirovaniya("Согласующий финансирование<br/>сделки")
  end
  subgraph r_khranitel["Хранитель учёта и<br/>документов"]
    o_proverka_schetov("Проверяющий счета перед<br/>оплатой")
    o_uchet_1s("Ведущий учёт в 1С")
    o_peredacha_na_oplatu("Передающий счета на оплату")
    o_arhiv_oplat("Раскладывающий оплаченное")
    o_tablitsa_oplat("Ведущий таблицу оплат")
  end
  subgraph r_podpisant["Подписант и плательщик"]
    o_oplata("Оплачивающий счета")
  end
  subgraph r_logist["Логист"]
    o_kontrol_postavki("Отслеживающий поставку")
  end
  o_postanovka_zakupki -->|"ставит"| o_prinyatie_zakupki
  o_postanovka_teh_soglasovaniya -->|"ставит"| o_teh_soglasovanie
  o_postanovka_oplaty -->|"ставит"| o_proverka_schetov
  o_postanovka_oplaty -->|"ставит"| o_uchet_1s
  o_peredacha_na_oplatu -->|"ставит"| o_oplata
  o_kontrol_vybora -.->|"следит"| o_vybor_postavshchika
  o_teh_soglasovanie -->|"Заключение ТС по<br/>предложениям"| o_postanovka_teh_soglasovaniya
  o_soglasovanie_finansirovaniya -.->|"согласует"| o_reshenie_sdelka
  o_teh_soglasovanie -.->|"согласует"| o_soglasovanie_dokumentov
  o_soglasovanie_otkloneniy -.->|"согласует"| o_soglasovanie_dokumentov
  o_soglasovanie_finansirovaniya -.->|"согласует"| o_soglasovanie_dokumentov
  o_oplata -->|"Платёжные поручения"| o_arhiv_oplat
  o_tablitsa_oplat -->|"Сведения об оплатах<br/>(таблица оплат)"| o_zakrytie_zakupki
  o_zakrytie_zakupki -->|"Закрытая задача<br/>«Закупка» — логисту"| o_kontrol_postavki
  o_prinyatie_zakupki --> o_papka_zakupki
  o_papka_zakupki --> o_povtornaya_rassylka
  o_povtornaya_rassylka --> o_kontrol_vybora
  o_vybor_postavshchika --> o_proverka_kontragenta
  o_proverka_kontragenta --> o_postanovka_teh_soglasovaniya
  o_teh_soglasovanie --> o_reshenie_sdelka
  o_reshenie_sdelka --> o_dogovor_postavki
  o_dogovor_postavki --> o_poluchenie_schetov
  o_poluchenie_schetov --> o_vedenie_sdelok
  o_vedenie_sdelok --> o_postanovka_teh_soglasovaniya
  o_postanovka_teh_soglasovaniya --> o_soglasovanie_dokumentov
  o_soglasovanie_dokumentov --> o_v_oplatu
  o_v_oplatu --> o_postanovka_oplaty
  o_proverka_schetov --> o_uchet_1s
  o_uchet_1s --> o_peredacha_na_oplatu
  o_arhiv_oplat --> o_tablitsa_oplat
```

## Шаги и обязанности

| № | Шаг | Делает | Ставит → принимает | Передаёт | Согласуют, помогают, узнают | Где |
|---|---|---|---|---|---|---|
| 0 | Вход в процесс- Поставлена задача на закупку по проекту. №Проекта -Закзачик-предмет: Закупить товары" (или принятие этой задачи?!) | [Принимающий задачу на закупку](../../reg/oby/prinyatie-zakupki.md) | [Ставящий задачу на закупку](../../reg/oby/postanovka-zakupki.md) → — |  |  | [Битрикс24: задачи по шаблонам](../../reg/mes.md#bitriks-zadacha) |
| 1 | Создание в папке "...Рабочие документы" подпапки "Закупки" | [Ведущий папку закупки](../../reg/oby/papka-zakupki.md) | — → — |  |  | [Диск: «Рабочие документы» → «Закупки»](../../reg/mes.md#disk-zakupki) |
| 2 | Создание в папке "... Закупки" подпапок "Счета", "Договоры" и "В оплату" | [Ведущий папку закупки](../../reg/oby/papka-zakupki.md) | — → — |  |  | [Диск: «Рабочие документы» → «Закупки»](../../reg/mes.md#disk-zakupki), [Битрикс24: статус проекта](../../reg/mes.md#bitriks-status-proekta) |
| 3 | Повторная рассылка и заполнение внешней таблицы | [Рассылающий повторные запросы](../../reg/oby/povtornaya-rassylka.md) | — → — | [Предложения поставщиков (листы 5-1, 5-2)](../../reg/art.md#predlozheniya-5-1) |  | [Лист «5-2 Запросы КП Закупки»](../../reg/mes.md#lis-5-2), [Лист «5-1 Сбор КП Закупки»](../../reg/mes.md#lis-5-1), [Почта](../../reg/mes.md#pochta) |
| 4 | Отслеживание комментариев по итогу общения с выбранными поставщиками на листе "5 Закупка товара". | [Отслеживающий выбор поставщиков](../../reg/oby/kontrol-vybora.md) | — → — |  | отслеживает: [Готовящий выбор поставщика](../../reg/oby/vybor-postavshchika.md) | [Лист «5-3 Выбор поставщиков Закупки»](../../reg/mes.md#lis-5-3) |
| 5 | Отслеживания результатов повторной рассылки на листе "3-3 Выбор поставщиков" В случае необходимости замены поставщиков, принятие решения по такой замене. | [Отслеживающий выбор поставщиков](../../reg/oby/kontrol-vybora.md) | — → — | [Решения по выбору поставщиков (лист 5-3)](../../reg/art.md#vybor-5-3) |  | [Лист «5-3 Выбор поставщиков Закупки»](../../reg/mes.md#lis-5-3) |
| 6 | Определение предложений с лучшими условиями и подготовка предложения по Окончательному выбору поставщика. | [Готовящий выбор поставщика](../../reg/oby/vybor-postavshchika.md) | — → — |  |  | [Лист «5-3 Выбор поставщиков Закупки»](../../reg/mes.md#lis-5-3), [Почта](../../reg/mes.md#pochta) |
| 7 | Проверка выбранных поставщиков на добросовестность | [Проверяющий контрагента](../../reg/oby/proverka-kontragenta.md) | — → — |  |  | [Таблица проверки контрагентов](../../reg/mes.md#tablitsa-kontragentov), [Лист «Отзывы о поставщиках»](../../reg/mes.md#lis-otzyvy) |
| 8 | Постановка задачи на проверку выбранных предложений ТС | [Ставящий задачи на техническое согласование](../../reg/oby/postanovka-teh-soglasovaniya.md) | — → [Согласующий техническую часть](../../reg/oby/teh-soglasovanie.md) | [Подзадача ТС на проверку предложений](../../reg/art.md#podzadacha-ts) |  | [Битрикс24: задачи по шаблонам](../../reg/mes.md#bitriks-zadacha) |
| 9 | Рассмотрение предложений поставщиков в технической части<br/>*Регламент: «как эти заключения отражаются в таблице, если не попадают на 3-2?».* | [Согласующий техническую часть](../../reg/oby/teh-soglasovanie.md) | [Ставящий задачи на техническое согласование](../../reg/oby/postanovka-teh-soglasovaniya.md) → [Ставящий задачи на техническое согласование](../../reg/oby/postanovka-teh-soglasovaniya.md) | [Заключение ТС по предложениям](../../reg/art.md#zaklyuchenie-ts) |  | [Битрикс24: задачи по шаблонам](../../reg/mes.md#bitriks-zadacha) |
| 10 | Решение о заключении сделки с выбранным поставщиком | [Решающий о сделке с поставщиком](../../reg/oby/reshenie-sdelka.md) | — → — | [Решение о сделке с поставщиком](../../reg/art.md#reshenie-sdelka) | согласуют: [Согласующий финансирование сделки](../../reg/oby/soglasovanie-finansirovaniya.md) |  |
| 11 | Подготовка договора поставки с поставщиком | [Готовящий договор поставки](../../reg/oby/dogovor-postavki.md) | — → — |  | помогают: [Хранитель учёта и документов (столбец K)](../../reg/rol/khranitel.md) | [Диск: «Рабочие документы» → «Закупки»](../../reg/mes.md#disk-zakupki) |
| 12 | Получение подписанных договоров или оформленных по нашим требованиям счетов от выбранных Поставщиков | [Добывающий счета и договоры](../../reg/oby/poluchenie-schetov.md) | — → — | [Счета и договоры поставщиков](../../reg/art.md#scheta-dogovory) |  | [Почта](../../reg/mes.md#pochta), [Диск: «Рабочие документы» → «Закупки»](../../reg/mes.md#disk-zakupki) |
| 13 | Ведение Листа 5 (Таблица закупки внешняя) ( 5-4 в будущем) | [Ведущий лист оформления сделок](../../reg/oby/vedenie-sdelok.md) | — → — |  |  | [Лист «5-5 Оформление сделок»](../../reg/mes.md#lis-5-5) |
| 14 | Постановка Задачи на согласование счетов/договоров в технической части | [Ставящий задачи на техническое согласование](../../reg/oby/postanovka-teh-soglasovaniya.md) | — → [Согласующий техническую часть](../../reg/oby/teh-soglasovanie.md) |  |  | [Битрикс24: задачи по шаблонам](../../reg/mes.md#bitriks-zadacha) |
| 15 | Рассмотрение и согласование счетов и договоров и других документов в технической части (в том числе путем подготовки ТЗ для договора с поставщиком) | [Проводящий согласование документов сделки](../../reg/oby/soglasovanie-dokumentov.md) | — → — |  | согласуют: [Согласующий техническую часть](../../reg/oby/teh-soglasovanie.md), [Согласующий сделку и отклонения](../../reg/oby/soglasovanie-otkloneniy.md), [Согласующий финансирование сделки](../../reg/oby/soglasovanie-finansirovaniya.md) | [Битрикс24: задачи по шаблонам](../../reg/mes.md#bitriks-zadacha), [Диск: «Рабочие документы» → «Закупки»](../../reg/mes.md#disk-zakupki) |
| 16 | Размещение в папке "в оплату" согласованных с ТС счетов и договоров для оплаты | [Передающий согласованное в оплату](../../reg/oby/v-oplatu.md) | — → — | [Счета и договоры «готов к оплате»](../../reg/art.md#scheta-v-oplatu) |  | [Диск: «Рабочие документы» → «Закупки»](../../reg/mes.md#disk-zakupki), [Лист «5-5 Оформление сделок»](../../reg/mes.md#lis-5-5) |
| 17 | Постановка Задачи K на проверку и оплату счетов и договоров, созданию в 1с Заказа покупателя и заказов поставщикам | [Ставящий задачу на оплату](../../reg/oby/postanovka-oplaty.md) | — → [Проверяющий счета перед оплатой](../../reg/oby/proverka-schetov.md) | [Задача «Оплатить счета»](../../reg/art.md#zadacha-oplatit) |  | [Битрикс24: задачи по шаблонам](../../reg/mes.md#bitriks-zadacha) |
| 18 | Информирование в задаче K о том, что размещены новые Счета и договора | [Ставящий задачу на оплату](../../reg/oby/postanovka-oplaty.md) | — → — | [Задача «Оплатить счета»](../../reg/art.md#zadacha-oplatit), [Счета и договоры «готов к оплате»](../../reg/art.md#scheta-v-oplatu) | узнают о результате: [Менеджер проекта](../../reg/rol/proekt.md) | [Битрикс24: задачи по шаблонам](../../reg/mes.md#bitriks-zadacha) |
| 19 | Проверка готовых к оплате счетов и договоров | [Проверяющий счета перед оплатой](../../reg/oby/proverka-schetov.md) | [Ставящий задачу на оплату](../../reg/oby/postanovka-oplaty.md) → — |  |  | [Диск: «Рабочие документы» → «Закупки»](../../reg/mes.md#disk-zakupki) |
| 20 | Создание заказа покупателя и поставщикам в 1с | [Ведущий учёт в 1С](../../reg/oby/uchet-1s.md) | [Ставящий задачу на оплату](../../reg/oby/postanovka-oplaty.md) → — |  |  | [1С](../../reg/mes.md#1s) |
| 21 | Передача полученных счетов M на оплату | [Передающий счета на оплату](../../reg/oby/peredacha-na-oplatu.md) | — → [Оплачивающий счета](../../reg/oby/oplata.md) | [Проверенные счета на оплату](../../reg/art.md#scheta-na-oplatu) |  |  |
| 22 | Оплата полученных счетов и передача платежных поручений K | [Оплачивающий счета](../../reg/oby/oplata.md) | [Передающий счета на оплату](../../reg/oby/peredacha-na-oplatu.md) → [Раскладывающий оплаченное](../../reg/oby/arhiv-oplat.md) | [Платёжные поручения](../../reg/art.md#platezhki) |  |  |
| 23 | Создание в папке ".... В оплату" подпапки "Оплачено" и перемещение в нее всех оплаченных счетов и договоров. Создание папки "Платежные поручения" и перемещение в нее всех Платежных поручений по оплаченным счетам и договорам | [Раскладывающий оплаченное](../../reg/oby/arhiv-oplat.md) | — → — |  |  | [Диск: «Рабочие документы» → «Закупки»](../../reg/mes.md#disk-zakupki) |
| 24 | Внесение в Таблицу Оплат сведений о произведенных оплатах по проекту<br/>*Директор: задачу по оплате у K принимает сотрудник контура 2.* | [Ведущий таблицу оплат](../../reg/oby/tablitsa-oplat.md) | — → [Закрывающий закупку](../../reg/oby/zakrytie-zakupki.md) | [Сведения об оплатах (таблица оплат)](../../reg/art.md#oplaty-v-tablitse) |  | [Внешняя таблица оплат](../../reg/mes.md#tablitsa-oplat), [Лист «6 Оплаты»](../../reg/mes.md#lis-6-oplaty) |
| 25 | Закрытие этапа Закупки<br/>*Директор: задачу по закупке у сотрудника контура 2 принимает логист.* | [Закрывающий закупку](../../reg/oby/zakrytie-zakupki.md) | — → [Отслеживающий поставку](../../reg/oby/kontrol-postavki.md) | [Закрытая задача «Закупка» — логисту](../../reg/art.md#zadacha-zakupka-zakryta) | помогают: [Менеджер проекта](../../reg/rol/proekt.md) | [Битрикс24: задачи по шаблонам](../../reg/mes.md#bitriks-zadacha), [Битрикс24: статус проекта](../../reg/mes.md#bitriks-status-proekta) |

## Где работают

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  o_prinyatie_zakupki("Принимающий задачу на<br/>закупку")
  o_papka_zakupki("Ведущий папку закупки")
  o_povtornaya_rassylka("Рассылающий повторные<br/>запросы")
  o_kontrol_vybora("Отслеживающий выбор<br/>поставщиков")
  o_vybor_postavshchika("Готовящий выбор поставщика")
  o_proverka_kontragenta("Проверяющий контрагента")
  o_postanovka_teh_soglasovaniya("Ставящий задачи на<br/>техническое согласование")
  o_teh_soglasovanie("Согласующий техническую<br/>часть")
  o_dogovor_postavki("Готовящий договор поставки")
  o_poluchenie_schetov("Добывающий счета и<br/>договоры")
  o_vedenie_sdelok("Ведущий лист оформления<br/>сделок")
  o_soglasovanie_dokumentov("Проводящий согласование<br/>документов сделки")
  o_v_oplatu("Передающий согласованное в<br/>оплату")
  o_postanovka_oplaty("Ставящий задачу на оплату")
  o_proverka_schetov("Проверяющий счета перед<br/>оплатой")
  o_uchet_1s("Ведущий учёт в 1С")
  o_arhiv_oplat("Раскладывающий оплаченное")
  o_tablitsa_oplat("Ведущий таблицу оплат")
  o_zakrytie_zakupki("Закрывающий закупку")
  subgraph v________["битрикс"]
    m_bitriks_zadacha{{"Битрикс24: задачи по<br/>шаблонам"}}
    m_bitriks_status_proekta{{"Битрикс24: статус проекта"}}
  end
  subgraph v_____["диск"]
    m_disk_zakupki[["Диск: «Рабочие документы»<br/>→ «Закупки»"]]
  end
  subgraph v_____["лист"]
    m_lis_5_2[/"Лист «5-2 Запросы КП<br/>Закупки»"/]
    m_lis_5_1[/"Лист «5-1 Сбор КП Закупки»"/]
    m_lis_5_3[/"Лист «5-3 Выбор<br/>поставщиков Закупки»"/]
    m_lis_otzyvy[/"Лист «Отзывы о<br/>поставщиках»"/]
    m_lis_5_5[/"Лист «5-5 Оформление<br/>сделок»"/]
    m_lis_6_oplaty[/"Лист «6 Оплаты»"/]
  end
  subgraph v______["почта"]
    m_pochta>"Почта"]
  end
  subgraph v________["таблица"]
    m_tablitsa_kontragentov[/"Таблица проверки<br/>контрагентов"/]
    m_tablitsa_oplat[/"Внешняя таблица оплат"/]
  end
  subgraph v_1_["1с"]
    m_1s[("1С")]
  end
  o_prinyatie_zakupki --> m_bitriks_zadacha
  o_papka_zakupki --> m_disk_zakupki
  o_papka_zakupki --> m_bitriks_status_proekta
  o_povtornaya_rassylka --> m_lis_5_2
  o_povtornaya_rassylka --> m_lis_5_1
  o_povtornaya_rassylka --> m_pochta
  o_kontrol_vybora --> m_lis_5_3
  o_vybor_postavshchika --> m_lis_5_3
  o_vybor_postavshchika --> m_pochta
  o_proverka_kontragenta --> m_tablitsa_kontragentov
  o_proverka_kontragenta --> m_lis_otzyvy
  o_postanovka_teh_soglasovaniya --> m_bitriks_zadacha
  o_teh_soglasovanie --> m_bitriks_zadacha
  o_dogovor_postavki --> m_disk_zakupki
  o_poluchenie_schetov --> m_pochta
  o_poluchenie_schetov --> m_disk_zakupki
  o_vedenie_sdelok --> m_lis_5_5
  o_soglasovanie_dokumentov --> m_bitriks_zadacha
  o_soglasovanie_dokumentov --> m_disk_zakupki
  o_v_oplatu --> m_disk_zakupki
  o_v_oplatu --> m_lis_5_5
  o_postanovka_oplaty --> m_bitriks_zadacha
  o_proverka_schetov --> m_disk_zakupki
  o_uchet_1s --> m_1s
  o_arhiv_oplat --> m_disk_zakupki
  o_tablitsa_oplat --> m_tablitsa_oplat
  o_tablitsa_oplat --> m_lis_6_oplaty
  o_zakrytie_zakupki --> m_bitriks_zadacha
  o_zakrytie_zakupki --> m_bitriks_status_proekta
```

## Статусы

**Статус проекта**

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
stateDiagram-v2
  direction LR
  state "Исполнение: Закупаем товары" as st0
  state "Исполняем договор" as st1
  [*] --> st0
  st0 --> st1 : закупка товара 25
```

**Статус сделки**

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
stateDiagram-v2
  direction LR
  state "Готово к оплате" as st0
  state "Оплачено" as st1
  [*] --> st0
  st0 --> st1 : закупка товара 22
```

Дальше: [Процесс. Поступление: контроль поставки, доплаты, доставка, приёмка](../r06-postuplenie/index.md).
