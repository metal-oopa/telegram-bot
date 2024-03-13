from dotenv import load_dotenv
import os
import telebot
from openai import OpenAI

from utils.utils import get_daily_horoscope, date_format_check
from constants.constants import ZODIAC_SIGNS, COMMANDS, ERROR_MESSAGES, RESPONSES, DAYS
load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

if not BOT_TOKEN:
    raise ValueError(f"BOT_TOKEN {ERROR_MESSAGES['not_found']}")

if not OPENAI_API_KEY:
    raise ValueError(f"OPENAI_API_KEY {ERROR_MESSAGES['not_found']}")

bot = telebot.TeleBot(BOT_TOKEN)
client = OpenAI(api_key=OPENAI_API_KEY)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    text = f"Hello, {message.from_user.first_name}! How are you doing?\n\n"
    for command, description in COMMANDS.items():
        text += f"/{command} - {description}\n"
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
    text = message.text
    bot.send_chat_action(message.chat.id, 'typing')

    reaction = telebot.types.ReactionTypeEmoji('👍')
    bot.set_message_reaction(
        message.chat.id, message.message_id, [reaction], True)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content":  text}],
    )
    completion = response.choices[0].message.content if response.choices[
        0].message.content else "I'm sorry, I don't understand."
    bot.send_message(message.chat.id, completion)


bot.infinity_polling()
