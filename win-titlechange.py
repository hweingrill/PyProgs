import PySimpleGUI as sg

layout = [[sg.Text('Enter what you would like the Window title to be changed to')],
          [sg.Input(key='_IN_')],
          [sg.Button('Change Title'), sg.Exit()] ]

window = sg.Window('ORIGINAL').Layout(layout)

while True:             # Event Loop
    event, values = window.Read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'Change Title':
        window.TKroot.title(values['_IN_'])
window.Close()
