"""
tcp套接字基础实例

"""

from socket import *
import re

chat = {}


def chat_dict():
    list_ = []
    with open("chat.txt", "r") as f:
        for line in f:
            list_ += re.findall("(\S+)\s+(.+)", line)
    return dict(list_)


def get_answer(question):
    for key in chat:
        if key in question:
            return chat[key]
        else:
            return "人家还小，不知道啦"


def main():
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.bind(("0.0.0.0", 8887))
    tcp_socket.listen(5)

    while True:
        connfd, addr = tcp_socket.accept()
        # 来自客户端的提问
        data = connfd.recv(1024)

        result = get_answer(data.decode())

        connfd.send(result.encode())
        connfd.close()

    tcp_socket.close()


if __name__ == '__main__':
    chat = chat_dict()
    print(chat)
    main()
