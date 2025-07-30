import socket
import win32api
import win32con
import protocol
from pynput.mouse import Button, Controller
import server_manage

port = server_manage.MOUSE_PORT
address = ('0.0.0.0', port)

mouse = Controller()

# Set pointer position
mouse.position = (10, 20)
print('Now we have moved it to {}'.format(
    mouse.position))

# Move pointer relative to current position
mouse.move(5, -5)

# Press and release
mouse.press(Button.left)
mouse.release(Button.left)

# Double click; this is different from pressing and releasing
# twice on macOS
mouse.click(Button.left, 2)

# Scroll two steps down
mouse.scroll(0, 2)

def process_request(request):
    parts = request.split(",")
    if parts[0] == "MOVE":
        mouse.move(int(parts[1]), int(parts[2]))
    elif parts[0] == "PRESS":
        if parts[1] == "LEFT": mouse.press(Button.left)
        else: mouse.press(Button.right)
    elif parts[0] == "SCROLL":
        mouse.scroll(int(parts[1]), int(parts[2]))

server_socket = server_manage.start_server(address)
client_socket = server_manage.get_client(server_socket)
while True:
    request = protocol.short_recv(client_socket).decode()
    print(request)
    if request:
        process_request(request)
    
server_socket.close()
client_socket.close()