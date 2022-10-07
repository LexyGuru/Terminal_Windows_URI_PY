import os
import beta_logo
import lang
import menu_list_def
from subprocess import Popen, CREATE_NEW_CONSOLE

from modul import steam_database_api

ROOT_DIR = os.path.abspath(os.curdir)
net_disabled = ROOT_DIR + "\\beta\\net_disabled.ps1"
net_enabled = ROOT_DIR + "\\beta\\net_enabled.ps1"
host_edit = ROOT_DIR + "\\beta\\hosts_edit.ps1"

steamjson = "c:\\temp\steamdb.json"


def beta_my_script():
    while True:
        menu_list_def.clear()
        beta_logo.logo.raw_logo()
        print("----------------------------------------")
        print("              beta project              ")
        print("----------------------------------------")
        print("[ 0]: Ethernet Disabled")
        print("[ 1]: Ethernet Enabled")
        print("[ 2]: HOSTS EDIT!!!")
        print("[ 3]: SteamDB finder starter")
        menu_list_def.exits_text()
        system_lista = int(input("" + lang.language.langs["main"][6]))

        if system_lista == 0:
            Popen('powershell ' + net_disabled, creationflags=CREATE_NEW_CONSOLE)

        if system_lista == 1:
            Popen('powershell ' + net_enabled, creationflags=CREATE_NEW_CONSOLE)

        if system_lista == 2:
            Popen('powershell ' + host_edit, creationflags=CREATE_NEW_CONSOLE)

        if system_lista == 3:
            while True:
                beta_logo.logo.raw_logo()
                print("")
                print("{[BETA TESTED] {[BETA TESTED]} {[BETA TESTED]}")
                print("")
                print("[ 0]: SteamDB Downloads (DOWNLOADS DATA)")
                print("[ 1]: SteamDB Finder (NO LOG FILE )")
                print("[ 2]: Run Steam Game (PL.: (CS:GO Appid:730)")
                menu_list_def.exits_text()
                system_lista = int(input("" + lang.language.langs["main"][6]))

                if system_lista == 0:
                    steam_database_api.SteamDB.steamdb_generate('self')

                if system_lista == 1:
                    steam_database_api.SteamDB.stamdb_finder('self')

                if system_lista == 2:
                    steam_database_api.SteamDB.steam_run_game('self')

                if system_lista == 20:
                    break
        if system_lista == 20:
            break




