.PHONY: init
init:
poetry_home = ${POETRY_HOME}

ifeq ("$(wildcard $(poetry_home))","")
poetry?=poetry
else
poetry=$(poetry_home)/poetry
endif

proj_name=medium_01_celery_example
compose_file=docker/compose.yaml
docker_env_file=./docker/.env
docker-compose=docker compose -f $(compose_file) -p $(proj_name) --project-directory=. --env-file=$(docker_env_file)

.PHONY: install
install: init
	$(poetry) install

.PHONY: run
run: init
ifdef port
	@echo 'port $(port)'
else
	port=8000
endif
	$(poetry) run python example/manage.py runserver $(port)

.PHONY: docker-build
docker-build: init
	$(docker-compose) build

.PHONY: docker-up
docker-up: docker-build
	$(docker-compose) up -d

.PHONY: docker-down
docker-down: init
	$(docker-compose) down

.PHONY: docker-ps
docker-ps: init
	$(docker-compose) ps
