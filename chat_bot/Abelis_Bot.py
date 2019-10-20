from chatterbot import ChatBot
from datawarehouse.bot_data import talks_data
from chatterbot.trainers import ListTrainer


class AbelisBot:

    def __init__(self):
        self.bot = ChatBot(name='Abellis',
                           read_only=True,
                           logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                           'chatterbot.logic.BestMatch'
                                           ],

                           )
        self.data = (talks_data.small_talk, talks_data.math_talk_1, talks_data.math_talk_2)


    def reply(self, msg):

        self.bot.get_response(msg)


    def train(self):

        list_trainer = ListTrainer(self.bot)
        for item in self.data:
            list_trainer.train(item)

if __name__ == "__main__":

    bot = AbelisBot()

    print(bot.reply('Olá'))