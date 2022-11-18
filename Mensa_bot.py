import argparse
import sys

from Api_requests import *
from telegram_bot import *
import glob

good_stuff = ['Burger', 'Nuggets', 'Schnitzel']

# when sending 
DEBUG = False
def check_for_saved_meals():
    print(glob.glob("/Users/tomherrmann/Documents/GitHub/Mensa-Bot/meals"))

def create_meal(meal, cantine, price):
    meal = {
        'dish': meal,
        'canteen': cantine,
        'price': price
    }
    return meal

def check_for_good_stuff(BOT_TOKEN, CHAT_ID):
    response = get_speiseplan_tomorrow()
    reminder = get_speiseplan_today()
    for meal in reminder:
        if [ele for ele in good_stuff if (ele in meal['dish'])]:
            if DEBUG == True:
                print("DEBUG REMINDER " + meal['dish'])
            else:
                if meal['canteen'] == 10:
                    canteen = "Ikum"
                telegram_bot_sendtext("REMINDER: Heute gibt es " + meal['dish'] + (meal['price']) + "€ in der Mensa" + canteen, BOT_TOKEN, CHAT_ID)


def get_feedback():
    response  = requests.get("https://mensa.mafiasi.de/api/feedback/meal")

def send_feedback(meal, feedback):
    pass


if __name__ == '__main__':
    check_for_good_stuff(sys.argv[1],sys.argv[2])



    # for meal in response:
    #     if [ele for ele in good_stuff if (ele in meal['dish'])]:
    #         if DEBUG == True:
    #             print("DEBUG: tomorrow" + meal['dish'])
    #         else:
    #             if meal['canteen'] == 10:
    #                  canteen = "Ikum"
    #             telegram_bot_sendtext("Morgen gibt es " + meal['dish'] + (meal['price']) + "€ in der Mensa" + canteen, BOT_TOKEN, CHAT_ID)
