import socket
import protocol
import server_manage
import tkinter as tk
from PIL import Image, ImageTk
from threading import Thread
from io import BytesIO
import time

port = server_manage.SCREEN_PORT

def image_open():
    global parent
    global image_label
    global current_image  # Add this global reference
    
    # Create the main window
    parent = tk.Tk()
    parent.title("Share screen")
    # Load the image 
    current_image = tk.PhotoImage(file=img_path)

    # Create a label to display the image
    image_label = tk.Label(parent, image=current_image)
    image_label.pack()
    
    # Remove time.sleep(2) - it blocks the GUI
    open_loop()

    # Start the Tkinter event loop
    parent.mainloop()

def open_loop():
    global current_image  # Reference the global variable
    if image_recv():
        try:
            # Load the image and keep a reference
            current_image = tk.PhotoImage(file=img_path)
            # Update the label with the new image
            image_label.configure(image=current_image)
        except tk.TclError:
            # Handle case where image file doesn't exist or is corrupted
            print(f"Error loading image: {img_path}")
        
    # Schedule the next update
    parent.after(int(protocol.REST_BETWEEN_SCREENSHOTS * 1000), open_loop)

def image_recv():
    image_data = protocol.recv(my_socket)
    if not image_data:
        return False
    with open(img_path, "wb") as sent_file:
        sent_file.write(image_data)
        return True

def main():
    global img_path
    global my_socket
    img_path = "recieved.png"
    my_socket = socket.socket()
    my_socket.connect(("127.0.0.1", port))
    print("connected")
    image_open()
    my_socket.close()

if __name__ == "__main__":
    main()