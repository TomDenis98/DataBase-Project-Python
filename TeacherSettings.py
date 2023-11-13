import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector
import subprocess
import sys

# Database connecting ----------------------------------
db_connection = mysql.connector.connect(  
host="localhost",  
user="root",  
password="root", # Enter your password
database="school")
db_cursor = db_connection.cursor(buffered=True)

# Get the teachernumber for 'travelling' between pages --------
teachernumber=sys.argv[1]

# Disclaimer Page -----------------------------------------
def Disclaimer():
    # Interface --------------------------------
    root.title('Disclaimer')
    discbg = Label(root, text=" ", width=500, height=500, bg='cornflowerblue').place(x=0,y=0)
    
    lblTitle = Label(root, text="Disclaimer", font=('Arial', '30', 'bold'), bg='cornflowerblue', fg="white")
    lblTitle.place(x=150, y=30)
    
    lblDisclaimer=Label(root,text="Diemen Academy exerts itself to keep the information   \n "
                              "on the websites and the apps actual. Despite this effort,\n "
                              "it could occur that the displayed information is incomplete \n"
                              " and/ or incorrect. Futhermore, the information could be  \n"
                              "adjusted and/or retracted at any time, without any \n"
                              " announcement. Consequently, no rights can be derived\n"
                              "from the websites and the apps of Diemen Academy \n"
                              " By using this app you agree to accept \n the disclaimer"
                              "without announcement",font=("Arial","9"),anchor="w").place(x=90,y=100)
    
    btnExit = Button(root, text="Exit", font=("Helvetica", 10), bg="grey", fg="white", activebackground='cornflowerblue', width=10,command=Exit)
    btnExit.place(x=325, y=400)

# Privacy Page -----------------------------------------
def Privacy():
    # Interface --------------------------------
    root.title('Privacy Statement')
    discbg = Label(root, text=" ", width=500, height=500, bg='cornflowerblue').place(x=0,y=0)
    
    lblTitle = Label(root, text="Privacy Statement", font=('Arial', '30', 'bold'), bg='cornflowerblue', fg="white")
    lblTitle.place(x=90, y=30)

    lblDisclaimer=Label(root,text="Diemen Academy is respecting the privacy of the app\n"
                              " useres and is assuring that the personal information \n "
                              "will be treated confidentially Personal information will \n"
                              "not be distributed among commercial institutions\n"
                              " for marketing purposes. By using this app you agree \n"
                              "to accept the Privacy.\n",font=("Arial","9"),anchor="w").place(x=100,y=100)

    btnExit = Button(root, text="Exit", font=("Helvetica", 10), bg="grey", fg="white", activebackground='cornflowerblue', width=10,command=Exit)
    btnExit.place(x=325, y=400)

def Exit():
    root.destroy()
    subprocess.Popen([sys.executable, 'TeacherSettings.py', teachernumber])

# Buttoncommands for pages ---------------------------------------
def OpenProfile():
    root.destroy()
    subprocess.Popen([sys.executable, 'TeacherProfile.py', teachernumber])
def OpenStudents():
    root.destroy()
    subprocess.Popen([sys.executable, 'TeacherStudentProfiles.py', teachernumber])
def OpenGrades():
    root.destroy()
    subprocess.Popen([sys.executable, 'Teachergrades.py', teachernumber])
    

# Canvas ----------------------------------------------------
w=500
h=500
root = Tk()
root.geometry("{}x{}".format(w,h))
canv = Canvas(root, width=w, height=h)
canv.pack(side="right")
canv.create_rectangle(0,0,w,h/4, fill='cornflowerblue', outline='')
canv.create_rectangle(100, 100, 400, 375, fill='whitesmoke', outline='lightgrey')

lblTitle = Label(root, text="Settings", font=('Arial', '30', 'bold'), bg='cornflowerblue', fg="white")
lblTitle.place(x=170, y=30)

myframe = Frame(root)
myframe.pack()

# Page buttons ------------------------------------------------------------
btnProfile = Button(root, text="My Profile", font=("Helvetica", 10), bg="grey", fg="white",activebackground='cornflowerblue', width=10, command=OpenProfile)  
btnProfile.place(x=70, y=400)
btnStudent = Button(root, text="Students", font=("Helvetica", 10), bg="grey", fg="white", activebackground='cornflower blue',width=10, command=OpenStudents)
btnStudent.place(x=170, y=400)
btnGrades = Button(root, text="Grades", font=("Helvetica", 10), bg="grey", fg="white", activebackground='cornflowerblue',width=10, command=OpenGrades)  
btnGrades.place(x=270, y=400)
btnSettings= Button(root, text="Settings", font=("Helvetica", 10), bg="cornflowerblue", fg="white", activebackground='cornflowerblue',width=10)
btnSettings.place(x=370, y=400)

# Settingsbuttons --------------------------------
btnDisclaimer= Button(root, text="Disclaimer", font=("Helvetica", 15), bg="grey", fg="white", activebackground='cornflowerblue',width=20, command=Disclaimer)  
btnDisclaimer.place(x=130, y=125)
btnPrivacy = Button(root, text="Privacy statement", font=("Helvetica", 15), bg="grey", fg="white",activebackground='cornflowerblue', width=20, command=Privacy)  
btnPrivacy.place(x=130, y=225)


root.title("Settings")
root.mainloop()
