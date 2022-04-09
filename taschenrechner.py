import PySimpleGUI as sg
 
class Calculator:
 
    def __init__(self):
        self.list_of_values = []
        self.list_of_operators = []
        self.result = 0
 
    def clear(self):
        self.list_of_values = []
        self.list_of_operators = []
        self.result = 0
 
    def add_value(self, value):
        self.list_of_values.append(float(value))
 
    def add_operator(self, operator):
        self.list_of_operators.append(operator)
 
    def return_result(self):
        self.result = self.list_of_values[0]
        for index in range(len(self.list_of_values)-1):
            operator = self.list_of_operators[index]
            if operator == '+':
                self.result += self.list_of_values[index+1]
            elif operator == '-':
                self.result -= self.list_of_values[index+1]
            elif operator == '*':
                self.result *= self.list_of_values[index+1]
            elif operator == '/':
                self.result /= self.list_of_values[index+1]
        return f'{self.result:.2f}'
 
 
class Gui:
 
    def __init__(self):
        self.BUTTON_SMALL = {'size': (4,2),'border_width': 1}
        self.BUTTON_LARGE = {'size': (10,2)}
        self.WINDOW_SIZE = (300, 344)
        self.GREY = '#e5e5e5'
        self.LIGHTGREY = '#f3f3f3'
        self.YELLOW = '#ffcc33'
        self.display = ''
        self.status = ''
        self.last_input = None
        self.result = None
 
        sg.SetOptions(button_color=('black', self.LIGHTGREY),
                      font=('Arial', 12),
                      background_color='white',
                      element_background_color='white',
                      input_text_color='black',
                      text_element_background_color='white',
                      input_elements_background_color='white',
                      element_padding=(6, 6)
                      )
 
        self.layout = [[sg.Graph(canvas_size=(300, 40), graph_bottom_left=(0,40), graph_top_right=(300,0),
                            background_color='white', key='_DESIGN_', pad=(0,0))],
                [sg.Text(size=(25, 1), justification='right', key='_DISPLAY_', border_width=2,
                                relief='sunk', text_color='black', font=('Arial', 20), pad=((20,20),(6,6)))],
                [sg.Button('7', pad=((20,6), (6,6)), **self.BUTTON_SMALL), sg.Button('8', **self.BUTTON_SMALL),
                   sg.Button('9', **self.BUTTON_SMALL), sg.Button('+', **self.BUTTON_LARGE)],
                [sg.Button('4', pad=((20,6), (6,6)), **self.BUTTON_SMALL), sg.Button('5', **self.BUTTON_SMALL),
                   sg.Button('6', **self.BUTTON_SMALL), sg.Button('-', **self.BUTTON_LARGE)],
                [sg.Button('1', pad=((20,6), (6,6)), **self.BUTTON_SMALL), sg.Button('2', **self.BUTTON_SMALL),
                   sg.Button('3', **self.BUTTON_SMALL), sg.Button('*', **self.BUTTON_LARGE)],
                [sg.Button('0', pad=((20,6), (6,6)), **self.BUTTON_SMALL), sg.Button('C', **self.BUTTON_SMALL),
                   sg.Button('=', focus = True, **self.BUTTON_SMALL), sg.Button('/', **self.BUTTON_LARGE)],
                [sg.Text(size=(60, 1), background_color=self.GREY, justification='right', key='_STATUS_',
                         pad=((0,0),(6,0)), font=('Arial', 7), text='', text_color='black')]]
 
        self.window = sg.Window('Taschenrechner', self.layout, default_button_element_size=(8,1), size=self.WINDOW_SIZE,
                                margins=(0,0))
        self.window.Finalize()
 
        design = self.window.FindElement('_DESIGN_')
 
        design.DrawRectangle((0,0), (300, 22), fill_color=self.YELLOW, line_width=0)
        design.DrawRectangle((0,25), (300, 35), fill_color=self.GREY, line_width=0)
 
        self.c = Calculator()
        self.start()
 
    def start(self):
 
        while True:
            event, values = self.window.read()
            if event in (None, 'Cancel'):
                break
 
            else:
                if event in '1 2 3 4 5 6 7 8 9 0'.split():
                    if self.last_input == 'numeric' or not self.last_input:
                        self.display += event
                        self.__show_display(self.display)
 
                    elif self.last_input == 'operation' or self.last_input == 'clear':
                        self.display = event
                        self.__show_display(self.display)
 
                    elif self.last_input == 'equal':
                        self.c.clear()
                        self.display = event
                        self.__show_display(self.display)
 
                    self.last_input = 'numeric'
 
                elif event in '+ - * /'.split():
                    if self.last_input == 'numeric':
                        self.c.add_value(self.display)
                        self.c.add_operator(event)
                        self.display += ' ' + event
                        self.__show_display(self.display)
                        self.status += ' ' + self.display
                        self.__show_status()
                        self.__clear_display()
 
                    elif self.last_input == 'equal':
                        self.c.clear()
                        self.c.add_value(self.result)
                        self.c.add_operator(event)
                        self.display += ' ' + event
                        self.status = self.result + ' ' + event
                        self.__show_status()
                        self.__show_display(self.display)
 
                    elif not self.last_input or self.last_input == 'operation' or self.last_input == 'clear':
                        self.__show_display('No Value Error')
                        self.status = ''
                        self.__show_status()
                        self.c.clear()
 
                    self.last_input = 'operation'
 
                elif event == '=':
                    if not self.last_input or self.last_input == 'equal' or self.last_input == 'operation' or \
                        self.last_input == 'clear':
                        self.__show_display('No Value Error')
                        self.status = ''
                        self.__show_status()
                        self.c.clear()
 
                    elif self.last_input == 'numeric':
                        self.c.add_value(self.display)
                        self.status += ' ' + self.display
                        try:
                            self.result = self.c.return_result()
                        except ZeroDivisionError:
                            self.__show_display('Zero Divison Error')
                            self.status = ''
                            self.__show_status()
                        else:
                            self.display = self.result
                            self.__show_display(self.display)
                            self.status += ' = ' + self.result
                            self.__show_status()
 
                    self.c.clear()
                    self.last_input = 'equal'
 
                elif event == 'C':
                    self.__clear_display()
                    self.__show_display(self.display)
                    self.status = ''
                    self.__show_status()
                    self.c.clear()
                    self.last_input = 'clear'
 
        self.window.close()
 
    def __clear_display(self):
        self.display = ''
 
    def __show_display(self, value):
        self.window.FindElement('_DISPLAY_').Update(value)
 
    def __show_status(self):
        self.window.FindElement('_STATUS_').Update(self.status)
 
Gui()
