.PHONY: all download openapi
all: download openapi
download:
	curl -o openapi.json http://localhost:8000/openapi.json

openapi:
	docker run --rm \
			-v ${PWD}:/local openapitools/openapi-generator-cli generate \
			-i /local/openapi.json \
			-g python \
			-c /local/config.json \
			-o /local
