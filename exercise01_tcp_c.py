from socket import *
import time

ADDR = ("127.0.0.1", 8886)
filename = "入君怀.png"


def main():
    tcp_socket_client = socket()
    tcp_socket_client.connect(ADDR)

    with open(filename, "rb") as file:
        while True:
            data = file.read(1024)
            tcp_socket_client.send(data)
            if not data:
                break

    time.sleep(0.1) #防止粘包
    tcp_socket_client.send("上传完成".encode())

    tcp_socket_client.close()


if __name__ == '__main__':
    main()
