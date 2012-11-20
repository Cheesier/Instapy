import Image
from CFilter import *

class CFilterGrayscale(CFilter):
    def applyFilter(self, aImage):
        # intialize a new filtered image
        new_image = Image.new('RGB', aImage.size)
        new_image_list = []
        #get the pixels list from the original image
        pixels = aImage.getdata()
        #traverse the pixel list and extract the R. G and B 
        #components for each pixel
        for pixel in pixels:
            r = int(pixel[0]);
            g = int(pixel[0]);
            b = int(pixel[0]);
            # human eye is bad at seeing red and blue, 
            # so we de-emphasize them
            v = int(0.2126*r + 0.7152*g + 0.0722*b);
            new_pixel = (v,v,v)
            new_image_list.append(new_pixel)
        new_image.putdata(new_image_list)
        return new_image