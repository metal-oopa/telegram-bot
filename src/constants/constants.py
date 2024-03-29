ZODIAC_SIGNS = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

DAYS = ["TODAY", "TOMORROW", "YESTERDAY"]

URLS = {
    "horoscope": "https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily",
    "weather": "http://api.openweathermap.org/data/2.5/weather",
    "waifu": "https://waifu.pics/api",
    "nsfw": "https://waifu.pics/api/nsfw/waifu",
    "sfw": "https://waifu.pics/api/sfw/waifu",
    "anime_pic": "f'https://api.jikan.moe/v3",
    "anime_quote": "https://animechan.xyz/api/random",
    "reko": "https://api.reko.moe",
    "webhook": "https://telegram-bot-roan-beta.vercel.app/"
}

ERROR_MESSAGES = {
    "not_found": "not found.",
    "invalid_date": "Invalid date format. Please use YYYY-MM-DD format or TODAY, TOMORROW, YESTERDAY.",
    "invalid_sign": "Invalid zodiac sign.",
    "error": "An error occurred. Please try again later.",
}

COMMANDS = {
    "hello": "Say hello to the bot.",
    "horoscope": "Get daily horoscope for a zodiac sign.",
    "weather": "Get weather for a city.",
    "recommend <MAL USERNAME>": "Get Anime recommendations.",
    "rquote": "Get a random anime quote.",
    "aquote <ANIME>": "Get a quote from a specific anime.",
    "cquote <CHARACTER>": "Get a quote from a specific character.",
    "nsfw": "Get a nsfw waifu pic.",
    "sfw": "Get a sfw waifu pic.",
    "waifu": "Get a waifu pic with option to choose tags",
    "help": "List all commands.",
}

RESPONSES = {
    "welcome": "Howdy, how are you doing?",
    "help": "Here are the commands you can use:\n\n",
    "horoscope": "What's your zodiac sign?\nChoose one: *Aries*, *Taurus*, *Gemini*, *Cancer,* *Leo*, *Virgo*, *Libra*, *Scorpio*, *Sagittarius*, *Capricorn*, *Aquarius*, and *Pisces*.",
    "day": "What day do you want to know?\nChoose one: *TODAY*, *TOMORROW*, *YESTERDAY*, or a past date in format YYYY-MM-DD.",
    "weather": "What city do you want to know the weather for?",
    "error": "An error occurred. Please try again later.",
    "no_username": "Please provide a username after the /recommend command.",
    "no_anime": "Please provide an anime title after the /aquote command.",
    "no_character": "Please provide a character name after the /cquote command.",
    "no_argument": "Please provide the argument after the command.",
}

WAIFU_PICS_CATEGORIES = {
    'sfw': ['waifu', 'neko', 'shinobu', 'megumin', 'bully', 'cuddle', 'cry', 'hug', 'awoo', 'kiss', 'lick', 'pat',
            'smug', 'bonk', 'yeet', 'blush', 'smile', 'wave', 'highfive', 'handhold', 'nom', 'bite', 'glomp', 'slap',
            'kill', 'kick', 'happy', 'wink', 'poke', 'dance', 'cringe'],
    'nsfw': ['waifu', 'neko', 'trap', 'blowjob']
}
