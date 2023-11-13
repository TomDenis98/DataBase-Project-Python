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
titlelabel = Label(root, text="Exam Management", font=("Helvetica", 23), bg="bisque", fg="black", width=20).place(x=240, y=20)

courselabel =Label(root, text="Course: ", font=("Helvetica", 10), bg="dark grey", fg="white", width=20).place(x=50,y=120)
course=StringVar()
courseentry=Entry(root, textvariable=course, width=30, bg='white').place(x=250, y=120)

roomlabel= Label(root, text="Room: ", font=("Helvetica", 10), bg="dark grey", fg="white", width=20).place(x=50, y=150)
room= StringVar()
roomentry= Entry(root, textvariable=room, width=30, bg='white').place(x=250, y=150)

resitlabel =Label(root, text="Resit (Y/N): ", font=("Helvetica", 10), bg="dark grey", fg="white", width=20).place(x=50, y=180)
resit=StringVar()
resitentry= Entry(root, textvariable=resit, width=30, bg='white').place(x=250, y=180)

datelabel =Label(root, text="Date (YYYY-MM-DD): ", font=("Helvetica", 10), bg="dark grey", fg="white", width=20).place(x=50, y=210)
date=StringVar()
dateentry=Entry(root, textvariable=date, width=30, bg='white').place(x=250, y=210)

timelabel =Label(root, text="Time (24Hr Clock): ", font=("Helvetica", 10), bg="dark grey", fg="white", width=20).place(x=50, y=240)
time=StringVar()
timeentry=Entry(root, textvariable=time, width=30, bg='white').place(x=250, y=240)


def Register(): 
    global course, room, resit, date, time
    course=course.get()
    room=room.get()
    resit=resit.get()
    date=date.get()
    time=time.get()
    query=(" INSERT into exam values ('{}', '{}', '{}', '{}', '{}') ".format(course, room, resit, date, time))
    print(query)
    db_cursor.execute(query)
    db_connection.commit()
    print('done')


def Update(): 
    global room, course, date
    room=room.get()
    course=course.get()
    date=date.get()
    query=("Update exam set room ='{}' where course='{}' and date='{}'".format(room, course, date))
    print(query)
    db_cursor.execute(query)
    db_connection.commit()
    print('done')


def Delete(): #gives error
    global course, date
    course=course.get
    date=date.get
    query=(" DELETE from  exam where course='{}' and date='{}'".format(course, date))
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
columns = ("#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9", "#10", "#11", "#12", "#13", "#14")
examTree = ttk.Treeview(root, show="headings",height="5", columns=columns)
examTree.heading('#1', text='Course', anchor='center')  
examTree.column('#1', width=60, anchor='center', stretch=False)  
examTree.heading('#2', text='Room', anchor='center')  
examTree.column('#2', width=60, anchor='center', stretch=False)  
examTree.heading('#3', text='Resit', anchor='center')  
examTree.column('#3',width=60, anchor='center', stretch=False)  
examTree.heading('#4', text='Date', anchor='center')  
examTree.column('#4',width=60, anchor='center', stretch=False)  
examTree.heading('#5', text='Time', anchor='center')  
examTree.column('#5',width=60, anchor='center', stretch=False)  
examTree.place(x=50, y=400, height=200, width=650)

vsb= ttk.Scrollbar(root, orient=VERTICAL,command=examTree.yview)  
vsb.place(x=50 + 650 + 1, y=400, height=180 + 20)  
examTree.configure(yscroll=vsb.set)  
hsb = ttk.Scrollbar(root, orient=HORIZONTAL, command=examTree.xview)  
hsb.place(x=50 , y=400+200+1, width=630 + 20)  
examTree.configure(xscroll=hsb.set)  



# Buttoncommands for pages -----------------------------------------------
def OpenCourse():
    root.destroy()
    subprocess.Popen([sys.executable, 'AdminCourse.py'])
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


#page buttons 
btnCourse = Button(root, text="Courses", font=("Helvetica", 10), bg="grey", fg="white", activebackground='bisque', width=10, command=OpenCourse).place(x=150, y=650)
btnExam = Button(root, text="Exams", font=("Helvetica", 10), bg="bisque", fg="black", activebackground='bisque',width=10).place(x=250, y=650) 
btnResult = Button(root, text="Results", font=("Helvetica", 10), bg="grey", fg="white",activebackground='bisque', width=10,  command=OpenResult).place(x=350, y=650) 
btnStudent= Button(root, text="Students", font=("Helvetica", 10), bg="grey", fg="white", activebackground='bisque',width=10, command=OpenStudent).place(x=450, y=650) 
btnStudy= Button(root, text="Studies", font=("Helvetica", 10), bg="grey", fg="white", activebackground='bisque',width=10, command=OpenStudy).place(x=550, y=650) 
btnEmployee= Button(root, text="Employees", font=("Helvetica", 10), bg="grey", fg="white", activebackground='bisque',width=10, command=OpenEmployees).place(x=650, y=650)  
btnExit= Button(root, text="Exit", font=("Helvetica", 10), bg="grey", fg="white", activebackground='bisque',width=10, command=Exit).place(x=650, y=710)



root.title("Admin Exam Management")
root.mainloop()
