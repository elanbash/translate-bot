import os
from typing import Final
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from googletrans import Translator

TOKEN: Final = os.getenv("TOKEN")


def main():
    bot = telegram.Bot(token=TOKEN)


if __name__ == '__main__':
    main()
