import socket
import tkinter as tk
import time
import PIL.ImageGrab
import protocol

def start_server(addr):
    sock = socket.socket()
    sock.bind(addr)
    sock.listen()
    print("server is up and running")
    return sock

def get_client(sock):
    print("waiting for client")
    sock_client, sock_address = sock.accept()
    print(f'Client connected: {sock_address} : {sock_client}')
    return sock_client

def take_screenshot():
    screen = PIL.ImageGrab.grab()
    screen.save("screenshot.jpg")
    data = "".encode()
    with open("screenshot.jpg", "rb") as screen_file:
        data = screen_file.read()
    return data

def main(addr):
    server_socket:socket = start_server(addr)
    client_socket:socket = get_client(server_socket)
    while True:
        protocol.split_send(client_socket, take_screenshot())
        time.sleep(0.1)
    
    server_socket.close()
    client_socket.close()

if __name__ == '__main__':
    port = 8852
    address = ('0.0.0.0', port)
    main(address)
