import PySimpleGUI as sg
from lsttab import rechlst as lstcalc

sg.theme('BluePurple')
font=('Monaco 12 bold')   

layout = [[sg.T('Einkommensteuer Österreich', font='Any 15', size=(25,1))],
          [sg.T('   Ihre Eingabe:              '),
           sg.I(key='-EIN-', enable_events=True, size=(13,1))],
          [sg.T('   Bemessung monatlich:'),
           sg.I(key='-BMG-', font=font, size=(13,1))],
          [sg.T('   Steuer monatlich:        '),
           sg.I(key='-TAX-', font=font, size=(13,1))],
          [sg.B('Calc', visible=False, bind_return_key=True), sg.Button('Exit'),
           sg.T('     Eingabe mit ENTER beenden!')]]

window = sg.Window('Berechnungsprogramm', layout)

def main():
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        if values['-EIN-'] == '':
            continue
        if values['-EIN-'][-1] not in ('0123456789.,'''):
            window['-EIN-'].update(values['-EIN-'][:-1])
        elif event == 'Calc':            
            bet=values['-EIN-']
            bet=bet.replace(",", ".")
            beta=float(bet)
            beta=('%8.2f' %(beta))
            beta=beta.replace(".", ",")
            window['-BMG-'].update(" € " +(beta))
            print(bet)
            bet=float(bet)*12
            steuer=lstcalc(bet)
            steuer=('%8.2f' %(steuer/12))
            steuer=str(steuer.replace(".", ","))
            window['-TAX-'].update(" € " + (steuer))
            for key in values['-EIN-']:
                window['-EIN-']('')
        if event == sg.WIN_CLOSED or event == 'Exit':   
            break
    window.close()

if __name__ == '__main__':    
    main()
    
