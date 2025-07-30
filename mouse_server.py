import socket
import win32api
import win32con
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

def main(addr):
    server_socket = start_server(addr)
    client_socket = get_client(server_socket)
    while True:
        request = protocol.short_recv(client_socket).decode()
        print(request)
        if request:
            print(request)
    
    server_socket.close()
    client_socket.close()

if __name__ == '__main__':
    port = 8853
    address = ('0.0.0.0', port)
    main(address)
