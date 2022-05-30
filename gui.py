# IMPORT MODULES
import cv2
from tkinter import *
from tkinter.filedialog import askopenfilename

# VERSION, VARIABLES
ver = 0.3

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

def importImage():
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # Read the input image
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    img = cv2.imread(askopenfilename())
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Display the output
    root.quit
    cv2.imshow('img', ResizeWithAspectRatio(img, height=1000))
    cv2.waitKey(0)

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
filemenu.add_command(label="Open", command=importImage)

# MENU, HELP
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About...", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

# FRAME ELEMENTS
frame = Label(
    root,
    text="Arc felismerő",
    font=(48)
    ).grid(
        row=0,
        column=0,
        pady=(100,10),
        padx=(140,100)
        )
Button(
    frame,
    text='Importálás',
    command=importImage
    ).grid(row=1,column=0)

# CONFIG, MAINLOOP
root.title('Program')
root.geometry('400x300')
root.resizable(False, False)
root.config(menu=menubar)
root.mainloop()
