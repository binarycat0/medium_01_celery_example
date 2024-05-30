FROM python:3.11-slim

RUN apt-get update  \
    && apt-get install -y make pipx  \
    && apt-get clean
RUN pipx install poetry

ENV POETRY_HOME=/root/.local/bin
COPY poetry.lock pyproject.toml Makefile ./
RUN make install

RUN mkdir -p /example
COPY ./example ./example

ARG DJANGO_SETTINGS_MODULE
ARG WEB_APP_PORT

ENV WEB_APP_PORT=${WEB_APP_PORT}
EXPOSE $WEB_APP_PORT

CMD make port=0.0.0.0:${WEB_APP_PORT} run
