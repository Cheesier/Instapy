from BaseAPI import BaseAPI

class Upload(BaseAPI):
    def process(self, data):
        return {'url': "upload files or something?"}
    
    def callback(self, data):
        return data