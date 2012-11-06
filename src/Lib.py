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

def isprime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False    
    else:
        for n in range(3, int(x**0.5)+2, 2):
            if x % n == 0:
                return False
        return True