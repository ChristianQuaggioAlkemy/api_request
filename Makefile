IMAGE_NAME="api_test"
VERSION=1.0

.PHONY: help build test shell

help:
	@echo "- make build                 Build docker image"
	@echo "- make test                  Run tests"

.DEFAULT_GOAL := help

build:
	@docker build --tag ${IMAGE_NAME}:latest --tag ${IMAGE_NAME}:${VERSION} .


test: build
	@docker run --rm -it ${IMAGE_NAME}

shell:
	@docker run --rm -it ${IMAGE_NAME} \
		bash -l
