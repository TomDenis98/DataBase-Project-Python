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
Titlelabel = Label(root, text="Result Management", font=("Helvetica", 23), bg="bisque", fg="black", width=20).place(x=240, y=20)

gradelabel = Label(root, text="Grade: ", bg="dark grey", width=20).place(x=50, y=120)
grade=StringVar()
gradeentry= Entry(root, textvariable=grade, width=30, bg='white').place(x=200, y=120)

examlabel = Label(root, text="Exam: ", bg="dark grey", width=20).place(x=50, y=150)
exam=StringVar()
examentry= Entry(root, textvariable=exam, width=30, bg='white').place(x=200, y=150)

studentlabel = Label(root, text="Student lastname: ", bg="dark grey", width=20).place(x=50, y=180)
student=StringVar()
studententry= Entry(root, textvariable=student, width=30, bg='white').place(x=200, y=180)

passedlabel = Label(root, text="Passed: ", bg="dark grey", width=20).place(x=50, y=210)
passed=StringVar()
passedentry= Entry(root, textvariable=passed, width=30, bg='white').place(x=200, y=210)

datelabel = Label(root, text="Date: (YYYY-MM-DD): ", bg="dark grey", width=20).place(x=50, y=240)
date=StringVar()
dateentry= Entry(root, textvariable=date, width=30, bg='white').place(x=200, y=240)

weight = Label(root, text="Weight: ", bg="dark grey", width=20).place(x=50, y=270)
weight=StringVar()
weightentry= Entry(root, textvariable=weight, width=30, bg='white').place(x=200, y=270)


def Register(): 
    global grade, exam, date, weight, student, passed
    grade=grade.get()
    exam=exam.get()
    date=date.get()
    weight=weight.get()
    student=student.get()
    passed=passed.get()
    query=(" INSERT into result values ({}, '{}', '{}', {}, '{}', '{}') ".format(grade, exam, date, weight, student, passed))
    db_cursor.execute(query)
    db_connection.commit()



def Update(): 
    global grade, student, exam
    grade=grade.get()
    student=student.get()
    exam=exam.get()
    query=("Update result set grade={} where student='{}' and exam='{}'".format(grade, student, exam))
    print(query)
    db_cursor.execute(query)
    db_connection.commit()
    print('done')


def Delete():
    global student, exam
    student=student.get()
    exam=exam.get()
    query=(" DELETE from  result where student='{}' and exam='{}'".format(student, exam))
    print(query)
    db_cursor.execute(query)
    db_connection.commit()   
    print('done')


# Buttons ------------------------------------------------------------------------
btnRegister = Button(root, text="Register", font=("Helvetica", 10), bg="white", fg="dark grey", width=10, command=Register)  
btnRegister.place(x=300, y=70)
btnUpdate = Button(root, text="Update", font=("Helvetica", 10), bg="white", fg="dark grey", width=10, command=Update)  
btnUpdate.place(x=400, y=70)
btnDelete = Button(root, text="Delete", font=("Helvetica", 10), bg="white", fg="dark grey", width=10, command=Delete)  
btnDelete.place(x=500, y=70)

# Treeview, shows the database ------------------------------------------
columns = ("#1", "#2", "#3", "#4")
resultTree = ttk.Treeview(root, show="headings",height="5", columns=columns)
resultTree.heading('#1', text='Grade', anchor='center')  
resultTree.column('#1', width=60, anchor='center', stretch=False)  
resultTree.heading('#2', text='Exam', anchor='center')  
resultTree.column('#2', width=60, anchor='center', stretch=False)  
resultTree.heading('#3', text='Student', anchor='center')  
resultTree.column('#3',width=70, anchor='center', stretch=False)  
resultTree.heading('#4', text='Passed', anchor='center')  
resultTree.column('#4',width=60, anchor='center', stretch=False)
resultTree.place(x=50, y=350, height=200, width=650) 


# Buttoncommands for pages ----------------------------------------------------
def OpenCourse():
    root.destroy()
    subprocess.Popen([sys.executable, 'AdminCourse.py'])
def OpenExam():
    root.destroy()
    subprocess.Popen([sys.executable, 'AdminExam.py'])
def OpenResult():
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
btnCourse = Button(root, text="Courses", font=("Helvetica", 10), bg="grey", fg="white", activebackground='bisque', width=10, command=OpenCourse).place(x=150, y=650)
btnExam = Button(root, text="Exams", font=("Helvetica", 10), bg="grey", fg="white", activebackground='bisque',width=10, command=OpenExam).place(x=250, y=650)  
btnResult = Button(root, text="Results", font=("Helvetica", 10), bg="bisque", fg="black",activebackground='bisque', width=10).place(x=350, y=650)
btnStudent= Button(root, text="Students", font=("Helvetica", 10), bg="grey", fg="white", activebackground='bisque',width=10, command=OpenStudent).place(x=450, y=650) 
btnStudy= Button(root, text="Studies", font=("Helvetica", 10), bg="grey", fg="white", activebackground='bisque',width=10, command=OpenStudy).place(x=550, y=650) 
btnEmployee= Button(root, text="Employees", font=("Helvetica", 10), bg="grey", fg="white", activebackground='bisque',width=10, command=OpenEmployees).place(x=650, y=650)  
btnExit= Button(root, text="Exit", font=("Helvetica", 10), bg="grey", fg="white", activebackground='bisque',width=10, command=Exit).place(x=650, y=710)

root.title("Admin Grades Management")
root.mainloop()
