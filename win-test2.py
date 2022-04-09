import PySimpleGUI as sg

"""
    "Print" to any Multiline Element in any of your windows.

    cprint in a really handy way to "print" to any multiline element in any one of your windows.
    There is an initial call - cprint_set_output_destination, where you set the output window and the key
    for the Multiline Element.
    There are FOUR different ways to indicate the color, from verbose to the most minimal are:
    1. Specify text_color and background_color in the cprint call
    2. Specify t, b paramters when calling cprint
    3. Specify c/colors parameter a tuple with (text color, background color)
    4. Specify c/colors parameter as a string "text on background"  e.g.  "white on red"
"""

def main():
    cprint = sg.cprint

    MLINE_KEY = '-ML-'+sg.WRITE_ONLY_KEY   # multiline element's key. Indicate it's an output only element
    MLINE_KEY2 = '-ML2-'+sg.WRITE_ONLY_KEY # multiline element's key. Indicate it's an output only element

    output_key = MLINE_KEY

    layout = [  [sg.Text('Multiline Color Print Demo', font='Any 14')],
                [sg.Multiline('Multiline\n', size=(80,20), key=MLINE_KEY)],
                [sg.Multiline('Multiline2\n', size=(80,20), key=MLINE_KEY2)],
                [sg.Text('Text color:'), sg.Input(size=(12,1), key='-TEXT COLOR-'),
                 sg.Text('on Background color:'), sg.Input(size=(12,1), key='-BG COLOR-')],
                [sg.Input('Type text to output here', size=(80,1), key='-IN-')],
                [sg.Button('Print', bind_return_key=True), sg.Button('Print short'),
                 sg.Button('Force 1'), sg.Button('Force 2'),
                 sg.Button('Use Input for colors'), sg.Button('Toggle Output Location'), 
                 sg.Button('Exit')],]
                #[sg.SystemTray.notify('Notification Title', 'This is the notification` message')]]

    window = sg.Window('Window Title', layout)

    sg.cprint_set_output_destination(window, output_key)

    while True:             # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Print':
            cprint(values['-IN-'], text_color=values['-TEXT COLOR-'], \
                   background_colore=values['-BG COLOR-'])

        elif event == 'Print short':
            cprint(values['-IN-'], c=(values['-TEXT COLOR-'], values['-BG COLOR-']))

        elif event.startswith('Use Input'):
            cprint(values['-IN-'], color=values['-IN-'])

        elif event.startswith('Toggle'):
            output_key = MLINE_KEY if output_key == MLINE_KEY2 else MLINE_KEY2
            sg.cprint_set_output_destination(window, output_key)
            cprint('Switched to this output element', c='white on red')

        elif event == 'Force 1':
            cprint(values['-IN-'], c=(values['-TEXT COLOR-'], values['-BG COLOR-']), key=MLINE_KEY)

        elif event == 'Force 2':
            cprint(values['-IN-'], c=(values['-TEXT COLOR-'], values['-BG COLOR-']), key=MLINE_KEY2)
    window.close()

if __name__ == '__main__':
    main()
