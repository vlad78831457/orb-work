# Координатор

Контур 0: ставит и принимает задачи этапов (например, задачу на заключение договора).

- **Контур:** 0
- **Источник:** регламент; ответы
- **Почему выделили:** В регламенте «принять задачу у Координатора» (Контрактация 20) и «передача на регистрацию Координатору» (Несоответствия 17). Директор (раунд 2, №7): это не столбец K, а кто-то из контура 0.
- **Догадка, не подтверждено:** Столбца в регламенте нет; что ещё делает — не сказано.

## Обязанности, которые мы ей приписываем

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  r_koordinator(["Координатор"])
  subgraph k_0["контур 0"]
    o_priemka_etapov("Принимающий этапы")
  end
  r_koordinator --> o_priemka_etapov
```

- [Принимающий этапы](../../reg/oby/priemka-etapov.md) — Принимает закрытые задачи этапов у исполнителей.

## С кем работает

Сколько раз работа переходит от должности к должности (ставит задачу, передаёт результат, следующий шаг) — по всем процессам.

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  r_prodazhi(["Менеджер по продажам"])
  r_koordinator(["Координатор"])
  style r_koordinator stroke-width:3px
  r_prodazhi -->|1| r_koordinator
```

