#!/usr/bin/env python3
import winsound
latin2morse_dict = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 
                    'E':'.', 'F':'..-.', 'G':'--.','H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 
                    'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 
                    'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 
                    'Y':'-.--', 'Z':'--..', '1':'.----', '2':'...--', 
                    '3':'...--', '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', '0':'-----', 
                    ',':'--..--', '.':'.-.-.-', '?':'..--..', ';':'-.-.-', 
                    ':':'---...', '/':'-..-.', '-':'-....-', '\'':'.----.', 
                    '(':'-.--.-', ')':'-.--.-', '[':'-.--.-', ']':'-.--.-', 
                    '{':'-.--.-', '}':'-.--.-', '_':'..--.-'}

#print(latin2morse_dict)

def txt2morse(txt, alpha):
    morse_code = ''
    for char in txt.upper():                    
        if char == ' ':
            morse_code += '   '
        else:
            if char in alpha.keys():            # ob Zeichen vorhanden
                morse_code += alpha[char] + ' '
            else:
                print ('kein Morsezeichen für : ', char)
                morse_code=' '
                break
    return morse_code

def morzei(mz):
    for zeich in mz:
        if zeich == "." :
            winsound.Beep(100, 200)
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

