import Image
from src.CFilter import *
import src.Lib

class CFilterPlainBorder(CFilter):
    def __init__(self, size=25, color=(1, 1, 1)):
        self.size = size
        self.color = color
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
                    
                if x > self.size and x < (width - self.size) and \
                y > self.size and y < (height - self.size):
                    r = int(pixels[y][x][0])
                    g = int(pixels[y][x][1])
                    b = int(pixels[y][x][2])
                else:
                    r = int(self.color[0]*255)
                    g = int(self.color[1]*255)
                    b = int(self.color[2]*255)
                
                new_pixel = (r,g,b)
                new_image_list.append(new_pixel)
                
        new_image.putdata(new_image_list)
        return new_image