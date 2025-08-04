import keyboard_server
import screen_server
from threading import Thread

screen_thread = Thread(target=screen_server.main)
keyboard_thread = Thread(target=keyboard_server.main)

screen_thread.start()
keyboard_thread.start()