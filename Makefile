# orb-work. Проверки — в Docker.
.PHONY: help test

help: ## список команд
	@grep -E '^[a-z-]+:.*## ' Makefile | sed 's/:.*## /\t/'

test: ## проверка репозитория (Docker)
	docker compose build -q test
	docker compose run --rm test
