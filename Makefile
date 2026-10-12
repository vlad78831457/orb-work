# orb-work. Проверки — в Docker.
.PHONY: help test inst full docx

help: ## список команд
	@grep -E '^[a-z-]+:.*## ' Makefile | sed 's/:.*## /\t/'

test: ## проверка репозитория (Docker)
	docker compose build -q test
	docker compose run --rm test

U := UID=$$(id -u) GID=$$(id -g)

inst: ## собрать инструкции из частей в inst/md-out (другая папка: make inst OUT=путь)
	mkdir -p $(or $(OUT),inst/md-out)
	docker compose build -q inst
	$(U) OUT=$(abspath $(or $(OUT),inst/md-out)) docker compose run --rm inst

full: ## собрать один полный md: make full F=raschet → inst/md-full-out (другая папка: OUT=путь)
	mkdir -p $(or $(OUT),inst/md-full-out)
	docker compose build -q inst
	$(U) OUT=$(abspath $(or $(OUT),inst/md-full-out)) docker compose run --rm inst --full $(F)

docx: ## вручную: старые тексты из raw/ в inst/docx/*.docx (Pandoc)
	mkdir -p inst/docx
	$(U) docker compose run --rm docx
