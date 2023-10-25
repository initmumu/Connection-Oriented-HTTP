from Exception.NotFillResponseInfo import NotFillResponseInfo

STATUS_CODE = {
    100: 'Continue',
    101: 'Switching Protocols',
    102: 'Processing',
    103: 'Early Hints',
    200: 'OK',
    201: 'Created',
    202: 'Accepted',
    203: 'Non-Authoritative Information',
    204: 'No Content',
    205: 'Reset Content',
    206: 'Partial Content',
    207: 'Multi-Status',
    208: 'Already Reported',
    226: 'IM Used',
    300: 'Multiple Choices',
    301: 'Moved Permanently',
    302: 'Found',
    303: 'See Other',
    304: 'Not Modified',
    305: 'Use Proxy',
    307: 'Temporary Redirect',
    308: 'Permanent Redirect',
    400: 'Bad Request',
    401: 'Unauthorized',
    402: 'Payment Required',
    403: 'Forbidden',
    404: 'Not Found',
    405: 'Method Not Allowed',
    406: 'Not Acceptable',
    407: 'Proxy Authentication Required',
    408: 'Request Timeout',
    409: 'Conflict',
    410: 'Gone',
    411: 'Length Required',
    412: 'Precondition Failed',
    413: 'Payload Too Large',
    414: 'URI Too Long',
    415: 'Unsupported Media Type',
    416: 'Range Not Satisfiable',
    417: 'Expectation Failed',
    418: 'I\'m a teapot',  # April Fools' joke from RFC 2324
    421: 'Misdirected Request',
    422: 'Unprocessable Entity',
    423: 'Locked',
    424: 'Failed Dependency',
    425: 'Too Early',
    426: 'Upgrade Required',
    428: 'Precondition Required',
    429: 'Too Many Requests',
    431: 'Request Header Fields Too Large',
    451: 'Unavailable For Legal Reasons',
    500: 'Internal Server Error',
    501: 'Not Implemented',
    502: 'Bad Gateway',
    503: 'Service Unavailable',
    504: 'Gateway Timeout',
    505: 'HTTP Version Not Supported',
    506: 'Variant Also Negotiates',
    507: 'Insufficient Storage',
    508: 'Loop Detected',
    510: 'Not Extended',
    511: 'Network Authentication Required'
}

class Response:
    def __init__(self):
        self.version = "HTTP/1.1"
        self.status = None
        self.status_msg = None

        self.header = dict()
        self.body = None

    def setResponse(self, res):
        header, self.body = tuple(res.split("\r\n\r\n"))
        
        header = header.split("\r\n")
        statusLine = header[0].split()
        self.version = statusLine[0]
        self.status = statusLine[1]
        self.status_msg = statusLine[2]

        for i in range(1, len(header)):
            key, value = header[i].split(": ")
            self.header[key] = value

    def setMethod(self, method):
        self.method = method

    def setVersion(self, version):
        self.version = version

    def setStatus(self, status):
        self.status = status
        self.status_msg = STATUS_CODE[status]

    def setHeader(self, key, value):
        self.header[key] = value

    def setBody(self, data):
        self.body = data

    def checkInfo(self):
        if self.version is None:
            return False
        
        if self.status is None:
            return False
        
        if self.status_msg is None:
            return False
        
        if self.body is None:
            return False
        
        return True


    def __str__(self):
        if not self.checkInfo():
            raise NotFillResponseInfo("All necessary elements are not provided")
        
        res = ""
        res += f"{self.version} {self.status} {self.status_msg}\r\n"
        for key, item in self.header.items():
            res += f"{key}: {item}\r\n"
        res += "\r\n"
        res += f"{self.body}"

        return res

    
