from CImageInstagram import *
from Filters.CFilterBrigthness import *
from Filters.CFilterBlur import *
from Filters.CFilterGrayscale import *
from Filters.CFilterVignette import *
from Filters.CFilterTest import *
from Filters.CFilterColor import *
from Filters.CFilterPrime import *
from Filters.CFilterPlainBorder import *
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

pics = os.listdir("../pic")

lastShown = time.time()
n = 0
while True:
    c = CImageInstagram("../pic/" + pics[n])
    c.applyFilter(random.sample(filters, 1))
    c.showImage()
    
    timeNow = time.time()
    print "lastShown:", timeNow-lastShown
    lastShown = timeNow
    
    time.sleep(1)
    n = (n+1)%len(pics)