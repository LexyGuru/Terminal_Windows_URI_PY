import os
import logo
import menu_list_def
import lang

menu_list_def.clear()

def surface_hub():
    while True:
        menu_list_def.clear()
        logo.logos.main_logo()
        menu_list_def.surface_hub.surface_hub_listA('self')
        menu_list_def.back_text()
        system_lista = int(input("" + lang.language.langs["main"][6]))

        if system_lista == 0:
            os.system("start ms-settings:surfacehub-accounts")
        if system_lista == 1:
            os.system("start ms-settings:surfacehub-calling")
        if system_lista == 2:
            os.system("start ms-settings:surfacehub-devicemanagenent")
        if system_lista == 3:
            os.system("start ms-settings:surfacehub-sessioncleanup")
        if system_lista == 4:
            os.system("start ms-settings:surfacehub-welcome")
        if system_lista == 20:
            break