import os
import subprocess
import lang
import logo
import menu_list_def

menu_list_def.clear()

ROOT_DIR = os.path.abspath(os.curdir)

start = ROOT_DIR + "winscript/godm.ps1"
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
                    print(lang.language.langs["manual_power"][0])
                    print(lang.language.langs["manual_power"][1])
                    menu_list_def.back_text()

                    jdoe = os.system("cmd.exe /c chcp 65001 > nul & powercfg /list")
                    print(jdoe)

                    system_lista = input("" + lang.language.langs["main"][9])

                    os.system("powercfg /setactive " + system_lista)

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
                    os.system('winget search --query ""')

                if system_lista == 1:
                    os.system("winget list")

                if system_lista == 2:
                    os.system("winget upgrade --all")

                if system_lista == 3:
                    os.system("winget import " + C_DIR_IN)

                if system_lista == 4:
                    os.system("winget export " + C_DIR_EX)

                if system_lista == 5:
                    os.system('winget search --query ""')
                    system_lista = input("" + lang.language.langs["main"][9])
                    os.system("winget install " + system_lista)


                if system_lista == 6:
                    os.system("winget list")
                    system_lista = input("" + lang.language.langs["main"][9])
                    os.system("winget uninstall " + system_lista)

                if system_lista == 20:
                    break

        if system_lista == 20:
            break
