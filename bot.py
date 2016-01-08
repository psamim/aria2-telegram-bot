#!/usr/bin/env python3

from telegram import Updater
import subprocess
import logging
import sys
import os

# Enable logging
logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

logger = logging.getLogger(__name__)

# Commands
def echo(bot, update):
    bot.sendMessage(update.message.chat_id, text=update.message.text)

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

def diana(bot, update, args):
    logger.info('Message for diana.')
    commands = list(args)
    commands.insert(0, "./diana/diana")
    logger.info('Command: "%s"' % (' '.join(commands)))

    # Correct telegram mistakes
    if commands[1] == 'help':
        commands[1] = '--help'

    try:
        output = subprocess.check_output(commands, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        output = e.output

    logger.info('Output: "%s"' % (output))
    bot.sendMessage(chat_id=update.message.chat_id, text=output.decode())

def main():
    token = os.environ["TOKEN"]
    updater = Updater(token)
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.addTelegramCommandHandler("diana", diana)

    # on noncommand i.e message - echo the message on Telegram
    # dp.addTelegramMessageHandler(echo)

    # on error - print error to stdout
    dp.addErrorHandler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
