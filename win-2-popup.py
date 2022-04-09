import PySimpleGUI as sg
import sys
while True:
    if len(sys.argv) == 1:
        event, values = sg.Window('My Script',
                    [[sg.Text('Document to open')],
                    [sg.In(), sg.FileBrowse('suchen')],
                    [sg.Open('aufmachen'), sg.Cancel()]]).read(close=True)
        fname = values[0]
    else:
        fname = sys.argv[1]
    
    if not fname:
        sg.popup("Cancel", "Keine Datei gewählt!")
        raise SystemExit("Cancelling: keine Datei gewählt")
    else:
        sg.popup('Die von dir gewähöte Datei: ', fname)



