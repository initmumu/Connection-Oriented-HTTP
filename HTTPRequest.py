class Request:
    def __init__(self):
        self.method = None
        self.url = None
        self.version = "HTTP/1.1"
        self.header = dict()

        self.data = None

    def setRequest(self, method, host, url, data=None):
        self.method = method
        self.url = url
        self.version = "HTTP/1.1"

        self.data = data

        self.header = dict()
        self.header["Host"] = host
        self.header["Accept"] = "*/*"
        self.setContentLength()

    def setHost(self, host):
        self.header["Host"] = host

    def setURL(self, url):
        self.url = url

    def setVersion(self, version):
        self.version = version

    def setData(self, data):
        self.data = data

    def setHeader(self, key, value):
        self.header[key] = value

    def setContentLength(self):
        if self.data is None:
            return
        
        self.header["Content-Length"] = len(self.data)

    def encode_data(self):
        if type(self.data) is str:
            self.data = self.data.encode("utf-8")
    
    def __str__(self):
        request = ""
        request += f"{self.method} {self.url} {self.version}\r\n"
        
        for key, item in self.header.items():
            request += f"{key}: {item}\r\n"

        request += "\r\n"
        request += f"{self.data}"

        return request

