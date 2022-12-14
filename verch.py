import requests
import os
import json
from sty import fg, ef, rs
import lang.language

ROOT_DIR = os.path.abspath(os.curdir)
file_exists = os.path.exists('ver.json')

if file_exists == True:
    pass

if file_exists == False:
    url = 'https://raw.githubusercontent.com/LexyGuru/Terminal_Windows_URI_PY/main/SVG_DIR/verzion.json'
    x = requests.get(url)
    current = x.json()

    json_object = json.dumps(current)

    with open("ver.json", "w") as outfile:
        outfile.write(json_object)



class verzion:
    def ver_ch(self):
        url = 'https://raw.githubusercontent.com/LexyGuru/Terminal_Windows_URI_PY/main/SVG_DIR/verzion.json'
        x = requests.get(url)
        new_ver = x.json()['next_current'][0]

        with open(ROOT_DIR + '\\ver.json', "r") as file:
            jsonData = json.load(file)
            current = jsonData['current'][0]

        a = current
        b = new_ver

        if b > a:

            print(fg(255, 64, 64) + lang.language.langs["verch_lang"][1] + b + fg.rs)


        elif a == b:
            print(fg(127, 255, 0) + lang.language.langs["verch_lang"][0] + a + fg.rs)


    def ver_ch_beta(self):
        url = 'https://raw.githubusercontent.com/LexyGuru/Terminal_Windows_URI_PY/beta/SVG_DIR/verzion.json'
        x = requests.get(url)
        beta_ver = x.json()['next_beta'][0]

        url = 'https://raw.githubusercontent.com/LexyGuru/Terminal_Windows_URI_PY/beta/SVG_DIR/verzion.json'
        x = requests.get(url)
        current = x.json()['current_beta'][0]

        a = current
        b = beta_ver

        if b > a:
            print(fg(255, 64, 64) + lang.language.langs["verch_lang"][1] + b + " " + lang.language.langs["verch_lang"][2] + fg.rs)

        elif a == b:
            print(fg(127, 255, 0) + lang.language.langs["verch_lang"][3] + a + fg.rs)

