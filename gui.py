# IMPORT MODULES
from tkinter import *
import cv2

# VERSION, VARIABLES
ver = 0.1

# FUNCTIONS
def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   
def about():
    filewin = Toplevel(root)
    button = Button(filewin, text=f"Készítette: Chen Kevin\nVerzió: {ver}")
    button.pack()
   
# CREATE WINDOW
root = Tk()
menubar = Menu(root)

# CREATE MENUPOINTS, MENU, FILE
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

# MENU, SEPARATOR
filemenu.add_separator()

# MENU, HELP
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

# CONFIG, MAINLOOP
root.config(menu=menubar)
root.mainloop()
