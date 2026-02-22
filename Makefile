.PHONY: run
run:
	uv run python -m src.flow.main

.PHONY: ruff
ruff:
	uv run ruff format .

.PHONY: run_%
run_%:
	uv run python -m curl_and_responses.$*.request

.PHONY: test
test: 
	uv run test.py

.PHONY: load
load:
	uv run load_json.py

.PHONY: run_registration
run_registration:
	uv run python -m src.flow.register_flow