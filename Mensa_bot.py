from datetime import datetime
import sys

from Api_requests import *
from telegram_bot import *
import glob

good_stuff = ['Burger', 'Nuggets', 'Schnitzel', 'schnitzel']

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
    response = get_speiseplan_today()
    Header = "Der heutige Speiseplan " + datetime.now().strftime("%d.%m.%Y") + " ist: \n"
    vegan = ""
    vegetarian = ""
    fav = ""
    for meal in response:
        if [ele for ele in good_stuff if (ele in meal['dish'])]:
            fav = "[FAVORITE]"
        if meal['vegan'] == True:
            vegan = '[vegan] '
        if meal['vegetarian'] == True:
            vegetarian = '[vegetarian] '
        Header = Header + '- ' + fav + vegan + vegetarian + meal['dish'] + ' ' + (meal['price']) + "€ \n"
        vegan = ""
        vegetarian = ""
        fav = ""
        if "&" in Header:
            Header = Header.replace("&", "und")
    telegram_bot_sendtext(Header, BOT_TOKEN, CHAT_ID)


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
