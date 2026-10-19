# Пишущий претензию о неуплате

Пишет претензию заказчику о неуплате, согласует с менеджером.

- **Обязанность:** одна, один ответственный. Ключ: `pretenziya-neuplata`
- **Предполагаем, что выполняет:** [Хранитель учёта и документов (столбец K)](../../reg/rol/khranitel.md)
- **Контур:** 3
- **Почему выделили:** Регламент: шаг 34 — столбец K.
- *Черновик — проверить.*

## Откуда задача и кому результат

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  o_pretenziya_neuplata("Пишущий претензию о<br/>неуплате")
  style o_pretenziya_neuplata stroke-width:3px
  o_oplaty_zakazchika("Отслеживающий оплаты<br/>заказчика")
  o_otpravka_pretenzii("Отправляющий претензию<br/>заказчику")
  o_oplaty_zakazchika -->|ставит| o_pretenziya_neuplata
  o_pretenziya_neuplata -->|передаёт| o_otpravka_pretenzii
```

## Шаги

| Процесс | № | Шаг | Здесь |
|---|---|---|---|
| [Процесс. Контроль исполнения заказчиком](../../pro/r11-kontrol-zakazchika/index.md) | 31 | Отслеживание сроков оплаты по проекту, | принимает результат |
| [Процесс. Контроль исполнения заказчиком](../../pro/r11-kontrol-zakazchika/index.md) | 34 | Написание претензии о неуплате | делает |

**Отдаёт:** [Претензия о неуплате](../../reg/art.md#pretenziya-neuplata)
