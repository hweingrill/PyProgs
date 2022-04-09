import PySimpleGUI as sg
from lsttab import rechlst as lstcalc

sg.theme('BluePurple'), font=('italic')

layout = [[sg.Text('Einkommensteuer Österreich', font='Any 14', size=(25,1))],
          [sg.T('   Ihre Eingabe:              '),
           sg.Input(key='-EIN-', enable_events=True, size=(13,1))],
          [sg.T('   Bemessung monatlich:'),  sg.Input(key='-BMG-', size=(13,1))],
          [sg.T('   Steuer monatlich:        '), sg.Input(key='-TAX-', size=(13,1))],
          [sg.Button('Calc', visible=False, bind_return_key=True), sg.Button('Exit'),
           sg.T('     Eingabe mit ENTER beenden!')]]

window = sg.Window('Berechnungsprogramm', layout)

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if values['-EIN-'] == '':
        continue
    if values['-EIN-'][-1] not in ('0123456789.,'''):
        window['-EIN-'].update(values['-EIN-'][:-1])
    elif event == 'Calc':            
        bet=values['-EIN-'.replace(",", ".")]
        bet=bet.replace(",", ".")
        beta=float(bet)
        beta=('%6.2f' %(beta))
        beta=beta.replace(".", ",")
        window['-BMG-'].update(" €   " +(beta))
        bet=bet.replace(",", ".")
        bet=float(bet)*12
        steuer=lstcalc(bet)
        steuer=('%6.2f' %(steuer/12))
        #steuer=str(steuer)
        steuer=str(steuer.replace(".", ","))
        window['-TAX-'].update(" €    " + (steuer))
        for key in values['-EIN-']:
            window['-EIN-']('')
        steuer=0

    if event == sg.WIN_CLOSED or event == 'Exit':   
        break
        
window.close()
