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

# Canvas ----------------------------------------------------
w=800
h=800
root = Tk()
root.geometry("{}x{}".format(w,h))
canv = Canvas(root, width=w, height=h)
canv.pack(side="right")
canv.create_rectangle(0,0,w,h/4, fill='cornflower blue', outline='')

# Get the teachernumber for 'travelling' between pages --------
teachernumber=sys.argv[1]

# Labels ------------------------------------------------------
titlelabel = Label(root, text="Result Management", font=("Helvetica", 23), bg="cornflowerblue", fg="white", width=20).place(x=240, y=30)

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


def Register(): #should show all labelentries
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
    
def Update(): #should only show labelentriess grade, student, exam
    global grade, student, exam
    grade=grade.get()
    student=student.get()
    exam=exam.get()
    query=("Update result set grade={} where student='{}' and exam='{}'".format(grade, student, exam))
    print(query)
    db_cursor.execute(query)
    db_connection.commit()
    print('done')

def Delete(): #should only show labelentries student, exam
    global student, exam
    student=student.get()
    exam=exam.get()
    query=(" DELETE from  result where student='{}' and exam='{}'".format(student, exam))
    print(query)
    db_cursor.execute(query)
    db_connection.commit()   
    print('done')


# Buttons ------------------------------------------------------------------------------
btnRegister = Button(root, text="Register", font=("Helvetica", 10), bg="white", fg="dark grey", width=10, command=Register)  
btnRegister.place(x=270, y=70)
btnUpdate = Button(root, text="Update", font=("Helvetica", 10), bg="white", fg="dark grey", width=10, command=Update)  
btnUpdate.place(x=370, y=70)
btnDelete = Button(root, text="Delete", font=("Helvetica", 10), bg="white", fg="dark grey", width=10, command=Delete)  
btnDelete.place(x=470, y=70)

# Treeview, shows the database ------------------------------------------------
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


# Buttoncommands for pages ----------------------------
def OpenProfile():
    root.destroy()
    subprocess.Popen([sys.executable, 'teacherProfile.py', teachernumber])
def OpenStudents():
    root.destroy()
    subprocess.Popen([sys.executable, 'teacherStudentProfiles.py', teachernumber])
def OpenSettings():
    root.destroy()
    subprocess.Popen([sys.executable, 'TeacherSettings.py', teachernumber])


# Page buttons --------------------------------------------
btnProfile = Button(root, text="My Profile", font=("Helvetica", 10), bg="grey", fg="white", activebackground='cornflower blue', width=10, command=OpenProfile)  
btnProfile.place(x=150, y=650)
btnStudent = Button(root, text="Students", font=("Helvetica", 10), bg="grey", fg="white", activebackground='cornflower blue',width=10, command=OpenStudents)
btnStudent.place(x=250, y=650)
btnGrades = Button(root, text="Grades", font=("Helvetica", 10), bg="cornflowerblue", fg="white",activebackground='cornflower blue', width=10) #no command, current page 
btnGrades.place(x=350, y=650)
btnSettings= Button(root, text="Settings", font=("Helvetica", 10), bg="grey", fg="white", activebackground='cornflower blue',width=10, command=OpenSettings)  
btnSettings.place(x=450, y=650)


root.title("Result management")
root.mainloop()
