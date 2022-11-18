import requests
import json

def get_speiseplan_today():
    response = requests.get("https://mensa.mafiasi.de/api/canteens/10/today/")
    return response.json()


def get_speiseplan_tomorrow():
    response = requests.get("https://mensa.mafiasi.de/api/canteens/10/tomorrow/")
    return response.json()