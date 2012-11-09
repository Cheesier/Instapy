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

lastShown = time.time()
n = 0

# Show slideshow
newPics = os.listdir("../slideshow")
while True:
    if n != current:
        c = CImageInstagram("../slideshow/" + newPics[n])
        c.showImage()
        
        timeNow = time.time()
        print "lastShown:", timeNow-lastShown
        lastShown = timeNow
        
        time.sleep(4.6)
    n = (n+1)%len(newPics)