from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.geometry("1255x944")
image = Image.open("hard.jpg")
photo = ImageTk.PhotoImage(image)
varun_label = Label(image=photo)
varun_label.pack()
root.mainloop()