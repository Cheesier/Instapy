import Image
from src.CFilter import *
import math
import src.Lib

class CFilterVignette(CFilter):
    def __init__(self, amount=1):
        self.amount = amount
    def applyFilter(self, aImage):
        # intialize a new filtered image
        new_image = Image.new('RGB', aImage.size)
        new_image_list = []
        #get the pixels list from the original image
        #pixels = aImage.getdata()
        
        pixels = src.Lib.to2d(aImage)
        
        height = len(pixels)
        width = len(pixels[0])
        
        hardness = 1
        
        for x in range(width):
            for y in range(height):
                
                dist = src.Lib.distanceFromPoint(x, y, width/2, height/2) / math.sqrt((width/2)**2 + (height/2)**2)
                
                r = pixels[y][x][0]*(self.amount-dist)
                g = pixels[y][x][1]*(self.amount-dist)
                b = pixels[y][x][2]*(self.amount-dist)
                
                r = int(r**hardness)
                g = int(g**hardness)
                b = int(b**hardness)
                
                
                # human eye is bad at seeing red and blue, 
                # so we de-emphasize them
                #v = int(r + g + b);
                new_pixel = (r,g,b)
                new_image_list.append(new_pixel)
                
        new_image.putdata(new_image_list)
        return new_image