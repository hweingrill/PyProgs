#!/usr/bin/env python
# -*- coding: utf-8 -*-
from colorama import init, Fore, Style
init()

print(Fore.GREEN + "Erfolgreich ist grün")
print(Fore.YELLOW + "Warnungen sind gelb")
print(Fore.RED + "Fehler sind rot")
print(Style.RESET_ALL, end="")
print("Textfarbe wieder normal")

# Wer den Style nicht von hand zurücksetzen will, kann die init() Funktion mit dem autoreset Parameter aufrufen.

init(autoreset=True)
x=input()
