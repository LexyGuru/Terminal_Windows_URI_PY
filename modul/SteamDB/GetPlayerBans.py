import menu_list_def
import requests
import json
import os
import logo
import verch

from sty import fg, ef, rs

class ANSI():
  def background(code):
    return "\33[{code}m".format(code=code)

  def style_text(code):
    return "\33[{code}m".format(code=code)

  def color_text(code):
    return "\33[{code}m".format(code=code)

class steamDB:

    def bann_user(self):
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
                url = ("https://api.steampowered.com/ISteamUser/GetPlayerBans/v1/?key=" + keyin + "&steamids=" + steamid)
                x = requests.get(url)
                h = x.json()['players'][0]
                print(fg(255, 80, 250) +
                      "Players: " + fg(255, 10, 70) + '\n'
                      "   SteamId: " + fg(255, 180, 70) + str(h.get('SteamId')) + '\n' + fg(255, 10, 70) +
                      "   CommunityBanned: " + fg(255, 180, 70) + str(h.get('CommunityBanned')) + '\n' + fg(255, 10, 70) +
                      "   VACBanned: " + fg(255, 180, 70) + str(h.get('VACBanned')) + '\n' + fg(255, 10, 70) +
                      "   NumberOfVACBans: " + fg(255, 180, 70) + str(h.get('NumberOfVACBans')) + '\n' + fg(255, 10, 70) +
                      "   DaysSinceLastBan: " + fg(255, 180, 70) + str(h.get('DaysSinceLastBan')) + '\n' + fg(255, 10, 70) +
                      "   NumberOfGameBans: " + fg(255, 180, 70) + str(h.get('NumberOfGameBans')) + '\n' + fg(255, 10, 70) +
                      "   EconomyBan: " + fg(255, 180, 70) + str(h.get('EconomyBan')) + '\n' + fg.rs)

                system_lista = int(input("[20]: Back: "))

            if system_lista == 20:
                break