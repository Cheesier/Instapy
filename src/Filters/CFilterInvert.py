import Image
from src.CFilter import *

class CFilterInvert(CFilter):
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
            
            r = 255 - r
            g = 255 - g
            b = 255 - b
            
            new_pixel = (r,g,b)
            new_image_list.append(new_pixel)
                
        new_image.putdata(new_image_list)
        return new_image