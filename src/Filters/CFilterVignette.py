import Image
from CFilter import *
import math

class CFilterVignette(CFilter):
    def applyFilter(self, aImage):
        def distanceFromCenter(self, pos):
            return math.sqrt((pos[0]-aImage.size[0]) + (pos[1]-aImage.size[1]))
        
        # intialize a new filtered image
        new_image = Image.new('RGB', aImage.size)
        new_image_list = []
        #get the pixels list from the original image
        pixels = aImage.getdata()
        """
        for pixel in pixels:
            r = int(pixel[0]);
            g = int(pixel[0]);
            b = int(pixel[0]);
            # human eye is bad at seeing red and blue, 
            # so we de-emphasize them
            v = int(0.2126*r + 0.7152*g + 0.0722*b);
            new_pixel = (v,v,v)
            new_image_list.append(new_pixel)
        """
        #traverse the pixel list and extract the R. G and B 
        #components for each pixel
        for x in range(aImage.size[1]):
            for y in range(aImage.size[0]):
                r = int(pixels[x][y][0]);
                g = int(pixels[x][y][0]);
                b = int(pixels[x][y][0]);
                # human eye is bad at seeing red and blue, 
                # so we de-emphasize them
                v = int(0.2126*r + 0.7152*g + 0.0722*b);
                new_pixel = (v,v,v)
                new_image_list.append(new_pixel)
                
        new_image.putdata(new_image_list)
        return new_image