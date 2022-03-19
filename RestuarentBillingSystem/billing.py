from tkinter import *

class main_Page(Tk):
    def __init__(self):
        self.i=0
        self.f2=Frame(bg="yellow")
        self.f2.place(x=0,y=0,width=1000,height=500)
        self.l=Label(self.f2,text="Har Har Mhadev",font=3)
        self.l2=Label(self.f2,text="Dish Name",font=3)
        self.l3 = Label(self.f2, text="Quantity", font=3)
        self.var=StringVar()
        self.varint=IntVar()
        self.E=Entry(self.f2, textvariable=self.var, font=3)
        self.E2=Entry(self.f2, textvariable=self.varint, font=3)
        self.list=Listbox(self.f2)

        self.item = ["PPF","PPS","MURK","MUKS","SKH"]
        self.update(self.item)
        self.list.bind("<<ListboxSelect>>", self.Fillout)
        self.E.bind("<KeyRelease>", self.check)
        #label for customer detail
        self.name = Label(self.f2, text="Customer Name ", font=3)
        self.mobile= Label(self.f2, text= "Mobile No.", font=3)
        self.nameVar=StringVar()
        self.mobileVar = IntVar()
        self.nameEntry= Entry(self.f2, textvariable=self.nameVar, font=3)
        self.mobileEntry= Entry(self.f2, textvariable= self.mobileVar, font=3)
        #pack()
        self.name.place(x=0,y=100)
        self.nameEntry.place(x=0,y=150)
        self.mobile.place(x=200,y=100)
        self.mobileEntry.place(x=200,y=150)
        #Button for add item and delete item
        self.addItem= Button(self.f2, text="AddItem", command=self.printBill)
        self.l.pack()
        self.l2.place(x=0,y=200)
        self.E.place(x=0,y=250)
        self.l3.place(x=200,y=200)
        self.E2.place(x=200,y=250)
        self.addItem.place(x=200, y=300)
        self.BillDisplay.place(x=500, y=30, width=500, height=470)
        #bill Area
        self.Txt= Text(self.f2, border=2, relief=GROOVE, bg="white")
        self.Txt.place(x=500,y=40)


    def update(self,data):
        self.list.delete(0,END)
        for item in data:
            self.list.insert(END, item)
    def Fillout(self,event):
        #delete whatever in the entry box
        self.E.delete(0,END)
        #add clicked item in the entry box
        self.E.insert(0, self.list.get(ANCHOR))
    def check(self,event):

        typed=self.E.get()
        if typed == '':
            data=self.item
        else:
            self.list.place(x=0,y=270)
            data=[]
            for i in self.item:
                if typed.lower() in i.lower():
                    data.append(i)
        self.update(data)

    def printBill(self):
        pass





