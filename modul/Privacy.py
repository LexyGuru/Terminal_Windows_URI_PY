import os
import logo
import menu_list_def
import lang

menu_list_def.clear()

def privacy():
    while True:
        menu_list_def.clear()
        logo.logos.main_logo()
        menu_list_def.privacy.privacy_listA('self')
        menu_list_def.extra_back_text()
        system_lista = int(input("" + lang.language.langs["main"][6]))

        if system_lista == 0:
            os.system("start ms-settings:privacy")
        if system_lista == 1:
            os.system("start ms-settings:privacy-speech")
        if system_lista == 2:
            os.system("start ms-settings:privacy-speechtyping")
        if system_lista == 3:
            while True:
                menu_list_def.clear()
                logo.logos.main_logo()
                menu_list_def.privacy.privacy_diagnostics_list('self')
                menu_list_def.back_text()
                diagnostics_lista = int(input("" + lang.language.langs["main"][6]))

                if diagnostics_lista == 0:
                    os.system("start ms-settings:privacy-feedback")
                if diagnostics_lista == 1:
                    os.system("start ms-settings:privacy-feedback")
                if diagnostics_lista == 20:
                    break
        if system_lista == 4:
            os.system("start ms-settings:privacy-activityhistory")
        if system_lista == 5:
            os.system("start ms-settings:privacy-location")
        if system_lista == 6:
            os.system("start ms-settings:privacy-webcam")
        if system_lista == 7:
            os.system("start ms-settings:privacy-microphone")
        if system_lista == 8:
            os.system("start ms-settings:privacy-voiceactivation")
        if system_lista == 9:
            os.system("start ms-settings:privacy-notifications")
        if system_lista == 10:
            os.system("start ms-settings:privacy-accountinfo")
        if system_lista == 11:
            os.system("start ms-settings:privacy-contacts")
        if system_lista == 12:
            os.system("start ms-settings:privacy-calendar")
        if system_lista == 13:
            os.system("start ms-settings:privacy-phonecalls")
        if system_lista == 14:
            os.system("start ms-settings:privacy-callhistory")
        if system_lista == 15:
            os.system("start ms-settings:privacy-email")
        if system_lista == 16:
            os.system("start ms-settings:privacy-eyetracker")
        if system_lista == 17:
            os.system("start ms-settings:privacy-tasks")
        if system_lista == 18:
            os.system("start ms-settings:privacy-messaging")
        if system_lista == 19:
            os.system("start ms-settings:privacy-radios")
        if system_lista == 20:
            os.system("start ms-settings:privacy-customdevices")
        if system_lista == 21:
            os.system("start ms-settings:privacy-backgroundapps")
        if system_lista == 22:
            os.system("start ms-settings:privacy-appdiagnostics")
        if system_lista == 23:
            os.system("start ms-settings:privacy-automaticfiledownloads")
        if system_lista == 24:
            os.system("start ms-settings:privacy-documents")
        if system_lista == 25:
            os.system("start ms-settings:privacy-downloadsfolder")
        if system_lista == 26:
            os.system("start ms-settings:privacy-pictures")
        if system_lista == 27:
            os.system("start ms-settings:privacy-documents")
        if system_lista == 28:
            os.system("start ms-settings:privacy-broadfilesystemaccess")

        if system_lista == 30:
            break