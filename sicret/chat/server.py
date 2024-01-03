import socket
import threading


class ChatServer:
    def __init__(self, host="127.0.0.1", port=6969):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []
        self.rooms = {}

        self.socket.bind((self.host, self.port))
        self.socket.listen()

    def broadcast(self, message):
        for client in self.clients:
            client.send(message)

    def handle(self, client):
        while True:
            try:
                message = client.recv(1024)
                self.broadcast(message)
            except:
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                # nickname = self.nicknames[index]
                self.broadcast("{} left!".format("ddd").encode("ascii"))
                # nicknames.remove(nickname)
                break

    def listen(self):
        while True:
            client, address = self.socket.accept()
            print("Connected with {}".format(str(address)))

            # client.send("NICKNAME".encode("ascii"))
            # nickname = client.recv(1024).decode("ascii")
            # nicknames.append(nickname)
            self.clients.append(client)
            # print("Nickname is {}".format(nickname))
            # broadcast("{} joined!".format(nickname).encode("ascii"))
            client.send("Connected to server!".encode("ascii"))
            thread = threading.Thread(target=self.handle, args=(client,))
            thread.start()
