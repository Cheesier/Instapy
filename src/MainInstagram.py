print "This is the first line of our Instagram application"
from CImageInstagram import CImageInstagram
from Filters.CFilterBrigthness import CFilterBrigthness
from Filters.CFilterBlur import CFilterBlur
from Filters.CFilterGrayscale import CFilterGrayscale
from Filters.CFilterVignette import CFilterVignette
from Filters.CFilterTest import CFilterTest
from Filters.CFilterColor import CFilterColor
from Filters.CFilterPrime import CFilterPrime
from Filters.CFilterContrast import CFilterContrast
from Filters.CFilterPlainBorder import CFilterPlainBorder
from Filters.CFilterInvert import CFilterInvert
import time


c = CImageInstagram("../pic/girl.jpg")
c.setDecription("This is a comment to this image")
c.printDescription()

filters =  [
           #CFilterPlainBorder(25, (0,0,0)),
           #CFilterColor([1,0,0]),
           #CFilterBlur(),
           #CFilterVignette(1),
           #CFilterPrime(),
           #CFilterInvert(),
           #CFilterContrast(),
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