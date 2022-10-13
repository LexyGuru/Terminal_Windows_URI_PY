import json
import os
import webbrowser

import requests
from pywinauto import Application

import beta_logo
import lang
import menu_list_def
from sty import fg, ef, rs

class game:
    @staticmethod
    def CSGOServers_730():
        while True:
            menu_list_def.clear()
            beta_logo.logos.beta_logo()
            menu_list_def.SteamDB_lang.GetGameServersStatus('self')
            menu_list_def.back_text()
            ROOT_DIR = os.path.abspath(os.curdir)
            keyload = int(input("" + lang.language.langs["main"][6]))

            if keyload == 0:
                webbrowser.open('https://steamcommunity.com/dev/apikey')
                webbrowser.open('https://steamcommunity.com/search/users/#text=')
                ROOT_DIR = os.path.abspath(os.curdir)
                confog_steam = ROOT_DIR + "\\config\\SteamDB_key.json"
                app = Application().start("notepad.exe " + confog_steam)

            if keyload == 1:
                while True:
                    menu_list_def.clear()
                    beta_logo.logos.beta_logo()
                    menu_list_def.SteamDB_lang.GetGameServersStatus_list('self')
                    menu_list_def.back_text()

                    with open(ROOT_DIR + '\\config\\SteamDB_key.json', "r") as file:
                        jsonData = json.load(file)
                    keyin = jsonData['steam_key'][0]

                    keyloadd = int(input("" + lang.language.langs["main"][6]))
                    if keyloadd == 0:
                        url = ("https://api.steampowered.com/ICSGOServers_730/GetGameServersStatus/v1/?key=" + keyin)
                        x = requests.get(url)
                        h = x.json()['result']['services']

                        print(fg(255, 80, 250) + "SessionsLogon: " + fg(255, 180, 70) + h.get('SessionsLogon') + fg.rs)
                        print(fg(255, 80, 240) + "SteamCommunity: " + fg(255, 180, 60) + h.get('SteamCommunity') + fg.rs)
                        print(fg(255, 80, 230) + "IEconItems: " + fg(255, 180, 50) + h.get('IEconItems') + fg.rs)
                        print(fg(255, 80, 220) + "Leaderboards: " + fg(255, 180, 40) + h.get('Leaderboards') + fg.rs)

                    if keyloadd == 1:
                        while True:
                            menu_list_def.clear()
                            beta_logo.logos.beta_logo()


                            url = ("https://api.steampowered.com/ICSGOServers_730/GetGameServersStatus/v1/?key=" + keyin)
                            x = requests.get(url)
                            h = x.json()['result']['datacenters']

                            dict_list_Peru = (h['Peru'])
                            dict_list_EU_West = (h['EU West'])
                            dict_list_EU_East = (h['EU East'])
                            dict_list_Poland = (h['Poland'])
                            dict_list_India_East = (h['India East'])
                            dict_list_Hong_Kong = (h['Hong Kong'])
                            dict_list_Spain = (h['Spain'])
                            dict_list_Chile = (h['Chile'])
                            dict_list_US_Southwest = (h['US Southwest'])
                            dict_list_US_Southeast = (h['US Southeast'])
                            dict_list_India = (h['India'])
                            dict_list_EU_North = (h['EU North'])
                            dict_list_Emirates = (h['Emirates'])
                            dict_list_US_Northwest = (h['US Northwest'])
                            dict_list_South_Africa = (h['South Africa'])
                            dict_list_Brazil = (h['Brazil'])
                            dict_list_US_Northeast = (h['US Northeast'])
                            dict_list_US_Northcentral = (h['US Northcentral'])
                            dict_list_Japan = (h['Japan'])
                            dict_list_Argentina = (h['Argentina'])
                            dict_list_South_Korea = (h['South Korea'])
                            dict_list_Singapore = (h['Singapore'])
                            dict_list_Australia = (h['Australia'])
                            dict_list_China_Shanghai = (h['China Shanghai'])
                            dict_list_China_Tianjin = (h['China Tianjin'])
                            dict_list_China_Guangzhou = (h['China Guangzhou'])

                            print(fg(255, 80, 250) +

                                "Peru: " + fg(255, 180, 70) +
                                "capacity: " + fg(255, 180, 70) + dict_list_Peru.get('capacity') +
                                " Load: " + fg(255, 180, 70) + dict_list_Peru.get('load') + fg.rs)

                            print(fg(255, 80, 245) +

                                "EU West: " + fg(255, 180, 70) +
                                "capacity: " + fg(255, 180, 70) + dict_list_EU_West.get('capacity') +
                                " Load: " + fg(255, 180, 70) + dict_list_EU_West.get('load') + fg.rs)

                            print(fg(255, 80, 240) +

                                "EU East: " + fg(255, 180, 70) +
                                "capacity: " + fg(255, 180, 70) + dict_list_EU_East.get('capacity') +
                                " Load: " + fg(255, 180, 70) + dict_list_EU_East.get('load') + fg.rs)

                            print(fg(255, 80, 235) +

                                "Poland: " + fg(255, 180, 70) +
                                "capacity: " + fg(255, 180, 70) + dict_list_Poland.get('capacity') +
                                " Load: " + fg(255, 180, 70) + dict_list_Poland.get('load') + fg.rs)

                            print(fg(255, 80, 230) +

                                "India East: " + fg(255, 180, 70) +
                                "capacity: " + fg(255, 180, 70) + dict_list_India_East.get('capacity') +
                                " Load: " + fg(255, 180, 70) + dict_list_India_East.get('load') + fg.rs)

                            print(fg(255, 80, 225) +

                                "Hong Kong: " + fg(255, 180, 70) +
                                "capacity: " + fg(255, 180, 70) + dict_list_Hong_Kong.get('capacity') +
                                " Load: " + fg(255, 180, 70) + dict_list_Hong_Kong.get('load') + fg.rs)

                            print(fg(255, 80, 220) +

                                "Spain: " + fg(255, 180, 70) +
                                "capacity: " + fg(255, 180, 70) + dict_list_Spain.get('capacity') +
                                " Load: " + fg(255, 180, 70) + dict_list_Spain.get('load') + fg.rs)

                            print(fg(255, 80, 215) +

                                 "Chile: " + fg(255, 180, 70) +
                                 "capacity: " + fg(255, 180, 70) + dict_list_Chile.get('capacity') +
                                " Load: " + fg(255, 180, 70) + dict_list_Chile.get('load') + fg.rs)

                            print(fg(255, 80, 210) +

                                "US Southwest: " + fg(255, 180, 70) +
                                "capacity: " + fg(255, 180, 70) + dict_list_US_Southwest.get('capacity') +
                              " Load: " + fg(255, 180, 70) + dict_list_US_Southwest.get('load') + fg.rs)

                            print(fg(255, 80, 205) +

                                "US Southeast: " + fg(255, 180, 70) +
                                "capacity: " + fg(255, 180, 70) + dict_list_US_Southeast.get('capacity') +
                                " Load: " + fg(255, 180, 70) + dict_list_US_Southeast.get('load') + fg.rs)

                            print(fg(255, 80, 200) +

                                "India: " + fg(255, 180, 70) +
                                "capacity: " + fg(255, 180, 70) + dict_list_India.get('capacity') +
                                " Load: " + fg(255, 180, 70) + dict_list_India.get('load') + fg.rs)

                            print(fg(255, 80, 195) +

                                "EU North: " + fg(255, 180, 70) +
                                "capacity: " + fg(255, 180, 70) + dict_list_EU_North.get('capacity') +
                                " Load: " + fg(255, 180, 70) + dict_list_EU_North.get('load') + fg.rs)

                            print(fg(255, 80, 190) +

                                "Emirates: " + fg(255, 180, 70) +
                                "capacity: " + fg(255, 180, 70) + dict_list_Emirates.get('capacity') +
                                " Load: " + fg(255, 180, 70) + dict_list_Emirates.get('load') + fg.rs)

                            print(fg(255, 80, 185) +

                                "US Northwest: " + fg(255, 180, 70) +
                                "capacity: " + fg(255, 180, 70) + dict_list_US_Northwest.get('capacity') +
                                " Load: " + fg(255, 180, 70) + dict_list_US_Northwest.get('load') + fg.rs)

                            print(fg(255, 80, 180) +

                                "South Africa: " + fg(255, 180, 70) +
                                "capacity: " + fg(255, 180, 70) + dict_list_South_Africa.get('capacity') +
                                " Load: " + fg(255, 180, 70) + dict_list_South_Africa.get('load') + fg.rs)

                            print(fg(255, 80, 175) +

                                "Brazil: " + fg(255, 180, 70) +
                                "capacity: " + fg(255, 180, 70) + dict_list_Brazil.get('capacity') +
                                " Load: " + fg(255, 180, 70) + dict_list_Brazil.get('load') + fg.rs)

                            print(fg(255, 80, 170) +

                                "US Northeast: " + fg(255, 180, 70) +
                                "capacity: " + fg(255, 180, 70) + dict_list_US_Northeast.get('capacity') +
                                " Load: " + fg(255, 180, 70) + dict_list_US_Northeast.get('load') + fg.rs)

                            print(fg(255, 80, 165) +

                                "US Northcentral: " + fg(255, 180, 70) +
                                "capacity: " + fg(255, 180, 70) + dict_list_US_Northcentral.get('capacity') +
                                " Load: " + fg(255, 180, 70) + dict_list_US_Northcentral.get('load') + fg.rs)

                            print(fg(255, 80, 160) +

                                "Japan: " + fg(255, 180, 70) +
                                "capacity: " + fg(255, 180, 70) + dict_list_Japan.get('capacity') +
                                " Load: " + fg(255, 180, 70) + dict_list_Japan.get('load') + fg.rs)

                            print(fg(255, 80, 155) +

                                "Argentina: " + fg(255, 180, 70) +
                                "capacity: " + fg(255, 180, 70) + dict_list_Argentina.get('capacity') +
                                " Load: " + fg(255, 180, 70) + dict_list_Argentina.get('load') + fg.rs)

                            print(fg(255, 80, 150) +

                                "South Korea: " + fg(255, 180, 70) +
                                "capacity: " + fg(255, 180, 70) + dict_list_South_Korea.get('capacity') +
                                " Load: " + fg(255, 180, 70) + dict_list_South_Korea.get('load') + fg.rs)

                            print(fg(255, 80, 145) +

                                "Singapore: " + fg(255, 180, 70) +
                                "capacity: " + fg(255, 180, 70) + dict_list_Singapore.get('capacity') +
                                " Load: " + fg(255, 180, 70) + dict_list_Singapore.get('load') + fg.rs)

                            print(fg(255, 80, 140) +

                                "Australia: " + fg(255, 180, 70) +
                                "capacity: " + fg(255, 180, 70) + dict_list_Australia.get('capacity') +
                                " Load: " + fg(255, 180, 70) + dict_list_Australia.get('load') + fg.rs)

                            print(fg(255, 80, 135) +

                                "China Shanghai: " + fg(255, 180, 70) +
                                "capacity: " + fg(255, 180, 70) + dict_list_China_Shanghai.get('capacity') +
                                " Load: " + fg(255, 180, 70) + dict_list_China_Shanghai.get('load') + fg.rs)

                            print(fg(255, 80, 130) +

                                "China Tianjin: " + fg(255, 180, 70) +
                                "capacity: " + fg(255, 180, 70) + dict_list_China_Tianjin.get('capacity') +
                                " Load: " + fg(255, 180, 70) + dict_list_China_Tianjin.get('load') + fg.rs)

                            print(fg(255, 80, 125) +

                                "China Guangzhou: " + fg(255, 180, 70) +
                                "capacity: " + fg(255, 180, 70) + dict_list_China_Guangzhou.get('capacity') +
                                " Load: " + fg(255, 180, 70) + dict_list_China_Guangzhou.get('load') + fg.rs)

                            menu_list_def.back_text()
                            keyloadd = int(input("" + lang.language.langs["main"][6]))

                            if keyloadd == 20:
                                break

                    if keyloadd == 2:
                        url = ("1https://api.steampowered.com/ICSGOServers_730/GetGameServersStatus/v1/?key=" + keyin)
                        x = requests.get(url)
                        h = x.json()['result']['matchmaking']
                        print(h)

                    if keyloadd == 3:
                        url = ("https://api.steampowered.com/ICSGOServers_730/GetGameServersStatus/v1/?key=" + keyin)
                        x = requests.get(url)
                        h = x.json()['result']['perfectworld']
                        print(h)

                    if keyloadd == 20:
                        break

            if keyload == 20:
                break

