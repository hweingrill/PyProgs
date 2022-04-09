# -*- coding:utf-8 -*-
#from playsound import playsound 
import winsound
print("beep")
winsound.Beep(345,456)
##beep gibt keinen Ton von sich,ist aber offensichtlich damit beschäftigt
##das heißt, der nächste Befehl kommt erst nach Ablauf der Zeit

print(" exit-ton")
winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
##hier nur ein sehr leises Pipsen, auch bei voller Lautstärke

print(" Arznei")
#playsound(r'D:\Projekte\ARZNEI.WAV')
##hier hört man was, das auch einigermassen laut genug ist.
print(" THE END")
