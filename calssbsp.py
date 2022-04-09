
import clskto as cls
kontoSchwarz=cls.Konto("Schwarz",["Schwarz","Bankangestellter","Papa"],10)
konto4711=cls.Konto("Schwarz",["Schwarz","Bankangestellter","Papa"],10)
ktonum=4711
(ktonum)=cls.Konto("Bauer",["Bauer","Bankangestellter","Papa"],66.0)
ktonum=4712
print(type(ktonum))
(ktonum)=cls.Konto("Schwar",["Schwar","Bankangestellter","Papa"],55.0)
kontoBraun=cls.Konto("Braun",["Braun"],1)
print ("Anzahl der Konten  :",cls.Konto.angelegteKonten)
print ("Anzahl der Konten 2:",cls.Konto.angelegteKonten)

print (kontoSchwarz.einzahlen(1499.00))
print (ktonum.einzahlen(499.00))
print (kontoBraun.einzahlen(199.00))
print (kontoSchwarz.auszahlen(1000, "Freundin"))
print (kontoSchwarz.abfrage())
print ((ktonum).abfrage())
#ktonum=4712
print (ktonum.abfrage())
print (kontoSchwarz.auszahlen(1600, "Papa"))
print (kontoSchwarz.auszahlen(900, "Schwarz"))

print ("Anzahl der Konten 3:",cls.Konto.angelegteKonten)

kontoWeiss=cls.Konto("Weiss",["Weiss"],30.00)
print("Konto Weiss angelegt")
print (kontoWeiss.einzahlen(970.00))

print ("Anzahl der Konten  :" ,cls.Konto.angelegteKonten)

print ("Kontostand von Schwarz : ",kontoSchwarz.abfrage())
print ("Kontostand von Braun   : ",kontoBraun.abfrage())
print ("Kontostand von Weiss   : ",kontoWeiss.abfrage())

del(kontoWeiss)
print ("Anzahl der Konten  :",cls.Konto.angelegteKonten)
