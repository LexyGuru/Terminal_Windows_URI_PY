import os
import subprocess
import requests
import lang

from pywinauto.application import Application

class SteamDB:
    def steamdb_generate(self):
        url = 'http://api.steampowered.com/ISteamApps/GetAppList/v2'
        x = requests.get(url)
        h = x.json()['applist']['apps']

        with open(r'c:\\temp\steamdb.txt', 'w', encoding="utf8") as fp:
            for item in h:
                # write each item on a new line
                fp.write("%s\n" % item)
                print('Done' + str(item))

    def steamdb_finder_a(self):
        # string to search in file
        '''word = 'Global Offensive'''
        word = input("" + lang.language.langs["main"][6])
        with open(r'c:\\temp\steamdb.txt', 'r', encoding="utf8") as fp:
            # read all lines in a list
            lines = fp.readlines()
            for line in lines:
                # check if string present on a current line
                if line.find(word) != -1:
                    print(word, 'string exists in file')
                    print('Line Number:', lines.index(line))
                    print('Line:', line)

    def steamdb_finder_b(self):
        print("[ 0]: Hungarian")
        print("[ 1]: English")
        selected_lang = int(input("Selected: "))

        if selected_lang == 0:
            app = Application().start("notepad.exe c:\\temp\steamdb.txt")
            app.UntitledNotepad.menu_select("S&zerkesztés->Keresés")

        if selected_lang == 1:
            app = Application().start("notepad.exe c:\\temp\steamdb.txt")
            app.UntitledNotepad.menu_select("Edit->Find")


    def steam_run_game(self):
        appid = input("Added Appidd: ")
        prgm_path = ""
        if os.environ.get("PROGRAMFILES(X86)") is None:  # this case is 32bit
            prgm_path = os.environ.get("PROGRAMFILES")
        else:
            prgm_path = os.environ.get("PROGRAMFILES(X86)")

        print(prgm_path + "\Steam\steam.exe -applaunch " + appid)

        startgame = prgm_path + "\Steam\steam.exe -applaunch " + appid
        subprocess.Popen(startgame)
