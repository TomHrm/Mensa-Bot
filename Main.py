from datetime import datetime, timedelta
import requests
import sys
import json

good_stuff = ['Burger', 'Nuggets', 'Schnitzel', 'schnitzel', "burger"]


def get_speiseplan_today():
    response = requests.get("https://mensa.mafiasi.de/api/canteens/10/today/")
    return response.json()


def get_speiseplan_tomorrow():
    response = requests.get("https://mensa.mafiasi.de/api/canteens/10/tomorrow/")
    return response.json()

def check_for_good_stuff(BOT_TOKEN, CHAT_ID):
    response = get_speiseplan_today()
    vegan = ""
    vegetarian = ""
    fav = ""
    if response:
        Header = "Der **heutige** Speiseplan " + datetime.today().strftime("%d.%m.%Y") + " ist: \n"
        send_message(Header, BOT_TOKEN, CHAT_ID)
        for meal in response:
            if [ele for ele in good_stuff if (ele in meal['dish'])]:
                fav = "⭐ "
            if meal['vegan'] == True:
                vegan = '🥦 '
            if meal['vegetarian'] == True:
                vegetarian = '🌿 '
            meal_text = '- ' + fav + vegan + vegetarian + meal['dish'] + ' ' + (meal['price']) + "€ \n\n"
            vegan = ""
            vegetarian = ""
            fav = ""
            send_message(meal_text, BOT_TOKEN, CHAT_ID)


def send_poll(BOT_TOKEN, CHAT_ID):
    """
    Send a poll to a specified Telegram chat.

    Args:
    token (str): Telegram Bot API token.
    CHAT_ID (str): Chat ID where the poll is to be sent.
    question (str): The question of the poll.
    options (list): A list of options for the poll.

    Returns:
    response: The response from the Telegram API.
    """
    url = 'https://api.telegram.org/bot' + BOT_TOKEN + '/sendPoll'
    payload = {
        'CHAT_ID': CHAT_ID,
        'question': "Wann gehen wir heute essen?",
        'options': json.dumps(["11:45", "12:00", "12:30", "13:00", "13:30"]),
        'type': 'regular',  # Change this to 'quiz' if you want to send a quiz instead of a poll
        'allows_multiple_answers': True,  # Change this to True if you want to allow multiple answers
        'is_anonymous': False  # Change this to True if you want the poll to be anonymous
    }
    response = requests.get(url, data=payload)


def send_message(bot_message, BOT_TOKEN, CHAT_ID):
    bot_token = BOT_TOKEN
    bot_chatID = CHAT_ID
    if "&" in bot_message:
        bot_message = bot_message.replace("&", "und")
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?CHAT_ID=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

def main():
    try:
        check_for_good_stuff(sys.argv[1],sys.argv[2])
        # check_for_good_stuff(token, CHAT_ID)
        send_poll(sys.argv[1],sys.argv[2])
    except UnboundLocalError:
        print("Error: Please provide a valid token and chat id")

if __name__ == '__main__':
    main()