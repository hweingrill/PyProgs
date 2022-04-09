import PySimpleGUI as sg
layout = [[sg.Text('Choose Options')],
            [sg.Checkbox('Save Posts', key="save-ed")],
                 [sg.Submit('Next'), sg.Cancel("Cancel")] ]

window = sg.Window('my bot', layout, icon="logo.ico")
event, values = window.read()

while True:
    event, values = window.read()
    print(event, values, )
    if event == sg.WIN_CLOSED or event == "Cancel":
        break
    if event == "save posts":
         
        if values['save-ed'] == True:
            save_input = values['usersave']
        elif values['save-ed'] == False:
            save_input = values['#usersave']
    if event == ['Next']:
        print(event, values, ('*'), save_input)
window.close()        
try:
    save_input = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[4]/div/div/button/div')
    save_input.click()
    sleep(randint(4,5))
except NoSuchElementException:
        pass
