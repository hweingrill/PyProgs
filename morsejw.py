#!/usr/bin/env python
latin2morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
                    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '...--',
                    '3': '...--', '4': '....-', '5': '.....', '6': '-....',
                    '7': '--...', '8': '---..', '9': '----.', '0': '-----',
                    ',': '--..--', '.': '.-.-.-', '?': '..--..', ';': '-.-.-',
                    ':': '---...', '/': '-..-.', '-': '-....-', '\'': '.----.',
                    '(': '-.--.-', ')': '-.--.-', '[': '-.--.-', ']': '-.--.-',
                    '{': '-.--.-', '}': '-.--.-', '_': '..--.-'}
# umdrehen key -> value für Rückübersetzung
morse2latin_dict = dict(zip(latin2morse_dict.values(),
                            latin2morse_dict.keys()))
print(morse2latin_dict)

def txt2morse(txt, alpha):
    morse_code = ''
    for char in txt.upper():
        if char == ' ':
            morse_code += '   '
        else:
            morse_code += alpha[char] + ' '
    return morse_code

def morse2txt(txt, alpha):
    res = ''
    mwords = txt.split('   ')
    for mw in mwords:
        for mx in mw.split():  # morse_code einzeln
            res += alpha[mx]  # aus dict alpha lt. mx holen
        res += ' '  # wort fertig dann space
    return res


def ifexist(txt, alpha):  # Funktion ob key vorhanden
    # die Funktion ifexist wäre eigentlich besser als Teil von txt2morse aufgehoben
    # y das erste mal definieren
    y = ' '
    for char in txt.upper():
        y = char
        if char != ' ':
            # tof = (char in alpha.keys()) wird nur ein einziges Mal in der nächsten Zeile benötigt
            if char in alpha.keys():
                y = ' '
            else:
                break
    return y


def main():                     # starte Endlosschleife
    while True:
        mstr = input('Text eingeben (leer = Ende): ')
        if mstr == '' or mstr == ' ':
            break
        y = ifexist(mstr, latin2morse_dict)
        if y == ' ':
            mstring = txt2morse(mstr, latin2morse_dict)  # (Eingabe, Dictionary)
            print(mstring)
            mstring = (morse2txt(mstring, morse2latin_dict))  # (Ausgabe, Dictionary)
            print('Eingabe: ', mstr, ' Rückübersetzung: ', mstring)
        else:
            print('kein Morsezeichen für : ', y)


# ----- body --------------------- body -------------------- body --#


# in Python kommt man eigentlich gut ohne globale Variablen aus
if __name__ == '__main__':
    # die try...except Abfrage macht hier durchaus Sinn, so kann man das Programm auch mit ^C abbrechen
    try:
        main()
    except KeyboardInterrupt:
        pass

# exit() wäre hier redundant
