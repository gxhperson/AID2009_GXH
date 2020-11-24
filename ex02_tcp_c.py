from socket import *

ADDR = ("127.0.0.1", 8888)


# 数据收发
while True:
    data = input(">>")
    if not data:
        break
    tcp_socket = socket()
    tcp_socket.connect(ADDR)
    tcp_socket.send(data.encode())
    data = tcp_socket.recv(1024)
    print("From server:", data.decode())
    tcp_socket.close()

#/home/tarena/AID2009/gxh/month02_1030/