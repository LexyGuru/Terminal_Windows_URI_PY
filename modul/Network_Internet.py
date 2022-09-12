import os
import logo
import menu_list_def
import lang

menu_list_def.clear()

def networks():
    while True:
        menu_list_def.clear()
        logo.logos.main_logo()
        menu_list_def.network_list.network_listA('self')
        menu_list_def.back_text()
        system_lista = int(input("" + lang.language.langs["main"][6]))

        if system_lista == 0:
            while True:
                menu_list_def.clear()
                logo.logos.main_logo()
                menu_list_def.network_list.menu_network_status_list('self')
                menu_list_def.back_text()

                net_list = int(input("" + lang.language.langs["main"][6]))

                if net_list == 0:
                    os.system("start ms-settings:network-status")
                if net_list == 1:
                    os.system("start ms-settings:datausage")
                if net_list == 2:
                    os.system("start ms-availablenetworks:")

                if net_list == 20:
                    break

        if system_lista == 1:
            os.system("start ms-settings:network-cellular")

        if system_lista == 2:
            while True:
                menu_list_def.clear()
                logo.logos.main_logo()
                menu_list_def.network_list.menu_network_wifi_list('self')
                menu_list_def.back_text()

                wifi_list = int(input("" + lang.language.langs["main"][6]))

                if wifi_list == 0:
                    os.system("start ms-settings:network-wifi")

                if wifi_list == 1:
                    os.system("start ms-availablenetworks:")

                if wifi_list == 2:
                    os.system("start ms-settings:network-wifisettings")

                if wifi_list == 20:
                    break

        if system_lista == 3:
            os.system("start ms-settings:network-wificalling")

        if system_lista == 4:
            os.system("start ms-settings:network-ethernet")

        if system_lista == 5:
            os.system("start ms-settings:network-dialup")

        if system_lista == 6:
            os.system("start ms-settings:network-directaccess")

        if system_lista == 7:
            os.system("start ms-settings:network-vpn")

        if system_lista == 8:
            os.system("start ms-settings:network-airplanemode")

        if system_lista == 9:
            os.system("start ms-settings:network-mobilehotspot")

        if system_lista == 10:
            os.system("start ms-settings:nfctransactions")

        if system_lista == 11:
            os.system("start ms-settings:network-proxy")

        if system_lista == 20:
            break
