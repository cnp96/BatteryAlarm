from winsound import Beep
from subprocess import check_output as co
from time import sleep

while True:
    o = co(["wmic", "path", "Win32_Battery", "get", "BatteryStatus,EstimatedChargeRemaining", "/format:LIST"], shell=False).replace("\r\r\n",'').split("=")
    status, charge = o[1][0], int(o[2])

    if charge<=40 and status=='1':
        #beep alarm as running on battery below 40%
        Beep(100,500)
    elif charge>=80 and status=='2':
        #beep alarm as fully charged but ac still connected
        Beep(500,500)
    else:
        sleep(1)
