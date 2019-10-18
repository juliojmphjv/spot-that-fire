FROM python:3.7

WORKDIR /root

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY app app
COPY pages pages
COPY manage.py .
COPY ./.docker/entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]
