from datetime import datetime, timedelta
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
    Header = "Der **heutige** Speiseplan " + datetime.now().strftime("%d.%m.%Y") + " ist: \n"
    vegan = ""
    vegetarian = ""
    fav = ""
    for meal in response:
        if [ele for ele in good_stuff if (ele in meal['dish'])]:
            fav = ":star: "
        if meal['vegan'] == True:
            vegan = '[vegan] '
        if meal['vegetarian'] == True:
            vegetarian = ':herb: '
        Header = Header + '- ' + fav + vegan + vegetarian + meal['dish'] + ' ' + (meal['price']) + "€ \n\n"
        vegan = ""
        vegetarian = ""
        fav = ""
    Header = Header + "Der **morgige** Speiseplan " + str(datetime.now()+timedelta(1)) + " ist: \n"
    response2 = get_speiseplan_tomorrow()
    for meal in response2:
        if [ele for ele in good_stuff if (ele in meal['dish'])]:
            fav = ":star: "
        if meal['vegan'] == True:
            vegan = '[vegan] '
        if meal['vegetarian'] == True:
            vegetarian = ":herb: "
        Header = Header + '- ' + fav + vegan + vegetarian + meal['dish'] + ' ' + (meal['price']) + "€ \n\n"
        vegan = ""
        vegetarian = ""
        fav = ""

    if "&" in Header:
        Header = Header.replace("&", "und")
    print(Header)
    #telegram_bot_sendtext(Header, BOT_TOKEN, CHAT_ID)


def get_feedback():
    response  = requests.get("https://mensa.mafiasi.de/api/feedback/meal")

def send_feedback(meal, feedback):
    pass


if __name__ == '__main__':
    if DEBUG == True:
        check_for_good_stuff(1, 1)
    else:
        check_for_good_stuff(sys.argv[1],sys.argv[2])




    # for meal in response:
    #     if [ele for ele in good_stuff if (ele in meal['dish'])]:
    #         if DEBUG == True:
    #             print("DEBUG: tomorrow" + meal['dish'])
    #         else:
    #             if meal['canteen'] == 10:
    #                  canteen = "Ikum"
    #             telegram_bot_sendtext("Morgen gibt es " + meal['dish'] + (meal['price']) + "€ in der Mensa" + canteen, BOT_TOKEN, CHAT_ID)
