# import http.client
# import time

# conn = http.client.HTTPConnection("localhost", 8000)

# print("Before:", conn._http_vsn, conn._http_vsn_str)  # 기본적으로 1.1로 설정됨
# conn._http_vsn = 11
# conn._http_vsn_str = 'HTTP/1.1'
# print("After:", conn._http_vsn, conn._http_vsn_str)  # 명시적으로 1.1로 설정함
# # Send a GET request to the server
# conn.request("GET", "/", headers={"Connection": "keep-alive"})
# response = conn.getresponse()

# # Print the response
# print("Status:", response.status, response.reason)
# print("Response body:", response.read().decode())

# time.sleep(100)
import requests
import time
a=requests.get("http://localhost:5000/")
print(a)
time.sleep(100)