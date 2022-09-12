import os
import logo
import menu_list_def
import lang
menu_list_def.clear()

def accounts():
    while True:
        menu_list_def.clear()
        logo.logos.main_logo()
        menu_list_def.accounts_list.accounts_listA('self')
        menu_list_def.back_text()
        system_lista = int(input("" + lang.language.langs["main"][6]))

        if system_lista == 0:
            os.system("start ms-settings:yourinfo")
        if system_lista == 1:
            os.system("start ms-settings:emailandaccounts")
        if system_lista == 2:
            while True:
                menu_list_def.clear()
                logo.logos.main_logo()
                menu_list_def.accounts_list.menu_accounts_sigin_list('self')
                menu_list_def.back_text()
                account_lista = int(input("" + lang.language.langs["main"][6]))

                if account_lista == 0:
                    os.system("start ms-settings:signinoptions")
                if account_lista == 1:
                    os.system("start ms-settings:signinoptions-launchfaceenrollment")
                if account_lista == 2:
                    os.system("start ms-settings:signinoptions-launchfingerprintenrollment")
                if account_lista == 3:
                    os.system("start ms-settings:signinoptions-launchsecuritykeyenrollment")
                if account_lista == 4:
                    os.system("start ms-settings:signinoptions-dynamiclock")
                if account_lista == 20:
                    break
        if system_lista == 3:
            os.system("start ms-settings:workplace")
        if system_lista == 4:
            while True:
                menu_list_def.clear()
                logo.logos.main_logo()
                menu_list_def.accounts_list.menu_accounts_family_list('self')
                menu_list_def.back_text()
                account_lista = int(input("" + lang.language.langs["main"][6]))

                if account_lista == 0:
                    os.system("start ms-settings:otherusers")
                if account_lista == 1:
                    os.system("start ms-settings:assignedaccess")
                if account_lista == 20:
                    break
        if system_lista == 5:
            os.system("start ms-settings:sync")
        if system_lista == 20:
            break

