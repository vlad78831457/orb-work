# Отслеживающий поставку

Находит оплаченные товары без статуса, подтверждает у поставщиков получение денег и сроки, следит за просрочками.

- **Обязанность:** одна, один ответственный. Ключ: `kontrol-postavki`
- **Предполагаем, что выполняет:** [Логист](../../reg/rol/logist.md)
- **Контур:** 4
- **Почему выделили:** Регламент: шаги 2, 3, 6 — у АС (логист); работа в таблице логиста.
- *Черновик — проверить.*

## Откуда задача и кому результат

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  o_kontrol_postavki("Отслеживающий поставку")
  style o_kontrol_postavki stroke-width:3px
  o_zakrytie_zakupki("Закрывающий закупку")
  o_zakrytie_zakupki -->|ставит| o_kontrol_postavki
```

## Шаги

| Процесс | № | Шаг | Здесь |
|---|---|---|---|
| [Процесс. Закупка товара](../../pro/r04-zakupka-tovara/index.md) | 25 | Закрытие этапа Закупки | принимает результат |
| [Процесс. Поступление: контроль поставки, доплаты, доставка, приёмка](../../pro/r06-postuplenie/index.md) | 2 | Отслеживание товаров со статусом ОПЛАЧЕНО но пока без "статуса" (на листе Рабочий лист) | делает |
| [Процесс. Поступление: контроль поставки, доплаты, доставка, приёмка](../../pro/r06-postuplenie/index.md) | 3 | Контакт с поставщиками подтверждение получения денег, уточнение сроков поставки | делает |
| [Процесс. Поступление: контроль поставки, доплаты, доставка, приёмка](../../pro/r06-postuplenie/index.md) | 6 | Контроль соблюдения сроков поставки ( и выявление просрочки) | делает |

**Получает:** [Формат приёмки](../../reg/art.md#format-priemki), [Плановые сроки поставки](../../reg/art.md#plan-sroki)

**Отдаёт:** [Статусы поставки (таблица логиста)](../../reg/art.md#statusy-postavki), [Сведения о просрочке поставки](../../reg/art.md#prosrochka)

**Где работает:** [Таблица логиста](../../reg/mes.md#tablitsa-logista), [Почта](../../reg/mes.md#pochta)
