from utils import utils
from constants import constants


def handle_horoscope_command(bot, message):
    text = constants.RESPONSES["horoscope"]
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, day_handler, bot)


def day_handler(message, bot):
    sign = message.text.capitalize()
    if sign not in constants.ZODIAC_SIGNS:
        bot.send_message(
            message.chat.id, constants.ERROR_MESSAGES["invalid_sign"])
        return
    text = constants.RESPONSES["day"]
    sent_msg = bot.send_message(
        message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(
        sent_msg, fetch_horoscope, sign, bot)


def fetch_horoscope(message, sign, bot):
    day = message.text
    if not utils.date_format_check(day) and day.upper() not in constants.DAYS:
        bot.send_message(
            message.chat.id, constants.ERROR_MESSAGES["invalid_date"])
        return

    horoscope = utils.get_daily_horoscope(sign, day)
    status = horoscope["status"]
    if status != 200:
        bot.send_message(message.chat.id, horoscope["message"])
        return

    data = horoscope["data"]
    horoscope_message = f'*Horoscope:* {data["horoscope_data"]}\n*Sign:* {sign}\n*Day:* {data["date"]}'
    bot.send_message(message.chat.id, "Here's your horoscope!")
    bot.send_message(message.chat.id, horoscope_message, parse_mode="Markdown")
