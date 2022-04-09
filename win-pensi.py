import PySimpleGUI as sg
from lsttab import rechlst as lstcalc
from lsttab import jahr
import datetime
import re

sg.ChangeLookAndFeel('BluePurple')
#sg.theme('BluePurple')
font=('Monaco 12 bold')

today = datetime.datetime.today()
j=(f"{today:%Y}")

layout = [[sg.T('Abrechnungs-Programm Pensionisten  ' + f'{today:%d.%m.%Y}', font='Any 14', size=(40,1))],
          [sg.T('     wählen sie ein Jahr:   '), sg.Combo(['2021', '2022', '2023'], 
           size=(6, 3), key='-COMBO-', default_value=j),
           sg.T('   BRUTTO: '),
           sg.I(key='-BRM-', font=font, size=(13,1))],
          [sg.T('Brutto monatlich: '),
           sg.In(key='-BTTO-', font=font, size=(12,1), do_not_clear=True, change_submits=True), 
           sg.T('      SV: '), sg.I(key='-SVK-', font=font, size=(13,1))],
          [sg.T('Freibetrag:          '),
           sg.In(key='-FREI-', font=font, size=(12,1), do_not_clear=True, change_submits=True),
           sg.T('     LST: '), sg.I(key='-LST-', font=font, size=(13,1))],
          [sg.T('Sonstiges:          '),
           sg.In(key='-PFGI-', font=font, size=(12,1), do_not_clear=True, change_submits=True),
           sg.T('      +/- : '), sg.I(key='-ZUAB-', font=font, size=(13,1))],
          [sg.B('Exit'), sg.B('Rechne', visible=True, ), 
           sg.T(' mit ENTER beenden!     NETTO: '),
           sg.I(key='-NTTO-', font=font, size=(13,1))],
          [sg.B('löschen', visible=True,),
           sg.T('Lösche Eingaben       -  "," verwenbar  -         ®(2022) H.Weingrill')]]

window = sg.Window('Pensionsberechnung', layout, finalize=True)
entry = window['-BTTO-']
entry.bind("<Return>", "RET")                       
entry = window['-FREI-']
entry.bind("<Return>", "RET")
entry = window['-PFGI-']
entry.bind("<Return>", "RET")

#window[1].update(True)                               # Radio-Button - ohne löschen - gesetzt

def main():
    bet=0
    beta=0.0
    freibet=0.0
    window.Element('-BTTO-').SetFocus()
    while True:
        event, values = window.Read(timeout=10) 
        #print(event, values)                         # nur für Test key='-NTTO-
        if event == sg.WIN_CLOSED or event == 'Exit':
           break
        
        if event == 'löschen':
            for key in values['-BTTO-']:              # löschen der Eingabefelder
               window['-BTTO-']('')
            for key in values['-FREI-']:              
                window['-FREI-']('')
            for key in values['-PFGI-']:             
                window['-PFGI-']('')
            continue

        if event in ('-BTTO-','-FREI-','-PFGI-'):
            window.find_element(event).Update(re.sub("[^0-9,-]", "", values[event]))
            if event == '-BTTO-':
                window.find_element(event).Update(re.sub("[^0-9,]", "", values[event]))
        
        if event == '-BTTO-RET':
            if values['-BTTO-'] == '0' or values['-BTTO-'] == '' or values['-BTTO-'] == (' no input '):
                window['-BTTO-'].update(" no input ")
                window.Element('-BTTO-').SetFocus()
                continue
            else:
                beta=values['-BTTO-']
                btto=brutto(beta)                   # btto in float
                window.find_element('-FREI-').SetFocus()
                
        if event == ('-FREI-RET'):
            beta=values['-FREI-']
            freibet=frei(beta)
            window.find_element('-PFGI-').SetFocus()
            
        if event == ('-PFGI-RET' ):
            beta=values['-PFGI-']
            pflege=pfleg(beta)            

        if event in ('Rechne','-PFGI-RET'):    
            if values['-BTTO-'] == '0' or values['-BTTO-'] == '' or values ['-BTTO-'] == (' no input '):
                window['-BTTO-'].update(" no input ")
                continue
        if event in ('Rechne','-PFGI-RET'):
            beta=values['-BTTO-']                     # Brutto
            btto=brutto(beta)                         
            beta=values['-FREI-']                     # Freibetrag
            freibet=frei(beta)
            beta=values['-PFGI-']                     # Pfelgegeld etc.
            pflege=pfleg(beta)            
            svbet=btto*5.1/100                           
            beta=('%9.2f' %(svbet))
            beta=beta.replace(".", ",")
            window['-SVK-'].update(" € " +(beta))     # Sozialversicherung
            bet=btto-svbet
            ntto=bet+pflege
            bet-=freibet                              # BMG +/- Freibetrag/Hinzurechnung 
            j=values['-COMBO-']
            bet=float(bet)*12
            basis=bet
            steuer, jahr=lstcalc(bet, j, basis)       # Steuerberechnung
            steuer=steuer/12
            steuer=float(steuer)
            ntto-=steuer
            steuer=('%9.2f' %(steuer))
            steuer=steuer.replace(".", ",")
            window['-LST-'].update(" € " + (steuer))  # Steuer
            ntto=('%9.2f' %(ntto))
            ntto=ntto.replace(".", ",")
            window['-NTTO-'].update(" € " + (ntto))   # Netto
            window.find_element('-BTTO-').SetFocus()
            
    window.close()

def aufbereit(bets):
    if bets == 0 or bets == '' or bets == ' ':
        bets='0,0'
    bets=bets.replace(",", ".")     
    bets=float(bets)
    betf=bets
    bets=('%9.2f' %(bets))
    bets=bets.replace(".", ",")
    return(bets, betf)

def brutto(bets):
    bets,betf=aufbereit(bets)
    window['-BTTO-'].update(bets)
    window['-BRM-'].update(" € " +(bets))
    return(betf)

def frei(bets):
    bets,betf=aufbereit(bets)
    window['-FREI-'].update(bets)
    return(betf)

def pfleg(bets):
    bets,betf=aufbereit(bets)
    window['-PFGI-'].update(bets)
    window['-ZUAB-'].update(" € " + bets)      
    return(betf)
  
        
if __name__ == '__main__':
    main()

