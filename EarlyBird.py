from datetime import datetime
import requests
import sys
import json

FAVORITE_DISHES = ['Burger', 'Nuggets', 'Schnitzel', 'schnitzel', "burger", 'nuggets']
API_BASE_URL = "https://mensa.mafiasi.de/api/canteens/10"
TELEGRAM_API_BASE_URL = "https://api.telegram.org/bot"

def get_menu(day):
    """
    Fetch the menu for a given day.

    Args:
    day (str): 'today' or 'tomorrow'.

    Returns:
    dict: JSON response from the API.
    """
    response = requests.get(f"{API_BASE_URL}/{day}/")
    return response.json()

def send_message(token, chat_id, message):
    """
    Send a message to a specified Telegram chat.

    Args:
    token (str): Telegram Bot API token.
    chat_id (str): Chat ID for the message.
    message (str): The message to be sent.

    Returns:
    dict: The response from the Telegram API.
    """
    url = f"{TELEGRAM_API_BASE_URL}{token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'Markdown'
    }
    response = requests.post(url, json=payload)
    return response.json()

def check_for_menu(token, chat_id):
    """
    Check today's menu and send messages to the chat.

    Args:
    token (str): Telegram Bot API token.
    chat_id (str): Chat ID for the messages.

    Returns:
    bool: True if there is a menu for today, False otherwise.
    """
    menu = get_menu("today")
    if not menu:
        return False

    header = f"Der **heutige** Speiseplan {datetime.today().strftime('%d.%m.%Y')} ist: \n"
    send_message(token, chat_id, header)

    for meal in menu:
        fav, vegan, vegetarian = "", "", ""
        if any(dish.lower() in meal['dish'].lower() for dish in FAVORITE_DISHES):
            fav = "⭐ "
            has_favorites = True
        if meal.get('vegan'):
            vegan = '🥦 '
        if meal.get('vegetarian'):
            vegetarian = '🌿 '

        meal_text = f"- {fav}{vegan}{vegetarian}{meal['dish']} {meal.get('price', 'N/A')}€ \n\n"
        send_message(token, chat_id, meal_text)

    return True

def send_poll(token, chat_id):
    """
    Send a poll to a specified Telegram chat.

    Args:
    token (str): Telegram Bot API token.
    chat_id (str): Chat ID for the poll.

    Returns:
    dict: The response from the Telegram API.
    """
    url = f"{TELEGRAM_API_BASE_URL}{token}/sendPoll"
    payload = {
        'chat_id': chat_id,
        'question': "Wann gehen wir heute essen?",
        'options': json.dumps(["Bin nicht am Ikum", "idk, maybe irgendwann",  "11:45", "12:00", "12:30", "13:00", "13:30"]),
        'allows_multiple_answers': False,
        'is_anonymous': False
    }
    response = requests.get(url, data=payload)
    return response.json()

def send_image(token, chat_id, image_url):
    """
    Send an image to a specified Telegram chat.

    Args:
    token (str): Telegram Bot API token.
    chat_id (str): Chat ID for the image.
    image_url (str): URL of the image to be sent.

    Returns:
    dict: The response from the Telegram API.
    """
    url = f"{TELEGRAM_API_BASE_URL}{token}/sendPhoto"
    payload = {
        'chat_id': chat_id,
        'photo': image_url
    }
    response = requests.get(url, data=payload)
    return response.json()

def main():
    try:
        token, chat_id = sys.argv[1], sys.argv[2]
        if check_for_menu(token, chat_id):
            send_poll(token, chat_id)
    except IndexError:
        print("Error: Please provide a valid token and chat id")

if __name__ == '__main__':
    main()
