from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title('images and butts')
#root.iconbitmap('c:/...ico')   #icon location in Windows



my_img = ImageTk.PhotoImage(Image.open("/Users/devon1/Desktop/picts/IMG_0107.JPG"))
my_img1 = ImageTk.PhotoImage(Image.open("/Users/devon1/Desktop/picts/IMG_1187.JPG"))
my_img2 = ImageTk.PhotoImage(Image.open("/Users/devon1/Desktop/picts/IMG_1080.JPG"))
my_img3 = ImageTk.PhotoImage(Image.open("/Users/devon1/Desktop/picts/IMG_1187.JPG"))
my_img4 = ImageTk.PhotoImage(Image.open("/Users/devon1/Desktop/picts/IMG_0107.JPG"))

image_list = [my_img, my_img1, my_img2, my_img3, my_img4]


my_label = Label(image=my_img)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))
    
    if image_number ==5:
        button_forward = Button(root, text=">>", state=DISABLED)

    
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number ==0:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


button_back = Button(root, text="<<", padx=40, pady=20, command=back, state=DISABLED)
button_forward = Button(root, text=">>", padx=40, pady=20, command=lambda: forward(2))
button_quit = Button(root, text="Exit App", padx=40, pady=20, command=root.quit)

button_quit.grid(row=1, column=1)
button_back.grid(row=1, column=0)
button_forward.grid(row=1, column=2)

root.mainloop()