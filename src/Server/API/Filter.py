from BaseAPI import BaseAPI
from CImageInstagram import CImageInstagram
import os

class Filter(BaseAPI):
    
    def process(self, filename="girl.jpg", filtername="blur"):
        path = "../../public/tmp/"
        
        # check if processed already, in that case just toss the url back
        if os.path.exists(path + filtername + "_" + filename):
            return {'src': '/tmp/' + filtername + "_" + filename,
                    'filter': filtername}
        
        # is the said file actually uploaded?
        elif not os.path.exists(path + filename):
            return self.retError("The file '{0}' is not uploaded to the server.".format(filename))
        
        
        c = CImageInstagram(path + filename)
        c.applyFilter(filtername)
        if c.isChanged():
            c.save(path + filtername + '_' + filename)
            return {'src': self.getUrl(filename, filtername.lower()),
                    'filter': filtername}
        else:
            return self.retError("No filter with that name, consult documentation.")
    
    def getUrl(self, filename, data):
        return "/tmp/" + data + "_" + filename
    
    def retError(self, msg):
        return {'Error': msg}