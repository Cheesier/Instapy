from BaseAPI import BaseAPI

class Upload(BaseAPI):
    def run(self, json):
        return self.callback({'url': "test"})
    
    def callback(self, json):
        return json