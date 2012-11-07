import Image
from CFilter import *
import math
import Lib
import time

class CFilterPrime(CFilter):
    def __init__(self, amount=1):
        self.amount = amount
    def applyFilter(self, aImage):
        oldtime = time.time()
        # intialize a new filtered image
        new_image = Image.new('RGB', aImage.size)
        new_image_list = []
        #get the pixels list from the original image
        #pixels = aImage.getdata()
        
        pixels = Lib.to2d(aImage)
        
        height = len(pixels)
        width = len(pixels[0])
        
        print height, width
        n = 0
        p = 1
        for x in range(width):
            for y in range(height):
                
                r = int(pixels[y][x][0]*self.amount)
                g = int(pixels[y][x][1]*self.amount)
                b = int(pixels[y][x][2]*self.amount)
                
                if Lib.isprime(n):
                    r=g=b=0
                    p+=1
                
                # human eye is bad at seeing red and blue, 
                # so we de-emphasize them
                #v = int(r + g + b);
                new_pixel = (r,g,b)
                new_image_list.append(new_pixel)
                n+=1
                
        new_image.putdata(new_image_list)
        timetaken = time.time()-oldtime
        print "primes:", n-p, ", out of", n , "pixels", ", it took", timetaken, "seconds"
        return new_image