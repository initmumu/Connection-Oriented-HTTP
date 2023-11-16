class BaseHandler:
    def __init__(self):
        self.router = dict()
        user = ""

    def registerHandler(self, url, handler):
        self.router[url] = handler

    def processEvent(self, req):
        try:
            handler = self.router[req.url]
            handler(req)
        except Exception as e:
            print(f"Can not find Event Handler for {req.url}")
            return
        
    def client_handler(self, client_socket):
        print("Client Address: ", client_socket.addr)
        user = client_socket.recv(1024)
        string = "User name :  %s "%user.decode()
        client_socket.sendall(string.encode())