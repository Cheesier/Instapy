import Image
from CFilter import CFilter
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

global filter_list
filter_list = {
           'blur': CFilterBlur(),
           'prime': CFilterPrime(),
           'vignette': CFilterVignette(),
           'invert': CFilterInvert(),
           'color': CFilterColor(),
           'contrast': CFilterContrast(),
           'plainborder': CFilterPlainBorder(),
           'brigthness': CFilterBrigthness(),
           'grayscale': CFilterGrayscale(),
           }

class CImageInstagram:
    def __init__(self, filename=None):
        self.name = filename
        self.im = Image.open(filename)
        self.im_copy = self.im
    def setDecription(self, description=None):
        self.desc = description
    def printDescription(self):
        print self.desc
    def applyFilter(self, aCFilter):
        if isinstance(aCFilter, list) and len(aCFilter) > 0 and isinstance(aCFilter[0], CFilter):
            self.im_copy = aCFilter[0].applyFilter(self.im_copy)
            print "added", aCFilter[0].__class__.__name__
            self.applyFilter(aCFilter[1:])
        elif isinstance(aCFilter, CFilter):
            self.im_copy = aCFilter.applyFilter(self.im_copy)
        elif isinstance(aCFilter, list) and len(aCFilter) > 0 and isinstance(aCFilter[0], str):
            self.applyFilter(filter_list[aCFilter[0]])
            self.applyFilter(aCFilter[1:])
        elif isinstance(aCFilter, str):
            if aCFilter in filter_list:
                self.im_copy = filter_list[aCFilter].applyFilter(self.im_copy)
    def isChanged(self):
        return self.im_copy != self.im
    def resetFilter(self):
        self.im_copy = self.im
    def showImage(self):
        self.im_copy.show()
    def save(self, filename):
        self.im_copy.save(filename)
    def getImage(self):
        return self.im_copy