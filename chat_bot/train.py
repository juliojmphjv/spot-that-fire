from chatterbot.trainers import ListTrainer
from datawarehouse.bot_data import talks_data
from .Abelis_Bot import AbelisBot
class TrainBot:

    def __init__(self):

        self.data = (talks_data.small_talk, talks_data.math_talk_1, talks_data.math_talk_2)

    def train(self):

        bot = AbelisBot()
        list_trainer = ListTrainer(bot)
        for item in self.data:
            list_trainer.train(item)

if __name__ == "__main__":
    train = TrainBot()
    train.train()