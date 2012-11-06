import Image

def to2d(image):
    data = []
    pix = image.load()
    for y in xrange(image.size[1]):
        data.append([pix[x, y] for x in xrange(image.size[0])])
    return data