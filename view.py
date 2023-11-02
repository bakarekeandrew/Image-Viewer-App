from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("ImageViewer App")
# root.iconbitmap('C:\Users\andre\Documents\personal development\python\Tkinter')

my_img1 = ImageTk.PhotoImage(Image.open("images/image1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/image2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/image3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/image4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/image5.jpg"))
my_img6 = ImageTk.PhotoImage(Image.open("images/image6.jpg"))
my_img7 = ImageTk.PhotoImage(Image.open("images/image7.jpg"))

my_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7]



my_label =  Label(image= my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def back(img_number):
    global my_label
    global button_next
    global button_back
    
    my_label.grid_forget()
    my_label = Label(image=my_list[img_number-1])
    button_next = Button(root, text=">>", command=lambda: forward(img_number + 1))
    button_back = Button(root, text="<<", command=lambda: forward(img_number - 1))

    if img_number == 1:
      button_next = Button(root, text="<<", state=DISABLED)

def forward(img_number):
    global my_label
    global button_next
    global button_back

    my_label.grid_forget()
    my_label = Label(image=my_list[img_number-1])
    button_next = Button(root, text=">>", command=lambda: forward(img_number + 1))
    button_back = Button(root, text="<<", command=lambda: forward(img_number - 1))
    
    if img_number == len(my_list):
      button_next = Button(root, text=">>", state=DISABLED)


    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_next.grid(row=1, column=2)
    


button_back = Button(root, text="<<", command=back, state= DISABLED)
button_quit = Button(text="Exit Program" , command=root.quit)
button_next = Button(root, text=">>", command=lambda: forward(1))

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_next.grid(row=1, column=2)
              







root.mainloop()
