# aus www.hdm-stuttgart.de/~maucher/Python/html/Klassen.html
import bkkonto as classbsp

def main():
#    kontoSchwarz=classbsp.Konto("Schwarz",["Schwarz","Banker","Papa"],10)
    kontoSchwarz=classbsp.Konto(ktouse,[ktouse,"Banker","Papa"],10)

    print('Inhaber: ', kontoSchwarz.lautend())
 
    mount=0.00
    x=''
    mount=(float(input('Einzahlungsbetrag: ')))
    print ((kontoSchwarz).einzahlen(mount))

    mount=(float(input('Auszahlungsbetrag Freundin: ')))
    print (kontoSchwarz.auszahlen(mount, "Freundin"))

    mount=(float(input('Auszahlungsbetrag Banker: ')))
    print (kontoSchwarz.auszahlen(mount, "Banker"))

    print ("Kontostand Schwarz: ",kontoSchwarz.abfrage())

    mount=(float(input('Auszahlungsbetrag Papa: ')))
    print (kontoSchwarz.auszahlen(mount, "Papa"))

    mount=(float(input('Auszahlungsbetrag Schwarz: ')))
    print (kontoSchwarz.auszahlen(mount, "Schwarz"))

    print ("Anzahl der Konten  :",classbsp.Konto.angelegteKonten)

    kontoWeiss=classbsp.Konto("Weiss")

    print ("Anzahl der Konten  :",classbsp.Konto.angelegteKonten)

    print ("Kontostand von Schwarz :",kontoSchwarz.abfrage())
    print ("kontostand von Weiss   :",kontoWeiss.abfrage())

    del(kontoWeiss)
    print ("Anzahl der Konten  :",classbsp.Konto.angelegteKonten)
    
ktouse=input('Kontoinhaber: ')    
if __name__ == '__main__':    
    try:
        main()
    except KeyboardInterrupt:
        pass
