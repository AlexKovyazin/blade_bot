import os
import telebot

from flask import Flask, request

from config import TOKEN, URL
from config import pg_connect, logger


bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=URL + TOKEN)
    return "!", 200


@server.route('/' + TOKEN, methods=['POST'])
def get_message():
    """
    Process message with Flask
    :return: response
    """
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200
