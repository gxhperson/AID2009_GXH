from socket import *

ADDR = ("127.0.0.1", 8888)
tcp_socket = socket()

# 连接服务端
tcp_socket.connect(ADDR)

# 数据收发
while True:
    data = input(">>")
    tcp_socket.send(data.encode())
    if not data:
        break
    # if data=="##":
    #     break
    data = tcp_socket.recv(1024)

    print("From server:", data.decode())

tcp_socket.close()

#/home/tarena/AID2009/gxh/month02_1030/