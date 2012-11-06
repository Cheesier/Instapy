import Image
import math

def to2d(image):
    data = []
    pix = image.load()
    for x in xrange(image.size[0]):
        data.append([pix[x,y] for y in xrange(image.size[1])])
    return data

def distanceFromPoint(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)