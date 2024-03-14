from utils import utils
from constants import constants


def handle_weather_command(bot, message, api_key):
    text = constants.RESPONSES["weather"]
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, fetch_weather, api_key, bot)


def fetch_weather(message, api_key, bot):
    city = message.text
    weather_data = utils.get_weather(city, api_key)
    if weather_data["cod"] != 200:
        bot.send_message(message.chat.id, weather_data["message"])
        return

    data = weather_data["main"]
    weather_message = f'*City:* {weather_data["name"]}\n*Temperature:* {data["temp"]}°C\nFeels like: {data["feels_like"]}°C\n*Humidity:* {data["humidity"]}%\n*Pressure:* {data["pressure"]}hPa'
    bot.send_message(message.chat.id, "Here's the weather!")
    bot.send_message(message.chat.id, weather_message, parse_mode="Markdown")
