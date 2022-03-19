from tkinter import *
i=0
def  add():
    global  i
    lbx.insert(ACTIVE,f"{i}")
    i+=1
root = Tk()
root.geometry("666x343")
root.title("ListBox")
lbx=Listbox(root)
lbx.pack()
lbx.insert(END,"First item of list box")
Button(root,text="Add_Item",command=add).pack()
root.mainloop()
