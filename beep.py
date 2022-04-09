import winsound
#frequency = 2500  # Set Frequency To 2500 Hertz
#duration = 500   # Set Duration To 1000 ms == 1 second
#winsound.Beep(frequency, duration)

print(' Der winsound.Beep() = Piepton ausgegeben.')

#winsound.Beep(900, 500)
#winsound.Beep(1200, 1000)
#winsound.Beep(1500, 1500)

#def morse():
    
#exit()
#def annoy():
#    for i in range(1, 10):
#       winsound.Beep(i * 100, 200)

winsound.Beep(1200, 1000)
#x=input('1: ')
winsound.Beep(1500, 1000)
#x=input('2: ')
winsound.Beep(1800, 1000)
x=input('3: ')
exit()
def sos():
    for i in range(0, 3):
        winsound.Beep(1500, 400)
        for i in range(0, 3):
            winsound.Beep(1500, 800)
            for i in range(0, 3):
                winsound.Beep(1500, 400)
sos()                
x=input('1: ')                
annoy()
x=input('2: ')
sos()
x=input('3: ')

