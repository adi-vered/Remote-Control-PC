import socket
import keyboard
import protocol
import server_manage

port = server_manage.KEYBOARD_PORT
address = ('0.0.0.0', port)

def main():
    server_socket = server_manage.start_server(address)
    client_socket = server_manage.get_client(server_socket)
    with open("C://Users//User//Documents//vs code python//Remote Control PC//check.txt" , "w") as my_file:
        while True:
            request = protocol.recv(client_socket).decode()
            if request:
                print(request)
                # keyboard.press_and_release(request)
                my_file.write(request)
                my_file.flush()
        
    server_socket.close()
    client_socket.close()

if __name__ == "__main__":
    main()