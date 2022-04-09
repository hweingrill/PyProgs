import PySimpleGUI as sg

sg.theme('Dark Green 2')

layout = [  [sg.Text('My Window')],
            [sg.Input(key='-IN1-')],
            [sg.Input(key='-IN2-')],
            [sg.Button('Go'), sg.Button('Unbind'),sg.Button('Exit')]
              ]

window = sg.Window('Window Title', layout, finalize=True)

window.bind("<Button-1>", 'Window Click')
window['Go'].bind("<Button-3>", ' +RIGHT CLICK+')
window['-IN2-'].bind("<FocusIn>", ' +FOCUS+')

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == 'Unbind':
        window['Go'].unbind('<Button-3>')

window.close()
