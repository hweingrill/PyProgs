import py_compile
name=input("Prog-Name: ")    # mir 'repr() wird 'text' ausgegeben
#name.ljust(12)
print(name)
py_compile.compile(name)

x=input('weiter mit ret: ')
