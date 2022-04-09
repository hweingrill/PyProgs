'''
Ein magisches Quadrat ist eine Tabelle mit n Zeilen und n Spalten, 
gefüllt mit den ersten n² natuerlichen Zahlen (beginnend mit 1), 
wobei die Summe der Zahlen in jede Zeile, Spalte und Diagonale gleich ist.
 
Schreibe ein Programm, welches das magische Quadrat einer ungeraden Zahl
zwischen 2 und 10 berechnet. 
Die ungerade Zahl darf nicht kleiner als 2 oder größer als 10 sein.
 
'''
 
# Prüffunktionen.
def zeilensumme(quadrat, i):
    summe = 0
    max(len(i) for i in quadrat)
    for n in range(len(quadrat)):
        print (quadrat[i][n])
        summe = summe + quadrat[i][n]
    return summe
 
def spaltensumme(quadrat, i):
    summe = 0
    for n in range(len(quadrat)):
        summe = summe + quadrat[n][i]
    return summe
 
def diagonalsumme_lr(quadrat):
    summe = 0
    i = 0
    for n in range(len(quadrat)):
        summe = summe + quadrat[i][n]
        i += 1
    return summe
 
def diagonalsumme_rl(quadrat):
    summe = 0
    i = len(quadrat) -1
    for n in range(len(quadrat)-1, -1, -1):
        summe = summe + quadrat[i][n]
        i -= 1
    return summe
 
 
# Prüfe Quadrat.
def pruefen(quadrat):   
    r = 0
    for i in range(0, dim-1):
        print(i)
        w=input('prüfen')
        if zeilensumme(quadrat,i) == qsum:
            if spaltensumme(quadrat,i) == qsum:
                r += 1   
                 
    if r == dim-1:
        if diagonalsumme_lr(quadrat) == qsum:  
            if diagonalsumme_rl(quadrat) == qsum:
                return 'richtig!'
 
    return 'falsch!'
 
# Test Quadrat erstellen.
def quadrat_erstellen(dim):
    quadrat = []
    for i in range(dim):
        quadrat.append(list([0 for x in range(dim)]))
    return quadrat
 
# Quadrat füllen.
def quadrat_ungerade(quadrat,dim,zahlen):
    
    x = (dim -1) // 2            # erste Zahl einfügen x=2 bei dim 5
    y = 0
    for i in range(0,dim**2 -0): #-0 zum testen -1, -2 usw.
        if x > dim-1:            # x=2 dim-1 = 4
            x = 0
        if y < 0:  
            y = dim-1
        if quadrat[y][x] != 0:   #
#            print(y , x, quadrat, '**')
            w=input
            x-=1; y+=2
            if y > dim-1: y = 1
            quadrat[y][x] = zahlen.pop(0)
#            print(quadrat)
        else:
            print(quadrat[y][x], zahlen)
            quadrat[y][x] = zahlen.pop(0)
#            print(quadrat[y][x], zahlen)
#            print('el :', quadrat,y ,x)
#            w=input('##')
        x+=1; y-=1  
 
 
# Start -----------------------------------------------.
 
dim    = 5          # größe Quadrat (ungerade Zahl)
qsum   = ( dim * (dim**2 + 1) ) / 2
zahlen = list( [x for x in range(1, dim**2 + 1)] )
print(dim, qsum, zahlen)

 
# Funktionen aufrufen.
quadrat = quadrat_erstellen(dim)
 
if dim % 2 != 0:
    quadrat_ungerade(quadrat, dim, zahlen)
 
# Quadrat formatiert ausgeben.
m = max(len(i) for i in quadrat)
print('lägste Liste in Quadrat: ', max(len(i) for i in quadrat))
y=input()

for l in quadrat:
    print(" ".join("{0:{1}}".format(i, m-1) for i in l))

print('\n  ', pruefen(quadrat), 'Quersumme =', int(qsum))
