from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from datawarehouse.bot_data import talks_data
import time

app = Flask(__name__)


def cadastro(nome, telefone, email, cep, cidade, iptu):
    pass


def salutation(msg):

    if msg == "1":
        return ""

    if msg == "2":
        return "Reportar"
    else:
        return (
            "Olá, eu sou a Abellis, uma inteligencia artificial. Envie *1* para se cadastrar em nosso sistema para receber notificações de incêndios florestais e relatórios. "
            "Ou envie *2* para reportar um incêndio."
        )


@app.route("/sms", methods=["GET", "POST"])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    bd = request.form["Body"]
    fr = request.form["From"]

    resposta = salutation(bd)
    # if bd == '1':
    #
    #
    # saudacao = 'Olá, eu sou a Abellis, a inteligencia artificial da Inbellis.'
    # options = 'Envie *1* para se cadastrar em nosso sistema para receber notificações de incêndios florestais e relatórios, ' \
    #           'Ou envie *2* para reportar um incêndio.'
    send = MessagingResponse()
    send.message(resposta)

    return str(send)


def replier(msg):

    resp = MessagingResponse()
    resp.message(msg)


def train_smart_bot():

    bot = ChatBot(
        name="Abellis",
        read_only=False,
        logic_adapters=[
            "chatterbot.logic.MathematicalEvaluation",
            "chatterbot.logic.BestMatch",
        ],
    )
    list_trainer = ListTrainer(bot)
    for item in (
        talks_data.small_talk,
        talks_data.math_talk_1,
        talks_data.math_talk_2,
    ):
        list_trainer.train(item)


if __name__ == "__main__":

    app.run(debug=True, host="0.0.0.0", port=4000)
