from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Hacker photos")

my_img = ImageTk.PhotoImage(Image.open("1.jpg"))
my_img1 = ImageTk.PhotoImage(Image.open("2.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("3.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("4.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("5.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("ico.jpg"))
my_img6 = ImageTk.PhotoImage(Image.open("6.jpg"))

image_list = [my_img, my_img1, my_img2, my_img3, my_img4, my_img5, my_img6]

frame = LabelFrame(root, text="Hacker photos", padx=5, pady=5)
frame.grid(row=0, column=0, columnspan=3, pady=10, padx=10)

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(frame, image=my_img)
my_label.grid(row=1, column=0, columnspan=3)

def next(num):
    global my_label
    global button_Next
    global button_Back

    my_label.grid_forget()
    my_label = Label(frame, image=image_list[num - 1])
    button_Next = Button(root, text=">>", padx=23, command=lambda: next(num + 1))
    button_Back = Button(root, text="<<", padx=23, command=lambda: back(num-1))

    if num == len(image_list):
        button_Next = Button(root, text=">>", state=DISABLED)


    my_label.grid(row=1, column=0, columnspan=3)
    button_Back.grid(row=2, column=0)
    button_Next.grid(row=2, column=2)

    status = Label(root, text="Image " + str(num) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=3, column=0, columnspan=3, sticky=W+E)


def back(num):
    global my_label
    global button_Next
    global button_Back

    my_label.grid_forget()
    my_label = Label(frame, image=image_list[num-1])
    button_Next = Button(root, text=">>", padx=23, command=lambda: next(num + 1))
    button_Back = Button(root, text="<<", padx=23, command=lambda: back(num - 1))

    if num == 1:
        button_Back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=1, column=0, columnspan=3)
    button_Back.grid(row=2, column=0)
    button_Next.grid(row=2, column=2)

    status = Label(root, text="Image " + str(num) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=3, column=0, columnspan=3, sticky=W + E)


button_Exit = Button(root, text="EXIT", padx=20, command=root.quit)
button_Back = Button(root, text="<<", padx=23, command=back, state=DISABLED)
button_Next = Button(root, text=">>", padx=23, command=lambda: next(2))

button_Back.grid(row=2, column=0)
button_Exit.grid(row=2, column=1, pady=10)
button_Next.grid(row=2, column=2)
status.grid(row=3, column=0, columnspan=3, sticky=W+E)


root.mainloop()
