"""
tcp套接字基础实例

"""
import time

from socket import *
tcp_socket=socket(AF_INET,SOCK_STREAM)
tcp_socket.bind(("0.0.0.0",8888))

#设置监听套接字
tcp_socket.listen(5)

#等待处理客户端连接
while True:
    print("Waiting for connect ...")
    connfd,addr=tcp_socket.accept()
    print("Connect from",addr)
    #收发数据
    while True:
        data =connfd.recv(5)
        if not data:
            break
        print("Receive",data.decode())
        # if data.decode() == "##":
        #     break
        connfd.send(b"Thanks")
        #粘包实验  等0.1秒
        time.sleep(0.1)

    connfd.close()

tcp_socket.close()



