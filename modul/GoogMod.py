import os
import subprocess
from subprocess import Popen, CREATE_NEW_CONSOLE
import lang
import logo
import menu_list_def

menu_list_def.clear()

ROOT_DIR = os.path.abspath(os.curdir)

start = ROOT_DIR + "\winscript\godm.ps1"
ms_list = ROOT_DIR + "\winscript\ms_list.ps1"

win_install = ROOT_DIR + "\winscript\win_inst_list.ps1"
win_search = ROOT_DIR + "\winscript\win_sear_que_inst.ps1"
win_upgrade = ROOT_DIR + "\winscript\win_upg_all.ps1"

power_set = ROOT_DIR + "\winscript\power_set.ps1"

C_DIR_IN = "C:/TEMP/IMPORT.json"
C_DIR_EX = "C:/TEMP/EXPORT.json"


def good():
    while True:
        menu_list_def.clear()
        logo.logos.main_logo()
        menu_list_def.goodm.goodmod_listA('self')
        menu_list_def.back_text()
        system_lista = int(input("" + lang.language.langs["main"][6]))

        if system_lista == 0:
            result = subprocess.run([r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe',
                                     r'' + start], stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT, shell=True)
            print(result)



        if system_lista == 1:
            while True:
                menu_list_def.clear()
                logo.logos.main_logo()
                menu_list_def.goodm.power_listA('self')
                menu_list_def.back_text()
                system_lista = int(input("" + lang.language.langs["main"][6]))

                if system_lista == 0:
                    os.system("powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61")

                if system_lista == 1:
                    os.system("start powercfg.cpl")

                if system_lista == 2:
                    menu_list_def.clear()
                    logo.logos.main_logo()
                    menu_list_def.goodm.power_menu_listA('self')
                    menu_list_def.back_text()

                    Popen('powershell ' + power_set, creationflags=CREATE_NEW_CONSOLE)
                    system_lista = input("" + lang.language.langs["main"][9])
                    os.system("powercfg /setactive " + system_lista)

                    if system_lista == 20:
                        break

                if system_lista == 20:
                    break

        if system_lista == 2:
            while True:
                menu_list_def.clear()
                logo.logos.main_logo()
                menu_list_def.goodm.microsoft_listA('self')
                menu_list_def.back_text()
                system_lista = int(input("" + lang.language.langs["main"][6]))

                if system_lista == 0:
                    Popen('powershell ' + ms_list, creationflags=CREATE_NEW_CONSOLE)

                if system_lista == 1:
                    Popen('powershell ' + win_install, creationflags=CREATE_NEW_CONSOLE)

                if system_lista == 2:
                    Popen('powershell ' + win_upgrade, creationflags=CREATE_NEW_CONSOLE)

                if system_lista == 3:
                    os.system("winget import " + C_DIR_IN)

                if system_lista == 4:
                    os.system("winget export " + C_DIR_EX)

                if system_lista == 5:

                    Popen('powershell ' + win_search, creationflags=CREATE_NEW_CONSOLE)
                    system_lista = input("" + lang.language.langs["main"][9])
                    os.system("winget install " + system_lista)

                if system_lista == 6:
                    Popen('powershell ' + win_install, creationflags=CREATE_NEW_CONSOLE)
                    system_lista = input("" + lang.language.langs["main"][9])
                    os.system("winget uninstall " + system_lista)

                if system_lista == 20:
                    break

        if system_lista == 20:
            break
