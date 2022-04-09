import datetime
class Konto:
    angelegteKonten=0
    def __init__(self,ktonr,inhaber,kdatum,autorisiert=["Verfueger"],startkap=0):
        self.__kontonr=ktonr
        self.__inhaber=inhaber
        self.__autorisiert=autorisiert
        self.__kontostand=startkap
        self.__ktodatum=kdatum
        Konto.angelegteKonten+=1
        xl=(ktonr, inhaber, autorisiert, startkap, datum)
        print('-ini-: ', xl)
        print(self.__kontonr)
        
    def lautend(self,ktonr):
        return self.__inhaber

    def auskap(self,ktonr):
        return(self.__kontostand)
              
    def ausver(self,ktonr):
        return(self.__autorisiert)
              
    def ausinh(self,ktonr):
        return(self.__inhaber)
    
    def ausnum(self,ktonr):
        return(self.__kontonr)

    def ausdat(self,ktonr):
        return(self.__ktodatum)

    def ausnum(self,ktonr):
        return(self.__kontonr)    
today = datetime.datetime.today()
datum=f'{today:%d.%m.%Y}'
ktonum=4712
ktouse="Renate"
verf=[ktouse,"Banker","Helmut"]
kap=100
ktonum=Konto(ktonum,ktouse,datum,verf,kap)
print ("Anzahl der Konten  :",Konto.angelegteKonten)
print('Inhaber: ', ktonum.lautend(ktonum))
ktonum=4711
ktouse="Helmut"
kap=150.0
verf=[ktouse,"Banker","Renate"]
ktonum=Konto(ktonum,ktouse,datum,verf,kap)

print ("Anzahl der Konten  :",Konto.angelegteKonten)

print('Ausgabe: ', ktonum.ausnum(ktonum))
print('Ausgabe: ', ktonum.ausinh(ktonum))
print('Ausgabe: ', ktonum.ausver(ktonum))
print('Ausgabe: ', ktonum.ausdat(ktonum))
print('Ausgabe: ', ktonum.auskap(ktonum))

#print(ktonum.inhaber)
