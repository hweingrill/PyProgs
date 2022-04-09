# magishe Quadrat formatiert ausgeben

values=['(a+b)','a','(12*a)','(7*a)','11*a','8*a','b','2*a',
    '5*a','10*a','3*a','3*a+b','4*a','2*(a+b)','6*a','9*a']
i=0
while i < 16:
    wert=(values[i])
    i += 1
    if not i % 4:
        print(wert) 
    else:
        print(wert, end=" " )
        
#wert = input("\nGib eine Zahl (über 21) ein: ")
wert=36
a=int(wert)
# a und b berechnen:
b=21
print(wert, b)
a = a // b
b = a % b
# Magisches Quadrat ausgeben:
i=0
while i < 16:
    wert=(values[i])   
    x=wert
    i += 1
    if not i % 4:
        print(wert) 
    else:
        print(wert, end=" " )
       
print("------------------------------------------------------------")
print('{0:2d}'.format(a+b),'{0:2d}'.format(a),'{0:2d}'.format(12*a),'{0:2d}'.format(7*a))
print('{0:2d}'.format(11*a),'{0:2d}'.format(8*a),'{0:2d}'.format(b),'{0:2d}'.format(2*a))
print('{0:2d}'.format(5*a),'{0:2d}'.format(10*a),'{0:2d}'.format(3*a),'{0:2d}'.format(3*a+b))
print('{0:2d}'.format(4*a),'{0:2d}'.format(2*a+b),'{0:2d}'.format(6*a),'{0:2d}'.format(9*a))
print('\nKontollesumme: ')
erg=((a+b)+a+(12*a)+(7*a))
print('{0:2d} Summe' .format(erg))
print("------------------------------------------------------------")

x=(a+b, a, 12*a, 7*a)
print(' aus sum: ', sum(a+b, a, 12*a, 7*a))


x=(a+b, a, 12*a, 7*a)
print('sum: ', sum(x))
x=(11*a,8*a,b,2*a)
print('sum: ', sum(x))
x=(5*a,10*a,3*a,3*a+b)
print('sum: ', sum(x))
x=(4*a,2*a+b,6*a,9*a)
print('sum: ', sum(x))


    




