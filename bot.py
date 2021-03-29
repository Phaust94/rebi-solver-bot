from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import os
os.chdir(os.path.join(*os.path.split(__file__)[:-1]))

from version import __version__
from secrets import API_KEY
from helpers import solve_rebus, brute_force


# noinspection PyUnusedLocal
def handle_text(update: Update, context: CallbackContext) -> None:
    txt = update.message.text
    solved = solve_rebus(txt)

    update.message.reply_text(solved)

    return None


# noinspection PyUnusedLocal
def info(update: Update, context: CallbackContext) -> None:
    msg = "This is a bot for solving rebi.\nVersion {}".format(
        __version__
    )
    update.message.reply_text(msg)
    return None


def error_handler(update: Update, context: CallbackContext) -> None:
    msg = f"An error occurred while handling that message:\n{context.error}"
    update.message.reply_text(msg)
    return None


# noinspection PyUnusedLocal
def brute_force_cmd(update: Update, context: CallbackContext) -> None:
    txt = update.message.text
    if txt.startswith(r"/b "):
        txt = txt[3:]
    res = brute_force(txt)
    update.message.reply_text(res)
    return None


def main():
    updater = Updater(API_KEY, workers=1)

    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))
    updater.dispatcher.add_handler(CommandHandler("info", info))
    updater.dispatcher.add_handler(CommandHandler("b", info))

    updater.dispatcher.add_error_handler(error_handler)

    updater.start_polling()
    updater.idle()
    return None


if __name__ == '__main__':
    main()
