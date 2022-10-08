import requests


class logo:
    @staticmethod
    def beta_logo():
        logo_test = "https://raw.githubusercontent.com/LexyGuru/Terminal_Windows_URI_PY/beta/beta/logo"
        response = requests.get(logo_test)
        data = response.text
        print(data)

    @staticmethod
    def lang_logo():
        logo_test = "https://raw.githubusercontent.com/LexyGuru/Terminal_Windows_URI_PY/beta/beta/logo_lang"
        response = requests.get(logo_test)
        data = response.text
        print(data)

