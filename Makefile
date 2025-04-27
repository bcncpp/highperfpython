all: lint format profile_julia
format: uv run ruff format .  # Format all files with ruff

lint:
	uv run ruff check --fix .  # Lint the code and automatically fix issues

profile_julia:
	# To sort by cumulative time spent inside each function, which helps us identify slow parts of the code.
	python -m cProfile -o profile.stats -s cumulative julia_main.py  # Run profiling with cumulative sorting
julia_line_profiler:
	# has a meaniful overhead in complex programs is not possible to see.
	kernprof -l -v julia_line_profile.py
julia_memory_profile:
	mprof run julia1_memoryprofiler.py
julia_time:
	# Measure execution time of julia_main.py
	time -p python julia_main.py  # Run the script and output the elapsed time
check_stat:
	python check_stat.py
webstat: profile_julia
	snakeviz profile.stats
pyspy:
	py-spy record -o profile.svg -- python julia_main.py

