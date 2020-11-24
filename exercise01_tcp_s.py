from socket import *
import time

ADDR=("0.0.0.0",8886)
filename="%s-%s-%s-%s-%s-%s.png"%time.localtime()[:6]


def new_photo(connfd):
    with open(filename,"wb") as file:
        # 收发
        while True:
            data = connfd.recv(1024)
            if not data:
                break
            file.write(data)

    time.sleep(0.1)
    if connfd.recv(1024).decode() == "上传完成":
        print("上传完成")


def main():
    tcp_socket_sevrver=socket()
    tcp_socket_sevrver.bind(ADDR)

    tcp_socket_sevrver.listen(5)
    connfd,addr=tcp_socket_sevrver.accept()

    new_photo(connfd)

    connfd.close()
    tcp_socket_sevrver.close()

if __name__ == '__main__':
    main()