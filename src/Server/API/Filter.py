from BaseAPI import BaseAPI
from src.Filters.CFilterBlur import CFilterBlur
from src.Filters.CFilterPrime import CFilterPrime
from src.Filters.CFilterVignette import CFilterVignette
from src.CImageInstagram import CImageInstagram
import os

class Filter(BaseAPI):
    global filters
    filters = {
                   'blur': CFilterBlur(),
                   'prime': CFilterPrime(),
                   'vignette': CFilterVignette(),
                  }
    
    def process(self, data):
        path = "../../public/img/"
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
        return "http://localhost:8080/img/" + data + "_" + filename
    
    def genReturn(self, path):
        return {'url': path}
    
    def callback(self, data):
        return data