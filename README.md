# Overview

## Introduction

Oopa Genie is a all in one telegram bot. Without using any commands, it will work like chatGPT. You can talk to the bot [here](https://t.me/genie_oopa_bot).

Oopa Genie is an all-in-one Telegram bot designed to enhance your messaging experience. You can interact with the bot [directly on Telegram](https://t.me/genie_oopa_bot).

## Features
 - **Horoscope**: Get daily horoscopes based on your zodiac sign.
 - **Weather Updates**: Receive current weather information for any city.
 - **Interactive Responses**: The bot reacts to your messages dynamically.
 - **Anime Pictures**: Sends random anime images.
 - **Anime Quotes**: Get inspirational quotes from various anime characters.
 - **Anime Recommendations**: Receive personalized anime suggestions.
 - **ChatGPT Integration**: Engage in AI-driven conversations if no commands are used.

## Usage

### General Commands
 - **/start** or **/hello**
    - Initiate interaction with the bot. The bot will send a welcome message.

 - **/help**
    - Display a list of available commands and features.

### Horoscope
 - **/horoscope**
    - The bot will prompt you to enter your zodiac sign.
    - Receive your daily horoscope based on the provided sign.

### Weather
 - **/weather <city>**
    - Replace <city> with the name of the city.
    - Get the current weather information for the specified location.

### Anime Features
 - **/waifu**
    - Receive a random anime image.

 - **/rquote**
    - Get a random quote from various anime.

 - **/aquote <anime_title>**
    - Replace <anime_title> with the title of an anime.
    - Receive a quote from the specified anime.

 - **/cquote <character_name>**
    - Replace <character_name> with the name of an anime character.
    - Get a quote from the specified character.

 - **/recommend <username>**
    - Replace <username> with your MyAnimeList username.
    - Receive anime recommendations based on your watch history.

## Installation

### Prerequisites
 - **Python 3.7 or higher**
 - **Telegram Bot Token**: Obtain from BotFather on Telegram
 - **OpenAI API Key**: Sign up at OpenAI to get an API key.
 - **OpenWeatherMap API Key**: Register at OpenWeatherMap for an API key.

### Setup
1. Clone the repository:
```bash
git clone https://github.com/your-username/oopa-genie.git
cd oopa-genie
``` 

2. Create a Virtual Environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add the environment variables as in the `.env.example` file.

5. Run the bot:
```bash
python main.py
```

6. Interact with the bot on Telegram.