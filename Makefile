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

full: ## собрать один полный md: make full F=raschet → inst/md-full-out (другая папка: OUT=путь)
	$(SOBRAT) --full $(F) --out $(or $(OUT),inst/md-full-out)

docx: ## вручную: старые тексты из raw/ в inst/docx/*.docx (Pandoc в Docker)
	mkdir -p inst/docx
	UID=$$(id -u) GID=$$(id -g) docker compose run --rm docx
