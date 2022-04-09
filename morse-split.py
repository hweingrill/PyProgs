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
print(morse2latin_dict)

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
    for mword in mwords:
        for mchar in mword.split():
            res += alpha[mchar]
        res += " "
    return res

def eingabe():                      # Funktion mit Rücgabewert getestet
    mtxt=input('Text eingeben - # = Ende: ')
    return mtxt

mstr=''
while mstr != "#":
    mstr = eingabe()
 #   mstr=input('Text eingeben - # = Ende: ')
    if mstr != "#":
        mstring = txt2morse(mstr, latin2morse_dict)  # (Eingabe, Dictionary)
        print(mstring)
        print(morse2txt(mstring, morse2latin_dict))

txt = "welcome to the jungle"
x = txt.split()
print(x)
txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
print(x) 
exit()

