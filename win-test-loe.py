import PySimpleGUI as sg
from lsttab import rechlst as lstcalc
from lsttab import bmgs
from lsttab import proz

steuer=0,0
sg.theme('BluePurple')

output_key='-WZEIL_KEY-'

layout = [[sg.Text('Anzeige der Eingabe:'), sg.Text(size=(15,1), key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          [sg.Input(key='-BMG-')],
          [sg.T(key='-WZEIL_KEY-')],
          [sg.Button('Calc'), sg.Button('Exit')],
          [sg.Text('Bemessungsgrundlage: '), sg.Text(size=(12,1), key='-AUS-')]]

window = sg.Window('Pattern 2B', layout)
#sg.cprint_set_output_destination(window.output_key)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Calc':
        
        window['-OUTPUT-'].update(values['-IN-'])        
        bet=values['-BMG-'.replace(",", ".")]
        bet=bet.replace(",", ".")
        window['-AUS-'].update(values['-BMG-'])
        bet=float(bet)*12
        steuer=lstcalc(bet)
        steuer=('%.2f' %(steuer/12))
        print (steuer)
        #steuer=('Steuer monatlich: %8.2f' %(steuer/12))
        steuer=str(steuer)
        values['-WZEIL_KEY-'] = str(steuer)
        window['-WZEIL_KEY-'].update(steuer)
        print (values)
        print(type(steuer), (steuer))
        
        #cprint(values['-IN-'], colors=values['-IN-'])
#    if event == 'Show':
#        # Update the "output" text element to be the value of "input" element
#        window['-OUTPUT-'].update(values['-IN-'])

window.close()
