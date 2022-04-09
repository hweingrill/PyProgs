import PySimpleGUI as sg

# Basic example of PSGWeb

def main():
    layout = [
        [sg.Text('This is a text element')],
        [sg.Input('vorgabewerte lt. sg.Input')],
        [sg.Combo(['Combo 1'])],
        [sg.Text('If you close the browser tab, the app will exit gracefully')],
        [sg.InputText('Source')],
        [sg.InputText('Dest')],
        [sg.Ok(), sg.Cancel(), sg.Exit()]
    ]

    window = sg.Window('Demo window..', layout)
#    i = 0
    while True:
        event, values = window.read(timeout=10)
        if event != sg.TIMEOUT_KEY:
            print(event, values)
        if event in (None, 'Exit'):
            break
        if event == 'Ok':
            window[3].update("* D *")
        if event == 'Cancel':
            window[0].update(' ** gelöscht **')
#            print(i)
#        i += 1
    window.close()

main()
print('Program terminating normally')
