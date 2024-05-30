.PHONY: init
init:
poetry_home = ${POETRY_HOME}

ifeq ("$(wildcard $(poetry_home))","")
poetry?=poetry
else
poetry=$(poetry_home)/poetry
endif

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

.PHONY: docker-up
docker-up:
	docker compose \
-f docker/compose.yaml \
-p medium_01_celery_example \
--project-directory=. \
--env-file=./docker/.env \
up -d

.PHONY: docker-down
docker-down:
	docker compose \
-f docker/compose.yaml \
-p medium_01_celery_example \
--project-directory=. \
--env-file=./docker/.env \
down

.PHONY: docker-ps
docker-ps:
	docker compose \
-f docker/compose.yaml \
-p medium_01_celery_example \
--project-directory=. \
--env-file=./docker/.env \
ps
