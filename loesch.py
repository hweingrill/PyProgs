Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = (map(lambda x: (float(9)/5)*x + 32, Celsius))
print (Fahrenheit)
#[102.56, 97.700000000000003, 99.140000000000001, 100.03999999999999]
C = map(lambda x: (float(5)/9)*(x-32), Fahrenheit)
print (C)
#[39.200000000000003, 36.5, 37.300000000000004, 37.799999999999997]
 
