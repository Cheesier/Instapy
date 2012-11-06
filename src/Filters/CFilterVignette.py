import Image
from CFilter import *
import math

class CFilterVignette(CFilter):
    def __init__(self, amount):
        self.amount = amount
    def applyFilter(self, aImage):
        def distanceFromCenter(x,y):
            return math.sqrt((x-aImage.size[0]/2)**2 + (y-aImage.size[1]/2)**2) / math.sqrt((aImage.size[0]/2)**2 + (aImage.size[1]/2)**2)
        # intialize a new filtered image
        new_image = Image.new('RGB', aImage.size)
        new_image_list = []
        #get the pixels list from the original image
        pixels = aImage.getdata()
        #pix = Lib.to2d(aImage)
        #print len(pix),len(pix[1])
        
        #traverse the pixel list and extract the R. G and B 
        #components for each pixel
        n = 0
        x = 0
        y = 0
        for pixel in pixels:
            n += 1
            x = n % aImage.size[0]
            y = int(math.floor(n / aImage.size[0]))
            
            dist = distanceFromCenter(x,y)
            
            r = int(pixel[0]*(self.amount-dist))
            g = int(pixel[1]*(self.amount-dist))
            b = int(pixel[2]*(self.amount-dist))
            
            # human eye is bad at seeing red and blue, 
            # so we de-emphasize them
            #v = int(r + g + b);
            new_pixel = (r,g,b)
            new_image_list.append(new_pixel)
                
        new_image.putdata(new_image_list)
        return new_image