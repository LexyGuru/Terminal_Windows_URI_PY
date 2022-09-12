import os
import logo
import menu_list_def
import lang

menu_list_def.clear()

def time_language():
    while True:
        menu_list_def.clear()
        logo.logos.main_logo()
        menu_list_def.time_language_list.time_language_listA('self')
        menu_list_def.back_text()
        system_lista = int(input("" + lang.language.langs["main"][6]))

        if system_lista == 0:
            os.system('start ms-settings:dateandtime')
        if system_lista == 1:
            os.system('start ms-settings:regionlanguage-jpnime')
        if system_lista == 2:
            os.system('start ms-settings:regionlanguage-chsime-pinyin')
        if system_lista == 5:
            os.system('start ms-settings:regionlanguage-chsime-wubi')
        if system_lista == 4:
            while True:
                menu_list_def.clear()
                logo.logos.main_logo()
                menu_list_def.time_language_list.menu_time_language_language_list('self')
                menu_list_def.back_text()
                language_lista = int(input("" + lang.language.langs["main"][6]))

                if language_lista == 0:
                    os.system('start ms-settings:regionlanguage')
                if language_lista == 1:
                    os.system('start ms-settings:regionlanguage-setdisplaylanguage')
                if language_lista == 2:
                    os.system('start ms-settings:regionlanguage-adddisplaylanguage')
                if language_lista == 20:
                    break
        if system_lista == 5:
            os.system('start ms-settings:speech')
        if system_lista == 20:
            break