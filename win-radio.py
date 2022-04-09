import PySimpleGUI as sg
layout = [[sg.T("")],[sg.T("        "), sg.Button('Hello World',size=(20,4))], [sg.T("")],
          [sg.T("         "), sg.Checkbox('Print On:', default=True, key="-IN-")],
          [sg.T("         "), sg.Radio('Permission Granted', "RADIO1", default=False, key="-IN2-")],
          [sg.T("         "), sg.Radio('Permission not Granted', "RADIO1", default=True)]]

###Setting Window
window = sg.Window('Push my Buttons', layout, size=(300,300))

###Showing the Application, also GUI functions can be placed here.

while True:
    event, values = window.read()
    print(event,values)
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif values["-IN-"] == True and values["-IN2-"] == True:
        print("Hello World!")
    
window.close()
