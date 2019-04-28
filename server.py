import socket
from _thread import *
from player import Player
import pickle
import game_state as g_s
import obj


def setup_game(obstacles):
    block_size = (30, 30)
    game_size = (500, 500)

    x = 0
    y = 0

    while x < game_size[0]:
        obstacles.append(obj.Object(x, y))
        obstacles.append(obj.Object(x, game_size[1] - block_size[1]))
        x += block_size[0]
    x = 0
    y = 0
    while y < game_size[1]:
        obstacles.append(obj.Object(x, y))
        obstacles.append(obj.Object(game_size[0] - block_size[0], y))
        y += block_size[1]


## WA wifi? bens server = '10.19.223.127'
## Labs comp server = '172.28.1.88'

players = {}
projectiles = {}
obstacles = []

setup_game(obstacles)


server = '128.208.1.137'
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")



def threaded_client(conn, player):
    start_state = [g_s.Game_State(player, players, projectiles), obstacles]
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

    players.pop(player)
    projectiles.pop(player)       

    print("Lost connection")
    conn.close()



    



next_player = 0

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    players[next_player] = Player(20, 20)
    projectiles[next_player] = []

    start_new_thread(threaded_client, (conn, next_player))

    next_player += 1

