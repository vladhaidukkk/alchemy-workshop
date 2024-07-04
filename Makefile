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
