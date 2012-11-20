import Image
from CFilter import *

class CFilterContrast(CFilter):
    def __init__(self, amount=1.2):
        self.amount = amount
    def applyFilter(self, aImage):
        # intialize a new filtered image
        new_image = Image.new('RGB', aImage.size)
        new_image_list = []
        #get the pixels list from the original image
        pixels = aImage.getdata()

        for pixel in pixels:                
            r = int(pixel[0])
            g = int(pixel[1])
            b = int(pixel[2])
            
            if r < 128:
                r = r - int(abs(r * self.amount - r))
            elif r >= 128:
                r = int(r * self.amount)
                
            if g < 128:
                g = g - int(abs(g * self.amount - g))
            elif g >= 128:
                g = int(g * self.amount)
                
            if b < 128:
                b = b - int(abs(b * self.amount - b))
            elif b >= 128:
                b = int(b * self.amount)
            
            new_pixel = (r,g,b)
            new_image_list.append(new_pixel)
                
        new_image.putdata(new_image_list)
        return new_image