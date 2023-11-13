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
                    database="school")
db_cursor = db_connection.cursor(buffered=True)

# Canvas -----------------------------------------------------
w=800
h=800
root = Tk()
root.geometry("{}x{}".format(w,h))
canv = Canvas(root, width=w, height=h)
canv.pack(side="right")
canv.create_rectangle(0,0,w,h/4, fill='bisque', outline='')


# Labels -----------------------------------------------------
titleLabel = Label(root, text="Course Management", font=("Helvetica", 23), bg='bisque', fg="black", width=20).place(x=240, y=20)

nameLabel =Label(root, text="Course name: ", font=("Helvetica", 10), bg="dark grey", fg="white", width=20).place(x=50, y=120)
name=StringVar()
nameentry=Entry(root, textvariable=name, width=30, bg='white').place(x=250, y=120)

desclabel =Label(root, text="Description: ", font=("Helvetica", 10), bg="dark grey", fg="white", width=20).place(x=50, y=150)
desc =StringVar()
descentry=Entry(root, textvariable=desc, width=30, bg='white').place(x=250, y=150)

study =Label(root, text="Study: ", font=("Helvetica", 10), bg="dark grey", fg="white", width=20).place(x=50, y=180)
study =StringVar()
studyentry=Entry(root, textvariable=study, width=30, bg='white').place(x=250, y=180)

teacherlabel =Label(root, text="Teacher(s) last name: ", font=("Helvetica", 10), bg="dark grey", fg="white", width=20).place(x=50, y=210)
teacher=StringVar()
teacherentry=Entry(root, textvariable=teacher, width=30, bg='white').place(x=250, y=210)

credlabel =Label(root, text="Credits: ", font=("Helvetica", 10), bg="dark grey", fg="white", width=20).place(x=50, y=240)
cred=StringVar()
credrentry=Entry(root, textvariable=cred, width=30, bg='white').place(x=250, y=240)


def Register(): # should show all labelentries
    global name, desc, study, teacher, cred
    name=name.get()
    desc=desc.get()
    study=study.get()
    teacher=teacher.get()
    cred=cred.get()
    query=(" INSERT into course values ('{}','{}','{}','{}', '{}')".format(name, desc, study, teacher, cred))
    print(query)
    db_cursor.execute(query)
    db_connection.commit()
    print('done')

def Delete(): # should only show labelentries name, study
    global name,study
    name=name.get
    study=study.get
    query=(" DELETE from  course where name='{}' and study='{}'".format(name, study))
    print(query)
    db_cursor.execute(query)
    db_connection.commit()   
    print('done')


# Buttons ------------------------------------------------------------------------
btnRegister = Button(root, text="Register", font=("Helvetica", 10), bg="white", fg="dark grey", width=10, command=Register)  
btnRegister.place(x=400, y=70)
 
btnDelete = Button(root, text="Delete", font=("Helvetica", 10), bg="white", fg="dark grey", width=10, command=Delete)  
btnDelete.place(x=500, y=70)

# Treeview, shows the database ------------------------------------------
columns = ("#1", "#2", "#3", "#4")
studyTree = ttk.Treeview(root, show="headings",height="5", columns=columns)
studyTree.heading('#1', text='Name', anchor='center')  
studyTree.column('#1', width=70, anchor='center', stretch=False)  
studyTree.heading('#2', text='Description', anchor='center')  
studyTree.column('#2', width=70, anchor='center', stretch=False)  
studyTree.heading('#3', text='Language', anchor='center')  
studyTree.column('#3',width=80, anchor='center', stretch=False)  
studyTree.heading('#4', text='Number of Years', anchor='center')  
studyTree.column('#4',width=100, anchor='center', stretch=False)  
studyTree.place(x=50, y=350, height=200, width=650)

vsb= ttk.Scrollbar(root, orient=VERTICAL,command=studyTree.yview)  
vsb.place(x=50 + 650 + 1, y=350, height=180 + 20)  
studyTree.configure(yscroll=vsb.set)  
hsb = ttk.Scrollbar(root, orient=HORIZONTAL, command=studyTree.xview)  
hsb.place(x=50 , y=350+200+1, width=630 + 20)  
studyTree.configure(xscroll=hsb.set)  


# Buttoncommands for pages --------------------------
def OpenExam():
    root.destroy()
    subprocess.Popen([sys.executable, 'AdminExam.py'])
def OpenResults():
    root.destroy()
    subprocess.Popen([sys.executable, 'AdminResults.py'])
def OpenStudent():
    root.destroy()
    subprocess.Popen([sys.executable, 'AdminStudent.py'])
def OpenStudy():
    root.destroy()
    subprocess.Popen([sys.executable, 'AdminStudy.py'])
def OpenEmployees():
    root.destroy()
    subprocess.Popen([sys.executable, 'AdminEmployee.py'])
def Exit():
    root.destroy()
    subprocess.Popen([sys.executable, 'AdministratorProfile.py'])

# Page buttons --------------------------------------------
btnCourse = Button(root, text="Courses", font=("Helvetica", 10), bg="bisque", fg="black", activebackground='bisque', width=10).place(x=150, y=650)
btnExam = Button(root, text="Exams", font=("Helvetica", 10), bg="grey", fg="white", activebackground='bisque',width=10, command=OpenExam).place(x=250, y=650)  
btnResult = Button(root, text="Results", font=("Helvetica", 10), bg="grey", fg="white",activebackground='bisque', width=10, command=OpenResults).place(x=350, y=650)
btnStudent= Button(root, text="Students", font=("Helvetica", 10), bg="grey", fg="white", activebackground='bisque',width=10, command=OpenStudent).place(x=450, y=650) 
btnStudy= Button(root, text="Studies", font=("Helvetica", 10), bg="grey", fg="white", activebackground='bisque',width=10, command=OpenStudy).place(x=550, y=650)
btnEmployee= Button(root, text="Employees", font=("Helvetica", 10), bg="grey", fg="white", activebackground='bisque',width=10, command=OpenEmployees).place(x=650, y=650)  
btnExit= Button(root, text="Exit", font=("Helvetica", 10), bg="grey", fg="white", activebackground='bisque',width=10, command=Exit).place(x=650, y=710)

root.title("Admin Course Management")
root.mainloop()
