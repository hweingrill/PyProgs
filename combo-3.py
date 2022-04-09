import PySimpleGUI as sg
data={8223, 9224, 8334}
l = []
l.append('Byte |   Value | Attribute')
l.append('     0 |  %5d  | Re-Assigned Sector Count' % data(0))
l.append('     1 |  %5d  | Program Fail Count (Worst Case Component)' % 8224)
l.append('     2 |  %5d  | Program Fail Count (SSD Total)' % 8334)




while True:
    layout = [[sg.Listbox(l, size=(70, 6))]]
    sg.Window("Dell SMART Attributes",
              layout+[[sg.OK()]],
              font=('monospace', 12)).Read()
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
            break
window.close()

