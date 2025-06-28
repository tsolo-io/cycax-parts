# SPDX-FileCopyrightText: 2025 Tsolo.io
#
# SPDX-License-Identifier: Apache-2.0

.ONESHELL: # Run all the commands in the same shell
.PHONY: docs build
.DEFAULT_GOAL := help

help:
	@echo "Help"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

build: example/hvac ## Build all the examples.
	hatch run python3 src/build.py

example/hvac: ## Build all the HVAC examples. This will build the Fan examples.
	hatch run python3 src/examples/build_hvac.py

format: ## Format the code.
	hatch run lint:fmt
