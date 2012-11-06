import Image
from CFilter import *

class CFilterBrigthness(CFilter):
    def __init__(self, brightness):
        self.brightness = brightness
    def applyFilter(self, aImage):    
        #define the brightness factor
        if aImage.mode != 'RGB':
            print "Covert image to RGB"
            aImage = aImage.convert('RGB')
            
        #intialize the new brighter image that we will create
        new_image = Image.new('RGB', aImage.size)
        new_image_list = []
        pixels = aImage.getdata()
        #for each pixel, append the brightened or 
        # darkened version to the new image list
            
        for pixel in pixels:
            new_pixel = (int(pixel[0] * self.brightness), \
                         int(pixel[1] * self.brightness), \
                         int(pixel[2] * self.brightness))
            # print new_pixel
            #check the new pixel values are within rgb range
            for pixel in new_pixel:
                if pixel > 255:
                    pixel = 255
                elif pixel < 0:
                    pixel = 0
            new_image_list.append(new_pixel)
        # print new_pixel
                #aImage.putdata(new_image_list)
        new_image.putdata(new_image_list)
        return new_image