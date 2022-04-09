import PySimpleGUI as sg
import bkkclass as cls                                    # class Konto:
import datetime
import bksqlcreate

sg.theme('lightgreen3')
font=('Monaco 11 bold')

today = datetime.datetime.today()
anldat=f'{today:%d.%m.%Y}'

layout1 =[[sg.T('Buchungen am:  '+ f'{today:%d.%m.%Y}', font='Any 15', size=(40,1))],
          [sg.T('Kontnummer:  '), sg.I(key='KTONR', do_not_clear=True,font=font, size=(13,1))],
          [sg.T('Kontoinhaber:  '), sg.I(key='KTOIN', font=font, size=(20,1))],
          [sg.T('Verfüger:         '), sg.I(key='VERF',font=font, size=(15,1))],
          [sg.T('Betrag:            '), sg.I(key='BETRAG', font=font, size=(13,1))],
          [sg.T('S a l d o :        '), sg.I(key='Saldo', font=font, size=(13,1))],  
          [sg.B('Exit'), sg.B(' OK '), sg.B('Anlage')]]

layout2 =[[sg.T('Kontenanlage am:  '+ f'{today:%d.%m.%Y}', font='Any 15', size=(40,1))],
          [sg.T('Kontnummer:   '), sg.I(key='ANLNR', font=font, size=(8,1))],
          [sg.T('Kontoinhaber:  '), sg.I(key='ANLIN', font=font, size=(20,1))], 
          [sg.T('Verfüger:         '), sg.I(key='BERE', font=font, size=(30,1))],
          [sg.T('Kreditrahmen:  '),sg.I(key='KRAM', font=font, size=(10,1))], 
          [sg.B('Exit'), sg.B(' OK ')]]
                     
win1 = sg.Window('Buchungsprogramm BK-Konten',  layout1, finalize=True)
entry = win1['KTONR']
entry.bind("<Return>", "RET")                       
entry = win1['BETRAG']
entry.bind("<Return>", "RET")

win2_active=False
bkkonot=0
win1.find_element('KTONR').SetFocus()

main in bkslqcreate
while True:
    evb, valsb = win1.read()
    print(evb, valsb)

    if evb == sg.WIN_CLOSED or evb == 'Exit':
        break
    if evb == 'Anlage'  and not win2_active:
        win2_active = True
#        win1.Hide()
        win2 = sg.Window('Kontenanlage', layout2, finalize=True)
        entry = win2['ANLNR']
        entry.bind("<Return>", "RET")                       
        entry = win2['ANLIN']
        entry.bind("<Return>", "RET")
        entry = win2['BERE']
        entry.bind("<Return>", "RET")
        entry = win2['KRAM']
        entry.bind("<Return>", "RET")
        win2.find_element('ANLNR').SetFocus()
        while True:
            eva, valsa = win2.read(timeout=100)
            if eva == sg.WIN_CLOSED or eva == 'Exit':
                win2.close()
                win2_active = False
                win1.UnHide()
                break
            if eva in ('ANLNR'):
                win2.find_element(eva).Update(re.sub("[^0-9]", "", valsa[eva]))
                print(eva, valsa)
            if eva == 'ANLNRRET':
                if valsa['ANLNR'] == '0' or valsa['ANLNR'] == '' or valsa['ANLNR'] == (' no input '):
                    win2['ANLNR'].update(" no input ")
                    win2.Element('ANLNR').SetFocus()
                    continue
                else:
                    ktonum=valsa['ANLNR']
                    print(ktonum)    
                    win2.find_element('ANLIN').SetFocus()
            if eva == 'ANLINRET':
                ktouse=valsa['ANLIN']
                win2.find_element('BERE').SetFocus()
                print(ktouse)
                print(type(ktouse))
            if eva ==  'BERERET':
                ktobere=valsa['BERE']
                print(ktonum, ktouse, ktobere)
                win2.find_element('KRAM').SetFocus()
            if eva ==  'KRAMRET':
                ktorahm=valsa['KRAM']
                print(ktorahm, type(ktorahm))
                print(ktonum, ktouse, ktobere, ktorahm, anldat)
            if eva == ' OK ':
                print(eva, valsa)
                print(type(ktouse))
                ktouse=cls.Konto(ktouse,ktonum,[ktouse,ktobere,"Banker"],100)
                print('Inhaber: ', ktouse.lautend())
                print ("Anzahl der Konten  :",cls.Konto.angelegteKonten)
                print ('Kontostand von ',+ ktouse, ': '.ktouse.abfrage())
             
            
    if evb in ('KTONR','BETRAG'):
        win1.find_element(evb).Update(re.sub("[^0-9]", "", valsb[evb]))
    if evb == 'KTONRRET' or evb == 'KTONR':
        ktouse=valsb['KTONR']
        print(ktouse)
        print('Inhaber: ', ktouse.lautend())
        
        
          

