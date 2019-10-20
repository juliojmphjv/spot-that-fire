
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from datawarehouse.bot_data import talks_data

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    bd = request.form['Body']
    fr = request.form['From']

    print(bd, fr)

    saudacao = 'Olá, eu sou a Abellis, como posso ajudar ?'
    resp = MessagingResponse()
    resp.message(saudacao)

    return str(resp)

def replier(msg):

    resp = MessagingResponse()
    resp.message(msg)

def train_smart_bot():

    bot = ChatBot(name='Abellis', read_only=False, logic_adapters=['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch'])
    list_trainer = ListTrainer(bot)
    for item in (talks_data.small_talk, talks_data.math_talk_1, talks_data.math_talk_2):
        list_trainer.train(item)



if __name__ == "__main__":

    app.run(debug=True, port=4000)

