import PySimpleGUI as sg
import re

sg.ChangeLookAndFeel('LightGreen')

layout = [[sg.Text('Time Input Validation Demonstration', font='Any 18')],
          [sg.In(key='_TIME1_', size=(3,1), change_submits=True, do_not_clear=True), sg.T(':', pad=(10,5)),
           sg.In(key='_TIME2_', size=(3,1), change_submits=True, do_not_clear=True), sg.T(':', pad=(10,5)),
           sg.In(key='_TIME3_', size=(3,1), change_submits=True, do_not_clear=True)],
          [sg.Multiline(key='_M_', do_not_clear=True)],
          [sg.R('mit ', 9,), sg.R('ohne ', 9), sg.OK()]]

window = sg.Window('Demo - Input Validation', font=('Helvetica 14')).Layout(layout)

while True:
    event, values = window.Read(timeout=10)
#    print(event, values)
    if event in (None, 'Quit'):
        break
    if event in ('_TIME1_', '_TIME2_', '_TIME3_'):
        window.find_element(event).Update(re.sub("[^0-9]", "", values[event]))
    if event == '_TIME1_' and len(window.find_element(event).Get()) == 2:
        window.find_element('_TIME2_').SetFocus()
        print('1. Feld: ', event, values)
    if event == '_TIME2_' and len(window.find_element(event).Get()) == 2:
        window.find_element('_TIME3_').SetFocus()
        print('2. Feld: ',event, values)
    if event == '_TIME3_' and len(window.find_element(event).Get()) == 2:
        window.find_element('_M_').SetFocus()
        print('3. Feld: ',event, values)
    if event == 'OK':
        print(event, values)
window.Close()
