from BaseAPI import BaseAPI
#from Filters.CFilterBlur import CFilterBlur
#from Filters.CFilterPrime import CFilterPrime
#from Filters.CFilterVignette import CFilterVignette
from CImageInstagram import CImageInstagram
import os

"""
global filters
filters = {
           'blur': CFilterBlur(),
           'prime': CFilterPrime(),
           'vignette': CFilterVignette(),
           }
"""

class Filter(BaseAPI):
    
    def process(self, data):
        path = "../../public/tmp/"
        filename = "girl.jpg"
        
        #if os.path.exists(path + data + "_" + filename):
        #    return self.genReturn(self.getUrl(filename, data))
        
        c = CImageInstagram(path + filename)
        c.applyFilter(data)
        c.save(path + data + '_' + filename)
        return self.getUrl(filename, data.lower())
    
    def getUrl(self, filename, data):
        return "http://localhost:8080/tmp/" + data + "_" + filename
    
    def genReturn(self, path):
        return {'url': path}
    
    def callback(self, data):
        return data