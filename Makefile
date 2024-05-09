default: fmt lint

# Dependencies Management
lock:
	uv pip compile pyproject.toml -o requirements.txt
	uv pip compile --extra dev pyproject.toml -o requirements-dev.txt

sync:
	uv pip sync requirements.txt

sync-dev:
	uv pip sync requirements-dev.txt

init-cli:
	uv pip install -e .

# Code Formatting & Linting
fmt:
	-isort app
	-black app
	-docformatter app

lint:
	-pyright app
	-flake8 app
	-autoflake app
	-bandit -c pyproject.toml -q -r app
