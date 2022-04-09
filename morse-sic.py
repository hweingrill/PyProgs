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
            print(char, 'Zeichen')
            if (latin2morse_dict.keys() != None):
                print('True')
            else:
                print('*Fals*')
            
    
def eingabe():                       # nur Test kürzer ohne def
    mtxt=input('Text eingeben (leer = Ende): ')
    tof = ifexist(mtxt, latin2morse_dict)
    print('in Eingabe')
    print('tof= ', tof)
    return mtxt
tof=''
mstr=''
y="A"
while mstr != " ":
    mstr = eingabe()
    tof = ( mstr in latin2morse_dict.keys() )
    print('tof-body: ', tof)
    if False:
        print ('nicht vorhanden')
        break
#   mstr=input('Text eingeben (leer = Ende): ')
    if mstr >= " ":
        mstring = txt2morse(mstr, latin2morse_dict)  # (Eingabe, Dictionary)
        print(mstring)
        #print(morse2txt(mstring, morse2latin_dict))
        mstring=(morse2txt(mstring, morse2latin_dict)) # (Ausgabe, Dictionary)
        print(mstring, mstr)
    else:
        break
exit()

