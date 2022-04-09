#!/usr/bin/env python
# Modul: Berechnung österr. Lohnsteuer
# import from lsttab .. rechlst .. bmgs .. proz

bmgs=[11000.0,7000.0,13000.0,19000.0, 30000.0, 90000.0, 0.0]  # für weiter[x]
proz=[0.0,0.20,0.35,0.42,0.48,0.50,0.55]           # Steuersatz [x]

def rechlst(brutto):
    steuer=0.0
    for x in range(0, 5):
        if brutto >= bmgs[x]:
            brutto=float(brutto)-float(bmgs[x])
            if bmgs[x] == 0.0:              # da keine Obergrenze in Stufe 5
                steuer += float(brutto)*proz[x]
            else:     
                steuer += bmgs[x]*proz[x]
        else:                               # BMG-Ende erreicht
            steuer += float(brutto)*proz[x]
            break
    return(steuer)

