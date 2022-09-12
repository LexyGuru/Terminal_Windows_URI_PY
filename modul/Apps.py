import os
import logo
import menu_list_def
import lang

menu_list_def.clear()

def apps():
    while True:
        menu_list_def.clear()
        logo.logos.main_logo()
        menu_list_def.apps_list.apps_listA('self')
        menu_list_def.back_text()
        system_lista = int(input("" + lang.language.langs["main"][6]))

        if system_lista == 0:
            while True:
                menu_list_def.clear()
                logo.logos.main_logo()
                menu_list_def.apps_list.menu_apps_list('self')
                menu_list_def.back_text()
                apps_lista = int(input("" + lang.language.langs["main"][6]))

                if apps_lista == 0:
                    os.system("start ms-settings:appsfeatures")
                if apps_lista == 1:
                    os.system("start ms-settings:optionalfeatures")

                if apps_lista == 20:
                    break

        if system_lista == 1:
            os.system("start ms-settings:defaultapps")

        if system_lista == 2:
            while True:
                menu_list_def.clear()
                logo.logos.main_logo()
                menu_list_def.apps_list.menu_apps_ofline_maps_list('self')
                menu_list_def.back_text()
                ofline_lista = int(input("" + lang.language.langs["main"][6]))

                if ofline_lista == 0:
                    os.system("start ms-settings:maps")
                if ofline_lista == 1:
                    os.system("start ms-settings:maps-downloadmaps")
                if ofline_lista == 20:
                    break

        if system_lista == 3:
            os.system("start ms-settings:appsforwebsites")
        if system_lista == 4:
            os.system("start ms-settings:videoplayback")
        if system_lista == 5:
            os.system("start ms-settings:startupapps")

        if system_lista == 20:
            break