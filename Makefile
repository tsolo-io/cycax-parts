.ONESHELL: # Run all the commands in the same shell
.PHONY: docs build
.DEFAULT_GOAL := help

help:
	@echo "Help"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

build:
	hatch run python3 src/cycax_parts/build.py
