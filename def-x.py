
def ausgabe(endwert, anfangswert=1, schrittweite=1):
    for x in range(anfangswert, endwert, schrittweite):
#        if x == 1:
#            print(" ", end=" ")
#        if x < 10:
#            print("", end=" ")
#        print(x, end=", ")
         print('%3d' % (x), end=",")
         y = x % 10
         if y == 0:
            print()
    print()        
    print('  Funktion ''"ausgabe"'' durchlaufen')
# Das Programm beginnt eigentlich hier!

print()
print('  Schleifenausgabe über ''"def-Funktion"'' ')
print()
ausgabe(51)
print()
ausgabe(91)
print()
# ---------------------------------------------

valone = 8
valtwo = 3
x = valone / valtwo
r = valone - (valtwo * x)
print ("  Answer: %s with a remainder of %s" % (x, r))

print('  ---------------------------')
x = 5.5
y = 6
r = y %x
print ("  Answer: %s / %s mit Rest %s" % (y, x, r))

x=input('  Weiter mit return: ')
exit()

