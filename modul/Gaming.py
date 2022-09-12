import os

import menu_list_def
import lang

menu_list_def.clear()

def gaming():
    while True:
        menu_list_def.clear()
        menu_list_def.gaming_list.gaming_listA('self')
        menu_list_def.back_text()
        system_lista = int(input("" + lang.language.langs["main"][6]))

        if system_lista == 0:
            os.system("start ms-settings:gaming-gamebar")
        if system_lista == 1:
            os.system("start ms-settings:gaming-gamedvr")
        if system_lista == 2:
            os.system("start ms-settings:gaming-gamemode")
        if system_lista == 3:
            os.system("start ms-settings:gaming-xboxnetworking")
        if system_lista == 20:
            break
