# LOGIN SCREEN #
from tkinter import *
import mysql.connector
import subprocess
import sys

# Connection to Database ---------------------
db_connection=mysql.connector.connect(
    host='localhost',  
    user='root',  
    password='root', #add your password for it to work
    database='school')
db_cursor=db_connection.cursor(buffered=True)

def signUp():
    # Interface --------------------------------
    root.title('DiemenAcademy SignUp')
    signblue = Label(root, text=" ", width=500, height=150, bg='cornflower blue').place(x=0,y=0)
    signbg = Label(root, text=" ", width=500, height=500).place(x=0,y=150)
    signlabel = Label(root, text='Sign Up', width=50).place(x=50, y=50)

    titlelbl = Label(root, text='Diemen Academy', bg='cornflower blue', fg='white', font=('Arial', '20', 'bold')).place(x=10, y=5)
    userlabel = Label(root, text='Email:', width=10).place(x=50, y=90)
    user = StringVar()
    userentry = Entry(root, textvariable=user,width=30).place(x=150, y=90)
    passwordlabel = Label(root, text='Password:', width=10).place(x=50, y=120)
    password = StringVar()
    passwordentry = Entry(root, textvariable=password, show='*',width=30).place(x=150, y=120)
    repasswordlabel = Label(root, text='Enter your password again:', width=30).place(x=130, y=155)
    repassword = StringVar()
    repasswordentry = Entry(root, textvariable=repassword, show='*',width=30).place(x=150, y=180)
    
    errortxt2 = StringVar()
    errortxt2.set('')
    errorlbl = Label(root, textvariable=errortxt2).place(x=130, y=210)
    
    signup2Button = Button(root, command=lambda: addUser(user, password, repassword, errortxt2), text='Sign Up', width=10, height=2, bg='grey', fg="white", activebackground='cornflower blue').place(x=50, y=190)
    exit2Button = Button(root, text='Exit', command=exitScript, width=10, height=2, bg='grey', fg="white", activebackground='cornflower blue').place(x=350, y=190)

def exitScript():
    root.destroy()
    subprocess.Popen([sys.executable, 'LoginScreen.py'])

def addUser(user, password, repassword, errortxt2):
    user=user.get()
    password=password.get()
    repassword=repassword.get()

    # Errors ---------------------------------------------------------------
    if password != repassword:
        errortxt2.set('The two passwords are not the same.')
    if user=='' or password=='':
        errortxt2.set('Please enter an email and password.')
    if not user.endswith('.diemenacademy.nl'):
        errortxt2.set('The email is not valid.')
    elif repassword=='':
        errortxt2.set('Please re-enter your password here.')
    # Determine what kind of user is logging in ---------------
    else:
        errortxt2.set('')
        if user.endswith('@administrator.diemenacademy.nl'):
            # check if the number exists in the DB ----------------
            # we weren't able to add admins to the database in time, so this feature doesn't work right now
            number = user[:-31]
            errortxt2.set('Your account has been registered.')

        elif user.endswith('@teacher.diemenacademy.nl'):
            y=0
            # check if the number exists in the DB ----------------
            number = user[:-25]
            db_cursor.execute('select teachernumber from teachers')
            result=db_cursor.fetchall()
            for x in result:
                x = str(x)
                x = x[1:-2]
                if number == x:
                    y = y+1          # if the teachernumber exists, y=1, else y=0
            if y==0: errortxt2.set('The email is incorrect.')
            errortxt2.set('Your account has been registered.')
            # add account info to the database
            db_cursor.execute("update teachers set workemail='{}' where teachernumber={};".format(user, number))
            db_connection.commit()
            db_cursor.execute("update teachers set Password='{}' where teachernumber={};".format(password, number))
            db_connection.commit()
            
        elif user.endswith('@student.diemenacademy.nl'):
            y=0
            # check if the number exists in the DB
            number = user[:-25]
            db_cursor.execute('select studentnumber from students')
            result=db_cursor.fetchall()
            for x in result:
                x = str(x)
                x = x[1:-2]
                if number == x:
                    y = y+1          # if the studentnumber exists, y=1, else y=0
            if y==0: errortxt2.set('The email is incorrect.')
            else: errortxt2.set('Your account has been registered.')
            # add account info to the database
            db_cursor.execute("update students set schoolemail='{}' where studentnumber={};".format(user, number))
            db_connection.commit()
            db_cursor.execute("update students set password='{}' where studentnumber={};".format(password, number))
            db_connection.commit()
    

def Login(user, password):
    user=user.get()
    password=password.get()
    if user=='' or password=='':
        errortxt.set('Please enter your username and password.')
    else: errortxt.set('')
    determineUser(user, password)


def determineUser(user, password): # determines which user, and opens the correct GUI
    exists=0
    line = user+ ' ' +password
    
    # Determines if the email exists in the database ---------
    if user.endswith('@teacher.diemenacademy.nl'):
        db_cursor.execute("select workemail from teachers")
    elif user.endswith('@student.diemenacademy.nl'):
        db_cursor.execute("select schoolemail from students")
    listofemails = db_cursor.fetchall()
    for email in listofemails:
        email = str(email)
        email = email[2:-3]
        if user == email: exists+=1
        
    # Determines if the password is correct based on the user ----------------------------------------
    if user.endswith('@teacher.diemenacademy.nl'):
        db_cursor.execute("select Password from teachers where workemail='{}';".format(user))
    elif user.endswith('@student.diemenacademy.nl'):
        db_cursor.execute("select password from students where schoolemail='{}';".format(user))
    userpassword = db_cursor.fetchall()
    userpassword = str(userpassword)
    userpassword = userpassword[3:-4]
    if password == userpassword: exists+=1

    # If not all values have been entered, give an error ---
    if line == ' ':
        errortxt.set('not all values have been entered.')
    # If the login is successful, open the correct UI ---------------------
    elif exists==2:
        errortxt.set('login successful.')
        if user.endswith('@student.diemenacademy.nl'):
            user = user[:-25]
            subprocess.Popen([sys.executable, 'Profile.py', user])
            root.destroy()
        elif user.endswith('@teacher.diemenacademy.nl'):
            number = user[:-25]
            root.destroy()
            subprocess.Popen([sys.executable, 'teacherProfile.py', user])
        elif user.endswith('@administrator.diemenacademy.nl'):
            root.destroy()
            subprocess.Popen([sys.executable, 'AdministratorProfile.py'])
    else:
        errortxt.set('the username and/or password is not correct.')


# Main -------------------------------------
root = Tk()
root.geometry('500x500')
root.title('DiemenAcademy Login')

lbl_blue = Label(root, text=" ", width=500, height=150, bg='cornflower blue').place(x=0,y=0)
lbl_bg = Label(root, text=" ", width=500, height=400).place(x=0,y=150)

titlelbl = Label(root, text='Diemen Academy', bg='cornflower blue', fg='white', font=('Arial', '20', 'bold')).place(x=10, y=5)
userlabel = Label(root, text='Username:', width=10).place(x=50, y=60)
user = StringVar()
userentry = Entry(root, textvariable=user, width=30).place(x=150, y=60)
passwordlabel = Label(root, text='Password:', width=10).place(x=50, y=90)
password = StringVar()
passwordentry = Entry(root, textvariable=password, show='*', width=30).place(x=150, y=90)
errortxt = StringVar()
errortxt.set('')
errorlbl = Label(root, textvariable=errortxt, bg='cornflower blue').place(x=150, y=125)

loginButton = Button(root, text='Login', command=lambda: Login(user, password), width=10, height=2, bg='grey', fg="white", activebackground='cornflower blue').place(x=50, y=130)
signupButton = Button(root, text='Sign Up', command=signUp, width=10, height=2, bg='grey', fg="white", activebackground='cornflower blue').place(x=50, y=180)
exitButton = Button(root, text='Exit', command=root.destroy, width=10, height=2, bg='grey', fg="white", activebackground='cornflower blue').place(x=350, y=180)

root.mainloop()
