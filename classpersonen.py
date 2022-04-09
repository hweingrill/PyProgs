# diese "Class" wird von clspers aufgerufen
# 'self' könnte auch pers sein und in funcname (etc) statt slef z.B auch "abc"

class Person:
  def __init__(self, name, age, town):
    self.name = name
    self.age = age
    self.town = town

  def funcname(self):
    print("Hello, mein Name ist " + self.name)
    
  def funcage(abc):  
#   print("Hello, mein Alter ist " + self.age)       # nur Wertrückgabe
    return(abc.age)

  def functown(self):
    x=("Ich wohne in " + self.town)                  # Text- + Wertrückgabe
    return(x)

