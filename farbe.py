
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from colorama import init, Fore, Style
init()
class bcolors:
    OK = '\033[92m'      #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m'    #RED
    RESET = '\033[0m'    #RESET COLOR
print(f"{bcolors.OK}File Saved Successfully!{bcolors.RESET}")
print(f"{bcolors.WARNING}Warning: Are you sure you want to continue?{bcolors.RESET}")
print(f"{bcolors.FAIL}Unable to delete record.{bcolors.RESET}")

import os
osname=os.name
directory=os.getcwd()
print(osname)
print(directory)
listung=os.system("dir *.py")
x=input()
listung=os.system("calc")
x=input()
listung=os.listdir(' *.py ')
print(listung)
x=input()
