import json
import codecs

hun = "lang/HU_HUN.json"
eng = "lang/US_EN.json"
lang = "lang/language.json"

json.load(codecs.open(lang, 'r', 'utf-8-sig'))
with open(lang, encoding='utf-8-sig') as f:
    data = json.load(f)

main_lang = data['main_lang']

if main_lang == ['hun']:
    lang = hun

if main_lang == ['eng']:
    lang = eng

json.load(codecs.open(lang, 'r', 'utf-8-sig'))
with open(lang, encoding='utf-8-sig') as f:
    langs = json.load(f)
