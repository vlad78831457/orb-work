# Отправляющий претензию заказчику

Отправляет заказчику претензию о неуплате.

- **Обязанность:** одна, один ответственный. Ключ: `otpravka-pretenzii`
- **Предполагаем, что выполняет:** [Логист](../../reg/rol/logist.md)
- **Контур:** 3
- **Почему выделили:** Регламент: шаг 35 — у АС (логист).
- *Черновик — проверить.*

## Откуда задача и кому результат

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  o_otpravka_pretenzii("Отправляющий претензию<br/>заказчику")
  style o_otpravka_pretenzii stroke-width:3px
  o_pretenziya_neuplata("Пишущий претензию о<br/>неуплате")
  o_pretenziya_neuplata -->|ставит| o_otpravka_pretenzii
```

## Шаги

| Процесс | № | Шаг | Здесь |
|---|---|---|---|
| [Процесс. Контроль исполнения заказчиком](../../pro/r11-kontrol-zakazchika/index.md) | 34 | Написание претензии о неуплате | принимает результат |
| [Процесс. Контроль исполнения заказчиком](../../pro/r11-kontrol-zakazchika/index.md) | 35 | Отправка претензии Заказчику о неуплате | делает |

**Получает:** [Претензия о неуплате](../../reg/art.md#pretenziya-neuplata)

**Отдаёт:** [Претензия о неуплате](../../reg/art.md#pretenziya-neuplata)

**Где работает:** [Почта](../../reg/mes.md#pochta), [Транспортная компания](../../reg/mes.md#transportnaya-kompaniya)
