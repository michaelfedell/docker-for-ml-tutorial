APP_NAME=iris-pipeline

requirements.txt: poetry.lock
	poetry export -f requirements.txt --output requirements.txt --without-hashes

requirements: requirements.txt

build: Dockerfile
	docker build -t ${APP_NAME}:latest .

run:
	docker run \
		-v $(shell pwd)/artifacts/:/app/artifacts\
		${APP_NAME}:latest

clean:
	docker stop ${APP_NAME} && docker rm ${APP_NAME}