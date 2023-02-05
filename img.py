import random
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry('800x800+1000+150')


# frame1 = Frame(root, height=500, width=500, bg='red')
# frame1.place(x=0, y=0)
my_pic = Image.open("/Users/devon/Desktop/21.png")
resized = my_pic.resize((50, 50), Image.ANTIALIAS)

resized_img = ImageTk.PhotoImage(resized)

# label = Label(root, bg='red', text="blah blah")
# label.pack()
# label.place(height=500, width=500, x=25, y=25)



label1 = Label(root, bg='green', borderwidth=3, height=150, width=150, relief="raised", image=resized_img)
label1.pack()
label1.place(anchor = E, height=150, width=150, x=700, y=75)


# butt = Button(root, text='click me')
# butt.pack()
# butt.place(x=400, y=400)

# label2 = Label(root, bg='yellow', borderwidth=10, relief="raised", padx=50, text="blah blah", anchor=E)
# label2.pack()
# label2.place(height=200, width=800, anchor = W, x=0, y=700)

root.mainloop()


