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
TitleLabel = Label(root, text="Employee Management", font=("Helvetica", 23), bg='bisque', fg="black", width=20).place(x=240, y=20)

fnameLabel =Label(root, text="First name: ", font=("Helvetica", 10), bg="dark grey", fg="white", width=20).place(x=50, y=120)
fname=StringVar()
fnameentry=Entry(root, textvariable=fname, width=30, bg='white').place(x=250, y=120)

lnameLabel =Label(root, text="Last name: ", font=("Helvetica", 10), bg="dark grey", fg="white", width=20).place(x=50, y=150)
lname=StringVar()
lnameentry=Entry(root, textvariable=lname, width=30, bg='white').place(x=250, y=150)

birthlabel =Label(root, text="Birthdate (YYYY-MM-DD): ", font=("Helvetica", 10), bg="dark grey", fg="white", width=20).place(x=50, y=180)
birth =StringVar()
birthentry=Entry(root, textvariable=birth, width=30, bg='white').place(x=250, y=180)

nationalitylabel =Label(root, text="Nationality: ", font=("Helvetica", 10), bg="dark grey", fg="white", width=20).place(x=50, y=210)
nationality =StringVar()
naionalityentry=Entry(root, textvariable=nationality, width=30, bg='white').place(x=250, y=210)

genderlabel =Label(root, text="Gender: ", font=("Helvetica", 10), bg="dark grey", fg="white", width=20).place(x=50, y=240)
gender=StringVar()
genderentry=Entry(root, textvariable=gender, width=30, bg='white').place(x=250, y=240)

streetlabel =Label(root, text="Street: ", font=("Helvetica", 10), bg="dark grey", fg="white", width=20).place(x=50, y=270)
street=StringVar()
streetentry=Entry(root, textvariable=street, width=30, bg='white').place(x=250, y=270)

nolabel =Label(root, text="Streetnumber: ", font=("Helvetica", 10), bg="dark grey", fg="white", width=20).place(x=50, y=300)
no=StringVar()
noentry=Entry(root, textvariable=no, width=30, bg='white').place(x=250, y=300)

postlabel =Label(root, text="Postal code ", font=("Helvetica", 10), bg="dark grey", fg="white", width=20).place(x=50, y=330)
post=StringVar()
postentry=Entry(root, textvariable=post, width=30, bg='white').place(x=250, y=330)

citylabel =Label(root, text="City: ", font=("Helvetica", 10), bg="dark grey", fg="white", width=20).place(x=50, y=360)
city=StringVar()
cityentry=Entry(root, textvariable=city, width=30, bg='white').place(x=250, y=360)

phonelabel =Label(root, text="Phonenumber: ", font=("Helvetica", 10), bg="dark grey", fg="white", width=20).place(x=50, y=390)
phone=StringVar()
phoneentry=Entry(root, textvariable=phone, width=30, bg='white').place(x=250, y=390)

emaillabel =Label(root, text="Personal emailadress: ", font=("Helvetica", 10), bg="dark grey", fg="white", width=20).place(x=50, y=420)
email=StringVar()
emailentry=Entry(root, textvariable=email, width=30, bg='white').place(x=250, y=420)

counselorlabel =Label(root, text="Study Counselor (Y/N)", font=("Helvetica", 10), bg="dark grey", fg="white", width=20).place(x=50, y=450)
counselor=StringVar()
counselorentry=Entry(root, textvariable=counselor, width=30, bg='white').place(x=250, y=450)

salarylabel =Label(root, text="Salary", font=("Helvetica", 10), bg="dark grey", fg="white", width=20).place(x=50, y=480)
salary=StringVar()
salaryentry=Entry(root, textvariable=salary, width=30, bg='white').place(x=250, y=480)


def Register(): 
    global fname, lname, birth, nationality, gender, street, no, post, city, phone,  salary, counselor, email
    fname=fname.get()
    lname=lname.get()
    birth=birth.get()
    nationality=nationality.get()
    gender=gender.get()
    street=street.get()
    no=no.get()
    post=post.get()
    city=city.get()
    phone=phone.get()
    salary=salary.get()
    counselor=counselor.get()
    email=email.get()
    query=(" INSERT into teachers values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}', 'Y','personalmail', 'test@teacher.diemenacademy.nl', 'iamteaching', '12345')"
    .format(fname, lname, birth, nationality, gender, street, no, post, city, phone, salary, counselor, email))
    print(query)
    db_cursor.execute(query)
    db_connection.commit()

    # Creating the teachernumbers ------------------------------------------
    number1 = []
    number2 = 86 
    number3 = []

    #First Number ------------------------------------------
    if gender[0][0]=='M' or 'm':
        number1=2
    if gender[0][0]=='F' or 'f':
        number1=8
    else:
        number1=4
    # can't implement secondnumber, study
    
    # Third Number ---------------------------------------
    birth=str(birth)
    birth=int((birth[2:4])+(birth[8:10]))
    birth/=2
    number3=int(birth)

    # Putting the numbers together ----------------------
    teachernr=str(number1)+ str(number2) + str(number3)+'0000' #the 0's fill up numbers that are too short
    teachernr=(teachernr[0:6]) #here all numbers get trimmed to equal length

    db_cursor.execute("Update teachers set teachernumber={} where lastname='{}';".format(teachernr, lname[0]))
    db_connection.commit()  
    print(name, teachernr, 'done')


def Delete(): # should only get fname, lname, birth
    global fname, lname, birth
    fname=fname.get()
    lname=lname.get()
    birth=birth.get()
    query=(" delete from teachers where firstname='{}' and lastname='{}' and dateofbirth='{}'".format(fname, lname, birth))
    db_cursor.execute(query)
    db_connection.commit()   
    print('done')


# Buttons ------------------------------------------------------------------------
btnRegister = Button(root, text="Register", font=("Helvetica", 10), bg="white", fg="dark grey", width=10, command=Register)  
btnRegister.place(x=400, y=70)

btnDelete = Button(root, text="Delete", font=("Helvetica", 10), bg="white", fg="dark grey", width=10, command=Delete)  
btnDelete.place(x=500, y=70)

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
def Exit():
    root.destroy()
    subprocess.Popen([sys.executable, 'AdministratorProfile.py'])

# Page buttons --------------------------------------------
btnCourse = Button(root, text="Courses", font=("Helvetica", 10), bg="grey", fg="white", activebackground='bisque', width=10, command=OpenCourse).place(x=150, y=650)
btnExam = Button(root, text="Exams", font=("Helvetica", 10), bg="grey", fg="white", activebackground='bisque',width=10, command=OpenExam).place(x=250, y=650)  
btnResult = Button(root, text="Results", font=("Helvetica", 10), bg="grey", fg="white",activebackground='bisque', width=10, command=OpenResult).place(x=350, y=650)
btnStudent= Button(root, text="Students", font=("Helvetica", 10), bg="grey", fg="white", activebackground='bisque',width=10, command=OpenStudent).place(x=450, y=650) 
btnStudy= Button(root, text="Studies", font=("Helvetica", 10), bg="grey", fg="white", activebackground='bisque',width=10, command= OpenStudy).place(x=550, y=650) 
btnEmployee= Button(root, text="Employees", font=("Helvetica", 10), bg="bisque", fg="black", activebackground='bisque',width=10).place(x=650, y=650)  
btnExit= Button(root, text="Exit", font=("Helvetica", 10), bg="grey", fg="white", activebackground='bisque',width=10, command=Exit).place(x=650, y=710)


root.title("Admin Student Management")
root.mainloop()
