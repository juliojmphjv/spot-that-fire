FROM python:3.7

WORKDIR /root

COPY ./requirements.txt .

RUN pip install -r requirements.txt

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
COPY callback_api.py callback_api.py
COPY datawarehouse datawarehouse
COPY data_visualization data_visualization
COPY data_analise data_analise
COPY plots plots
COPY ./.docker/entrypoint.sh /

VOLUME /root/data

ENTRYPOINT ["/entrypoint.sh"]
