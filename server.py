import socket, sys
from _thread import *

class Server():
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

def read_pos(s):
    s = s.split(',')
    return int(s[0]), int(s[1])

def make_pos(t):
    return f'{t[0]},{t[1]}'

pos = [(0, 0), (50, 50)]

def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ''
    while True:
        try:
            data = read_pos(conn.recv(2048).decode)
            pos[player] = data

            if not data:
                print(f'Client {player} disconnected')
                break
            else:
                reply = pos[player - 1]
                print(f'Received: {data}')
                print(f'Sending: {reply}')
            conn.sendall(str.encode(make_pos(reply)))
        except:
            break
    print('Lost Connection')
    conn.close()

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
        print(f"Connected to: {addr}")
        start_new_thread(threaded_client, (conn, client_num))
        client_num += 1
