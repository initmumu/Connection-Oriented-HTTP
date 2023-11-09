# import http.server
# import socketserver
# import threading

# PORT = 8000

# class HTTPServer2(socketserver.ThreadingMixIn, socketserver.TCPServer):
#     def service_actions(self):
#         # 여기에 원하는 커스텀 동작을 추가합니다.
#         print(threading.active_count())

# Handler = http.server.SimpleHTTPRequestHandler

# # with HTTPServer2(("", PORT), Handler) as httpd:
# #     print("Serving at port", PORT)
# #     httpd.serve_forever()

# import http.server
# import socketserver
# import threading
# class HTTPServer2(socketserver.ThreadingMixIn, socketserver.TCPServer):
#     def service_actions(self):
#         # 여기에 원하는 커스텀 동작을 추가합니다.
#         print("활성 쓰레드 수: ", threading.active_count())

# class MyHandler(http.server.SimpleHTTPRequestHandler):

#     # Override method to add 'Connection: keep-alive' header
#     def send_response(self, code, message=None):
#         self.send_response_only(code, message)
#         self.send_header('Connection', 'keep-alive')  # Add this line
#         self.send_header('Content-type', 'text/html')
#         self.end_headers()

#     def do_GET(self):
#         super().do_GET()
#         print("[클라이언트 접속]")
#         self.send_response(200)
#         self.wfile.write(b'Hello, world!')

# # Create server with handler
# PORT = 8080
# httpd = HTTPServer2(("", PORT), MyHandler)

# print("serving at port", PORT)
# httpd.serve_forever()

from flask import Flask
import threading
import time
def f():
    while True:
        time.sleep(3)
        print(threading.active_count())

t = threading.Thread(target=f)
t.start()

app = Flask(__name__)

@app.route("/")
def hello_connection():
    return "Connected"

if __name__ == "__main__":
    app.run(debug=True, threaded=True)