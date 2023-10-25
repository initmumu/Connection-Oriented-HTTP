class Request:
    def __init__(self, method, host, url, data=None):
        self.method = method
        self.url = url
        self.version = "HTTP/1.1"

        self.data = data
        self.encode_data()

        self.header = dict()
        self.header["Host"] = host
        self.header["Accept"] = "*/*"
        self.header["Content-Length"] = self.calc_content_length()

    def encode_data(self):
        if type(self.data) is str:
            self.data = self.data.encode("utf-8")

    def calc_content_length(self):  
        return len(self.data)
    
    def get(self):
        request = ""
        request += f"{self.method} {self.url} {self.version}\r\n"
        
        for key, item in self.header.items():
            request += f"{key}: {item}\r\n"

        request += "\r\n"
        request += f"{self.data}"

        return request

