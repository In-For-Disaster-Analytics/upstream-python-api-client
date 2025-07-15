all:
	make openapi

openapi:
	docker run --rm \
			-v ${PWD}:/local openapitools/openapi-generator-cli generate \
			-i /local/openapi.json \
			-g python \
			-c /local/config.json \
			-o /local
