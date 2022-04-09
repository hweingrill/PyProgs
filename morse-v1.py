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
    morse_code = ""
    for char in txt.upper():
        if char == " ":
            morse_code += "   "
        else:
            morse_code += alpha[char] + " "
    return morse_code

def morse2txt(txt, alpha):
    res = ""
    mwords = txt.split("   ")
    for mw in mwords:
        for mx in mw.split():       # morse_code einzeln
            res += alpha[mx]        # aus dict alpha lt. mx holen
        res += " "                  # wort fertig dann space
    return res

def ifexist(txt, alpha):            # Funktion ob key vorhanden
    for char in txt.upper():
        if char != " ":
#            print(char, 'Zeichen')
            tof = (char in latin2morse_dict.keys())
#            print(tof, 'in ifexist')
            global y
            y=''
            if tof == False:
 #               global y
                y=char
                break
    return y   
    
def eingabe():                       # nur Test kürzer ohne def
    y=""
    mtxt=input('Text eingeben (leer = Ende): ')
    y = ifexist(mtxt, latin2morse_dict)
#    print('y in Eingabe', y)
    return mtxt

#---------------------------------------------------------- body --#
tof=''
mstr=''
y=""
while mstr != " ":
    mstr = eingabe()
    if y != '':
        print ('nicht erlaubt: ', y)
        mstr=" "
        mstring=''
#   mstr=input('Text eingeben (leer = Ende): ')
    if mstr >= " ":
        mstring = txt2morse(mstr, latin2morse_dict)  # (Eingabe, Dictionary)
        print(mstring)
        #print(morse2txt(mstring, morse2latin_dict))
        mstring=(morse2txt(mstring, morse2latin_dict)) # (Ausgabe, Dictionary)
        print(mstring, mstr)
#    else:
#        break
exit()

