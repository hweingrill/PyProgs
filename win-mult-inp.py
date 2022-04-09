import PySimpleGUI as sg

"""
    For Reddit - Input a value, then enter another 3 more into same input box. Store in a list
"""

layout = [  [sg.Text('Multiple Data Entry')],
            [sg.Text('Initial Value', justification='r', size=(12,1), key='-TEXT-'), sg.Input(size=(8,1),do_not_clear=False, key='-IN-')],
            [sg.Button('Enter', bind_return_key=True), sg.Button('Exit')]  ]

window = sg.Window('Muleiple Data Entry', layout)

counter = 0
stuff_entered = []
while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Enter':
        stuff_entered.append(values['-IN-'])
        if counter > 2:
            break
        window['-TEXT-'].update(f'Input Value {counter+1}')
        counter += 1
        print(stuff_entered)

window.close()
sg.popup(f'You entered {stuff_entered}')
