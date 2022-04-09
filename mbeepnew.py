#!/usr/bin/env python3
import winsound
from morse import latin2morse_dict
from morse import txt2morse
print(latin2morse_dict)


def morzei(mz):
    for zeich in mz:
        if zeich == "." :
            winsound.Beep(100, 100)
            winsound.Beep(2500, 300)
        elif zeich == "-":
            winsound.Beep(2500, 600)
        elif zeich == " ":
            winsound.Beep(100, 300)
            

def main():
    while True:
        mstr=input('Text eingeben (leer = Ende): ')
        if mstr == '' or mstr == ' ':
            break
        mstring = txt2morse(mstr, latin2morse_dict)    # (Eingabe, Dictionary)
        if mstring != ' ':
            print(mstring)
            morzei(mstring)
            
#----- body --------------------- body -------------------- body --#

if __name__ == '__main__':    
    try:
        main()
    except KeyboardInterrupt:
        pass

