APP_NAME=iris-inference

requirements.txt: poetry.lock
	poetry export -f requirements.txt --output requirements.txt --without-hashes

requirements: requirements.txt

build: Dockerfile
	docker build -t ${APP_NAME}:latest .

run:
	docker run --name ${APP_NAME} \
		-v $(shell pwd)/../pipeline/artifacts/:/app/artifacts\
		-p 80:80 ${APP_NAME}

clean:
	docker stop ${APP_NAME} && docker rm ${APP_NAME}