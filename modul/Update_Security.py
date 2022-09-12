import os
import logo
import menu_list_def
import lang

menu_list_def.clear()

def update():
    while True:
        menu_list_def.clear()
        logo.logos.main_logo()
        menu_list_def.update.update_listA('self')
        menu_list_def.back_text()
        system_lista = int(input("" + lang.language.langs["main"][6]))

        if system_lista == 0:
            while True:
                menu_list_def.clear()
                logo.logos.main_logo()
                menu_list_def.update.windows_menu_update_list('self')
                menu_list_def.back_text()
                update_lista = int(input("" + lang.language.langs["main"][6]))

                if update_lista == 0:
                    os.system("start ms-settings:windowsupdate")
                if update_lista == 1:
                    os.system("start ms-settings:windowsupdate-action")
                if update_lista == 2:
                    os.system("start ms-settings:windowsupdate-optionalupdates")
                if update_lista == 3:
                    os.system("start ms-settings:windowsupdate-activehours")
                if update_lista == 4:
                    os.system("start ms-settings:windowsupdate-history")
                if update_lista == 5:
                    os.system("start ms-settings:windowsupdate-restartoptions")
                if update_lista == 6:
                    os.system("start ms-settings:windowsupdate-options")

                if update_lista == 20:
                    break

        if system_lista == 1:
            os.system("start ms-settings:delivery-optimization")
        if system_lista == 2:
            while True:
                menu_list_def.clear()
                logo.logos.main_logo()
                menu_list_def.update.windows_menu_security_list('self')
                menu_list_def.back_text()
                security_lista = int(input("" + lang.language.langs["main"][6]))

                if security_lista == 0:
                    os.system("start ms-settings:windowsdefender")
                if security_lista == 1:
                    os.system("start windowsdefender:")
                if security_lista == 20:
                    break

        if system_lista == 3:
            os.system("start ms-settings:backup")
        if system_lista == 4:
            os.system("start ms-settings:troubleshoot")
        if system_lista == 5:
            os.system("start ms-settings:recovery")
        if system_lista == 6:
            os.system("start ms-settings:activation")
        if system_lista == 7:
            os.system("start ms-settings:findmydevice")
        if system_lista == 8:
            os.system("start ms-settings:developers")
        if system_lista == 9:
            os.system("start ms-settings:windowsinsider")

        if system_lista == 20:
            break