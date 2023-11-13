import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector
import subprocess
import sys

# Database connecting -------------------------------------
db_connection = mysql.connector.connect(  
    host="localhost",  
    user="root",  
    password="root", # Enter your password
    database="school"
    )
db_cursor = db_connection.cursor(buffered=True)

# Canvas -----------------------------------------------------
w=800
h=800
root = Tk()
root.geometry("{}x{}".format(w,h))
canv = Canvas(root, width=w, height=h)
canv.pack(side="right")
canv.create_rectangle(0,0,w,h/4, fill='deep pink', outline='')
 
# Get the studentnumber from login --------
studentnumber=sys.argv[1]

# Fills the values with info from the database ---------------------
def Addprofile(studentnumber):
    # Upper box -------------------------------------------------------------
    columns = ("1", "2", "3", "4", "5")
    studentTree = ttk.Treeview(root, show="headings",height="50", columns=columns)
    studentTree.heading('1', text='Studentnumber', anchor='center')  
    studentTree.column('1', width=100, anchor='center', stretch=False)  
    studentTree.heading('2', text='Birthdate', anchor='center')  
    studentTree.column('2', width=80, anchor='center', stretch=False)  
    studentTree.heading('3', text='Gender', anchor='center')  
    studentTree.column('3',width=80, anchor='center', stretch=False)
    studentTree.heading('4', text='Adress', anchor='center')  
    studentTree.column('4',width=200, anchor='center', stretch=False) 
    studentTree.column('5',width=200, anchor='center', stretch=False)

    db_cursor.execute("select dateofbirth from students where studentnumber='{}'".format(studentnumber))
    birthdate = db_cursor.fetchall()
    db_cursor.execute("select gender  from students where studentnumber='{}'".format(studentnumber))
    gender = db_cursor.fetchall()
    db_cursor.execute("select street from students where studentnumber='{}'".format(studentnumber))
    street= db_cursor.fetchall()
    db_cursor.execute("select  streetnumber, postalcode, city   from students where studentnumber='{}'".format(studentnumber))
    postalcode = db_cursor.fetchall()

    row=[]
    row.append(studentnumber)
    row.append(birthdate[0])
    row.append(gender[0])
    row.append(street[0][0])
    row.append(postalcode[0])

    studentTree.insert('', tk.END, values= (row))
    studentTree.place(x=50, y=100, height=200, width=650)

    #Lower box -------------------------------------------------------------
    columns = ("5", "6", "7", "8", "9", "10")
    studentTree = ttk.Treeview(root, show="headings",height="50", columns=columns)
    studentTree.heading('5', text='Phone', anchor='center')  
    studentTree.column('5',width=100, anchor='center', stretch=False)
    studentTree.heading('6', text='Email', anchor='center')  
    studentTree.column('6',width=100, anchor='center', stretch=False)
    studentTree.heading('7', text='Study', anchor='center')  
    studentTree.column('7', width=200, anchor='center', stretch=False)
    studentTree.heading('8', text='Enrollment', anchor='center')  
    studentTree.column('8',width=100, anchor='center', stretch=False)
    studentTree.heading('9', text='Counselor', anchor='center')  
    studentTree.column('9',width=100, anchor='center', stretch=False)
    
    db_cursor.execute("select phonenumber from students where studentnumber='{}'".format(studentnumber))
    phone = db_cursor.fetchall()
    db_cursor.execute("select email from students where studentnumber='{}'".format(studentnumber))
    email = db_cursor.fetchall()
    db_cursor.execute("select study from students where studentnumber='{}'".format(studentnumber))
    study = db_cursor.fetchall()
    db_cursor.execute("select startyear  from students where studentnumber='{}'".format(studentnumber))
    enrollment = db_cursor.fetchall()
    db_cursor.execute("select firstname, lastname from teachers where lastname=(select studycounselor from students where studentnumber='{}')".format(studentnumber))
    counselor = db_cursor.fetchall()

    row=[]
    row.append(phone)
    row.append(email)
    row.append(study)
    row.append(enrollment)
    row.append(counselor[0])

    studentTree.insert('', tk.END, values= (row))
    studentTree.place(x=50, y=400, height=200, width=650)

    db_cursor.execute("select firstname, studentnumber  from students where studentnumber='{}'".format(studentnumber))
    name = db_cursor.fetchall()

    lblTitle = Label(root, text="Profile of {}".format(name[0][0]), font=('Arial', '30', 'bold'), bg='deeppink', fg="white", width=20)
    lblTitle.place(x=150, y=30)


# Buttoncommands for pages --------------------------
def OpenGrades():
    root.destroy()
    subprocess.Popen([sys.executable, 'Grades.py', studentnumber])
def OpenSettings():
    root.destroy()
    subprocess.Popen([sys.executable, 'Settings.py', studentnumber])

myframe = Frame(root)
myframe.pack()

# Page buttons --------------------------------------------
btnProfile = Button(root, text="My Profile", font=("Helvetica", 10), bg="deeppink", fg="white",activebackground='deeppink', width=10)#no command, current page  
btnProfile.place(x=250, y=650)
btnGrades = Button(root, text="Grades", font=("Helvetica", 10), bg="grey", fg="white", activebackground='deeppink',width=10, command=OpenGrades)  
btnGrades.place(x=350, y=650)
btnSettings= Button(root, text="Settings", font=("Helvetica", 10), bg="grey", fg="white", activebackground='deeppink',width=10, command=OpenSettings)  
btnSettings.place(x=450, y=650)


Addprofile(studentnumber) 
root.title("Profile")
root.mainloop()
