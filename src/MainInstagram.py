print "This is the first line of our Instagram application"
import CImageInstagram
from Filters.CFilterBrigthness import *
from Filters.CFilterBlur import *
from Filters.CFilterGrayscale import *
from Filters.CFilterVignette import *
from Filters.CFilterTest import *
from Filters.CFilterColor import *
from Filters.CFilterPrime import *


c = CImageInstagram.CImageInstagram("../pic/girl.jpg")
c.setDecription("This is a comment to this image")
c.printDescription()

"""
f = CFilterGrayscale()
c.applyFilter(f)
c.showImage()

f = CFilterBrigthness(0.5)
c.applyFilter(f)
c.showImage()

f = CFilterBlur()
c.applyFilter(f)
c.showImage()
"""

#c.applyFilter(CFilterTest())
c.applyFilter(CFilterColor((1,0,0)))
c.applyFilter(CFilterVignette(1))
c.showImage()
c.im_copy.save("../editedpic/latest.png")