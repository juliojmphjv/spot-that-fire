FROM python:3.7

WORKDIR /root

ENV DEBIAN_FRONTEND noninteractive

COPY ./requirements.txt .

RUN pip install -r requirements.txt \
    && apt-get update -y \
    && apt-get install -y runit \
    && mkdir /etc/service

COPY ./.docker/services /etc/service
COPY app app
COPY pages pages
COPY services services
COPY manage.py .
COPY templates templates
COPY static static
COPY notification_sender notification_sender
COPY incra_data incra_data
COPY cadastro cadastro
COPY chat_bot chat_bot

COPY ./.docker/entrypoint.sh /

VOLUME /root/data

ENTRYPOINT ["/entrypoint.sh"]
