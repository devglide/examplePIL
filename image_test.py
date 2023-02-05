from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.geometry('1100x700+1500+150')
root.title('guess!!!')


bg = Image.open("/Users/devon/maxresdefault.jpg")

test = ImageTk.PhotoImage(bg)

label1 = Label( root, image=test)
label1.image = test

label1.place(x=0, y=0)

root.mainloop()