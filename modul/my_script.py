import os

import beta_logo
import lang
import menu_list_def
from subprocess import Popen, CREATE_NEW_CONSOLE

ROOT_DIR = os.path.abspath(os.curdir)
net_disabled = ROOT_DIR + "\\beta\\net_disabled.ps1"
net_enabled = ROOT_DIR + "\\beta\\net_enabled.ps1"
host_edit = ROOT_DIR + "\\beta\\hosts_edit.ps1"


def beta_my_script():
    while True:
        menu_list_def.clear()
        beta_logo.logo()
        print("----------------------------------------")
        print("              beta project              ")
        print("----------------------------------------")
        print("[ 0]: Ethernet Disabled")
        print("[ 1]: Ethernet Enabled")
        print("[ 2]: HOSTS EDIT!!!")
        menu_list_def.exits_text()
        system_lista = int(input("" + lang.language.langs["main"][6]))

        if system_lista == 0:
            Popen('powershell ' + net_disabled, creationflags=CREATE_NEW_CONSOLE)

        if system_lista == 1:
            Popen('powershell ' + net_enabled, creationflags=CREATE_NEW_CONSOLE)

        if system_lista == 2:
            Popen('powershell ' + host_edit, creationflags=CREATE_NEW_CONSOLE)

        if system_lista == 20:
            break




