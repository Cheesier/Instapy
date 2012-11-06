import Image

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
        self.im_copy = aCFilter.applyFilter(self.im_copy)
    def resetFilter(self):
        self.im_copy = self.im
    def showImage(self):
        self.im_copy.show()
    def save(self, filename):
        self.im_copy.save(filename)