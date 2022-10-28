import webbrowser
from pywinauto import Application

import beta.logo_class
import lang
import verch
import os
import menu_list_def
import steamdb_gen
import beta
import Apps.Speedtest.speedtestss



ROOT_DIR = os.path.abspath(os.curdir)
def setmenulista():
    while True:
        menu_list_def.clear()
        beta.logo_class.logo_all.main_logo_v2()
        verch.verzion.ver_ch('self')
        verch.verzion.ver_ch_beta('self')
        print("")
        print("Settings WindowsURIpy")
        print("")
        print("[ 0]: SteamDB")
        print("[ 1]: SteamDB Game Downloads")
        print("[ 2]: Language")
        print("[ 3]: Helper")
        menu_list_def.exits_text()

        menulista = int(input("" + lang.language.langs["main"][6]))


        if menulista == 0:
            webbrowser.open('https://steamcommunity.com/dev/apikey')
            webbrowser.open('https://findsteamid.com/en/home')
            app = Application().start("notepad.exe " + ROOT_DIR + "\\config\\SteamDB_key.json")

        if menulista == 1:
            steamdb_gen.steamdb_generate('self')

        if menulista == 2:
            app = Application().start("notepad.exe " + ROOT_DIR + "\\lang\\language.json")

        if menulista == 3:
            while True:
                menu_list_def.clear()
                beta.logo_class.logo_all.main_logo_v2()
                verch.verzion.ver_ch('self')
                verch.verzion.ver_ch_beta('self')
                print("")
                print("" + lang.language.langs["about"][0])
                print("" + lang.language.langs["about"][1])

                menu_list_def.exits_text()

                menulista = int(input("" + lang.language.langs["main"][6]))
                if menulista == 1:
                    Apps.Speedtest.speedtestss.speedtest.speedtest_start_save('self')
                if menulista == 2:
                    pass
                if menulista == 20:
                    break

        if menulista == 20:
            break

setmenulista()
