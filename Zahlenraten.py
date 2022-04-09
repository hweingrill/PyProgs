import random
durchgang = 0
aktiv = True
ratezahl = random.randint(0,100)
print(ratezahl)
while aktiv:
    durchgang = durchgang + 1
    print()   # für Abstand (nur Optik)
    print(durchgang)
    benutzereingabe = int (input("Bitte Zahl eingeben: "))
    
    if benutzereingabe == ratezahl:
        print("Gewonnen! Die geheime Zahl ist nicht mehr geheim")
        aktiv = False
        break
    elif benutzereingabe > ratezahl:
        print("deine geratene Zahl ist zu groß")
    else:
        print("deine geratene Zahl ist zu klein")
        
    if (durchgang == 7):
        print("Schade – verloren. Einfach nochmals probieren")
        print("Es war die Zahl " + str(ratezahl))
        aktiv = False
print("Ende des Spiels")
