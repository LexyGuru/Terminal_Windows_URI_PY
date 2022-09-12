import os
import logo
import menu_list_def
import lang

menu_list_def.clear()

def personalization():
    while True:
        menu_list_def.clear()
        logo.logos.main_logo()
        menu_list_def.personalization_list.personalization_listA('self')
        menu_list_def.back_text()
        system_lista = int(input("" + lang.language.langs["main"][6]))

        if system_lista == 0:
            os.system("start ms-settings:personalization-background")
        if system_lista == 1:
            os.system("start ms-settings:colors")
        if system_lista == 2:
            os.system("start ms-settings:lockscreen")
        if system_lista == 3:
            os.system("start ms-settings:themes")
        if system_lista == 4:
            os.system("start 	ms-settings:fonts")
        if system_lista == 5:
            while True:
                menu_list_def.clear()
                logo.logos.main_logo()
                menu_list_def.personalization_list.menu_start_personalization_list('self')
                menu_list_def.back_text()
                start_lista = int(input("" + lang.language.langs["main"][6]))

                if start_lista == 0:
                    os.system("start ms-settings:personalization-start")
                if start_lista == 1:
                    os.system("start ms-settings:personalization-start-places")

                if start_lista == 20:
                    break

        if system_lista == 6:
            os.system("start ms-settings:taskbar")

        if system_lista == 20:
            break