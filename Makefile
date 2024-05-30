SHELL = /bin/sh

.DEFAULT_GOAL:=help

.PHONY: install
install: 
	poetry install

.PHONY: test-main-parser
test-main-parser:
	pytest ./tests/tests_log_parser.py -v

.PHONY: shell
shell:
	poetry shell

.PHONY: run-data-parser
run-data-parser:
	poetry shell

.PHONY: run-main-parser
FILE ?= $(error FILE is not set)
INIT_DATE ?= $(error INIT_DATE is not set)
END_DATE ?= $(error END_DATE is not set)
HOST ?= $(error HOST is not set)
run-main-parser:
	python scripts/main_data_parser.py $(FILE) $(INIT_DATE) $(END_DATE) $(HOST)

.PHONY: run-unlimited-parser
FILE ?= $(error FILE is not set)
HOST_FROM ?= $(error HOST_FROM is not set)
HOST_TO ?= $(error HOST_TO is not set)
run-unlimited-parser:
	python scripts/realtime_log_parser.py $(FILE) $(HOST_FROM) $(HOST_TO)