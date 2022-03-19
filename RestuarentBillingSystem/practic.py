# import  sqlite3

# conect with db

#conn = sqlite3.connect('test.db')


#conn = sqlite3.connect('login.db')
# command = "SELECT * FROM LogInfo"
# pas = conn.execute(command)
#
# for i in pas:
#     print(i)
# n="anuj"
# p="rawal"
# #command = "INSERT INTO LogInfo VALUES(?,?)",
# conn.execute("INSERT INTO LogInfo VALUES(?,?)",(n,p))
# conn.commit()

# a=conn.execute(f"SELECT * FROM LogInfo")
# for i in a:
#      print(i)

# a="anuj"
# file = open(f'{a}.txt','a')
# import random
# import datetime
# import time
# a=random.randint(1,1000)
# print(a)
# b=datetime.date.today().strftime('%d/%m/%y')
# c=datetime.datetime.now().strftime('%H:%M:%S')
# print(b)
# print(c)
from tkinter import *
import sqlite3
root = Tk()
root.geometry("533x633")
frame = Frame(root,bg="yellow",borderwidth=0)
updateValueLabel= Label(frame,text="Update values", font=5, bg="yellow", fg="blue")
#--------------------------dbms----------------------------------------------------
con = sqlite3.connect('test.db')
command = '''CREATE TABLE IF NOT EXISTS product(productName varchar(20) NOT NULL PRIMARY KEY,productPrice real not null)'''
con.execute(command)
#--------------------------Functions-----------------------------------------------
def addProduct():
    proname = usernamef1.get()
    proprice = passwordf2.get()
    if proname and proprice.isnumeric():

        con.execute("INSERT INTO product VALUES(?,?)",(proname,proprice))
        con.commit()

        a=con.execute("SELECT * FROM product")
        for i in a:
            print(i)

        addProductmsgLabel.config(text="successfully submited")
    else:
        addProductmsgLabel.config(text="Please fill correct values")

def updateRecord():
    pron_name = productNameEntry.get()
    updateprice = productPriceEntry.get()
    if pron_name and updateprice.isnumeric():

        con.execute("UPDATE product set productPrice=?  where productName=?",(pron_name,updateprice))
        con.commit()
        a=con.execute("SELECT * FROM product")
        for i in a:
            print(i)

        updateProductmsgLabel.config(text="successfully submited")
    else:
        updateProductmsgLabel.config(text="Please fill correct values")
#Add product --------------------------------------------------------------------
proLabel = Label(frame,text="Add New Product",font=0, bg="yellow", fg="green")
addProductFrame = Frame(frame,borderwidth=5, bg="orange")
addProductmsgLabel = Label(frame,text="fill into the blanks",font=0, bg="yellow", fg="red")
usernamel1 = Label(addProductFrame, text="ProductName ", font=2)
passwordl2 = Label(addProductFrame, text="ProductPrice  ", font=2)
UsernameRegister = StringVar()
PasswordRegister = StringVar()
usernamef1 = Entry(addProductFrame, textvariable=UsernameRegister, font=2, borderwidth=2)
passwordf2 = Entry(addProductFrame, textvariable=PasswordRegister,  font=2, borderwidth=2)
regitrationbtn = Button(addProductFrame, text="Submit", pady=10, font=2, command  = addProduct)
#Add product component ------------------------------------------------------------------------
frame.place(x=0,y=0,width=533, height=633)
updateValueLabel.pack()
proLabel.pack()
addProductmsgLabel.pack()
addProductFrame.pack()
usernamel1.grid(row=0,column=0,pady=10)
passwordl2.grid(row=1,column=0,pady=10)
usernamef1.grid(row=0,column=1,pady=10)
passwordf2.grid(row=1,column=1,pady=10)
regitrationbtn.grid(row=2,column=1)
#update record-------------------------------------------
updateLabel = Label(frame,text="Update Product Price",font=0, bg="yellow", fg="green")
updateProductFrame = Frame(frame,borderwidth=5, bg="orange")
updateProductmsgLabel = Label(frame,text="fill into the blanks",font=0, bg="yellow", fg="red")
productNameLabel = Label(updateProductFrame, text="ProductName ", font=2)
productPriceLabel = Label(updateProductFrame, text="ProductPrice  ", font=2)
UsernameRegister = StringVar()
PasswordRegister = StringVar()
productNameEntry = Entry(updateProductFrame, textvariable=UsernameRegister, font=2, borderwidth=2)
productPriceEntry = Entry(updateProductFrame, textvariable=PasswordRegister,  font=2, borderwidth=2)
updatebtn = Button(updateProductFrame, text="Update", pady=10, font=2,command=updateRecord)
#update record component bind----------------------------------------------------------------------------
updateLabel.pack()
updateProductmsgLabel.pack()
updateProductFrame.pack()
productNameLabel.grid(row=0,column=0,pady=10)
productPriceLabel.grid(row=1,column=0,pady=10)
productNameEntry.grid(row=0,column=1,pady=10)
productPriceEntry.grid(row=1,column=1,pady=10)
updatebtn.grid(row=2,column=1)
#Delete record component------------------------------------------------------------------------------------
deleteLabel = Label(frame,text="Delete record",font=0, bg="yellow", fg="green")
deleteProductFrame = Frame(frame,borderwidth=5, bg="orange")
deleteProductmsgLabel = Label(frame,text="fill into the blanks",font=0, bg="yellow", fg="red")
deleteproductNameLabel = Label(deleteProductFrame, text="ProductName ", font=2)

UsernameRegister = StringVar()
PasswordRegister = StringVar()
deleteproductNameEntry = Entry(deleteProductFrame, textvariable=UsernameRegister, font=2, borderwidth=2)

deleteupdatebtn = Button(deleteProductFrame, text="Delete", pady=10, font=2)
#Delete component bind-------------------------------------------------------------------------------------------
deleteLabel.pack()
deleteProductmsgLabel.pack()
deleteProductFrame.pack()
deleteproductNameLabel.grid(row=0,column=0,pady=10)

deleteproductNameEntry.grid(row=0,column=1,pady=10)

deleteupdatebtn.grid(row=1,column=1)
root.mainloop();