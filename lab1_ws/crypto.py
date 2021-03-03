"""
Simple Bot to reply to Telegram messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import requests
import json
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):

    update.message.reply_text("TIENES LOS SIGUIENTES COMANDOS:")
    update.message.reply_text("/START = Inicializar el bot con un saludo\n/DINERO = Consultar cuanto dinero tenemos actualmente\n/MINAR = Ver cuanto dinero tengo minado actualmente\n/DIBUJO = Te devuelve un dibujo hecho con amor")

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def dinero(update, context):
    uri = "https://api.kraken.com/0/public/Ticker?pair=ADAEUR,%20XDGEUR,%20BTCEUR,%20XETHZEUR"
    metodoa = 'GET'
    goiburuak = {'Host': 'api.kraken.com'}
    edukia = ''

    erantzuna = requests.request(metodoa, uri, headers=goiburuak, data=edukia)
    edukia = json.loads(erantzuna.content)

    # DOGE PRICE
    dogePrice = float(edukia["result"]["XDGEUR"]["c"][0])
    dogeEur = 15
    dogeCoins = 312.50
    dogeTotal = dogePrice*dogeCoins

    # ADA PRICE
    adaPrice = float(edukia["result"]["ADAEUR"]["c"][0])
    adaEur = 20
    adaCoins = 16.50
    adaTotal = adaPrice*adaCoins

    # BTC PRICE
    btcPrice = float(edukia["result"]["XXBTZEUR"]["c"][0])
    btcEur = 75
    btcCoins = 0.001575
    btcTotal = btcPrice*btcCoins

    # ETH PRICE
    ethPrice = float(edukia["result"]["XETHZEUR"]["c"][0])
    ethCoins = 0.03756
    ethEur = 50
    ethTotal = ethPrice*ethCoins

    update.message.reply_text("ETHEREUM PRICE (eur) = " + str(ethPrice)+"\n"+"  - Teniamos "+str(ethEur)+" -> "+str(ethTotal))
    update.message.reply_text("BITCOIN PRICE (eur) = " + str(btcPrice)+"\n"+"  - Teniamos "+str(btcEur)+" -> "+str(btcTotal))
    update.message.reply_text("DOGECOIN PRICE (eur) = " + str(dogePrice)+"\n"+"  - Teniamos "+str(dogeEur)+" -> "+str(dogeTotal))
    update.message.reply_text("CARDANO PRICE (eur) = " + str(adaPrice)+"\n"+"  - Teniamos "+str(adaEur)+" -> "+str(adaTotal))


def dibujo(update, context):
    update.message.reply_text("┼┼┼┼┼┼┼▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄┼┼┼┼┼┼\n┼┼┼┼┼┼┼█▒▒░░░░░░░░░▒▒█┼┼┼┼┼┼\n┼┼┼┼┼┼┼┼█░░█░░░░░█░░█┼┼┼┼┼┼┼\n┼┼┼┼─▄▄──█░░░▀█▀░░░█──▄▄─┼┼┼\n┼┼┼┼█░░█─▀▄░░░░░░░▄▀─█░░█┼┼┼\n┼██░██░████░██░░░██░░░█████┼\n┼██▄██░██▄▄░██░░░██░░░██░██┼\n┼██▀██░██▀▀░██░░░██░░░██░██┼\n┼██░██░████░████░████░█████┼")

def minero(update, context):
    uri = "https://eth.2miners.com/api/accounts/0x3C99c18A9DB8063F2edB586AE24E9d05DD045b2e"
    metodoa = 'GET'
    goiburuak = {'Host': 'eth.2miners.com'}
    edukia = ''

    erantzuna = requests.request(metodoa, uri, headers=goiburuak, data=edukia)
    edukia = json.loads(erantzuna.content)
    money = float(edukia["stats"]["balance"]) * (10 ** (-9))

    uri = "https://api.gdax.com/products/eth-eur/ticker"
    metodoa = 'GET'
    goiburuak = {'Host': 'api.gdax.com'}
    edukia = ''
    erantzuna = requests.request(metodoa, uri, headers=goiburuak, data=edukia)
    edukia = json.loads(erantzuna.content)
    price = float(edukia["price"])
    act = money * price

    update.message.reply_text("ETHEREUM PRICE (eur) = " + str(price))
    update.message.reply_text("MONEY (eth) = " + str(money))
    update.message.reply_text("MONEY (eur) = " + str(act) + " €")

def sumar(update,context):
    try:
        numero1 = int(context.args[0])
        numero2 = int(context.args[1])

        suma = numero1 + numero2

        update.message.reply_text("La suma es "+str(suma))

    except (ValueError):
        update.message.reply_text("por favor utilice dos numeros")

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1638741516:AAEosfIW_f2qIAIRSvgSMq5Ta-dQQSJ1Cl4", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("START", start))
    dp.add_handler(CommandHandler("DINERO", dinero))
    dp.add_handler(CommandHandler("MINAR", minero))
    dp.add_handler(CommandHandler("DIBUJO", dibujo))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
