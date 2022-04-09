from getpass import getpass
from colorama import init, Fore, Style
init()

print(Fore.CYAN + Style.BRIGHT + "hangman in Python" + Style.RESET_ALL)
  
erraten = []
nutzereingabe = ""
 
ratewort=getpass(prompt='zu erratendes Wort: ')
print()
fehlversuche = 5
for buchstaben in ratewort:
    if buchstaben != " ":
        fehlversuche += 1
for buchstaben in ratewort:
    erraten.append('_')
while nutzereingabe != "bye":
    for ausgabe in erraten:
        print (ausgabe, end=' ')
    print()
    print ("Sie haben noch " + (Fore.YELLOW +Style.BRIGHT + str(fehlversuche))
           + " Versuche! " + Style.RESET_ALL + "Zum Beenden geben sie \'bye' ein.")
    nutzereingabe = input("Ihr Vorschlag: ")
    x = 0
    for buchstaben in ratewort:
        if buchstaben.lower() == nutzereingabe.lower():
            print ("Treffer", (x))
            erraten[x] = buchstaben
        x += 1
    print()
    if '_' in erraten:
        print('Noch nicht gewonnen!')
        fehlversuche -= 1
        if fehlversuche  == 0:
            print(Fore.RED + Style.BRIGHT + "Schade - verloren!" + Style.RESET_ALL)
            nutzereingabe = input("weiter mt return")
            break
    else:
        print(Fore.RED + Style.BRIGHT +"Gewonnen! "+ Style.RESET_ALL +
              "Das Wort war: " + Fore.WHITE + Style.BRIGHT + ratewort + Style.RESET_ALL)
        nutzereingabe = input("weiter mt return")
        break
