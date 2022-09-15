import os

import menu_list_def
import logo
import lang

menu_list_def.clear()

def extra():
    while True:
        menu_list_def.clear()
        logo.logos.main_logo()
        menu_list_def.extra_list.extra_listA('self')
        menu_list_def.extra_back_text()
        system_lista = int(input("" + lang.language.langs["main"][6]))

        if system_lista == 0:
            os.system("start ms-settings:extras")
        if system_lista == 1:
            os.system("start ms-availablenetworks:")
        if system_lista == 2:
            os.system("start calculator:")
        if system_lista == 3:
            os.system("start outlookcal:")
        if system_lista == 4:
            os.system("start microsoft.windows.camera:")
        if system_lista == 5:
            os.system("start ms-settings-connectabledevices:devicediscovery")
        if system_lista == 6:
            os.system("start ms-clock:")
        if system_lista == 7:
            os.system("start feedback-hub:")
        if system_lista == 8:
            os.system("start mswindowsmusic:")
        if system_lista == 9:
            os.system("start outlookmail:")
        if system_lista == 10:
            os.system("start 	bingmaps:")
        if system_lista == 11:
            os.system("start 	microsoft-edge:")
        if system_lista == 12:
            os.system("start 	bingnews:")
        if system_lista == 13:
            os.system("start xboxliveapp-1297287741:")
        if system_lista == 14:
            os.system("start 	ms-windows-store:")
        if system_lista == 15:
            os.system("start mswindowsvideo:")
        if system_lista == 16:
            os.system("start 	ms-actioncenter:")
        if system_lista == 17:
            os.system("start 	ms-people:")
        if system_lista == 18:
            os.system("start 	ms-people:settings")
        if system_lista == 19:
            os.system("start 	ms-photos:")
        if system_lista == 20:
            os.system("start 	ms-settings-displays-topology:projection")
        if system_lista == 21:
            os.system("start 	ms-settings:")
        if system_lista == 22:
            os.system("start 	ms-ScreenSketch:")
        if system_lista == 23:
            os.system("start 	ms-screenclip:")
        if system_lista == 24:
            os.system("start ms-get-started:")
        if system_lista == 25:
            while True:
                menu_list_def.clear()
                logo.logos.main_logo()
                menu_list_def.extra_list.menu_weather_list('self')
                menu_list_def.back_text()
                weather_lista = int(input("" + lang.language.langs["main"][6]))

                if weather_lista == 0:
                    os.system("start bingweather:")
                if weather_lista == 1:
                    os.system("start msnweather:")
                if weather_lista == 20:
                    break

        if system_lista == 26:
            os.system("start windowsdefender:")
        if system_lista == 30:
            break