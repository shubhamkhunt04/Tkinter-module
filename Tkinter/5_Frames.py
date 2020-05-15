from tkinter import *

sk_root = Tk()
sk_root.geometry("500x300")
f1 = Frame(sk_root , bg="green",borderwidth = 6)
f1.pack(side = LEFT,fill = "y")

l = Label(f1,text="hello shubham")
l.pack()
sk_root.mainloop()