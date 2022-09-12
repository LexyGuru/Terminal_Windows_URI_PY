import os
import menu_list_def
import lang
import logo

menu_list_def.clear()

def systems():
    while True:
        menu_list_def.clear()
        logo.logos.main_logo()
        menu_list_def.system_lista.system_listaA('self')
        menu_list_def.back_text()
        system_lista = int(input("" + lang.language.langs["main"][6]))

        """Display SYSTEM LIST"""
        if system_lista == 0:
            while True:
                menu_list_def.clear()
                logo.logos.main_logo()
                menu_list_def.system_lista.menu_system_display_list('self')
                menu_list_def.back_text()
                display_lista = int(input("" + lang.language.langs["main"][6]))

                if display_lista == 0:
                    os.system("start ms-settings:display")
                if display_lista == 1:
                    os.system("start ms-settings:nightlight")
                if display_lista == 2:
                    os.system("start ms-settings:display-advanced")
                if display_lista == 3:
                    os.system("start ms-settings-connectabledevices:devicediscovery")
                if display_lista == 4:
                    os.system("start ms-settings:display-advancedgraphics")

                if display_lista == 20:
                    break

        """Sound (build 17063) SYSTEM LIST"""
        if system_lista == 1:
            while True:
                menu_list_def.clear()
                logo.logos.main_logo()
                menu_list_def.system_lista.menu_system_audio_list('self')
                menu_list_def.back_text()
                display_lista = int(input("" + lang.language.langs["main"][6]))

                if display_lista == 0:
                    os.system("start ms-settings:sound")

                if display_lista == 1:
                    os.system("start ms-settings:sound-devices")

                if display_lista == 2:
                    os.system("start ms-settings:apps-volume")

                if display_lista == 20:
                    break

        """	Notifications & actions  SYSTEM LIST"""
        if system_lista == 2:
            os.system("start ms-settings:notifications")

        """Focus assist (build 17074) SYSTEM LIST"""
        if system_lista == 3:
            while True:
                menu_list_def.clear()
                menu_list_def.system_lista.menu_system_focus_list('self')
                menu_list_def.back_text()
                display_lista = int(input("" + lang.language.langs["main"][6]))

                if display_lista == 0:
                    os.system("start ms-settings:quiethours")

                if display_lista == 1:
                    os.system("start ms-settings:quietmomentsscheduled")

                if display_lista == 2:
                    os.system("start ms-settings:quietmomentspresentation")

                if display_lista == 3:
                    os.system("start ms-settings:quietmomentsgame")

                if display_lista == 20:
                    break


        """Power & sleep SYSTEM LIST"""
        if system_lista == 4:
            os.system("start ms-settings:powersleep")

        """	Battery SYSTEM LIST"""
        if system_lista == 5:
            while True:
                menu_list_def.clear()
                menu_list_def.system_lista.menu_system_battery_list('self')
                menu_list_def.back_text()
                display_lista = int(input("" + lang.language.langs["main"][6]))

                if display_lista == 0:
                    os.system("start ms-settings:batterysaver")

                if display_lista == 1:
                    os.system("start ms-settings:batterysaver-usagedetails")

                if display_lista == 2:
                    os.system("start ms-settings:batterysaver-settings")

                if display_lista == 20:
                    break

        """Storage SYSTEM LIST"""
        if system_lista == 6:
            while True:
                menu_list_def.clear()
                menu_list_def.system_lista.menu_system_storage_list('self')
                menu_list_def.back_text()
                display_lista = int(input("" + lang.language.langs["main"][6]))

                if display_lista == 0:
                    os.system("start ms-settings:storagesense")

                if display_lista == 1:
                    os.system("start ms-settings:storagepolicies")

                if display_lista == 2:
                    os.system("start ms-settings:savelocations")

                if display_lista == 20:
                    break

        """Tablet SYSTEM LIST"""
        if system_lista == 7:
            os.system("start ms-settings:tabletmode")

        """Multitasking SYSTEM LIST"""
        if system_lista == 8:
            os.system("start ms-settings:multitasking")

        """	Projecting to this PC SYSTEM LIST"""
        if system_lista == 9:
            os.system("start ms-settings:project")

        """Shared experiences SYSTEM LIST"""
        if system_lista == 10:
            os.system("start ms-settings:crossdevice")

        """Clipboard (build 17666) SYSTEM LIST"""
        if system_lista == 11:
            os.system("start ms-settings:clipboard")

        """Remote Desktop SYSTEM LIST"""
        if system_lista == 12:
            os.system("start ms-settings:remotedesktop")

        """Device Encryption (if available) SYSTEM LIST"""
        if system_lista == 13:
            os.system("start ms-settings:deviceencryption")

        """About SYSTEM LIST"""
        if system_lista == 14:
            os.system("start ms-settings:about")

        if system_lista == 20:
            break
