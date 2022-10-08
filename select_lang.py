# starter
# language selected
import os
import beta_logo

import logo
import json

beta_logo.logo.lang_logo()

def language():

    select_language = ["0: hun", "1: eng"]
    print(select_language, "\n")

    main_set = select_language[int(input("select lang: "))]

    if main_set == select_language[0]:
        lang_sets = {
            "main_lang": [
                "hun"
            ]
        }

        json_object = json.dumps(lang_sets, indent=4)

        with open("lang/language.json", "w") as outfile:
            outfile.write(json_object)


    if main_set == select_language[1]:
        lang_sets = {
            "main_lang": [
                "eng"
            ]
        }

        json_object = json.dumps(lang_sets, indent=4)

        with open("lang/language.json", "w") as outfile:
            outfile.write(json_object)


language()