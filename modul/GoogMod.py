import os
import subprocess
from subprocess import Popen, CREATE_NEW_CONSOLE
import lang
import logo
import menu_list_def

menu_list_def.clear()

ROOT_DIR = os.path.abspath(os.curdir)

start = ROOT_DIR + "\winscript\godm.ps1"
ms_list = ROOT_DIR + "\winscript\ms_list.ps1"
win_install = ROOT_DIR + "\winscript\win_inst_list.ps1"
win_search = ROOT_DIR + "\winscript\win_sear_que_inst.ps1"
win_upgrade = ROOT_DIR + "\winscript\win_upg_all.ps1"
power_set = ROOT_DIR + "\winscript\power_set.ps1"

update_powershell = ROOT_DIR + "\winscript\windows_runas_update.ps1"
update_powershell_fixer = ROOT_DIR + "\winscript\windows_runas_update_fixer.ps1"

'''***************************************************************************************'''
restart_vga_driver = ROOT_DIR + "\winscript\windows_runas_vga_driver_restart.ps1"
restart_vga_driver_start = ROOT_DIR + "\winscript\windows_runas_vga_restart_start.ps1"
restart_vga_id = "pnputil /restart-device "
vga_list = '"'
'''***************************************************************************************'''

steam_fix = ROOT_DIR + "\winscript\steam_fix_service.ps1"

C_DIR_VGA_IN = "C:/TEMP/"
C_DIR_IN = "C:/TEMP/IMPORT.json"
C_DIR_EX = "C:/TEMP/EXPORT.json"

w_scan_updates = "Update-MpSignature"
w_scan_Quick = "Start-MpScan -ScanType QuickScan"
w_scan_Full = "Start-MpScan -ScanType FullScan"


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
                    menu_list_def.goodm.power_menu_listA('self')
                    menu_list_def.back_text()

                    Popen('powershell ' + power_set, creationflags=CREATE_NEW_CONSOLE)
                    system_lista = input("" + lang.language.langs["main"][9])
                    os.system("powercfg /setactive " + system_lista)

                    if system_lista == 20:
                        break

                if system_lista == 20:
                    break

        if system_lista == 2:
            while True:
                menu_list_def.clear()
                logo.logos.main_logo()
                menu_list_def.microsoft.microsoft_listA('self')
                menu_list_def.back_text()
                system_lista = int(input("" + lang.language.langs["main"][6]))

                if system_lista == 0:
                    Popen('powershell ' + ms_list, creationflags=CREATE_NEW_CONSOLE)

                if system_lista == 1:
                    Popen('powershell ' + win_install, creationflags=CREATE_NEW_CONSOLE)

                if system_lista == 2:
                    Popen('powershell ' + win_upgrade, creationflags=CREATE_NEW_CONSOLE)

                if system_lista == 3:
                    os.system("winget import " + C_DIR_IN)

                if system_lista == 4:
                    os.system("winget export " + C_DIR_EX)

                if system_lista == 5:
                    while True:
                        menu_list_def.clear()
                        logo.logos.main_logo()
                        menu_list_def.microsoft.microsoft_install('self')
                        menu_list_def.back_text()

                        if system_lista == 0:
                            Popen('powershell ' + win_search, creationflags=CREATE_NEW_CONSOLE)

                        if system_lista == 1:
                            system_lista = input("" + lang.language.langs["main"][9])
                            os.system("winget install " + system_lista)

                        if system_lista == 20:
                            break

                if system_lista == 6:
                    while True:
                        menu_list_def.clear()
                        logo.logos.main_logo()
                        menu_list_def.microsoft.microsoft_uninstall('self')
                        menu_list_def.back_text()
                        system_lista = int(input("" + lang.language.langs["main"][6]))

                        if system_lista == 0:
                            Popen('powershell ' + win_install, creationflags=CREATE_NEW_CONSOLE)

                        if system_lista == 1:
                            system_lista = input("" + lang.language.langs["main"][9])
                            os.system("winget uninstall " + system_lista)

                        if system_lista == 20:
                            break

                if system_lista == 20:
                    break

        if system_lista == 3:
            while True:
                menu_list_def.clear()
                logo.logos.main_logo()
                menu_list_def.goodm.Update_Fixer('self')
                menu_list_def.back_text()
                system_lista = int(input("" + lang.language.langs["main"][6]))

                if system_lista == 0:
                    Popen('powershell ' + update_powershell, creationflags=CREATE_NEW_CONSOLE)

                if system_lista == 1:
                    Popen('powershell ' + update_powershell_fixer, creationflags=CREATE_NEW_CONSOLE)

                if system_lista == 2:
                    Popen('powershell ' + steam_fix, creationflags=CREATE_NEW_CONSOLE)

                if system_lista == 3:

                    Popen('powershell ' + restart_vga_driver, creationflags=CREATE_NEW_CONSOLE)
                    system_lista = input("" + lang.language.langs["main"][10])

                    ''' 
                    "x" - Create - will create a file, returns an error if the file exist 
                    "a" - Append - will create a file if the specified file does not exist
                    "w" - Write - will create a file if the specified file does not exist
                    '''

                    f = open(C_DIR_VGA_IN + "ScriptVGARestart.ps1", "w")
                    f.write(restart_vga_id + vga_list + system_lista + vga_list)
                    f.close()

                    file = restart_vga_driver_start
                    Popen('powershell ' + file)


                if system_lista == 20:
                    break

        if system_lista == 4:
            while True:
                menu_list_def.clear()
                logo.logos.main_logo()
                menu_list_def.goodm.Windows_Defender('self')
                menu_list_def.back_text()
                system_lista = int(input("" + lang.language.langs["main"][6]))

                if system_lista == 0:
                    Popen('powershell ' + w_scan_updates, creationflags=CREATE_NEW_CONSOLE)

                if system_lista == 1:
                    Popen('powershell ' + w_scan_Quick, creationflags=CREATE_NEW_CONSOLE)

                if system_lista == 2:
                    Popen('powershell ' + w_scan_Full, creationflags=CREATE_NEW_CONSOLE)

                if system_lista == 20:
                    break

        if system_lista == 20:
            break
