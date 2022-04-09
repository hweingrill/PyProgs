year = 2016
event = 'Referendum'
print (f'  Results of the {year} {event}')
# 'Results of the 2016 Referendum'

# Die str.format()Methode der Strings erfordert mehr manuellen Aufwand.
# Sie werden weiterhin {und verwenden }, um zu markieren, wo eine
# Variable ersetzt wird, und können detaillierte Formatierungsanweisungen
# bereitstellen, aber Sie müssen auch die zu formatierenden Informationen
# bereitstellen.

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('  Die Anzahl wird auf 9-Stellen begrenzt und der %-Satz auf 2,2 Stellen')
print ('{:-9}  YES votes {:2.2%}'.format(yes_votes, percentage))
# ' 42572654 YES votes  49.67%'

x=input(' Weiter mit ret: ')

s = 'Hello, world.'
str(s)
# 'Hello, world.'
repr(s)
# "'Hello, world.'"
str(1/7)
# '0.14285714285714285'
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
# The value of x is 32.5, and y is 40000...
# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
#'hello, world\n'
# The argument to repr() may be any Python object:
repr((x, y, ('spam', 'eggs')))

x=input(' Weiter mit ret: ')
