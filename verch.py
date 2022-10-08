import requests

class ANSI():
  def background(code):
    return "\33[{code}m".format(code=code)

  def style_text(code):
    return "\33[{code}m".format(code=code)

  def color_text(code):
    return "\33[{code}m".format(code=code)

url = 'https://raw.githubusercontent.com/LexyGuru/Terminal_Windows_URI_PY/main/SVG_DIR/verzion.json'
x = requests.get(url)
current = x.json()['current'][0]

url = 'https://raw.githubusercontent.com/LexyGuru/Terminal_Windows_URI_PY/beta/SVG_DIR/verzion.json'
x = requests.get(url)
new_ver = x.json()['current'][0]

def ver_ch():
  a = current
  b = new_ver

  if b > a:
    example_ansi = ANSI.background(0) + ANSI.color_text(39) + ANSI.style_text(31) + "New ver: " + b
    print(example_ansi)

  elif a == b:
    example_ansi = ANSI.background(0) + ANSI.color_text(49) + ANSI.style_text(92) + "Not Update: " + a
    print(example_ansi)
