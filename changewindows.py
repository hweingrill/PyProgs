import sys

if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

layout = [[sg.Text('Your typed chars appear here:'), sg.Text('', key='_OUTPUT_')],
            [sg.Input(do_not_clear=True, key='_IN_')],
            [sg.Button('Show'), sg.Button('Exit')]]

layoux = [[sg.Text('Seond Window chars appear here:'), sg.Text('', key='OUTPUT')],
            [sg.Input(do_not_clear=True, key='IN')],
            [sg.Button('Sho'), sg.Button('Exi')]]


window = sg.Window('Window Title').Layout(layout)

while True:             # Event Loop
    event, values = window.Read()
    print(event, values)
    if event is None or event == 'Exit':
        break
    if event == 'Show':
        # change the "output" element to be the value of "input" element
        wind = sg.Window('Second Windows').Layout(layoux)
        #sg.Popup('Test second window')
        even, valu = wind.Read()
        print(even, valu)
        if even is None or even == 'Exi':
            break
        if even == 'Sho':
            wind.close()
            #window.find_element('_OUTPUT_').Update(values['_IN_'])

window.Close()
