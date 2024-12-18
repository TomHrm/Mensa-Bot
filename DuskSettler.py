import requests
def get_reactions(token, chat_id, message_id):
    """
    Get the reactions to a message.

    Args:
    token (str): Telegram Bot API token.
    chat_id (str): Chat ID for the message.
    message_id (str): ID of the message to get reactions for.

    Returns:
    dict: The response from the Telegram API.
    """
    url = f"{TELEGRAM_API_BASE_URL}{token}/getPollVoters"
    payload = {
        'chat_id': chat_id,
        'message_id': message_id
    }
    response = requests.get(url, data=payload)
    return response.json()

def get_poll_results(token, chat_id, message_id):
    """
    Get the results of a poll.

    Args:
    token (str): Telegram Bot API token.
    chat_id (str): Chat ID for the poll.
    message_id (str): ID of the poll to get results for.

    Returns:
    dict: The response from the Telegram API.
    """
    url = f"{TELEGRAM_API_BASE_URL}{token}/stopPoll"
    payload = {
        'chat_id': chat_id,
        'message_id': message_id
    }
    response = requests.get(url, data=payload)
    return response.json()
