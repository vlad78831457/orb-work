# orb-work. Проверка и сборка идут прямо на стенде: нужны sh, git, python3 и PyYAML.
.PHONY: help test test-docker inst full docx mermaid mermaid-setup reglament reglament-xlsx listy podpisi clasp-setup clasp-login gas-pull gas-kopiya gas-push veb-push veb-zabrat agy-setup

SOBRAT := python3 inst/src/skripty/sobrat.py
DATE ?= $(shell date +%F)

help: ## список команд
	@grep -E '^[a-z-]+:.*## ' Makefile | sed 's/:.*## /\t/'

test: ## проверка репозитория
	sh tools/check.sh

test-docker: ## та же проверка в чистом окружении (Docker), по желанию
	docker compose build -q test
	docker compose run --rm test

inst: ## собрать инструкции из частей в inst/md-out (другая папка: make inst OUT=путь)
	$(SOBRAT) --out $(or $(OUT),inst/md-out)

full: ## собрать короткий и полный md: make full F=tio.skr-zapusk-triggerov → inst/md-full-out/tio/
	$(SOBRAT) --full $(F) --date $(DATE) --out $(or $(OUT),inst/md-full-out)

docx: ## вручную: короткий и полный .docx с датой: make docx F=tio.skr-zapusk-triggerov → inst/docx/tio/
	$(SOBRAT) --full $(F) --date $(DATE) --out inst/md-full-out
	sh tools/docx.sh $(F) $(DATE)

podpisi: ## редактор подписей на снимках: http://localhost:8765 (с ноутбука: ssh -L 8765:localhost:8765 ag12)
	python3 tools/podpisi/server.py

mermaid: ## проверить схемы Mermaid в inst/md-out настоящим mermaid-cli (по желанию; новые и изменённые)
	taskset -c 0 python3 tools/mermaid.py

clasp-setup: ## поставить clasp (Apps Script из командной строки) в .tools/clasp
	mkdir -p .tools/clasp && taskset -c 0 npm --prefix .tools/clasp install --no-audit --no-fund @google/clasp@3.4.1

clasp-login: ## вход в Google для clasp — делает директор сам
	sh tools/gas.sh login

gas-pull: ## скачать скрипты таблицы в raw/gas/NAME: make gas-pull ID=<scriptId> NAME=<имя>
	sh tools/gas.sh pull "$(ID)" "$(NAME)"

gas-kopiya: ## пометить raw/gas/NAME как копию для опытов (без этого push не пойдёт)
	sh tools/gas.sh kopiya "$(NAME)"

gas-push: ## записать raw/gas/NAME в копию: make gas-push NAME=<имя>
	sh tools/gas.sh push "$(NAME)"

veb-push: ## добавить вебхук tools/veb в копию raw/gas/NAME и записать: make veb-push NAME=<имя>
	sh tools/gas.sh veb "$(NAME)"

veb-zabrat: ## забрать JSON вебхука в raw/veb: make veb-zabrat IMYA=proekta [LIST="лист"]
	IMYA="$(IMYA)" LIST="$(LIST)" python3 tools/veb/zabrat.py

agy-setup: ## поставить Antigravity CLI (agy) в .tools/agy, со сверкой контрольной суммы
	sh tools/agy-setup.sh

mermaid-setup: ## поставить mermaid-cli в .tools/ (нужны nodejs и npm в системе)
	mkdir -p .tools; [ -f .tools/package.json ] || echo '{"private":true}' > .tools/package.json
	cd .tools && PUPPETEER_CACHE_DIR=$(CURDIR)/.tools/puppeteer taskset -c 0 npm install --no-audit --no-fund @mermaid-js/mermaid-cli@11.4.2

reglament: ## пересобрать pro/*/reglament.yaml из регламента: make reglament X=raw/…/Распределение задач….xlsx
	taskset -c 0 python3 inst/src/skripty/import_reglament.py "$(X)"

reglament-xlsx: ## книга регламента для Google Таблиц из репозитория: make reglament-xlsx [OUT=raw/…/….xlsx] (нужен python3-openpyxl)
	taskset -c 0 python3 inst/src/skripty/reglament_xlsx.py --out "$(or $(OUT),raw/$(shell date +%F)-reglament/Регламент — обязанности и шаги $(shell date +%F).xlsx)"

LISTY_P ?= $(shell find raw -name '*Чистая таблица*.xlsx' 2>/dev/null | sort | tail -n 1)
LISTY_O ?= $(shell find raw -name '*ТАБЛИЦА ОПЛАТ*.xlsx' 2>/dev/null | sort | tail -n 1)
listy: ## устройство листов обеих таблиц → lis/*/struktura.yaml и заготовки (make listy [LISTY_P=… LISTY_O=…])
	taskset -c 0 python3 inst/src/skripty/import_listy.py --zagotovki proekta="$(LISTY_P)" oplat="$(LISTY_O)"
