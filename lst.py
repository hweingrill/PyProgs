# Lohnsteuerberrechnung Österreich

stufe1=11000.0
stufe2=7000.0
stufe3=13000.0
stufe4=9000.0
stufe5=0.0

brutto=input("LST-Bemessung monatl.:   ")
betrag=float(brutto)*12
print('Jahresbemessung: %9.2f' % betrag)

if betrag >= 11000:
    betrag=float(betrag)-float(stufe1)
else:
    stufe1 = 0.0
    stufe2 = 0.0
    stufe3 = 0.0
    stufe4 = 0.0
    betrag = 0.0
   
if betrag >= 7000:                              # Stufe 2
    betrag = float(betrag) - float(stufe2)
else:
    stufe2 = float(betrag)
    stufe3 = 0,0
    stufe4 = 0.0
    betrag = 0.0
    
if betrag >= 13000:
    betrag = float(betrag) - float(stufe3)
else:
    stufe3 = float(betrag)
    stufe4 = 0.0
    betrag = 0.0
        
if betrag >= 9000:
    betrag = float(betrag) - float(stufe4)
    stufe5 = betrag
    
steuer  = (stufe2 * 0.20)
steuer += (stufe3 * 0.325)
steuer += (stufe4 * 0.42)
steuer += (stufe5 * 0.50)

print('Steuer jährl.  : %9.2f' % steuer)
print('Steuer monatl. : %9.2f' %(steuer/12))



