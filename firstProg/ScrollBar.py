from tkinter import *
root = Tk()
root.geometry("666x343")
root.title("ScrollBar")
#for connecting scrollbar to a widget
#1.yscrollcommand=scrollbar.set
#2.scrollbar.config(command=widget.yview)
scrollbar = Scrollbar(root)
scrollbar.pack(fill=Y,side=RIGHT)
#lbx=Listbox(root,yscrollcommand=scrollbar.set)
#for i in range(344):
#    lbx.insert(END,f"{i}")
#lbx.pack(fill=BOTH)
text=Text(root,yscrollcommand=scrollbar.set)
text.pack()
scrollbar.config(command=text.yview)
root.mainloop()