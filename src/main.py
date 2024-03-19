from dotenv import load_dotenv
import telebot
from openai import OpenAI
from flask import Flask, request, jsonify

from src.constants.constants import RESPONSES, URLS
from src.utils import horoscope, weather, waifu, message_handlers, quotes, recommendation
from src.config.config import get_environment_variable
load_dotenv()

BOT_TOKEN = get_environment_variable('BOT_TOKEN')
OPENAI_API_KEY = get_environment_variable('OPENAI_API_KEY')
OPENWEATHERMAP_API_KEY = get_environment_variable('OPENWEATHERMAP_API_KEY')
SECRET = get_environment_variable('SECRET')

url = URLS['webhook'] + SECRET
bot = telebot.TeleBot(BOT_TOKEN, threaded=False)
client = OpenAI(api_key=OPENAI_API_KEY)
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!', 200


def error_handler(func):
    def wrapper(message):
        try:
            return func(message)
        except IndexError:
            bot.send_message(message.chat.id, RESPONSES['no_argument'])
        except Exception as e:
            bot.send_message(message.chat.id, RESPONSES['error'])
    return wrapper


@app.route('/' + SECRET, methods=['POST'])
def getMessage():
    update = telebot.types.Update.de_json(
        request.stream.read().decode('utf-8'))
    if update is not None:
        print("Update received", update)
        bot.process_new_updates([update])
    return "OK", 200


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": 404, "message": "Not Found"}), 404


@bot.message_handler(commands=['start', 'hello'])
def handle_welcome_message(message):
    message_handlers.send_welcome(bot, message)


@bot.message_handler(commands=['help'])
def handle_help_message(message):
    message_handlers.send_help(bot, message)


@bot.message_handler(commands=['recommend'])
@error_handler
def handle_recommendations_command(message):
    username = message.text.split(' ', 1)[1]
    recommendation.anime_recommendations_handler(bot, message, username)


@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    try:
        if call.data.startswith('next_anime'):
            username, number = call.data.split(' ')[1:]
            recommendation.anime_recommendations_handler(
                bot, call.message, username, int(number))
    except ValueError:
        bot.send_message(call.message.chat.id, "Invalid number format.")
    except Exception as e:
        bot.send_message(call.message.chat.id, RESPONSES['error'])


@bot.message_handler(commands=['rquote'])
def handle_random_quote_command(message):
    quotes.handle_rquote_command(bot, message)


@bot.message_handler(commands=['aquote'])
@error_handler
def handle_anime_quote_command(message):
    title = message.text.split(' ', 1)[1]
    quotes.handle_aquote_command(bot, message, title)


@bot.message_handler(commands=['cquote'])
@error_handler
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


if __name__ == '__main__':
    app.run()
    bot.remove_webhook()
    bot.set_webhook(url=url, drop_pending_updates=True)
