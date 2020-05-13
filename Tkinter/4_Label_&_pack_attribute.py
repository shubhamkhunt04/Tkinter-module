from tkinter import *

sk_root = Tk()

sk_root.geometry("480x530")
sk_root.title("Shubham GUI")

# Important Label Options
#
# text = adds the text
# bd = background
# fg = foreground
# font = sets the font
# padx = x padding
# pady = y padding
# relief = border styling = SUNKEN , RAISED, GROOVE ,RIDGE

title_label = Label(text="hello shubham khunt",bg="red",fg = "green",padx=113,font="comicsansns 18 bold",borderwidth = 5 , relief=SUNKEN)

# important pack attribute
# anchor = nw
# side = top,bottom,left,right
# fill
# padx
# pady

title_label.pack(anchor = "se",side = BOTTOM,fill=X)

sk_root.mainloop()