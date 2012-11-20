from BaseAPI import BaseAPI
from Filters.CFilterBlur import CFilterBlur
from Filters.CFilterPrime import CFilterPrime
from Filters.CFilterVignette import CFilterVignette
from CImageInstagram import CImageInstagram
import os

class Filter(BaseAPI):
    
    global filters
    filters = {
                   'blur': CFilterBlur(),
                   'prime': CFilterPrime(),
                   'vignette': CFilterVignette(),
                  }
    
    def process(self, data):
        path = "../../public/tmp/"
        filename = "girl.jpg"
        
        if os.path.exists(path + data + "_" + filename):
            return self.genReturn(self.getUrl(filename, data))
        
        c = CImageInstagram(path + filename)
        if data in filters:
            c.applyFilter(filters[data])
            c.im_copy.save(path + data + "_" + filename)
            return self.genReturn(self.getUrl(filename, data))
        else:
            return {'error': "no such filter"}
    
    def getUrl(self, filename, data):
        return "http://localhost:8080/tmp/" + data + "_" + filename
    
    def genReturn(self, path):
        return {'url': path}
    
    def callback(self, data):
        return data