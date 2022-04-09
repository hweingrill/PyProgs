import PySimpleGUI as sg

filename=r'c:\autoexec.bat'

layout = [[sg.Input('', key='cur_file', disabled=True, size=(20,1))], [sg.Button("OK")]]
window = sg.Window("demo", layout=layout)
window.Read()
window.Element('cur_file').Update(value=filename)
window.Element('cur_file').SetTooltip(filename)
window.Read()
window.Close()
