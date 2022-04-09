
#fout=open("ftest.dat","a")
#fout.write("Erster String ")
#fout.write("Zweiter String ")
#fout.write("Dritter String ")
#fout.close()

fin = open("ftest.dat","r")
dateiinhalt = fin.readline()
print (dateiinhalt)
print ("Typ:  "),type(dateiinhalt)
print ("Inhalt: ",end=''), dateiinhalt
fin.close()
