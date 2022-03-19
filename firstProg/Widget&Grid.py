from tkinter import *
root=Tk()
root.geometry("655x333")
def getval():
    print(user.get())
    print(passw.get())
l1=Label(root,text="Username")
l2=Label(root,text="Password")
l1.grid()
l2.grid(row=1)
#Variable classes in tkinter
#BooleanVar,StringVar,IntVar,DoubleVar
user=StringVar()
passw=StringVar()
userentry=Entry(root,textvariable=user)
passentry=Entry(root,textvariable=passw)
userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)
Button(text="Submit",command=getval).grid()
root.mainloop()