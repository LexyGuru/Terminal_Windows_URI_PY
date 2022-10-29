import psutil
import os

def checkProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;


if checkProcessRunning('main') == True:
    for process in psutil.process_iter():
        if process.name() == 'main.exe':
            process.kill()

    if os.path.exists("ver.json"):
        os.remove("ver.json")
    else:
        print("The file does not exist")

if checkProcessRunning('main') == False:
    print('No process was running')

    if os.path.exists("ver.json"):
        os.remove("ver.json")
    else:
        print("The file does not exist")



