from dotenv import load_dotenv
import os
import telebot

from utils.utils import get_daily_horoscope, date_format_check
from constants.constants import ZODIAC_SIGNS, COMMANDS, ERROR_MESSAGES, RESPONSES, DAYS
load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')

if not BOT_TOKEN:
    raise ValueError(ERROR_MESSAGES["token_not_found"])

bot = telebot.TeleBot(BOT_TOKEN)  # type: ignore


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    text = f"Hello, {message.from_user.first_name}! How are you doing?"
    bot.reply_to(message, text)


@bot.message_handler(commands=['help'])
def send_help(message):
    text = RESPONSES["help"]
    for command, description in COMMANDS.items():
        text += f"/{command} - {description}\n"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['horoscope'])
def sign_handler(message):
    text = RESPONSES["horoscope"]
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, day_handler)


def day_handler(message):
    sign = message.text
    if sign.capitalize() not in ZODIAC_SIGNS:
        bot.send_message(message.chat.id, ERROR_MESSAGES["invalid_sign"])
        return
    text = RESPONSES["day"]
    sent_msg = bot.send_message(
        message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(
        sent_msg, fetch_horoscope, sign.capitalize())


def fetch_horoscope(message, sign):
    day = message.text
    # check if date is in correct format
    if not date_format_check(day) and day.upper() not in DAYS:
        bot.send_message(
            message.chat.id, ERROR_MESSAGES["invalid_date"])
        return

    horoscope = get_daily_horoscope(sign, day)
    status = horoscope["status"]
    if status != 200:
        bot.send_message(message.chat.id, horoscope["message"])
        return

    data = horoscope["data"]
    horoscope_message = f'*Horoscope:* {data["horoscope_data"]}\n*Sign:* {sign}\n*Day:* {data["date"]}'
    bot.send_message(message.chat.id, "Here's your horoscope!")
    bot.send_message(message.chat.id, horoscope_message, parse_mode="Markdown")


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
