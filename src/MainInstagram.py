print "This is the first line of our Instagram application"
from CImageInstagram import *
from Filters.CFilterBrigthness import *
from Filters.CFilterBlur import *
from Filters.CFilterGrayscale import *
from Filters.CFilterVignette import *
from Filters.CFilterTest import *
from Filters.CFilterColor import *
from Filters.CFilterPrime import *
from Filters.CFilterContrast import *
from Filters.CFilterPlainBorder import *
import time


c = CImageInstagram("../pic/insta04.jpg")
c.setDecription("This is a comment to this image")
c.printDescription()

filters =  [
           #CFilterPlainBorder(25, (0,0,0)),
           #CFilterColor([1,0,0]),
           #CFilterBlur(),
           #CFilterVignette(1),
           #CFilterPrime(),
           CFilterContrast(),
           #CFilterBrigthness(1),
           #CFilterGrayscale(),
           #CFilterTest(),
           ]

oldtime =  time.time()
c.applyFilter(filters)
print time.time()-oldtime, "seconds taken for all filters"
#c.applyFilter(CFilterVignette(1))
c.showImage()
#c.im_copy.save("../editedpic/latest.png")