import keyboard_client
import screen_client
from threading import Thread

screen_thread = Thread(target=screen_client.main)
keyboard_thread = Thread(target=keyboard_client.main)

screen_thread.start()
keyboard_thread.start()
asdsdfssbdfdfssdfddfdfgvbbmrrt