import os
import menu_list_def
import lang
import logo

menu_list_def.clear()

def phone():
    while True:
        menu_list_def.clear()
        logo.logos.main_logo()
        menu_list_def.phone_list.phone_listA('self')
        menu_list_def.back_text()
        system_lista = int(input("" + lang.language.langs["main"][6]))

        if system_lista == 0:
            os.system("start ms-settings:mobile-devices")

        if system_lista == 1:
            os.system("start ms-settings:mobile-devices-addphone")

        if system_lista == 2:
            os.system("start ms-settings:mobile-devices-addphone-direct")

        if system_lista == 20:
            break
