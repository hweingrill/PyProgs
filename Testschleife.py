# Schleifentest wihle mit if-Abfrage
x = 0
durchgang = 1
while durchgang < 11:
    print(durchgang, end=", ")
    durchgang += 1
    if durchgang == 6:
        print()
        x = input("0 = Ende: ")
        if x == "0":
  #          print(x)
            break
        else:
            print("es geht weiter")       
if durchgang == 11:
    print()
    print("Schleifenende")
else:
    print("Ende mit Abbruch")
durchgang = input("weiter mt return ")



