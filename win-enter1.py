import PySimpleGUI as sg

layout = [  [sg.Text('Input element that clears after every read')],
            [sg.Input('Initial text', key='-I-', do_not_clear=False)],
            [sg.Button('Go'), sg.Button('Exit')] ]

window = sg.Window('Input auto-clear', layout)

while True:             # Event Loop
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    print(event, values)
window.close()
