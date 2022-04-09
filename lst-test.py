#!/usr/bin/env python
# Lohnsteuerberrechnung Österreich mit import

from lsttab import rechlst as lstcalc
from lsttab import bmgs
from lsttab import proz


def main():
    while True:
        print('\nLohnsteuerberrechnung - Österreich!')
        print('---- mit import lsttab -------------')
        for x in range(0, 4):
            print ('Bmg: %8.2f' % bmgs[x], ' mit %4.1f' % (proz[x]*100),'%' )
        print ('Bmg: darüber   mit %4.1f' % (proz[x + 1]*100),'%' )
        print('Eingabe Bmg oder leer = Ende')
        bet=input('LST-Bemessung monatl.: ')
        if bet == '' or bet == ' ':
            break
        else:
            bet=bet.replace(",", ".")
            bet=float(bet)*12
            print('Jahresbemessung: %9.2f' % bet)
            steuer=lstcalc(bet)
            print('Steuer jährlich : %8.2f' % steuer)
            print('Steuer monatlich: %8.2f' %(steuer/12))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass

exit()                      # für python shell
