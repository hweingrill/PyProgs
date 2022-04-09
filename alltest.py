#! /usr/bin/env python3

'''
from
http://projecteuler.net/problem=1
challenge:

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000

sum([x for x in range (10) if not x % 3 or not x % 5])
23
'''

print ("Die Summe aller durch 3 oder durch 5 teilbaren Zahlen unter 1000 ist {}."
       .format(sum([x for x in range (1000) if not x % 3 or not x % 5])))

a=1
b=2
s = ((a+b), 7*a, (2*a)+b)
x = sum(s)
print (x)
