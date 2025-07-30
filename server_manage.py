import socket

KEYBOARD_PORT = 8851
SCREEN_PORT = 8852
MOUSE_PORT = 8853

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

