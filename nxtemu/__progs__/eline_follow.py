from api import *


def main():
    while 1:
        if Sensor(IN_1) < 50:
            OnRev(OUT_A, 100)
            OnFwd(OUT_B, 100)
            #Wait(80)
        elif Sensor(IN_3) < 50:
            OnRev(OUT_B, 100)
            OnFwd(OUT_A, 100)
            #Wait(80)
        else:
            OnFwd(OUT_AB, 80)
        
        ticker()#lfixed
