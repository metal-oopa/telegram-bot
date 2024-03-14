from dotenv import load_dotenv
import telebot
from openai import OpenAI

from config.config import get_environment_variable
from utils import horoscope, weather, waifu, message_handlers, quotes
load_dotenv()

BOT_TOKEN = get_environment_variable('BOT_TOKEN')
OPENAI_API_KEY = get_environment_variable('OPENAI_API_KEY')
OPENWEATHERMAP_API_KEY = get_environment_variable('OPENWEATHERMAP_API_KEY')

bot = telebot.TeleBot(BOT_TOKEN)
client = OpenAI(api_key=OPENAI_API_KEY)

# TODO: Add recommendations (if possible), memes


@bot.message_handler(commands=['start', 'hello'])
def handle_welcome_message(message):
    message_handlers.send_welcome(bot, message)


@bot.message_handler(commands=['help'])
def handle_help_message(message):
    message_handlers.send_help(bot, message)


@bot.message_handler(commands=['rquote'])
def handle_random_quote_command(message):
    quotes.handle_rquote_command(bot, message)


@bot.message_handler(commands=['aquote'])
def handle_anime_quote_command(message):
    title = message.text.split(' ', 1)[1]
    quotes.handle_aquote_command(bot, message, title)


@bot.message_handler(commands=['cquote'])
def handle_character_quote_command(message):
    character = message.text.split(' ', 1)[1]
    quotes.handle_cquote_command(bot, message, character)


@bot.message_handler(commands=['horoscope'])
def handle_horoscope_command(message):
    horoscope.handle_horoscope_command(bot, message)


@bot.message_handler(commands=['weather'])
def handle_weather_command(message):
    weather.handle_weather_command(bot, message, OPENWEATHERMAP_API_KEY)


@bot.message_handler(commands=['waifu'])
def handle_waifu_command(message):
    waifu.handle_waifu_command(bot, message)


@bot.message_handler(commands=['nsfw'])
def nsfw_waifu_handler(message):
    waifu.handle_nsfw_waifu_command(bot, message)


@bot.message_handler(commands=['sfw'])
def sfw_waifu_handler(message):
    waifu.handle_sfw_waifu_command(bot, message)


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    message_handlers.echo_all(bot, client, message)


bot.infinity_polling()
