import os
import functions_framework
from flask import Request, Response
from telegram import Bot, Update
from telegram.ext import Dispatcher, MessageHandler, Filters

# Initialize bot with token from Firebase environment variables
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
bot = Bot(token=TELEGRAM_TOKEN)
dispatcher = Dispatcher(bot, None, workers=0)

# Simple echo handler
def echo(update, context):
    update.message.reply_text(f"📱 You said: {update.message.text}")

dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# Firebase HTTP trigger
@functions_framework.http
def webhook(request: Request) -> Response:
    if request.method == "POST":
        update = Update.de_json(request.get_json(force=True), bot)
        dispatcher.process_update(update)
    return Response("OK", status=200)
