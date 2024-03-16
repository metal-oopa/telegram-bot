from src.utils import utils
from telebot import types


def anime_recommendations_handler(bot, message, username, number=1):
    """Handle anime recommendations."""
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(
        'Next anime ➡️', callback_data=f'next_anime {username} {number+1}')
    markup.add(button1)

    page = 1
    batch = 1
    recommendations = utils.get_anime_recommendations(username, page, batch)
    if recommendations['data'] and number <= len(recommendations['data']):
        anime = recommendations['data'][number-1]
        genres = ', '.join(anime['details']['genres'])
        title = anime['details']['title']
        score = anime['details']['mean']
        length = anime['details']['length']
        rating = anime['details']['rating']
        picture_url = anime['details']['picture']
        bot.send_photo(message.chat.id, photo=picture_url, caption=f"{title}\nMal mean score: {score}\nGenres: {genres}\nLength: {length}\nRating: {rating}",
                       reply_markup=markup)
    else:
        bot.send_message(
            message.chat.id, "No more recommendations available.")
        return
