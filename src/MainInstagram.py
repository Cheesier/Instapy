print "This is the first line of our Instagram application"
import CImageInstagram
from Filters.CFilterBrigthness import *
from Filters.CFilterBlur import *
from Filters.CFilterGrayscale import *
from Filters.CFilterVignette import *


c = CImageInstagram.CImageInstagram("../pic/insta01.jpg")
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

f = CFilterVignette()
c.applyFilter(f)
c.showImage()