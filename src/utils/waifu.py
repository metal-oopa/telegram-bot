from utils import utils
from constants import constants


def handle_waifu_command(bot, message):
    text = "What category do you want to use? sfw or nsfw"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, fetch_waifu_pic, bot)


def fetch_waifu_pic(message, bot):
    category = message.text
    if category.lower() not in ["sfw", "nsfw"]:
        bot.send_message(message.chat.id, "Invalid category.")
        return

    text = f"Choose a tag from the list: \n"
    for tag in constants.WAIFU_PICS_CATEGORIES[category.lower()]:
        text += f"{tag} "

    sent_msg = bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(
        sent_msg, send_waifu_pic, category.lower(), bot)


def send_waifu_pic(message, category, bot):
    tags = message.text
    if tags.lower() not in constants.WAIFU_PICS_CATEGORIES[category]:
        bot.send_message(message.chat.id, "Invalid tag.")
        return
    waifu_pic = utils.get_waifu_pic(category, tags)
    if not waifu_pic["url"]:
        bot.send_message(message.chat.id, constants.ERROR_MESSAGES["error"])
        return

    bot.send_photo(message.chat.id, waifu_pic["url"])


def handle_nsfw_waifu_command(bot, message):
    waifu_pic = utils.get_random_nsfw_waifu_pic()
    if not waifu_pic["url"]:
        bot.send_message(message.chat.id, constants.ERROR_MESSAGES["error"])
        return

    bot.send_photo(message.chat.id, waifu_pic["url"])


def handle_sfw_waifu_command(bot, message):
    waifu_pic = utils.get_random_sfw_waifu_pic()
    if not waifu_pic["url"]:
        bot.send_message(message.chat.id, constants.ERROR_MESSAGES["error"])
        return

    bot.send_photo(message.chat.id, waifu_pic["url"])
