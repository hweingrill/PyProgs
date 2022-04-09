# Lohnsteuerberrechnung Österreich

bmg=[11000.0,7000.0,13000.0,9000.0, 0.0]
proz=[0.0,.20,.325,.42,.50]

x=0
for x in range(0, 4):
    print ('Bmg: %8.2f' % bmg[x], ' mit %3.0f' % (proz[x]*100),'%' )
print ('Bmg: darüber   mit %3.0f' % (proz[x + 1]*100),'%' )
        
brutto=input("LST-Bemessung monatl.: ")
betrag=float(brutto)*12
print('Jahresbemessung: %9.2f' % betrag)
steuer=0.0
for x in range(0, 5):
    if betrag >= bmg[x]:
        betrag=float(betrag)-float(bmg[x])
        if bmg[x] == 0.0:                   # keine Obergrenze in Stufe 5
            steuer += float(betrag)*proz[x]
        else:     
            steuer += bmg[x]*proz[x]
    else:                                   # BMG-Ende erreicht
        steuer += float(betrag)*proz[x]
        break
    
print('Steuer jährlich : %8.2f' % steuer)
print('Steuer monatlich: %8.2f' %(steuer/12))



