#!/usr/bin/env python
# Lohnsteuerberrechnung Österreich
from lsttab import rechlst as lstcalc
from lsttab import bmgs                 # weil hier angesprochen
#from lsttab import proz
#from lsttab import jahr

def main():
    while True:
        print('\nPensionsberechnung - Österreich!')
        print('--------------------------------')
        jahr=2021
       #proz[2]=0.325
        bet = input('Brutto: ')
        bet = bet.replace(",", ".")
        bet=float(bet)
        basis=bet*14
        svbet=bet*float(5.1)/100
        print('SV    :%9.2f' % svbet)
        bet-=svbet
        ntto=bet
        basis=bet*12
        svbet = input('Freibet:  ')
        if svbet =='' or bet == ' ':
            svbet = 0
        if svbet != 0:
            svbet = svbet.replace(",", ".")
        svbet = float(svbet)
        bet += svbet
        print('BMG   :%9.2f' % bet)
        if bet == '' or bet == ' ':
            break
        else:
            bet=float(bet)*12
            bet, Jahr=lstcalc(bet, jahr, basis)
            steuer=float(bet)
            print('Steuer:%9.2f' %(steuer/12))
            ntto-=(steuer/12)
            print('Netto :%9.2f' % ntto)
            
if __name__ == '__main__':    
    try:
        main()
    except KeyboardInterrupt:
        pass
exit()                      # für python shell
