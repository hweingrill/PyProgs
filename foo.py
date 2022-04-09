print("before import")
import math

print("before functionA")
def functionA():
    print("Function A")

print("before functionB")
def functionB():
    print("Function B {}".format(math.sqrt(100)))

print("before __guard")
if __name__== '__main__':   
    functionA()
    functionB()
print(__name__)    
print("after __guard")

print('before func. pyramid')
import pyramid
pyramid
print(__name__)


