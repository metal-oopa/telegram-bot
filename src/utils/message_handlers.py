import telebot
from src.constants import constants


def send_welcome(bot, message):
    text = f"Hello, {message.from_user.first_name}! How are you doing?\n\n"
    for command, description in constants.COMMANDS.items():
        text += f"/{command} - {description}\n"
    bot.reply_to(message, text)


def send_help(bot, message):
    text = constants.RESPONSES["help"]
    for command, description in constants.COMMANDS.items():
        text += f"/{command} - {description}\n"
    text += "\nFor all other messages, ChatGPT will respond with a generated message."
    bot.send_message(message.chat.id, text)


def echo_all(bot, client, message):
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
