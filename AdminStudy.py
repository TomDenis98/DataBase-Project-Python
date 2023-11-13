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

#labels
TitleLabel = Label(root, text="Study Management", font=("Helvetica", 23), bg='bisque', fg="black", width=20).place(x=240, y=20)

nameLabel =Label(root, text="Name: ", font=("Helvetica", 10), bg="dark grey", fg="white", width=20).place(x=50, y=120)
name=StringVar()
nameentry=Entry(root, textvariable=name, width=30, bg='white').place(x=250, y=120)

desclabel =Label(root, text="Description: ", font=("Helvetica", 10), bg="dark grey", fg="white", width=20).place(x=50, y=150)
desc =StringVar()
descentry=Entry(root, textvariable=desc, width=30, bg='white').place(x=250, y=150)

language =Label(root, text="Language: ", font=("Helvetica", 10), bg="dark grey", fg="white", width=20).place(x=50, y=180)
language =StringVar()
languageentry=Entry(root, textvariable=language, width=30, bg='white').place(x=250, y=180)

yearlabel =Label(root, text="Number of Years: ", font=("Helvetica", 10), bg="dark grey", fg="white", width=20).place(x=50, y=210)
year=StringVar()
yearentry=Entry(root, textvariable=year, width=30, bg='white').place(x=250, y=210)

timelabel =Label(root, text="Fulltime:(Y/N) ", font=("Helvetica", 10), bg="dark grey", fg="white", width=20).place(x=50, y=240)
time =StringVar()
timeentry=Entry(root, textvariable=time, width=30, bg='white').place(x=250, y=240)


def Register(): # should show all labelentries
    global name, time, desc, language, year
    name=name.get()
    time=time.get()
    desc=desc.get()
    language=language.get()
    year=year.get()
    print(time)
    query=(" INSERT into study values ('{}', '{}', '{}','{}','{}')".format(name, time, desc, language, year))
    print(query)
    db_cursor.execute(query)
    db_connection.commit()
    print('done')


def Update(): # should only show labelentriess grade, student, exam
    global grade, student, exam
    grade=grade.get()
    student=student.get()
    exam=exam.get()
    query=("Update result set grade={} where student='{}' and exam='{}'".format(grade, student, exam))
    print(query)
    db_cursor.execute(query)
    db_connection.commit()
    print('done')


def Delete(): # should only show labelentries student, exam
    global student, exam
    student=student.get()
    exam=exam.get()
    query=(" DELETE from  result where student='{}' and exam='{}'".format(student, exam))
    print(query)
    db_cursor.execute(query)
    db_connection.commit()   
    print('done')


# Buttons ------------------------------------------------------------------------
btnRegister = Button(root, text="Create", font=("Helvetica", 10), bg="white", fg="dark grey", width=10, command=Register)  
btnRegister.place(x=200, y=70)
btnRegister = Button(root, text="Register", font=("Helvetica", 10), bg="white", fg="dark grey", width=10, command=Register)  
btnRegister.place(x=300, y=70)
btnUpdate = Button(root, text="Update", font=("Helvetica", 10), bg="white", fg="dark grey", width=10, command=Update)  
btnUpdate.place(x=400, y=70)
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
def OpenEmployees():
    root.destroy()
    subprocess.Popen([sys.executable, 'AdminEmployee.py'])
def Exit():
    root.destroy()
    subprocess.Popen([sys.executable, 'AdministratorProfile.py'])

#page buttons
btnCourse = Button(root, text="Courses", font=("Helvetica", 10), bg="grey", fg="white", activebackground='bisque', width=10, command=OpenCourse).place(x=150, y=650)
btnExam = Button(root, text="Exams", font=("Helvetica", 10), bg="grey", fg="white", activebackground='bisque',width=10, command=OpenExam).place(x=250, y=650)  
btnResult = Button(root, text="Results", font=("Helvetica", 10), bg="grey", fg="white",activebackground='bisque', width=10, command=OpenResult).place(x=350, y=650)
btnStudentb= Button(root, text="Students", font=("Helvetica", 10), bg="grey", fg="white", activebackground='bisque',width=10, command=OpenStudent).place(x=450, y=650) 
btnStudy = Button(root, text="Studies", font=("Helvetica", 10), bg="bisque", fg="black", activebackground='bisque',width=10).place(x=550, y=650)
btnEmployees = Button(root, text="Employees", font=("Helvetica", 10), bg="grey", fg="white", activebackground='bisque',width=10, command=OpenEmployees).place(x=650, y=650)  
btnExit = Button(root, text="Exit", font=("Helvetica", 10), bg="grey", fg="white", activebackground='bisque',width=10, command=Exit).place(x=650, y=710)

root.title("Admin Study Management")
root.mainloop()
