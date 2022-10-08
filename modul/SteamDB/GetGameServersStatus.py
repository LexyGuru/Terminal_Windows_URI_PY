import webbrowser
import requests

import beta_logo
import menu_list_def


class game:
    def CSGOServers_730(self):
        while True:
            menu_list_def.clear()
            beta_logo.logo.beta_logo()

            print("[ 0]: Steam Web API key")
            print("[ 1]: CS:GO Server Status")

            menu_list_def.exits_text()
            keyload = int(input("Number: "))

            if keyload == 0:
                global keyin
                webbrowser.open('https://steamcommunity.com/dev/apikey')
                keyin = input("key: ")

            if keyload == 1:
                while True:
                    menu_list_def.clear()
                    beta_logo.logo.beta_logo()
                    print("Added Api key")
                    '''keyin = input("key: ")'''
                    print("[ 0]: Services")
                    print("[ 1]: datacenters")
                    print("[ 2]: matchmaking")
                    print("[ 3]: perfectworld")
                    menu_list_def.exits_text()

                    keyload = int(input("Number: "))

                    if keyload == 0:
                        url = ("https://api.steampowered.com/ICSGOServers_730/GetGameServersStatus/v1/?key=" + keyin)
                        x = requests.get(url)
                        h = x.json()['result']['services']
                        print(h)

                    if keyload == 1:
                        url = ("https://api.steampowered.com/ICSGOServers_730/GetGameServersStatus/v1/?key=" + keyin)
                        x = requests.get(url)
                        h = x.json()['result']['datacenters']
                        print(h)

                    if keyload == 2:
                        url = ("https://api.steampowered.com/ICSGOServers_730/GetGameServersStatus/v1/?key=" + keyin)
                        x = requests.get(url)
                        h = x.json()['result']['matchmaking']
                        print(h)

                    if keyload == 3:
                        url = ("https://api.steampowered.com/ICSGOServers_730/GetGameServersStatus/v1/?key=" + keyin)
                        x = requests.get(url)
                        h = x.json()['result']['perfectworld']
                        print(h)

                    if keyload == 20:
                        break

            if keyload == 20:
                break

