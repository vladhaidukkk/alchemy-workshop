default: fmt

lock:
	uv pip compile pyproject.toml -o requirements.txt
	uv pip compile --extra dev pyproject.toml -o requirements-dev.txt

sync:
	uv pip sync requirements.txt

sync-dev:
	uv pip sync requirements-dev.txt

fmt:
	-isort app
	-black app
