#!/bin/bash

GUNICORN_CONF=gunicorn_api.conf.py
GUNICORN_PID=gunicorn_api.pid

pipenv run gunicorn --reload -c $GUNICORN_CONF --pid $GUNICORN_PID src.app:app
