
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 9000))

server.listen()

print("Server is listening on port 9000...")

connection, address = server.accept()

print("Connected client:", address)

data = connection.recv(1024)

print("Received data:", data.decode("utf-8"))

connection.sendall(b"Hello! Python received your message.")

connection.close()
server.close()
