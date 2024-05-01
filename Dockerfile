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

EXPOSE 8000
CMD ["make", "run"]
