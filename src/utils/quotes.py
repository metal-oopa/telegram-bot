from src.utils import utils
from src.constants import constants


def handle_rquote_command(bot, message):
    """ Handle /rquote command """
    quote = utils.get_random_anime_quote()
    if quote:
        picture_url = utils.get_character_picture(quote['character'])
        if picture_url:
            bot.send_photo(message.chat.id, picture_url,
                           caption=f"{quote['quote']}\n- {quote['character']} ({(quote['anime'])})")
        else:
            bot.send_message(
                message.chat.id, f"{quote['quote']}\n- {quote['character']} ({(quote['anime'])})")
    else:
        bot.send_message(message.chat.id, constants.ERROR_MESSAGES['error'])


def handle_aquote_command(bot, message, title):
    """ Handle /aquote command """
    quote = utils.get_anime_quote(title)
    if quote:
        picture_url = utils.get_character_picture(quote['character'])
        if picture_url:
            bot.send_photo(message.chat.id, picture_url,
                           caption=f"{quote['quote']}\n- {quote['character']} ({(quote['anime'])})")
        else:
            bot.send_message(
                message.chat.id, f"{quote['quote']}\n- {quote['character']} ({(quote['anime'])})")
    else:
        bot.send_message(message.chat.id, constants.ERROR_MESSAGES['error'])


def handle_cquote_command(bot, message, character):
    """ Handle /cquote command """
    quote = utils.get_character_quote(character)
    if quote:
        picture_url = utils.get_character_picture(quote['character'])
        if picture_url:
            bot.send_photo(message.chat.id, picture_url,
                           caption=f"{quote['quote']}\n- {quote['character']} ({(quote['anime'])})")
        else:
            bot.send_message(
                message.chat.id, f"{quote['quote']}\n- {quote['character']} ({(quote['anime'])})")
    else:
        bot.send_message(message.chat.id, constants.ERROR_MESSAGES['error'])
