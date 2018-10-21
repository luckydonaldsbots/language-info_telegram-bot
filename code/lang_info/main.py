# -*- coding: utf-8 -*-
import requests
from flask import Flask, url_for
from luckydonaldUtils.logger import logging
from pytgbot import Bot
from pytgbot.api_types.receivable.media import Audio
from pytgbot.api_types.receivable.peer import User
from pytgbot.api_types.receivable.updates import Message
from teleflask import Teleflask
from teleflask.messages import HTMLMessage
from luckydonaldUtils.exceptions import assert_type_or_raise
from luckydonaldUtils.tg_bots.gitinfo import version_bp, version_tbp

from .langs import l
from .secrets import API_KEY, URL_HOSTNAME, URL_PATH

__author__ = 'luckydonald'
logger = logging.getLogger(__name__)
logging.add_colored_handler(level=logging.DEBUG)

app = Flask(__name__)
app.register_blueprint(version_bp)
# sentry = add_error_reporting(app)

bot = Teleflask(API_KEY, hostname=URL_HOSTNAME, hostpath=URL_PATH, hookpath="/income/{API_KEY}")
bot.init_app(app)
bot.register_tblueprint(version_tbp)

assert_type_or_raise(bot.bot, Bot)


@app.errorhandler(404)
def url_404(error):
    return "Nope.", 404
# end def


@app.route("/", methods=["GET","POST"])
def url_root():
    return "Yep."
# end def


@app.route("/healthcheck")
def url_healthcheck():
    return '[ OK ]', 200
    #return '[FAIL]', 500
# end def



@bot.command("start")
def cmd_start(update, text):
    return HTMLMessage(l(update.message).start_message)
# end def


@bot.command("help")
def cmd_start(update, text):
    return HTMLMessage(l(update.message).help_message)
# end def

@bot.on_message
def on_msg(update, msg):
    """
    :type  msg: Message
    """
    ln = l(update.message)
    return HTMLMessage(ln.lang_response.format(lang=msg.from_peer.language_code))
# end def
