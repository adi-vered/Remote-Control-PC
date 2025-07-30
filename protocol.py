BUFFER_LENGTH = 1024
MESSAGE_HEADER_LENGTH = 6
UTF8 = "utf-8"

def split_send(sock, data):
    sock.send(str(len(data)).zfill(MESSAGE_HEADER_LENGTH).encode())
    for i in range(0, len(data), BUFFER_LENGTH):
        sock.send(data[i:i + BUFFER_LENGTH])

def split_recv(sock):
    request_length = int(sock.recv(MESSAGE_HEADER_LENGTH).decode())
    request = "".encode()
    while len(request) < request_length:
        request += sock.recv(BUFFER_LENGTH)
    return request

def short_send(sock, data):
    header = str(len(data)).zfill(MESSAGE_HEADER_LENGTH).encode()
    sock.send(header)
    sock.send(data)

def short_recv(sock):
    request_len = int(sock.recv(MESSAGE_HEADER_LENGTH).decode())
    request = sock.recv(request_len)
    return request