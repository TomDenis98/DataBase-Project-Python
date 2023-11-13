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
                    password="atjfjlca", # Enter your password
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
TitleLabel = Label(root, text="Student Management", font=("Helvetica", 23), bg='bisque', fg="black", width=20).place(x=240, y=20)

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

studylabel =Label(root, text="Study: ", font=("Helvetica", 10), bg="dark grey", fg="white", width=20).place(x=50, y=450)
study=StringVar()
studyentry=Entry(root, textvariable=study, width=30, bg='white').place(x=250, y=450)

startlabel =Label(root, text="Year of enrollment: ", font=("Helvetica", 10), bg="dark grey", fg="white", width=20).place(x=50, y=480)
start=StringVar()
startentry=Entry(root, textvariable=start, width=30, bg='white').place(x=250, y=480)

counselorlabel =Label(root, text="Study Counselor ", font=("Helvetica", 10), bg="dark grey", fg="white", width=20).place(x=50, y=510)
counselor=StringVar()
counselorentry=Entry(root, textvariable=counselor, width=30, bg='white').place(x=250, y=510)


def Register(): 
    global fname, lname, birth, nationality, gender, street, no, post, city, phone,  email, study, start, counselor
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
    email=email.get()
    study=study.get()
    start=start.get()
    query=(" INSERT into students values ('4', '{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}', 'Y', '{}', '{}', 'test', 'password')"
    .format(fname, lname, birth, nationality, gender, street, no, post, city, phone,  email, study, start, counselor))
    print(query)
    db_cursor.execute(query)
    db_connection.commit()

    
    # Studentnumber generator --------------------------------------------------- 
    number1 = []
    number2 = []
    number3 = []
    number4 = 00

    # Select attributes for primary key -------------------------------------------
    db_cursor.execute("select startyear from students where lastname='{}'".format(lname))
    startyear= db_cursor.fetchall()
    db_cursor.execute("select study from students where lastname='{}'".format(lname))
    study= db_cursor.fetchall()
    db_cursor.execute("select dateofbirth from students where lastname='{}'".format(lname))
    birthyear= db_cursor.fetchall()

    # First Number -------------------------------------------
    yr = start
    nr=int(yr)-2000
    number1.append(nr)

    # Second Number ---------------------------------------
    nr2=1
    x = str(study[0][0])
    if x == 'BIMparttime':
        nr2=3
    elif x == 'MathematicalEngineering':
        nr2=4
    elif x == 'PrecisionEngineering':
        nr2=5
    elif x == 'Planedesign':
        nr2=6
    elif x == 'BusinessICT':
        nr2=7
    elif x == 'Architecture':
        nr2=8     
    else:
        nr2=1
    number2.append(int(nr2))

    # Third Number ---------------------------------------
    birth=str(birth)
    birth=int((birth[2:4])+(birth[8:10]))
    birth/=5
    number3=int(birth)

    # Putting the numbers together ----------------------
    studentnr=str(number1[0])+ str(number2[0]) + str(number3)+ str(number4)+ '0000000' #the 0's fill up numbers that are too short
    studentnr=(studentnr[0:7]) #here all numbers get trimmed to equal length

    db_cursor.execute("Update students set studentnumber={} where lastname='{}';".format(studentnr, lname))
    db_connection.commit()  
    print(studentnr, 'done')


def Delete(): #should only get fname, lname, birth
    global fname, lname, birth
    fname=fname.get()
    lname=lname.get()
    birth=birth.get()
    query=(" delete from students where firstname='{}' and lastname='{}' and dateofbirth='{}'".format(fname, lname, birth))
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
btnResult = Button(root, text="Results", font=("Helvetica", 10), bg="grey", fg="white",activebackground='bisque', width=10, command=OpenResult).place(x=350, y=650)
btnStudent= Button(root, text="Students", font=("Helvetica", 10), bg="bisque", fg="black", activebackground='bisque',width=10).place(x=450, y=650)
btnStudy= Button(root, text="Studies", font=("Helvetica", 10), bg="grey", fg="white", activebackground='bisque',width=10, command= OpenStudy).place(x=550, y=650) 
btnEmployee= Button(root, text="Employees", font=("Helvetica", 10), bg="grey", fg="white", activebackground='bisque',width=10, command=OpenEmployees).place(x=650, y=650)  
btnExit= Button(root, text="Exit", font=("Helvetica", 10), bg="grey", fg="white", activebackground='bisque',width=10, command=Exit).place(x=650, y=710)

root.title("Admin Student Management")
root.mainloop()
