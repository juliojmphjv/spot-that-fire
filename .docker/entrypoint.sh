#!/bin/sh

python manage.py migrate
python manage.py createdataframe

exec python manage.py runserver 0.0.0.0:8000
