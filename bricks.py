def is_anagram(firstWord, secondWord):
    laenge = len(firstWord)
    list = []
    for i in range(0, laenge):
        for x in range(0, laenge):
            vlg = firstWord[x]         # buchstaben vergleichen
            print (vlg)
            xx=x+1
            if vlg != secondWord[i]:
                pass
                #list.append(ii)
                #list.append('F '+vlg)
                #list.append(xx)
            else:
                list.append('T '+vlg)
                list.append(xx)               
                break                   # wenn gefunden beenden
        print(list)

    return list, laenge
    
list, laenge = is_anagram("scare", "races")
print(list, laenge)

#--------------------------------------------------------------#



# Warum fügst Du False zur Liste hinzu, wenn Du es gar nicht verwenden willst?


def is_anagram(first_word, second_word):
    result = []
    for character1 in first_word:
        for character2 in second_word:
            if character1 == character2:
                result.append(True)
                break
    return result

def is_anagram(first_word, second_word):
    result = []
    for character in first_word:
        if character in second_word:
            result.append(True)
    return result

# Was man, leicht in eine Listcomprehension umwandeln kann:


def is_anagram(first_word, second_word):
    return [True for character in first_word if character in second_word]

# Oder, da es nur um die Anzahl der Trues geht:


def is_anagram(first_word, second_word):
    return sum(character in second_word for character in first_word)

#if list  == True:   
#    ausgabe = True
#else:
#    ausgabe = False
#print(ausgabe)
