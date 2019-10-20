#!/bin/sh

python manage.py migrate
python manage.py createdataframe
python manage.py createdataframeincra

exec python manage.py runserver 0.0.0.0:8000
