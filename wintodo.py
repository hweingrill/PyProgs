import PySimpleGUI as sg

def ToDoItem(num):
    #return [sg.Text(f'{num}. '), sg.CBox(''), sg.In()]
    return [sg.Text(f'{num}. '),  sg.In()]

layout = [ToDoItem(x) for x in range(1,7)]+[[sg.Button('Save'), sg.Button('Exit')]]

window = sg.Window('LST - Berechnung', layout)   
event, values = window.read()


