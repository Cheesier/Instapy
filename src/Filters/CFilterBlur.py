from src.CFilter import *
from ImageFilter import *

class CFilterBlur(CFilter):
    def applyFilter(self, aImage):
        aImage = aImage.filter(BLUR)
        return aImage