import os

import requests

def steamdb_generate(self):
    url = 'http://api.steampowered.com/ISteamApps/GetAppList/v2'
    x = requests.get(url)
    h = x.json()['applist']['apps']
    os.system("mkdir c:\\temp\\")
    with open(r'c:\\temp\\steamdb.txt', 'w', encoding="utf8") as fp:
        for item in h:
            # write each item on a new line
            fp.write("%s\n" % item)
            print('Done' + str(item))



