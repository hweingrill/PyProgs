import classpersonen as clp

p1 = clp.Person("John", str(36), "Graz")     # Objektanlage
p1.funcname()
x=p1.funcage()
print(x)
x=p1.functown()
print('aus return: ',x)

p2 = clp.Person("Gerald", str(40), "London")
p2.funcname()
x=p2.funcage()
print('Mein Alter ist: ' + x)
x=p2.functown()                              # Rückgabewert über return
print('aus return :',x)




# ergibt diese Ausgabe:
"""
Hello, mein Name ist John
36
aus return:  Ich wohne in Graz
Hello, mein Name ist Gerald
Mein Alter ist: 40
aus return : Ich wohne in London
"""
