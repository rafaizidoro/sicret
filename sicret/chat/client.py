import socket
import threading


class ChatClient:
    def __init__(self, host="127.0.0.1", port=6969):
        self.host = host
        self.port = port

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def receive(self):
        while True:  # making valid connection
            try:
                message = self.socket.recv(1024).decode("ascii")
                print(message)
            except:
                print("An error occured!")
                self.socket.close()
                break

    def write(self):
        while True:
            message = "{}: {}".format("U", input(""))
            self.socket.send(message.encode("ascii"))

    def run(self):
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

        write_thread = threading.Thread(target=self.write)
        write_thread.start()
