include .env-local
export

.PHONY: init
init:
poetry_home=${POETRY_HOME}

ifeq ("$(wildcard $(poetry_home))","")
poetry?=poetry
else
poetry=$(poetry_home)/poetry
endif

proj_name=medium_01_celery_example
compose_file=docker/compose.yaml
compose_file_all=docker/compose-all.yaml
docker_env_file=./docker/.env-docker
docker-compose-common=docker compose -p $(proj_name) --project-directory=. --env-file=$(docker_env_file)
docker-compose=$(docker-compose-common) -f $(compose_file)
docker-compose-all=$(docker-compose-common) -f $(compose_file_all)

.PHONY: install
install: init
	$(poetry) install --no-interaction --no-root

.PHONY: gunicorn
gunicorn: init
	$(poetry) run gunicorn example.wsgi --reload --pythonpath=example -w 2 -b 0.0.0.0:${WEB_APP_PORT}

.PHONY: run
run: init
	$(poetry) run python example/manage.py runserver 0.0.0.0:${WEB_APP_PORT}

.PHONY: collectstatic
collectstatic: init
	$(poetry) run python example/manage.py collectstatic --no-input

.PHONY: migrate
migrate: init
	$(poetry) run python example/manage.py migrate

.PHONY: initadmin
initadmin: init
	$(poetry) run python example/manage.py createsuperuser --username=${DJANGO_SUPERUSER_NAME} --noinput --skip-checks

.PHONY: docker-build
docker-build: init
	$(docker-compose) build

.PHONY: docker-up
docker-up: docker-build
	$(docker-compose) up -d

.PHONY: docker-up-all
docker-up-all: docker-build
	$(docker-compose-all) up -d

.PHONY: docker-down
docker-down: init
	$(docker-compose) down

.PHONY: docker-ps
docker-ps: init
	$(docker-compose) ps

.PHONY: celery-worker
celery-worker:
	$(poetry) run celery \
	--workdir=example \
	-A ${CELERY_WORKER_APP_NAME} \
	worker \
	--events \
	--queues default \
	-l ${CELERY_WORKER_LOG_LEVEL}