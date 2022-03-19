from tkinter import *
root=Tk()
root.geometry("655x333")
def hello():
    print("hello tkinter")
root.title("Button")
f1=Frame(root,bg="grey",borderwidth=6)
f1.pack()
b1=Button(f1,text="print",fg="red",command=hello)
b1.pack(side=LEFT)
b2=Button(f1,text="print",fg="red",)
b2.pack(side=LEFT)
b3=Button(f1,text="print",fg="red",)
b3.pack(side=LEFT)
b4=Button(f1,text="print",fg="red",)
b4.pack()

root.mainloop()