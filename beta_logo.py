import requests


class logo:
    @staticmethod
    def raw_logo():
        logo_test = "https://raw.githubusercontent.com/LexyGuru/Terminal_Windows_URI_PY/beta/beta/logo"
        response = requests.get(logo_test)
        data = response.text
        print(data)

logo.raw_logo()
