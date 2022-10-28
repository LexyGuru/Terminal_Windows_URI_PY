import json
import codecs
import os


ROOT_DIR = os.path.abspath(os.curdir)
#-------------------------------------------------------------------
# MAIN LANG
#-------------------------------------------------------------------

hun = ROOT_DIR + "\\lang\\HU_HUN.json"
eng = ROOT_DIR + "\\lang\\US_EN.json"
lang = ROOT_DIR + "\\lang\\language.json"

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

#-------------------------------------------------------------------
# STEAMDB
#-------------------------------------------------------------------

hundb = ROOT_DIR + "\\lang\\SteamDB_HUN.json"
engdb = ROOT_DIR + "\\lang\\SteamDB_ENG.json"

langdb = ROOT_DIR + "\\lang\\language.json"

json.load(codecs.open(langdb, 'r', 'utf-8-sig'))
with open(langdb, encoding='utf-8-sig') as f:
    datadb = json.load(f)

steam_lang = datadb['steam_lang']

if steam_lang == ['hun']:
    langdb = hundb

if steam_lang == ['eng']:
    langdb = engdb

json.load(codecs.open(langdb, 'r', 'utf-8-sig'))
with open(langdb, encoding='utf-8-sig') as f:
    langdb = json.load(f)

#-------------------------------------------------------------------
# NOTEPAD
#-------------------------------------------------------------------

notepad = ROOT_DIR + "\\lang\\language.json"
notepad_lang = ROOT_DIR + "\\lang\\notepad_lang.json"

json.load(codecs.open(notepad, 'r', 'utf-8-sig'))
with open(notepad, encoding='utf-8-sig') as f:
    datadb = json.load(f)

langnote = datadb['notepad_langs']

json.load(codecs.open(notepad_lang, 'r', 'utf-8-sig'))
with open(notepad_lang, encoding='utf-8-sig') as f:
    notepad_lang = json.load(f)

if langnote == ['eng']:
 note = notepad_lang['eng']

if langnote == ['hun']:
 note = notepad_lang['hun']

if langnote == ['de']:
 note = notepad_lang['de']






