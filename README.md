[![Python Package using Conda](https://github.com/TomHrm/Mensa-Bot/actions/workflows/python-package-conda.yml/badge.svg)](https://github.com/TomHrm/Mensa-Bot/actions/workflows/python-package-conda.yml)
# MensaBot

MensaBot is a simple Python application designed to interact with a canteen's menu API and a Telegram bot. It fetches the daily menu from the canteen, checks for favorite dishes, and can send this information along with a custom poll to a specified Telegram chat.

## Features

- Fetch daily menu from a specified API.
- Check for specified favorite dishes in the menu.
- Send the menu and favorite dishes information to a Telegram chat.
- Send a custom poll to a Telegram chat.

## Requirements

- Python 3
- `requests` library

## Installation

1. Ensure Python 3 is installed on your system. If not, you can download it from [python.org](https://www.python.org/downloads/).

2. Install packages  using pip:

   ```bash
   pip install -r requirements.txt
    ```
## Usage 
1. lone the repository or download the mensa_bot.py script.
2. Run the script from the command line, providing the Telegram Bot API token and the chat ID as arguments:

   ```bash
   python mensa_bot.py <token> <chat_id>
   ```
Replace <TELEGRAM_BOT_TOKEN> with your Telegram Bot's API token and <TELEGRAM_CHAT_ID> with the ID of the chat where you want to send messages and polls.

## Configuration
To customize the list of favorite dishes, modify the FAVORITE_DISHES list in the MensaBot class:

   ```python
    FAVORITE_DISHES = ['Burger', 'Nuggets', 'Schnitzel', 'schnitzel', "burger"]
   ```


## Contributing

Contributions to MensaBot are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
