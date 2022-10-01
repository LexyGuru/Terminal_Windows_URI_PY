import os

import guiprint

import lang
import logo
import menu_list_def
from subprocess import Popen, CREATE_NEW_CONSOLE

ROOT_DIR = os.path.abspath(os.curdir)
net_disabled = ROOT_DIR + "\\beta\\net_disabled.ps1"
net_enabled = ROOT_DIR + "\\beta\\net_enabled.ps1"
host_edit = ROOT_DIR + "\\beta\\hosts_edit.ps1"


def beta_my_script():
    while True:
        menu_list_def.clear()
        a = "----------------------------------------\n"
        b = "             BETA PROJECT               \n"
        c = "          WARNING NOT TESTED            \n"
        d = "----------------------------------------\n"
        guiprint.print(a + b + c + d)
        '''logo.logos.main_logo()'''
        logo_test = "https://raw.githubusercontent.com/LexyGuru/Terminal_Windows_URI_PY/main/logo.py"

        import requests
        response = requests.get(logo_test)
        data = response.text
        print(data)

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




