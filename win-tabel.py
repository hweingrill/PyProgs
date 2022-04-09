import PySimpleGUI as sg
                        # Listbox mit ok

l = []
l.append('Byte |   Value | Attribute')
l.append('     0 |  %5d  | Re-Assigned Sector Count' % 8223)
l.append('     1 |  %5d  | Program Fail Count (Worst Case Component)' % 8224)
l.append('     2 |  %5d  | Program Fail Count (SSD Total)' % 8334)


layout = [[sg.Listbox(l, size=(70, 6))]]
    
window=sg.Window("Dell SMART Attributes",
    layout+[[sg.OK('OK')]],
    font=('monospace', 12))#.Read()
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'OK':
            break
window.close()

