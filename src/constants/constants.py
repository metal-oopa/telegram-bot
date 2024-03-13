ZODIAC_SIGNS = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

DAYS = ["TODAY", "TOMORROW", "YESTERDAY"]

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
    "nsfw": "Get a nsfw waifu pic.",
    "sfw": "Get a sfw waifu pic.",
    "waifu": "Get a waifu pic with option to choose tags",
    "help": "List all commands.\n\n",
}

RESPONSES = {
    "welcome": "Howdy, how are you doing?",
    "help": "Here are the commands you can use:\n\n",
    "horoscope": "What's your zodiac sign?\nChoose one: *Aries*, *Taurus*, *Gemini*, *Cancer,* *Leo*, *Virgo*, *Libra*, *Scorpio*, *Sagittarius*, *Capricorn*, *Aquarius*, and *Pisces*.",
    "day": "What day do you want to know?\nChoose one: *TODAY*, *TOMORROW*, *YESTERDAY*, or a past date in format YYYY-MM-DD.",
    "weather": "What city do you want to know the weather for?",
}

WAIFU_PICS_CATEGORIES = {
    'sfw': ['waifu', 'neko', 'shinobu', 'megumin', 'bully', 'cuddle', 'cry', 'hug', 'awoo', 'kiss', 'lick', 'pat',
            'smug', 'bonk', 'yeet', 'blush', 'smile', 'wave', 'highfive', 'handhold', 'nom', 'bite', 'glomp', 'slap',
            'kill', 'kick', 'happy', 'wink', 'poke', 'dance', 'cringe'],
    'nsfw': ['waifu', 'neko', 'trap', 'blowjob']
}
