import os

import menu_list_def
import logo
import lang

menu_list_def.clear()

def mixed_reality():
    while True:
        menu_list_def.clear()
        logo.logos.main_logo()
        menu_list_def.mixed_reality.mixed_reality_listA('self')
        menu_list_def.back_text()
        system_lista = int(input("" + lang.language.langs["main"][6]))

        if system_lista == 0:
            os.system("start ms-settings:holographic-audio")
        if system_lista == 1:
            os.system("start ms-settings:privacy-holographic-environment")
        if system_lista == 2:
            os.system("start ms-settings:holographic-headset")
        if system_lista == 3:
            os.system("start ms-settings:holographic-management")
        if system_lista == 20:
            break