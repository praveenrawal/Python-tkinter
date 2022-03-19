from tkinter import *
import tkinter.messagebox as msg

root = Tk()
root.geometry("666x333")
root.title("pyCharm")
def myfunc():
    print("hello brother")
    msg.showinfo("print","you want to print")
#mymenu =  Menu(root)
#mymenu.add_command(label="File",command=myfunc)
#mymenu.add_command(label="exit",command=quit)
#root.config(menu=mymenu)
filemenu  =  Menu(root)
m1  =  Menu(filemenu,tearoff=0)
m1.add_command(label="NewProject")
m1.add_command(label="save")
m1.add_command(label="print",command=myfunc)
m1.add_command(label="Exit",command=quit)
root.config(menu=filemenu)
filemenu.add_cascade(label="file",menu=m1)
root.mainloop()