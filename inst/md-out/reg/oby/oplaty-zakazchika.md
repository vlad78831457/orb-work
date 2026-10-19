# Отслеживающий оплаты заказчика

Следит за сроками оплаты по проекту, учитывает поступления от заказчиков, поставщиков и страховых, вносит платежи в систему.

- **Обязанность:** одна, один ответственный. Ключ: `oplaty-zakazchika`
- **Предполагаем, что выполняет:** [Хранитель учёта и документов (столбец K)](../../reg/rol/khranitel.md)
- **Контур:** 3
- **Почему выделили:** Регламент: шаги 31–33 — столбец K.
- **Догадка, не подтверждено:** «Прописать инструмент» и «что тут писать?» — инструмента пока нет.
- *Черновик — проверить.*

## Откуда задача и кому результат

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  o_oplaty_zakazchika("Отслеживающий оплаты<br/>заказчика")
  style o_oplaty_zakazchika stroke-width:3px
  o_pretenziya_neuplata("Пишущий претензию о<br/>неуплате")
  o_oplaty_zakazchika -->|передаёт| o_pretenziya_neuplata
```

## Шаги

| Процесс | № | Шаг | Здесь |
|---|---|---|---|
| [Процесс. Контроль исполнения заказчиком](../../pro/r11-kontrol-zakazchika/index.md) | 31 | Отслеживание сроков оплаты по проекту, | делает |
| [Процесс. Контроль исполнения заказчиком](../../pro/r11-kontrol-zakazchika/index.md) | 32 | Отслеживание и учет оплат от заказчиков и поступлений (типа денег от поставщиков и страховых) по проекту | делает |
| [Процесс. Контроль исполнения заказчиком](../../pro/r11-kontrol-zakazchika/index.md) | 33 | Занесение информации о платежах в систему | делает |

**Где работает:** [1С](../../reg/mes.md#1s)
