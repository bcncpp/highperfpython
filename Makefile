format: 
	uv run ruff format .
lint: 
	uv run ruff check --fix .
profile_julia:
	#  to sort by cumulative time spent inside each function; this gives us a view into the slowest parts of a section of code.
	python -m cProfile -s cumulative julia_main.py

julia_time:
	time -p python julia_main.py