from socket import *

ADDR = ("127.0.0.1", 8887)


# 数据收发
while True:
    data = input("我：")
    if not data:
        break
    tcp_socket = socket()

    tcp_socket.connect(ADDR)
    tcp_socket.send(data.encode())

    data = tcp_socket.recv(1024)


    print("小美:", data.decode())

tcp_socket.close()

#/home/tarena/AID2009/gxh/month02_1030/