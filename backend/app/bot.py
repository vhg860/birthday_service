import os
from telegram import Bot

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

bot = Bot(token=TELEGRAM_TOKEN)


def send_telegram_message(username, message):
    from django.contrib.auth import get_user_model

    User = get_user_model()
    user = User.objects.get(username=username)
    if user:
        chat_id = user.telegram_chat_id
        bot.send_message(chat_id, message)
