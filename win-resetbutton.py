import PySimpleGUI as sg

choices = ('Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Purple', 'Chartreuse', 'Gelb', 'Grün')

layout = [  [sg.Text('What is your favorite color?')],
            [sg.Listbox(choices, size=(15, len(choices)), key='-COLOR-', enable_events=True)] ]

window = sg.Window('Pick a color', layout)

while True:                  # the event loop
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if values['-COLOR-']:    # if something is highlighted in the list
        sg.popup(f"Your favorite color is {values['-COLOR-'][0]}")
window.close()

#--------------------------------------------

layout = [
    [sg.Radio("First", "AL", key='Radio1'),
     sg.Radio("Second", "AL", key='Radio2'),
     sg.Radio("Third", "AL", key='Radio3'),
     sg.Radio("Forth", "AL", key='Radio3'),],
    [sg.Button('Reset')]]

window = sg.Window("Radio", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Reset':
        window["Radio1"].reset_group()          # gesetzte Radio-Buttons löschen

window.close()
