print "This is the first line of our Instagram application"
import Image
import ImageFilter
#im = Image.open("../pic/girl.jpg")
#im.filter(ImageFilter.BLUR).rotate(45).show()

class CImageInstagram:
    def __init__(self, filename=None):
        self.name = filename
        self.im = Image.open(filename)
    def setDecription(self, description=None):
        self.desc = description
    def printDescription(self):
        print self.desc
    def setFilter(self, filter=None):
        self.im = self.im.filter(filter)
        self.im.show()
        
c = CImageInstagram("../pic/insta01.jpg")
c.setDecription("This is a comment to this image")
c.printDescription()
c.setFilter(ImageFilter.EMBOSS)