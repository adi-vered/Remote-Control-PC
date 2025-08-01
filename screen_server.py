import socket
import tkinter as tk
import time
import PIL.ImageGrab
import protocol
import server_manage

def take_screenshot():
    screen = PIL.ImageGrab.grab()
    screen.save("screenshot.jpg")
    data = "".encode()
    with open("screenshot.jpg", "rb") as screen_file:
        data = screen_file.read()
    return data

port = server_manage.SCREEN_PORT
address = ('0.0.0.0', port)
server_socket:socket = server_manage.start_server(address)
client_socket:socket = server_manage.get_client(server_socket)
while True:
    protocol.split_send(client_socket, take_screenshot())
    time.sleep(0.1)
    
server_socket.close()
client_socket.close()


