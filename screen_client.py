import socket
import protocol
import server_manage
import tkinter as tk
from PIL import Image, ImageTk
from threading import Thread
from io import BytesIO

port = server_manage.SCREEN_PORT

my_socket = socket.socket()
my_socket.connect(("127.0.0.1", port))
print("connected")

root = tk.Tk()
canvas = tk.Canvas(root, height=400, width=400)
img_id = canvas.create_image(200, 200)

img_path = 'sent.jpg'
def open_image():
    with open(img_path, "rb") as file:
        stream = BytesIO(file.read())
    img = ImageTk.PhotoImage(Image.open(stream).convert("RGBA"))
    canvas.itemconfig(img_id, image=img)
    print("hi")
    root.after(100, open_image)

def tk_loop_start():
    open_image()
    root.mainloop()


def image_recv():
    while True:
        image_data = protocol.recv(my_socket)
        if not image_data:
            continue
        with open(img_path, "wb") as sent_file:
            sent_file.write(image_data)

    my_socket.close()

tk_loop_start()