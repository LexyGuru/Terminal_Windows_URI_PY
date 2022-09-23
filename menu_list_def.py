import color_def_list
import lang.language
import os
import logo


def clear():
    os.system("cls")

def next_text():
    print("")
    print(lang.language.langs['main'][2])
    print("")

def back_to_menu_text():
    print("")
    print(lang.language.langs['main'][3])
    print("")

def back_text():
    print("")
    print(lang.language.langs['main'][1])
    print("")

def extra_back_text():
    print("")
    print(lang.language.langs['main'][8])
    print("")


def exits_text():
    print("")
    print(lang.language.langs['main'][5])
    print("")


def menu_listaA():
    lista = lang.language.langs['menu_list']
    i = 0
    for i in range(0, len(lista)):
        print(lista[i])


class system_lista:

    def system_listaA(self):
        lista = lang.language.langs['menu_system']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

    def menu_system_display_list(self):
        lista = lang.language.langs['menu_system_display_list']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

    def menu_system_audio_list(self):
        lista = lang.language.langs['menu_system_audio_list']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

    def menu_system_focus_list(self):
        lista = lang.language.langs['menu_system_focus_list']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

    def menu_system_battery_list(self):
        lista = lang.language.langs['menu_system_battery_list']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

    def menu_system_storage_list(self):
        lista = lang.language.langs['menu_system_storage_list']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])


class devices_list:

    def devices_listA(self):
        lista = lang.language.langs['devices_list']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

    def menu_devices_typing_list(self):
        lista = lang.language.langs['devices_menu_typing_list']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])


class phone_list:

    def phone_listA(self):
        lista = lang.language.langs['phone_list']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])


class network_list:

    def network_listA(self):
        lista = lang.language.langs['network_list']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

    def menu_network_status_list(self):
        lista = lang.language.langs['network_menu_status_list']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

    def menu_network_wifi_list(self):
        lista = lang.language.langs['network_menu_wifi_list']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])


class personalization_list:

    def personalization_listA(self):
        lista = lang.language.langs['personalization_list']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

    def menu_start_personalization_list(self):
        lista = lang.language.langs['personalization_menu_start_list']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

class apps_list:

    def apps_listA(self):
        lista = lang.language.langs['apps_list']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

    def menu_apps_list(self):
        lista = lang.language.langs['apps_menu_apps_list']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

    def menu_apps_ofline_maps_list(self):
        lista = lang.language.langs['offline_maps_menu_apps_list']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

class accounts_list:

    def accounts_listA(self):
        lista = lang.language.langs['accounts_list']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

    def menu_accounts_sigin_list(self):
        lista = lang.language.langs['accounts_menu_sigin_list']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

    def menu_accounts_family_list(self):
        lista = lang.language.langs['accounts_menu_family_list']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])


class time_language_list:

    def time_language_listA(self):
        lista = lang.language.langs['time_language_list']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

    def menu_time_language_language_list(self):
        lista = lang.language.langs['time_language_menu_language_list']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])


class gaming_list:

    def gaming_listA(self):
        lista = lang.language.langs['gaming_list']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])


class extra_list:

    def extra_listA(self):
        lista = lang.language.langs['extras_list']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

    def menu_weather_list(self):
        lista = lang.language.langs['extras_menu_weather_list']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])


class ease_of_access:

    def eace_of_access_listA(self):
        lista = lang.language.langs['ease_of_access_list']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

    def ease_of_access_narrator_list(self):
        lista = lang.language.langs['ease_of_access_menu_narrator_list']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])


class search:

    def search_listA(self):
        lista = lang.language.langs['search_list']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

class privacy:

    def privacy_listA(self):
        lista = lang.language.langs['privacy_list']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

    def privacy_diagnostics_list(self):
        lista = lang.language.langs['privacy_menu_diagnostics_list']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])


class update:

    def update_listA(self):
        lista = lang.language.langs['update_list']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

    def windows_menu_update_list(self):
        lista = lang.language.langs['windows_menu_update_list']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

    def windows_menu_security_list(self):
        lista = lang.language.langs['windows_menu_security_list']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])


class mixed_reality:

    def mixed_reality_listA(self):
        lista = lang.language.langs['mixed_reality_list']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])


class surface_hub:

    def surface_hub_listA(self):
        lista = lang.language.langs['surface_hub_list']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

class shell:

    def shell_commands_list_0(self):
        lista = lang.language.langs['shell_commads']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

    def shell_commands_list_1(self):
        lista = lang.language.langs['shell_commads_1']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

    def shell_commands_list_2(self):
        lista = lang.language.langs['shell_commads_2']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

    def shell_commands_list_3(self):
        lista = lang.language.langs['shell_commads_3']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

    def shell_commands_list_4(self):
        lista = lang.language.langs['shell_commads_4']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

    def shell_commands_list_5(self):
        lista = lang.language.langs['shell_commads_5']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

    def shell_commands_list_6(self):
        lista = lang.language.langs['shell_commads_6']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

    def shell_commands_list_7(self):
        lista = lang.language.langs['shell_commads_7']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

    def shell_commands_list_8(self):
        lista = lang.language.langs['shell_commads_8']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

    def shell_commands_list_9(self):
        lista = lang.language.langs['shell_commads_9']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

    def shell_commands_list_10(self):
        lista = lang.language.langs['shell_commads_10']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

class goodm:

    def goodmod_listA(self):
        lista = lang.language.langs['goodmod']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

    def power_listA(self):
        lista = lang.language.langs['power_goodmod']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

    def microsoft_listA(self):
        lista = lang.language.langs['Microsoft_Store']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])