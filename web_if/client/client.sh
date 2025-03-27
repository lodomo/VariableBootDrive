#!/bin/bash

GUNICORN_CONF=gunicorn_client.conf.py
GUNICORN_PID=gunicorn_client.pid

pipenv run gunicorn --reload -c $GUNICORN_CONF --pid $GUNICORN_PID app:app
