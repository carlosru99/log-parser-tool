SHELL = /bin/sh

.DEFAULT_GOAL:=help

.PHONY: install
install: 
	poetry install


##@ Tests
.PHONY: test
test: ## Run tests using pytest.
	venv/bin/python -m pytest tests

##@ Linting
.PHONY: lint
lint: ## Lint code with flake8.
	venv/bin/pip install flake8
	venv/bin/flake8 .

##@ Formatting
.PHONY: format
format: ## Format code with black.
	venv/bin/pip install black
	venv/bin/black .

##@ Typing
.PHONY: type-check
type-check: ## Check types with mypy.
	venv/bin/pip install mypy
	venv/bin/mypy .

##@ Others
.PHONY: shell
shell: ## Activate virtual environment shell.
	. venv/bin/activate

##@ Help
.PHONY: help
help: ## Show help.
	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make \033[36m<target>\033[0m\n"} /^[a-z \/A-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
