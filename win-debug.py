import PySimpleGUI as sg
import time
import imwatchingyou as imw  # STEP 1

"""
 Demo program that shows you how to integrate the PySimpleGUI Debugger
 into your program.
 This particular program is a GUI based program simply to make it
 easier for you to interact and change things.

 In this example, the debugger is not started initiallly.
 You click the "Debug" button to launch it, There are THREE steps,
 and they are copy and pastes.
 1. At the top of your app to debug add
 import imwatchingyou
 2. When you want to show a debug window, call one of two functions:
 imwatchingyou.show_debug_window()
 imwatchingyou.show_popout_window()
 3. You must find a location in your code to "refresh" the debugger.
 Some loop that's executed often. In this loop add this call:
 imwatchingyou.refresh()
"""

layout = [
 [sg.Text('A typical PSG application')],
 [sg.Input(key='-IN-')],
 [sg.Text(' ', key='-OUT-', size=(45, 1))],
 [sg.CBox('Cbox 1'), sg.CBox('Cbox 2')],
 [sg.Radio('a', 1, key='-R1-'), sg.Radio('b', 1, key='-R2-'),
  sg.Radio('c', 1, key='-R3-')],
 [sg.Combo(['c1', 'c2', 'c3'], size=(6, 3), key='-COMBO-')],
 [sg.Output(size=(50, 6))],
 [sg.Ok(), sg.Exit(), sg.Button('Enable'), sg.Debug(key='Debug')],
]

window = sg.Window('This is your Application Window',
   layout, debugger_enabled=True, finalize=True)
counter = 0

while True:                           # Your Event Loop
    imw.refresh_debugger()
    window.enable_debugger()
    event, values = window.read(timeout=150)
    if event == 'Debug':
        imw.show_debugger_window()
    if values[1] == True:             # wenn kein key angegeben!
        window['-OUT-'].update('cbox-2 gedr.')
    if values[0] == True:
        imw.show_debugger_popout_window()
        window['-OUT-'].update('cbox-1 gedr.')
    if values[0] and values[1]:
        window['-OUT-'].update('CB-1 + CB2 - gedrückt')
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == 'Enable':
        counter += 1
        print(counter)
        window['-OUT-'].update(values['-IN-'])

window.close()
