import PySimpleGUI as sg

sg.theme('Light Blue 3')
# This design pattern simulates button callbacks
# This implementation uses a simple "Dispatch Dictionary"
# to store events and functions
# The callback functions

def button1():
    sg.popup_ok(' Erledigt ')
    print('Button 1 callback')

def button2():
    sg.popup_ok(' Button-2 gedrückt ')
    print('Button 2 callback')

                    # Lookup dictionary that maps button to function to call
dispatch_dictionary = {'1':button1, '2':button2}

layout = [[sg.Text('Please click a button', auto_size_text=True)],
          [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Quit()]]

window = sg.Window('Button callback example', layout)
                    
while True:
    event, value = window.read()            
    print(event, value)
    if event in ('Quit', sg.WIN_CLOSED):
        break
                    # Lookup event in function dictionary
    if event in dispatch_dictionary:
        func_to_call = dispatch_dictionary[event]   # get function from dispatch dictionary
        func_to_call()
    else:
        print('Event {} not in dispatch dictionary'.format(event))

window.close()

sg.popup_ok('Done')
