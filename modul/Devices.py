import os
import menu_list_def
import lang
import logo

menu_list_def.clear()

def devices():
    while True:
        menu_list_def.clear()
        logo.logos.main_logo()
        menu_list_def.devices_list.devices_listA('self')
        menu_list_def.back_text()

        system_lista = int(input("" + lang.language.langs["main"][6]))

        if system_lista == 0:
            os.system("start ms-settings:bluetooth")

        if system_lista == 1:
            os.system("start ms-settings:printers")
        if system_lista == 2:
            os.system("start ms-settings:mousetouchpad")

        if system_lista == 3:
            os.system("start ms-settings:devices-touchpad")

        if system_lista == 4:
            while True:
                menu_list_def.clear()
                logo.logos.main_logo()
                menu_list_def.devices_list.menu_devices_typing_list('self')
                menu_list_def.back_text()
                typing_lista = int(input("" + lang.language.langs["main"][6]))

                if typing_lista == 0:
                    os.system("start ms-settings:typing")

                if typing_lista == 1:
                    os.system("start ms - settings:devicestyping-hwkbtextsuggestions")

                if typing_lista == 20:
                    break

        if system_lista == 5:
            os.system("start ms-settings:wheel")

        if system_lista == 6:
            os.system("start ms-settings:pen")

        if system_lista == 7:
            os.system("start ms-settings:autoplay")

        if system_lista == 8:
            os.system("start ms-settings:usb")

        if system_lista == 20:
            break