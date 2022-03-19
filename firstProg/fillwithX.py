from tkinter import *
def rootx():
    root=Tk()
    root.geometry("500x400")
    root.title("GUI")
    lab=Label(text="Ready",bg="yellow",fg="green")
    lab.pack(side=BOTTOM,anchor="se",fill=X)
    lab.pack()
    root.mainloop()
rootx()