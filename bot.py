from telegram import Updater
import subprocess
import logging
import sys

# Enable logging
root = logging.getLogger()
root.setLevel(logging.INFO)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = \
    logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)

logger = logging.getLogger(__name__)

# Commands
def echo(bot, update):
    bot.sendMessage(update.message.chat_id, text=update.message.text)

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

def diana(bot, update, args):
    command = ' '.join(args)

    try:
        output = subprocess.check_output(["./diana/diana", command], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        output = e.output

    for line in output.splitlines():
        bot.sendMessage(chat_id=update.message.chat_id, text=line.decode())

def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("161505178:AAGCkozCAakR6CDKw2SQTiO_-jeX_eM0xGY")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.addTelegramCommandHandler("diana", diana)

    # on noncommand i.e message - echo the message on Telegram
    # dp.addTelegramMessageHandler(echo)

    # on error - print error to stdout
    dp.addErrorHandler(error)

    # Start the Bot
    updater.start_polling(timeout=5)

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
