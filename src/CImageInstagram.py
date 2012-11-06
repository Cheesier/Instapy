import Image

class CImageInstagram:
    def __init__(self, filename=None):
        self.name = filename
        self.im = Image.open(filename)
    def setDecription(self, description=None):
        self.desc = description
    def printDescription(self):
        print self.desc
    def applyFilter(self, aCFilter):
        self.im_copy = aCFilter.applyFilter(self.im)
    def showImage(self):
        self.im_copy.show()