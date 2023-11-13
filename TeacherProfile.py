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

# Canvas -----------------------------------------------------
w=800
h=800
root = Tk()
root.geometry("{}x{}".format(w,h))
canv = Canvas(root, width=w, height=h)
canv.pack(side="right")
canv.create_rectangle(0,0,w,h/4, fill='cornflowerblue', outline='')

# Get the teachernumber from login --------
teachernumber=sys.argv[1]
# Gets the lastname, and removes the extra characters (square brackets, commas, etc.) -----------------
db_cursor.execute("select lastname from teachers where teachernumber='{}'".format(teachernumber))
lastname = db_cursor.fetchall()
lastname = str(lastname)
lastname = lastname[3:-4]


# Fills the values with info from the database ---------------------
def Addprofile(teacherID):
    # Upper box -------------------------------------------------------------
    columns = ("1", "2", "3", "4", "5")
    studentTree = ttk.Treeview(root, show="headings",height="50", columns=columns)
    studentTree.heading('1', text='Birthdate', anchor='center')  
    studentTree.column('1', width=100, anchor='center', stretch=False)  
    studentTree.heading('2', text='Gender', anchor='center')  
    studentTree.column('2', width=80, anchor='center', stretch=False)  
    studentTree.heading('3', text='Adress', anchor='center')  
    studentTree.column('3',width=200, anchor='center', stretch=False)
    studentTree.heading('4', text='', anchor='center')  
    studentTree.column('4',width=200, anchor='center', stretch=False) 
    studentTree.column('5',width=200, anchor='center', stretch=False)

    db_cursor.execute("select dateofbirth from teachers where teachernumber='{}'".format(teachernumber))
    birthdate = db_cursor.fetchall()
    db_cursor.execute("select gender from teachers where teachernumber='{}'".format(teachernumber))
    gender = db_cursor.fetchall()
    db_cursor.execute("select street from teachers where teachernumber='{}'".format(teachernumber))
    street= db_cursor.fetchall()
    db_cursor.execute("select  streetnumber, postalcode, city from teachers where teachernumber='{}'".format(teachernumber))
    postalcode = db_cursor.fetchall()

    row=[]
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
    studentTree.column('6',width=150, anchor='center', stretch=False)
    studentTree.heading('7', text='Study', anchor='center')  
    studentTree.column('7', width=100, anchor='center', stretch=False)
    studentTree.heading('8', text='Courses', anchor='center')  
    studentTree.column('8',width=100, anchor='center', stretch=False)
    studentTree.heading('9', text='Counseling', anchor='center')  
    studentTree.column('9',width=200, anchor='center', stretch=False)
    
    db_cursor.execute("select phonenumber from teachers where teachernumber='{}'".format(teachernumber))
    phone = db_cursor.fetchall()
    db_cursor.execute("select email from teachers where teachernumber='{}'".format(teachernumber))
    email = db_cursor.fetchall()
    db_cursor.execute("select study from course where teacher=(select lastname from teachers where teachernumber='{}')".format(teachernumber))
    study = db_cursor.fetchall()
    db_cursor.execute("select name from course where teacher=(select lastname from teachers where teachernumber='{}')".format(teachernumber))
    courses= db_cursor.fetchall()
    db_cursor.execute("select firstname, lastname from students where studycounselor='{}'".format(teachernumber))
    counseling = db_cursor.fetchall()

    row=[]
    row.append(phone)
    row.append(email)
    row.append(study)
    row.append(courses)
    row.append(counseling)

    studentTree.insert('', tk.END, values= (row))
    studentTree.place(x=50, y=400, height=200, width=650)

    db_cursor.execute("select firstname, teachernumber  from teachers where teachernumber='{}'".format(teachernumber))
    name = db_cursor.fetchall()
    
    lblTitle = Label(root, text="Profile of {}".format(name[0][0]), font=('Arial', '30', 'bold'), bg='cornflowerblue', fg="white", width=20)
    lblTitle.place(x=150, y=30)


# Buttoncommands for pages --------------------------
def OpenStudents():
    root.destroy()
    subprocess.Popen([sys.executable, 'TeacherStudentProfiles.py', teachernumber])
def OpenGrades():
    root.destroy()
    subprocess.Popen([sys.executable, 'Teachergrades.py', teachernumber])
def OpenSettings():
    root.destroy()
    subprocess.Popen([sys.executable, 'TeacherSettings.py', teachernumber])

myframe = Frame(root)
myframe.pack()

# Page buttons --------------------------------------------
btnProfile = Button(root, text="My Profile", font=("Helvetica", 10), bg="cornflowerblue", fg="white", activebackground='cornflower blue', width=10)  
btnProfile.place(x=150, y=650)
btnStudent = Button(root, text="Students", font=("Helvetica", 10), bg="grey", fg="white", activebackground='cornflower blue',width=10, command=OpenStudents)
btnStudent.place(x=250, y=650)
btnGrades = Button(root, text="Grades", font=("Helvetica", 10), bg="grey", fg="white",activebackground='cornflower blue', width=10, command=OpenGrades) #no command, current page 
btnGrades.place(x=350, y=650)
btnSettings= Button(root, text="Settings", font=("Helvetica", 10), bg="grey", fg="white", activebackground='cornflower blue',width=10, command=OpenSettings)  
btnSettings.place(x=450, y=650)


Addprofile(teachernumber)
root.title("Teacher Profile")
root.mainloop()
