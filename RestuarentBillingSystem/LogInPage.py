from tkinter import *
import winsound
import mainPage
import sqlite3
class Log_in_page(Tk):
    def __init__(self):
        super().__init__()
        self.odd=1
        self.geometry("1280x650")
        self.title("Maruthi")
        self.fr = Frame(self,borderwidth=0, bg="yellow" )
        self.l= Label(self.fr,text="Restaurant Billing System", font=5, bg="yellow", fg="blue")
        self.l.pack(pady=20)
        #login frame
        self.fr2 = Frame(self.fr,borderwidth=5,bg="orange")
        self.l1 = Label(self.fr2,text="Username ",font=5)
        self.l2 = Label(self.fr2,text="Password ", font=5)
        self.l1.grid(row=1, column=1, pady=10 )
        self.l2.grid(row=2, column=1, pady=10)
        self.Username=StringVar()
        self.Password=StringVar()
        self.f1 = Entry(self.fr2,textvariable=self.Username,font=5, borderwidth=2 )
        self.f2 = Entry(self.fr2,textvariable=self.Password,show="*",font=5, borderwidth=2  )
        self.f1.focus();
        self.f1.grid(row=1, column=2 )
        self.f2.grid(row=2, column=2 )
        self.fr.place(x=0,y=0,width=1280, height=650)
        self.loginmsg=StringVar()
        self.loginmsg.set("fill login information")
        self.msglabel = Label(self.fr,textvariable=self.loginmsg,font=5,fg='red')
        self.msglabel.pack(pady=10)
        self.LogIn = Button(self.fr2, text="LogIn", pady=10, font=5, command=self.validate)
        self.LogIn.grid(row=3, column=2, sticky=SE)
        self.LogIn.bind("<Return>", self.valid)
        self.fr2.pack()
        self.registrationmsg = StringVar()
        self.registrationmsg.set("for registeration")
        self.msglabelRegister = Label(self.fr,textvariable=self.registrationmsg,font=5,fg="red")
        self.msglabelRegister.pack(pady=40)
        #self.LogIn.focus()
        #registered frame
        self.registerFrame = Frame(self.fr, borderwidth=5, bg="orange")
        self.usernamel1 = Label(self.registerFrame, text="Username ", font=5)
        self.passwordl2 = Label(self.registerFrame, text="Password ", font=5)
        self.confirmasswordl2 = Label(self.registerFrame, text="Confirm     ", font=5)
        self.usernamel1.grid(row=1, column=1, pady=10)
        self.passwordl2.grid(row=2, column=1, pady=10)
        self.confirmasswordl2.grid(row=3,column=1,pady=10)
        self.UsernameRegister = StringVar()
        self.PasswordRegister = StringVar()
        self.confirmRegister = StringVar()
        self.usernamef1 = Entry(self.registerFrame, textvariable=self.UsernameRegister, font=5, borderwidth=2)
        self.passwordf2 = Entry(self.registerFrame, textvariable=self.PasswordRegister, show="*", font=5, borderwidth=2)
        self.confirmPassword = Entry(self.registerFrame, textvariable=self.confirmRegister, show="*", font=5, borderwidth=2)
        #self.usernamef1.focus();
        self.usernamef1.grid(row=1, column=2)
        self.passwordf2.grid(row=2, column=2)
        self.confirmPassword.grid(row=3,column=2)
        self.registerFrame.pack()
        self.regitrationbtn = Button(self.registerFrame, text="Registration", pady=10, font=5,command = self.registration)
        self.regitrationbtn.grid(row=4, column=2, sticky=SE)
        #self.LogIn.bind("<Return>", self.valid)



    def validate(self):
        # database file
        con = sqlite3.connect('login.db')
        # command = '''CREATE TABLE LogInfo(username CHAR(20) PRIMARY KEY NOT NULL,password CHAR(20) NOT NULL )'''
        a=self.Username.get()
        b=self.Password.get()
        command = "SELECT * FROM LogInfo"
        confirm = con.execute(command)
        flag=0
        for i in confirm:
            if i[0]==a and i[1]==b:
                mainPage.main_Page()
                flag = 1
                break

        if flag==0:
            winsound.Beep(700,50)
            self.loginmsg.set("wrong id and pass")
        else:
            self.loginmsg.set("successful")
        con.close();

    def valid(self,e):
        self.validate()

    def registration(self):
        conn = sqlite3.connect('login.db')
        user=self.UsernameRegister.get()
        pas = self.PasswordRegister.get()
        confirm=self.confirmRegister.get()
        if pas != confirm:
            self.registrationmsg.set("confirm password not match")
        else:
            conn.execute("INSERT INTO LogInfo VALUES(?,?)",(user,pas))
            self.registrationmsg.set("registration succesful")
        conn.commit()
        conn.close()



















