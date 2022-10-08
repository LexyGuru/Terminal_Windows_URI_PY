import requests
import os
import json

ROOT_DIR = os.path.abspath(os.curdir)

class ANSI():
    def background(code):
        return "\33[{code}m".format(code=code)

    def style_text(code):
        return "\33[{code}m".format(code=code)

    def color_text(code):
        return "\33[{code}m".format(code=code)

class verzion():
    def ver_ch(self):
        with open(ROOT_DIR + '\\lang\\version.json', "r") as file:
            jsonData = json.load(file)
            current = jsonData['current'][0]

        url = 'https://raw.githubusercontent.com/LexyGuru/Terminal_Windows_URI_PY/main/SVG_DIR/verzion.json'
        x = requests.get(url)
        new_ver = x.json()['current'][0]

        a = current
        b = new_ver

        if b > a:
            example_ansi = ANSI.background(0) + ANSI.color_text(39) + ANSI.style_text(31) + "New ver: " + b
            print(example_ansi)

        elif a == b:
            example_ansi = ANSI.background(0) + ANSI.color_text(49) + ANSI.style_text(92) + "Not Update: " + a
            print(example_ansi)

    def ver_ch_beta(self):
        url = 'https://raw.githubusercontent.com/LexyGuru/Terminal_Windows_URI_PY/beta/SVG_DIR/verzion.json'
        x = requests.get(url)
        beta_ver = x.json()['current'][0]

        with open(ROOT_DIR + '\\lang\\version.json', "r") as file:
            jsonData = json.load(file)
            current = jsonData['current'][0]

        a = current
        b = beta_ver

        if b > a:
            example_ansi = ANSI.background(0) + ANSI.color_text(39) + ANSI.style_text(31) + "New beta ver: " + b + " github"
            print(example_ansi)

        elif a == b:
            example_ansi = ANSI.background(0) + ANSI.color_text(49) + ANSI.style_text(92) + "Not Update: " + a
            print(example_ansi)


'''print(verzion.ver_ch('self'))
print(verzion.ver_ch_beta('self'))'''
