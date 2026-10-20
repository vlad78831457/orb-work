# Лист «Технический лист»

Таблица: внешняя таблица оплат · контур 3.

**Зачем:** сведений нет — по названию лист можно сравнить с регламентом, это позже (ответ директора, раунд 5).

Устройство листа — заголовки, вид столбцов, списки, формулы, связи с другими листами — собрано из таблицы ниже. Строка заголовков на этом листе угадана по закреплённой области — проверить.

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

- **Таблица:** внешняя таблица оплат, лист «Технический лист»; контур 3
- **Размер:** `A1:R698`, закреплено до `A11`
- **Каркас:** свой, не общий; строка заголовков — 10, угадана по закреплённой области — проверить
- **Формул:** 1; заполненных ячеек без формул в данных: 7; списков: 0; условного форматирования: 0; объединённых ячеек: 0

## Связи с другими листами

- **Его данные используют:** [6 Оплаты Внешняя](../k3-vo-6-oplaty-vneshnyaya/index.md) (1), [7 Проверки Документов](../k3-vo-7-proverki-dokumentov/index.md) (2), [Сводная Прочее](../k3-vo-svodnaya-prochee/index.md) (2)

В скобках и на стрелках — сколько формул ссылаются.

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  s_k3_vo_tekhnicheskiy_list["Технический лист"]
  style s_k3_vo_tekhnicheskiy_list stroke-width:3px
  s_k3_vo_6_oplaty_vneshnyaya["6 Оплаты Внешняя"]
  s_k3_vo_7_proverki_dokumentov["7 Проверки Документов"]
  s_k3_vo_svodnaya_prochee["Сводная Прочее"]
  s_k3_vo_tekhnicheskiy_list -->|"1"| s_k3_vo_6_oplaty_vneshnyaya
  s_k3_vo_tekhnicheskiy_list -->|"2"| s_k3_vo_7_proverki_dokumentov
  s_k3_vo_tekhnicheskiy_list -->|"2"| s_k3_vo_svodnaya_prochee
```
