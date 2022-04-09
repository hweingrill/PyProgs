from PySimpleGUI import *
  
layout = [[Txt(''  * 10)],
          [Text('', size = (15, 1), font = ('Helvetica', 18),
                text_color = 'black', key = 'input')],
          [Txt(''  * 10)],
          [ReadFormButton('c'), ReadFormButton('«')],
          [ReadFormButton('7'), ReadFormButton('8'), ReadFormButton('9'), ReadFormButton('/')],
          [ReadFormButton('4'), ReadFormButton('5'), ReadFormButton('6'), ReadFormButton('*')],
          [ReadFormButton('1'), ReadFormButton('2'), ReadFormButton('3'), ReadFormButton('-')],
          [ReadFormButton('.'), ReadFormButton('0'), ReadFormButton('='), ReadFormButton('+')],
          ]
  
# Set PySimpleGUI
form = FlexForm('CALCULATOR', default_button_element_size = (5, 2),
                auto_size_buttons = False, grab_anywhere = False)
form.Layout(layout)
  
Result = ''                           # Result Value
  
while True:                           # Make Infinite Loop 
    button, value = form.Read()       # Button Values
      
    if button == 'c':                 
        Result = ''
        form.find_element('input').Update(Result)

    elif button=='«':
        Result = Result[:-1]
        form.find_element('input').Update(Result)
    elif len(Result) == 16 :
        pass
      
    elif button == '=':            # Ergebnis ausgeben
        Answer = eval(Result)      # eval: wertet z.B.: 5*6 9/3 aus
        Answer = str(round(float(Answer),3))
        form.find_element('input').Update(Answer)
        Result = Answer
          
    elif button == 'Quit'  or button == None:
        break
    else:
        Result += button
        form.find_element('input').Update(Result)
        print(Result, button)
