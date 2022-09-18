
import subprocess

import lang
import logo
import menu_list_def

menu_list_def.clear()

start = "winscript/godm.ps1"

def good():
    while True:
        menu_list_def.clear()
        logo.logos.main_logo()
        print("[0]: GoodMod")
        menu_list_def.back_text()
        system_lista = int(input("" + lang.language.langs["main"][6]))

        if system_lista == 0:
            result = subprocess.run([r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe',
                                     r'' + start], stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT, shell=True)
            print(result)

        if system_lista == 20:
            break
