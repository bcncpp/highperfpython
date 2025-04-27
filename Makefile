format: 
	uv run ruff format .
lint: 
	uv run ruff check --fix .
profile_julia:
	python -m cProfile -s cumulative julia_main.py