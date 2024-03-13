import requests
from datetime import datetime


def get_daily_horoscope(sign: str, day: str) -> dict:
    """Get daily horoscope for a zodiac sign.

    Keyword arguments:
    sign:str - Zodiac sign
    day:str - Date in format (YYYY-MM-DD) OR TODAY OR TOMORROW OR YESTERDAY
    Return:dict - JSON data
    """
    url = "https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily"
    params = {"sign": sign, "day": day}
    response = requests.get(url, params)

    return response.json()

# get waifu pic from waifu.pics based on the category, sfw or nsfw, and tags


def get_waifu_pic(category: str, tags: str) -> dict:
    """Get waifu pic from waifu.pics based on the category, sfw or nsfw, and tags.

    Keyword arguments:
    category:str - Category (sfw or nsfw)
    tags:str - Tags
    Return:dict - JSON data
    """
    url = f"https://waifu.pics/api/{category}/{tags}"
    response = requests.get(url)

    return response.json()


def get_random_nsfw_waifu_pic() -> dict:
    """Get random nsfw waifu pic.

    Return:dict - JSON data
    """
    url = "https://waifu.pics/api/nsfw/waifu"
    response = requests.get(url)

    return response.json()


def get_random_sfw_waifu_pic() -> dict:
    """Get random sfw waifu pic.

    Return:dict - JSON data
    """
    url = "https://waifu.pics/api/sfw/waifu"
    response = requests.get(url)

    return response.json()


def get_weather(city: str, api_key: str) -> dict:
    """Get weather for a city.

    Keyword arguments:
    city:str - City name
    Return:dict - JSON data
    """
    url = "https://api.openweathermap.org/data/2.5/weather"
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
