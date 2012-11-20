import Image
from CFilter import *

class CFilterColor(CFilter):
    def __init__(self, amount=(1,1,1)):
        self.amount = amount
    def applyFilter(self, aImage):
        # intialize a new filtered image
        new_image = Image.new('RGB', aImage.size)
        new_image_list = []
        #get the pixels list from the original image
        pixels = aImage.getdata()
        
        for pixel in pixels:
                
            r = int(pixel[0]*self.amount[0])
            g = int(pixel[1]*self.amount[1])
            b = int(pixel[2]*self.amount[2])
            
            new_pixel = (r,g,b)
            new_image_list.append(new_pixel)
                
        new_image.putdata(new_image_list)
        return new_image