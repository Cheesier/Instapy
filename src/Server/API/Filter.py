from BaseAPI import BaseAPI
from Filters.CFilterBlur import CFilterBlur
from CImageInstagram import CImageInstagram

class Filter(BaseAPI):
    
    def __init__(self):
        self.filters = {
                   'blur': CFilterBlur(),
                  }
    
    def process(self, data):
        #filter = data['filter']
        #self.filters[filter.lower()].run(data)
        
        #if True: # found filter and image
            #c = CImageInstagram("../../../public/img/girl.jpg")
            #c.applyFilter(self.filter['blur'])
            #c.im_copy.save("../../../public/img/girl_blur.jpg")
        return {'url': "http://localhost:8080/img/girl.jpg"}
    
    def callback(self, data):
        return data