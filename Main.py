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

def check_for_good_stuff(token, chat_id):
    response = get_speiseplan_today()
    vegan = ""
    vegetarian = ""
    fav = ""
    if response:
        Header = "Der **heutige** Speiseplan " + datetime.today().strftime("%d.%m.%Y") + " ist: \n"
        send_message(token, chat_id, Header)
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
            send_message(token, chat_id, meal_text)


def send_poll(token, chat_id):
    """
    Send a poll to a specified Telegram chat.

    Args:
    token (str): Telegram Bot API token.
    chat_id (str): Chat ID where the poll is to be sent.
    question (str): The question of the poll.
    options (list): A list of options for the poll.

    Returns:
    response: The response from the Telegram API.
    """
    chat_id = chat_id
    url = 'https://api.telegram.org/bot' + token + '/sendPoll'
    payload = {
        'chat_id': chat_id,
        'question': "Wann gehen wir heute essen?",
        'options': json.dumps(["Bin nicht am Ikum", "11:45", "12:00", "12:30", "13:00", "13:30"]),
        'allows_multiple_answers': False,  # Change this to True if you want to allow multiple answers
        'is_anonymous': False  # Change this to True if you want the poll to be anonymous
    }
    response = requests.get(url, data=payload)
    print(response.json())
    return response.json()

def send_message(token, chat_id, message):
    parse_mode = 'Markdown'
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': parse_mode
    }
    response = requests.post(url, json=payload)
    return response.json()

def main():
    try:
        check_for_good_stuff(sys.argv[1],sys.argv[2])
        send_poll(sys.argv[1],sys.argv[2])
    except UnboundLocalError:
        print("Error: Please provide a valid token and chat id")

if __name__ == '__main__':
    main()