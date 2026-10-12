# Рабочий контур на стенде ag12

Вся работа по `orb-work` идёт на стенде `ag12`, отдельно от штаба: свой агент, свой доступ к GitHub только к этому проекту,
свой учёт времени (Monitask). Решение директора от 2026-10-12.

## Что уже стоит на ag12 (поставил агент штаба 2026-10-12)

- Docker, `gh`, Claude Code, `git`, `make`, `tmux`.
- Копия репозитория — `~/pr/orb-work`, ветка `main`; адрес GitHub записан, но доступа ещё нет.
- Исходная папка директора `~/orb-work` не тронута.

## Что сделать директору — один раз

1. **Токен GitHub только для этого проекта.** GitHub → Settings → Developer settings → Fine-grained tokens → Generate new token.
   Repository access — *Only select repositories*: `orb-work` и `orb-sheet`. Permissions — *Contents*: Read and write; *Pull requests*: Read and write.
   Срок — на выбор; когда истечёт, повторить шаги 1–2.
2. **Вход на стенде.** `ssh ag12`, затем:

   ```
   gh auth login --hostname github.com --git-protocol https
   ```

   выбрать *Paste an authentication token* и вставить токен. Затем `gh auth setup-git`.
   Проверка: `cd ~/pr/orb-work && git pull && gh pr list`.
3. **Claude Code.** `cd ~/pr/orb-work && claude`, войти в свою учётку. Контекст агент возьмёт сам из `CLAUDE.md`.

Токен, а не ключ SSH: он ограничен двумя репозиториями. Если стенд потерян или токен утёк — отозвать его на GitHub, остальные проекты не задеты.

## Как работать

```
ssh ag12            # или из VS Code: evo-code 12 /home/ag/pr/orb-work
tmux new -A -s work
cd ~/pr/orb-work && claude
```

- Monitask считает время на рабочем месте; всё, что по `orb-work`, делается в этом окне.
- PR появляются в <https://github.com/vlad78831457/orb-work/pulls>; вливает директор.
- Собранные инструкции — `~/pr/orb-work/inst/dist/*.docx`; забрать на рабочее место: `scp 'ag12:pr/orb-work/inst/dist/*.docx' .`

## Чего здесь нет

- Штаба `evo` и других проектов: агент контура о них не знает и доступа к ним не имеет.
- Памяти агента штаба: контекст контура — `CLAUDE.md`, `STATUS.md`, `GOALS.md` и история PR.
- Доступа к рабочим таблицам Google. Чтобы агент их увидел, директор кладёт выгрузки в `raw/` (вопрос 1 в `GOALS.md`).
