import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector
import subprocess
import sys

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


root = Tk()
root.geometry('800x800')

canv = Canvas(root, width=800, height=800)
canv.pack(side='right')
canv.create_rectangle(0,0,800,200, fill='bisque', outline='')

lblTitle = Label(root, text="Diemen Academy", font=("Helvetica", 23), bg='bisque', fg="white")
lblTitle.place(x=20, y=10)
lblAdmin = Label(root, text="Profile of Admin", font=("Arial", 32, 'bold'), bg='bisque', fg='black').place(x=220, y=70)

btnCourse = Button(canv, text = "Course Management", command = OpenCourse, width=20, font=("Helvetica", 10), fg='white', bg='grey', activebackground='bisque')
btnCourse.place(x=60, y=210)
btnExam = Button(canv, text = "Exam Management", command = OpenExam, width=20, font=("Helvetica", 10), fg='white', bg='grey', activebackground='bisque')
btnExam.place(x=60, y=250)
btnResult = Button(canv, text = "Result Management", command = OpenResult, width=20, font=("Helvetica", 10), fg='white', bg='grey', activebackground='bisque')
btnResult.place(x=60, y=290)
btnStudent = Button(canv, text = "Student Management", command = OpenStudent, width=20, font=("Helvetica", 10), fg='white', bg='grey', activebackground='bisque')
btnStudent.place(x=60, y=330)
btnStudy = Button(canv, text = "Study Management", command = OpenStudy, width=20, font=("Helvetica", 10), fg='white', bg='grey', activebackground='bisque')
btnStudy.place(x=60, y=370)
btnEmployee = Button(canv, text = "Employee Management", command = OpenEmployees, width=20, font=("Helvetica", 10), fg='white', bg='grey', activebackground='bisque')
btnEmployee.place(x=60, y=410)




btnExit = Button(root, text="Exit", font=("Helvetica", 10), bg="grey", fg="white", activebackground='bisque',width=10, command=Exit).place(x=650, y=710)

root.title('Administrator Profile')
root.mainloop()


