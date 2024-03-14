import re
import requests
from datetime import datetime
from constants import constants
from random import randint


def get_daily_horoscope(sign: str, day: str) -> dict:
    """Get daily horoscope for a zodiac sign.

    Keyword arguments:
    sign:str - Zodiac sign
    day:str - Date in format (YYYY-MM-DD) OR TODAY OR TOMORROW OR YESTERDAY
    Return:dict - JSON data
    """
    url = constants.URLS['horoscope']
    params = {"sign": sign, "day": day}
    response = requests.get(url, params)

    return response.json()


def get_character_quote(character: str):
    """ Get a quote by a spacific character """
    try:
        parameters = {'name': character}
        query = requests.get(
            f"{constants.URLS['anime_quote']}/character", params=parameters)
        if valid_query(query):
            return query.json()
    except Exception as e:
        print(e)


def get_anime_quote(title: str):
    try:
        parameters = {'title': title}
        query = requests.get(
            f"{constants.URLS['anime_quote']}/anime", params=parameters)
        if valid_query(query):
            return query.json()
    except Exception as e:
        print(e)


def get_random_anime_quote():
    try:
        query = requests.get(constants.URLS['anime_quote'])
        if valid_query(query):
            return query.json()
    except Exception as e:
        print(e)


def get_character_picture(character) -> str:
    """ Retrive a random character image """
    results = None
    try:
        parameters = {'q': character, 'limit': 3}
        query = requests.get("https://api.jikan.moe/v4/characters",
                             params=parameters, timeout=10)
        if query.status_code == 200:
            results = query.json()['data'][0]
    except:
        pass
    picture_url = None
    if results:
        character_id = results['mal_id']
        try:
            pictures_list = requests.get(
                f'https://api.jikan.moe/v4/characters/{character_id}/pictures', timeout=10).json()['data']
            if len(pictures_list) <= 0:
                return ""
            picture_url = pictures_list[randint(
                0, len(pictures_list)-1)]['jpg']['image_url']
        except:
            pass
    return picture_url if picture_url else ""


def get_waifu_pic(category: str, tags: str) -> dict:
    """Get waifu pic from waifu.pics based on the category, sfw or nsfw, and tags.

    Keyword arguments:
    category:str - Category (sfw or nsfw)
    tags:str - Tags
    Return:dict - JSON data
    """
    url = f"{constants.URLS['waifu']}/{category}/{tags}"
    response = requests.get(url)

    return response.json()


def get_random_nsfw_waifu_pic() -> dict:
    """Get random nsfw waifu pic.

    Return:dict - JSON data
    """
    url = constants.URLS['nsfw']
    response = requests.get(url)

    return response.json()


def get_random_sfw_waifu_pic() -> dict:
    """Get random sfw waifu pic.

    Return:dict - JSON data
    """
    url = constants.URLS['sfw']
    response = requests.get(url)

    return response.json()


def get_weather(city: str, api_key: str) -> dict:
    """Get weather for a city.

    Keyword arguments:
    city:str - City name
    Return:dict - JSON data
    """
    url = constants.URLS['weather']
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(url, params)

    return response.json()


def date_format_check(date: str) -> bool:
    """Check if date is in correct format (YYYY-MM-DD).

    Keyword arguments:
    date:str - Date in format (YYYY-MM-DD)
    Return:bool - True if date is in correct format, False otherwise
    """
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def valid_query(query) -> bool:
    if query.status_code == 200:
        return True
    return False
