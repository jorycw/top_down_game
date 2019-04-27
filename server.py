import socket, sys
from _thread import *

class Server():
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

class Client():
    def __init__(self, addr, cid):
        self.addr = addr
        self.cid = cid

    def threaded_client(self, conn):
        reply = ''
        while True:
            try:
                data = conn.recv(2048)
                reply = data.decode('utf-8')
                if not data:
                    print(f'Client {self.cid} disconnected')
                    break
                else:
                    print(f'Received: {reply}')
                    print(f'Sending: {reply}')
                conn.sendall(str.encode(reply))
            except:
                break

if __name__ == '__main__':
    server = Server('10.19.223.127', 5555)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind((server.ip, server.port))
    except socket.error as e:
        print(str(e))

    s.listen(2)
    print("Server started")

    clients = []
    client_num = 0
    while True:
        conn, addr = s.accept()
        clients.append(Client(addr, client_num))
        client_num += 1

        print(f"Connected to: {addr}")
        start_new_thread(clients[0].threaded_client, (conn))
