from CImageInstagram import *
from Filters.CFilterBrigthness import *
from Filters.CFilterBlur import *
from Filters.CFilterGrayscale import *
from Filters.CFilterVignette import *
from Filters.CFilterTest import *
from Filters.CFilterColor import *
from Filters.CFilterPrime import *
from Filters.CFilterPlainBorder import *
from Lib import *
import threading
import os
import random
from Tkinter import Tk, Label
import ImageTk
import sys
    

filters = [
           CFilterVignette(),
           CFilterGrayscale(),
           CFilterColor((1,0,0)),
           CFilterPrime(),
           CFilterPlainBorder(),
           CFilterBlur(),
           ]

# Add new filtered images
pics = os.listdir("../pic")

"""
for image in range(len(pics)):
    c = CImageInstagram("../pic/" + pics[image])
    c.applyFilter(random.sample(filters, 1))
    c.save("../slideshow/" + pics[image])
"""

global current, running
current = -1
running = True

class applyFilterLoop(threading.Thread):
    def run(self):
        p = 0
        while running:
            global current
            current = p
            c = CImageInstagram("../pic/" + pics[p])
            c.applyFilter(random.sample(filters, 1))
            c.save("../slideshow/" + pics[p])
            p = (p+1)%len(pics)

filterLoop = applyFilterLoop()
filterLoop.start()


"""
Slideshow Window
"""

slides = os.listdir("../slideshow")
global n,size
n = 0
size = 1280,800

root = Tk()
root.geometry(str(size[0])+"x"+str(size[1]))
panel = Label(root)
panel.pack(side = "bottom", fill = "both", expand = "yes")

# for debug
def callbackRight(e):
    changePic("next")

#for debug
def callbackLeft(e):
    changePic("prev")

def autoChange():
    changePic("next")
    root.after(5000, autoChange)

# change the id of the img to show
def updatePos(direction):
    print direction
    global n
    if direction ==  "next":
        n = (n+1)%len(pics)
    elif direction == "prev":
        n = (n-1)%len(pics)
    else:
        raise Exception("Got invalid direction")
    if n == current:
        updatePos(direction)

def changePic(direction):
    global n
    updatePos(direction)
    img = Image.open("../slideshow/"+slides[n])
    img = resize(img)
    photo = ImageTk.PhotoImage(img)
    panel.configure(image = photo)
    panel.image = photo

def resize(image):
    width, height = image.size
    print "ratio", width/float(height)
    ratio = max(width/float(size[0]), height/float(size[1]))
    return image.resize((int(width/ratio), int(height/ratio)), Image.ANTIALIAS)

root.after(0, autoChange) # set the initial image, no delay
root.bind("<Right>", callbackRight) # debug key control
root.bind("<Left>", callbackLeft) # debug key control
root.mainloop()

# Stop the program execution after the slideshow is closed
running = False
print "Terminating"