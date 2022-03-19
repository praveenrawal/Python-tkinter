from tkinter import *
import tkinter.messagebox as msg
import os
import practic
import random
import datetime
import sqlite3
class main_Page(Tk):
    def __init__(self):
        self.frame1=Frame(bg="white")
        self.frame1.place(x=0, y=0, width=1280, height=720)
        #billing system
        self.frame2=Frame(self.frame1,bg="yellow", relief=GROOVE, border=2)
        self.frame2.place(x=0,y=0,width=1280,height=40)
        self.l=Label(self.frame2,text="MARUTI SANDWICH CHORNER",bg="yellow")
        self.l.pack(pady=6)
        #left frame
        self.frame3=Frame(self.frame1,bg="yellow", relief=GROOVE, border=2)
        self.frame3.place(x=0, y=80, width=630, height=670)
        #right frame
        self.frame4 = Frame(self.frame1, bg="yellow", relief=GROOVE, border=2)
        self.frame4.place(x=640, y=80, width=640, height=670)
        #left frmae3 element

        self.label1 = Label(self.frame3, text="Customer_Name ", font=3)
        self.name= StringVar()
        self.entry1 = Entry(self.frame3, textvariable=self.name, font=3, border=2)
        self.entry1.focus()
        self.label1.grid(row=0,column=0, pady=40)
        self.entry1.grid(row=0, column=1,pady=40)
            #---------------------------------------------------------------------
        self.label2 = Label(self.frame3, text="mobile_Number  ", font=3)
        self.number = IntVar()
        self.entry2 = Entry(self.frame3, textvariable=self.number, font=3,border=2)
        self.label2.grid(row=0,column=2,pady=40 )
        self.entry2.grid(row=0, column=3, pady=40)
           #--------------------------------------------------------------------
        self.label3 = Label(self.frame3, text="product_-_Name ", font=3)
        self.product = StringVar()
        self.entry3 = Entry(self.frame3, textvariable=self.product, font=3,border=2)
        self.label4 = Label(self.frame3, text="product_Quantity ", font=3)
        self.Qty = IntVar()
        self.entry4 = Entry(self.frame3, textvariable=self.Qty, font=3,border=2)
        self.label3.grid(row=1,column=0)
        self.entry3.grid(row=1,column=1)
        self.label4.grid(row=1,column=2)
        self.entry4.grid(row=1,column=3)
            #-----------------------------------------------------------------------
        self.btn1 = Button(self.frame3,text="add_Item", font=3, command=self.add_Item)
        self.btn3 = Button(self.frame3, text="Refresh", font=3,command=self.referesh)
        self.btn4 = Button(self.frame3, text="print_Bill", font=3, command = self.printFile)
        self.btn2 = Button(self.frame3, text="Update_Price_Item", font=3, command=self.msgBox)
        self.btn1.grid(row=2,column=0,pady=40)
        self.btn3.grid(row=2,column=1,pady=40)
        self.btn4.grid(row=2,column=2,pady=40)
        self.btn2.grid(row=3,column=1,pady=40)



        # frame4 element
        self.yscroll_y= Scrollbar(self.frame4, orient=VERTICAL)
        self.textarea= Text(self.frame4, yscrollcommand= self.yscroll_y)
        self.yscroll_y.pack(side=RIGHT,fill=Y)
        self.yscroll_y.config(command=self.textarea.yview)
        self.textarea.place(width=620,height=630)
        #-----------------------------------

        #-----------------------------------
        self.even = 0
        self.sum=0

    def referesh(self):
        self.textarea.delete("1.0","end")
        self.even = 0

    def add_Item(self):
        c_Name=self.name.get()
        c_Num=self.number.get()
        item=self.product.get()
        qty=self.Qty.get()
        price=0
        date = datetime.date.today().strftime('%d/%m/%y')
        time = datetime.datetime.now().strftime('%H:%M:%S')
        if self.even == 0:
            self.textarea.insert(END, "==========================================================================")
            self.textarea.insert(END, f"\n{time}\t\tMARUTI\t\t{date}")
            self.textarea.insert(END,f"\n\nCustomer_name:{c_Name} \t\t contact_No.:{c_Num}")
            self.textarea.insert(END, "\n==========================================================================")
            self.textarea.insert(END,"\n\nProduct \t\t QTY \t\t Price \t\t Total")
            self.even = 1
        if item == "panipuri" :
            price=30
        if item == "bhel" :
            price=40
        if item == "PPF":
            price=30
        if item == "PPS" :
            price=50
        if item == "vegs" :
            price=40
        self.textarea.insert(END,f"\n{item} \t\t {qty} \t\t {price} \t\t {price*qty} ")
        #self.textarea.insert("end","Total")
        self.sum+=price*qty

    def msgBox(self):
        a=msg.askquestion("MARUTI","You Want To Update")
        if a == "yes":
            root = Tk()
            root.geometry("533x433")
            frame = Frame(root,bg="yellow")
            frame.pack()
            root.mainloop();



    def printFile(self):
        text = self.textarea.get("1.0","end")
        filename = self.name.get() + f'{self.number.get()}'
        file = open(f'{filename}.txt',"a")
        for i in text:
            file.write(i)
        file.write(f"\n \t\t  \t\t  \t\t {self.sum}")

        os.startfile(f'{filename}.txt','print')





