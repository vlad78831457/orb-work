# orb-work. Проверки — в Docker.
.PHONY: help test inst

help: ## список команд
	@grep -E '^[a-z-]+:.*## ' Makefile | sed 's/:.*## /\t/'

test: ## проверка репозитория (Docker)
	docker compose build -q test
	docker compose run --rm test

inst: ## собрать инструкции в inst/dist/*.docx (Docker, Pandoc)
	mkdir -p inst/dist
	docker compose build -q inst
	UID=$$(id -u) GID=$$(id -g) docker compose run --rm inst
