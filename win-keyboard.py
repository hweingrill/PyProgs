#!/usr/bin/env python
import sys
import PySimpleGUI as sg

layout = [[sg.Text("Hold down a key")],
          [sg.Button("OK")]]

window = sg.Window("Realtime Keyboard Test", return_keyboard_events=True, use_default_focus=False).Layout(layout)

while True:
    event, values = window.Read(timeout=50)

    if event == "OK":
        print(event, values, "exiting")
        break
    if event is not sg.TIMEOUT_KEY:
        print(event)
        if len(event) == 1:
            print(event, ord(event))
            #print('%s - %s' % (event, ord(event)))
        else:
            print(event, 'else')
    elif event is None:
        break
