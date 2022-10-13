import webbrowser

import menu_list_def
import requests
import json
import os
import logo
import verch

class ANSI():
  def background(code):
    return "\33[{code}m".format(code=code)

  def style_text(code):
    return "\33[{code}m".format(code=code)

  def color_text(code):
    return "\33[{code}m".format(code=code)

class steamDB:

    def my_userid_info(self):
        while True:
            menu_list_def.clear()
            logo.logos.main_logo()
            verch.verzion.ver_ch('self')
            verch.verzion.ver_ch_beta('self')
            example_ansi = ANSI.background(2) + ANSI.color_text(49) + ANSI.style_text(39) + ""
            print(example_ansi)

            ROOT_DIR = os.path.abspath(os.curdir)

            with open(ROOT_DIR + '\\config\\SteamDB_key.json', "r") as file:
                jsonData = json.load(file)
                keyin = jsonData['steam_key'][0]
                steamid = jsonData['steamid'][0]

                url = ("https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key=" + keyin + "&steamid=" + steamid)
                x = requests.get(url)
                h = x.json()['response']['game_count']
                print("All Games in steam: " + str(h) + "\n")

                hh =x.json()['response']['games']
                for item in hh:
                    # write each item on a new line
                    print("%s" % item)

                system_lista = int(input("[20]: Back: "))

            if system_lista == 20:
                break

    def userid_info(self):
        while True:
            menu_list_def.clear()
            logo.logos.main_logo()
            verch.verzion.ver_ch('self')
            verch.verzion.ver_ch_beta('self')
            example_ansi = ANSI.background(2) + ANSI.color_text(49) + ANSI.style_text(39) + ""
            print(example_ansi)

            ROOT_DIR = os.path.abspath(os.curdir)

            with open(ROOT_DIR + '\\config\\SteamDB_key.json', "r") as file:
                jsonData = json.load(file)
                keyin = jsonData['steam_key'][0]
                webbrowser.open('https://steamcommunity.com/search/users/#text=')
                steamid = input("steamID64 (Dec): ")

                url = ("https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key=" + keyin + "&steamid=" + steamid)
                x = requests.get(url)
                h = x.json()['response']['game_count']
                print("All Games in steam: " + str(h) + "\n")

                hh =x.json()['response']['games']
                for item in hh:
                    # write each item on a new line
                    print("%s" % item)

                system_lista = int(input("[20]: Back: "))

            if system_lista == 20:
                break


'''import datetime
def convert(sec):
    td = datetime.timedelta(seconds=sec, microseconds=sec-int(sec))
    return td.days/7, (td.days/7)%7, td.seconds/3600, (td.seconds/60)%60, td.seconds%60, td.microseconds, td.microseconds/1000

seconds = 8*24*60*60 + 1665322861  # 8 days, 6 hours (21600 seconds), 27.123 seconds
w, d, h, m, s, us, ms = convert(seconds)
print('{}s / {}w {}d {}h {}m {}s {}us {}ms'.format(seconds,w,d,h,m,s,us,ms))'''