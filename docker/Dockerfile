FROM python:3.11-slim

RUN apt-get update  \
    && apt-get install -y make pipx  \
    && apt-get clean
RUN pipx install poetry

ENV POETRY_HOME=/root/.local/bin
COPY poetry.lock pyproject.toml Makefile ./
RUN make install

COPY ./docker/entrypoints/celery_entrypoint.sh /celery_entrypoint.sh
COPY ./docker/entrypoints/django_entrypoint.sh /django_entrypoint.sh

RUN chmod +x /django_entrypoint.sh
RUN chmod +x /celery_entrypoint.sh

RUN mkdir -p /example
COPY ./example /example
ENV PYTHONPATH=/example

ARG WEB_APP_PORT
EXPOSE $WEB_APP_PORT