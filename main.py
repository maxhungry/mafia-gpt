import openai

from config import OPENAI_API_KEY
from mafia.game import Game

openai.api_key = OPENAI_API_KEY


def main():
    game = Game()
    game.start()


if __name__ == '__main__':
    main()
