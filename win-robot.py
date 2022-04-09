#Here is the code to make, show and get results from this window:

import PySimpleGUI as sg

gui_rows = [[sg.Text('Robotics Remote Control')],
            [sg.T(' '  * 10), sg.RealtimeButton('Forward')],
            [sg.RealtimeButton('Left'), sg.T(' '  * 15), sg.RealtimeButton('Right')],
            [sg.T(' '  * 10), sg.RealtimeButton('Reverse')],
            [sg.T('')],
            [sg.Quit(button_color=('black', 'orange'))]
            ]

window = sg.Window('Robotics Remote Control', gui_rows)

#
# Some place later in your code...
# You need to perform a Read or Refresh call on your window every now and then or
# else it will apprear as if the program has locked up.
#
# your program's main loop
while (True):
    # This is the code that reads and updates your window
    event, values = window.read(timeout=50)
    print(event)
    if event in ('Quit', sg.WIN_CLOSED):
        break

window.close()  # Don't forget to close your window!

#Diese Schleife liest Tastenwerte und druckt sie. Wenn auf eine der Echtzeit-Schaltflächen
#geklickt wird, gibt der Aufruf von window.readeinen Schaltflächennamen zurück, der mit
#dem Namen der gedrückten Schaltfläche oder der Taste übereinstimmt, wenn der Schaltfläche
#eine Taste zugewiesen war. Es werden weiterhin Werte zurückgegeben, solange die Taste
#gedrückt bleibt. Nach dem Loslassen gibt Read Timeout-Ereignisse zurück, bis erneut auf
#eine Schaltfläche geklickt wird.
#Dateitypen Die Schaltflächen FileBrowse& SaveAshaben eine zusätzliche Einstellung namens
#file_types. Diese Variable wird verwendet, um die im Dateidialogfeld angezeigten Dateien
#zu filtern. Der Standardwert für diese Einstellung ist

#FileTypes=(("ALL Files", "*.*"),)

#Dieser Code erzeugt ein Fenster, in dem die Schaltfläche Durchsuchen nur Dateien des Typs .TXT anzeigt
#layout =  [[sg.In() ,sg.FileBrowse(file_types=(("Text Files", "*.txt"),))]]
#Die ENTER-Taste Die ENTER-Taste ist ein wichtiger Teil der Dateneingabe für Windows.
#Es gibt eine lange Tradition, dass die Eingabetaste zum schnellen Senden von Fenstern
#verwendet wird. PySimpleGUI implementiert dies, indem die EINGABETASTE an die erste
#Schaltfläche gebunden wird, die ein Fenster schließt oder liest.
#Die Eingabetaste kann an eine bestimmte Schaltfläche "gebunden" werden, sodass beim Drücken der
#Taste das Fenster so zurückkehrt, als ob die Schaltfläche angeklickt worden wäre. Dies geschieht
#über den bind_return_keyParameter in den Tastenaufrufen. Wenn es mehr als 1 Schaltfläche in
#einem Fenster gibt, wird die ERSTE Schaltfläche vom Typ Fenster schließen oder Fenster lesen verwendet.
#Zuerst wird bestimmt, indem das Fenster von oben nach unten und von links nach rechts gescannt wird.
#ButtonMenu-Element

#Das ButtonMenu-Element erzeugt einen einzigartigen Effekt. Es ist eine Schaltfläche, die, wenn sie angeklickt wird, ein Menü anzeigt. Es ist wie das Klicken auf eines der Menüelemente der obersten Ebene in einer Menüleiste. Als Ergebnis nimmt die Menüdefinition das Format eines einzelnen Menüeintrags von einer normalen Menüdefinition an. Eine normale Menüdefinition ist eine Liste von Listen. Diese Definition ist eine dieser Listen.

# ['Menu', ['&Pause Graph', 'Menu item::optional_key']]

#Die allererste Zeichenfolge gibt normalerweise an, was in der Menüleiste angezeigt wird. In diesem Fall wird der Wert nicht verwendet . Den Text für die Schaltfläche setzen Sie mit einem anderen Parameter, dem Parameter button_textparm.
#Eine Verwendung dieses Elements besteht darin, eine "falsche Menüleiste" mit einem farbigen Hintergrund zu erstellen. Bei normalen Menüleisten kann die Hintergrundfarbe nicht geändert werden. Nicht so bei ButtonMenus.
#Schaltflächenmenü
#Rückgabewerte für ButtonMenus werden über das Rückgabewerteverzeichnis gesendet. Wenn eine Auswahl getroffen wird, wird ein Ereignis generiert, das dem Schlüsselwert von ButtonMenu entspricht. Verwenden Sie diesen Schlüsselwert, um den vom Benutzer ausgewählten Wert nachzuschlagen. Dies ist derselbe Mechanismus wie beim Menüleistenelement, unterscheidet sich jedoch vom Popup-Menü (Rechtsklick).
#VerticalSeparator-Element
