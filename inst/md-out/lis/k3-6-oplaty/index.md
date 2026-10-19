> Черновик: текст не проверен.

# Лист «6 Оплаты»

**Назначение**

*Не описано — см. вопросы ниже.*


Устройство листа — размер, столбцы, формулы, связи с другими листами — собрано из таблицы в конце страницы.

## Осталось сделать

**Вопросы**

1. Для чего этот лист и кто в нём работает?
2. Какие столбцы заполняет человек, а какие считаются сами?
3. Что на листе нельзя трогать?
4. Верен ли список столбцов выше — выгрузка была неполной?

## Устройство (из таблицы)

- **Таблица:** таблица проекта, лист «6 Оплаты»; контур 3
- **Размер:** `A1:CC310`
- **Каркас:** свой, не общий; строка заголовков — 1, угадана по закреплённой области — проверить
- **Формул:** 7; заполненных ячеек без формул в данных: 0; списков: 0; условного форматирования: 12; объединённых ячеек: 0
- **Данные из других таблиц (IMPORTRANGE):** 1

## Связи с другими листами

- **Берёт данные с листов:** [S-10 Для Внешней Оплаты](../k2-s-10-dlya-vneshney-oplaty/index.md) (1), [6 Оплаты Внешняя](../k3-vo-6-oplaty-vneshnyaya/index.md) (1)
- **Его данные используют:** [Настройки писем](../k0-nastroyki-pisem/index.md) (3), [S-10 Финансист сбор данных](../k0-s-10-finansist-sbor-dannykh/index.md) (1), [S-10 ОтчетыПроектов](../k0-s-10-otchetyproektov/index.md) (7), [S-10 Оформление сделок Выборка](../k2-s-10-oformlenie-sdelok-vyborka/index.md) (16)

В скобках и на стрелках — сколько формул ссылаются.

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  s_k3_6_oplaty["6 Оплаты"]
  style s_k3_6_oplaty stroke-width:3px
  s_k2_s_10_dlya_vneshney_oplaty["S-10 Для Внешней<br/>Оплаты"]
  s_k3_vo_6_oplaty_vneshnyaya["6 Оплаты Внешняя"]
  s_k0_nastroyki_pisem["Настройки писем"]
  s_k0_s_10_finansist_sbor_dannykh["S-10 Финансист сбор<br/>данных"]
  s_k0_s_10_otchetyproektov["S-10 ОтчетыПроектов"]
  s_k2_s_10_oformlenie_sdelok_vyborka["S-10 Оформление сделок<br/>Выборка"]
  s_k2_s_10_dlya_vneshney_oplaty -->|"1"| s_k3_6_oplaty
  s_k3_vo_6_oplaty_vneshnyaya -->|"1"| s_k3_6_oplaty
  s_k3_6_oplaty -->|"3"| s_k0_nastroyki_pisem
  s_k3_6_oplaty -->|"1"| s_k0_s_10_finansist_sbor_dannykh
  s_k3_6_oplaty -->|"7"| s_k0_s_10_otchetyproektov
  s_k3_6_oplaty -->|"16"| s_k2_s_10_oformlenie_sdelok_vyborka
```

## Кто здесь работает (по процессам)

Обязанности, у которых место работы — этот лист (из разбора регламента); должность — в карточке обязанности.

[Ведущий таблицу оплат](../../reg/oby/tablitsa-oplat.md)

## Столбцы

Устройство — из таблицы; «Что это» и «Как заполняют» — из `stolbtsy.yaml` (заполняем руками).

| Столбец | Заголовок | Служебное имя | Вид | Заполняется | Список | Что это | Как заполняют |
|---|---|---|---|---|---|---|---|
| A | #N/A |  |  | формула |  |  |  |
| G |  |  |  | формула |  |  |  |
| H |  |  |  | формула |  |  |  |
| I |  |  |  | формула |  |  |  |
| J |  |  |  | формула |  |  |  |
| K |  |  |  | формула |  |  |  |

<details><summary>Формулы столбцов (6)</summary>

| Столбец | Строка | Формула |
|---|---|---|
| A | 1 | <code>=IMPORTRANGE( 'S-10 Для Внешней Оплаты'!$F$6, "'6 Оплаты Внешняя'!A1:D")</code> |
| G | 1 | <code>=LAMBDA(theData,theUrl,theEmpty, IF(theUrl="", {theEmpty;{"","","","","Нет внешней таблицы оплат. ошибка"}},IF( ISERR(theData), {theEmpty;{"","","",theData,"&lt;&lt; Откройте доступ ошибка"};{"","","",theUrl,"&lt;&lt; Внешняя таблица оплат","")</code> |
| H | 10 | <code>="COMPUTED_VALUE"</code> |
| I | 10 | <code>="COMPUTED_VALUE"</code> |
| J | 10 | <code>="COMPUTED_VALUE"</code> |
| K | 10 | <code>="COMPUTED_VALUE"</code> |

</details>
