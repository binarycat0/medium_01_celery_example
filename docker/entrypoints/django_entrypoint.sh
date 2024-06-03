#!/bin/sh
make migrate
make initadmin
make collectstatic
make gunicorn