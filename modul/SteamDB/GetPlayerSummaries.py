import json
import os
import webbrowser

import requests

import beta.logo_class
import logo
import menu_list_def
import verch
from colorama import Fore, Back, Style


class ANSI():
  def background(code):
    return "\33[{code}m".format(code=code)

  def style_text(code):
    return "\33[{code}m".format(code=code)

  def color_text(code):
    return "\33[{code}m".format(code=code)

def GetPlayerSummaries():
    while True:
        menu_list_def.clear()
        '''logo.logos.main_logo()'''
        beta.logo_class.logo_all.SteramDB_logo_v2()
        verch.verzion.ver_ch('self')
        verch.verzion.ver_ch_beta('self')
        example_ansi = ANSI.background(2) + ANSI.color_text(49) + ANSI.style_text(39) + ""
        print(example_ansi)

        ROOT_DIR = os.path.abspath(os.curdir)

        with open(ROOT_DIR + '\\config\\SteamDB_key.json', "r") as file:
            jsonData = json.load(file)
            keyin = jsonData['steam_key'][0]
            steamid = jsonData['steamid'][0]
            url = ("https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key=" + keyin + "&steamids=" + steamid)
            x = requests.get(url)
            h = x.json()['response']['players'][0]

            print("steamid: " + h.get('steamid'))
            print("personaname: " + h.get('personaname'))
            print("realname: " + str(h.get('realname')))
            print("profileurl: " + h.get('profileurl'))
            print("avatar: " + h.get('avatar'))
            print("avatarfull: " + h.get('avatarfull'))
            print("lastlogoff: " + str(h.get('lastlogoff')))
            print("loccountrycode: " + h.get('loccountrycode'))

            system_lista = int(input("[20]: Back: "))

        if system_lista == 20:
            break

def GetPlayerSummaries_player():
    while True:
        menu_list_def.clear()
        '''logo.logos.main_logo()'''
        beta.logo_class.logo_all.SteramDB_logo_v2()
        verch.verzion.ver_ch('self')
        verch.verzion.ver_ch_beta('self')
        example_ansi = ANSI.background(2) + ANSI.color_text(49) + ANSI.style_text(39) + ""
        print(example_ansi)

        ROOT_DIR = os.path.abspath(os.curdir)

        with open(ROOT_DIR + '\\config\\SteamDB_key.json', "r") as file:
            jsonData = json.load(file)
            keyin = jsonData['steam_key'][0]
            print("[ 0]: SteamUserFinder Web")
            print("[ 1]: SteamUser Info")
            print("[20]: Back")
            system_lista = int(input("Input: "))

            if system_lista == 0:
                webbrowser.open('https://steamcommunity.com/search/users/#text=')

            if system_lista == 1:

                menu_list_def.clear()
                beta.logo_class.logo_all.SteramDB_logo_v2()
                verch.verzion.ver_ch('self')
                verch.verzion.ver_ch_beta('self')
                example_ansi = ANSI.background(2) + ANSI.color_text(49) + ANSI.style_text(39) + ""
                print(example_ansi)

                print(50 * "-")
                print(Fore.RED + 'steamcommunity.com/profiles/', (Fore.GREEN + 'xxxxxxxxxxxxxxxxx'))
                print(Style.RESET_ALL)
                print(50 * "-")

                steamids = input("steamID64 (Dec): ")

                url = ("https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key=" + keyin + "&steamids=" + steamids )
                x = requests.get(url)
                h = x.json()['response']['players'][0]

                menu_list_def.clear()
                beta.logo_class.logo_all.SteramDB_logo_v2()
                verch.verzion.ver_ch('self')
                verch.verzion.ver_ch_beta('self')
                example_ansi = ANSI.background(2) + ANSI.color_text(49) + ANSI.style_text(39) + ""
                print(example_ansi)

                print("steamid: " + h.get('steamid'))
                print("personaname: " + h.get('personaname'))
                print("realname: " + str(h.get('realname')))
                print("profileurl: " + h.get('profileurl'))
                print("avatar: " + h.get('avatar'))
                print("avatarfull: " + h.get('avatarfull'))
                print("lastlogoff: " + str(h.get('lastlogoff')))
                print("loccountrycode: " + h.get('loccountrycode'))

                system_lista = int(input("[20]: Back: "))

            if system_lista == 20:
                break


