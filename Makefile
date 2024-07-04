default: fmt lint

# Code Quality
fmt:
	ruff format app

lint:
	ruff check app

fix:
	ruff check --fix app

typecheck:
	pyright app

# Local Development
docker-up:
	docker compose -f docker-compose-local.yaml up -d
