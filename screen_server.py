import socket
import time
import PIL.ImageGrab
import protocol
import server_manage

screenshot_path = "screenshot.png"
def take_screenshot():
    screen = PIL.ImageGrab.grab()
    screen.save(screenshot_path)
    data = "".encode()
    with open(screenshot_path, "rb") as screen_file:
        data = screen_file.read()
    return data

port = server_manage.SCREEN_PORT
address = ('0.0.0.0', port)
def main():
    server_socket:socket = server_manage.start_server(address)
    client_socket:socket = server_manage.get_client(server_socket)
    while True:
        protocol.send(client_socket, take_screenshot())
        time.sleep(protocol.REST_BETWEEN_SCREENSHOTS)
        
    server_socket.close()
    client_socket.close()

if __name__ == "__main__":
    main()
