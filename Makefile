# orb-work. Проверка и сборка идут прямо на стенде: нужны sh, git, python3 и PyYAML.
.PHONY: help test test-docker inst full docx

SOBRAT := python3 inst/src/skripty/sobrat.py

help: ## список команд
	@grep -E '^[a-z-]+:.*## ' Makefile | sed 's/:.*## /\t/'

test: ## проверка репозитория
	sh tools/check.sh

test-docker: ## та же проверка в чистом окружении (Docker), по желанию
	docker compose build -q test
	docker compose run --rm test

inst: ## собрать инструкции из частей в inst/md-out (другая папка: make inst OUT=путь)
	$(SOBRAT) --out $(or $(OUT),inst/md-out)

full: ## собрать полный md: make full F=tio.tov-razdelenie → inst/md-full-out/tio/tov-razdelenie.md
	$(SOBRAT) --full $(F) --out $(or $(OUT),inst/md-full-out)

docx: ## вручную: полный документ в .docx (Pandoc в Docker): make docx F=tio.tov-razdelenie → inst/docx/tio/…
	$(SOBRAT) --full $(F) --out inst/md-full-out
	sh tools/docx.sh $(F)
