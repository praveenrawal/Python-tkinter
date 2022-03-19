from tkinter import *
root = Tk()
root.geometry("322x544")
root.title("Calculator")
scvalue = StringVar()
screen = Entry(root,textvar = scvalue , font="lucida 40 bold").pack()
root.mainloop()