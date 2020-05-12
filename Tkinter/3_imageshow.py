from tkinter import *
from PIL import Image,ImageTK

sk_root = Tk()

sk_root.geometry("600x600")
#photo = PhotoImage(file="name.png")

# for JPG iamge

image = Image.open("splash.jpg")
photo = ImageTK.PhotoImage(image)

sk_label = Label(image=photo)
sk_label.pack()

sk_root.mainloop()