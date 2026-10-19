# Принимающий этапы

Принимает закрытые задачи этапов у исполнителей.

- **Обязанность:** одна, один ответственный. Ключ: `priemka-etapov`
- **Предполагаем, что выполняет:** [Координатор](../../reg/rol/koordinator.md)
- **Контур:** 0
- **Почему выделили:** «Менеджеру принять задачу по заключению договора у Координатора» — кто-то принимает результат этапа.
- **Догадка, не подтверждено:** Шага с исполнителем «Координатор» в регламенте нет — обязанность выведена из текста.
- *Черновик — проверить.*

## Откуда задача и кому результат

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "16px", "primaryColor": "#e8f0fe", "primaryTextColor": "#111827", "primaryBorderColor": "#4b5563", "lineColor": "#2563eb", "textColor": "#111827", "clusterBkg": "#fffbe6", "clusterBorder": "#9ca3af", "edgeLabelBackground": "#ffffff", "signalColor": "#2563eb", "signalTextColor": "#1d4ed8", "noteBkgColor": "#fff3b0", "noteTextColor": "#111827", "noteBorderColor": "#a16207", "actorBkg": "#e8f0fe", "actorTextColor": "#111827", "actorBorder": "#4b5563", "actorLineColor": "#9ca3af", "labelBoxBkgColor": "#e8f0fe", "labelTextColor": "#111827"}}}%%
flowchart LR
  o_priemka_etapov("Принимающий этапы")
  style o_priemka_etapov stroke-width:3px
  o_zakrytie_kontraktatsii("Закрывающий контрактацию")
  o_zakrytie_kontraktatsii -->|ставит| o_priemka_etapov
```

## Шаги

| Процесс | № | Шаг | Здесь |
|---|---|---|---|
| [Процесс. Контрактация](../../pro/r02-kontraktatsiya/index.md) | 20 | Приемка этапа Контрактации | принимает результат |
