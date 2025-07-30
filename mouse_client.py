import socket
import win32api
import win32con
import protocol
import time

from pynput import mouse

def on_move(x, y, injected):
    print(f'Pointer moved to {x,y}')

def on_click(x, y, button, pressed, injected):
    print(f'{'Pressed' if pressed else 'Released'} at {x, y}')

def on_scroll(x, y, dx, dy, injected):
    print(f'Scrolled {'down' if dy < 0 else 'up'} at {x, y}, dx:{dx} dy: {dy}')

# Collect events until released
with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)
listener.start()

