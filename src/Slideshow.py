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
from Tkinter import Tk, Canvas, Frame, BOTH, NW
import ImageTk

class ImgDisplayer(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Slideshow")        
        self.pack(fill=BOTH, expand=1)
        
        self.img = Image.open("../pic/girl.jpg")
        self.tatras = ImageTk.PhotoImage(self.img)

        canvas = Canvas(self, width=self.img.size[0]+20, 
           height=self.img.size[1]+20)
        canvas.create_image(10, 10, anchor=NW, image=self.tatras)
        canvas.pack(fill=BOTH, expand=1)


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
global current
current = -1

class applyFilterLoop(threading.Thread):
    def run(self):
        p = 0
        while True:
            global current
            current = p
            c = CImageInstagram("../pic/" + pics[p])
            c.applyFilter(random.sample(filters, 1))
            c.save("../slideshow/" + pics[p])
            p = (p+1)%len(pics)

filterLoop = applyFilterLoop()
filterLoop.start()

def newImage():
    root.after(5000, newImage)

# window stuff
root = Tk()
ex = ImgDisplayer(root)
ex.focus()
root.after(5000, newImage)
root.mainloop()

lastShown = time.time()
n = 0

# Show slideshow
newPics = os.listdir("../slideshow")
while True:
    if n != current:
        c = CImageInstagram("../slideshow/" + newPics[n])
        ex.img = c.getImage()
        root.mainloop()
        #c.showImage()
        
        timeNow = time.time()
        print "lastShown:", timeNow-lastShown
        lastShown = timeNow
        
        time.sleep(4.8)
    n = (n+1)%len(newPics)