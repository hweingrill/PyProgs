import PySimpleGUI as sg
for i in range(10):
    sg.Print(i)
print=sg.Print    
"""
  ____                         
 |  _ \ ___  _ __  _   _ _ __  
 | |_) / _ \| '_ \| | | | '_ \ 
 |  __/ (_) | |_) | |_| | |_) |
 |_|   \___/| .__/ \__,_| .__/ 
            |_|         |_|  
A Popup demonstration. A "Popup" window is shown over the main
window.  Clicking OK will close the Popup and you return to main again.
"""

print('Starting up...')

layout = [
    [sg.Text('Your typed chars appear here:'), sg.Text('', key='_OUTPUT_')],
    [sg.Input('', key='_IN_')],
    [sg.B('Show'), sg.B('Blank'), sg.B('Fill'), sg.B('Exit')]
]

window = sg.Window('Window Title', layout)

while True:  # Event Loop
    print('in event loop')
    event, values = window.read()

    print(event, values)
    if event in (None, 'Exit'):
        break
    
    if event == 'Blank':
        print('Blank-gedrückt')
        sg.popup('PopUp-Fenster!   ', 'You typed: ' + values['_IN_'])
        window['_IN_'].update("")
    
    if event == 'Show':
        sg.popup('A popup!', ' You typed ', values['_IN_'])
        
    if event == 'Fill':
        print('Fill-gedrückt')
        window['_IN_'].update("**** füllen ***")
        
window.close()
