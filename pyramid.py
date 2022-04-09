height = int(input('gib die Höhe ein: '))

for i in range(height):
    for j in range(height -i -1):
#        print (i,j, end='=i j')
        print(' ', end='')
    for j in range(i+1):
        print('*', end=' ')
    print('\n', end='')
x=input( "\nweiter: ")

print('types')
count1=15
print('count1 = ' + str(count1) +' type ', type(count1))
count2=15.5
print('count2 = ' + str(count2) +' type ', type(count2))
count3=15+6j
print('count3 = ' + str(count3) +' type ', type(count3))
count4='abc'
print('count4 = ' + str(count4) +' type ', type(count4))
x=input( "weiter: ")

zahlen = [3, 6, 9, 12, 15]
for num in zahlen:
    quotient = num / 3
    print(f"{num} divided by 3 is {int(quotient)}.")
