'''import os
import subprocess
from subprocess import Popen, CREATE_NEW_CONSOLE'''

import lang
import logo
import menu_list_def

def beta_my_script():
    while True:
        menu_list_def.clear()
        logo.logos.main_logo()
        print("beta project ")
        menu_list_def.exits_text()

        system_lista = int(input("" + lang.language.langs["main"][6]))

        if system_lista == 0:
            pass

        if system_lista == 20:
            break




