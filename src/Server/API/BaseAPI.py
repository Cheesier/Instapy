
class BaseAPI:
    def run(self, data):
        return self.callback(self.process(data))
    
    def process(self, data):
        pass
    
    def callback(self, data):
        pass