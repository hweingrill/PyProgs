import PySimpleGUI as sg

layout = [
            [sg.Text('My layout', key='_TEXT_')],
            [sg.Input(key='_INPUT_')],
            [sg.Button('Update')]]

window = sg.Window('My new window', layout)

while True:             # Event Loop
    event, values = window.Read()
    if event is None:
        break
    window['_TEXT_'].Update(values['_INPUT_'])
