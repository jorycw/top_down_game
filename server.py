import socket
from _thread import *
from player import Player
import pickle
import game_state as g_s

## WA wifi? bens server = '10.19.223.127'
## Labs comp server = '172.28.1.88'
server = '128.208.1.137'
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

players = []
projectiles = {}

def threaded_client(conn, player):
    start_state = g_s.Game_State(player, players, projectiles)
    print(start_state)
    conn.send(pickle.dumps(start_state))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(4096))
            players[player] = data[0]
            if data[1] != None:
                projectiles[player].append(data[1])

            for p in projectiles[player]:
                p.update()

            if not data:
                print("Disconnected")
                break
            else:
                reply = g_s.Game_State(player, players, projectiles)

                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    players.append(Player(20, 20))
    projectiles[len(players) - 1] = []

    start_new_thread(threaded_client, (conn, len(players) - 1))