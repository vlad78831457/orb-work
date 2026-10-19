# orb-work. Проверка и сборка идут прямо на стенде: нужны sh, git, python3 и PyYAML.
.PHONY: help test test-docker inst full docx mermaid mermaid-setup reglament reglament-xlsx

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

mermaid: ## проверить схемы Mermaid в inst/md-out настоящим mermaid-cli (по желанию; новые и изменённые)
	taskset -c 0 python3 tools/mermaid.py

mermaid-setup: ## поставить mermaid-cli в .tools/ (нужны nodejs и npm в системе)
	mkdir -p .tools; [ -f .tools/package.json ] || echo '{"private":true}' > .tools/package.json
	cd .tools && PUPPETEER_CACHE_DIR=$(CURDIR)/.tools/puppeteer taskset -c 0 npm install --no-audit --no-fund @mermaid-js/mermaid-cli@11.4.2

reglament: ## пересобрать pro/*/reglament.yaml из регламента: make reglament X=raw/…/Распределение задач….xlsx
	taskset -c 0 python3 inst/src/skripty/import_reglament.py "$(X)"

reglament-xlsx: ## книга регламента для Google Таблиц из репозитория: make reglament-xlsx [OUT=raw/…/….xlsx] (нужен python3-openpyxl)
	taskset -c 0 python3 inst/src/skripty/reglament_xlsx.py --out "$(or $(OUT),raw/$(shell date +%F)-reglament/Регламент — обязанности и шаги $(shell date +%F).xlsx)"
