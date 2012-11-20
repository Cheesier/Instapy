import Image
from CFilter import *
import math
import Lib
import time

class CFilterPrime(CFilter):
    def __init__(self, multiply=(0, 0, 0)):
        self.multiply = multiply
    def applyFilter(self, aImage):
        # intialize a new filtered image
        new_image = Image.new('RGB', aImage.size)
        new_image_list = []
        #get the pixels list from the original image
        pixels = aImage.getdata()
        
        primes = Lib.primes
        prime = 0
        
        n = 0
        p = 1
        #for x in range(width):
            #for y in range(height):
        for pixel in pixels:
                
            r = int(pixel[0])
            g = int(pixel[1])
            b = int(pixel[2])
            
            if primes[prime] == n:
                r*= int(self.multiply[0])
                g*= int(self.multiply[1])
                b*= int(self.multiply[2])
                p+=1
                prime += 1
            
            new_pixel = (r,g,b)
            new_image_list.append(new_pixel)
            n+=1
                
        new_image.putdata(new_image_list)
        print "primes:", n-p, ", out of", n , "pixels"
        return new_image