import requests
def telegram_bot_sendtext(bot_message, BOT_TOKEN, CHAT_ID):
    bot_token = BOT_TOKEN
    bot_chatID = CHAT_ID
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()