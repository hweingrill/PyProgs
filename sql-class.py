from tkinter import *
from tkinter import messagebox as ms
from tkinter import ttk
import sqlite3
#from PIL import Image,ImageTk
import datetime

global time 
time = datetime.datetime.now()

with sqlite3.connect('Gym.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS Users (UserID INTEGER PRIMARY KEY,FirstName TEXT ,LastName TEXT ,Gender TEXT,Email TEXT NOT NULL,Phone TEXT NOT NULL,Username TEXT NOT NULL,Password TEXT NOT NULL);')
c.execute('CREATE TABLE IF NOT EXISTS Staff (StaffID INTEGER PRIMARY KEY, Role TEXT NOT NULL, Name TEXT);')
c.execute('CREATE TABLE IF NOT EXISTS Gym (GymID INTEGER PRIMARY KEY, Location TEXT);')
c.execute('CREATE TABLE IF NOT EXISTS Class (ClassID INTEGER PRIMARY KEY, ClassType TEXT, Location TEXT, UserID INTEGER, Staff TEXT, StaffID INTEGER, Time TEXT, FOREIGN KEY (UserID) REFERENCES Users(UserID), FOREIGN KEY (StaffID) REFERENCES Staff (StaffID));')
db.commit()
db.close()

class main:
    def __init__(self,master):
        self.master = master
        self.variable_edit_class = StringVar()
        self.variable_edit_time = StringVar()
        self.variable_edit_location = StringVar()
        self.variable_edit_staff = StringVar()
        self.widgets()

def edit_sql(self):
    username = self.Username.get()
    password = self.Password.get()
    classes = self.variable_edit_class.get()
    location = self.variable_edit_location.get()
    time = self.variable_edit_time.get()
    staff = self.variable_staff.get()

    with sqlite3.connect('Gym.db') as db:
        c = db.cursor()

    c.execute('SELECT UserID FROM Users WHERE Username = (?) AND Password =(?)', (str(username),str(password)))

    result = c.fetchall()
    for row in result:
        r = row[0]
        print(row)

    e_sql= "UPDATE Class SET (ClassType,Location,UserID,Staff,Time) VALUES (?,?,?,?,?)"
    c.execute(e_sql,(classes,location,r,staff,time))

def widgets(self):
    self.editf = Frame(self.master, height=500,width=600)

    green_label_12 = Label(self.editf,text = "", font=('arial',15),fg='black',bg='light sea green',width=600,height=3)
    green_label_12.place(x=0,y=5)

    edit_class_label = Label(self.editf, text = "Class Bookings", font =('arial',15, 'bold'),fg = 'black',bg = 'light sea green')
    edit_class_label.place(x=220,y=20)

    back_btn11 = Button(self.editf, text ='Back', width = 5,bg = 'brown', command=self.dashboard)
    back_btn11.place(x=10,y=465)

    edit_classes_label = Label(self.editf, text = "Class", font =('arial',15),fg = 'black')
    edit_classes_label.place(x=25,y=110)

    edit_time_label = Label(self.editf, text = "Time", font =('arial',15),fg = 'black')
    edit_time_label.place(x=250,y=110)

    edit_location_label = Label(self.editf, text = "Location", font =('arial',15),fg = 'black')
    edit_location_label.place(x=25,y=200)

    edit_staff_label = Label(self.editf, text = "Staff", font =('arial',15),fg = 'black')
    edit_staff_label.place(x=260,y=200)

    Edit_Classes = [
        "Boxing",
        "Cardio",
        "Gym",
        "Strength",
        "Swim",
        "Yoga"
        ]


    self.variable_edit_class.set("Please Select")

    edit_booking_options = OptionMenu(self.editf,self.variable_edit_class,*Edit_Classes)
    edit_booking_options.place(x=90,y=110)

    Edit_Times = [
        "8:00 AM",
        "9:00 AM",
        "10:00 AM",
        "11:00 AM",
        "12:00 PM",
        "1:00 PM",
        "2:00 PM",
        "3:00 PM",
        "4:00 PM",
        "5:00 PM",
        "6:00 PM"
        ]

    self.variable_edit_time.set("Please Select")

    edit_time_options = OptionMenu(self.editf,self.variable_edit_time,*Edit_Times)
    edit_time_options.place(x=315,y=110)

    Edit_Location = [
        "Carrara",
        "Nerang",
        "Robina",
        "Helensvale"
        ]


    self.variable_edit_location.set("Please Select")

    edit_location_options = OptionMenu(self.editf,self.variable_edit_location,*Edit_Location)
    edit_location_options.place(x=115,y=200)

    Edit_Staff = [
            "Any",
            "John Cena",
            "Mike Tyson",
            "The Rock",
            "Terry Crews",
            "Mr George",
            "None"
            ]

    self.variable_edit_staff.set("Please Select")
    edit_staff_options = OptionMenu(self.editf,self.variable_edit_staff,*Edit_Staff)
    edit_staff_options.place(x=325,y=200)

    submit_btn_4 = Button(self.editf, text ='Update', width = 6,bg = 'dodger blue', command=self.edit_sql)
    submit_btn_4.place(x=535,y=470)


root = Tk()
