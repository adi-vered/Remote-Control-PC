import socket
import win32api
import win32con
import protocol
import time

from pynput import mouse

port = 8853

my_socket = socket.socket()
my_socket.connect(("127.0.0.1", port))
print("connected")

def on_move(x, y, injected):
    protocol.short_send(my_socket, f'MOVE,{x},{y}'.encode())

def on_click(x, y, button, pressed, injected):
    button_clicked = 'LEFT' if button == mouse.Button.left else 'RIGHT'
    protocol.short_send(my_socket, f'{'PRESS' if pressed else 'RELEASE'},{button_clicked}'.encode())

def on_scroll(x, y, dx, dy, injected):
    protocol.short_send(my_socket, f'SCROLL,{dx},{dy}'.encode())

# Collect events until released
with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()

my_socket.close()
