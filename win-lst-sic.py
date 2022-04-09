import PySimpleGUI as sg
from lsttab import rechlst as lstcalc
from lsttab import bmgs
from lsttab import proz

steuer=0,0
sg.theme('BluePurple')

layout = [[sg.Text('Einkommensteuer Österreich', font='Any 14', size=(25,1))],
          [sg.T('   Bemessung monatlich:'),  sg.Input(key='-EIN-',  size=(13,1))],      
          [sg.T('   Steuer monatlich:        '), sg.Input(key='-TAX-', size=(13,1))],
          [sg.Button('Calc', visible=False, bind_return_key=True), sg.Button('Exit'),
           sg.T('     Eingabe mit ENTER beenden!')]]

window = sg.Window('Berechnungsprogramm', layout)

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if values['-EIN-'] in " €":
        window['-EIN-'].update(' ') 
    print(values)
    
    if values['-EIN-'][-1] not in ('0123456789.,'):
        window['-EIN-'].update(values['-EIN-'][:-1])
    if values['-EIN-'] in " €":
        window['-EIN-'].update(" " ) 
        print(values)
    elif event == 'Calc':            
        bet=values['-EIN-'.replace(",", ".")]
        window['-EIN-'].update(" €   " +(bet))
        bet=bet.replace(",", ".")
        bet=float(bet)*12
        steuer=lstcalc(bet)
        steuer=('%.2f' %(steuer/12))
        steuer=str(steuer)
        steuer=steuer.replace(".", ",")
        window['-TAX-'].update(" €     " + (steuer))
        values['-EIN-'] = str('€')

        print (values) 
        steuer=0
        

    if event == sg.WIN_CLOSED or event == 'Exit':   
        break
        
        
window.close()
