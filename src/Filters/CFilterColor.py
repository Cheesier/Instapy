import Lib
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
        #pixels = aImage.getdata()
        
        pixels = Lib.to2d(aImage)
        
        height = len(pixels)
        width = len(pixels[0])
        
        for x in range(width):
            for y in range(height):
                
                r = int(pixels[y][x][0]*self.amount[0])
                g = int(pixels[y][x][1]*self.amount[1])
                b = int(pixels[y][x][2]*self.amount[2])
                
                # human eye is bad at seeing red and blue, 
                # so we de-emphasize them
                #v = int(r + g + b);
                new_pixel = (r,g,b)
                new_image_list.append(new_pixel)
                
        new_image.putdata(new_image_list)
        return new_image