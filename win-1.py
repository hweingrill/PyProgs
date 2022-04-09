import PySimpleGUI as sg

sg.theme('LightBlue')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Programm zu Berechnung der öster.. Lohnsteuer', font='Arial 12')],
            [sg.Text('Eingabe Bemessungsgrundlage monatl.'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Lohnsteuer Österreich', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('eingegeben wurd: ', values[0])
    
    bet=values[0]
    print(bet.replace(',', '.'))
    bet = bet.replace(",", ".")
    print('das war meine Eingabe: ', bet)
    print(type(bet))
    x = bet.replace(".", ",")
    bet=(float(bet))
    
    print('x-str: ',x)
    print('{:9.2f}'. format (bet))
    #print(type(bet))
    

window.close()
