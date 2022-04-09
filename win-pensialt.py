import PySimpleGUI as sg
from lsttab import rechlst as lstcalc
from lsttab import jahr
import datetime

sg.theme('BluePurple')
font=('Monaco 12 bold')

today = datetime.datetime.today()
j=(f"{today:%Y}")

layout = [[sg.T('Abrechnungs-Programm Pensionisten  ' + f'{today:%d.%m.%Y}', font='Any 14', size=(40,1))],
          [sg.T('     wählen sie ein Jahr:   '), sg.Combo(['2021', '2022', '2023'], 
           size=(6, 3), key='-COMBO-', default_value=j),
           sg.T('   BRUTTO: '), sg.I(key='-BRM-', font=font, size=(13,1))],
          [sg.T('Brutto monatlich: '), sg.I(key='-BTTO-', font=font,enable_events=True, size=(12,1)),
           sg.T('      SV: '), sg.I(key='-SVK-', font=font, size=(13,1))],
          [sg.T('Freibetrag:          '),
           sg.I(key='-FREI-', font=font, enable_events=True, size=(12,1)),
           sg.T('     LST: '), sg.I(key='-LST-', font=font, size=(13,1))],
          [sg.T('Sonstiges:          '),
           sg.I(key='-PFGI-', font=font, enable_events=True, size=(12,1)),
           sg.T('      +/- : '), sg.I(key='-ZUAB-', font=font, enable_events=True, size=(13,1))],
          [sg.B('Exit'), sg.B('Rechne', visible=True, ), 
           sg.T('                                   NETTO:  '),
           sg.I(key='-NTTO-', font=font, size=(13,1))],
          [sg.R('mit ', 1,), sg.R('ohne ', 1), sg.T('Löschung der Eingabe                ®(2022) H.Weingrill')],]
                     
window = sg.Window('Pensionsberechnung',  layout, finalize=True)
window[1].update(True)                               # Radio-Button - ohne löschen - gesetzt
betf=0.0
def main():
    while True:
        event, values = window.read(timeout=10)
        #print(event, values)                        # nur für Test key='-NTTO-
        if event == sg.WIN_CLOSED or event == 'Exit':
           break
        if values['-BTTO-'] != '':
            if values['-BTTO-'][-1] not in ('0123456789.,'''):
                window['-BTTO-'].update(values['-BTTO-'][:-1])
        if values['-FREI-'] != '':
            if values['-FREI-'][-1] not in ('0123456789.-,'''):
                window['-FREI-'].update(values['-FREI-'][:-1])
        if values['-PFGI-'] != '':        
            if values['-PFGI-'][-1] not in ('0123456789.,'''):
                window['-PFGI-'].update(values['-PFGI-'][:-1])
                
        if event == 'Rechne':
            if values['-BTTO-'] == '0' or values['-BTTO-'] == '' or values ['-BTTO-'] == (' no input '):
                window['-BTTO-'].update(" no input ")
                continue
        if event == 'Rechne':
            bet=values['-BTTO-']                       # Brutto
            bet=bet.replace(",", ".")     
            beta=float(bet)
            bet=float(bet)
            ntto=bet
            beta=('%9.2f' %(beta))
            beta=beta.replace(".", ",")
            window['-BRM-'].update(" € " +(beta))
            window['-BTTO-'].update(beta)

            svbet=bet*5.1/100                           
            bet-=svbet
            ntto-=svbet
            beta=('%9.2f' %(svbet))
            beta=beta.replace(".", ",")
            window['-SVK-'].update(" € " +(beta))      # Sozialversicherung
            
            beta=values['-FREI-']
            if beta == 0 or beta == '' or beta == ' ':
                beta='0,0'
            beta=beta.replace(",", ".")
            beta=float(beta)
            bet-=beta
            beta=('%9.2f' %(beta))
            beta=beta.replace(".", ",")    
            window['-FREI-'].update(beta)            # Frei- oder Hinzurechnung

            pflege=values['-PFGI-']
            if pflege == 0 or pflege == '' or pflege == ' ':
                pflege='0,0'
            pflege=pflege.replace(",", ".")
            pflege=float(pflege)
            ntto+=pflege
            pflege=('%9.2f' %(pflege))
            pflege=pflege.replace(".", ",")
            window['-PFGI-'].update(pflege)
            window['-ZUAB-'].update(" € " + pflege)      # Pfleggeld oder Abzug
            
            j=values['-COMBO-']
            bet=float(bet)*12
            basis=bet
            steuer, jahr=lstcalc(bet, j, basis)
            steuer=steuer/12
            steuer=float(steuer)
            ntto-=steuer
            steuer=('%9.2f' %(steuer))
            steuer=steuer.replace(".", ",")
            window['-LST-'].update(" € " + (steuer))      # Steuer
            ntto=('%9.2f' %(ntto))
            ntto=ntto.replace(".", ",")
            window['-NTTO-'].update(" € " + (ntto))

            if values[0] == True:
                for key in values['-BTTO-']:              # löschen der Eingabefelder
                    window['-BTTO-']('')
                for key in values['-FREI-']:              
                    window['-FREI-']('')
                for key in values['-PFGI-']:             
                    window['-PFGI-']('')    
    window.close()
        
if __name__ == '__main__':
    main()

