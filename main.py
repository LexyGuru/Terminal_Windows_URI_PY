import logo
import menu_list_def
import lang
import os

ROOT_DIR = os.path.abspath(os.curdir)

"""MODUL LIST IMPORT"""
import modul.Accounts
import modul.Apps
import modul.Devices
import modul.Ease_of_Access
import modul.Extras
import modul.Gaming
import modul.Mixed_reality
import modul.Network_Internet
import modul.Personalization
import modul.Phone
import modul.Privacy
import modul.Search
import modul.System
import modul.Time_Language
import modul.Update_Security
import modul.Surface_Hub
import modul.Shell_Command
import modul.GoogMod
import verch

''' // BETA PROJECT //'''
import modul.my_script
import modul.SteamDB.GetGameServersStatus


class ANSI():
  def background(code):
    return "\33[{code}m".format(code=code)

  def style_text(code):
    return "\33[{code}m".format(code=code)

  def color_text(code):
    return "\33[{code}m".format(code=code)

def menulista():
    while True:
        menu_list_def.clear()
        logo.logos.main_logo()
        verch.verzion.ver_ch('self')
        verch.verzion.ver_ch_beta('self')

        example_ansi = ANSI.background(2) + ANSI.color_text(49) + ANSI.style_text(39) + ""
        print(example_ansi)
        menu_list_def.menu_listaA()
        menu_list_def.exits_text()

        system_lista = int(input("" + lang.language.langs["main"][6]))

        if system_lista == 0:
            modul.System.systems()
        if system_lista == 1:
            modul.Devices.devices()
        if system_lista == 2:
            modul.Phone.phone()
        if system_lista == 3:
            modul.Network_Internet.networks()
        if system_lista == 4:
            modul.Personalization.personalization()
        if system_lista == 5:
            modul.Apps.apps()
        if system_lista == 6:
            modul.Accounts.accounts()
        if system_lista == 7:
            modul.Time_Language.time_language()
        if system_lista == 8:
            modul.Gaming.gaming()
        if system_lista == 9:
            modul.Extras.extra()
        if system_lista == 10:
            modul.Ease_of_Access.ease_of_access()
        if system_lista == 11:
            modul.Search.search()
        if system_lista == 12:
            modul.Privacy.privacy()
        if system_lista == 13:
            modul.Update_Security.update()
        if system_lista == 14:
            modul.Mixed_reality.mixed_reality()
        if system_lista == 15:
            modul.Surface_Hub.surface_hub()
        if system_lista == 16:
            modul.Shell_Command.menu()
        if system_lista == 17:
            modul.GoogMod.good()

        if system_lista == 99:
            modul.my_script.beta_my_script()
        if system_lista == 98:
            modul.SteamDB.GetGameServersStatus.game.CSGOServers_730('self')

        if system_lista == 20:
            exit()

menulista()