print "This is the first line of our Instagram application"
import CImageInstagram
from CFilterBrigthness import *
from CFilterBlur import *


c = CImageInstagram.CImageInstagram("../pic/insta01.jpg")
c.setDecription("This is a comment to this image")
c.printDescription()


f = CFilterBrigthness(0.5)
c.applyFilter(f)
c.showImage()

f = CFilterBlur()
c.applyFilter(f)
c.showImage()

