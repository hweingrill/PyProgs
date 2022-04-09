#!/usr/bin/env python
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
# umdrehen key -> value für Rückübersetzung
morse2latin_dict = dict(zip(latin2morse_dict.values(),
                            latin2morse_dict.keys()))
#print(morse2latin_dict)


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


def morse2txt(txt, alpha):
    res = ''
    mwords = txt.split('   ')
    for mw in mwords:
        for mx in mw.split():           # morse_code einzeln
            res += alpha[mx]            # aus dict alpha lt. mx holen
        res += ' '                      # wort fertig dann space
    return res

    
def main():
    while True:
        mstr=input('Text eingeben (leer = Ende): ')
        if mstr == '' or mstr == ' ':
            break
        mstring = txt2morse(mstr, latin2morse_dict)    # (Eingabe, Dictionary)
        if mstring != ' ':
            print (mstring)
            mstring=(morse2txt(mstring, morse2latin_dict)) # (Ausgabe, Dictionary)
            print('Eingabe: ', mstr, ' Rückübersetzung: ', mstring)
        
#----- body --------------------- body -------------------- body --#

if __name__ == '__main__':    
    try:
        main()
    except KeyboardInterrupt:
        pass
