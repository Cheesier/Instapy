import Image

def to2d(image):
    pix = image.getdata()
    size = image.size
    
    sizeX = size[0]
    data = []
    temp = []
    for i in range(len(pix)):
        temp.append(pix[i])
        if (i != 0 and i % sizeX == 0) or i == len(pix)-1:
            data.append([temp])
            temp = []
    return data