import socket
import queue
import threading
import HTTPRequest

class HTTPClient:
    def __init__(self, server_host, server_port):
        # 원격 서버 주소
        self.SERVER_HOST = server_host
        self.SERVER_PORT = server_port

        # 메시지 큐 생성
        self.sendMQ = queue.Queue()
        self.recvMQ = queue.Queue()

        # TCP 소켓 생성
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # 원격 서버에 접속 (TCP 3-way-handshake)
        self.client_socket.connect((self.SERVER_HOST, self.SERVER_PORT))

        # 송신 쓰레드 생성
        sender_thread = threading.Thread(target=self.message_sender)

        # 송신 쓰레드 실행
        sender_thread.start()

        # 수신 쓰레드 생성
        receiver_thread = threading.Thread(target=self.message_receiver)


        # 수신 쓰레드 실행
        receiver_thread.start()


    def send_message(self, msg):
        '''
        msg: string
        '''
        req = HTTPRequest.Request("GET", self.SERVER_HOST, "/", msg)
        self.sendMQ.put(req.get())
        
    
    def message_sender(self):
        while True:
            item = self.sendMQ.get()
            self.client_socket.sendall(item.encode())
            self.sendMQ.task_done()

    def recv_message(self):
        return self.recvMQ.get()

    def message_receiver(self):
        while True:
            item = self.client_socket.recv(1024)
            self.recvMQ.put(item.decode('utf-8'))
    

