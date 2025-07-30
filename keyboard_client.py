import socket
import keyboard
import protocol

port = 8851
my_socket = socket.socket()

def start_log():
    keyboard.on_release(callback=callback)
    keyboard.wait()
    
def callback(event):
    button = event.name
    protocol.short_send(my_socket, button.encode())

def main():
    my_socket.connect(("127.0.0.1", port))
    print("connected")
    start_log()
    my_socket.close()
    print("end")

if __name__ == "__main__":
    main()