import socket
import queue
import threading
from .HTTPRequest import Request
from .HTTPResponse import Response

class HTTPClient:
    def __init__(self, server_host, server_port):
        self.SERVER_HOST = server_host
        self.SERVER_PORT = server_port

        self.sendMQ = queue.Queue()
        self.recvMQ = queue.Queue()

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.SERVER_HOST, self.SERVER_PORT))

        sender_thread = threading.Thread(target=self.messageSender)
        sender_thread.daemon = True
        sender_thread.start()

        receiver_thread = threading.Thread(target=self.messageReceiver)
        receiver_thread.daemon = True
        receiver_thread.start()


    def sendMessage(self, msg):
        '''
        msg: string
        '''
        req = Request()
        req.setRequest("GET", self.SERVER_HOST, "/", msg)
        self.sendMQ.put(str(req))
    
    def messageSender(self):
        while True:
            item = self.sendMQ.get()
            self.client_socket.sendall(item.encode())
            self.sendMQ.task_done()

    def recvMessage(self):
        originalMsg = self.recvMQ.get()
        res = Response()
        res.setResponse(originalMsg)

        return res

    def messageReceiver(self):
        while True:
            item = self.client_socket.recv(1024).decode('utf-8')
            if item.startswith("EM"):
                print(item) # EM 출력
            
            else:
                self.recvMQ.put(item)
    
    def close(self):
        self.client_socket.close()

