class Konto:
    angelegteKonten=0
    
    def __init__(self,ktonr,inhaber,autorisiert=["Verfueger"],startkap=0):
        self.__kontonr=ktonr
        self.__inhaber=inhaber
        self.__autorisiert=autorisiert
        self.__rahmen=rahmen
        self.__kontostand=startkap
        self.__datum=datum
        Konto.angelegteKonten+=1
        print(ktonr, inhaber, autorisiert, startkap)
        print(self.__kontonr)

    def __del__(self):
        Konto.angelegteKonten-=1

    def einzahlen(self,betrag):
        if (type(betrag)==float or type(betrag)==int or type(betrag)==long) and betrag>0:
            self.__kontostand +=betrag
            print ("Neuer Kontostand: ", end='')
        else:
            print ("FEHLER: Falsche Betragsangabe")
        return self.__kontostand

    def auszahlen(self,betrag,initiator):
        if not initiator in self.__autorisiert:
            print (initiator+" ist nicht berechtigt")
            print ("Neuer Kontostand: ", end='')
        elif self.__kontostand < betrag:
            print ("Es befinden sich nur noch %10.2f Euro auf dem Konto" % self.__kontostand)
        else:
            self.__kontostand -=betrag
            print ("Neuer Kontostand: ", end='')
            if self.__kontostand == 0:
                self.kontostand = 0
        return self.__kontostand
    
    def lautend(self,ktonr):
        return self.__inhaber
     
    def abfrage(self):
        if self.__kontostand == 0:
            self.__kontostand = 0.0
        return self.__kontostand

    def auskap(self,ktonr):
        return(self.__kontostand)
              
    def ausver(self,ktonr):
        return(self.__autorisiert)
              
    def ausinh(self,ktonr):
        return(self.__inhaber)
    
    def ausnum(self,ktonr):
        return(self.__kontonr)

