import requests

url = 'https://raw.githubusercontent.com/LexyGuru/Terminal_Windows_URI_PY/beta/SVG_DIR/verzion.json'
x = requests.get(url)
h = x.json()['current']
print(h)

url = 'https://raw.githubusercontent.com/LexyGuru/Terminal_Windows_URI_PY/beta/SVG_DIR/verzion.json'
x = requests.get(url)
h = x.json()['current']


