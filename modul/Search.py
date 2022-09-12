import os
import logo
import menu_list_def
import lang

menu_list_def.clear()

def search():
    while True:
        menu_list_def.clear()
        logo.logos.main_logo()
        menu_list_def.search.search_listA('self')
        menu_list_def.back_text()
        system_lista = int(input("" + lang.language.langs["main"][6]))

        if system_lista == 0:
            os.system("start ms-settings:search-permissions")
        if system_lista == 1:
            os.system("start ms-settings:cortana-windowssearch")
        if system_lista == 20:
            break