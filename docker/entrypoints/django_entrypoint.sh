#!/bin/sh
make migrate
make collectstatic
make gunicorn