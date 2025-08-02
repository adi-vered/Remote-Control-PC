BUFFER_LENGTH = 1024
MESSAGE_HEADER_LENGTH = 10
UTF8 = "utf-8"
BYTE_NUM = 4
BYTE_ORDER = "big"

def send(sock, data):
    sock.send(len(data).to_bytes(BYTE_NUM, byteorder=BYTE_ORDER, signed=False))
    sock.send(data)

def recv(sock):
    request_len = int.from_bytes(sock.recv(BYTE_NUM), byteorder=BYTE_ORDER, signed=False)
    total = b""
    while len(total) < request_len:
        part = sock.recv(BUFFER_LENGTH)
        total += part
    return total
