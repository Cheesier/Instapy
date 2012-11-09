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
import os
import random

filters = [
           CFilterVignette(),
           CFilterGrayscale(),
           #CFilterColor(),
           #CFilterPrime(),
           CFilterPlainBorder(),
           CFilterBlur(),
           ]

# Remove old images
oldPics = os.listdir("../slideshow")
for image in range(len(oldPics)):
    removeImg("../slideshow/" + oldPics[image])

# Add new filtered images
pics = os.listdir("../pic")
for image in range(len(pics)):
    c = CImageInstagram("../pic/" + pics[image])
    c.applyFilter(random.sample(filters, 1))
    c.save("../slideshow/" + pics[image])

lastShown = time.time()
n = 0

# Show slideshow
newPics = os.listdir("../pic")
while True:
    c = CImageInstagram("../pic/" + newPics[n])
    c.showImage()
    
    timeNow = time.time()
    print "lastShown:", timeNow-lastShown
    lastShown = timeNow
    
    time.sleep(1)
    n = (n+1)%len(newPics)