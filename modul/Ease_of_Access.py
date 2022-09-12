import os

import menu_list_def
import lang

menu_list_def.clear()

def ease_of_access():
    while True:
        menu_list_def.clear()
        menu_list_def.ease_of_access.eace_of_access_listA('self')
        menu_list_def.back_text()
        system_lista = int(input("" + lang.language.langs["main"][6]))

        if system_lista == 0:
            os.system("start ms-settings:easeofaccess-display")
        if system_lista == 1:
            os.system("start ms-settings:easeofaccess-cursorandpointersize")
        if system_lista == 2:
            os.system("start ms-settings:easeofaccess-cursor")
        if system_lista == 3:
            os.system("start ms-settings:easeofaccess-magnifier")
        if system_lista == 4:
            os.system("start ms-settings:easeofaccess-colorfilter")
        if system_lista == 5:
            os.system("start ms-settings:easeofaccess-highcontrast")
        if system_lista == 6:
            while True:
                menu_list_def.clear()
                menu_list_def.ease_of_access.ease_of_access_narrator_list('self')
                menu_list_def.back_text()
                ease_lista = int(input("" + lang.language.langs["main"][6]))

                if ease_lista == 0:
                    os.system("start ms-settings:easeofaccess-narrator")
                if ease_lista == 0:
                    os.system("start ms-settings:easeofaccess-narrator-isautostartenabled")
                if ease_lista == 20:
                    break

        if system_lista == 7:
            os.system("start ms-settings:easeofaccess-audio")
        if system_lista == 8:
            os.system("start ms-settings:easeofaccess-closedcaptioning")
        if system_lista == 9:
            os.system("start ms-settings:easeofaccess-speechrecognition")
        if system_lista == 10:
            os.system("start ms-settings:easeofaccess-keyboard")
        if system_lista == 11:
            os.system("start ms-settings:easeofaccess-mouse")
        if system_lista == 12:
            os.system("start ms-settings:easeofaccess-eyecontrol")

        if system_lista == 20:
            break