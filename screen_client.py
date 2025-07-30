import socket
import protocol

port = 8852

my_socket = socket.socket()
my_socket.connect(("127.0.0.1", port))
print("connected")

while True:
    image_data = protocol.split_recv(my_socket)
    if not image_data:
        continue
    with open("sent.jpg", "wb") as sent_file:
        sent_file.write(image_data)

my_socket.close()