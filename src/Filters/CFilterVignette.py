import Image
from CFilter import *
import math
import Lib

class CFilterVignette(CFilter):
    def __init__(self, amount=1):
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
        
        hardness = 1
        
        for x in range(width):
            for y in range(height):
                
                dist = Lib.distanceFromPoint(x, y, width/2, height/2) / math.sqrt((width/2)**2 + (height/2)**2)
                
                r = int(pixels[y][x][0]*(self.amount-dist))
                g = int(pixels[y][x][1]*(self.amount-dist))
                b = int(pixels[y][x][2]*(self.amount-dist))
                
                #r = int(r**hardness)
                #g = int(g**hardness)
                #b = int(b**hardness)
                
                new_image_list.append((r,g,b))
                
        new_image.putdata(new_image_list)
        return new_image