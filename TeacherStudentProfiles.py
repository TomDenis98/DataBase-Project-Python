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
canv.create_rectangle(0,0,w,h/4, fill='cornflower blue', outline='')

# Get the teachernumber for 'travelling' between pages --------
teachernumber=sys.argv[1]

# Look up students box --------------------------------------------------
studentnumberlabel = Label(root, text="Search studentnumber", bg="dark grey", width=20).place(x=50, y=120)
studentnumber=StringVar()
studentnumberentry= Entry(root, textvariable=studentnumber, width=30, bg='white').place(x=200, y=120)
studentnumber='1612400' 

# Outline box of values ---------------------------------------------------
# Upper box -----------------------------------------------------------------
columns = ("#1", "#2", "#3", "#4")
studentTree = ttk.Treeview(root, show="headings",height="50", columns=columns)
studentTree.heading('#1', text='Subject', anchor='center')  
studentTree.column('#1', width=200, anchor='center', stretch=False)  
studentTree.heading('#2', text='Grade', anchor='center')  
studentTree.column('#2', width=100, anchor='center', stretch=False)  
studentTree.heading('#3', text='Weight', anchor='center')  
studentTree.column('#3',width=100, anchor='center', stretch=False)
studentTree.heading('#4', text='Date', anchor='center')  
studentTree.column('#4',width=200, anchor='center', stretch=False)


# Fills the values with info from the database ---------------------
def Addgrades(studentnumber):
    print(studentnumber)
    db_cursor.execute("select firstname from students where studentnumber='{}'".format(studentnumber))
    firstname = db_cursor.fetchall()
    db_cursor.execute("select exam from result where student=(select lastname from students where studentnumber='{}')".format(studentnumber))
    courselist=db_cursor.fetchall()
    
    for course in courselist:
        db_cursor.execute("select grade from result where student=(select lastname from students where studentnumber='{}') and exam='{}'".format(studentnumber, course[0]))
        grade = db_cursor.fetchall()
        db_cursor.execute("select weight from result where student=(select lastname from students where studentnumber='{}') and exam='{}'".format(studentnumber, course[0]))
        weight = db_cursor.fetchall()
        db_cursor.execute("select date from result where student=(select lastname from students where studentnumber='{}') and exam='{}'".format(studentnumber, course[0]))
        date = db_cursor.fetchall()

        row=[]
        row.append(course[0])
        row.append(grade)
        row.append(weight)
        row.append(date)

        studentTree.insert('', tk.END, values= (row))       
        studentTree.place(x=50, y=100, height=200, width=650)

        lblTitle = Label(root, text="Student information of {}".format(firstname[0][0]), font=('Arial', '30', 'bold'), bg='cornflowerblue', fg="white", width=30)
        lblTitle.place(x=0, y=30)

vsb= ttk.Scrollbar(root, orient=VERTICAL,command=studentTree.yview)  
vsb.place(x=50 + 650 + 1, y=100, height=500)  
studentTree.configure(yscroll=vsb.set) 

#Lower box --------------------------------------------------
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
row.append(birthdate)
row.append(gender[0])
row.append(street[0][0])
row.append(postalcode[0])

studentTree.insert('', tk.END, values= (row))
studentTree.place(x=50, y=900, height=900, width=350)


# Buttoncommands for pages --------------------------
def OpenProfile():
    root.destroy()
    subprocess.Popen([sys.executable, 'TeacherProfile.py', teachernumber])
def OpenSettings():
    root.destroy()
    subprocess.Popen([sys.executable, 'TeacherSettings.py', teachernumber])
def OpenGrades():
    root.destroy()
    subprocess.Popen([sys.executable, 'Teachergrades.py', teachernumber])

# Page buttons --------------------------------------------
btnProfile = Button(root, text="My Profile", font=("Helvetica", 10), bg="grey", fg="white", activebackground='cornflower blue', width=10, command=OpenProfile)  
btnProfile.place(x=150, y=650)
btnStudent = Button(root, text="Students", font=("Helvetica", 10), bg="cornflowerblue", fg="white", activebackground='cornflower blue',width=10) #no command, already here 
btnStudent.place(x=250, y=650)
btnGrades = Button(root, text="Grades", font=("Helvetica", 10), bg="grey", fg="white",activebackground='cornflower blue', width=10, command=OpenGrades)  
btnGrades.place(x=350, y=650)
btnSettings= Button(root, text="Settings", font=("Helvetica", 10), bg="grey", fg="white", activebackground='cornflower blue',width=10, command=OpenSettings)  
btnSettings.place(x=450, y=650)


Addgrades(studentnumber) 
root.title("Student information")
root.mainloop()
