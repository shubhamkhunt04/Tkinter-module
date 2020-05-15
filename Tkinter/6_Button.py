from tkinter import  *

sk_root = Tk()

sk_root.geometry("655x333")

def printfun():
    print("Hello shubham bro")

frame = Frame(sk_root,borderwidth=6,bg="green",relie = SUNKEN)
frame.pack(side = LEFT ,anchor = "nw")

b1 = Button(frame,fg="red",text = "click shubhalaaa1",command=printfun)
b1.pack(side=LEFT)

b2 = Button(frame,fg="red",text = "click shubhalaaa2")
b2.pack(side=LEFT)

b3 = Button(frame,fg="red",text = "click shubhalaaa3")
b3.pack(side=LEFT)

sk_root.mainloop()