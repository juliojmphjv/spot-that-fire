#!/bin/sh

set -e

python manage.py migrate
python manage.py createdataframe
python manage.py createdataframeincra
python callback_api.py &
python manage.py runserver 0.0.0.0:8000

