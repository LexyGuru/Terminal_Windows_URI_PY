import os
import logo
import menu_list_def
import lang

menu_list_def.clear()

def menu():
    shell_command.shell_cmd_list_0('self')

class shell_command:
    def shell_cmd_list_0(self):
        while True:
            menu_list_def.clear()
            logo.logos.main_logo()
            menu_list_def.shell.shell_commands_list_0('self')
            menu_list_def.next_text()
            menu_list_def.back_text()
            system_lista = int(input("" + lang.language.langs["main"][6]))

            if system_lista == 0:
                os.system('explorer "shell:3D Objects"')
            if system_lista == 1:
                os.system('explorer "shell:AccountPictures"')
            if system_lista == 2:
                os.system('explorer "shell:AddNewProgramsFolder"')
            if system_lista == 3:
                os.system('explorer "shell:Administrative Tools"')
            if system_lista == 4:
                os.system('explorer "shell:AppData"')
            if system_lista == 5:
                os.system('explorer "shell:Application Shortcuts"')
            if system_lista == 6:
                os.system('explorer "shell:AppsFolder"')
            if system_lista == 7:
                os.system('explorer "shell:AppUpdatesFolder"')
            if system_lista == 8:
                os.system('explorer "shell:Cache"')
            if system_lista == 9:
                os.system('explorer "shell:Camera Roll"')
            if system_lista == 10:
                os.system('explorer "shell:CD Burning"')
            if system_lista == 11:

                shell_command.shell_cmd_list_1(self)

            if system_lista == 20:
                break

    def shell_cmd_list_1(self):
        while True:
            menu_list_def.clear()
            logo.logos.main_logo()
            menu_list_def.shell.shell_commands_list_1('self')
            menu_list_def.next_text()
            menu_list_def.back_text()
            system_lista = int(input("" + lang.language.langs["main"][6]))

            if system_lista == 0:
                os.system('explorer "shell:ChangeRemoveProgramsFolder"')
            if system_lista == 1:
                os.system('explorer "shell:Common Administrative Tools"')
            if system_lista == 2:
                os.system('explorer "shell:Common AppData"')
            if system_lista == 3:
                os.system('explorer "shell:Common Desktop"')
            if system_lista == 4:
                os.system('explorer "shell:Common Documents"')
            if system_lista == 5:
                os.system('explorer "shell:CommonDownloads"')
            if system_lista == 6:
                os.system('explorer "shell:CommonMusic"')
            if system_lista == 7:
                os.system('explorer "shell:CommonPictures"')
            if system_lista == 8:
                os.system('explorer "shell:Common Programs"')
            if system_lista == 9:
                os.system('explorer "shell:CommonRingtones"')
            if system_lista == 10:
                os.system('explorer "shell:Common Start Menu"')

            if system_lista == 11:

                shell_command.shell_cmd_list_2(self)

            if system_lista == 20:
                break
    def shell_cmd_list_2(self):
        while True:
            menu_list_def.clear()
            logo.logos.main_logo()
            menu_list_def.shell.shell_commands_list_2('self')
            menu_list_def.next_text()
            menu_list_def.back_text()
            system_lista = int(input("" + lang.language.langs["main"][6]))

            if system_lista == 0:
                os.system('explorer "shell:Common Startup"')
            if system_lista == 1:
                os.system('explorer "shell:Common Templates"')
            if system_lista == 2:
                os.system('explorer "shell:CommonVideo"')
            if system_lista == 3:
                os.system('explorer "shell:ConflictFolder"')
            if system_lista == 4:
                os.system('explorer "shell:ConnectionsFolder"')
            if system_lista == 5:
                os.system('explorer "shell:Contacts"')
            if system_lista == 6:
                os.system('explorer "shell:ControlPanelFolder"')
            if system_lista == 7:
                os.system('explorer "shell:Cookies"')
            if system_lista == 8:
                os.system('explorer "shell:Cookies\Low"')
            if system_lista == 9:
                os.system('explorer "shell:CredentialManager"')
            if system_lista == 10:
                os.system('explorer "shell:CryptoKeys"')

            if system_lista == 11:

                shell_command.shell_cmd_list_3(self)

            if system_lista == 20:
                break
    def shell_cmd_list_3(self):
        while True:
            menu_list_def.clear()
            logo.logos.main_logo()
            menu_list_def.shell.shell_commands_list_3('self')
            menu_list_def.next_text()
            menu_list_def.back_text()
            system_lista = int(input("" + lang.language.langs["main"][6]))

            if system_lista == 0:
                os.system('explorer "shell:desktop"')
            if system_lista == 1:
                os.system('explorer "shell:device Metadata Store"')
            if system_lista == 2:
                os.system('explorer "shell:documentsLibrary"')
            if system_lista == 3:
                os.system('explorer "shell:downloads"')
            if system_lista == 4:
                os.system('explorer "shell:dpapiKeys"')
            if system_lista == 5:
                os.system('explorer "shell:Favorites"')
            if system_lista == 6:
                os.system('explorer "shell:Fonts"')
            if system_lista == 7:
                os.system('explorer "shell:Games"')
            if system_lista == 8:
                os.system('explorer "shell:GameTasks"')
            if system_lista == 9:
                os.system('explorer "shell:History"')
            if system_lista == 10:
                os.system('explorer "shell:HomeGroupCurrentUserFolder"')

            if system_lista == 11:

                shell_command.shell_cmd_list_4(self)

            if system_lista == 20:
                break

    def shell_cmd_list_4(self):
        while True:
            menu_list_def.clear()
            logo.logos.main_logo()
            menu_list_def.shell.shell_commands_list_4('self')
            menu_list_def.next_text()
            menu_list_def.back_text()
            system_lista = int(input("" + lang.language.langs["main"][6]))

            if system_lista == 0:
                os.system('explorer "shell:HomeGroupFolder"')
            if system_lista == 1:
                os.system('explorer "shell:ImplicitAppShortcuts	"')
            if system_lista == 2:
                os.system('explorer "shell:InternetFolder"')
            if system_lista == 3:
                os.system('explorer "shell:Libraries"')
            if system_lista == 4:
                os.system('explorer "shell:Links"')
            if system_lista == 5:
                os.system('explorer "shell:Local AppData"')
            if system_lista == 6:
                os.system('explorer "shell:LocalAppDataLow"')
            if system_lista == 7:
                os.system('explorer "shell:LocalAppDataLow"')
            if system_lista == 8:
                os.system('explorer "shell:MyComputerFolder"')
            if system_lista == 9:
                os.system('explorer "shell:My Music"')
            if system_lista == 10:
                os.system('explorer "shell:My Pictures"')

            if system_lista == 11:

                shell_command.shell_cmd_list_5(self)

            if system_lista == 20:
                break


    def shell_cmd_list_5(self):
        while True:
            menu_list_def.clear()
            logo.logos.main_logo()
            menu_list_def.shell.shell_commands_list_5('self')
            menu_list_def.next_text()
            menu_list_def.back_text()
            system_lista = int(input("" + lang.language.langs["main"][6]))

            if system_lista == 0:
                os.system('explorer "shell:My Video"')
            if system_lista == 1:
                os.system('explorer "shell:NetHood"')
            if system_lista == 2:
                os.system('explorer "shell:NetworkPlacesFolder"')
            if system_lista == 3:
                os.system('explorer "shell:OneDrive	"')
            if system_lista == 4:
                os.system('explorer "shell:OneDriveCameraRoll"')
            if system_lista == 5:
                os.system('explorer "shell:OneDriveDocuments"')
            if system_lista == 6:
                os.system('explorer "shell:OneDriveMusic"')
            if system_lista == 7:
                os.system('explorer "shell:OneDrivePictures"')
            if system_lista == 8:
                os.system('explorer "shell:Personal"')
            if system_lista == 9:
                os.system('explorer "shell:PicturesLibrary"')
            if system_lista == 10:
                os.system('explorer "shell:PrintersFolder"')

            if system_lista == 11:

                shell_command.shell_cmd_list_6(self)

            if system_lista == 20:
                break

    def shell_cmd_list_6(self):
        while True:
            menu_list_def.clear()
            logo.logos.main_logo()
            menu_list_def.shell.shell_commands_list_6('self')
            menu_list_def.next_text()
            menu_list_def.back_text()
            system_lista = int(input("" + lang.language.langs["main"][6]))

            if system_lista == 0:
                os.system('explorer "shell:PrintHood"')
            if system_lista == 1:
                os.system('explorer "shell:Profile"')
            if system_lista == 2:
                os.system('explorer "shell:ProgramFiles"')
            if system_lista == 3:
                os.system('explorer "shell:ProgramFilesCommon"')
            if system_lista == 4:
                os.system('explorer "shell:ProgramFilesCommonX64"')
            if system_lista == 5:
                os.system('explorer "shell:ProgramFilesCommonX86"')
            if system_lista == 6:
                os.system('explorer "shell:ProgramFilesX64"')
            if system_lista == 7:
                os.system('explorer "shell:ProgramFilesX86"')
            if system_lista == 8:
                os.system('explorer "shell:Programs"')
            if system_lista == 9:
                os.system('explorer "shell:Public"')
            if system_lista == 10:
                os.system('explorer "shell:PublicAccountPictures"')

            if system_lista == 11:

                shell_command.shell_cmd_list_7(self)

            if system_lista == 20:
                break

    def shell_cmd_list_7(self):
        while True:
            menu_list_def.clear()
            logo.logos.main_logo()
            menu_list_def.shell.shell_commands_list_7('self')
            menu_list_def.next_text()
            menu_list_def.back_text()
            system_lista = int(input("" + lang.language.langs["main"][6]))

            if system_lista == 0:
                os.system('explorer "shell:PublicGameTasks"')
            if system_lista == 1:
                os.system('explorer "shell:PublicLibraries"')
            if system_lista == 2:
                os.system('explorer "shell:Quick Launch"')
            if system_lista == 3:
                os.system('explorer "shell:Recent"')
            if system_lista == 4:
                os.system('explorer "shell:RecordedTVLibrary"')
            if system_lista == 5:
                os.system('explorer "shell:RecycleBinFolder"')
            if system_lista == 6:
                os.system('explorer "shell:ResourceDir"')
            if system_lista == 7:
                os.system('explorer "shell:Ringtones"')
            if system_lista == 8:
                os.system('explorer "shell:Roamed Tile Images"')
            if system_lista == 9:
                os.system('explorer "shell:Roaming Tiles"')
            if system_lista == 10:
                os.system('explorer "shell:::{2559a1f3-21d7-11d4-bdaf-00c04f60b9f0}"')

            if system_lista == 11:

                shell_command.shell_cmd_list_8(self)

            if system_lista == 20:
                break

    def shell_cmd_list_8(self):
        while True:
            menu_list_def.clear()
            logo.logos.main_logo()
            menu_list_def.shell.shell_commands_list_8('self')
            menu_list_def.next_text()
            menu_list_def.back_text()
            system_lista = int(input("" + lang.language.langs["main"][6]))

            if system_lista == 0:
                os.system('explorer "shell:SavedGames"')
            if system_lista == 1:
                os.system('explorer "shell:Screenshots"')
            if system_lista == 2:
                os.system('explorer "shell:Searches"')
            if system_lista == 3:
                os.system('explorer "shell:SearchHistoryFolder"')
            if system_lista == 4:
                os.system('explorer "shell:SearchHomeFolder"')
            if system_lista == 5:
                os.system('explorer "shell:SearchTemplatesFolder"')
            if system_lista == 6:
                os.system('explorer "shell:SendTo"')
            if system_lista == 7:
                os.system('explorer "shell:Start Menu"')
            if system_lista == 8:
                os.system('explorer "shell:StartMenuAllPrograms"')
            if system_lista == 9:
                os.system('explorer "shell:Startup"')
            if system_lista == 10:
                os.system('explorer "shell:SyncCenterFolder"')

            if system_lista == 11:

                shell_command.shell_cmd_list_9(self)

            if system_lista == 20:
                break


    def shell_cmd_list_9(self):
        while True:
            menu_list_def.clear()
            logo.logos.main_logo()
            menu_list_def.shell.shell_commands_list_9('self')
            menu_list_def.next_text()
            menu_list_def.back_text()
            system_lista = int(input("" + lang.language.langs["main"][6]))

            if system_lista == 0:
                os.system('explorer "shell:SyncResultsFolder"')
            if system_lista == 1:
                os.system('explorer "shell:SyncSetupFolder"')
            if system_lista == 2:
                os.system('explorer "shell:System"')
            if system_lista == 3:
                os.system('explorer "shell:SystemCertificates"')
            if system_lista == 4:
                os.system('explorer "shell:SystemX86"')
            if system_lista == 5:
                os.system('explorer "shell:Templates"')
            if system_lista == 6:
                os.system('explorer "shell:ThisPCDesktopFolder"')
            if system_lista == 7:
                os.system('explorer "shell:UsersFilesFolder"')
            if system_lista == 8:
                os.system('explorer "shell:UsersFilesFolder"')
            if system_lista == 9:
                os.system('explorer "shell:UserProfiles"')
            if system_lista == 10:
                os.system('explorer "shell:UserProgramFiles"')

            if system_lista == 11:

                shell_command.shell_cmd_list_10(self)

            if system_lista == 20:
                break


    def shell_cmd_list_10(self):
        while True:
            menu_list_def.clear()
            logo.logos.main_logo()
            menu_list_def.shell.shell_commands_list_10('self')
            menu_list_def.back_to_menu_text()
            menu_list_def.back_text()
            system_lista = int(input("" + lang.language.langs["main"][6]))

            if system_lista == 0:
                os.system('explorer "shell:UserProgramFilesCommon"')
            if system_lista == 1:
                os.system('explorer "shell:UsersLibrariesFolder"')
            if system_lista == 2:
                os.system('explorer "shell:VideosLibrary"')
            if system_lista == 3:
                os.system('explorer "shell:Windows"')

            if system_lista == 11:
                from main import menulista
                menulista()


            if system_lista == 20:
                break




