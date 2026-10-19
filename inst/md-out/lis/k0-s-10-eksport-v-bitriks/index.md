# Лист «S-10 Экспорт в Битрикс»

Таблица: таблица проекта · контур 0.

**Зачем** (со слов директора): собирает данные для выгрузки в Битрикс24.

Устройство листа — заголовки, вид столбцов, списки, формулы, связи с другими листами — собрано из таблицы ниже.

## Зачем лист — подробно

*Заполнить:* что на листе происходит, откуда приходят данные и куда уходят.

## Как заполнять

*Заполнить:* какие столбцы вводят руками, какие считаются сами. Что значит каждый столбец — в `stolbtsy.yaml` рядом (поля `chto` и `kak`).

## Что нельзя трогать

*Заполнить.*

## Инструкции и умения

*Заполнить:* какие инструкции и умения относятся к листу.

## Осталось сделать

- Заполнить разделы выше и `stolbtsy.yaml`.

## Устройство (из таблицы)

- **Таблица:** таблица проекта, лист «S-10 Экспорт в Битрикс»; контур 0
- **Размер:** `A1:J60`, закреплено до `A11`
- **Каркас:** общий — служебные строки, заголовки в строке 10 ([что значат служебные строки](../../zna/lis-sluzhebnye-stroki/index.md))
- **Формул:** 48; заполненных ячеек без формул в данных: 75; списков: 1; условного форматирования: 0; объединённых ячеек: 0

## Связи с другими листами

- **Берёт данные с листов:** [S-10 Конвейер Запросов КП](../k1-s-10-konveyer-zaprosov-kp/index.md) (25), [2-2 Проблемы по проекту](../k1-2-2-problemy-po-proektu/index.md) (20), [2-1 Вопросы от Поставщиков](../k1-2-1-voprosy-ot-postavshchikov/index.md) (20), [3-2 Экспертиза предложений](../k1-3-2-ekspertiza-predlozheniy/index.md) (17), [1-1 Сбор КП](../k1-1-1-sbor-kp/index.md) (11), [Настройки писем](../k0-nastroyki-pisem/index.md) (10), [4-1 Расчет рентабельности КП](../k1-4-1-raschet-rentabelnosti-kp/index.md) (8), [3-3 Выбор поставщиков](../k1-3-3-vybor-postavshchikov/index.md) (7), [S-10 Справочник полей Битрикс](../k0-s-10-spravochnik-poley-bitriks/index.md) (6), [4-1 Расчет рентабельности КП в1](../k1-4-1-raschet-rentabelnosti-kp-v1/index.md) (2), [1-2 Запросы по товарным группам](../k1-1-2-zaprosy-po-tovarnym-gruppam/index.md) (2), [S-10 Новые предложения](../k1-s-10-novye-predlozheniya/index.md) (2)
- **Его данные используют:** [4-1 Расчет рентабельности КП](../k1-4-1-raschet-rentabelnosti-kp/index.md) (2)

В скобках и на стрелках — сколько формул ссылаются.

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  s_k0_s_10_eksport_v_bitriks["S-10 Экспорт в Битрикс"]
  style s_k0_s_10_eksport_v_bitriks stroke-width:3px
  s_k1_s_10_konveyer_zaprosov_kp["S-10 Конвейер Запросов<br/>КП"]
  s_k1_2_2_problemy_po_proektu["2-2 Проблемы по<br/>проекту"]
  s_k1_2_1_voprosy_ot_postavshchikov["2-1 Вопросы от<br/>Поставщиков"]
  s_k1_3_2_ekspertiza_predlozheniy["3-2 Экспертиза<br/>предложений"]
  s_k1_1_1_sbor_kp["1-1 Сбор КП"]
  s_k0_nastroyki_pisem["Настройки писем"]
  s_k1_4_1_raschet_rentabelnosti_kp["4-1 Расчет<br/>рентабельности КП"]
  s_k1_3_3_vybor_postavshchikov["3-3 Выбор поставщиков"]
  s_k0_s_10_spravochnik_poley_bitriks["S-10 Справочник полей<br/>Битрикс"]
  s_k1_4_1_raschet_rentabelnosti_kp_v1["4-1 Расчет<br/>рентабельности КП в1"]
  s_k1_1_2_zaprosy_po_tovarnym_gruppam["1-2 Запросы по<br/>товарным группам"]
  s_k1_s_10_novye_predlozheniya["S-10 Новые предложения"]
  s_k1_s_10_konveyer_zaprosov_kp -->|"25"| s_k0_s_10_eksport_v_bitriks
  s_k1_2_2_problemy_po_proektu -->|"20"| s_k0_s_10_eksport_v_bitriks
  s_k1_2_1_voprosy_ot_postavshchikov -->|"20"| s_k0_s_10_eksport_v_bitriks
  s_k1_3_2_ekspertiza_predlozheniy -->|"17"| s_k0_s_10_eksport_v_bitriks
  s_k1_1_1_sbor_kp -->|"11"| s_k0_s_10_eksport_v_bitriks
  s_k0_nastroyki_pisem -->|"10"| s_k0_s_10_eksport_v_bitriks
  s_k1_4_1_raschet_rentabelnosti_kp -->|"8"| s_k0_s_10_eksport_v_bitriks
  s_k1_3_3_vybor_postavshchikov -->|"7"| s_k0_s_10_eksport_v_bitriks
  s_k0_s_10_spravochnik_poley_bitriks -->|"6"| s_k0_s_10_eksport_v_bitriks
  s_k1_4_1_raschet_rentabelnosti_kp_v1 -->|"2"| s_k0_s_10_eksport_v_bitriks
  s_k1_1_2_zaprosy_po_tovarnym_gruppam -->|"2"| s_k0_s_10_eksport_v_bitriks
  s_k1_s_10_novye_predlozheniya -->|"2"| s_k0_s_10_eksport_v_bitriks
  s_k0_s_10_eksport_v_bitriks -->|"2"| s_k1_4_1_raschet_rentabelnosti_kp
```

## Столбцы

Устройство — из таблицы; «Что это» и «Как заполняют» — из `stolbtsy.yaml` (заполняем руками).

| Столбец | Заголовок | Служебное имя | Вид | Заполняется | Список | Что это | Как заполняют |
|---|---|---|---|---|---|---|---|
| A *(скрыт)* |  |  |  | руками? |  |  |  |
| B *(скрыт)* |  |  |  | руками? |  |  |  |
| C | Индификатор поля |  | formulaCell | формула |  |  |  |
| D | Экспортировать | needToSend |  | руками, из списка | "Нет,Да" |  |  |
| E | Номер | Номер |  | формула |  |  |  |
| F | Название | Название |  | руками? |  |  |  |
| G | Значение | Значение | formulaCell | формула |  |  |  |
| H |  |  |  | формула |  |  |  |

<details><summary>Формулы столбцов (3)</summary>

| Столбец | Строка | Формула |
|---|---|---|
| E | 11 | <code>=ROW()-10</code> |
| G | 11 | <code>=TEXTJOIN(CHAR(10),TRUE, IF('Настройки писем'!AF7&gt;0,"у "&amp;'Настройки писем'!AF7&amp;" из "&amp;'Настройки писем'!AF6&amp;" тов. нет цен",), IF('Настройки писем'!AF8&gt;0,"у "&amp;'Настройки писем'!AF8&amp;" из "&amp;'Настройки писем'!AF6&amp;" тов &lt; "&amp;'1-1 Сбор КП'!$B$8&amp;" предложен",), IF('Настройки писем'!AF7+'Настройки писем'!AF8=0,"У всех товаров достаточно предложений",), 'S-10 Экспорт в Битрикс'!G32,'S-10 Экспорт в Битрикс' …</code> |
| H | 24 | <code>= IFERROR(VLOOKUP(G24,{'S-10 Справочник полей Битрикс'!G:G,'S-10 Справочник полей Битрикс'!H:H},2,false), )</code> |

</details>
