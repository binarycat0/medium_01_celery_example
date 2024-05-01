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
	$(poetry) run python example/manage.py runserver

.PHONY: docker-up

docker-up:
	docker compose up

.PHONY: docker-down

docker-down:
	docker compose down